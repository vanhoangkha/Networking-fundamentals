#!/usr/bin/env python3
"""
Script sửa lỗi bảng cuối cùng - hoàn thiện tất cả
"""

import os
import re
import glob

def fix_number_format(text):
    """Sửa format số trong bảng"""
    # Sửa các số có dấu phay và chấm lỗi
    text = re.sub(r'1,000,\s*000', '1,000,000', text)
    text = re.sub(r'1,000\.\s*000,000', '1,000,000,000', text)
    text = re.sub(r'1,000,000,\s*000', '1,000,000,000', text)
    text = re.sub(r'(\d+),\s+(\d+)', r'\1,\2', text)  # Loại bỏ space sau dấu phẩy
    text = re.sub(r'(\d+)\.\s+(\d+)', r'\1.\2', text)  # Loại bỏ space sau dấu chấm
    
    return text

def fix_table_content(content):
    """Sửa nội dung bảng"""
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        if '|' in line and not line.strip().startswith('```'):
            # Sửa format số trong dòng bảng
            line = fix_number_format(line)
            
            # Đảm bảo format bảng đúng
            if '|' in line:
                parts = line.split('|')
                cleaned_parts = []
                
                for part in parts:
                    part = part.strip()
                    if part:
                        cleaned_parts.append(part)
                
                if cleaned_parts:
                    # Kiểm tra xem có phải separator không
                    is_separator = all(re.match(r'^[-:\s]*$', part) for part in cleaned_parts)
                    
                    if is_separator:
                        # Tạo separator chuẩn
                        separator_parts = []
                        for part in cleaned_parts:
                            if ':' in part:
                                if part.startswith(':') and part.endswith(':'):
                                    separator_parts.append(':-------:')
                                elif part.endswith(':'):
                                    separator_parts.append('-------:')
                                else:
                                    separator_parts.append(':-------')
                            else:
                                separator_parts.append('-------')
                        line = '| ' + ' | '.join(separator_parts) + ' |'
                    else:
                        # Dòng dữ liệu thường
                        line = '| ' + ' | '.join(cleaned_parts) + ' |'
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def process_file(file_path):
    """Xử lý một file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Sửa bảng
        fixed_content = fix_table_content(content)
        
        # Lưu nếu có thay đổi
        if fixed_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Lỗi: {e}")
        return False

def main():
    base_dir = "/home/ubuntu/NEO/Networking fundamentals"
    pattern = os.path.join(base_dir, "Day*.md")
    files = glob.glob(pattern)
    
    print("🎯 SỬA LỖI BẢNG CUỐI CÙNG")
    print("=" * 30)
    
    fixed_count = 0
    for file_path in sorted(files):
        filename = os.path.basename(file_path)
        if process_file(file_path):
            fixed_count += 1
            print(f"✅ {filename}")
        else:
            print(f"⚪ {filename}")
    
    print(f"\n🎉 Hoàn thành! Đã sửa {fixed_count}/{len(files)} file")

if __name__ == "__main__":
    main()
