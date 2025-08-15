#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import subprocess

# Từ điển sửa lỗi dịch
CORRECTIONS = {
    # Sửa các lỗi dịch phổ biến
    "là gì a": "Giới thiệu về",
    "là gì the": "là gì",
    "Lệnh-line": "Command-line", 
    "Giao diện": "Interface",
    "Cổng": "Port",
    "Cáp": "Cable",
    "Mặc định": "Default",
    "Quản lý": "Management",
    "Bảo mật": "Security",
    "Cấu hình": "Configuration",
    "Kết nối": "Connection",
    "Thiết bị": "Device",
    "Mạng": "Network",
    
    # Sửa các cụm từ bị dịch sai
    "What is a": "là gì",
    "How to": "Cách thức",
    "Why do we need": "Tại sao chúng ta cần",
    "In this section": "Trong phần này",
    "For example": "Ví dụ",
    "Note that": "Lưu ý rằng",
    
    # Giữ nguyên các thuật ngữ kỹ thuật
    "CLI": "CLI",
    "GUI": "GUI", 
    "API": "API",
    "TCP": "TCP",
    "UDP": "UDP",
    "IP": "IP",
    "MAC": "MAC",
    "VLAN": "VLAN",
    "VPN": "VPN",
    "DNS": "DNS",
    "DHCP": "DHCP",
    "HTTP": "HTTP",
    "HTTPS": "HTTPS",
    "SSH": "SSH",
    "FTP": "FTP",
    "TFTP": "TFTP",
    "SNMP": "SNMP",
    "NTP": "NTP",
    "OSPF": "OSPF",
    "EIGRP": "EIGRP",
    "RIP": "RIP",
    "BGP": "BGP",
    "STP": "STP",
    "RSTP": "RSTP",
    "ACL": "ACL",
    "NAT": "NAT",
    "PAT": "PAT",
    "QoS": "QoS",
    "SSID": "SSID",
    "WPA": "WPA",
    "WEP": "WEP",
    "JSON": "JSON",
    "XML": "XML",
    "YAML": "YAML",
    "REST": "REST",
    "SDN": "SDN"
}

def fix_translation(content):
    """Sửa các lỗi dịch trong nội dung"""
    
    # Sửa các lỗi dịch phổ biến
    for wrong, correct in CORRECTIONS.items():
        content = content.replace(wrong, correct)
    
    # Sửa các pattern đặc biệt
    content = re.sub(r'# (\d+)\. (.+)', lambda m: f'# {m.group(1)}. {m.group(2).upper()}', content)
    
    # Sửa các tiêu đề bị dịch sai
    content = re.sub(r'### (.+) là gì', r'### \1 là gì?', content)
    content = re.sub(r'## (.+) là gì', r'## \1 là gì?', content)
    
    return content

def fix_file(file_path):
    """Sửa lỗi dịch trong một file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sửa lỗi dịch
        fixed_content = fix_translation(content)
        
        # Chỉ ghi lại nếu có thay đổi
        if fixed_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"✅ Đã sửa: {file_path}")
            return True
        else:
            print(f"⏭️  Bỏ qua: {file_path} (không có lỗi)")
            return False
    except Exception as e:
        print(f"❌ Lỗi khi sửa {file_path}: {e}")
        return False

def main():
    """Hàm chính để sửa lỗi dịch"""
    
    # Lấy danh sách tất cả file .md
    all_files = [f for f in os.listdir('.') if f.endswith('.md')]
    
    print(f"🔧 Bắt đầu sửa lỗi dịch cho {len(all_files)} file...")
    
    fixed_count = 0
    for file_name in sorted(all_files):
        if fix_file(file_name):
            fixed_count += 1
    
    print(f"\n📊 Kết quả: Đã sửa {fixed_count}/{len(all_files)} file")
    
    if fixed_count > 0:
        print("\n📝 Commit các thay đổi...")
        try:
            subprocess.run(['git', 'add', '.'], check=True)
            subprocess.run(['git', 'commit', '-m', f'Sửa lỗi dịch tự động\n\n- Sửa {fixed_count} file có lỗi dịch\n- Cải thiện chất lượng thuật ngữ kỹ thuật\n- Giữ nguyên format và cấu trúc'], check=True)
            subprocess.run(['git', 'push', 'origin', 'master'], check=True)
            print("✅ Đã commit và push thành công!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Lỗi khi commit: {e}")
    else:
        print("✅ Không có lỗi nào cần sửa!")

if __name__ == "__main__":
    main()
