#!/usr/bin/env python3
"""
Script kiểm tra văn phong nâng cao cho tài liệu CCNA
Đảm bảo tính nhất quán và chuyên nghiệp trong văn bản
"""

import os
import re
import glob
from pathlib import Path

class AdvancedStyleChecker:
    def __init__(self):
        # Quy tắc văn phong nâng cao
        self.style_improvements = {
            # Cải thiện cách diễn đạt
            "có thể được sử dụng": "có thể sử dụng",
            "được sử dụng để": "dùng để",
            "có khả năng": "có thể",
            "thực hiện việc": "thực hiện",
            "tiến hành": "thực hiện",
            "đảm bảo rằng": "đảm bảo",
            "chắc chắn rằng": "đảm bảo",
            "trong trường hợp mà": "khi",
            "trong trường hợp": "khi",
            "bởi vì": "vì",
            "do đó mà": "do đó",
            "vì vậy mà": "vì vậy",
            "tuy nhiên": "nhưng",
            "mặc dù vậy": "tuy vậy",
            "ngoài ra": "bên cạnh đó",
            
            # Chuẩn hóa thuật ngữ kỹ thuật
            "địa chỉ ip": "địa chỉ IP",
            "giao thức tcp": "giao thức TCP",
            "giao thức udp": "giao thức UDP",
            "mô hình osi": "mô hình OSI",
            "ethernet": "Ethernet",
            "internet": "Internet",
            "wifi": "Wi-Fi",
            "bluetooth": "Bluetooth",
            
            # Cải thiện cách viết số và đơn vị
            "1 byte": "1 byte",
            "2 byte": "2 byte",
            "8 bit": "8 bit",
            "16 bit": "16 bit",
            "32 bit": "32 bit",
            "64 bit": "64 bit",
            
            # Chuẩn hóa dấu câu
            " ,": ",",
            " .": ".",
            " :": ":",
            " ;": ";",
            "( ": "(",
            " )": ")",
            "[ ": "[",
            " ]": "]",
            "{ ": "{",
            " }": "}",
        }
        
        # Quy tắc format đặc biệt
        self.format_rules = [
            # Chuẩn hóa bullet points
            (r'^•\s*', '- '),
            (r'^-\s+', '- '),
            (r'^\*\s+', '- '),
            
            # Chuẩn hóa heading
            (r'^#{1,6}\s*(.+)', lambda m: '#' * len(m.group(0).split()[0]) + ' ' + ' '.join(m.group(0).split()[1:])),
            
            # Chuẩn hóa code blocks
            (r'`([^`\n]+)`', r'`\1`'),
            
            # Chuẩn hóa emphasis
            (r'\*\*([^*]+)\*\*', r'**\1**'),
            (r'\*([^*]+)\*', r'*\1*'),
            
            # Loại bỏ khoảng trắng thừa
            (r'\s+', ' '),
            (r'^\s+|\s+$', ''),
        ]
        
        # Từ khóa cần viết hoa nhất quán
        self.technical_terms = {
            'cisco': 'Cisco',
            'ieee': 'IEEE',
            'iso': 'ISO',
            'ietf': 'IETF',
            'rfc': 'RFC',
            'tcp': 'TCP',
            'udp': 'UDP',
            'ip': 'IP',
            'ipv4': 'IPv4',
            'ipv6': 'IPv6',
            'http': 'HTTP',
            'https': 'HTTPS',
            'ftp': 'FTP',
            'tftp': 'TFTP',
            'ssh': 'SSH',
            'telnet': 'Telnet',
            'snmp': 'SNMP',
            'dhcp': 'DHCP',
            'dns': 'DNS',
            'vlan': 'VLAN',
            'stp': 'STP',
            'rstp': 'RSTP',
            'ospf': 'OSPF',
            'eigrp': 'EIGRP',
            'rip': 'RIP',
            'bgp': 'BGP',
            'nat': 'NAT',
            'pat': 'PAT',
            'acl': 'ACL',
            'qos': 'QoS',
            'vpn': 'VPN',
            'mpls': 'MPLS',
            'hsrp': 'HSRP',
            'vrrp': 'VRRP',
            'glbp': 'GLBP',
            'etherchannel': 'EtherChannel',
            'poe': 'PoE',
            'cdp': 'CDP',
            'lldp': 'LLDP',
            'ntp': 'NTP',
            'syslog': 'SYSLOG',
            'aaa': 'AAA',
            'radius': 'RADIUS',
            'tacacs': 'TACACS',
            'wpa': 'WPA',
            'wep': 'WEP',
            'wpa2': 'WPA2',
            'wpa3': 'WPA3',
            'ssid': 'SSID',
            'bssid': 'BSSID',
            'ess': 'ESS',
            'bss': 'BSS',
            'lan': 'LAN',
            'wan': 'WAN',
            'man': 'MAN',
            'pan': 'PAN',
            'cli': 'CLI',
            'gui': 'GUI',
            'api': 'API',
            'rest': 'REST',
            'json': 'JSON',
            'xml': 'XML',
            'yaml': 'YAML',
            'sql': 'SQL',
            'html': 'HTML',
            'css': 'CSS',
            'javascript': 'JavaScript',
            'python': 'Python',
            'ansible': 'Ansible',
            'puppet': 'Puppet',
            'chef': 'Chef',
            'docker': 'Docker',
            'kubernetes': 'Kubernetes',
            'vmware': 'VMware',
            'aws': 'AWS',
            'azure': 'Azure',
            'gcp': 'GCP',
        }

    def improve_style(self, text):
        """Cải thiện văn phong tổng thể"""
        improved_text = text
        changes_made = []
        
        # Áp dụng cải thiện văn phong
        for old_phrase, new_phrase in self.style_improvements.items():
            if old_phrase in improved_text:
                improved_text = improved_text.replace(old_phrase, new_phrase)
                changes_made.append(f"'{old_phrase}' → '{new_phrase}'")
        
        # Áp dụng quy tắc format
        for pattern, replacement in self.format_rules:
            if callable(replacement):
                improved_text = re.sub(pattern, replacement, improved_text, flags=re.MULTILINE)
            else:
                improved_text = re.sub(pattern, replacement, improved_text, flags=re.MULTILINE)
        
        # Chuẩn hóa thuật ngữ kỹ thuật
        for term_lower, term_correct in self.technical_terms.items():
            pattern = r'\b' + re.escape(term_lower) + r'\b'
            if re.search(pattern, improved_text, re.IGNORECASE):
                improved_text = re.sub(pattern, term_correct, improved_text, flags=re.IGNORECASE)
                changes_made.append(f"'{term_lower}' → '{term_correct}'")
        
        return improved_text, changes_made

    def check_consistency(self, text):
        """Kiểm tra tính nhất quán"""
        issues = []
        
        lines = text.split('\n')
        
        # Kiểm tra format heading
        for i, line in enumerate(lines, 1):
            if line.startswith('#'):
                # Kiểm tra space sau #
                if not re.match(r'^#+\s+', line):
                    issues.append(f"Dòng {i}: Thiếu khoảng trắng sau dấu # trong heading")
                
                # Kiểm tra viết hoa heading
                heading_text = re.sub(r'^#+\s*', '', line)
                if heading_text and not heading_text[0].isupper():
                    issues.append(f"Dòng {i}: Heading nên bắt đầu bằng chữ hoa")
        
        # Kiểm tra bullet points
        bullet_styles = set()
        for line in lines:
            if re.match(r'^\s*[-*•]\s', line):
                bullet_char = re.match(r'^\s*([-*•])', line).group(1)
                bullet_styles.add(bullet_char)
        
        if len(bullet_styles) > 1:
            issues.append(f"Không nhất quán trong bullet points: {bullet_styles}")
        
        return issues

    def process_file(self, file_path):
        """Xử lý một file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Cải thiện văn phong
            content, style_changes = self.improve_style(content)
            
            # Kiểm tra tính nhất quán
            consistency_issues = self.check_consistency(content)
            
            # Lưu file nếu có thay đổi
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            return {
                'file': os.path.basename(file_path),
                'style_changes': style_changes,
                'consistency_issues': consistency_issues,
                'changed': content != original_content
            }
            
        except Exception as e:
            return {
                'file': os.path.basename(file_path),
                'error': str(e),
                'changed': False
            }

def main():
    checker = AdvancedStyleChecker()
    base_dir = "/home/ubuntu/NEO/Networking fundamentals"
    pattern = os.path.join(base_dir, "Day*.md")
    files = glob.glob(pattern)
    
    print("🎨 KIỂM TRA VĂN PHONG NÂNG CAO")
    print("=" * 50)
    
    total_files = len(files)
    files_changed = 0
    total_style_changes = 0
    total_consistency_issues = 0
    
    results = []
    
    for file_path in sorted(files):
        result = checker.process_file(file_path)
        results.append(result)
        
        if result.get('changed'):
            files_changed += 1
        
        if result.get('style_changes'):
            total_style_changes += len(result['style_changes'])
            print(f"🎨 {result['file']}: {len(result['style_changes'])} cải thiện văn phong")
        
        if result.get('consistency_issues'):
            total_consistency_issues += len(result['consistency_issues'])
            print(f"⚠️  {result['file']}: {len(result['consistency_issues'])} vấn đề nhất quán")
        
        if result.get('error'):
            print(f"❌ {result['file']}: Lỗi - {result['error']}")
        elif not result.get('style_changes') and not result.get('consistency_issues'):
            print(f"✅ {result['file']}: Hoàn hảo")
    
    # Tạo báo cáo
    report_path = os.path.join(base_dir, "ADVANCED_STYLE_REPORT.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# BÁO CÁO KIỂM TRA VĂN PHONG NÂNG CAO\n\n")
        f.write(f"**Ngày kiểm tra**: {os.popen('date').read().strip()}\n\n")
        f.write("## Tổng kết\n\n")
        f.write(f"- **Tổng số file**: {total_files}\n")
        f.write(f"- **File đã cải thiện**: {files_changed}\n")
        f.write(f"- **Tổng cải thiện văn phong**: {total_style_changes}\n")
        f.write(f"- **Tổng vấn đề nhất quán**: {total_consistency_issues}\n\n")
        
        if total_style_changes > 0:
            f.write("## Chi tiết cải thiện văn phong\n\n")
            for result in results:
                if result.get('style_changes'):
                    f.write(f"### {result['file']}\n\n")
                    for change in result['style_changes'][:10]:  # Chỉ hiển thị 10 thay đổi đầu
                        f.write(f"- {change}\n")
                    if len(result['style_changes']) > 10:
                        f.write(f"- ... và {len(result['style_changes']) - 10} thay đổi khác\n")
                    f.write("\n")
        
        if total_consistency_issues > 0:
            f.write("## Vấn đề nhất quán cần chú ý\n\n")
            for result in results:
                if result.get('consistency_issues'):
                    f.write(f"### {result['file']}\n\n")
                    for issue in result['consistency_issues']:
                        f.write(f"- {issue}\n")
                    f.write("\n")
    
    print("\n" + "=" * 50)
    print("📊 TỔNG KẾT VĂN PHONG NÂNG CAO:")
    print(f"✅ Đã kiểm tra: {total_files} file")
    print(f"🎨 Đã cải thiện: {files_changed} file")
    print(f"✏️  Cải thiện văn phong: {total_style_changes}")
    print(f"⚠️  Vấn đề nhất quán: {total_consistency_issues}")
    print(f"📋 Báo cáo chi tiết: ADVANCED_STYLE_REPORT.md")

if __name__ == "__main__":
    main()
