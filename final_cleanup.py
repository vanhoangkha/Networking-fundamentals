#!/usr/bin/env python3
"""
Script dọn dẹp cuối cùng để sửa các vấn đề format
"""

import os
import re
import glob

def clean_file(file_path):
    """Dọn dẹp format file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Sửa các vấn đề format
        lines = content.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Loại bỏ heading trùng lặp và sai format
            if re.match(r'^## \d+\.\d+ # \d+\.\d+', line):
                # Lấy phần sau dấu # cuối cùng
                parts = line.split('# ')
                if len(parts) > 1:
                    line = '## ' + parts[-1]
            
            # Sửa heading bị lỗi
            line = re.sub(r'^## \d+\.\d+ (.+)', r'## \1', line)
            line = re.sub(r'^# (\d+\.\d+\.\d+) (.+)', r'### \1 \2', line)
            
            # Sửa các vấn đề khác
            line = re.sub(r'\*\*(.+?): \*\*', r'**\1:**', line)  # Sửa bold với dấu hai chấm
            line = re.sub(r' - to - ', ' - ', line)  # Sửa dấu gạch ngang
            line = re.sub(r'\((.+?)\) \(\1\)', r'(\1)', line)  # Loại bỏ lặp trong ngoặc
            
            cleaned_lines.append(line)
        
        # Loại bỏ dòng trống thừa
        final_lines = []
        prev_empty = False
        
        for line in cleaned_lines:
            if line.strip() == '':
                if not prev_empty:
                    final_lines.append(line)
                prev_empty = True
            else:
                final_lines.append(line)
                prev_empty = False
        
        content = '\n'.join(final_lines)
        
        # Lưu file nếu có thay đổi
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Lỗi khi xử lý {file_path}: {e}")
        return False

def main():
    base_dir = "/home/ubuntu/NEO/Networking fundamentals"
    pattern = os.path.join(base_dir, "Day*.md")
    files = glob.glob(pattern)
    
    print("🧹 DỌNG DẸP CUỐI CÙNG")
    print("=" * 30)
    
    fixed_count = 0
    for file_path in sorted(files):
        filename = os.path.basename(file_path)
        if clean_file(file_path):
            print(f"✅ {filename}")
            fixed_count += 1
        else:
            print(f"⚪ {filename}")
    
    print(f"\n🎉 Hoàn thành! Đã sửa {fixed_count}/{len(files)} file")

if __name__ == "__main__":
    main()
