#!/usr/bin/env python3
"""
Script sửa lỗi bảng nâng cao - đảm bảo format hoàn hảo
"""

import os
import re
import glob

def fix_table_advanced(content):
    """Sửa lỗi bảng nâng cao"""
    lines = content.split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Phát hiện bảng
        if '|' in line and not line.strip().startswith('```'):
            # Thu thập tất cả dòng của bảng
            table_lines = []
            j = i
            
            while j < len(lines) and ('|' in lines[j] or lines[j].strip() == ''):
                if '|' in lines[j]:
                    table_lines.append(lines[j])
                j += 1
            
            if len(table_lines) >= 2:
                # Sửa bảng
                fixed_table = fix_single_table(table_lines)
                fixed_lines.extend(fixed_table)
                i = j
            else:
                fixed_lines.append(line)
                i += 1
        else:
            fixed_lines.append(line)
            i += 1
    
    return '\n'.join(fixed_lines)

def fix_single_table(table_lines):
    """Sửa một bảng cụ thể"""
    if not table_lines:
        return table_lines
    
    fixed_table = []
    
    for i, line in enumerate(table_lines):
        # Loại bỏ khoảng trắng đầu cuối
        line = line.strip()
        
        if not line or '|' not in line:
            continue
        
        # Tách cells
        cells = line.split('|')
        
        # Loại bỏ cell trống ở đầu và cuối
        if cells and cells[0].strip() == '':
            cells = cells[1:]
        if cells and cells[-1].strip() == '':
            cells = cells[:-1]
        
        # Làm sạch từng cell
        cleaned_cells = []
        for cell in cells:
            cell = cell.strip()
            # Sửa lỗi spacing trong số
            cell = re.sub(r'(\d+),\s*(\d+)', r'\1,\2', cell)  # 1, 000 -> 1,000
            cell = re.sub(r'(\d+)\.\s*(\d+)', r'\1.\2', cell)  # 802. 3 -> 802.3
            cleaned_cells.append(cell)
        
        # Kiểm tra xem có phải separator không
        is_separator = all(re.match(r'^[-:\s]*$', cell) for cell in cleaned_cells if cell)
        
        if is_separator and i == 1:  # Dòng separator thường là dòng thứ 2
            # Tạo separator chuẩn
            separator_cells = []
            for cell in cleaned_cells:
                if cell:
                    if ':' in cell:
                        if cell.startswith(':') and cell.endswith(':'):
                            separator_cells.append(':-------:')
                        elif cell.endswith(':'):
                            separator_cells.append('-------:')
                        else:
                            separator_cells.append(':-------')
                    else:
                        separator_cells.append('-------')
                else:
                    separator_cells.append('-------')
            
            fixed_line = '| ' + ' | '.join(separator_cells) + ' |'
        else:
            # Dòng dữ liệu
            fixed_line = '| ' + ' | '.join(cleaned_cells) + ' |'
        
        fixed_table.append(fixed_line)
    
    return fixed_table

def process_file(file_path):
    """Xử lý một file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Sửa bảng
        fixed_content = fix_table_advanced(content)
        
        # Lưu nếu có thay đổi
        if fixed_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Lỗi khi xử lý {file_path}: {e}")
        return False

def main():
    base_dir = "/home/ubuntu/NEO/Networking fundamentals"
    pattern = os.path.join(base_dir, "Day*.md")
    files = glob.glob(pattern)
    
    print("🔧 SỬA LỖI BẢNG NÂNG CAO")
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
