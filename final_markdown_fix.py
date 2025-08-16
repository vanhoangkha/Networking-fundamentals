#!/usr/bin/env python3
"""
Script sửa lỗi markdown cuối cùng - đảm bảo format hoàn hảo
"""

import os
import re
import glob

def fix_markdown_completely(file_path):
    """Sửa lỗi markdown hoàn toàn"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Lấy thông tin từ tên file
        filename = os.path.basename(file_path)
        day_match = re.match(r'Day(\d+)_(.+)\.md', filename)
        if not day_match:
            return False
        
        day_num = day_match.group(1).zfill(2)
        title_raw = day_match.group(2).replace('_', ' ')
        title = title_raw.upper()
        
        lines = content.split('\n')
        fixed_lines = []
        
        # Header chính
        fixed_lines.append(f"# NGÀY {day_num}: {title}")
        fixed_lines.append("")
        
        section_counter = 1
        subsection_counter = 1
        
        skip_next_empty = False
        
        for i, line in enumerate(lines):
            # Bỏ qua header cũ
            if line.startswith('# NGÀY'):
                continue
            
            # Xử lý headers
            if line.startswith('## '):
                # Lấy nội dung sau ##
                header_content = re.sub(r'^##\s*\d*\.?\d*\s*', '', line).strip()
                if header_content and not header_content.startswith('.'):
                    fixed_lines.append(f"## {day_num}.{section_counter} {header_content}")
                    section_counter += 1
                    subsection_counter = 1
                    skip_next_empty = True
                continue
            
            elif line.startswith('### '):
                # Subsection
                header_content = re.sub(r'^###\s*\d*\.?\d*\.?\d*\s*', '', line).strip()
                if header_content:
                    fixed_lines.append(f"### {day_num}.{section_counter-1}.{subsection_counter} {header_content}")
                    subsection_counter += 1
                    skip_next_empty = True
                continue
            
            # Bỏ qua dòng trống sau header
            if skip_next_empty and line.strip() == '':
                skip_next_empty = False
                continue
            skip_next_empty = False
            
            # Sửa các lỗi khác
            # Sửa bold text bị lỗi
            line = re.sub(r'- \*([^*]+)\*\*', r'**\1**', line)
            
            # Sửa bullet points
            if line.strip().startswith('- '):
                line = re.sub(r'^(\s*)- ', r'\1- ', line)
            
            # Sửa emphasis
            line = re.sub(r'\*\*([^*]+?)\s*:\s*\*\*', r'**\1:**', line)
            
            # Sửa links
            line = line.replace('https://github.com', 'https://github.com')
            
            fixed_lines.append(line)
        
        # Loại bỏ dòng trống thừa
        final_lines = []
        prev_empty = False
        
        for line in fixed_lines:
            if line.strip() == '':
                if not prev_empty:
                    final_lines.append('')
                prev_empty = True
            else:
                final_lines.append(line)
                prev_empty = False
        
        # Loại bỏ dòng trống cuối file
        while final_lines and final_lines[-1] == '':
            final_lines.pop()
        
        # Ghi file
        final_content = '\n'.join(final_lines)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        return True
        
    except Exception as e:
        print(f"Lỗi: {e}")
        return False

def main():
    base_dir = "/home/ubuntu/NEO/Networking fundamentals"
    pattern = os.path.join(base_dir, "Day*.md")
    files = glob.glob(pattern)
    
    print("🔧 SỬA LỖI MARKDOWN CUỐI CÙNG")
    print("=" * 35)
    
    success_count = 0
    for file_path in sorted(files):
        filename = os.path.basename(file_path)
        if fix_markdown_completely(file_path):
            success_count += 1
            print(f"✅ {filename}")
        else:
            print(f"❌ {filename}")
    
    print(f"\n🎉 Hoàn thành! Đã sửa {success_count}/{len(files)} file")

if __name__ == "__main__":
    main()
