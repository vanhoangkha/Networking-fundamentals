# NGÀY 06: ETHERNET LAN SWITCHING PART2

Một Khung Ethernet trông như:

Header Ethernet --- DỮ LIỆU (Gói tin) --- Trailer Ethernet

![image](https://github.com/psaumur/CCNA/assets/106411237/27c1877f-57d7-44ea-8c64-b0ec2b308ad0)

Header Ethernet chứa 5 Trường:

Preamble -- SFD -- Đích -- Nguồn -- Loại/Độ dài
7 byte   -- 1 byte -- 6 byte -- 6 byte -- 2 byte

Trailer Ethernet chứa 1 Trường:

FCS (Chuỗi Kiểm tra Khung) = 4 byte

- PREAMBLE + SFD thường không được coi là một phần của Header Ethernet.

DO ĐÓ kích thước của Header Ethernet + Trailer là 18 byte (6 + 6 + 2 + 4 byte cho Chuỗi KIỂM TRA KHUNG)

- --

Kích thước TỐI THIỂU cho một Khung Ethernet (Header + Payload [Gói tin] + Trailer) là 64 BYTE.

64 BYTE - 18 BYTE (kích thước Header + Trailer) = 46 BYTE

DO ĐÓ kích thước PAYLOAD DỮ LIỆU TỐI THIỂU (Gói tin) là 46 BYTE!

NẾU PAYLOAD NHỎ HƠN 46 BYTE thì BYTE PADDING được thêm vào (byte padding là một chuỗi số 0) cho đến khi bằng 46 BYTE.

- --

Khi một PC gửi một Gói tin đến một Thiết bị với Địa chỉ IP không biết, nó sử dụng ARP Request.

![image](https://github.com/psaumur/CCNA/assets/106411237/e2d0e5d2-7c98-4671-b356-903132fd7525)

- ARP viết tắt của 'Giao thức Phân giải Địa chỉ' (Address Resolution Protocol).
- Nó được sử dụng để khám phá Địa chỉ Tầng 2 (Địa chỉ MAC) của một Địa chỉ Tầng 3 đã biết (Địa chỉ IP)
- Bao gồm hai thông điệp:
- ARP REQUEST (Thông điệp nguồn)
- ARP REPLY (Thông điệp đích)
- ARP REQUEST là Broadcast = được gửi đến tất cả host trên Mạng, ngoại trừ host mà nó nhận được yêu cầu.

Một Khung ARP REQUEST có:
- Địa chỉ IP Nguồn
- Địa chỉ IP Đích
- Địa chỉ MAC Nguồn
- Địa chỉ MAC Broadcast - FFFF.FFFF.FFFF

Một Khung ARP REPLY có:
- Địa chỉ IP Nguồn
- Địa chỉ IP Đích
- Địa chỉ MAC Nguồn
- Địa chỉ MAC Đích

ARP REPLY là một Khung Unicast đã biết = Chỉ được gửi đến host đã gửi ARP REQUEST.

![image](https://github.com/psaumur/CCNA/assets/106411237/914cdf2a-c631-47e5-80f9-46e32ebed311)

- --

PING

- Một tiện ích Mạng được sử dụng để kiểm tra khả năng kết nối
- Đo thời gian khứ hồi
- Sử dụng hai thông điệp:
- ICMP Echo REQUEST
- ICMP Echo REPLY
- Là Unicast
- Lệnh để sử dụng ping:
- ping <địa-chỉ-ip>

Theo mặc định, CISCO IOS gửi 5 ICMP request/reply (Kích thước mặc định là 100-byte)

- Dấu chấm (.) là ping thất bại
- Dấu chấm than (!) là ping thành công

- --

CÁC LỆNH CISCO IOS HỮU ÍCH (từ chế độ Privileged EXEC)

PC1# show arp // hiển thị bảng ARP của host

![image](https://github.com/psaumur/CCNA/assets/106411237/da199d21-4f41-485e-8917-ca8e3d789617)

- --

SW1# show mac-address-table // hiển thị bảng MAC của switch

![image](https://github.com/psaumur/CCNA/assets/106411237/c1cd95dd-7742-4703-9487-946652c95485)

Sẽ hiển thị:

VLAN --- Địa chỉ MAC --- Loại --- Cổng(giao diện)

(VLAN = Mạng Cục bộ Ảo)

- --

![image](https://github.com/psaumur/CCNA/assets/106411237/657b054b-a90c-4e5f-8544-2a51082cb631)

SW1# clear mac-address-table dynamic <địa chỉ MAC tùy chọn>
// xóa toàn bộ bảng MAC của switch.
// NẾU địa chỉ MAC tùy chọn được sử dụng, nó sẽ xóa Địa chỉ MAC CỤ THỂ.

SW1# clear mac-address-table dynamic interface <giao diện tùy chọn>
// xóa mục bảng MAC của Switch theo **tên Giao diện**.