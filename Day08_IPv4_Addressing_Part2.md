# 8. ĐỊA CHỈ IPv4: PHẦN 2

## SỐ HOST TỐI ĐA TRÊN MỖI MẠNG

Hãy lấy một Mạng Class C:
**192.168.1.0/24** (cho phạm vi từ 0 ---> 255)

Nói cách khác, phần HOST (.0) bằng 8 bit nên...

Phần Host = 8 bit = 2^8 = 256

TUY NHIÊN, vì địa chỉ Mạng (Mạng ID) **192.168.1.0** được Dành riêng VÀ **192.168.1.255** (địa chỉ Broadcast) cũng được dành riêng.

**Số HOST tối đa trên mỗi Mạng = 2^8-2 = 254 host**

---

## MẠNG CLASS B THÌ SAO?

**172.16.0.0/16** ----> **172.16.255.255/16**

Phần Host = 16 bit = 2^16 = 65,536

**Số host tối đa trên mỗi Mạng = 2^16-2 = 65,534 host**

---

## MẠNG CLASS A THÌ SAO?

**10.0.0.0/8** -------------> **10.255.255.255/8**

Phần Host = 24 bit = 2^24 = 16,777,216

**Số host tối đa trên mỗi Mạng = 2^24-2 = 16,777,214 host**

---

## CÔNG THỨC TÍNH TOÁN

DO ĐÓ: Công thức để tính số HOST trên một Mạng là:

**2^N - 2** (2 lũy thừa N trừ 2)

trong đó **N = số bit HOST**

---

## ĐỊA CHỈ CÓ THỂ SỬ DỤNG ĐẦU TIÊN / CUỐI CÙNG

### Mạng Class C

**192.168.1.0/24** (địa chỉ Mạng)

Cộng 1 nên phần Host = 00000001
**192.168.1.1/24 = ĐỊA CHỈ CÓ THỂ SỬ DỤNG ĐẦU TIÊN**

---

**192.168.1.255/24** (địa chỉ Broadcast)

Trừ 1 từ địa chỉ Broadcast = 11111110
**192.168.1.254/24 = ĐỊA CHỈ CÓ THỂ SỬ DỤNG CUỐI CÙNG**

---

### Mạng Class B

**172.16.0.0/16** (địa chỉ Mạng)

Cộng 1 vào phần Host nên 0000 0000 0000 0001
**172.16.0.1/16 là ĐỊA CHỈ CÓ THỂ SỬ DỤNG ĐẦU TIÊN**

---

**172.16.255.255/16** (địa chỉ Broadcast)

Trừ 1 từ địa chỉ Broadcast nên 1111 1111 1111 1110
**172.16.255.254/16 là ĐỊA CHỈ CÓ THỂ SỬ DỤNG CUỐI CÙNG**

---

### Mạng Class A

**10.0.0.0/8** (địa chỉ Mạng)

Cộng 1 vào phần Host nên 00000000 00000000 00000001
**10.0.0.1/8 là ĐỊA CHỈ CÓ THỂ SỬ DỤNG ĐẦU TIÊN**

---

**10.255.255.255/8** (địa chỉ Broadcast)

Trừ 1 từ địa chỉ Broadcast nên 1111 1111 1111 1110
**10.255.255.254/8 là ĐỊA CHỈ CÓ THỂ SỬ DỤNG CUỐI CÙNG**

---

## CẤU HÌNH THIẾT BỊ CISCO CLI

```
R1> enable
R1# show ip interface brief
```

Liệt kê các Giao diện, Địa chỉ IP, Phương pháp, Trạng thái và Giao thức.

**Giao diện:**
- Những giao diện Cổng nào có sẵn/được kết nối

**Địa chỉ IP:**
- Tự giải thích. Địa chỉ IP nào được gán.

**Phương pháp:**
- Địa chỉ IP được gán bằng phương pháp nào?

**Trạng thái (Trạng thái Tầng 1):**
- Trạng thái hiện tại của Giao diện
- 'administratively down' = Giao diện đã bị vô hiệu hóa bằng lệnh 'shutdown'

**Administratively down là trạng thái Mặc định của các giao diện Cisco Router.**

**Giao diện Switch Cisco KHÔNG bị administratively down theo Mặc định.**

**Giao thức (Trạng thái Tầng 2):**
- Không thể hoạt động nếu Trạng thái (Tầng 1) bị down

![image](https://github.com/psaumur/CCNA/assets/106411237/fa113ff0-a8ee-410b-ab3e-64684654cac6)

---

## CẤU HÌNH GIAO DIỆN

```
// lệnh configure terminal
R1# conf t

// Điều này vào chế độ Cấu hình Giao diện
R1(config)# interface gigabitethernet 0/0
```

Điều này có thể được rút ngắn thành 'g0/0' như chúng được liệt kê trong sơ đồ Mạng vật lý.

![image](https://github.com/psaumur/CCNA/assets/106411237/df83bf09-c391-45b7-b1b4-41db061b84f4)

```
// Điều này đặt Địa chỉ IP và MASK mạng con của Thiết bị
R1(config-if)# ip address 10.255.255.254 255.0.0.0

// Điều này kích hoạt Thiết bị
R1(config-if)# no shutdown
```

---

## THÔNG BÁO TRẠNG THÁI

Hai thông báo sẽ xuất hiện cho thấy trạng thái đã thay đổi thành 'up' (Trạng thái).

Thông báo thứ hai sẽ hiển thị Giao thức dòng hiện tại là 'up' (Giao thức).

```
// 'do' cho phép bạn chạy lệnh Privileged EXEC từ bên ngoài chế độ.
R1(config-if)# do show ip interface brief
```

Tốt để xác nhận rằng Thiết bị/Giao diện bạn đã cấu hình đang hoạt động.

---

## CÁC LỆNH CLI 'SHOW' KHÁC

![image](https://github.com/psaumur/CCNA/assets/106411237/bdc1152e-1946-4ddb-ae72-1e23b9c9defa)

### `show interfaces <tên giao diện>`
- Hiển thị thông tin Tầng 1 và Tầng 2 về giao diện và một số Tầng 3.
- Hiển thị địa chỉ MAC (hoặc địa chỉ BIA)
- Địa chỉ IP
- ... và nhiều hơn nữa

### `show interfaces description`
- Cho phép bạn thêm mô tả cho các giao diện.

**Ví dụ:**
```
// Chế độ cấu hình cho Giao diện Gigabyte 0/0
R1(config)# int g0/0
R1(config-if)# description ## to SW1 ##
```

Điều này đặt cột 'Description' để hiển thị:

| Giao diện | Mô tả |
|-----------|-------|
| Gi0/0     | ## to SW1 ## |
