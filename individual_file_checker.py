#!/usr/bin/env python3
"""
Script kiểm tra từng file một cách chi tiết
Phân tích sâu từng file để đảm bảo chất lượng cao nhất
"""

import os
import re
import glob
from pathlib import Path

class IndividualFileChecker:
    def __init__(self):
        self.detailed_results = []
        
    def check_file_structure(self, content, filename):
        """Kiểm tra cấu trúc file chi tiết"""
        issues = []
        
        lines = content.split('\n')
        
        # Kiểm tra header chính
        if not lines[0].startswith('# NGÀY'):
            issues.append("❌ Thiếu header chính 'NGÀY XX:'")
        else:
            # Kiểm tra format header
            header_match = re.match(r'# NGÀY (\d+): (.+)', lines[0])
            if not header_match:
                issues.append("❌ Format header không đúng")
            else:
                day_num = header_match.group(1)
                title = header_match.group(2)
                expected_day = filename.split('_')[0].replace('Day', '').zfill(2)
                if day_num != expected_day:
                    issues.append(f"❌ Số ngày không khớp: header có {day_num}, filename có {expected_day}")
        
        # Kiểm tra sections
        sections = []
        subsections = []
        
        for i, line in enumerate(lines):
            if line.startswith('## '):
                sections.append((i+1, line))
            elif line.startswith('### '):
                subsections.append((i+1, line))
        
        if len(sections) < 2:
            issues.append("⚠️ Ít sections (nên có ít nhất 2 sections)")
        
        # Kiểm tra format sections
        for line_num, section in sections:
            if not re.match(r'## \d+\.\d+ .+', section):
                issues.append(f"❌ Dòng {line_num}: Section format sai '{section[:50]}...'")
        
        # Kiểm tra format subsections
        for line_num, subsection in subsections:
            if not re.match(r'### \d+\.\d+\.\d+ .+', subsection):
                issues.append(f"❌ Dòng {line_num}: Subsection format sai '{subsection[:50]}...'")
        
        return issues
    
    def check_content_quality(self, content):
        """Kiểm tra chất lượng nội dung"""
        issues = []
        
        # Kiểm tra độ dài nội dung
        word_count = len(re.findall(r'\b\w+\b', content))
        if word_count < 200:
            issues.append(f"⚠️ Nội dung quá ngắn ({word_count} từ)")
        elif word_count > 5000:
            issues.append(f"⚠️ Nội dung quá dài ({word_count} từ)")
        
        # Kiểm tra câu quá dài
        sentences = re.split(r'[.!?]+', content)
        long_sentences = [s for s in sentences if len(s.strip()) > 200]
        if long_sentences:
            issues.append(f"⚠️ {len(long_sentences)} câu quá dài (>200 ký tự)")
        
        # Kiểm tra đoạn văn quá dài
        paragraphs = content.split('\n\n')
        long_paragraphs = [p for p in paragraphs if len(p.strip()) > 1000]
        if long_paragraphs:
            issues.append(f"⚠️ {len(long_paragraphs)} đoạn văn quá dài (>1000 ký tự)")
        
        return issues
    
    def check_markdown_syntax(self, content):
        """Kiểm tra markdown syntax chi tiết"""
        issues = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Kiểm tra headers
            if line.startswith('#'):
                if not re.match(r'^#+\s+', line):
                    issues.append(f"❌ Dòng {i}: Header thiếu space sau #")
                
                # Kiểm tra level headers hợp lý
                level = len(line) - len(line.lstrip('#'))
                if level > 6:
                    issues.append(f"❌ Dòng {i}: Header level quá sâu ({level})")
            
            # Kiểm tra lists
            if re.match(r'^\s*[-*+]\s*$', line):
                issues.append(f"❌ Dòng {i}: List item trống")
            
            # Kiểm tra bold/italic
            bold_count = line.count('**')
            if bold_count % 2 != 0:
                issues.append(f"❌ Dòng {i}: Bold text không đóng đúng")
            
            italic_count = line.count('*') - bold_count
            if italic_count % 2 != 0:
                issues.append(f"❌ Dòng {i}: Italic text không đóng đúng")
            
            # Kiểm tra code blocks
            if line.strip() == '```':
                # Tìm code block đóng
                found_close = False
                for j in range(i, len(lines)):
                    if lines[j].strip() == '```':
                        found_close = True
                        break
                if not found_close:
                    issues.append(f"❌ Dòng {i}: Code block không đóng")
            
            # Kiểm tra links
            if '[' in line and ']' in line and '(' in line and ')' in line:
                # Kiểm tra format link
                if not re.search(r'\[([^\]]+)\]\(([^)]+)\)', line):
                    issues.append(f"❌ Dòng {i}: Link format có thể sai")
            
            # Kiểm tra images
            if line.strip().startswith('!['):
                if not re.match(r'!\[([^\]]*)\]\(([^)]+)\)', line.strip()):
                    issues.append(f"❌ Dòng {i}: Image format sai")
        
        return issues
    
    def check_tables(self, content):
        """Kiểm tra bảng chi tiết"""
        issues = []
        lines = content.split('\n')
        
        in_table = False
        table_start = 0
        table_lines = []
        
        for i, line in enumerate(lines):
            if '|' in line and not line.strip().startswith('```'):
                if not in_table:
                    in_table = True
                    table_start = i + 1
                    table_lines = []
                table_lines.append(line)
            else:
                if in_table and table_lines:
                    # Kiểm tra bảng vừa kết thúc
                    table_issues = self.validate_table(table_lines, table_start)
                    issues.extend(table_issues)
                    table_lines = []
                in_table = False
        
        # Kiểm tra bảng cuối file
        if table_lines:
            table_issues = self.validate_table(table_lines, table_start)
            issues.extend(table_issues)
        
        return issues
    
    def validate_table(self, table_lines, start_line):
        """Validate một bảng cụ thể"""
        issues = []
        
        if len(table_lines) < 2:
            issues.append(f"❌ Dòng {start_line}: Bảng cần ít nhất 2 dòng")
            return issues
        
        # Kiểm tra header
        header_cells = len([cell for cell in table_lines[0].split('|') if cell.strip()])
        
        # Kiểm tra separator
        if len(table_lines) > 1:
            separator_cells = len([cell for cell in table_lines[1].split('|') if cell.strip()])
            if header_cells != separator_cells:
                issues.append(f"❌ Dòng {start_line+1}: Separator không khớp với header")
        
        # Kiểm tra data rows
        for i, line in enumerate(table_lines[2:], 2):
            data_cells = len([cell for cell in line.split('|') if cell.strip()])
            if data_cells != header_cells:
                issues.append(f"❌ Dòng {start_line+i}: Số cột không khớp ({data_cells} vs {header_cells})")
        
        return issues
    
    def check_terminology(self, content):
        """Kiểm tra thuật ngữ kỹ thuật"""
        issues = []
        
        # Thuật ngữ cần viết hoa
        terms_to_check = {
            'tcp': 'TCP',
            'udp': 'UDP', 
            'ip': 'IP',
            'http': 'HTTP',
            'https': 'HTTPS',
            'ftp': 'FTP',
            'ssh': 'SSH',
            'dns': 'DNS',
            'dhcp': 'DHCP',
            'lan': 'LAN',
            'wan': 'WAN',
            'vlan': 'VLAN',
            'osi': 'OSI',
            'cisco': 'Cisco',
            'ieee': 'IEEE'
        }
        
        for wrong, correct in terms_to_check.items():
            # Tìm các trường hợp viết sai
            pattern = r'\b' + re.escape(wrong) + r'\b'
            matches = re.findall(pattern, content, re.IGNORECASE)
            
            wrong_cases = [m for m in matches if m != correct]
            if wrong_cases:
                issues.append(f"⚠️ Thuật ngữ '{wrong}' nên viết '{correct}' ({len(wrong_cases)} lần)")
        
        return issues
    
    def check_spelling(self, content):
        """Kiểm tra chính tả"""
        issues = []
        
        common_typos = {
            'thiêt bị': 'thiết bị',
            'kêt nối': 'kết nối',
            'truyên': 'truyền',
            'cấu hinh': 'cấu hình',
            'giao thưc': 'giao thức',
            'định tuyen': 'định tuyến',
            'bảo mât': 'bảo mật'
        }
        
        for wrong, correct in common_typos.items():
            if wrong in content:
                count = content.count(wrong)
                issues.append(f"❌ Lỗi chính tả: '{wrong}' → '{correct}' ({count} lần)")
        
        return issues
    
    def analyze_file(self, file_path):
        """Phân tích chi tiết một file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            filename = os.path.basename(file_path)
            
            # Thực hiện các kiểm tra
            structure_issues = self.check_file_structure(content, filename)
            content_issues = self.check_content_quality(content)
            markdown_issues = self.check_markdown_syntax(content)
            table_issues = self.check_tables(content)
            terminology_issues = self.check_terminology(content)
            spelling_issues = self.check_spelling(content)
            
            # Tính toán metrics
            word_count = len(re.findall(r'\b\w+\b', content))
            line_count = len(content.split('\n'))
            char_count = len(content)
            
            # Tổng hợp kết quả
            all_issues = (structure_issues + content_issues + markdown_issues + 
                         table_issues + terminology_issues + spelling_issues)
            
            # Tính điểm chất lượng
            total_issues = len(all_issues)
            critical_issues = len([i for i in all_issues if i.startswith('❌')])
            warning_issues = len([i for i in all_issues if i.startswith('⚠️')])
            
            # Công thức tính điểm: 100 - (critical*2 + warning*1)
            quality_score = max(0, 100 - (critical_issues * 2 + warning_issues * 1))
            
            return {
                'file': filename,
                'quality_score': quality_score,
                'total_issues': total_issues,
                'critical_issues': critical_issues,
                'warning_issues': warning_issues,
                'word_count': word_count,
                'line_count': line_count,
                'char_count': char_count,
                'issues': {
                    'structure': structure_issues,
                    'content': content_issues,
                    'markdown': markdown_issues,
                    'tables': table_issues,
                    'terminology': terminology_issues,
                    'spelling': spelling_issues
                }
            }
            
        except Exception as e:
            return {
                'file': os.path.basename(file_path),
                'error': str(e),
                'quality_score': 0
            }

def main():
    checker = IndividualFileChecker()
    base_dir = "/home/ubuntu/NEO/Networking fundamentals"
    pattern = os.path.join(base_dir, "Day*.md")
    files = glob.glob(pattern)
    
    print("🔍 KIỂM TRA TỪNG FILE CHI TIẾT")
    print("=" * 50)
    
    results = []
    total_score = 0
    
    for file_path in sorted(files):
        result = checker.analyze_file(file_path)
        results.append(result)
        
        filename = result['file']
        
        if result.get('error'):
            print(f"❌ {filename}: Lỗi - {result['error']}")
        else:
            score = result['quality_score']
            total_issues = result['total_issues']
            critical = result['critical_issues']
            warning = result['warning_issues']
            
            total_score += score
            
            # Hiển thị kết quả với màu sắc
            if score >= 90:
                status = "🟢 XUẤT SẮC"
            elif score >= 80:
                status = "🟡 TỐT"
            elif score >= 70:
                status = "🟠 TRUNG BÌNH"
            else:
                status = "🔴 CẦN CẢI THIỆN"
            
            print(f"{status} {filename}: {score}/100 điểm ({critical} critical, {warning} warning)")
    
    # Tạo báo cáo chi tiết
    avg_score = total_score / len(results) if results else 0
    
    report_path = os.path.join(base_dir, "INDIVIDUAL_FILE_REPORT.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# BÁO CÁO KIỂM TRA TỪNG FILE CHI TIẾT\n\n")
        f.write(f"**Ngày kiểm tra**: {os.popen('date').read().strip()}\n\n")
        
        f.write("## 📊 Tổng kết\n\n")
        f.write(f"- **Tổng số file**: {len(results)}\n")
        f.write(f"- **Điểm trung bình**: {avg_score:.1f}/100\n")
        
        # Phân loại theo điểm
        excellent = len([r for r in results if r.get('quality_score', 0) >= 90])
        good = len([r for r in results if 80 <= r.get('quality_score', 0) < 90])
        average = len([r for r in results if 70 <= r.get('quality_score', 0) < 80])
        poor = len([r for r in results if r.get('quality_score', 0) < 70])
        
        f.write(f"- **Xuất sắc (90-100)**: {excellent} file\n")
        f.write(f"- **Tốt (80-89)**: {good} file\n")
        f.write(f"- **Trung bình (70-79)**: {average} file\n")
        f.write(f"- **Cần cải thiện (<70)**: {poor} file\n\n")
        
        # Top file tốt nhất
        best_files = sorted([r for r in results if not r.get('error')], 
                           key=lambda x: x['quality_score'], reverse=True)[:10]
        
        f.write("## 🏆 Top 10 file chất lượng cao nhất\n\n")
        for i, result in enumerate(best_files, 1):
            f.write(f"{i}. **{result['file']}**: {result['quality_score']}/100 điểm\n")
        f.write("\n")
        
        # Top file cần cải thiện
        worst_files = sorted([r for r in results if not r.get('error')], 
                            key=lambda x: x['quality_score'])[:10]
        
        f.write("## ⚠️ Top 10 file cần cải thiện\n\n")
        for i, result in enumerate(worst_files, 1):
            f.write(f"{i}. **{result['file']}**: {result['quality_score']}/100 điểm\n")
        f.write("\n")
        
        # Chi tiết từng file
        f.write("## 📋 Chi tiết từng file\n\n")
        for result in sorted(results, key=lambda x: x.get('quality_score', 0), reverse=True):
            f.write(f"### {result['file']}\n\n")
            
            if result.get('error'):
                f.write(f"❌ **Lỗi**: {result['error']}\n\n")
                continue
            
            score = result['quality_score']
            f.write(f"**Điểm chất lượng**: {score}/100\n")
            f.write(f"**Số từ**: {result['word_count']}\n")
            f.write(f"**Số dòng**: {result['line_count']}\n")
            f.write(f"**Tổng vấn đề**: {result['total_issues']} ({result['critical_issues']} critical, {result['warning_issues']} warning)\n\n")
            
            # Hiển thị vấn đề theo loại
            for category, issues in result['issues'].items():
                if issues:
                    f.write(f"**{category.title()}**:\n")
                    for issue in issues[:5]:  # Chỉ hiển thị 5 vấn đề đầu
                        f.write(f"- {issue}\n")
                    if len(issues) > 5:
                        f.write(f"- ... và {len(issues) - 5} vấn đề khác\n")
                    f.write("\n")
    
    print("\n" + "=" * 50)
    print("📊 TỔNG KẾT KIỂM TRA TỪNG FILE:")
    print(f"✅ Đã kiểm tra: {len(results)} file")
    print(f"📈 Điểm trung bình: {avg_score:.1f}/100")
    print(f"🟢 Xuất sắc: {excellent} file")
    print(f"🟡 Tốt: {good} file") 
    print(f"🟠 Trung bình: {average} file")
    print(f"🔴 Cần cải thiện: {poor} file")
    print(f"📋 Báo cáo chi tiết: INDIVIDUAL_FILE_REPORT.md")

if __name__ == "__main__":
    main()
