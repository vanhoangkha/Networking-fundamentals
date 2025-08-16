# NGÀY 19: VLAN PART3

## 19.1 NATIVE VLAN TRÊN router (ROAS)! [image](https: //github. com/psaumur/CCNA/assets/106411237/838b9835-d17d-4d57-bac1-52f7e3adfd77)

**Native VLAN untagged frames nhanh hơn và hiệu quả hơn (nhỏ hơn) so với tagged frames. **
Hãy reset tất cả switch (SW1 và SW2) về Native VLAN 10: ! [image](https: //github. com/psaumur/CCNA/assets/106411237/1e903c1b-b814-40b5-aaea-1ba9f3f192c8)
## 19.2 HAI PHƯƠNG PHÁP CẤU HÌNH NATIVE VLAN TRÊN router

## 19.3 Phương pháp 1: Sử dụng Sub-Interface

Sử dụng lệnh **"encapsulation dot1q <VLAN-id>"** trên Sub-Interface: ! [image](https: //github. com/psaumur/CCNA/assets/106411237/2ea65208-6b2a-4cac-a463-982a731c9e24)
## 19.4 Phương pháp 2: Sử dụng Physical Interface

Cấu hình địa chỉ IP cho Native VLAN trên **physical interface** của router (lệnh **"encapsulation dot1q"** KHÔNG cần thiết): ! [image](https: //github. com/psaumur/CCNA/assets/106411237/dabcc3b4-13c3-4d60-abe2-c7cbb5edd4c2)
## 19.5 Kết quả "show running-config" của G0/0 Interface: ! [image](https: //github. com/psaumur/CCNA/assets/106411237/37ce4f0f-0ac0-45ce-802f-5fd11057f69d)

- --
## 19.6 LAYER 3 (MULTILAYER) switch

## 19.7 Biểu tượng xuất hiện: ! [image](https: //github. com/psaumur/CCNA/assets/106411237/0d63f5f9-5efe-4c61-a8e6-3cd6a1161d2a)

## 19.8 Đặc điểm Multilayer switch: - **MULTILAYER switch** có thể cả **Switching và Routing**

- Nó có **LAYER 3 AWARE**
- Bạn có thể gán **địa chỉ IP** cho các L3 Virtual Interface. như một router
- Bạn có thể tạo **Virtual Interface** cho mỗi VLAN và gán địa chỉ IP cho các interface đó
- Bạn có thể cấu hình **routes** trên nó, giống như một router
- Nó có thể sử dụng cho **inter-VLAN routing**! [image](https: //github. com/psaumur/CCNA/assets/106411237/af59481b-d0cb-41d7-9eba-7c8d47131c28)
## 19.9 Thay đổi cấu trúc mạng: **SW2 được thay thế bằng Layer 3 switch**

- Kết nối Multi-VLAN đến R1 được loại bỏ
- Thay thế bằng kết nối Layer 3 point-to-point! [image](https: //github. com/psaumur/CCNA/assets/106411237/8f3ad167-d774-4fcb-96a5-66e568edead8)
- --
## 19.10 SVI (switch VIRTUAL INTERFACE)

## 19.11 Định nghĩa SVI: - **SVI (switch Virtual Interface)** là các virtual interface mà bạn có thể gán địa chỉ IP trong MULTILAYER switch

- Cấu hình mỗi HOST sử dụng **SVI (KHÔNG phải router R1)** làm Gateway Address
- Để gửi lưu lượng đến SUBNET/VLAN khác nhau. PC sẽ gửi lưu lượng đến switch, và switch sẽ định tuyến lưu lượng! [image](https: //github. com/psaumur/CCNA/assets/106411237/5409b2cc-f876-4754-afe3-33298930fd7a)! [image](https: //github. com/psaumur/CCNA/assets/106411237/953372de-579a-4803-9418-0bd1aeef229d)
- --
## 19.12 CẤU HÌNH LẠI R1

## 19.13 Xóa cấu hình R1 để làm việc với kết nối Layer 3 Point-to-Point: ! [image](https: //github. com/psaumur/CCNA/assets/106411237/40354cbe-df39-4a78-97cd-bbb0bc10549c)

## 19.14 Các lệnh quan trọng: ```

router(config)# no interface <sub-interface-id> // Xóa VLAN Interface
router(config)# default interface g0/0 // Reset g0/0 về cài đặt mặc định
```
Sau đó cấu hình Interface G0/0 mặc định của R1 với địa chỉ IP: **192. 168. 1. 194** (theo sơ đồ mạng)
- --
## 19.15 CẤU HÌNH SW2 SỬ DỤNG SVI! [image](https: //github. com/psaumur/CCNA/assets/106411237/24d64087-f98c-4a1e-a07f-3f93f06f93a9)

## 19.16 Các lệnh quan trọng: ```

switch(config)# default interface <interface-id> // Reset interface về mặc định
switch(config)# IP routing // Kích hoạt Layer 3 routing
switch(config-if)# no switchport // Chuyển từ L2 switchport sang L3 routed port
```
**Lệnh "IP routing"** là **QUAN TRỌNG** để kích hoạt Layer 3 Routing trên switch. **Lệnh "no switchport"** cấu hình interface từ Layer 2 Switchport thành Layer 3 "routed port". ## 19. 17 Đặt Default Route: Đặt Default Route đến R1 (192. 168. 1. 194) để tất cả lưu lượng rời khỏi mạng được định tuyến qua Gateway of Last Resort của R1 (Gateway mặc định). ! [image](https: //github. com/psaumur/CCNA/assets/106411237/7a682a2f-3ae3-420b-8f68-9e1050dd82c6)! [image](https: //github. com/psaumur/CCNA/assets/106411237/c0b544b7-8f32-49ae-9a46-d09390a3d08c)
- --
## 19.17 CẤU HÌNH SVI TRÊN SW2

## 19.18 Virtual Layer 3 Routing Interface: ! [image](https: //github. com/psaumur/CCNA/assets/106411237/7c1710fb-40d7-44a4-8336-b037e1c2ea77)

**SVI bị shutdown theo mặc định**, vì vậy nhớ sử dụng **"no shutdown"**! [image](https: //github. com/psaumur/CCNA/assets/106411237/2b5b13c3-1364-4296-886c-0bd9b00b4167)
## 19.19 Tạo SVI không biết (VLAN 40): Khi tạo SVI không biết (VLAN 40), Status/Protocol là **"down/down"**

- --
## 19.20 ĐIỀU KIỆN ĐỂ SVI "UP/UP"

## 19.21 SVI sẽ "up/up" khi: 1. **VLAN phải tồn tại** trên switch

2. **switch phải có ít nhất MỘT Access Port** trong VLAN ở trạng thái "up/up" **VÀ/HOẶC** một Trunk Port cho phép VLAN ở trạng thái "up/up"
3. **VLAN không được shutdown** (bạn có thể sử dụng lệnh "shutdown" để vô hiệu hóa VLAN)
4. **SVI không được shutdown** (SVI bị vô hiệu hóa theo mặc định)! [image](https: //github. com/psaumur/CCNA/assets/106411237/558ef418-5902-42d0-b4a5-cce14b56b77e)
- --
## 19.22 KẾT QUẢ CUỐI CÙNG

**VLAN Trunk đã được thay thế thành công bằng Layer 3 switch SVI. **
Tất cả host nên có thể kết nối với nhau (kiểm tra bằng "ping") cũng như tiếp cận Internet bên ngoài (qua biểu tượng Cloud gắn với R1). - --
## 19.23 TÓM TẮT LAYER 3 switch

## 19.24 Ưu điểm: - **Hiệu suất cao hơn** ROAS (không cần sub-interface)

- **Định tuyến nhanh** giữa các VLAN
- **Giảm tải** cho router chính
- **Linh hoạt** trong thiết kế mạng
## 19.25 Lệnh cấu hình cơ bản: ```

switch(config)# IP routing // Kích hoạt routing
switch(config)# interface VLAN 10 // Tạo SVI
switch(config-if)# IP address 192. 168. 10. 1 255. 255. 255. 0
switch(config-if)# no shutdown // Kích hoạt SVI
switch(config-if)# no switchport // Chuyển sang routed port
```
| ## 19.26 So sánh ROAS vs Layer 3 switch: | Đặc điểm | ROAS | Layer 3 switch |
| ------- | ------- | ------- |
| Hiệu suất | Thấp hơn | Cao hơn |
| Cấu hình | Phức tạp | Đơn giản hơn |
| Chi phí | Thấp | Cao hơn |
| Khả năng mở rộng | Hạn chế | Tốt |