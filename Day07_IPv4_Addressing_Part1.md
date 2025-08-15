# 7. ĐỊA CHỈ IPv4: PHẦN 1

## MÔ HÌNH OSI - TẦNG MẠNG (Tầng 3)

- Cung cấp kết nối giữa các host cuối trên các mạng KHÁC NHAU (tức là: bên ngoài LAN)
- Cung cấp địa chỉ logic (địa chỉ IP)
- Cung cấp lựa chọn đường đi giữa NGUỒN và ĐÍCH
- ROUTER hoạt động tại TẦNG 3

## ĐỊNH TUYẾN

SWITCH (Thiết bị Tầng 2) không tách biệt các mạng khác nhau. Chúng kết nối và MỞ RỘNG mạng trong cùng một LAN.

Tuy nhiên, bằng cách thêm một Router giữa hai SWITCH, bạn tạo ra một SỰ PHÂN CHIA trong Mạng; mỗi mạng có địa chỉ IP Mạng riêng.

Ví dụ:
- 192.168.1.0/24 (255.255.255.0)
- 192.168.2.0/24 (255.255.255.0)

![image](https://github.com/psaumur/CCNA/assets/106411237/3d414956-cb53-46f6-b386-3fc9bba11802)

ROUTER có địa chỉ IP duy nhất cho MỖI kết nối Giao diện của chúng, tùy thuộc vào vị trí của chúng.

- Địa chỉ IP cho Giao diện G0/0 của Router là: 192.168.1.254/24
- Địa chỉ IP cho Giao diện G0/1 của Router là: 192.168.2.254/24

![image](https://github.com/psaumur/CCNA/assets/106411237/6e593774-4113-4493-89bb-4d394cb29e1d)

Địa chỉ IP phụ thuộc vào địa chỉ Mạng của LAN mà nó kết nối.

Phần Mạng của một địa chỉ IP nhất định sẽ giống nhau cho tất cả HOST trên một LAN nhất định.

**Ví dụ:**
- 192.168.1.100
- 192.168.1.105  
- 192.168.1.205

Tất cả các địa chỉ này đều trên CÙNG MỘT Mạng vì phần Mạng của địa chỉ IP của chúng giống nhau (192.168.1) trong khi phần HOST (100,105,205) là DUY NHẤT!

Khi một thông điệp Broadcast đến Router, nó KHÔNG tiếp tục đi xa hơn. Nó ở lại trong LAN CỤC BỘ (Switch/Host).

---

## HEADER IPv4

![image](https://github.com/psaumur/CCNA/assets/106411237/4f4bd7da-1876-4000-8229-be4b8792a86d)

IP (hoặc Giao thức Internet) là Giao thức Tầng 3 chính được sử dụng ngày nay.

Phiên bản 4 là phiên bản được sử dụng trong hầu hết các mạng.

Header IPv4 chứa NHIỀU trường hơn Header Ethernet.

Header IPv4 chứa trường địa chỉ IP NGUỒN và địa chỉ IP ĐÍCH.

Trường này dài 32-bit (4-byte) (0-31)

**192.168.1.254** (mỗi số thập phân đại diện cho 8 bit)

Dịch sang Nhị phân:
**11000000 . 10101000 . 00000001 . 11111110**

MỖI nhóm 8 bit này được gọi là một OCTET

Vì Nhị phân khó đọc đối với con người, chúng ta sử dụng định dạng Thập phân có Dấu chấm.

---

## ÔN TẬP VỀ THẬP PHÂN VÀ THẬP LỤC PHÂN

![image](https://github.com/psaumur/CCNA/assets/106411237/e45f0ea9-a705-463b-bb9b-d81034cf130d)

**Thập phân (cơ số 10)**
Ví dụ: 3294 = (3 × 1000) + (2 × 100) + (9 × 10) + (4 × 1)

**Thập lục phân (cơ số 16)**
Ví dụ: 3294, sẽ là CDE

```
C (C × 256 / 12 × 256 = 3072) // vị trí 256
D (D × 16 / D=13 nên 16×13 = 208) // vị trí 16  
E (E × 1 / E = 14) // vị trí 1
```

Cộng tất cả lại, chúng ta được 3294

---

## CHUYỂN ĐỔI SỐ NHỊ PHÂN SANG SỐ THẬP PHÂN

Cách tương tự như chuyển đổi sang Thập lục phân.

**10001111**

```
1 × 128 = 128
1 × 8 = 8  
1 × 4 = 4
1 × 2 = 2
1 × 1 = 1
```

Cộng tất cả lại: 128 + 8 + 4 + 2 + 1 = **143**

---

**Ví dụ khác: 01110110**

```
1 × 64 = 64
1 × 32 = 32
1 × 16 = 16
1 × 4 = 4
1 × 2 = 2
```

Cộng tất cả lại: 64 + 32 + 16 + 4 + 2 = **118**

---

**Ví dụ khác: 11101100**

```
1 × 128 = 128
1 × 64 = 64
1 × 32 = 32
1 × 8 = 8
1 × 4 = 4
```

Cộng tất cả lại: 128 + 64 + 32 + 8 + 4 = **236**

---

## CHUYỂN ĐỔI SỐ THẬP PHÂN SANG SỐ NHỊ PHÂN

Lấy số 221.

Chúng ta có thể lấy số đó và bắt đầu trừ từ TRÁI sang PHẢI của các vị trí Nhị phân.

**221**

```
221 - 128 = 93 nên chúng ta đặt 1 vào vị trí "128"
```
10000000

```
93 - 64 = 29 nên chúng ta đặt 1 khác vào vị trí "64"
29 - 32 không thể nên chúng ta đặt 0 vào vị trí "32"
29 - 16 = 13 nên chúng ta đặt 1 vào vị trí "16"
13 - 8 = 5 nên chúng ta đặt 1 vào vị trí "8"
5 - 4 = 1 nên chúng ta đặt 1 vào vị trí "4"
1 - 2 không thể nên chúng ta đặt 0 vào vị trí "2"
1 - 1 có thể nên chúng ta đặt 1 vào vị trí "1"
```

Điều này cho phép chúng ta viết ra số NHỊ PHÂN cho 221.
Đó là: **11011101**

---

**Ví dụ khác: 127**

```
127 - 128 không thể nên 0 ở "128"
127 - 64 có thể nên 1 ở "64"
63 - 32 có thể nên 1 ở "32"
31 - 16 có thể nên 1 ở "16"
15 - 8 có thể nên 1 ở "8"
7 - 4 có thể nên 1 ở "4"
3 - 2 có thể nên 1 ở "2"
1 có thể nên 1 ở "1"
```

Vậy 127, ở dạng NHỊ PHÂN, là **01111111**

---

**Ví dụ khác: 207**

Cách khác, bạn có thể trừ số từ '255' (là 11111111). Phần còn lại có thể được sử dụng để "tìm" vị trí của các số 0 trong số nhị phân.

255 - 207 = 48 nên...
**11001111** (32 + 16 = 48) là câu trả lời đúng.

---

## ĐỊA CHỈ IPv4

Bây giờ chúng ta biết rằng Địa chỉ IP là chuyển đổi Thập phân có Dấu chấm của một chuỗi SỐ NHỊ PHÂN (được chia thành 4 OCTET) như sau:

**192.168.1.254/24**

Nhưng /24 có nghĩa là gì?

![image](https://github.com/psaumur/CCNA/assets/106411237/808fa7fa-0239-42fa-9706-79db87ea167e)

Nó có nghĩa là 24 BIT ĐẦU TIÊN của địa chỉ này đại diện cho phần Mạng của địa chỉ.

- **192.168.1** là PHẦN MẠNG (3 OCTET đầu tiên)
- **.254** là PHẦN HOST (OCTET cuối cùng)

![image](https://github.com/psaumur/CCNA/assets/106411237/2e7c64e1-5689-486a-bba0-9623f5e8de7d)

---

## BÀI TẬP CHUYỂN ĐỔI

**CHUYỂN ĐỔI số NHỊ PHÂN này thành địa chỉ IPv4:**

**10011010010011100110111100100000**

Chia thành các Octet:
**10011010 . 01001110 . 01101111 . 00100000**

Octet:
1. 128 + 16 + 8 + 2 = **154**
2. 64 + 8 + 4 + 2 = **78**
3. 64 + 32 + 8 + 4 + 2 + 1 = **111**
4. 32 = **32**

Địa chỉ IPv4 là: **154.78.111.32/16**
- **154.78** là PHẦN MẠNG
- **111.32** là PHẦN HOST

**Ví dụ khác:**
**00001100100000001111101100010111**

Chia thành các Octet:
**00001100 . 10000000 . 11111011 . 00010111**

Octet:
1. 8 + 4 = **12**
2. 128 = **128**
3. 255 - 4 = **251**
4. 16 + 4 + 2 + 1 = **23**

Địa chỉ IPv4 là: **12.128.251.23/8**
- **12** là PHẦN MẠNG
- **128.251.23** là PHẦN HOST

---

## CÁC LỚP ĐỊA CHỈ IPv4

Địa chỉ IPv4 được chia thành 5 'lớp' khác nhau.

Lớp của một IPv4 được xác định bởi OCTET ĐẦU TIÊN của địa chỉ.

| LỚP | OCTET ĐẦU TIÊN | PHẠM VI SỐ OCTET ĐẦU TIÊN |
|-----|----------------|---------------------------|
| A   | 0xxxxxxx       | 0-126 + 127 'loopback'   |
| B   | 10xxxxxx       | 128-191                   |
| C   | 110xxxxx       | 192-223                   |
| D   | 1110xxxx       | 224-239                   |
| E   | 1111xxxx       | 240-255                   |

Từ bảng trên, nếu OCTET ĐẦU TIÊN BẮT ĐẦU bằng 0, phạm vi số của thập phân có dấu chấm đầu tiên có thể là từ 0-127.

Các LỚP chúng ta sẽ tập trung vào là LỚP A đến LỚP C.

![image](https://github.com/psaumur/CCNA/assets/106411237/7cc286bf-ce76-4eee-af52-062a63dac2b4)

- **LỚP D** được dành riêng cho địa chỉ 'Multicast'
- **LỚP E** được dành riêng cho địa chỉ 'THỰC NGHIỆM'

---

## TẠI SAO LỚP A THƯỜNG CÓ PHẠM VI 1-126?

Vì 127 thường được dành riêng cho 'địa chỉ loopback'

**127.0.0.0 đến 127.255.255.255** được sử dụng để kiểm tra Mạng.
- Được sử dụng để kiểm tra 'ngăn xếp Mạng' (mô hình OSI & TCP/IP) trên Thiết bị cục bộ.

---

## ĐỘ DÀI PREFIX

![image](https://github.com/psaumur/CCNA/assets/106411237/25f7db1a-f934-4c73-9926-66bb207fd292)

ĐỘ DÀI PREFIX là ĐỘ DÀI của PHẦN MẠNG của địa chỉ.

Từ các ví dụ trên:
- **12.128.251.23/8** là địa chỉ LỚP A
- **154.78.111.32/16** là địa chỉ LỚP B  
- **192.168.1.254/24** là địa chỉ LỚP C

Vì phần Mạng của LỚP A rất ngắn, có nghĩa là có NHIỀU Host tiềm năng hơn.

Vì phần Mạng của LỚP C rất dài, có nghĩa là ít Host tiềm năng hơn.

---

## NETMASK

![image](https://github.com/psaumur/CCNA/assets/106411237/874c022f-9b8c-4862-a495-597682b014a4)

NETMASK được viết như một địa chỉ IP Thập phân có Dấu chấm

- **LỚP A**: /8 = 255.0.0.0
- **LỚP B**: /16 = 255.255.0.0
- **LỚP C**: /24 = 255.255.255.0

---

## ĐỊA CHỈ MẠNG

![image](https://github.com/psaumur/CCNA/assets/106411237/12178b46-2604-468b-a11c-2a94087b023d)

Nếu PHẦN HOST của một địa chỉ IP là TẤT CẢ số 0, có nghĩa là đó là địa chỉ Mạng = định danh của chính Mạng đó.

**Ví dụ:** 192.168.1.0/24 = ĐÂY là một địa chỉ Mạng.

- Một địa chỉ Mạng không thể được gán cho một HOST.
- Một địa chỉ Mạng là địa chỉ ĐẦU TIÊN.

![image](https://github.com/psaumur/CCNA/assets/106411237/53eafb43-2a6f-422c-af19-866946d78efa)

## ĐỊA CHỈ BROADCAST

Nếu PHẦN HOST của một địa chỉ IP là TẤT CẢ số 1, có nghĩa là đó là địa chỉ Broadcast cho Mạng.

- Một địa chỉ Broadcast không thể được gán cho một HOST.

**DESTINATION IP:** 192.168.1.255 (địa chỉ IP Broadcast)
**DESTINATION MAC:** FFFF.FFFF.FFFF (địa chỉ MAC Broadcast)

Vì có hai địa chỉ 'dành riêng', phạm vi của ĐỊA CHỈ HOST CÓ THỂ SỬ DỤNG là từ 1 đến 254.
