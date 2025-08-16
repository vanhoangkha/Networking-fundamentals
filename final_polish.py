#!/usr/bin/env python3
"""
Script tinh chỉnh cuối cùng cho tài liệu CCNA
Sửa các vấn đề còn lại và hoàn thiện định dạng
"""

import os
import re
import glob
from pathlib import Path

def fix_file_formatting(file_path):
    """Sửa các vấn đề định dạng còn lại"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Loại bỏ header trùng lặp
        lines = content.split('\n')
        cleaned_lines = []
        header_found = False
        
        for line in lines:
            # Bỏ qua header trùng lặp
            if line.startswith('# NGÀY') and header_found:
                continue
            elif line.startswith('# NGÀY') and not header_found:
                header_found = True
                cleaned_lines.append(line)
            elif line.startswith('# ') and any(x in line for x in ['1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.']):
                # Bỏ qua header cũ với số
                continue
            else:
                cleaned_lines.append(line)
        
        # Sửa các vấn đề định dạng khác
        content = '\n'.join(cleaned_lines)
        
        # Sửa bullet points
        content = re.sub(r'^•--', '**Đặc điểm:**', content, flags=re.MULTILINE)
        content = re.sub(r'^•', '-', content, flags=re.MULTILINE)
        
        # Sửa HTTPS thành https trong links
        content = content.replace('HTTPS://github.com', 'https://github.com')
        
        # Cải thiện formatting cho bảng
        content = re.sub(r'\|\s*---\s*\|', '|-------|', content)
        
        # Ghi lại file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return True
        
    except Exception as e:
        print(f"Lỗi khi xử lý {file_path}: {e}")
        return False

def main():
    base_dir = "/home/ubuntu/NEO/Networking fundamentals"
    pattern = os.path.join(base_dir, "Day*.md")
    files = glob.glob(pattern)
    
    print("🔧 Đang tinh chỉnh cuối cùng...")
    
    success_count = 0
    for file_path in sorted(files):
        filename = os.path.basename(file_path)
        if fix_file_formatting(file_path):
            success_count += 1
            print(f"✅ {filename}")
        else:
            print(f"❌ {filename}")
    
    print(f"\n🎉 Hoàn thành! Đã tinh chỉnh {success_count}/{len(files)} file")

if __name__ == "__main__":
    main()
