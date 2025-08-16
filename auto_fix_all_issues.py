#!/usr/bin/env python3
"""
Script tự động sửa tất cả vấn đề về format và văn phong
"""

import os
import re
import glob
from pathlib import Path

class AutoFixer:
    def __init__(self):
        self.fixes_applied = []
        
        # Từ điển thuật ngữ chuẩn (case-sensitive)
        self.terminology_fixes = {
            'Firewall': 'tường lửa',
            'firewall': 'tường lửa',
            'FIREWALL': 'tường lửa',
            'Switch': 'switch',
            'SWITCH': 'switch',
            'Router': 'router',
            'ROUTER': 'router',
            'Ethernet': 'Ethernet',
            'ethernet': 'Ethernet',
            'ETHERNET': 'Ethernet',
            'Internet': 'Internet',
            'internet': 'Internet',
            'INTERNET': 'Internet',
            'Tcp': 'TCP',
            'tcp': 'TCP',
            'Udp': 'UDP',
            'udp': 'UDP',
            'Ip': 'IP',
            'ip': 'IP',
            'Ipv4': 'IPv4',
            'ipv4': 'IPv4',
            'IPV4': 'IPv4',
            'Ipv6': 'IPv6',
            'ipv6': 'IPv6',
            'IPV6': 'IPv6',
            'Lan': 'LAN',
            'lan': 'LAN',
            'Wan': 'WAN',
            'wan': 'WAN',
            'Vlan': 'VLAN',
            'vlan': 'VLAN',
            'Dns': 'DNS',
            'dns': 'DNS',
            'Dhcp': 'DHCP',
            'dhcp': 'DHCP',
            'Http': 'HTTP',
            'http': 'HTTP',
            'Https': 'HTTPS',
            'https': 'HTTPS',
            'Ftp': 'FTP',
            'ftp': 'FTP',
            'Ssh': 'SSH',
            'ssh': 'SSH',
            'Cli': 'CLI',
            'cli': 'CLI',
            'Gui': 'GUI',
            'gui': 'GUI',
            'Api': 'API',
            'api': 'API',
            'Osi': 'OSI',
            'osi': 'OSI',
            'Cisco': 'Cisco',
            'cisco': 'Cisco',
            'CISCO': 'Cisco',
            'Ieee': 'IEEE',
            'ieee': 'IEEE'
        }
        
        # Lỗi chính tả
        self.spelling_fixes = {
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
        
        # Cải thiện văn phong
        self.style_fixes = {
            'được sử dụng để': 'dùng để',
            'có thể được': 'có thể',
            'là một': 'là',
            'trong trường hợp': 'khi',
            'bởi vì': 'vì',
            'do đó mà': 'do đó',
            'tuy nhiên': 'nhưng',
            'mặc dù vậy': 'tuy vậy',
            'ngoài ra': 'bên cạnh đó',
            'có khả năng': 'có thể',
            'thực hiện việc': 'thực hiện',
            'tiến hành': 'thực hiện',
            'đảm bảo rằng': 'đảm bảo',
            'chắc chắn rằng': 'đảm bảo'
        }

    def fix_terminology(self, content):
        """Sửa thuật ngữ kỹ thuật"""
        original_content = content
        
        for wrong_term, correct_term in self.terminology_fixes.items():
            # Sử dụng word boundary để tránh thay thế nhầm
            pattern = r'\b' + re.escape(wrong_term) + r'\b'
            if re.search(pattern, content):
                content = re.sub(pattern, correct_term, content)
                count = len(re.findall(pattern, original_content))
                self.fixes_applied.append(f"Thuật ngữ: '{wrong_term}' → '{correct_term}' ({count} lần)")
        
        return content

    def fix_spelling(self, content):
        """Sửa lỗi chính tả"""
        for wrong, correct in self.spelling_fixes.items():
            if wrong in content:
                count = content.count(wrong)
                content = content.replace(wrong, correct)
                self.fixes_applied.append(f"Chính tả: '{wrong}' → '{correct}' ({count} lần)")
        
        return content

    def fix_style(self, content):
        """Cải thiện văn phong"""
        for old_phrase, new_phrase in self.style_fixes.items():
            if old_phrase in content:
                count = content.count(old_phrase)
                content = content.replace(old_phrase, new_phrase)
                self.fixes_applied.append(f"Văn phong: '{old_phrase}' → '{new_phrase}' ({count} lần)")
        
        return content

    def fix_structure(self, content, filename):
        """Sửa cấu trúc file"""
        lines = content.split('\n')
        fixed_lines = []
        
        # Lấy thông tin ngày từ filename
        day_match = re.match(r'Day(\d+)_(.+)\.md', filename)
        if not day_match:
            return content
        
        day_num = day_match.group(1).zfill(2)
        title_raw = day_match.group(2).replace('_', ' ')
        title = title_raw.upper()
        
        # Đảm bảo header chính đúng format
        if not content.startswith(f'# NGÀY {day_num}:'):
            self.fixes_applied.append("Sửa header chính")
        
        section_counter = 1
        subsection_counter = 1
        
        for line in lines:
            # Sửa headers
            if line.startswith('# NGÀY'):
                fixed_lines.append(f"# NGÀY {day_num}: {title}")
            elif line.startswith('## '):
                # Main section
                header_content = re.sub(r'^##\s*\d*\.?\d*\s*', '', line).strip()
                if header_content:
                    fixed_lines.append(f"## {day_num}.{section_counter} {header_content}")
                    section_counter += 1
                    subsection_counter = 1
            elif line.startswith('### '):
                # Subsection
                header_content = re.sub(r'^###\s*\d*\.?\d*\.?\d*\s*', '', line).strip()
                if header_content:
                    fixed_lines.append(f"### {day_num}.{section_counter-1}.{subsection_counter} {header_content}")
                    subsection_counter += 1
            else:
                fixed_lines.append(line)
        
        return '\n'.join(fixed_lines)

    def fix_markdown(self, content):
        """Sửa markdown syntax"""
        # Sửa headers thiếu space
        content = re.sub(r'^(#+)([^#\s])', r'\1 \2', content, flags=re.MULTILINE)
        
        # Sửa bold text
        content = re.sub(r'\*\*([^*]+?)\s*:\s*\*\*', r'**\1:**', content)
        
        # Sửa bullet points
        content = re.sub(r'^\s*[•*+]\s*', '- ', content, flags=re.MULTILINE)
        
        # Sửa links
        content = content.replace('HTTPS://', 'https://')
        
        return content

    def fix_consistency(self, content):
        """Sửa tính nhất quán"""
        # Chuẩn hóa spacing giữa số và đơn vị
        content = re.sub(r'(\d+)(byte|bit|Mbps|Gbps|km|m|ms|s)\b', r'\1 \2', content)
        
        # Chuẩn hóa dấu câu
        content = re.sub(r'\s+([,.;:!?])', r'\1', content)
        content = re.sub(r'([,.;:!?])\s*', r'\1 ', content)
        
        return content

    def fix_readability(self, content):
        """Cải thiện khả năng đọc"""
        # Chia câu quá dài
        sentences = re.split(r'([.!?]+)', content)
        fixed_sentences = []
        
        for sentence in sentences:
            if len(sentence.strip()) > 200 and '.' not in sentence[-10:]:
                # Tìm chỗ phù hợp để chia câu
                if ', ' in sentence:
                    parts = sentence.split(', ')
                    mid = len(parts) // 2
                    sentence = ', '.join(parts[:mid]) + '. ' + ', '.join(parts[mid:])
                    self.fixes_applied.append("Chia câu quá dài")
            
            fixed_sentences.append(sentence)
        
        return ''.join(fixed_sentences)

    def fix_spacing(self, content):
        """Sửa spacing"""
        lines = content.split('\n')
        fixed_lines = []
        prev_empty = False
        
        for line in lines:
            # Loại bỏ trailing spaces
            line = line.rstrip()
            
            # Kiểm soát empty lines
            if line.strip() == '':
                if not prev_empty:
                    fixed_lines.append('')
                prev_empty = True
            else:
                fixed_lines.append(line)
                prev_empty = False
        
        # Loại bỏ empty lines ở cuối
        while fixed_lines and fixed_lines[-1] == '':
            fixed_lines.pop()
        
        return '\n'.join(fixed_lines)

    def fix_file(self, file_path):
        """Sửa một file hoàn toàn"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            self.fixes_applied = []
            filename = os.path.basename(file_path)
            
            # Áp dụng tất cả các fixes
            content = self.fix_spelling(content)
            content = self.fix_terminology(content)
            content = self.fix_style(content)
            content = self.fix_structure(content, filename)
            content = self.fix_markdown(content)
            content = self.fix_consistency(content)
            content = self.fix_readability(content)
            content = self.fix_spacing(content)
            
            # Lưu file nếu có thay đổi
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                return {
                    'file': filename,
                    'fixes': self.fixes_applied,
                    'changed': True
                }
            else:
                return {
                    'file': filename,
                    'fixes': [],
                    'changed': False
                }
                
        except Exception as e:
            return {
                'file': os.path.basename(file_path),
                'error': str(e),
                'changed': False
            }

def main():
    fixer = AutoFixer()
    base_dir = "/home/ubuntu/NEO/Networking fundamentals"
    pattern = os.path.join(base_dir, "Day*.md")
    files = glob.glob(pattern)
    
    print("🔧 TỰ ĐỘNG SỬA TẤT CẢ VẤN ĐỀ")
    print("=" * 40)
    
    total_files = len(files)
    files_fixed = 0
    total_fixes = 0
    
    results = []
    
    for file_path in sorted(files):
        result = fixer.fix_file(file_path)
        results.append(result)
        
        if result.get('changed'):
            files_fixed += 1
            fix_count = len(result.get('fixes', []))
            total_fixes += fix_count
            print(f"🔧 {result['file']}: {fix_count} lỗi đã sửa")
        elif result.get('error'):
            print(f"❌ {result['file']}: Lỗi - {result['error']}")
        else:
            print(f"✅ {result['file']}: Không cần sửa")
    
    # Tạo báo cáo
    report_path = os.path.join(base_dir, "AUTO_FIX_REPORT.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# BÁO CÁO TỰ ĐỘNG SỬA LỖI\n\n")
        f.write(f"**Ngày sửa**: {os.popen('date').read().strip()}\n\n")
        f.write("## Tổng kết\n\n")
        f.write(f"- **Tổng số file**: {total_files}\n")
        f.write(f"- **File đã sửa**: {files_fixed}\n")
        f.write(f"- **Tổng lỗi đã sửa**: {total_fixes}\n\n")
        
        f.write("## Chi tiết từng file\n\n")
        for result in results:
            f.write(f"### {result['file']}\n\n")
            
            if result.get('error'):
                f.write(f"❌ **Lỗi**: {result['error']}\n\n")
                continue
            
            if result.get('fixes'):
                f.write("**Lỗi đã sửa:**\n")
                for fix in result['fixes']:
                    f.write(f"- {fix}\n")
                f.write("\n")
            else:
                f.write("✅ Không cần sửa\n\n")
    
    print("\n" + "=" * 40)
    print("📊 TỔNG KẾT TỰ ĐỘNG SỬA LỖI:")
    print(f"✅ Đã kiểm tra: {total_files} file")
    print(f"🔧 Đã sửa: {files_fixed} file")
    print(f"🛠️  Tổng lỗi đã sửa: {total_fixes}")
    print(f"📋 Báo cáo chi tiết: AUTO_FIX_REPORT.md")

if __name__ == "__main__":
    main()
