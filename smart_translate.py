#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import subprocess

# Từ điển dịch thông minh - chỉ dịch những gì cần thiết
SMART_TRANSLATIONS = {
    # Headers
    "ETHERNET LAN SWITCHING": "CHUYỂN MẠCH ETHERNET LAN",
    "IPV4 ADDRESSING": "ĐỊA CHỈ IPV4", 
    "SWITCH INTERFACES": "GIAO DIỆN SWITCH",
    "THE IPV4 HEADER": "HEADER IPV4",
    "ROUTING FUNDAMENTALS": "CƠ BẢN VỀ ĐỊNH TUYẾN",
    "STATIC ROUTING": "ĐỊNH TUYẾN TĨNH",
    "LIFE OF A PACKET": "VÒNG ĐỜI CỦA GÓI TIN",
    "SUBNETTING": "CHIA MẠNG CON",
    
    # Common phrases - dịch cả câu
    "What is a": "là gì",
    "What are": "là gì", 
    "How do you": "Làm thế nào để bạn",
    "How to": "Cách thức",
    "Why do we need": "Tại sao chúng ta cần",
    "For example": "Ví dụ",
    "Note that": "Lưu ý rằng",
    "In other words": "Nói cách khác",
    "To summarize": "Tóm lại",
    "As we can see": "Như chúng ta có thể thấy",
    
    # Technical terms
    "Network": "Mạng",
    "Device": "Thiết bị", 
    "Router": "Router",
    "Switch": "Switch",
    "Interface": "Giao diện",
    "Port": "Cổng",
    "Cable": "Cáp",
    "Address": "Địa chỉ",
    "Packet": "Gói tin",
    "Frame": "Khung",
    "Header": "Header",
    "Trailer": "Trailer",
    "Protocol": "Giao thức",
    "Configuration": "Cấu hình",
    "Command": "Lệnh",
    "Password": "Mật khẩu",
    "Security": "Bảo mật",
    "Access": "Truy cập",
    "Control": "Kiểm soát",
    "Management": "Quản lý",
    "Routing": "Định tuyến",
    "Switching": "Chuyển mạch",
    "Subnet": "Mạng con",
    "VLAN": "VLAN",
    "Trunk": "Trunk",
    "Quality of Service": "Chất lượng dịch vụ",
    "Wireless": "Không dây",
    "Firewall": "Tường lửa",
    "Encryption": "Mã hóa",
    "Authentication": "Xác thực",
    "Authorization": "Ủy quyền",
    "Accounting": "Kế toán",
    
    # Specific networking terms
    "MAC Address": "Địa chỉ MAC",
    "IP Address": "Địa chỉ IP", 
    "Default Gateway": "Gateway mặc định",
    "Subnet Mask": "Subnet Mask",
    "DHCP": "DHCP",
    "DNS": "DNS",
    "NAT": "NAT",
    "ACL": "ACL",
    "QoS": "QoS",
    "VPN": "VPN",
    "OSPF": "OSPF",
    "EIGRP": "EIGRP",
    "RIP": "RIP",
    "BGP": "BGP",
    "STP": "STP",
    "RSTP": "RSTP",
    "PVST": "PVST",
    "EtherChannel": "EtherChannel",
    "LACP": "LACP",
    "PAgP": "PAgP",
    
    # Common words
    " is ": " là ",
    " are ": " là ",
    " and ": " và ",
    " or ": " hoặc ",
    " the ": " ",
    " a ": " một ",
    " an ": " một ",
    " of ": " của ",
    " in ": " trong ",
    " on ": " trên ",
    " at ": " tại ",
    " to ": " đến ",
    " for ": " cho ",
    " with ": " với ",
    " by ": " bởi ",
    " from ": " từ ",
    " can ": " có thể ",
    " will ": " sẽ ",
    " would ": " sẽ ",
    " should ": " nên ",
    " must ": " phải ",
    " may ": " có thể ",
    " might ": " có thể ",
    " could ": " có thể ",
}

def smart_translate_content(content):
    """Dịch thông minh - chỉ dịch những phần cần thiết"""
    
    # Bảo vệ code blocks
    code_blocks = []
    code_pattern = r'```[\s\S]*?```'
    for i, match in enumerate(re.finditer(code_pattern, content)):
        code_blocks.append(match.group())
        content = content.replace(match.group(), f'__CODE_BLOCK_{i}__')
    
    # Bảo vệ inline code
    inline_codes = []
    inline_pattern = r'`[^`]+`'
    for i, match in enumerate(re.finditer(inline_pattern, content)):
        inline_codes.append(match.group())
        content = content.replace(match.group(), f'__INLINE_CODE_{i}__')
    
    # Bảo vệ images
    images = []
    image_pattern = r'!\[.*?\]\(.*?\)'
    for i, match in enumerate(re.finditer(image_pattern, content)):
        images.append(match.group())
        content = content.replace(match.group(), f'__IMAGE_{i}__')
    
    # Bảo vệ URLs
    urls = []
    url_pattern = r'https?://[^\s\)]+'
    for i, match in enumerate(re.finditer(url_pattern, content)):
        urls.append(match.group())
        content = content.replace(match.group(), f'__URL_{i}__')
    
    # Dịch theo thứ tự từ dài đến ngắn
    sorted_translations = sorted(SMART_TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)
    
    for en_text, vi_text in sorted_translations:
        if en_text.strip() and vi_text.strip():
            # Dịch với word boundaries để tránh dịch nhầm
            pattern = r'\b' + re.escape(en_text) + r'\b'
            content = re.sub(pattern, vi_text, content, flags=re.IGNORECASE)
    
    # Khôi phục các phần đã bảo vệ
    for i, code_block in enumerate(code_blocks):
        content = content.replace(f'__CODE_BLOCK_{i}__', code_block)
    
    for i, inline_code in enumerate(inline_codes):
        content = content.replace(f'__INLINE_CODE_{i}__', inline_code)
    
    for i, image in enumerate(images):
        content = content.replace(f'__IMAGE_{i}__', image)
    
    for i, url in enumerate(urls):
        content = content.replace(f'__URL_{i}__', url)
    
    # Làm sạch
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'\n\s+', '\n', content)
    
    return content

def translate_file_smart(file_path):
    """Dịch một file một cách thông minh"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Dịch nội dung
        translated_content = smart_translate_content(original_content)
        
        # Chỉ ghi nếu có thay đổi
        if translated_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(translated_content)
            print(f"✅ Đã dịch: {file_path}")
            return True
        else:
            print(f"⏭️  Bỏ qua: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Lỗi: {file_path} - {e}")
        return False

def main():
    """Dịch tất cả các file chưa được dịch hoàn chỉnh"""
    
    # Danh sách file đã dịch hoàn chỉnh
    completed_files = [
        "README.md",
        "Day01_Network_Devices.md",
        "Day02_Interfaces_and_Cables.md", 
        "Day03_OSI_Model_TCPSuite.md",
        "Day04_Intro_to_CLI.md",
        "Day05_Ethernet_LAN_Switching_Part1.md"
    ]
    
    # Lấy tất cả file .md
    all_files = [f for f in os.listdir('.') if f.endswith('.md') and f.startswith('Day')]
    
    # File cần dịch
    files_to_translate = [f for f in all_files if f not in completed_files]
    
    print(f"🚀 Bắt đầu dịch thông minh {len(files_to_translate)} file...")
    
    success_count = 0
    for file_name in sorted(files_to_translate):
        if translate_file_smart(file_name):
            success_count += 1
    
    print(f"\n📊 Kết quả: Đã dịch {success_count}/{len(files_to_translate)} file")
    
    if success_count > 0:
        print("\n📝 Commit thay đổi...")
        try:
            subprocess.run(['git', 'add', '.'], check=True)
            subprocess.run(['git', 'commit', '-m', f'Dịch thông minh {success_count} file\n\n- Dịch các thuật ngữ kỹ thuật chính\n- Dịch tiêu đề và cụm từ quan trọng\n- Giữ nguyên format và cấu trúc\n- Bảo vệ code, hình ảnh và URL'], check=True)
            subprocess.run(['git', 'push', 'origin', 'master'], check=True)
            print("✅ Đã commit và push thành công!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Lỗi commit: {e}")

if __name__ == "__main__":
    main()
