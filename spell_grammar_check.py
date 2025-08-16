#!/usr/bin/env python3
"""
Script kiểm tra chính tả và văn phong cho tài liệu CCNA
Sửa các lỗi phổ biến và cải thiện văn phong tiếng Việt
"""

import os
import re
import glob
from pathlib import Path

class VietnameseSpellChecker:
    def __init__(self):
        # Từ điển sửa lỗi chính tả phổ biến
        self.spelling_corrections = {
            # Lỗi chính tả thường gặp
            "thiêt bị": "thiết bị",
            "mang": "mạng",
            "kêt nối": "kết nối",
            "truyên": "truyền",
            "nhận": "nhận",
            "cấu hinh": "cấu hình",
            "giao thưc": "giao thức",
            "định tuyen": "định tuyến",
            "bảo mât": "bảo mật",
            "phần mêm": "phần mềm",
            "phần cứng": "phần cứng",
            
            # Thuật ngữ kỹ thuật chuẩn hóa
            "switch": "switch",
            "router": "router",
            "hub": "hub",
            "firewall": "tường lửa",
            "ethernet": "Ethernet",
            "internet": "Internet",
            
            # Viết hoa đúng
            "tcp/ip": "TCP/IP",
            "osi": "OSI",
            "lan": "LAN",
            "wan": "WAN",
            "vlan": "VLAN",
            "ip": "IP",
            "dns": "DNS",
            "dhcp": "DHCP",
            "http": "HTTP",
            "https": "HTTPS",
            "ftp": "FTP",
            "ssh": "SSH",
            "snmp": "SNMP",
            
            # Sửa lỗi dấu câu và khoảng trắng
            " ,": ",",
            " .": ".",
            " :": ":",
            " ;": ";",
            "( ": "(",
            " )": ")",
            "[ ": "[",
            " ]": "]",
            
            # Cải thiện văn phong
            "là một": "là",
            "có thể được": "có thể",
            "được sử dụng để": "dùng để",
            "trong trường hợp": "khi",
            "bởi vì": "vì",
            "do đó": "vậy nên",
            "tuy nhiên": "nhưng",
            "mặc dù": "dù",
        }
        
        # Quy tắc văn phong
        self.style_rules = {
            # Chuẩn hóa cách viết số
            r'\b(\d+)\s+(byte|bit|Mbps|Gbps|km|m|ms|s)\b': r'\1 \2',
            
            # Chuẩn hóa dấu gạch ngang
            r'\s*-\s*': ' - ',
            
            # Chuẩn hóa dấu hai chấm
            r'\s*:\s*': ': ',
            
            # Loại bỏ khoảng trắng thừa
            r'\s+': ' ',
            r'^\s+|\s+$': '',
            
            # Chuẩn hóa bullet points
            r'^•\s*': '- ',
            r'^-\s+': '- ',
        }
        
        # Từ khóa cần viết hoa
        self.capitalize_terms = [
            'Cisco', 'IEEE', 'ISO', 'IETF', 'RFC', 'TCP', 'UDP', 'IP', 'IPv4', 'IPv6',
            'HTTP', 'HTTPS', 'FTP', 'TFTP', 'SSH', 'Telnet', 'SNMP', 'DHCP', 'DNS',
            'VLAN', 'STP', 'RSTP', 'OSPF', 'EIGRP', 'RIP', 'BGP', 'NAT', 'PAT',
            'ACL', 'QoS', 'VPN', 'MPLS', 'HSRP', 'VRRP', 'GLBP', 'EtherChannel',
            'PoE', 'CDP', 'LLDP', 'NTP', 'SYSLOG', 'AAA', 'RADIUS', 'TACACS',
            'WPA', 'WEP', 'WPA2', 'WPA3', 'SSID', 'BSSID', 'ESS', 'BSS'
        ]

    def check_spelling(self, text):
        """Kiểm tra và sửa lỗi chính tả"""
        corrected_text = text
        corrections_made = []
        
        for wrong, correct in self.spelling_corrections.items():
            if wrong in corrected_text:
                corrected_text = corrected_text.replace(wrong, correct)
                corrections_made.append(f"{wrong} → {correct}")
        
        return corrected_text, corrections_made

    def improve_style(self, text):
        """Cải thiện văn phong"""
        improved_text = text
        
        # Áp dụng các quy tắc văn phong
        for pattern, replacement in self.style_rules.items():
            improved_text = re.sub(pattern, replacement, improved_text, flags=re.MULTILINE)
        
        # Viết hoa các thuật ngữ kỹ thuật
        for term in self.capitalize_terms:
            pattern = r'\b' + re.escape(term.lower()) + r'\b'
            improved_text = re.sub(pattern, term, improved_text, flags=re.IGNORECASE)
        
        return improved_text

    def check_grammar(self, text):
        """Kiểm tra ngữ pháp cơ bản"""
        grammar_issues = []
        
        # Kiểm tra dấu câu
        lines = text.split('\n')
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('```'):
                # Kiểm tra câu kết thúc bằng dấu câu
                if line and line[-1] not in '.!?:' and not line.endswith('```') and '|' not in line:
                    if len(line) > 10:  # Chỉ kiểm tra câu dài
                        grammar_issues.append(f"Dòng {i}: Thiếu dấu câu kết thúc")
                
                # Kiểm tra viết hoa đầu câu
                if line and line[0].islower() and not line.startswith('-') and not line.startswith('*'):
                    grammar_issues.append(f"Dòng {i}: Nên viết hoa chữ cái đầu")
        
        return grammar_issues

    def process_file(self, file_path):
        """Xử lý một file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Kiểm tra chính tả
            content, spelling_corrections = self.check_spelling(content)
            
            # Cải thiện văn phong
            content = self.improve_style(content)
            
            # Kiểm tra ngữ pháp
            grammar_issues = self.check_grammar(content)
            
            # Lưu file nếu có thay đổi
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            return {
                'file': os.path.basename(file_path),
                'spelling_corrections': spelling_corrections,
                'grammar_issues': grammar_issues,
                'changed': content != original_content
            }
            
        except Exception as e:
            return {
                'file': os.path.basename(file_path),
                'error': str(e),
                'changed': False
            }

def main():
    checker = VietnameseSpellChecker()
    base_dir = "/home/ubuntu/NEO/Networking fundamentals"
    pattern = os.path.join(base_dir, "Day*.md")
    files = glob.glob(pattern)
    
    print("🔍 KIỂM TRA CHÍNH TẢ VÀ VĂN PHONG")
    print("=" * 50)
    
    total_files = len(files)
    files_changed = 0
    total_corrections = 0
    total_grammar_issues = 0
    
    results = []
    
    for file_path in sorted(files):
        result = checker.process_file(file_path)
        results.append(result)
        
        if result.get('changed'):
            files_changed += 1
        
        if result.get('spelling_corrections'):
            total_corrections += len(result['spelling_corrections'])
            print(f"✏️  {result['file']}: {len(result['spelling_corrections'])} lỗi chính tả đã sửa")
        
        if result.get('grammar_issues'):
            total_grammar_issues += len(result['grammar_issues'])
            print(f"📝 {result['file']}: {len(result['grammar_issues'])} vấn đề ngữ pháp")
        
        if result.get('error'):
            print(f"❌ {result['file']}: Lỗi - {result['error']}")
        elif not result.get('spelling_corrections') and not result.get('grammar_issues'):
            print(f"✅ {result['file']}: Không có lỗi")
    
    # Tạo báo cáo chi tiết
    report_path = os.path.join(base_dir, "SPELL_GRAMMAR_REPORT.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# BÁO CÁO KIỂM TRA CHÍNH TẢ VÀ VĂN PHONG\n\n")
        f.write(f"**Ngày kiểm tra**: {os.popen('date').read().strip()}\n\n")
        f.write("## Tổng kết\n\n")
        f.write(f"- **Tổng số file**: {total_files}\n")
        f.write(f"- **File đã sửa**: {files_changed}\n")
        f.write(f"- **Tổng lỗi chính tả đã sửa**: {total_corrections}\n")
        f.write(f"- **Tổng vấn đề ngữ pháp**: {total_grammar_issues}\n\n")
        
        f.write("## Chi tiết từng file\n\n")
        for result in results:
            f.write(f"### {result['file']}\n\n")
            
            if result.get('error'):
                f.write(f"❌ **Lỗi**: {result['error']}\n\n")
                continue
            
            if result.get('spelling_corrections'):
                f.write("**Lỗi chính tả đã sửa:**\n")
                for correction in result['spelling_corrections']:
                    f.write(f"- {correction}\n")
                f.write("\n")
            
            if result.get('grammar_issues'):
                f.write("**Vấn đề ngữ pháp:**\n")
                for issue in result['grammar_issues']:
                    f.write(f"- {issue}\n")
                f.write("\n")
            
            if not result.get('spelling_corrections') and not result.get('grammar_issues'):
                f.write("✅ Không có lỗi\n\n")
    
    print("\n" + "=" * 50)
    print("📊 TỔNG KẾT:")
    print(f"✅ Đã kiểm tra: {total_files} file")
    print(f"✏️  Đã sửa: {files_changed} file")
    print(f"🔧 Lỗi chính tả đã sửa: {total_corrections}")
    print(f"📝 Vấn đề ngữ pháp: {total_grammar_issues}")
    print(f"📋 Báo cáo chi tiết: SPELL_GRAMMAR_REPORT.md")

if __name__ == "__main__":
    main()
