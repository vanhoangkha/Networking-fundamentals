#!/usr/bin/env python3
"""
Script sửa các vấn đề cụ thể đã phát hiện
"""

import os
import re

def fix_day15_issues():
    """Sửa các vấn đề trong Day15"""
    file_path = "/home/ubuntu/NEO/Networking fundamentals/Day15_Subnetting_Part2.md"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sửa bảng bị lỗi
        # Thay thế bảng Class C
        old_table_c = """| ## 15.13 Class C (192.168.1.0/24): | CIDR | Subnet Mask | Số Subnet | Host/Subnet | Tổng Host |
| ------- | ------- | ------- | ------- | ------- |
| /25 | 255.255.255.128 | 2 | 126 | 252 |
| /26 | 255.255.255.192 | 4 | 62 | 248 |
| /27 | 255.255.255.224 | 8 | 30 | 240 |
| /28 | 255.255.255.240 | 16 | 14 | 224 |
| /29 | 255.255.255.248 | 32 | 6 | 192 |
| /30 | 255.255.255.252 | 64 | 2 | 128 |"""

        new_table_c = """## 15.13 Class C (192.168.1.0/24)

| CIDR | Subnet Mask | Số Subnet | Host/Subnet | Tổng Host |
| ------- | ------- | ------- | ------- | ------- |
| /25 | 255.255.255.128 | 2 | 126 | 252 |
| /26 | 255.255.255.192 | 4 | 62 | 248 |
| /27 | 255.255.255.224 | 8 | 30 | 240 |
| /28 | 255.255.255.240 | 16 | 14 | 224 |
| /29 | 255.255.255.248 | 32 | 6 | 192 |
| /30 | 255.255.255.252 | 64 | 2 | 128 |"""

        content = content.replace(old_table_c, new_table_c)
        
        # Thay thế bảng Class B
        old_table_b = """| ## 15.14 Class B (172.16.0.0/16): | CIDR | Subnet Mask | Số Subnet | Host/Subnet | Tổng Host |
| ------- | ------- | ------- | ------- | ------- |
| /17 | 255.255.128.0 | 2 | 32,766 | 65,532 |
| /18 | 255.255.192.0 | 4 | 16,382 | 65,528 |"""

        new_table_b = """## 15.14 Class B (172.16.0.0/16)

| CIDR | Subnet Mask | Số Subnet | Host/Subnet | Tổng Host |
| ------- | ------- | ------- | ------- | ------- |
| /17 | 255.255.128.0 | 2 | 32,766 | 65,532 |
| /18 | 255.255.192.0 | 4 | 16,382 | 65,528 |"""

        content = content.replace(old_table_b, new_table_b)
        
        # Sửa các lỗi bold text
        content = re.sub(r'\*\*([^*]+?)\s*:\s*\*\*', r'**\1:**', content)
        
        # Sửa thuật ngữ
        content = content.replace('https', 'HTTPS')
        
        # Lưu file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("Đã sửa Day15_Subnetting_Part2.md")
        return True
        
    except Exception as e:
        print(f"Lỗi khi sửa Day15: {e}")
        return False

def fix_day20_issues():
    """Sửa các vấn đề trong Day20"""
    file_path = "/home/ubuntu/NEO/Networking fundamentals/Day20_DTP_VTP.md"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sửa các lỗi format và thuật ngữ
        content = re.sub(r'\*\*([^*]+?)\s*:\s*\*\*', r'**\1:**', content)
        content = content.replace('vlan', 'VLAN')
        content = content.replace('cisco', 'Cisco')
        
        # Lưu file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("Đã sửa Day20_DTP_VTP.md")
        return True
        
    except Exception as e:
        print(f"Lỗi khi sửa Day20: {e}")
        return False

def fix_common_issues():
    """Sửa các lỗi phổ biến trong tất cả file"""
    import glob
    
    base_dir = "/home/ubuntu/NEO/Networking fundamentals"
    pattern = os.path.join(base_dir, "Day*.md")
    files = glob.glob(pattern)
    
    fixed_count = 0
    
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Sửa các lỗi phổ biến
            content = re.sub(r'\*\*([^*]+?)\s*:\s*\*\*', r'**\1:**', content)
            content = content.replace('https', 'HTTPS')
            content = content.replace('http', 'HTTP')
            content = content.replace('tcp', 'TCP')
            content = content.replace('udp', 'UDP')
            content = content.replace('ip', 'IP')
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixed_count += 1
                
        except Exception as e:
            print(f"Lỗi khi sửa {os.path.basename(file_path)}: {e}")
    
    print(f"Đã sửa {fixed_count} file với các lỗi phổ biến")

def main():
    print("SỬA CÁC VẤN ĐỀ CỤ THỂ")
    print("=" * 30)
    
    # Sửa file có vấn đề nghiêm trọng
    fix_day15_issues()
    fix_day20_issues()
    
    # Sửa các lỗi phổ biến
    fix_common_issues()
    
    print("\nHoàn thành sửa lỗi!")

if __name__ == "__main__":
    main()
