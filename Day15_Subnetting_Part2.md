# NGÀY 15: SUBNETTING PART2

## 15.1 CHIA MẠNG CON CLASS C! [image](https: //github. com/psaumur/CCNA/assets/106411237/08be5a37-fa2c-4483-94c9-6c3d05229894)

## 15.2 Đặc điểm Class C: - **Prefix mặc định: ** /24 (255. 255. 255. 0)

- **Số host mặc định: ** 254 host (2^8 - 2)
- **Phạm vi: ** 192. 0. 0. 0 - 223. 255. 255. 255
## 15.3 Ví dụ chia mạng con Class C: - *Mạng gốc: ** 192. 168. 1. 0/24

## 15.4 Chia thành 2 subnet (/25): - **Subnet 1: ** 192. 168. 1. 0/25 (192. 168. 1. 0 - 192. 168. 1. 127)

- Network: 192. 168. 1. 0
- Broadcast: 192. 168. 1. 127
- Host sử dụng được: 192. 168. 1. 1 - 192. 168. 1. 126 (126 host)
- **Subnet 2: ** 192. 168. 1. 128/25 (192. 168. 1. 128 - 192. 168. 1. 255)
- Network: 192. 168. 1. 128
- Broadcast: 192. 168. 1. 255
- Host sử dụng được: 192. 168. 1. 129 - 192. 168. 1. 254 (126 host)
## 15.5 Chia thành 4 subnet (/26): - **Subnet 1: ** 192. 168. 1. 0/26 (0-63) → 62 host

- **Subnet 2: ** 192. 168. 1. 64/26 (64-127) → 62 host
- **Subnet 3: ** 192. 168. 1. 128/26 (128-191) → 62 host
- **Subnet 4: ** 192. 168. 1. 192/26 (192-255) → 62 host
## 15.6 Chia thành 8 subnet (/27): - Mỗi subnet có 30 host sử dụng được (2^5 - 2)

- Kích thước mỗi subnet: 32 địa chỉ
- --
## 15.7 CHIA MẠNG CON CLASS B! [image](https: //github. com/psaumur/CCNA/assets/106411237/44e8cdcb-16c2-41c4-8f22-a0a31071550a)

## 15.8 Đặc điểm Class B: - **Prefix mặc định: ** /16 (255. 255. 0. 0)

- **Số host mặc định: ** 65, 534 host (2^16 - 2)
- **Phạm vi: ** 128. 0. 0. 0 - 191. 255. 255. 255
## 15.9 Ví dụ chia mạng con Class B: - *Mạng gốc: ** 172. 16. 0. 0/16

## 15.10 Chia thành 2 subnet (/17): - **Subnet 1: ** 172. 16. 0. 0/17

- Phạm vi: 172. 16. 0. 0 - 172. 16. 127. 255
- Host: 32, 766
- **Subnet 2: ** 172. 16. 128. 0/17
- Phạm vi: 172. 16. 128. 0 - 172. 16. 255. 255
- Host: 32, 766
## 15.11 Chia thành 4 subnet (/18): - **Subnet 1: ** 172. 16. 0. 0/18 (0. 0 - 63. 255)

- **Subnet 2: ** 172. 16. 64. 0/18 (64. 0 - 127. 255)
- **Subnet 3: ** 172. 16. 128. 0/18 (128. 0 - 191. 255)
- **Subnet 4: ** 172. 16. 192. 0/18 (192. 0 - 255. 255)
Mỗi subnet có 16, 382 host sử dụng được. ## 15. 12 Chia thành 256 subnet (/24): - Tương đương với chia thành các mạng Class C
- Mỗi subnet có 254 host
- **Ví dụ: **
- 172. 16. 0. 0/24
- 172. 16. 1. 0/24
- 172. 16. 2. 0/24
-. . . - 172. 16. 255. 0/24
- --
## 15.12 SO SÁNH CÁC PHƯƠNG PHÁP CHIA MẠNG CON

| ## 15.13 Class C (192.168.1.0/24): | CIDR | Subnet Mask | Số Subnet | Host/Subnet | Tổng Host |
| ------- | ------- | ------- | ------- | ------- |
| /25 | 255.255.255.128 | 2 | 126 | 252 |
| /26 | 255.255.255.192 | 4 | 62 | 248 |
| /27 | 255.255.255.224 | 8 | 30 | 240 |
| /28 | 255.255.255.240 | 16 | 14 | 224 |
| /29 | 255.255.255.248 | 32 | 6 | 192 |
| /30 | 255.255.255.252 | 64 | 2 | 128 |
| ## 15.14 Class B (172.16.0.0/16): | CIDR | Subnet Mask | Số Subnet | Host/Subnet | Tổng Host |
| ------- | ------- | ------- | ------- | ------- |
| /17 | 255.255.128.0 | 2 | 32,766 | 65,532 |
| /18 | 255.255.192.0 | 4 | 16,382 | 65,528 |
| /19 | 255.255.224.0 | 8 | 8,190 | 65,520 |
| /20 | 255.255.240.0 | 16 | 4,094 | 65,504 |
| /21 | 255.255.248.0 | 32 | 2,046 | 65,472 |
| /22 | 255.255.252.0 | 64 | 1,022 | 65,408 |
| /23 | 255.255.254.0 | 128 | 510 | 65,280 |
| /24 | 255.255.255.0 | 256 | 254 | 65,024 |
- --
## 15.15 NGUYÊN TẮC QUAN TRỌNG

## 15.16 Quy tắc Powers of 2: - Số subnet = 2^(số bit mượn)

- Số host/subnet = 2^(số bit host còn lại) - 2
## 15.17 Subnet Mask: - Bit 1 = phần network

- Bit 0 = phần host
- Càng nhiều bit network → càng nhiều subnet, ít host
- Càng ít bit network → ít subnet, nhiều host
## 15.18 Địa chỉ đặc biệt: - **Network address: ** Tất cả bit host = 0

- **Broadcast address: ** Tất cả bit host = 1
- **First usable: ** Network + 1
- **Last usable: ** Broadcast - 1
## 15.19 Lưu ý thực tế: - /30 thường dùng cho point-to-point links (chỉ 2 host)

- /31 dùng cho point-to-point (không có network/broadcast)
- /32 là host route (chỉ 1 địa chỉ cụ thể)