# 2. GIAO DIỆN VÀ CÁP MẠNG

SWITCH cung cấp nhiều CỔNG để kết nối (thường là 24 cổng)

Những CỔNG này thường là cổng RJ-45 (Registered Jack).

---

ETHERNET LÀ GÌ?

- Ethernet là một tập hợp các giao thức/tiêu chuẩn mạng.

Tại sao chúng ta cần các giao thức và tiêu chuẩn mạng?

- cung cấp các tiêu chuẩn giao tiếp chung qua mạng.
- cung cấp các tiêu chuẩn phần cứng chung để cho phép kết nối giữa các thiết bị.

Kết nối giữa các thiết bị hoạt động ở một tốc độ đã đặt.

Những tốc độ này được đo bằng "bit trên giây" (bps)

Một bit là giá trị "0" hoặc "1".
Một byte là 8 bit (0 và 1)

| Kích Thước | Số Bit |
| --- | --- |
| 1 kilobit (Kb) |  1,000 |
| 1 megabit (Mb) | 1,000,000 |
| 1 gigabit (Gb) | 1,000,000,000 |
| 1 terabit (Tb) | 1,000,000,000,000  |

Các tiêu chuẩn Ethernet:

- Được định nghĩa trong tiêu chuẩn IEEE 802.3 năm 1983
- IEEE = Viện Kỹ sư Điện và Điện tử

TIÊU CHUẨN ETHERNET (ĐỒNG)

| Tốc Độ | Tên Thông Dụng | Tiêu Chuẩn | Loại Cáp | Khoảng Cách Truyền Tối Đa |
| --- | --- | --- | --- | --- |
| 10 Mbps | Ethernet | 802.3i | 10BASE-T | Tối đa 100m |
| 100 Mbps | Fast Ethernet | 802.3u | 100BASE-T | Tối đa 100m |
| 1 Gbps | Gigabit Ethernet | 802.3ab | 1000BASE-T | Tối đa 100m |
| 10 Gbps | 10 Gigabit Ethernet | 802.3an | 10GBASE-T | Tối đa 100m |

BASE = đề cập đến Tín hiệu Băng tần Cơ sở

T = Cặp Xoắn (Twisted Pair)

Hầu hết Ethernet sử dụng cáp đồng.

UTP hoặc Cặp Xoắn Không Che Chắn
(không có lá chắn kim loại)
Xoắn bảo vệ chống nhiễu điện từ EMI (Electromagnetic Interference)

Hầu hết sử dụng 8 dây (4 cặp) tuy nhiên ...

10/100BASE-T = 2 cặp (4 dây)

![image](https://github.com/psaumur/CCNA/assets/106411237/00b27997-a78a-4e81-a878-7f8ab7e3279e)

---

Các thiết bị giao tiếp qua kết nối của chúng như thế nào?

Mỗi cáp ethernet có đầu cắm RJ-45 với 8 chân ở các đầu.

![image](https://github.com/psaumur/CCNA/assets/106411237/323930c9-3387-4bf9-aae1-f61db0fd9c04)

- PC Truyền(TX) dữ liệu trên Chân #1-2
- Switch Nhận(RX) dữ liệu trên Chân #1-2
- PC Nhận(RX) dữ liệu trên Chân #3,6
- Switch Truyền(TX) dữ liệu trên Chân #3,6

Điều này cho phép truyền dữ liệu Song công Toàn phần (Full-Duplex).

---

Điều gì xảy ra nếu Router / Switch kết nối?

![image](https://github.com/psaumur/CCNA/assets/106411237/907259d9-1837-4d53-8f45-a42934fb66f2)

- Router Truyền(TX) dữ liệu trên Chân #1-2
- Router Nhận(RX) dữ liệu trên Chân #3,6
- Switch Truyền(TX) dữ liệu trên Chân #3,6
- Switch Nhận(RX) dữ liệu trên Chân #1-2

Router và PC kết nối với Switch theo cùng một cách.

Cáp được sử dụng để kết nối được gọi là cáp "Thẳng" (Straight-Through).

---

Điều gì xảy ra nếu chúng ta muốn kết nối các thiết bị tương tự với nhau?

Chúng ta KHÔNG THỂ sử dụng cáp "Thẳng".
Chúng ta PHẢI sử dụng cáp "Chéo" (Crossover).

Cáp này hoán đổi các chân ở một đầu để cho phép kết nối hoạt động.

![image](https://github.com/psaumur/CCNA/assets/106411237/d98646ad-366f-4e96-8c6f-f6b5f32f9bdc)

CHÂN#1 -----> CHÂN#3
CHÂN#2 -----> CHÂN#6

CHÂN#3 -----> CHÂN#1
CHÂN#6 -----> CHÂN#2

---

| LOẠI THIẾT BỊ | CHÂN TRUYỀN (TX) | CHÂN NHẬN (RX) |
| --- | --- | --- |
| ROUTER | 1 và 2 | 3 và 6 |
| FIREWALL | 1 và 2 | 3 và 6 |
| PC | 1 và 2 | 3 và 6 |
| SWITCH | 3 và 6 | 1 và 2 |

---

Hầu hết thiết bị hiện đại hiện có AUTO MDI-X **tự động phát hiện** chân nào mà thiết bị láng giềng đang truyền và điều chỉnh các chân mà chúng nhận dữ liệu.

1000BASE-T/10GBASE-T = 4 cặp (8 dây)

Mỗi cặp dây là **hai chiều** nên có thể truyền/nhận nhanh hơn nhiều so với 10/100BASE-T.

![image](https://github.com/psaumur/CCNA/assets/106411237/763c841a-d7b5-4e87-8500-b54d623af620)

---

Kết nối Cáp Quang:

- Được định nghĩa trong tiêu chuẩn IEEE 802.3ae

Bộ Thu Phát SFP (Small Form-Factor Pluggable) cho phép cáp quang kết nối với switch/router.

- Có các cáp riêng biệt để truyền / nhận.

4 phần của cáp quang.

![image](https://github.com/psaumur/CCNA/assets/106411237/70b81cde-265f-413b-815b-3e7184ea0586)

Có HAI loại cáp quang.

Đơn Mode (Single-Mode):

![image](https://github.com/psaumur/CCNA/assets/106411237/d9a4b633-44c2-491d-92e4-329dd3b9074b)

- Hẹp hơn đa mode
- Ánh sáng đi vào ở một góc duy nhất (mode) từ bộ truyền dựa trên laser.
- Cho phép cáp dài hơn cả UTP và cáp quang đa mode.
- Đắt hơn cáp quang đa mode (do bộ truyền SFP dựa trên laser đắt hơn)

Đa Mode (Multimode):

![image](https://github.com/psaumur/CCNA/assets/106411237/e73ec4d0-9aa1-4a75-848c-3af70e770dce)

- Lõi rộng hơn Đơn mode
- Cho phép nhiều góc (mode) của sóng ánh sáng đi vào lõi
- Cho phép cáp dài hơn UTP nhưng ngắn hơn đơn mode
- Rẻ hơn cáp quang đơn mode (do bộ truyền SFP dựa trên LED rẻ hơn)

---

Tiêu Chuẩn Cáp Quang:

| Tốc Độ | Tiêu Chuẩn | Tốc Độ Kết Nối | Hỗ Trợ Mode | Khoảng Cách Truyền Tối Đa |
| --- | --- | --- | --- | --- |
| 1000BASE-LX | 802.3z | 1 Gbps | Đa mode / Đơn mode | 550 mét (Đa) / 5km (Đơn) |
| 10GBASE-SR | 802.3ae | 10 Gbps | Đa mode | 400 mét |
| 10GBASE-LR | 802.3ae | 10 Gbps | Đơn mode | 10 kilômét |
| 10GBASE-ER | 802.3ae | 10 Gbps | Đơn mode | 30 kilômét |

---

So Sánh Cáp UTP vs Cáp Quang:

UTP:

- Chi phí thấp hơn cáp quang.
- Khoảng cách tối đa ngắn hơn cáp quang (~100m).
- Có thể dễ bị nhiễu EMI (Nhiễu Điện từ).
- Cổng RJ45 sử dụng với UTP rẻ hơn cổng SFP.
- Phát ra (rò rỉ) tín hiệu yếu bên ngoài cáp, có thể bị sao chép (rủi ro bảo mật).

Cáp Quang:

- Chi phí cao hơn UTP.
- Khoảng cách tối đa dài hơn UTP.
- Không dễ bị nhiễu EMI.
- Cổng SFP đắt hơn cổng RJ45 (đơn mode đắt hơn đa mode).
- Không phát ra tín hiệu nào bên ngoài cáp (không có rủi ro bảo mật).
