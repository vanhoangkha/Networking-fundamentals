#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import subprocess

# Từ điển dịch thuật ngữ kỹ thuật
TECHNICAL_TERMS = {
    # Networking terms
    "Network": "Mạng",
    "Router": "Router", 
    "Switch": "Switch",
    "Hub": "Hub",
    "Bridge": "Bridge",
    "Gateway": "Gateway",
    "Firewall": "Tường lửa",
    "Access Point": "Điểm truy cập",
    "Wireless": "Không dây",
    "Ethernet": "Ethernet",
    "Cable": "Cáp",
    "Interface": "Giao diện",
    "Port": "Cổng",
    "Protocol": "Giao thức",
    "Packet": "Gói tin",
    "Frame": "Khung",
    "Segment": "Đoạn",
    "Header": "Header",
    "Trailer": "Trailer",
    "Encapsulation": "Đóng gói",
    "De-encapsulation": "Mở gói",
    
    # IP and addressing
    "IP Address": "Địa chỉ IP",
    "IPv4": "IPv4",
    "IPv6": "IPv6", 
    "Subnet": "Mạng con",
    "Subnetting": "Chia mạng con",
    "VLSM": "VLSM",
    "CIDR": "CIDR",
    "Broadcast": "Broadcast",
    "Multicast": "Multicast",
    "Unicast": "Unicast",
    "MAC Address": "Địa chỉ MAC",
    
    # Routing
    "Routing": "Định tuyến",
    "Static Routing": "Định tuyến tĩnh",
    "Dynamic Routing": "Định tuyến động",
    "Route": "Tuyến đường",
    "Routing Table": "Bảng định tuyến",
    "Default Route": "Tuyến đường mặc định",
    "Administrative Distance": "Khoảng cách quản trị",
    "Metric": "Metric",
    
    # Protocols
    "TCP": "TCP",
    "UDP": "UDP",
    "HTTP": "HTTP",
    "HTTPS": "HTTPS",
    "FTP": "FTP",
    "TFTP": "TFTP",
    "SSH": "SSH",
    "Telnet": "Telnet",
    "SNMP": "SNMP",
    "DNS": "DNS",
    "DHCP": "DHCP",
    "NTP": "NTP",
    "OSPF": "OSPF",
    "EIGRP": "EIGRP",
    "RIP": "RIP",
    "BGP": "BGP",
    
    # VLAN
    "VLAN": "VLAN",
    "Trunk": "Trunk",
    "Access": "Access",
    "Native VLAN": "VLAN gốc",
    "Voice VLAN": "VLAN thoại",
    "DTP": "DTP",
    "VTP": "VTP",
    
    # Spanning Tree
    "Spanning Tree": "Spanning Tree",
    "STP": "STP",
    "RSTP": "RSTP",
    "Root Bridge": "Bridge gốc",
    "Designated Port": "Cổng được chỉ định",
    "Blocked Port": "Cổng bị chặn",
    
    # Security
    "Security": "Bảo mật",
    "Access Control List": "Danh sách kiểm soát truy cập",
    "ACL": "ACL",
    "Standard ACL": "ACL chuẩn",
    "Extended ACL": "ACL mở rộng",
    "Port Security": "Bảo mật cổng",
    "DHCP Snooping": "DHCP Snooping",
    "ARP Inspection": "Kiểm tra ARP",
    
    # QoS
    "Quality of Service": "Chất lượng dịch vụ",
    "QoS": "QoS",
    "Traffic Shaping": "Định hình lưu lượng",
    "Policing": "Kiểm soát",
    "Classification": "Phân loại",
    "Marking": "Đánh dấu",
    
    # NAT
    "Network Address Translation": "Dịch địa chỉ mạng",
    "NAT": "NAT",
    "Static NAT": "NAT tĩnh",
    "Dynamic NAT": "NAT động",
    "PAT": "PAT",
    "Port Address Translation": "Dịch địa chỉ cổng",
    
    # Wireless
    "SSID": "SSID",
    "WPA": "WPA",
    "WEP": "WEP",
    "WPA2": "WPA2",
    "WPA3": "WPA3",
    "Access Point": "Điểm truy cập",
    "Wireless Controller": "Bộ điều khiển không dây",
    
    # Automation
    "Automation": "Tự động hóa",
    "API": "API",
    "REST": "REST",
    "JSON": "JSON",
    "XML": "XML",
    "YAML": "YAML",
    "Ansible": "Ansible",
    "Puppet": "Puppet",
    "Chef": "Chef",
    "SDN": "SDN",
    "Software Defined Networking": "Mạng định nghĩa bằng phần mềm",
    
    # General terms
    "Configuration": "Cấu hình",
    "Command": "Lệnh",
    "CLI": "CLI",
    "Command Line Interface": "Giao diện dòng lệnh",
    "Enable": "Kích hoạt",
    "Disable": "Vô hiệu hóa",
    "Default": "Mặc định",
    "Administrative": "Quản trị",
    "Management": "Quản lý",
    "Monitoring": "Giám sát",
    "Troubleshooting": "Khắc phục sự cố",
    "Topology": "Cấu trúc mạng",
    "Architecture": "Kiến trúc",
    "Infrastructure": "Hạ tầng",
    "Enterprise": "Doanh nghiệp",
    "Campus": "Campus",
    "WAN": "WAN",
    "LAN": "LAN",
    "MAN": "MAN",
    "Internet": "Internet",
    "Intranet": "Intranet",
    "Extranet": "Extranet"
}

# Từ điển dịch các cụm từ thông dụng
COMMON_PHRASES = {
    "What is": "là gì",
    "How to": "Cách",
    "Why do we need": "Tại sao chúng ta cần",
    "The purpose of": "Mục đích của",
    "In this section": "Trong phần này",
    "For example": "Ví dụ",
    "Note that": "Lưu ý rằng",
    "It is important to": "Điều quan trọng là",
    "Keep in mind": "Hãy nhớ rằng",
    "As we can see": "Như chúng ta có thể thấy",
    "In other words": "Nói cách khác",
    "To summarize": "Tóm lại",
    "In conclusion": "Kết luận",
    "Best practices": "Thực hành tốt nhất",
    "Common mistakes": "Lỗi thường gặp",
    "Troubleshooting": "Khắc phục sự cố"
}

def translate_content(content):
    """
    Dịch nội dung từ tiếng Anh sang tiếng Việt
    Giữ nguyên các thuật ngữ kỹ thuật và code
    """
    
    # Giữ nguyên các code block
    code_blocks = []
    code_pattern = r'```[\s\S]*?```'
    for match in re.finditer(code_pattern, content):
        code_blocks.append(match.group())
        content = content.replace(match.group(), f'__CODE_BLOCK_{len(code_blocks)-1}__')
    
    # Giữ nguyên các inline code
    inline_codes = []
    inline_pattern = r'`[^`]+`'
    for match in re.finditer(inline_pattern, content):
        inline_codes.append(match.group())
        content = content.replace(match.group(), f'__INLINE_CODE_{len(inline_codes)-1}__')
    
    # Giữ nguyên các link hình ảnh
    image_links = []
    image_pattern = r'!\[.*?\]\(.*?\)'
    for match in re.finditer(image_pattern, content):
        image_links.append(match.group())
        content = content.replace(match.group(), f'__IMAGE_{len(image_links)-1}__')
    
    # Dịch các cụm từ thông dụng trước
    for en_phrase, vi_phrase in COMMON_PHRASES.items():
        content = re.sub(r'\b' + re.escape(en_phrase) + r'\b', vi_phrase, content, flags=re.IGNORECASE)
    
    # Dịch các thuật ngữ kỹ thuật
    for en_term, vi_term in TECHNICAL_TERMS.items():
        # Chỉ thay thế nếu không phải là phần của từ khác
        content = re.sub(r'\b' + re.escape(en_term) + r'\b', vi_term, content, flags=re.IGNORECASE)
    
    # Khôi phục các code block
    for i, code_block in enumerate(code_blocks):
        content = content.replace(f'__CODE_BLOCK_{i}__', code_block)
    
    # Khôi phục các inline code
    for i, inline_code in enumerate(inline_codes):
        content = content.replace(f'__INLINE_CODE_{i}__', inline_code)
    
    # Khôi phục các link hình ảnh
    for i, image_link in enumerate(image_links):
        content = content.replace(f'__IMAGE_{i}__', image_link)
    
    return content

def translate_file(file_path):
    """Dịch một file markdown"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Dịch nội dung
        translated_content = translate_content(content)
        
        # Ghi lại file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        
        print(f"✅ Đã dịch: {file_path}")
        return True
    except Exception as e:
        print(f"❌ Lỗi khi dịch {file_path}: {e}")
        return False

def main():
    """Hàm chính để dịch tất cả các file"""
    
    # Danh sách các file cần dịch (bỏ qua những file đã dịch)
    translated_files = [
        "README.md",
        "Day01_Network_Devices.md", 
        "Day02_Interfaces_and_Cables.md",
        "Day03_OSI_Model_TCPSuite.md"
    ]
    
    # Lấy danh sách tất cả file .md
    all_files = [f for f in os.listdir('.') if f.endswith('.md') and f.startswith('Day')]
    
    # Lọc ra những file chưa dịch
    files_to_translate = [f for f in all_files if f not in translated_files]
    
    print(f"🚀 Bắt đầu dịch {len(files_to_translate)} file...")
    
    success_count = 0
    for file_name in sorted(files_to_translate):
        if translate_file(file_name):
            success_count += 1
    
    print(f"\n📊 Kết quả: Đã dịch thành công {success_count}/{len(files_to_translate)} file")
    
    if success_count > 0:
        print("\n📝 Commit các thay đổi...")
        try:
            subprocess.run(['git', 'add', '.'], check=True)
            subprocess.run(['git', 'commit', '-m', f'Dịch tự động {success_count} file sang tiếng Việt\n\n- Sử dụng script tự động để dịch các thuật ngữ kỹ thuật\n- Giữ nguyên code, hình ảnh và format\n- Dịch các cụm từ thông dụng'], check=True)
            subprocess.run(['git', 'push', 'origin', 'master'], check=True)
            print("✅ Đã commit và push thành công!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Lỗi khi commit: {e}")

if __name__ == "__main__":
    main()
