#!/usr/bin/env python3
"""
Script kiểm tra và sửa định dạng bảng trong tài liệu CCNA
Đảm bảo tất cả bảng tuân thủ chuẩn markdown
"""

import os
import re
import glob
from pathlib import Path

class TableFormatChecker:
    def __init__(self):
        self.fixes_applied = []
        self.tables_found = 0
        self.tables_fixed = 0
        
    def detect_tables(self, content):
        """Phát hiện các bảng trong nội dung"""
        lines = content.split('\n')
        tables = []
        current_table = []
        in_table = False
        
        for i, line in enumerate(lines):
            # Phát hiện dòng có ký tự |
            if '|' in line and not line.strip().startswith('```'):
                if not in_table:
                    in_table = True
                    current_table = []
                current_table.append((i, line))
            else:
                if in_table and current_table:
                    tables.append(current_table)
                    current_table = []
                in_table = False
        
        # Thêm bảng cuối nếu có
        if current_table:
            tables.append(current_table)
            
        return tables
    
    def fix_table_format(self, table_lines):
        """Sửa định dạng một bảng"""
        if not table_lines:
            return table_lines
        
        fixed_lines = []
        
        for line_num, line in table_lines:
            original_line = line
            
            # Loại bỏ khoảng trắng đầu cuối
            line = line.strip()
            
            # Đảm bảo bảng bắt đầu và kết thúc bằng |
            if line and '|' in line:
                # Tách các cell
                cells = line.split('|')
                
                # Loại bỏ cell trống ở đầu và cuối nếu có
                if cells and cells[0].strip() == '':
                    cells = cells[1:]
                if cells and cells[-1].strip() == '':
                    cells = cells[:-1]
                
                # Làm sạch từng cell
                cleaned_cells = []
                for cell in cells:
                    cell = cell.strip()
                    cleaned_cells.append(cell)
                
                # Kiểm tra xem có phải dòng separator không
                is_separator = all(re.match(r'^[-:\s]*$', cell) for cell in cleaned_cells if cell)
                
                if is_separator:
                    # Tạo separator chuẩn
                    separator_cells = []
                    for cell in cleaned_cells:
                        if cell:
                            if ':' in cell:
                                if cell.startswith(':') and cell.endswith(':'):
                                    separator_cells.append(':-------:')  # Center align
                                elif cell.endswith(':'):
                                    separator_cells.append('-------:')   # Right align
                                else:
                                    separator_cells.append(':-------')   # Left align
                            else:
                                separator_cells.append('-------')       # Default
                        else:
                            separator_cells.append('-------')
                    
                    line = '| ' + ' | '.join(separator_cells) + ' |'
                else:
                    # Dòng dữ liệu thường
                    line = '| ' + ' | '.join(cleaned_cells) + ' |'
                
                if line != original_line:
                    self.fixes_applied.append(f"Dòng {line_num + 1}: Sửa format bảng")
            
            fixed_lines.append((line_num, line))
        
        return fixed_lines
    
    def fix_file_tables(self, file_path):
        """Sửa tất cả bảng trong một file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            self.fixes_applied = []
            
            # Phát hiện bảng
            tables = self.detect_tables(content)
            self.tables_found += len(tables)
            
            if not tables:
                return {
                    'file': os.path.basename(file_path),
                    'tables_found': 0,
                    'tables_fixed': 0,
                    'fixes': [],
                    'changed': False
                }
            
            # Sửa từng bảng
            lines = content.split('\n')
            tables_fixed_count = 0
            
            for table in tables:
                fixed_table = self.fix_table_format(table)
                
                # Thay thế các dòng đã sửa
                table_changed = False
                for (line_num, new_line), (orig_line_num, orig_line) in zip(fixed_table, table):
                    if new_line != orig_line:
                        lines[line_num] = new_line
                        table_changed = True
                
                if table_changed:
                    tables_fixed_count += 1
            
            self.tables_fixed += tables_fixed_count
            
            # Tạo nội dung mới
            new_content = '\n'.join(lines)
            
            # Lưu file nếu có thay đổi
            if new_content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                return {
                    'file': os.path.basename(file_path),
                    'tables_found': len(tables),
                    'tables_fixed': tables_fixed_count,
                    'fixes': self.fixes_applied,
                    'changed': True
                }
            else:
                return {
                    'file': os.path.basename(file_path),
                    'tables_found': len(tables),
                    'tables_fixed': 0,
                    'fixes': [],
                    'changed': False
                }
                
        except Exception as e:
            return {
                'file': os.path.basename(file_path),
                'error': str(e),
                'changed': False
            }
    
    def validate_table_structure(self, table_lines):
        """Kiểm tra cấu trúc bảng có hợp lệ không"""
        if len(table_lines) < 2:
            return False, "Bảng cần ít nhất 2 dòng (header + separator)"
        
        # Kiểm tra dòng đầu (header)
        header_line = table_lines[0][1]
        header_cells = len([cell for cell in header_line.split('|') if cell.strip()])
        
        # Kiểm tra dòng thứ 2 (separator)
        separator_line = table_lines[1][1]
        separator_cells = len([cell for cell in separator_line.split('|') if cell.strip()])
        
        if header_cells != separator_cells:
            return False, f"Số cột không khớp: header có {header_cells}, separator có {separator_cells}"
        
        # Kiểm tra các dòng dữ liệu
        for i, (line_num, line) in enumerate(table_lines[2:], 2):
            data_cells = len([cell for cell in line.split('|') if cell.strip()])
            if data_cells != header_cells:
                return False, f"Dòng {i+1} có {data_cells} cột, khác với header ({header_cells} cột)"
        
        return True, "Cấu trúc bảng hợp lệ"

def main():
    checker = TableFormatChecker()
    base_dir = "/home/ubuntu/NEO/Networking fundamentals"
    pattern = os.path.join(base_dir, "Day*.md")
    files = glob.glob(pattern)
    
    print("📊 KIỂM TRA VÀ SỬA ĐỊNH DẠNG BẢNG")
    print("=" * 45)
    
    total_files = len(files)
    files_with_tables = 0
    files_fixed = 0
    
    results = []
    
    for file_path in sorted(files):
        result = checker.fix_file_tables(file_path)
        results.append(result)
        
        filename = result['file']
        
        if result.get('error'):
            print(f"❌ {filename}: Lỗi - {result['error']}")
        elif result.get('tables_found', 0) > 0:
            files_with_tables += 1
            tables_found = result.get('tables_found', 0)
            tables_fixed = result.get('tables_fixed', 0)
            
            if result.get('changed'):
                files_fixed += 1
                print(f"🔧 {filename}: {tables_found} bảng, {tables_fixed} đã sửa")
            else:
                print(f"✅ {filename}: {tables_found} bảng, đã chuẩn")
        else:
            print(f"⚪ {filename}: Không có bảng")
    
    # Tạo báo cáo
    report_path = os.path.join(base_dir, "TABLE_FORMAT_REPORT.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# BÁO CÁO KIỂM TRA ĐỊNH DẠNG BẢNG\n\n")
        f.write(f"**Ngày kiểm tra**: {os.popen('date').read().strip()}\n\n")
        f.write("## Tổng kết\n\n")
        f.write(f"- **Tổng số file**: {total_files}\n")
        f.write(f"- **File có bảng**: {files_with_tables}\n")
        f.write(f"- **File đã sửa**: {files_fixed}\n")
        f.write(f"- **Tổng bảng tìm thấy**: {checker.tables_found}\n")
        f.write(f"- **Tổng bảng đã sửa**: {checker.tables_fixed}\n\n")
        
        f.write("## Chi tiết từng file\n\n")
        for result in results:
            f.write(f"### {result['file']}\n\n")
            
            if result.get('error'):
                f.write(f"❌ **Lỗi**: {result['error']}\n\n")
                continue
            
            tables_found = result.get('tables_found', 0)
            if tables_found == 0:
                f.write("⚪ Không có bảng\n\n")
                continue
            
            tables_fixed = result.get('tables_fixed', 0)
            f.write(f"**Bảng tìm thấy**: {tables_found}\n")
            f.write(f"**Bảng đã sửa**: {tables_fixed}\n")
            
            if result.get('fixes'):
                f.write("**Chi tiết sửa chữa:**\n")
                for fix in result['fixes'][:10]:  # Chỉ hiển thị 10 fix đầu
                    f.write(f"- {fix}\n")
                if len(result['fixes']) > 10:
                    f.write(f"- ... và {len(result['fixes']) - 10} sửa chữa khác\n")
            else:
                f.write("✅ Tất cả bảng đã đúng định dạng\n")
            
            f.write("\n")
    
    print("\n" + "=" * 45)
    print("📊 TỔNG KẾT KIỂM TRA BẢNG:")
    print(f"✅ Đã kiểm tra: {total_files} file")
    print(f"📊 File có bảng: {files_with_tables} file")
    print(f"🔧 File đã sửa: {files_fixed} file")
    print(f"📋 Tổng bảng: {checker.tables_found}")
    print(f"🛠️  Bảng đã sửa: {checker.tables_fixed}")
    print(f"📄 Báo cáo chi tiết: TABLE_FORMAT_REPORT.md")

if __name__ == "__main__":
    main()
