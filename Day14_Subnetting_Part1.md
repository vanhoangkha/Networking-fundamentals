# NGÀY 14: SUBNETTING PART1

## 14.1 GIỚI THIỆU VỀ CHIA MẠNG CON! [image](https: //github. com/psaumur/CCNA/assets/106411237/a475e909-59b8-4615-a0b9-8a3c1fbdc313)

**Chỉ có địa chỉ Class A, B, C mới có thể gán cho một Thiết bị như một Địa chỉ IP. **
| CLASS | PREFIX LENGTH |
| ------- | ------- |
| A | /8 |
| B | /16 |
| C | /24 | ! [image](https: //github. com/psaumur/CCNA/assets/106411237/f0836136-c4a9-475b-b6c2-d1c550b8cfdd) |
## 14.2 VẤN ĐỀ VỚI HỆ THỐNG CLASSFUL

**IANA (Internet Assigned Numbers Authority)** gán địa chỉ IPv4/mạng cho các công ty dựa trên quy mô của họ. **Vấn đề với việc gán 'CLASSFUL'** là nó dẫn đến lãng phí địa chỉ IP. **Ví dụ: ** Một công ty cần 5000 địa chỉ được gán một IP CLASS B, để lại 60000+ địa chỉ không sử dụng. - --
## 14.3 GIẢI PHÁP: CIDR

**IETF (Internet Engineering Task Force)** giới thiệu **CIDR** năm 1993 để thay thế hệ thống địa chỉ "classful". **CIDR (Classless Inter-Domain Routing)** loại bỏ yêu cầu về kích thước của CLASS A, B, và C. - Điều này cho phép các mạng lớn hơn được chia thành các mạng nhỏ hơn, cho phép hiệu quả cao hơn. - Những mạng nhỏ hơn này được gọi là **"SUB-NETWORKS"** hoặc **"SUBNETS"**
- --
## 14.4 TÍNH TOÁN SỐ ĐỊA CHỈ SỬ DỤNG ĐƯỢC

**CÔNG THỨC: ** `2^n - 2 = Địa chỉ sử dụng được`
Trong đó: **n = số bit host**
- --
## 14.5 THỰC HÀNH CIDR

## 14.6 Ví dụ 1: 203. 0. 113. 0/25

**/25** có nghĩa là prefix mạng con là 25 bit
**203. 0. 113. 0** được viết dưới dạng nhị phân: ```
| 1100 1011.0000 0000.0111 0001.0 | 000 0000 |
```
(Prefix mạng con là 25 bit đầu tiên)
Chuyển tất cả bit thành 1, ta được **Subnet Mask** cho /25: ```
| 1111 1111.1111 1111.1111 1111.1 | 000 0000 |
```
Bằng: **255. 255. 255. 128** (vì octet cuối là 1000 0000 = 128 trong nhị phân)
**Số host cho 203. 0. 113. 0/25: **
- 2^(7 bit) hoặc (128) - 2 = **126 host**
- --
## 14.7 Ví dụ 2: /28 là gì? - *203. 0. 113. 0** được viết dưới dạng nhị phân: ```

| 1100 1011.0000 0000.0111 0001.0000 | 0000 |
```
(Prefix mạng con là 28 bit đầu tiên)
Chuyển tất cả bit thành 1, ta được **Subnet Mask** cho /28: ```
| 1111 1111.1111 1111.1111 1111.1111 | 0000 |
```
Bằng: **255. 255. 255. 240**
Tính toán octet cuối: 1111 0000 = 128+64+32+16 = 240
**Subnet Mask cho /28** là 255. 255. 255. 240 có 16 host/nhóm (2^4 bit = 16) - 2 IP dành riêng cho Mạng và Broadcast
- --
## 14.8 BẢNG THAM KHẢO CHIA MẠNG CON

| Kích thước nhóm | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| Subnet Mask | 128 | 192 | 224 | 240 | 248 | 252 | 254 | 255 |
| CIDR | /25 | /26 | /27 | /28 | /29 | /30 | /31 | /32 |
| Octet thứ 3 | /17 | /18 | /19 | /20 | /21 | /22 | /23 | /24 |
| Octet thứ 2 | /9 | /10 | /11 | /12 | /13 | /14 | /15 | /16 |
| Octet thứ 1 | /1 | /2 | /3 | /4 | /5 | /6 | /7 | /8 |
- --
## 14.9 PHƯƠNG PHÁP GIẢI CHIA MẠNG CON

## 14.10 Các bước cơ bản: 1. **Sử dụng CIDR/Mask để tìm cột trong Bảng tham khảo**

- CIDR/Subnet Mask tương ứng với nhau
- Xác định Kích thước nhóm
- Tăng theo Kích thước nhóm cho đến khi VƯỢT QUA IP mục tiêu
2. **Nếu vượt qua IP mục tiêu đạt 256: **
- Tăng Octet TRƯỚC nó lên một
- Octet hiện tại trở thành 0
- **Ví dụ: ** 10. 2. 2. 256 → 10. 2. 3. 0
3. **Xác định các thông số: **
- Số TRƯỚC IP mục tiêu là **Network ID**
- Số SAU IP mục tiêu là **Next Network**
- Địa chỉ IP TRƯỚC Next Network là **Broadcast**
- Địa chỉ IP SAU Network ID là **First Host**
- Địa chỉ IP TRƯỚC Broadcast IP là **Last Host**
- Kích thước nhóm là tổng số địa chỉ IP (trừ 2 cho số sử dụng được)
- --
## 14.11 GIẢI CHIA MẠNG CON CHO OCTET THỨ 3

**Quy tắc: **
- Mọi số BÊN TRÁI octet thứ 3 là **255**
- Mọi số BÊN PHẢI octet thứ 3 là **0**
## 14.12 Ví dụ: 10. 4. 77. 188/19

**Subnet Mask: ** 255. 255. 224. 0
**Tính toán: **
- 256 - 224 = 32
- Sử dụng 32, ta đi qua các khối địa chỉ: 0, 32, 64, 96
- Vì 77 nằm giữa 64 và 96, đây là phạm vi của chúng ta
**Kết quả: **
- **Network: ** 10. 4. 64. 0
- **Next Network: ** 10. 4. 96. 0
- **Số địa chỉ IP: ** 2^(32-19) = 2^13 = 8192
- --
## 14.13 PHƯƠNG PHÁP THAY THẾ CHO BẢNG THAM KHẢO! [image](https: //github. com/user-attachments/assets/d1e103b8-142a-44cc-8ab4-f5337268c9de)

## 14.14 Các bước: 1. **Tìm "magic octet"** nơi IP/Prefix nằm trong bảng bit

2. **Đếm số bit mạng** (trái sang phải) trong octet đó
3. **Trừ số đó từ 256** để tìm số Subnet Mask trong "magic octet"
4. **Chia số IP octet** trong "magic octet" cho kích thước nhóm địa chỉ
5. **Tính Base Network và Broadcast**
6. **Số subnet: ** 2^(số bit mạng trong magic octet)
7. **Tổng số host sử dụng được: ** 2^(32 - Prefix Length) - 2
- --
## 14.15 VÍ DỤ THỰC HÀNH

## 14.16 Ví dụ 1: 154. 219. 154. 180/20

```
Octet thứ 3 = Magic Octet
Kích thước nhóm địa chỉ = 16 (đếm 4 bit)
256 - 16 = 240 → Subnet Mask: 255. 255. 240. 0
154 ÷ 16 = 9 (có dư)
9 × 16 = 144 (Base Network)
Network: 154. 219. 144. 0
Broadcast: 154. 219. 159. 255
Subnets: 2^4 = 16
Tổng host: 2^(32-20) - 2 = 4094
```
## 14.17 Ví dụ 2: 84. 75. 21. 6/10

```
Octet thứ 2 = Magic Octet
Kích thước nhóm địa chỉ = 64
256 - 64 = 192 → Subnet: 255. 192. 0. 0
75 ÷ 64 = 1 (có dư)
1 × 64 = 64 (Base Network)
Network: 84. 64. 0. 0
Broadcast: 84. 127. 255. 255
Subnets: 2^2 = 4
Tổng host: 2^(32-10) - 2 = 4, 194, 302
```