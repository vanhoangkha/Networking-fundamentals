# NGÀY 16: SUBNETTING VLSM PART3

## 16.1 QUÁ TRÌNH CHIA MẠNG CON
Quá trình chia mạng con Class A, Class B, và Class C là giống hệt nhau.

## 16.2 CHIA MẠNG CON CLASS A
**Cho mạng 10.0.0.0/8**, bạn phải tạo 2000 subnet để phân phối cho các doanh nghiệp khác nhau. Bạn phải sử dụng prefix length nào?

**Tính toán:**
- 2^10 = 1024 (không đủ)
- 2^11 = 2048 (đủ)

Chúng ta phải "mượn" 11 bit (từ trái sang phải) để có đủ subnet:

```
0000 1010 . 0000 0000 . 000|00000 . 0000 0000
8 bit     + 8 bit     + 3 = 19 bit
```

**Subnet mask:**
```
1111 1111 . 1111 1111 . 111|00000 . 0000 0000
255.255.224.0
```

**Đáp án là /19** (/8 + /11 = /19)

**Số host trên mỗi subnet:**
Còn lại 13 bit host: 2^13 - 2 = **8190 host trên mỗi subnet**

- --

## 16.3 VARIABLE-LENGTH SUBNET MASKS (VLSM)
## 16.4 So sánh FLSM vs VLSM:
**FLSM (Fixed-Length Subnet Masks):**
- Tất cả subnet sử dụng cùng prefix length
- Ví dụ: Chia mạng Class C thành 4 subnet sử dụng /26

**VLSM (Variable-Length Subnet Masks):**
- Quá trình tạo các subnet có kích thước khác nhau
- Sử dụng địa chỉ mạng hiệu quả hơn
- Phức tạp hơn FLSM nhưng dễ nếu làm theo đúng các bước

- --

## 16.5 VÍ DỤ THỰC HÀNH VLSM
![image](https://github.com/psaumur/CCNA/assets/106411237/30a08f93-796a-4fe9-854e-58af0bcbd69b)

![image](https://github.com/psaumur/CCNA/assets/106411237/ad7d7ac0-5e00-4662-8192-f7f9db86f1d9)

![image](https://github.com/psaumur/CCNA/assets/106411237/dc006342-4bd9-40d4-b1c5-9ac7a670ed96)

## 16.6 Yêu cầu (sắp xếp theo thứ tự từ lớn đến nhỏ):
1. **TOKYO LAN A** (110 HOST)
2. **TORONTO LAN B** (45 HOST)
3. **TORONTO LAN A** (29 HOST)
4. **TOKYO LAN B** (8 HOST)
5. **POINT-TO-POINT CONNECTION** (giữa hai Router)

## 16.7 Mạng gốc: 192.168.1.0/24
```
192.168.1.0/24
11000000.10101000.00000001|00000000
(octet cuối là host = 254 host sử dụng được)
```

**Nguyên tắc:**
- Dịch TRÁI → TĂNG ĐÔI số host
- Dịch PHẢI → GIẢM NỬA số host

- --

## 16.8 BƯỚC 1: TOKYO LAN A (110 HOST)
Cần mượn 1 bit host sang phải để có 2^7 = 128 host (đủ cho 110 host):

```
192.168.1.0/25
11000000.10101000.00000001.0|0000000

Chuyển bit host còn lại thành 1: 01111111 = 127
Broadcast: 192.168.1.127/25
```

**Kết quả TOKYO LAN A:**
- **Network:** 192.168.1.0/25
- **Broadcast:** 192.168.1.127/25
- **First usable:** 192.168.1.1/25
- **Last usable:** 192.168.1.126/25
- **Tổng host sử dụng được:** 126 (2^7 - 2)

**Subnet tiếp theo bắt đầu từ:** 192.168.1.128

- --

## 16.9 BƯỚC 2: TORONTO LAN B (45 HOST)
Cần 2^6 = 64 host (đủ cho 45 host):

```
192.168.1.128/26
11000000.10101000.00000001.10|000000

Chuyển bit host thành 1: 10111111 = 191
Broadcast: 192.168.1.191/26
```

**Kết quả TORONTO LAN B:**
- **Network:** 192.168.1.128/26
- **Broadcast:** 192.168.1.191/26
- **First usable:** 192.168.1.129/26
- **Last usable:** 192.168.1.190/26
- **Tổng host sử dụng được:** 62 (2^6 - 2)

**Subnet tiếp theo bắt đầu từ:** 192.168.1.192

- --

## 16.10 BƯỚC 3: TORONTO LAN A (29 HOST)
Cần 2^5 = 32 host (đủ cho 29 host):

```
192.168.1.192/27
11000000.10101000.00000001.110|00000

Chuyển bit host thành 1: 11011111 = 223
Broadcast: 192.168.1.223/27
```

**Kết quả TORONTO LAN A:**
- **Network:** 192.168.1.192/27
- **Broadcast:** 192.168.1.223/27
- **First usable:** 192.168.1.193/27
- **Last usable:** 192.168.1.222/27
- **Tổng host sử dụng được:** 30 (2^5 - 2)

**Subnet tiếp theo bắt đầu từ:** 192.168.1.224

- --

## 16.11 BƯỚC 4: TOKYO LAN B (8 HOST)
Cần 2^4 = 16 host (đủ cho 8 host):

```
192.168.1.224/28
11000000.10101000.00000001.1110|0000

Chuyển bit host thành 1: 11101111 = 239
Broadcast: 192.168.1.239/28
```

**Kết quả TOKYO LAN B:**
- **Network:** 192.168.1.224/28
- **Broadcast:** 192.168.1.239/28
- **First usable:** 192.168.1.225/28
- **Last usable:** 192.168.1.238/28
- **Tổng host sử dụng được:** 14 (2^4 - 2)

**Subnet tiếp theo bắt đầu từ:** 192.168.1.240

- --

## 16.12 BƯỚC 5: POINT-TO-POINT CONNECTION
Chỉ cần 2 host cho kết nối point-to-point:

```
192.168.1.240/30
11000000.10101000.00000001.111100|00

Chuyển bit host thành 1: 11110011 = 243
Broadcast: 192.168.1.243/30
```

**Kết quả POINT-TO-POINT:**
- **Network:** 192.168.1.240/30
- **Broadcast:** 192.168.1.243/30
- **First usable:** 192.168.1.241/30
- **Last usable:** 192.168.1.242/30
- **Tổng host sử dụng được:** 2 (2^2 - 2)

- --

## 16.13 TÓM TẮT KẾT QUẢ VLSM
| Subnet | Network | Broadcast | Usable Range | Host | CIDR |
|--------|---------|-----------|--------------|------|------|
| Tokyo LAN A | 192.168.1.0 | 192.168.1.127 | .1 - .126 | 126 | /25 |
| Toronto LAN B | 192.168.1.128 | 192.168.1.191 | .129 - .190 | 62 | /26 |
| Toronto LAN A | 192.168.1.192 | 192.168.1.223 | .193 - .222 | 30 | /27 |
| Tokyo LAN B | 192.168.1.224 | 192.168.1.239 | .225 - .238 | 14 | /28 |
| Point-to-Point | 192.168.1.240 | 192.168.1.243 | .241 - .242 | 2 | /30 |

**Địa chỉ còn lại:** 192.168.1.244 - 192.168.1.255 (12 địa chỉ)

- --

## 16.14 NGUYÊN TẮC VLSM
1. **Sắp xếp theo thứ tự giảm dần** số host cần thiết
2. **Bắt đầu từ subnet lớn nhất** để tránh lãng phí
3. **Tính toán chính xác** số bit cần mượn: 2^n ≥ số host cần + 2
4. **Kiểm tra không trùng lặp** địa chỉ giữa các subnet
5. **Để lại không gian** cho mở rộng tương lai

- --

## 16.15 TRANG WEB THỰC HÀNH BỔ SUNG
- **http://www.subnettingquestions.com**
- **http://subnetting.org**
- **https://subnettingpractice.com** ⭐ **(Được khuyến nghị)**