# NGÀY 09: SWITCH INTERFACES

![image](https://github.com/psaumur/CCNA/assets/106411237/5d0d80dc-74d1-4656-841c-fcaa2b89c760)

## 09.1 CISCO CLI CHO SWITCH
![image](https://github.com/psaumur/CCNA/assets/106411237/e3947ef5-9100-426f-8d62-fd4ce5224351)

```
// vào chế độ Privileged EXEC
SW1> enable

// Hiển thị tất cả giao diện của Switch 1
SW1# show ip interface brief
```

Điều này sẽ hiển thị các giao diện hiện tại trên Switch 1. Nó có cùng cấu trúc thông tin như Cisco Router.

Chú ý các cột Trạng thái (Tầng 2) và Giao thức (Tầng 1) đang hiển thị "up/up".

Không giống như ROUTER, SWITCH không Mặc định là 'administratively down/down' (shutdown).

Các thiết bị không kết nối sẽ hiển thị là "down" và "down" (không kết nối với Thiết bị khác)

![image](https://github.com/psaumur/CCNA/assets/106411237/e0fdc339-21d9-4313-b7d8-78303a7ba1ea)

```
// Hiển thị trạng thái của tất cả giao diện trên SW1
SW1# show interfaces status
```

Điều này sẽ liệt kê:

- **Ports** - Cổng
- **Name** (là description) - Tên (là mô tả)
- **Status** (trạng thái kết nối) - Trạng thái
- **VLAN** (có thể được sử dụng để chia LAN)
- VLAN 1 là Mặc định
- **Duplex** (kết nối có thể gửi/nhận cùng lúc không?)
- Auto là Mặc định
- **Speed** (tốc độ tính bằng bps) - Tốc độ
- Auto là Mặc định
- **Type** (phương tiện nào đang được sử dụng, tốc độ của Giao diện) - Loại

- --

![image](https://github.com/psaumur/CCNA/assets/106411237/12a33be7-795f-467a-87a4-42c5b218960b)

![image](https://github.com/psaumur/CCNA/assets/106411237/7b5953f7-77d3-4826-8efc-072498a7f9c0)

- --

## 09.2 PHẠM VI GIAO DIỆN
Các Giao diện không sử dụng có thể gây ra rủi ro Bảo mật nên nên vô hiệu hóa chúng.

Tuy nhiên, nếu bạn có 28+ giao diện không sử dụng, bạn có phải làm từng cái một không?

**Trả lời: Không!**

Có một Lệnh để áp dụng cấu hình cho một phạm vi giao diện.

Trong Chế độ Config Toàn cục (config t):

![image](https://github.com/psaumur/CCNA/assets/106411237/06e2e267-1e07-48a1-8c8c-8edbd5bd48ae)

```
SW1(config)# interface range f0/5 - 12
// Chọn tất cả giao diện từ 0/5 đến 0/12

SW1(config-if-range)# description ## not in use ##

SW1(config-if-range)# shutdown
<< điều này sẽ liệt kê tất cả giao diện được đặt thành administratively down >>
```

Xác nhận bằng 'show interfaces status' trong chế độ Privileged EXEC hoặc nếu trong chế độ CONFIG, sử dụng 'do show interfaces status'

![image](https://github.com/psaumur/CCNA/assets/106411237/8d1d49d3-e000-4570-ab7e-b994b959ebd5)

- --

## 09.3 FULL / HALF DUPLEX
## 09.4 HALF DUPLEX:
- Thiết bị không thể gửi/nhận dữ liệu cùng lúc. Nếu nó đang nhận một Khung, nó phải đợi trước khi gửi một Khung.

## 09.5 FULL DUPLEX:
- Thiết bị có thể gửi/nhận dữ liệu cùng lúc. Nó KHÔNG phải đợi.

**HẦU HẾT SWITCH hiện đại hỗ trợ FULL DUPLEX.**

- --

## 09.6 HALF DUPLEX ĐƯỢC SỬ DỤNG Ở ĐÂU?
Hầu như không có đâu. Trong quá khứ, LAN HUB sử dụng HALF DUPLEX.

Khi nhiều gói tin được Hub nhận, Hub sẽ đơn giản FLOOD các kết nối với dữ liệu Khung, gây ra COLLISION (trên Giao diện), và các host sẽ không nhận được Khung nguyên vẹn.

Tất cả thiết bị kết nối với một Hub được gọi là một **COLLISION DOMAIN**.

Để XỬ LÝ COLLISION, các thiết bị Ethernet sử dụng cơ chế gọi là **CSMA/CD**.

**CSMA/CD = CARRIER SENSE MULTIPLE ACCESS với COLLISION DETECTION.**

- Trước khi gửi khung, các thiết bị 'lắng nghe' collision domain cho đến khi chúng phát hiện rằng các thiết bị khác không gửi.
- NẾU xảy ra collision, Thiết bị gửi tín hiệu jamming để thông báo cho các thiết bị khác rằng đã xảy ra collision.
- Mỗi Thiết bị sẽ đợi một khoảng thời gian ngẫu nhiên trước khi gửi khung lại.
- Quá trình lặp lại.

- --

## 09.7 SWITCH VS HUB
**SWITCH tinh vi hơn HUB.**

**HUB là Thiết bị Tầng 1**
- Collision thường xảy ra và sử dụng CSMA/CD.

**SWITCH là Thiết bị Tầng 2**
- Collision HIẾM KHI xảy ra.

- --

![image](https://github.com/psaumur/CCNA/assets/106411237/feff3816-1449-4282-bc44-71575333a1e0)

## 09.8 TỰ ĐỘNG THƯƠNG LƯỢNG TỐC ĐỘ / DUPLEX
- Các giao diện có thể chạy ở tốc độ khác nhau (10/100 hoặc 10/100/1000) có cài đặt Mặc định là SPEED AUTO và DUPLEX AUTO.
- Các giao diện 'quảng cáo' khả năng của chúng cho Thiết bị láng giềng, và chúng thương lượng cài đặt TỐC ĐỘ và DUPLEX tốt nhất mà cả hai đều có khả năng.

## 09.9 NẾU TỰ ĐỘNG THƯƠNG LƯỢNG BỊ VÔ HIỆU HÓA trên Thiết bị kết nối với Switch?
![image](https://github.com/psaumur/CCNA/assets/106411237/30519cf7-0a79-4996-a8d8-dfac689f4005)

**TỐC ĐỘ:** Switch sẽ cố gắng gửi ở tốc độ mà Thiết bị khác đang hoạt động. Nếu không thể gửi ở tốc độ đó, nó sẽ sử dụng tốc độ chậm nhất được hỗ trợ (tức là: 10 Mbps trên giao diện 10/100/1000).

**DUPLEX:** Nếu tốc độ là 10 hoặc 100 Mbps, Switch sẽ sử dụng HALF DUPLEX. Nếu tốc độ là 1000 Mbps hoặc lớn hơn, nó sẽ sử dụng FULL DUPLEX.

- --

## 09.10 BỘ ĐẾM GIAO DIỆN VÀ LỖI
Hiển thị bằng cách sử dụng:

```
// chế độ Privileged EXEC
SW1# show interfaces <tên giao diện>
```

Thống kê lỗi sẽ ở phía dưới.

![image](https://github.com/psaumur/CCNA/assets/106411237/20d6affd-6014-427d-9ad9-c638ace358f8)

**Gói tin Nhận / Tổng byte nhận.**

**Runts**: Khung nhỏ hơn kích thước khung tối thiểu (64 byte)

**Giants**: Khung lớn hơn kích thước khung tối đa (1518 byte)

**CRC**: Khung không vượt qua kiểm tra CRC (trong Ethernet FCS Trailer)

**Frame**: Khung có định dạng không chính xác (do lỗi)

**Input errors**: Tổng của các bộ đếm khác nhau, chẳng hạn như bốn loại trên

**Output errors**: Khung mà Switch cố gắng gửi, nhưng thất bại do lỗi