# 5. CHUYỂN MẠCH ETHERNET LAN: PHẦN 1

![image](https://github.com/psaumur/CCNA/assets/106411237/a40e81d9-c008-4fb4-8580-2eaf63003e63)

![image](https://github.com/psaumur/CCNA/assets/106411237/2db46525-98b8-4211-aeb3-efc34bd84222)

LAN

- LAN là một Mạng được chứa trong một khu vực tương đối nhỏ.
- Router được sử dụng để kết nối các LAN riêng biệt

![image](https://github.com/psaumur/CCNA/assets/106411237/2a4de9d4-3408-49b9-9492-42b7eb56fe27)

Một Khung Ethernet trông như:

![image](https://github.com/psaumur/CCNA/assets/106411237/ad579917-f9a0-4cd8-be25-351ecbfc87af)

Trailer Ethernet --- Gói tin --- Header Ethernet

Header Ethernet chứa 5 Trường:

Preamble -- SFD -- Đích -- Nguồn -- Loại
7 byte   -- 1 byte -- 6 byte -- 6 byte -- 2 byte

---

PREAMBLE:

- Độ dài: 7 byte (56 bit)
- Xen kẽ số 1 và số 0
- 10101010 * 7 lần
- Cho phép các thiết bị đồng bộ hóa đồng hồ máy thu của chúng

SFD: 'Bộ Phân Cách Bắt Đầu Khung' (Start Frame Delimiter)

- Độ dài: 1 byte (8 bit)
- 10101011
- Đánh dấu kết thúc PREAMBLE và bắt đầu PHẦN CÒN LẠI của Khung.

---

ĐÍCH VÀ NGUỒN

- Địa chỉ Tầng 2
- Chỉ ra các thiết bị gửi/nhận Khung
- MAC = 'Kiểm Soát Truy Cập Phương Tiện' (Media Access Control)
- = Địa chỉ 6 byte (48-bit) của thiết bị vật lý

---

LOẠI / ĐỘ DÀI

- Trường 2 byte (16-bit)
- Giá trị **1500 hoặc nhỏ hơn** trong trường này chỉ ra ĐỘ DÀI của Gói tin được đóng gói (tính bằng byte)
- Giá trị **1536 hoặc lớn hơn** trong trường này chỉ ra LOẠI của Gói tin được đóng gói và độ dài được xác định qua các phương pháp khác.
- IPv4 = 0x0800 (thập lục phân) = 2048 trong thập phân
- IPv6 = 0x86DD (thập lục phân) = 34525 trong thập phân
- Giao thức Tầng 3 được sử dụng trong Gói tin được đóng gói, hầu như luôn là Giao thức Internet (IP) phiên bản 4 hoặc phiên bản 6.

---

Trailer Ethernet chứa:

FCS

- 'CHUỖI KIỂM TRA KHUNG' (Frame Check Sequence)
- Dài 4 byte (32 bit)
- Phát hiện dữ liệu bị hỏng bằng cách chạy thuật toán 'CRC' trên dữ liệu nhận được
- CRC = "Kiểm Tra Dư Thừa Vòng" (Cyclic Redundancy Check)

---

Tổng cộng Khung Ethernet = 26 byte (Header + Trailer)

![image](https://github.com/psaumur/CCNA/assets/106411237/c8c1a143-0675-4aa4-83bc-6031d10cc0b8)

---

Địa chỉ MAC (dài 48 bit)

- Địa chỉ vật lý 6-byte (48-bit) được gán cho thiết bị khi nó được sản xuất.
- Còn gọi là 'Địa chỉ Được Ghi Sẵn' (Burned-In Address - BIA)
- Là duy nhất toàn cầu
- 3 byte đầu là OUI (Định danh Duy nhất Tổ chức) được gán cho công ty sản xuất thiết bị
- 3 byte cuối là duy nhất cho chính thiết bị đó
- Được viết dưới dạng 12 ký tự thập lục phân

Ví dụ:

E8:BA:70 // 11:28:74
OUI      // ID Thiết bị Duy nhất

THẬP LỤC PHÂN

![image](https://github.com/psaumur/CCNA/assets/106411237/65a5e84a-b8db-46f5-b288-518139e99453)

TÊN GIAO DIỆN

F0/1, F0/2, F0/3... F viết tắt của "Fast Ethernet" hoặc giao diện 100 Mbps.

---

BẢNG ĐỊA CHỈ MAC

Mỗi Switch lưu trữ một BẢNG ĐỊA CHỈ MAC HỌC ĐỘNG, sử dụng Địa chỉ MAC NGUỒN của các khung mà nó nhận được.

![image](https://github.com/psaumur/CCNA/assets/106411237/582421a9-6351-48b7-bfe1-c2153520920c)

Khi Switch không biết Địa chỉ MAC ĐÍCH của một Khung (Khung Unicast KHÔNG BIẾT), nó buộc phải FLOOD khung - Chuyển tiếp khung ra khỏi TẤT CẢ các giao diện của nó, ngoại trừ giao diện mà nó nhận Gói tin.

Khi một Khung Unicast ĐÃ BIẾT được biết (Địa chỉ MAC được nhận dạng bởi mục trong BẢNG ĐỊA CHỈ MAC), Khung được CHUYỂN TIẾP như bình thường.

![image](https://github.com/psaumur/CCNA/assets/106411237/ff731ab3-fad2-4e10-9fa7-ce583a6a0bb2)

- Lưu ý: Địa chỉ MAC Động được loại bỏ khỏi BẢNG ĐỊA CHỈ MAC sau mỗi 5 phút không hoạt động.
