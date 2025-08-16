#!/usr/bin/env python3
"""
Script kiểm tra chất lượng toàn diện cho tài liệu CCNA
Bao gồm format, văn phong, markdown, và tính nhất quán
"""

import os
import re
import glob
from pathlib import Path
from collections import defaultdict

class ComprehensiveQualityChecker:
    def __init__(self):
        self.issues = defaultdict(list)
        self.stats = defaultdict(int)
        
        # Từ điển thuật ngữ chuẩn
        self.standard_terms = {
            'switch': 'switch',
            'router': 'router',
            'firewall': 'tường lửa',
            'ethernet': 'Ethernet',
            'internet': 'Internet',
            'tcp': 'TCP',
            'udp': 'UDP',
            'ip': 'IP',
            'ipv4': 'IPv4',
            'ipv6': 'IPv6',
            'lan': 'LAN',
            'wan': 'WAN',
            'vlan': 'VLAN',
            'dns': 'DNS',
            'dhcp': 'DHCP',
            'http': 'HTTP',
            'https': 'HTTPS',
            'ftp': 'FTP',
            'ssh': 'SSH',
            'cli': 'CLI',
            'gui': 'GUI',
            'api': 'API',
            'osi': 'OSI',
            'cisco': 'Cisco',
            'ieee': 'IEEE'
        }
        
        # Lỗi chính tả phổ biến
        self.common_typos = {
            'thiêt bị': 'thiết bị',
            'mang': 'mạng',
            'kêt nối': 'kết nối',
            'truyên': 'truyền',
            'cấu hinh': 'cấu hình',
            'giao thưc': 'giao thức',
            'định tuyen': 'định tuyến',
            'bảo mât': 'bảo mật',
            'phần mêm': 'phần mềm'
        }
        
        # Cụm từ cần cải thiện văn phong
        self.style_improvements = {
            'được sử dụng để': 'dùng để',
            'có thể được': 'có thể',
            'là một': 'là',
            'trong trường hợp': 'khi',
            'bởi vì': 'vì',
            'do đó mà': 'do đó',
            'tuy nhiên': 'nhưng',
            'mặc dù vậy': 'tuy vậy'
        }

    def check_file_structure(self, content, filename):
        """Kiểm tra cấu trúc file"""
        issues = []
        
        # Kiểm tra header chính
        if not content.startswith('# NGÀY'):
            issues.append("Thiếu header chính 'NGÀY XX:'")
        
        # Kiểm tra sections
        sections = re.findall(r'^## \d+\.\d+ (.+)', content, re.MULTILINE)
        if len(sections) < 2:
            issues.append("Quá ít sections (nên có ít nhất 2 sections)")
        
        # Kiểm tra subsections
        subsections = re.findall(r'^### \d+\.\d+\.\d+ (.+)', content, re.MULTILINE)
        
        return issues

    def check_markdown_syntax(self, content):
        """Kiểm tra markdown syntax"""
        issues = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Kiểm tra headers
            if line.startswith('#'):
                if not re.match(r'^#+\s+', line):
                    issues.append(f"Dòng {i}: Header thiếu space sau #")
            
            # Kiểm tra lists
            if re.match(r'^\s*[-*+]\s*$', line):
                issues.append(f"Dòng {i}: List item trống")
            
            # Kiểm tra bold/italic
            if '**' in line:
                if line.count('**') % 2 != 0:
                    issues.append(f"Dòng {i}: Bold text không đóng đúng")
            
            # Kiểm tra links
            if '[' in line and ']' in line:
                if not re.search(r'\[([^\]]+)\]\(([^)]+)\)', line):
                    if '[' in line and ']' in line and '(' in line and ')' in line:
                        issues.append(f"Dòng {i}: Link syntax có thể sai")
        
        return issues

    def check_spelling(self, content):
        """Kiểm tra chính tả"""
        issues = []
        
        for wrong, correct in self.common_typos.items():
            if wrong in content:
                count = content.count(wrong)
                issues.append(f"Lỗi chính tả: '{wrong}' → '{correct}' ({count} lần)")
        
        return issues

    def check_terminology(self, content):
        """Kiểm tra thuật ngữ kỹ thuật"""
        issues = []
        
        for term_lower, term_correct in self.standard_terms.items():
            # Tìm các biến thể sai
            pattern = r'\b' + re.escape(term_lower) + r'\b'
            matches = re.findall(pattern, content, re.IGNORECASE)
            
            for match in matches:
                if match != term_correct:
                    issues.append(f"Thuật ngữ: '{match}' nên là '{term_correct}'")
        
        return issues

    def check_style(self, content):
        """Kiểm tra văn phong"""
        issues = []
        
        for old_phrase, new_phrase in self.style_improvements.items():
            if old_phrase in content:
                count = content.count(old_phrase)
                issues.append(f"Văn phong: '{old_phrase}' → '{new_phrase}' ({count} lần)")
        
        # Kiểm tra câu quá dài
        sentences = re.split(r'[.!?]+', content)
        for sentence in sentences:
            if len(sentence.strip()) > 200:
                issues.append(f"Câu quá dài ({len(sentence)} ký tự): {sentence[:50]}...")
        
        return issues

    def check_consistency(self, content):
        """Kiểm tra tính nhất quán"""
        issues = []
        
        # Kiểm tra bullet points
        bullet_types = set()
        for line in content.split('\n'):
            if re.match(r'^\s*[-*+•]\s', line):
                bullet_char = re.match(r'^\s*([-*+•])', line).group(1)
                bullet_types.add(bullet_char)
        
        if len(bullet_types) > 1:
            issues.append(f"Bullet points không nhất quán: {bullet_types}")
        
        # Kiểm tra cách viết số
        numbers = re.findall(r'\d+\s*(byte|bit|Mbps|Gbps|km|m)', content)
        if numbers:
            # Kiểm tra có space giữa số và đơn vị
            for match in re.finditer(r'\d+(byte|bit|Mbps|Gbps|km|m)', content):
                issues.append(f"Thiếu space giữa số và đơn vị: {match.group()}")
        
        return issues

    def check_readability(self, content):
        """Kiểm tra khả năng đọc"""
        issues = []
        
        # Đếm từ và câu
        words = len(re.findall(r'\b\w+\b', content))
        sentences = len(re.findall(r'[.!?]+', content))
        
        if sentences > 0:
            avg_words_per_sentence = words / sentences
            if avg_words_per_sentence > 25:
                issues.append(f"Câu trung bình quá dài ({avg_words_per_sentence:.1f} từ/câu)")
        
        # Kiểm tra đoạn văn quá dài
        paragraphs = content.split('\n\n')
        for i, para in enumerate(paragraphs):
            if len(para.strip()) > 1000:
                issues.append(f"Đoạn {i+1} quá dài ({len(para)} ký tự)")
        
        return issues

    def analyze_file(self, file_path):
        """Phân tích một file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            filename = os.path.basename(file_path)
            
            # Thực hiện các kiểm tra
            structure_issues = self.check_file_structure(content, filename)
            markdown_issues = self.check_markdown_syntax(content)
            spelling_issues = self.check_spelling(content)
            terminology_issues = self.check_terminology(content)
            style_issues = self.check_style(content)
            consistency_issues = self.check_consistency(content)
            readability_issues = self.check_readability(content)
            
            # Tổng hợp kết quả
            all_issues = {
                'structure': structure_issues,
                'markdown': markdown_issues,
                'spelling': spelling_issues,
                'terminology': terminology_issues,
                'style': style_issues,
                'consistency': consistency_issues,
                'readability': readability_issues
            }
            
            # Cập nhật thống kê
            total_issues = sum(len(issues) for issues in all_issues.values())
            self.stats['total_files'] += 1
            self.stats['total_issues'] += total_issues
            
            if total_issues == 0:
                self.stats['perfect_files'] += 1
            
            return {
                'file': filename,
                'issues': all_issues,
                'total_issues': total_issues,
                'word_count': len(re.findall(r'\b\w+\b', content)),
                'line_count': len(content.split('\n'))
            }
            
        except Exception as e:
            return {
                'file': os.path.basename(file_path),
                'error': str(e),
                'total_issues': 0
            }

    def generate_report(self, results):
        """Tạo báo cáo chi tiết"""
        report = []
        report.append("# BÁO CÁO KIỂM TRA CHẤT LƯỢNG TOÀN DIỆN\n")
        report.append(f"**Ngày kiểm tra**: {os.popen('date').read().strip()}\n")
        
        # Thống kê tổng quan
        report.append("## 📊 Thống kê tổng quan\n")
        report.append(f"- **Tổng số file**: {self.stats['total_files']}")
        report.append(f"- **File hoàn hảo**: {self.stats['perfect_files']}")
        report.append(f"- **Tổng vấn đề**: {self.stats['total_issues']}")
        report.append(f"- **Tỷ lệ hoàn hảo**: {self.stats['perfect_files']/self.stats['total_files']*100:.1f}%\n")
        
        # Phân loại vấn đề
        issue_categories = defaultdict(int)
        for result in results:
            if 'issues' in result:
                for category, issues in result['issues'].items():
                    issue_categories[category] += len(issues)
        
        report.append("## 🔍 Phân loại vấn đề\n")
        for category, count in sorted(issue_categories.items(), key=lambda x: x[1], reverse=True):
            report.append(f"- **{category.title()}**: {count} vấn đề")
        report.append("")
        
        # Top file có nhiều vấn đề nhất
        problematic_files = [r for r in results if r.get('total_issues', 0) > 0]
        problematic_files.sort(key=lambda x: x.get('total_issues', 0), reverse=True)
        
        if problematic_files:
            report.append("## ⚠️ File cần chú ý nhất\n")
            for result in problematic_files[:10]:
                report.append(f"- **{result['file']}**: {result['total_issues']} vấn đề")
            report.append("")
        
        # File hoàn hảo
        perfect_files = [r for r in results if r.get('total_issues', 0) == 0]
        if perfect_files:
            report.append("## ✅ File hoàn hảo\n")
            for result in perfect_files[:10]:
                report.append(f"- {result['file']}")
            if len(perfect_files) > 10:
                report.append(f"- ... và {len(perfect_files) - 10} file khác")
            report.append("")
        
        # Chi tiết từng file
        report.append("## 📋 Chi tiết từng file\n")
        for result in results:
            report.append(f"### {result['file']}\n")
            
            if result.get('error'):
                report.append(f"❌ **Lỗi**: {result['error']}\n")
                continue
            
            if result.get('total_issues', 0) == 0:
                report.append("✅ **Hoàn hảo** - Không có vấn đề\n")
                continue
            
            report.append(f"**Tổng vấn đề**: {result['total_issues']}")
            report.append(f"**Số từ**: {result.get('word_count', 0)}")
            report.append(f"**Số dòng**: {result.get('line_count', 0)}\n")
            
            for category, issues in result.get('issues', {}).items():
                if issues:
                    report.append(f"**{category.title()}**:")
                    for issue in issues[:5]:  # Chỉ hiển thị 5 vấn đề đầu
                        report.append(f"- {issue}")
                    if len(issues) > 5:
                        report.append(f"- ... và {len(issues) - 5} vấn đề khác")
                    report.append("")
        
        return '\n'.join(report)

def main():
    checker = ComprehensiveQualityChecker()
    base_dir = "/home/ubuntu/NEO/Networking fundamentals"
    pattern = os.path.join(base_dir, "Day*.md")
    files = glob.glob(pattern)
    
    print("🔍 KIỂM TRA CHẤT LƯỢNG TOÀN DIỆN")
    print("=" * 50)
    
    results = []
    
    for file_path in sorted(files):
        result = checker.analyze_file(file_path)
        results.append(result)
        
        filename = result['file']
        total_issues = result.get('total_issues', 0)
        
        if result.get('error'):
            print(f"❌ {filename}: Lỗi - {result['error']}")
        elif total_issues == 0:
            print(f"✅ {filename}: Hoàn hảo")
        else:
            print(f"⚠️  {filename}: {total_issues} vấn đề")
    
    # Tạo báo cáo
    report_content = checker.generate_report(results)
    report_path = os.path.join(base_dir, "COMPREHENSIVE_QUALITY_REPORT.md")
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print("\n" + "=" * 50)
    print("📊 TỔNG KẾT:")
    print(f"✅ Đã kiểm tra: {checker.stats['total_files']} file")
    print(f"🏆 File hoàn hảo: {checker.stats['perfect_files']} file")
    print(f"⚠️  Tổng vấn đề: {checker.stats['total_issues']}")
    print(f"📈 Tỷ lệ hoàn hảo: {checker.stats['perfect_files']/checker.stats['total_files']*100:.1f}%")
    print(f"📋 Báo cáo chi tiết: COMPREHENSIVE_QUALITY_REPORT.md")

if __name__ == "__main__":
    main()
