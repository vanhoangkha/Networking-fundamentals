# NGÀY 23: RAPID SPANNING TREE PROTOCOL

## 23.1 SO SÁNH CÁC PHIÊN BẢN STP (Tiêu chuẩn vs. Cisco)! [image](https: //github. com/psaumur/CCNA/assets/106411237/ca5ff85c-842e-4ed3-9b6a-f9d6ed546a78)

| Tiêu chuẩn IEEE | Tên Cisco | Mô tả |
| ------- | ------- | ------- |
| 802.1D | STP | Classic Spanning Tree |
| 802.1w | RSTP | Rapid Spanning Tree |
| 802.1 s | MSTP | Multiple Spanning Tree |
| - | PVST+ | Per-VLAN Spanning Tree Plus |
| - | Rapid PVST+ | Rapid Per-VLAN Spanning Tree Plus |
**Chúng ta chỉ quan tâm đến 802. 1w cho HẦU HẾT các trường hợp sử dụng. MSTP (802. 1 s) hữu ích hơn cho mạng RẤT LỚN. **
- --
## 23.2 RAPID PER-VLAN SPANNING TREE PLUS LÀ GÌ? > **RSTP không phải là thuật toán Spanning Tree dựa trên thời gian như 802. 1D. Do đó, RSTP cung cấp cải tiến so với 30 giây hoặc hơn mà 802. 1D cần để chuyển link sang forwarding. Trái tim của giao thức là cơ chế handshake Bridge-Bridge mới, cho phép port chuyển trực tiếp sang forwarding. **

- --
## 23.3 ĐIỂM TƯƠNG ĐỒNG GIỮA STP VÀ RSTP

- **RSTP phục vụ cùng mục đích** như STP. chặn các PORT cụ thể để ngăn chặn **VÒNG LẶP TẦNG 2**
- **RSTP bầu chọn Root Bridge** với cùng quy tắc như STP
- **RSTP bầu chọn ROOT PORT** với cùng quy tắc như STP
- **RSTP bầu chọn DESIGNATED PORT** với cùng quy tắc như STP
- --
## 23.4 ĐIỂM KHÁC BIỆT GIỮA STP VÀ RSTP

## 23.5 PORT COST! [image](https: //github. com/psaumur/CCNA/assets/106411237/b250c6da-2579-4576-8e93-5a8f8e66d873)

**(HỌC VÀ GHI NHỚ Port Cost của STP và RSTP)**
| Tốc độ Link | STP Cost | RSTP Cost |
| ------- | ------- | ------- |
| 10 Mbps | 100 | 2,000,000 |
| 100 Mbps | 19 | 200.000 |
| 1 Gbps | 4 | 20,000 |
| 10 Gbps | 2 | 2,000 |
| 100 Gbps | N/A | 200 |
| 1 Tbps | N/A | 20 |
- --
## 23.6 RSTP PORT STATES! [image](https: //github. com/psaumur/CCNA/assets/106411237/054d5037-a60e-478e-986b-6f43825a0d1a)

| ## 23.7 So sánh trạng thái: | STP States | RSTP States | Mô tả |
| ------- | ------- | ------- |
| Disabled | **Discarding** | Port bị vô hiệu hóa |
| Blocking | **Discarding** | Port chặn để tránh loop |
| Listening | **Discarding** | Port đang lắng nghe |
| Learning | **Learning** | Port đang học MAC |
| Forwarding | **Forwarding** | Port chuyển tiếp bình thường |
## 23.8 Quy tắc trạng thái RSTP: - Nếu Port bị **VÔ HIỆU HÓA QUẢN TRỊ** (lệnh "shutdown") = **DISCARDING STATE**

- Nếu Port được **BẬT** nhưng **CHẶN lưu lượng** để ngăn **VÒNG LẶP TẦNG 2** = **DISCARDING STATE**
- --
## 23.9 RSTP ROLES

## 23.10 Vai trò không thay đổi: - **ROOT Port role** vẫn không thay đổi trong RSTP

- **DESIGNATED Port role** vẫn không thay đổi trong RSTP
## 23.11 Vai trò mới: **NON-DESIGNATED Port role được chia thành HAI vai trò riêng biệt trong RSTP: **

1. **ALTERNATE Port role**
2. **BACKUP Port role**
- --
## 23.12 RSTP: ALTERNATE PORT ROLE

**RSTP ALTERNATE Port ROLE là DISCARDING Port nhận BPDU superior từ switch khác**
- Điều này **giống như** những gì bạn đã học về **BLOCKING PORT** trong classic STP! [image](https: //github. com/psaumur/CCNA/assets/106411237/7d81e70c-3b31-4448-9d45-9aadb738c74d)
## 23.13 Chức năng Alternate Port: - **ALTERNATE Port** (được gắn nhãn "A" ở trên) hoạt động như **backup cho ROOT Port**

- Nếu **ROOT Port bị lỗi**. switch có thể **ngay lập tức chuyển** Alternate Port tốt nhất sang **FORWARDING**! [image](https: //github. com/psaumur/CCNA/assets/106411237/41f3be85-6225-4749-83b4-f76952c5756a)
💡 **Việc chuyển ngay lập tức sang FORWARDING STATE này hoạt động như tính năng tùy chọn classic STP gọi là UplinkFast. Vì nó được tích hợp vào RSTP, bạn không cần kích hoạt UplinkFast khi sử dụng RSTP/Rapid PVST+**
- --
## 23.14 UPLINKFAST VÀ BACKBONEFAST

## 23.15 BackboneFast: ! [image](https: //github. com/psaumur/CCNA/assets/106411237/c4cea7b7-599f-4ec8-b9d3-a5acba71a5f5)

- **BackboneFast** cho phép SW3 hết hạn **MAX AGE TIMER** trên Interface và nhanh chóng **FORWARD** các BPDU superior đến SW2
- **CHỨC NĂNG này được tích hợp vào RSTP**. vì vậy không cần cấu hình
## 23.16 Tóm tắt: 💡 **UplinkFast và BackboneFast** là hai tính năng tùy chọn trong Classic STP. Chúng phải được cấu hình để hoạt động trên switch (không cần biết cho CCNA)

- **Cả hai tính năng đều được tích hợp vào RSTP**, vì vậy bạn **KHÔNG phải cấu hình** chúng. Chúng hoạt động theo Mặc định
- Bạn **KHÔNG cần hiểu chi tiết** về chúng cho CCNA. Biết tên và mục đích CƠ BẢN (giúp BLOCKING/DISCARDING PORT nhanh chóng chuyển sang FORWARDING)
- --
## 23.17 RSTP: BACKUP PORT ROLE

**RSTP BACKUP Port role là DISCARDING Port nhận BPDU superior từ Interface khác trên cùng switch**
## 23.18 Điều kiện xảy ra: - Điều này chỉ xảy ra khi **HAI INTERFACE được kết nối với cùng COLLISION DOMAIN** (qua Hub)

- **Hub KHÔNG được sử dụng** trong mạng hiện đại. vì vậy bạn có thể sẽ **KHÔNG gặp** RSTP BACKUP Port
- Hoạt động như **BACKUP cho DESIGNATED Port**
💡 **Interface có Port ID THẤP HƠN sẽ được chọn làm DESIGNATED Port, và interface khác sẽ là BACKUP Port. **! [image](https: //github. com/psaumur/CCNA/assets/106411237/61aefc04-b3a9-484a-bbfa-1efe792c73c7)
- --
## 23.19 TƯƠNG THÍCH GIỮA RSTP VÀ CLASSIC STP! [image](https: //github. com/psaumur/CCNA/assets/106411237/be4d404d-829d-41ab-ba39-34e918ed7ea9)! [image](https: //github. com/psaumur/CCNA/assets/106411237/b5dec396-d5fc-486b-9110-5dcc2c4dc4aa)! [image](https: //github. com/psaumur/CCNA/assets/106411237/1930a17b-6c74-4756-b89d-4148008f586b)

💡 **RAPID STP tương thích với CLASSIC STP. **
💡 **Interface trên RAPID STP-enabled switch kết nối với CLASSIC STP-enabled switch sẽ hoạt động trong CLASSIC STP MODE** (Timer, BLOCKING >>> LISTENING >>> LEARNING >>> FORWARDING, v. v. )
- --
## 23.20 RAPID STP BPDU

## 23.21 So sánh CLASSIC STP (TRÁI) vs RAPID STP BPDU (PHẢI): ! [image](https: //github. com/psaumur/CCNA/assets/106411237/2d2deb45-3f81-4c60-b9fa-0f6c3fe7c060)

## 23.22 Khác biệt trong BPDU: **Classic STP BPDU: **

- Protocol Version Identifier: Spanning Tree **(0)**
- BPDU Type: Configuration **(0x00)**
- BPDU flags: **0x00**
**RAPID STP BPDU: **
- Protocol Version Identifier: Spanning Tree **(2)**
- BPDU Type: Configuration **(0x02)**
- BPDU flags: **0x3c**
## 23.23 Khác biệt hoạt động: - Trong **CLASSIC STP**: chỉ **Root Bridge tạo BPDU**. và các switch khác chỉ **CHUYỂN TIẾP** BPDU nhận được

- Trong **RAPID STP**: **TẤT CẢ switch tạo và gửi BPDU riêng** từ **DESIGNATED PORT** của chúng
- --
## 23.24 RAPID SPANNING TREE PROTOCOL

## 23.25 Cải tiến thời gian: - **TẤT CẢ switch chạy RAPID STP** gửi BPDU riêng mỗi **"hello" time (2 Giây)**

- **switch "age" thông tin BPDU** nhanh hơn nhiều: - Trong **CLASSIC STP**: switch đợi **10 "hello" interval (20 giây)**
- Trong **RAPID STP**: switch coi neighbor bị mất nếu **miss 3 BPDU (6 giây)**. Sau đó sẽ **"flush" TẤT CẢ địa chỉ MAC** học được trên Interface đó! [image](https: //github. com/psaumur/CCNA/assets/106411237/c03d2645-42d8-4d95-b486-999e82ac12a8)
- --
## 23.26 RSTP LINK TYPES! [image](https: //github. com/psaumur/CCNA/assets/106411237/e837a271-ad13-4d6a-a800-434a0eff2576)

```
<E> = EDGE
<P> = POINT-TO-POINT
<S> = SHARED
```
**RSTP phân biệt giữa BA "link type" khác nhau: EDGE. POINT-TO-POINT, và SHARED**
- --
## 23.27 EDGE PORTS

- **Kết nối với END HOST**
- Vì **KHÔNG CÓ RỦI RO tạo VÒNG LẶP**, chúng có thể **chuyển thẳng sang FORWARDING STATE** mà không cần quá trình thương lượng! - Chúng hoạt động như **CLASSIC STP Port với PORTFAST ENABLED**
```
switch(config-if)# spanning-tree portfast
```
- --
## 23.28 POINT-TO-POINT PORTS

- **Kết nối trực tiếp** với switch khác
- Hoạt động trong **FULL-DUPLEX**
- Bạn **không cần cấu hình** Interface là POINT-TO-POINT (nó sẽ được phát hiện)
```
switch(config-if)# spanning-tree link-type point-to-point
```
- --
## 23.29 SHARED PORTS

- **Kết nối với switch khác** (hoặc switch) qua **Hub**
- Hoạt động trong **HALF-DUPLEX**
- Bạn **không cần cấu hình** Interface là SHARED (nó sẽ được phát hiện)
```
switch(config-if)# spanning-tree link-type shared
```
- --
## 23.30 BÀI TẬP THỰC HÀNH! [image](https: //github. com/psaumur/CCNA/assets/106411237/a7314f6f-55f0-4e62-bd24-b311b090afe8)

## 23.31 Phân tích topology: **SW1 (Root Bridge): **

- G0/0-0/3 = **DESIGNATED**
**SW2: **
- G0/0 = **ROOT Port**
- G0/1 = **DESIGNATED Port**
- G0/2 = **BACKUP Port**
- G0/3 = **DESIGNATED Port**
**SW3: **
- G0/0 = **DESIGNATED Port**
- G0/1 = **ALTERNATE Port**
- G0/2 = **ROOT Port**
- G0/3 = **DESIGNATED Port**
**SW4: **
- G0/0 = **ROOT Port**
- G0/1 = **ALTERNATE Port**
- G0/2 = **DESIGNATED Port**
## 23.32 Link Types: - Kết nối giữa SW1 G0/0 và SW2 G0/0 = **POINT-TO-POINT**

- Kết nối giữa SW3 G0/0 và SW4 G0/0 = **POINT-TO-POINT**
- Kết nối giữa SW1 G0/1 và G0/2 đến SW3 G0/1 và G0/2 = **POINT-TO-POINT**
- Kết nối đến tất cả END HOST = **EDGE**
- Kết nối từ SW4 đến Hub = **SHARED**
- Kết nối từ SW2 đến Hub = **SHARED**
## 23.33 Đáp án: ! [image](https: //github. com/psaumur/CCNA/assets/106411237/b76eb7be-897a-4617-990e-f399ceaea5f2)

- --
## 23.34 TÓM TẮT RSTP

## 23.35 Ưu điểm chính: - **Hội tụ nhanh hơn** (giây thay vì phút)

- **Tương thích ngược** với Classic STP
- **Tích hợp UplinkFast và BackboneFast**
- **Phân loại link type** tự động
## 23.36 Lệnh cấu hình: ```

spanning-tree mode rapid-pvst // Bật Rapid PVST+
spanning-tree link-type point-to-point // Cấu hình link type
spanning-tree portfast // Edge port
show spanning-tree // Kiểm tra RSTP
```
## 23.37 Port roles RSTP: - **Root Port** - Đường đến Root Bridge

- **Designated Port** - Chuyển tiếp trên segment
- **Alternate Port** - Backup cho Root Port
- **Backup Port** - Backup cho Designated Port (hiếm gặp)