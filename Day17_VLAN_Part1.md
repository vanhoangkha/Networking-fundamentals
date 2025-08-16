# NGÀY 17: VLAN PART1

## 17.1 LAN LÀ GÌ?
**LAN** là một **BROADCAST DOMAIN** duy nhất, bao gồm tất cả các thiết bị trong Broadcast domain đó.

## 17.2 BROADCAST DOMAIN
**Broadcast Domain** là nhóm các thiết bị sẽ nhận được một Khung Broadcast (Destination MAC: FFFF.FFFF.FFFF) được gửi bởi bất kỳ thành viên nào.

## 17.3 Hình ảnh LAN với BỐN Broadcast Domain (192.168.1.0/24)
![image](https://github.com/psaumur/CCNA/assets/106411237/de712483-e881-41f5-9525-576216186498)

- --

## 17.4 VẤN ĐỀ VỚI LAN TRUYỀN THỐNG
## 17.5 HIỆU SUẤT:
Nhiều lưu lượng Broadcast không cần thiết có thể làm giảm hiệu suất Mạng.

![image](https://github.com/psaumur/CCNA/assets/106411237/a807fdc5-27b9-4735-8b8d-51bdc0c91a8c)

Khung Broadcast làm ngập tất cả subnet với lưu lượng không cần thiết.

![image](https://github.com/psaumur/CCNA/assets/106411237/fcd03904-a193-4423-8940-09be1df1bd2c)

## 17.6 BẢO MẬT:
Ngay cả trong cùng một văn phòng, bạn muốn hạn chế ai có Truy cập vào cái gì.

Bạn có thể áp dụng chính sách Bảo mật trên Router/Tường lửa.

**Vấn đề:** Vì đây là một LAN, PC có thể tiếp cận nhau trực tiếp mà không cần lưu lượng đi qua Router. Vì vậy, ngay cả khi bạn cấu hình chính sách Bảo mật, chúng sẽ không có hiệu lực.

![image](https://github.com/psaumur/CCNA/assets/106411237/7bd562fc-7dff-4692-81d7-c026b007df8f)

- --

## 17.7 VLAN LÀ GÌ?
**VLAN (Virtual Local Area Network):**

- **Tách biệt logic** các end-host tại **TẦNG 2**
- Được **cấu hình trên Switch Tầng 2** trên cơ sở từng Giao diện
- Bất kỳ **END HOST** nào kết nối với Giao diện đó đều là **một phần của VLAN đó**

- --

## 17.8 MỤC ĐÍCH CỦA VLAN
## 17.9 HIỆU SUẤT MẠNG:
- **Giảm lưu lượng Broadcast không cần thiết**, giúp ngăn chặn tắc nghẽn Mạng và cải thiện hiệu suất Mạng

## 17.10 BẢO MẬT MẠNG:
- **Hạn chế lưu lượng Broadcast và Unicast không biết**, cũng cải thiện Bảo mật Mạng, vì thông điệp sẽ không được nhận bởi các thiết bị bên ngoài VLAN

![image](https://github.com/psaumur/CCNA/assets/106411237/fae2f1ed-ffc3-4d91-adf7-16a67c2dc5aa)

**SWITCH không chuyển tiếp lưu lượng trực tiếp giữa các HOST trong VLAN khác nhau**

![image](https://github.com/psaumur/CCNA/assets/106411237/2e5834e9-9096-46eb-bb96-ba8459338107)

![image](https://github.com/psaumur/CCNA/assets/106411237/3046f727-fad4-421e-85ef-63a73e109f83)

## 17.11 Gửi Gói tin đến VLAN khác (Định tuyến qua R1)
![image](https://github.com/psaumur/CCNA/assets/106411237/7090ef6d-ce8c-454f-b80d-f6dfd82745c8)

![image](https://github.com/psaumur/CCNA/assets/106411237/b7237602-5b46-4c31-bd75-2e50e0fb1017)

- --

## 17.12 CÁCH CẤU HÌNH VLAN TRÊN CISCO SWITCH
## 17.13 Lệnh kiểm tra VLAN:
```
#show vlan brief
```

![image](https://github.com/psaumur/CCNA/assets/106411237/13ce8382-6aea-484e-9580-d91c98189522)

**Hiển thị:**
- VLAN nào tồn tại trên Switch
- INTERFACE nào thuộc về mỗi VLAN

**VLAN 1 (Default), 1002-1005** tồn tại theo Mặc định và **không thể xóa (5 VLAN)**

- --

## 17.14 CÁCH GÁN INTERFACE VÀO VLAN
![image](https://github.com/psaumur/CCNA/assets/106411237/ed31145d-7949-4c68-b88a-97716beaf074)

## 17.15 Các bước cấu hình:
**1) Sử dụng lệnh "interface range"** để chọn tất cả interface cùng lúc

**2) Sử dụng lệnh "switchport mode access"** để đặt Interface làm Access Port

- --

## 17.16 ACCESS PORT LÀ GÌ?
**Access Port** là một **SWITCHPORT** thuộc về **một VLAN duy nhất**, và thường kết nối với end host như PC.

**SWITCHPORT** mang nhiều VLAN được gọi là **"Trunk PORT"** (thông tin thêm về Trunk trong chương tiếp theo)

**3) Sử dụng lệnh "switchport access vlan"** để gán VLAN cho Port

![image](https://github.com/psaumur/CCNA/assets/106411237/b1bdb937-3707-496f-bc49-445df354d16b)

- --

## 17.17 TẠO VÀ ĐẶT TÊN VLAN
## 17.18 Tạo VLAN:
```
Switch(config)# vlan <số>
```
Sử dụng **"#vlan <số>"** để vào **Chế độ Cấu hình** cho một VLAN nhất định (điều này cũng có thể tạo VLAN)

## 17.19 Đặt tên VLAN:
```
Switch(config-vlan)# name <tên>
```
Sử dụng **"#name <tên>"** để cấu hình TÊN cho VLAN của bạn

## 17.20 Kiểm tra cấu hình:
```
Switch# show vlan brief
```

![image](https://github.com/psaumur/CCNA/assets/106411237/2f7d26d8-9b2a-43a3-b213-fec4f984a309)

- --

## 17.21 KIỂM TRA VLAN
## 17.22 Test VLAN 10:
Ping từ PC1 sử dụng 255.255.255.255 (FFFF:FFFF:FFFF) làm ngập các gói Broadcast chỉ đến R1 và các host VLAN10

![image](https://github.com/psaumur/CCNA/assets/106411237/5c64e485-f492-4436-9c1d-3a1ab20fbe05)

- --

## 17.23 TÓM TẮT VLAN
## 17.24 Lợi ích chính:
1. **Cải thiện hiệu suất** - Giảm lưu lượng broadcast
2. **Tăng bảo mật** - Tách biệt lưu lượng
3. **Quản lý linh hoạt** - Nhóm thiết bị logic

## 17.25 Các khái niệm quan trọng:
- **Broadcast Domain** = một VLAN
- **Access Port** = thuộc một VLAN duy nhất
- **VLAN 1** = VLAN mặc định (không thể xóa)
- **Inter-VLAN routing** = cần Router để giao tiếp giữa VLAN

## 17.26 Lệnh cơ bản:
```
show vlan brief                    // Xem VLAN
vlan <số>                         // Tạo VLAN
name <tên>                        // Đặt tên VLAN
interface range <range>           // Chọn nhiều interface
switchport mode access            // Đặt làm access port
switchport access vlan <số>       // Gán vào VLAN
```