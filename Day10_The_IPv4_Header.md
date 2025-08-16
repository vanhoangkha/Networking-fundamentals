# NGÀY 10: THE IPV4 HEADER

## 10.1 GIỚI THIỆU

**Header Giao thức Internet phiên bản 4** hoặc **Header IPv4**
Header được sử dụng tại **TẦNG 3** để giúp gửi dữ liệu giữa các thiết bị trên các mạng riêng biệt. thậm chí ở phía bên kia thế giới qua Internet. Điều này được gọi là **Định tuyến**. **Header IPv4** dùng để **ĐÓNG GÓI** một Đoạn TCP hoặc UDP. **Để ôn tập: **! [image](https: //github. com/psaumur/CCNA/assets/106411237/64906e3c-0bae-4c2c-96ca-4e6850f3844a)
- --
## 10.2 CÁC TRƯỜNG CỦA HEADER IPv4! [image](https: //github. com/psaumur/CCNA/assets/106411237/f2667488-2769-4e62-bee7-eddbf9e00058)

| TRƯỜNG | SỐ BIT |
| --- | --- |
| VERSION | 4 |
| IHL | 4 |
| DSCP | 6 |
| ECN | 2 |
| TOTAL LENGTH | 16 |
| IDENTIFICATION | 16 |
| FLAGS | 3 |
| FRAGMENT OFFSET | 13 |
| TIME TO LIVE | 8 |
| PROTOCOL | 8 |
| HEADER CHECKSUM | 16 |
| SOURCE ADDRESS | 32 |
| DESTINATION ADDRESS | 32 |
| OPTIONS | 320 Max |
- --
## 10.3 VERSION: - **ĐỘ DÀI: ** 4 bit

- Xác định phiên bản IP được sử dụng (IPv4 hoặc IPv6)
- **IPv4** = 0100 trong Nhị phân (Thập phân 4)
- **IPv6** = 0110 trong Nhị phân (Thập phân 6)
- --
## 10.4 Internet HEADER LENGTH (IHL): - **ĐỘ DÀI: ** 4 bit

- Trường cuối cùng của Header IPv4 (Options) có độ dài thay đổi nên trường này cần thiết để chỉ ra tổng độ dài của Header. - Xác định độ dài của Header theo **ĐƠN VỊ TĂNG 4-BYTE**. - Giá trị **TỐI THIỂU** là 5 (5 × 4-byte = 20 byte) - Trường OPTIONS trống
- Giá trị **TỐI ĐA** là 15 (15 × 4-byte = 60 byte)
**ĐỘ DÀI Header IPv4 TỐI THIỂU = 20 Byte! **
**ĐỘ DÀI Header IPv4 TỐI ĐA = 60 Byte! **
- --
## 10.5 DSCP (DIFFERENTIATED SERVICES CODE POINT): - **ĐỘ DÀI: ** 6 bit

- Được sử dụng cho **QoS (Chất lượng Dịch vụ)**
- Được sử dụng để ưu tiên dữ liệu nhạy cảm với độ trễ (streaming voice, video, v. v. )
- --
## 10.6 ECN (EXPLICIT CONGESTION NOTIFICATION): - **ĐỘ DÀI: ** 2 bit

- Cung cấp thông báo đầu cuối đến đầu cuối (giữa hai điểm cuối) về tắc nghẽn Mạng MÀ KHÔNG loại bỏ gói tin. - Tính năng tùy chọn yêu cầu cả hai điểm cuối, cũng như Hạ tầng Mạng cơ bản hỗ trợ nó. - --
## 10.7 TOTAL LENGTH: - **ĐỘ DÀI: ** 16 bit

- Chỉ ra độ dài TỔNG của Gói tin (Header L3 + Đoạn L4)
- Được đo bằng byte (không phải đơn vị tăng 4-byte như IHL)
- Giá trị tối thiểu là 20 Byte (Header IPv4 KHÔNG có dữ liệu được đóng gói)
- Giá trị tối đa là 65. 535 (giá trị 16-bit TỐI ĐA) = 2^16
- --
## 10.8 IDENTIFICATION: - **ĐỘ DÀI: ** 16 bit

- Nếu một Gói tin bị phân mảnh do quá lớn, trường này dùng để xác định Gói tin nào mà mảnh thuộc về. - Tất cả các mảnh của cùng một Gói tin sẽ có Header IPv4 riêng với cùng giá trị trong trường này. - Gói tin bị phân mảnh nếu lớn hơn **MTU (Maximum Transmission Unit)**
- MTU thường là 1500 byte (Kích thước tối đa của một Khung Ethernet)
- Các mảnh được tái lắp ráp bởi host nhận. - --
## 10.9 FLAGS: - **ĐỘ DÀI: ** 3 bit

- Được sử dụng để Kiểm soát/xác định các mảnh. - **Bit 0: ** Dành riêng, luôn được đặt thành 0. - **Bit 1: ** Don't Fragment (DF bit), dùng để chỉ ra một Gói tin không nên bị phân mảnh. - **Bit 2: ** More Fragments (MF bit), được đặt thành 1 nếu có nhiều mảnh hơn trong Gói tin, được đặt thành 0 cho mảnh cuối cùng hoặc KHÔNG có mảnh. - --
## 10.10 FRAGMENT OFFSET: - **ĐỘ DÀI: ** 13 bit

- Được sử dụng để chỉ ra vị trí của mảnh trong Gói tin IP gốc, chưa phân mảnh. - Cho phép các gói tin bị phân mảnh được tái lắp ráp ngay cả khi các mảnh đến không theo thứ tự. - --
## 10.11 TIME TO LIVE (TTL): - **ĐỘ DÀI: ** 8 bit

- router sẽ loại bỏ một Gói tin có TTL bằng 0
- Được sử dụng để ngăn chặn vòng lặp vô hạn
- Ban đầu được thiết kế để chỉ ra thời gian sống tối đa của gói tin tính bằng giây. - Trong thực tế, chỉ ra 'số hop': mỗi khi Gói tin đến một router, router giảm TTL đi 1. - TTL Mặc định được khuyến nghị là 64. - --
## 10.12 PROTOCOL: - **ĐỘ DÀI: ** 8 bit

- Chỉ ra Giao thức của PDU Tầng 4 được đóng gói
- **Giá trị 1: ** ICMP
- **Giá trị 6: ** TCP
- **Giá trị 17: ** UDP
- **Giá trị 89: ** OSPF (Giao thức Định tuyến Động)
- Danh sách số Giao thức trên Wikipedia: List of IP Protocol Numbers
- --
## 10.13 HEADER CHECKSUM: - **ĐỘ DÀI: ** 16 bit

- Checksum được tính toán để kiểm tra lỗi trong Header IPv4. - Khi một router nhận một Gói tin, nó tính toán checksum của Header và so sánh với checksum trong trường này của Header. - Nếu chúng không khớp, router loại bỏ Gói tin. - Được sử dụng để kiểm tra LỖI chỉ trong Header IPv4. - IP dựa vào Giao thức được đóng gói để phát hiện lỗi trong dữ liệu được đóng gói. - Cả TCP và UDP đều có trường checksum riêng để phát hiện lỗi trong dữ liệu được đóng gói. - --
## 10.14 SOURCE VÀ DESTINATION: - **ĐỘ DÀI: ** 32 bit mỗi trường

- **SOURCE IP** = Địa chỉ IPv4 của Người gửi Gói tin. - **DESTINATION IP** = Địa chỉ IPv4 của Người nhận dự định của Gói tin. - --
## 10.15 OPTIONS: - **ĐỘ DÀI: ** 0-320 bit

- Tùy chọn / Hiếm khi được sử dụng
- Nếu trường IHL lớn hơn 5, có nghĩa là Options có mặt.