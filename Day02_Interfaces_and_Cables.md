# NGÀY 02: INTERFACES AND CABLES

## 02.1 Giao diện switch

**switch** cung cấp nhiều **cổng kết nối** (thường là 24 cổng) để các thiết bị mạng có thể kết nối. Các cổng này thường sử dụng chuẩn **RJ-45** (Registered Jack-45). ## 02. 2 Ethernet là gì? **Ethernet** là tập hợp các giao thức và tiêu chuẩn mạng được sử dụng rộng rãi trong mạng LAN. **Lý do chính: **
- Cung cấp các tiêu chuẩn giao tiếp chung qua mạng
- Đảm bảo tính tương thích phần cứng giữa các thiết bị từ các nhà sản xuất khác nhau
- Tạo ra môi trường mạng ổn định và đáng tin cậy
## 02.2 Tốc độ kết nối và đơn vị đo

**Kết nối** giữa các thiết bị hoạt động ở một tốc độ xác định, được đo bằng **"bit trên giây" (bps)**. - **Bit**: Đơn vị dữ liệu nhỏ nhất, có giá trị "0" hoặc "1"
- **Byte**: Bằng 8 bit
| Đơn vị | Số bit |
| ------- | ------- |
| 1 kilobit (Kb) | 1,000 |
| 1 megabit (Mb) | 1,000,000 |
| 1 gigabit (Gb) | 1,000,000,000 |
| 1 terabit (Tb) | 1,000,000,000,000 |
## 02.3 Tiêu chuẩn Ethernet

| **Tiêu chuẩn IEEE 802.3** được định nghĩa năm 1983 bởi **IEEE** (Viện Kỹ sư Điện và Điện tử). | Tốc độ | Tên thông dụng | Tiêu chuẩn | Loại cáp | Khoảng cách tối đa |
| ------- | ------- | ------- | ------- | ------- |
| 10 Mbps | Ethernet | 802.3i | 10BASE-T | 100 m |
| 100 Mbps | Fast Ethernet | 802.3u | 100BASE-T | 100 m |
| 1 Gbps | Gigabit Ethernet | 802.3ab | 1000BASE-T | 100 m |
| 10 Gbps | 10 Gigabit Ethernet | 802.3an | 10GBASE-T | 100 m |
**Giải thích ký hiệu: **
- **BASE**: Tín hiệu băng tần cơ sở (Baseband signaling)
- **T**: Cặp xoắn (Twisted Pair)
**Đặc điểm: **
- Cáp cặp xoắn không có lá chắn kim loại
- Việc xoắn các dây giúp bảo vệ chống nhiễu điện từ EMI (Electromagnetic Interference)
- Hầu hết sử dụng 8 dây (4 cặp)
**Sử dụng dây: **
- **10/100BASE-T**: Chỉ sử dụng 2 cặp (4 dây)
- **1000BASE-T/10GBASE-T**: Sử dụng đầy đủ 4 cặp (8 dây)! [image](https: //github. com/psaumur/CCNA/assets/106411237/00b27997-a78a-4e81-a878-7f8ab7e3279e)
## 02.4 Cách thức giao tiếp qua cáp Ethernet

Mỗi cáp Ethernet có đầu cắm RJ-45 với **8 chân** ở mỗi đầu. ! [image](https: //github. com/psaumur/CCNA/assets/106411237/323930c9-3387-4bf9-aae1-f61db0fd9c04)
**Phân bổ chân: **
- **PC Truyền (TX)**: Chân #1-2
- **switch Nhận (RX)**: Chân #1-2
- **PC Nhận (RX)**: Chân #3. 6
- **switch Truyền (TX)**: Chân #3, 6
Cấu hình này cho phép truyền dữ liệu **Song công toàn phần** (Full-Duplex). ! [image](https: //github. com/psaumur/CCNA/assets/106411237/907259d9-1837-4d53-8f45-a42934fb66f2)
**Phân bổ chân: **
- **router Truyền (TX)**: Chân #1-2
- **router Nhận (RX)**: Chân #3, 6
- **switch Truyền (TX)**: Chân #3. 6
- **switch Nhận (RX)**: Chân #1-2
router và PC kết nối với switch theo cùng một cách, sử dụng **cáp thẳng** (Straight-Through cable). ## 02. 6 Loại cáp kết nối
- Sử dụng để kết nối các thiết bị **khác loại** (PC-switch. router-switch)
- Thứ tự dây ở hai đầu giống nhau
- Sử dụng để kết nối các thiết bị **cùng loại** (PC-PC, switch-switch)
- Hoán đổi các chân ở một đầu để cho phép kết nối hoạt động! [image](https: //github. com/psaumur/CCNA/assets/106411237/d98646ad-366f-4e96-8c6f-f6b5f32f9bdc)
**Sơ đồ hoán đổi chân: **
- CHÂN #1 ↔ CHÂN #3
- CHÂN #2 ↔ CHÂN #6
- CHÂN #3 ↔ CHÂN #1
- CHÂN #6 ↔ CHÂN #2
| Loại thiết bị | Chân truyền (TX) | Chân nhận (RX) |
| ------- | ------- | ------- |
| router | 1 và 2 | 3 và 6 |
| tường lửa | 1 và 2 | 3 và 6 |
| PC | 1 và 2 | 3 và 6 |
| switch | 3 và 6 | 1 và 2 |
**Hầu hết thiết bị hiện đại** đều có tính năng **Auto MDI-X** - tự động phát hiện chân nào mà thiết bị láng giềng đang truyền và điều chỉnh các chân nhận dữ liệu tương ứng. - Sử dụng **4 cặp (8 dây)**
- Mỗi cặp dây hoạt động **hai chiều** (bidirectional)
- Cho phép truyền/nhận nhanh hơn nhiều so với 10/100BASE-T! [image](https: //github. com/psaumur/CCNA/assets/106411237/763c841a-d7b5-4e87-8500-b54d623af620)
## 02.5 Cáp quang (Fiber Optic Cable)

- Được định nghĩa trong tiêu chuẩn **IEEE 802. 3ae**
**SFP** (Small Form-Factor Pluggable) cho phép cáp quang kết nối với switch/router. - Có các cáp riêng biệt để **truyền** và **nhận**! [image](https: //github. com/psaumur/CCNA/assets/106411237/70b81cde-265f-413b-815b-3e7184ea0586)
**Bốn thành phần chính: **
1. **Lõi** (Core): Truyền ánh sáng
2. **Lớp phủ** (Cladding): Phản xạ ánh sáng về lõi
3. **Lớp đệm** (Buffer): Bảo vệ
4. **Vỏ ngoài** (Outer jacket): Bảo vệ tổng thể
## 02.6 A. Cáp đơn mode (Single-Mode)! [image](https: //github. com/psaumur/CCNA/assets/106411237/d9a4b633-44c2-491d-92e4-329dd3b9074b)

**Đặc điểm: **
- Lõi hẹp hơn cáp đa mode
- Ánh sáng truyền theo một góc duy nhất (mode) từ bộ truyền laser
- Cho phép khoảng cách truyền dài nhất
- **Chi phí cao hơn** do sử dụng bộ truyền SFP dựa trên laser
## 02.7 B. Cáp đa mode (Multimode)! [image](https: //github. com/psaumur/CCNA/assets/106411237/e73ec4d0-9aa1-4a75-848c-3af70e770dce)

**Đặc điểm: **
- Lõi rộng hơn cáp đơn mode
- Cho phép nhiều góc (mode) của sóng ánh sáng truyền qua lõi
- Khoảng cách truyền dài hơn UTP nhưng ngắn hơn đơn mode
- **Chi phí thấp hơn** do sử dụng bộ truyền SFP dựa trên LED
| Tiêu chuẩn | Chuẩn IEEE | Tốc độ | Loại mode | Khoảng cách tối đa |
| ------- | ------- | ------- | ------- | ------- |
| 1000BASE-LX | 802.3z | 1 Gbps | Đa mode / Đơn mode | 550 m (Đa) / 5 km (Đơn) |
| 10GBASE-SR | 802.3ae | 10 Gbps | Đa mode | 400 m |
| 10GBASE-LR | 802.3ae | 10 Gbps | Đơn mode | 10 km |
| 10GBASE-ER | 802.3ae | 10 Gbps | Đơn mode | 30 km |
## 02.8 So sánh cáp UTP và cáp quang

**Ưu điểm: **
- Chi phí thấp hơn cáp quang
- Cổng RJ45 rẻ hơn cổng SFP
- Dễ lắp đặt và bảo trì
**Nhược điểm: **
- Khoảng cách tối đa ngắn (~100 m)
- Dễ bị nhiễu EMI (Nhiễu điện từ)
- Phát ra tín hiệu yếu bên ngoài cáp (rủi ro bảo mật)
**Ưu điểm: **
- Khoảng cách truyền dài hơn UTP
- Không bị nhiễu EMI
- Không phát ra tín hiệu bên ngoài cáp (bảo mật cao)
- Băng thông lớn
**Nhược điểm: **
- Chi phí cao hơn UTP
- Cổng SFP đắt hơn cổng RJ45 (đơn mode đắt hơn đa mode)
- Yêu cầu kỹ thuật lắp đặt cao hơn