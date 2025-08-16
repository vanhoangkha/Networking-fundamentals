#!/usr/bin/env python3
"""
Script sửa lỗi định dạng markdown cho tài liệu CCNA
Đảm bảo markdown syntax đúng chuẩn
"""

import os
import re
import glob
from pathlib import Path

class MarkdownFixer:
    def __init__(self):
        self.fixes_applied = []
        
    def fix_headers(self, content):
        """Sửa lỗi headers markdown"""
        lines = content.split('\n')
        fixed_lines = []
        
        for line in lines:
            original_line = line
            
            # Sửa headers không có space sau #
            if re.match(r'^#+[^#\s]', line):
                line = re.sub(r'^(#+)([^#\s])', r'\1 \2', line)
                self.fixes_applied.append(f"Header spacing: '{original_line}' → '{line}'")
            
            # Sửa headers trùng lặp hoặc sai format
            if re.match(r'^## \d+\.\d+ (.+)', line):
                match = re.match(r'^## \d+\.\d+ (.+)', line)
                if match:
                    line = f"## {match.group(1)}"
                    self.fixes_applied.append(f"Header format: '{original_line}' → '{line}'")
            
            # Sửa headers với số thừa
            if re.match(r'^### \d+\.\d+\.\d+ (.+)', line):
                match = re.match(r'^### \d+\.\d+\.\d+ (.+)', line)
                if match:
                    line = f"### {match.group(1)}"
                    self.fixes_applied.append(f"Subheader format: '{original_line}' → '{line}'")
            
            fixed_lines.append(line)
        
        return '\n'.join(fixed_lines)
    
    def fix_lists(self, content):
        """Sửa lỗi lists markdown"""
        lines = content.split('\n')
        fixed_lines = []
        
        for line in lines:
            original_line = line
            
            # Chuẩn hóa bullet points
            if re.match(r'^\s*[•*]\s*', line):
                # Thay thế bullet points thành dấu gạch ngang
                line = re.sub(r'^\s*[•*]\s*', '- ', line)
                self.fixes_applied.append(f"Bullet point: '{original_line}' → '{line}'")
            
            # Sửa spacing trong lists
            if re.match(r'^-\s{2,}', line):
                line = re.sub(r'^-\s{2,}', '- ', line)
                self.fixes_applied.append(f"List spacing: '{original_line}' → '{line}'")
            
            fixed_lines.append(line)
        
        return '\n'.join(fixed_lines)
    
    def fix_emphasis(self, content):
        """Sửa lỗi emphasis (bold, italic)"""
        original_content = content
        
        # Sửa bold text
        content = re.sub(r'\*\*([^*]+?)\s*:\s*\*\*', r'**\1:**', content)
        
        # Sửa italic text
        content = re.sub(r'\*([^*]+?)\*', r'*\1*', content)
        
        # Sửa code inline
        content = re.sub(r'`([^`]+?)`', r'`\1`', content)
        
        if content != original_content:
            self.fixes_applied.append("Fixed emphasis formatting")
        
        return content
    
    def fix_links_images(self, content):
        """Sửa lỗi links và images"""
        original_content = content
        
        # Sửa image links
        content = re.sub(r'!\[image\]\(HTTPS://', r'![image](https://', content)
        
        # Sửa broken links
        content = re.sub(r'\[([^\]]+)\]\(\s*([^)]+)\s*\)', r'[\1](\2)', content)
        
        if content != original_content:
            self.fixes_applied.append("Fixed links and images")
        
        return content
    
    def fix_tables(self, content):
        """Sửa lỗi tables markdown"""
        lines = content.split('\n')
        fixed_lines = []
        in_table = False
        
        for i, line in enumerate(lines):
            original_line = line
            
            # Detect table
            if '|' in line and not line.strip().startswith('```'):
                in_table = True
                
                # Sửa table formatting
                if re.match(r'^\s*\|.*\|\s*$', line):
                    # Đảm bảo có space quanh |
                    line = re.sub(r'\s*\|\s*', ' | ', line)
                    line = line.strip()
                    
                    # Đảm bảo bắt đầu và kết thúc bằng |
                    if not line.startswith('|'):
                        line = '| ' + line
                    if not line.endswith('|'):
                        line = line + ' |'
                    
                    if line != original_line:
                        self.fixes_applied.append(f"Table format: '{original_line}' → '{line}'")
                
                # Sửa table separator
                elif re.match(r'^\s*\|[\s\-\|]+\|\s*$', line):
                    parts = line.split('|')
                    separator_parts = []
                    for part in parts:
                        if part.strip():
                            if '-' in part:
                                separator_parts.append('-------')
                            else:
                                separator_parts.append('')
                    
                    if separator_parts:
                        line = '| ' + ' | '.join(separator_parts) + ' |'
                        if line != original_line:
                            self.fixes_applied.append(f"Table separator: '{original_line}' → '{line}'")
            else:
                in_table = False
            
            fixed_lines.append(line)
        
        return '\n'.join(fixed_lines)
    
    def fix_code_blocks(self, content):
        """Sửa lỗi code blocks"""
        original_content = content
        
        # Sửa code blocks không đóng
        content = re.sub(r'^```([^`\n]*)\n(.*?)\n```', r'```\1\n\2\n```', content, flags=re.MULTILINE | re.DOTALL)
        
        if content != original_content:
            self.fixes_applied.append("Fixed code blocks")
        
        return content
    
    def fix_spacing(self, content):
        """Sửa lỗi spacing"""
        lines = content.split('\n')
        fixed_lines = []
        prev_empty = False
        
        for line in lines:
            # Loại bỏ trailing spaces
            line = line.rstrip()
            
            # Kiểm soát empty lines
            if line.strip() == '':
                if not prev_empty:
                    fixed_lines.append('')
                prev_empty = True
            else:
                fixed_lines.append(line)
                prev_empty = False
        
        # Loại bỏ empty lines ở cuối
        while fixed_lines and fixed_lines[-1] == '':
            fixed_lines.pop()
        
        result = '\n'.join(fixed_lines)
        
        if result != content:
            self.fixes_applied.append("Fixed spacing and empty lines")
        
        return result
    
    def fix_file(self, file_path):
        """Sửa một file markdown"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            self.fixes_applied = []
            
            # Áp dụng các fixes
            content = self.fix_headers(content)
            content = self.fix_lists(content)
            content = self.fix_emphasis(content)
            content = self.fix_links_images(content)
            content = self.fix_tables(content)
            content = self.fix_code_blocks(content)
            content = self.fix_spacing(content)
            
            # Lưu file nếu có thay đổi
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                return {
                    'file': os.path.basename(file_path),
                    'fixes': self.fixes_applied,
                    'changed': True
                }
            else:
                return {
                    'file': os.path.basename(file_path),
                    'fixes': [],
                    'changed': False
                }
                
        except Exception as e:
            return {
                'file': os.path.basename(file_path),
                'error': str(e),
                'changed': False
            }

def main():
    fixer = MarkdownFixer()
    base_dir = "/home/ubuntu/NEO/Networking fundamentals"
    pattern = os.path.join(base_dir, "Day*.md")
    files = glob.glob(pattern)
    
    print("🔧 SỬA LỖI ĐỊNH DẠNG MARKDOWN")
    print("=" * 40)
    
    total_files = len(files)
    files_fixed = 0
    total_fixes = 0
    
    results = []
    
    for file_path in sorted(files):
        result = fixer.fix_file(file_path)
        results.append(result)
        
        if result.get('changed'):
            files_fixed += 1
            fix_count = len(result.get('fixes', []))
            total_fixes += fix_count
            print(f"🔧 {result['file']}: {fix_count} lỗi đã sửa")
            
            # Hiển thị một vài fixes đầu tiên
            for fix in result.get('fixes', [])[:3]:
                print(f"   - {fix}")
            if len(result.get('fixes', [])) > 3:
                print(f"   - ... và {len(result.get('fixes', [])) - 3} lỗi khác")
        
        elif result.get('error'):
            print(f"❌ {result['file']}: Lỗi - {result['error']}")
        else:
            print(f"✅ {result['file']}: Markdown đã chuẩn")
    
    # Tạo báo cáo
    report_path = os.path.join(base_dir, "MARKDOWN_FIX_REPORT.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# BÁO CÁO SỬA LỖI MARKDOWN\n\n")
        f.write(f"**Ngày sửa**: {os.popen('date').read().strip()}\n\n")
        f.write("## Tổng kết\n\n")
        f.write(f"- **Tổng số file**: {total_files}\n")
        f.write(f"- **File đã sửa**: {files_fixed}\n")
        f.write(f"- **Tổng lỗi đã sửa**: {total_fixes}\n\n")
        
        f.write("## Chi tiết từng file\n\n")
        for result in results:
            f.write(f"### {result['file']}\n\n")
            
            if result.get('error'):
                f.write(f"❌ **Lỗi**: {result['error']}\n\n")
                continue
            
            if result.get('fixes'):
                f.write("**Lỗi đã sửa:**\n")
                for fix in result['fixes']:
                    f.write(f"- {fix}\n")
                f.write("\n")
            else:
                f.write("✅ Markdown đã chuẩn\n\n")
    
    print("\n" + "=" * 40)
    print("📊 TỔNG KẾT SỬA LỖI MARKDOWN:")
    print(f"✅ Đã kiểm tra: {total_files} file")
    print(f"🔧 Đã sửa: {files_fixed} file")
    print(f"🛠️  Tổng lỗi đã sửa: {total_fixes}")
    print(f"📋 Báo cáo chi tiết: MARKDOWN_FIX_REPORT.md")

if __name__ == "__main__":
    main()
