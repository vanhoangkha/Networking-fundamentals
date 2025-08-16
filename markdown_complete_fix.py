#!/usr/bin/env python3
"""
Script sửa lỗi markdown hoàn toàn - khôi phục từ backup và format lại
"""

import os
import re
import glob
from pathlib import Path

def restore_and_fix_file(file_path):
    """Khôi phục từ backup và format lại đúng chuẩn"""
    backup_path = file_path + '.backup'
    
    if not os.path.exists(backup_path):
        print(f"❌ Không tìm thấy backup cho {os.path.basename(file_path)}")
        return False
    
    try:
        # Đọc file backup
        with open(backup_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Lấy thông tin ngày từ tên file
        filename = os.path.basename(file_path)
        day_match = re.match(r'Day(\d+)_(.+)\.md', filename)
        if not day_match:
            return False
        
        day_num = day_match.group(1).zfill(2)
        title_raw = day_match.group(2).replace('_', ' ')
        
        # Tạo tiêu đề chuẩn
        title = title_raw.upper()
        
        # Xử lý nội dung
        lines = content.split('\n')
        processed_lines = []
        
        # Thêm header chuẩn
        processed_lines.append(f"# NGÀY {day_num}: {title}")
        processed_lines.append("")
        
        section_num = 1
        subsection_num = 1
        
        for line in lines:
            # Bỏ qua header cũ
            if line.startswith('# ') and any(x in line.lower() for x in ['ngày', 'day', str(int(day_num))]):
                continue
            
            # Xử lý headers
            if line.startswith('##'):
                # Main section
                clean_title = re.sub(r'^#+\s*\d*\.?\d*\s*', '', line).strip()
                if clean_title:
                    processed_lines.append(f"## {day_num}.{section_num} {clean_title}")
                    section_num += 1
                    subsection_num = 1
            elif line.startswith('###'):
                # Subsection
                clean_title = re.sub(r'^#+\s*\d*\.?\d*\.?\d*\s*', '', line).strip()
                if clean_title:
                    processed_lines.append(f"### {day_num}.{section_num-1}.{subsection_num} {clean_title}")
                    subsection_num += 1
            else:
                # Xử lý nội dung thường
                # Sửa bullet points
                if re.match(r'^\s*[•*-]\s*', line):
                    line = re.sub(r'^\s*[•*-]\s*', '- ', line)
                
                # Sửa bold text
                line = re.sub(r'\*\*([^*]+?)\s*:\s*\*\*', r'**\1:**', line)
                
                # Sửa links
                line = line.replace('HTTPS://', 'https://')
                
                processed_lines.append(line)
        
        # Loại bỏ dòng trống thừa
        final_lines = []
        prev_empty = False
        
        for line in processed_lines:
            if line.strip() == '':
                if not prev_empty:
                    final_lines.append('')
                prev_empty = True
            else:
                final_lines.append(line)
                prev_empty = False
        
        # Ghi file mới
        final_content = '\n'.join(final_lines)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        return True
        
    except Exception as e:
        print(f"❌ Lỗi khi xử lý {filename}: {e}")
        return False

def main():
    base_dir = "/home/ubuntu/NEO/Networking fundamentals"
    pattern = os.path.join(base_dir, "Day*.md")
    files = glob.glob(pattern)
    
    print("🔄 KHÔI PHỤC VÀ SỬA LỖI MARKDOWN HOÀN TOÀN")
    print("=" * 50)
    
    success_count = 0
    for file_path in sorted(files):
        filename = os.path.basename(file_path)
        if restore_and_fix_file(file_path):
            success_count += 1
            print(f"✅ {filename}")
        else:
            print(f"❌ {filename}")
    
    print(f"\n🎉 Hoàn thành! Đã sửa {success_count}/{len(files)} file")

if __name__ == "__main__":
    main()
