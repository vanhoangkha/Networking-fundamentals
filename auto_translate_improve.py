#!/usr/bin/env python3
"""
Script tự động cải thiện chất lượng dịch thuật cho tài liệu CCNA
Chuẩn hóa thuật ngữ kỹ thuật và định dạng theo chuẩn tài liệu đào tạo
"""

import os
import re
import glob
from pathlib import Path

class CCNATranslationImprover:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.processed_files = []
        
        # Từ điển thuật ngữ chuẩn hóa
        self.terminology_dict = {
            # Thiết bị mạng
            "switch": "switch",
            "router": "router", 
            "firewall": "tường lửa",
            "hub": "hub",
            
            # Giao thức
            "TCP": "TCP",
            "UDP": "UDP", 
            "IP": "IP",
            "HTTP": "HTTP",
            "HTTPS": "HTTPS",
            "FTP": "FTP",
            "SMTP": "SMTP",
            "DNS": "DNS",
            "DHCP": "DHCP",
            
            # Mô hình OSI
            "Physical Layer": "Tầng Vật lý",
            "Data Link Layer": "Tầng Liên kết dữ liệu", 
            "Network Layer": "Tầng Mạng",
            "Transport Layer": "Tầng Vận chuyển",
            "Session Layer": "Tầng Phiên",
            "Presentation Layer": "Tầng Trình bày",
            "Application Layer": "Tầng Ứng dụng",
            
            # Các khái niệm mạng
            "LAN": "LAN (Local Area Network)",
            "WAN": "WAN (Wide Area Network)",
            "VLAN": "VLAN",
            "subnet": "mạng con",
            "subnetting": "chia mạng con",
            "routing": "định tuyến",
            "switching": "chuyển mạch",
            
            # Cáp và kết nối
            "UTP": "UTP (Unshielded Twisted Pair)",
            "STP": "STP (Shielded Twisted Pair)",
            "fiber optic": "cáp quang",
            "ethernet": "Ethernet",
            
            # CLI và cấu hình
            "CLI": "CLI (Command Line Interface)",
            "GUI": "GUI (Graphical User Interface)",
            "running-config": "running-config",
            "startup-config": "startup-config",
        }
        
    def improve_file_structure(self, content, day_number, title):
        """Cải thiện cấu trúc file theo chuẩn tài liệu đào tạo"""
        
        # Tạo header chuẩn
        header = f"# NGÀY {day_number}: {title.upper()}\n\n"
        
        # Xử lý nội dung
        lines = content.split('\n')
        improved_lines = []
        section_counter = 1
        subsection_counter = 1
        
        for line in lines:
            # Bỏ qua header cũ
            if line.startswith('# ') and any(x in line.lower() for x in ['ngày', 'day']):
                continue
                
            # Cải thiện heading structure
            if line.startswith('##'):
                line = f"## {day_number}.{section_counter} " + line[2:].strip()
                section_counter += 1
                subsection_counter = 1
            elif line.startswith('###'):
                line = f"### {day_number}.{section_counter-1}.{subsection_counter} " + line[3:].strip()
                subsection_counter += 1
                
            # Cải thiện formatting
            line = self.improve_formatting(line)
            improved_lines.append(line)
            
        return header + '\n'.join(improved_lines)
    
    def improve_formatting(self, line):
        """Cải thiện định dạng văn bản"""
        
        # Chuẩn hóa thuật ngữ
        for en_term, vi_term in self.terminology_dict.items():
            line = re.sub(rf'\b{re.escape(en_term)}\b', vi_term, line, flags=re.IGNORECASE)
            
        # Cải thiện bullet points
        if line.strip().startswith('-'):
            line = line.replace('-', '•', 1)
            
        # Cải thiện emphasis
        line = re.sub(r'\*\*(.*?)\*\*', r'**\1**', line)  # Bold
        line = re.sub(r'\*(.*?)\*', r'*\1*', line)        # Italic
        
        # Cải thiện code blocks
        if '`' in line and not line.strip().startswith('```'):
            line = re.sub(r'`([^`]+)`', r'`\1`', line)
            
        return line
    
    def extract_day_info(self, filename):
        """Trích xuất thông tin ngày và tiêu đề từ tên file"""
        match = re.match(r'Day(\d+)_(.+)\.md', filename)
        if match:
            day_num = match.group(1).zfill(2)
            title = match.group(2).replace('_', ' ')
            return day_num, title
        return None, None
    
    def process_file(self, file_path):
        """Xử lý một file cụ thể"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            filename = os.path.basename(file_path)
            day_num, title = self.extract_day_info(filename)
            
            if not day_num or not title:
                print(f"Không thể xác định thông tin ngày cho file: {filename}")
                return False
                
            # Cải thiện nội dung
            improved_content = self.improve_file_structure(content, day_num, title)
            
            # Tạo backup
            backup_path = file_path + '.backup'
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            # Ghi file đã cải thiện
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(improved_content)
                
            self.processed_files.append(filename)
            print(f"✅ Đã cải thiện: {filename}")
            return True
            
        except Exception as e:
            print(f"❌ Lỗi khi xử lý {filename}: {str(e)}")
            return False
    
    def process_all_files(self):
        """Xử lý tất cả các file Day*.md"""
        pattern = str(self.base_dir / "Day*.md")
        files = glob.glob(pattern)
        files.sort()
        
        print(f"Tìm thấy {len(files)} file cần xử lý...")
        
        success_count = 0
        for file_path in files:
            if self.process_file(file_path):
                success_count += 1
                
        print(f"\n📊 Kết quả:")
        print(f"✅ Thành công: {success_count}/{len(files)} file")
        print(f"📝 Danh sách file đã xử lý:")
        for filename in self.processed_files:
            print(f"   - {filename}")
            
    def create_progress_report(self):
        """Tạo báo cáo tiến độ"""
        report_path = self.base_dir / "TRANSLATION_PROGRESS.md"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("# BÁO CÁO TIẾN ĐỘ DỊCH THUẬT VÀ CẢI THIỆN\n\n")
            f.write(f"**Ngày cập nhật**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Tổng số file đã xử lý**: {len(self.processed_files)}\n\n")
            f.write("## Danh sách file đã cải thiện:\n\n")
            
            for i, filename in enumerate(self.processed_files, 1):
                f.write(f"{i}. {filename}\n")
                
            f.write("\n## Các cải thiện đã thực hiện:\n\n")
            f.write("- ✅ Chuẩn hóa cấu trúc tiêu đề\n")
            f.write("- ✅ Cải thiện định dạng văn bản\n") 
            f.write("- ✅ Chuẩn hóa thuật ngữ kỹ thuật\n")
            f.write("- ✅ Tối ưu hóa bố cục nội dung\n")
            f.write("- ✅ Tạo backup cho tất cả file gốc\n")

if __name__ == "__main__":
    import datetime
    
    # Khởi tạo và chạy
    base_directory = "/home/ubuntu/NEO/Networking fundamentals"
    improver = CCNATranslationImprover(base_directory)
    
    print("🚀 Bắt đầu quá trình cải thiện tài liệu CCNA...")
    print("=" * 50)
    
    improver.process_all_files()
    improver.create_progress_report()
    
    print("\n🎉 Hoàn thành quá trình cải thiện!")
    print("📋 Đã tạo báo cáo tiến độ: TRANSLATION_PROGRESS.md")
