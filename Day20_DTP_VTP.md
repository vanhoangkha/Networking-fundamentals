# NGÀY 20: DTP VTP

## 20.1 DTP (DYNAMIC TRUNKING PROTOCOL)

**DTP** là giao thức cho phép **switch** thương lượng trạng thái của SWITCHPORT mà không cần cấu hình thủ công. để trở thành: - **Access PORT**
- **Trunk PORT**
**DTP được BẬT theo mặc định** trên tất cả Cisco switch Interface
Chúng ta đã cấu hình thủ công SWITCHPORT sử dụng: - `switchport mode access`
- `switchport mode trunk`
💡 **Lệnh kiểm tra:** `show interfaces <interface-id> switchport` sẽ hiển thị cài đặt switchport. **Vì mục đích Bảo mật, khuyến nghị cấu hình thủ công. DTP nên được vô hiệu hóa trên TẤT CẢ SWITCHPORT**! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/bf716a33-8e11-4c09-bb0b-336ba48ef26d)
- --
## 20.2 CÁC CHẾ ĐỘ DTP

## 20.3 DYNAMIC DESIRABLE: - Chế độ này sẽ **chủ động cố gắng** tạo Trunk với switch Cisco khác

- Sẽ tạo Trunk nếu kết nối với SWITCHPORT ở các chế độ sau: - `switchport mode trunk`
- `switchport mode dynamic desirable`
- `switchport mode dynamic auto`
**TUY NHIÊN. . . ** nếu interface khác được đặt thành "static access" (chế độ Access), nó sẽ KHÔNG tạo Trunk, nó sẽ là Access Port
## 20.4 DYNAMIC AUTO: - Chế độ này sẽ **KHÔNG chủ động** cố gắng tạo Trunk với switch Cisco khác

- Sẽ tạo Trunk nếu switch được kết nối đang chủ động cố gắng tạo Trunk
- Nó sẽ tạo Trunk với SWITCHPORT ở các chế độ sau: - `switchport mode trunk`
- `switchport mode dynamic desirable`
**Kết nối Trunk đến Access sẽ hoạt động trong Chế độ Không Khớp (Mismatched Mode). Cấu hình này KHÔNG hoạt động và sẽ gây lỗi. Lưu lượng sẽ KHÔNG hoạt động. **
- --
## 20.5 BẢNG TƯƠNG THÍCH CÁC CHẾ ĐỘ! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/93d5e4f4-cb24-4d3f-ba62-fd002581cfbb)

| ## 20.6 Tóm tắt tương thích: | Chế độ 1 | Chế độ 2 | Kết quả |
| ------- | ------- | ------- |
| Access | Access | Access |
| Access | Dynamic Desirable | Access |
| Access | Dynamic Auto | Access |
| Access | Trunk | **KHÔNG HOẠT ĐỘNG** |
| Dynamic Desirable | Dynamic Desirable | **Trunk** |
| Dynamic Desirable | Dynamic Auto | **Trunk** |
| Dynamic Desirable | Trunk | **Trunk** |
| Dynamic Auto | Dynamic Auto | Access |
| Dynamic Auto | Trunk | **Trunk** |
| Trunk | Trunk | **Trunk** |
- --
## 20.7 THIẾT BỊ KHÔNG HỖ TRỢ DTP

**DTP sẽ KHÔNG tạo Trunk với:**
- router
- PC
- Thiết bị khác. . . **SWITCHPORT sẽ chỉ ở chế độ Access! **
- --
## 20.8 CÀI ĐẶT MẶC ĐỊNH

## 20.9 switch CŨ: - `switchport mode dynamic desirable` = Chế độ quản trị mặc định

## 20.10 switch MỚI: - `switchport mode dynamic auto` = Chế độ quản trị mặc định

- --
## 20.11 VÔ HIỆU HÓA DTP NEGOTIATION

## 20.12 Cách vô hiệu hóa DTP trên Interface: ```

switch(config-if)# switchport nonegotiate
```
HOẶC
```
switch(config-if)# switchport mode access
```
**Khuyến nghị bảo mật:** Vô hiệu hóa DTP trên tất cả SWITCHPORT và cấu hình thủ công làm Access hoặc Trunk port. - --
## 20.13 ENCAPSULATION NEGOTIATION

**switch hỗ trợ cả hai:**
- 802. 1Q
- ISL
Trunk Encapsulation có thể sử dụng DTP để thương lượng Encapsulation sẽ sử dụng. ## 20. 14 Cài đặt mặc định: 💡 `switchport trunk encapsulation negotiate`
## 20.14 Quy tắc ưu tiên: - **ISL được ưu tiên hơn 802. 1Q**

- Nếu CẢ HAI switch hỗ trợ ISL, ISL sẽ được chọn
## 20.15 DTP frames được gửi trong: - **VLAN1** khi sử dụng ISL

- **Native VLAN** khi sử dụng 802. 1Q (Native VLAN mặc định là VLAN1)
- --
## 20.16 VTP (VLAN TRUNKING PROTOCOL)

## 20.17 Lệnh kiểm tra: ```

switch# show vtp status
```
## 20.18 Định nghĩa VTP: - **Giao thức** để cấu hình VLAN trên switch Trung tâm

- Một **SERVER** mà các switch khác đồng bộ hóa (tự động cấu hình bằng kết nối)
- Các switch khác (**VTP CLIENT**) sẽ đồng bộ hóa VLAN database với SERVER
- **Được thiết kế** cho mạng lớn với nhiều VLAN (giảm cấu hình thủ công)
- **HIẾM KHI được sử dụng. Khuyến nghị KHÔNG SỬ DỤNG**
- --
## 20.19 PHIÊN BẢN VTP

## 20.20 Ba phiên bản VTP:**VTP v1: **

- KHÔNG hỗ trợ Extended VLAN Range 1006-4094
**VTP v2:**
- KHÔNG hỗ trợ Extended VLAN Range 1006-4094
- Hỗ trợ Token Ring VLAN; tương tự V1
**VTP v3:**
- Hỗ trợ Extended VLAN Range 1006-4094
- CLIENT lưu trữ VLAN database trong NVRAM
- --
## 20.21 BA CHẾ ĐỘ VTP

## 20.22 SERVER

## 20.23 CLIENT

## 20.24 TRANSPARENT

**Cisco switch hoạt động ở chế độ VTP SERVER theo mặc định**! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/87dcd7ff-f3d3-4441-841c-a0506c249f03)
- --
## 20.25 VTP SERVER

## 20.26 Khả năng: - Có thể **THÊM / SỬA ĐỔI / XÓA** VLAN

- **Lưu trữ** VLAN database trong NVRAM
- **Tăng Revision Number** mỗi khi VLAN được Thêm/Sửa đổi/Xóa
- **Quảng bá Phiên bản Mới nhất** của VLAN database trên Trunk interface
- VTP CLIENT đồng bộ hóa VLAN database với nó
- **VTP SERVER cũng hoạt động như VTP CLIENT**
- **DO ĐÓ. VTP SERVER sẽ đồng bộ hóa với VTP SERVER khác có Revision Number cao hơn**
🚨 **Nguy hiểm của VTP:** Kết nối switch cũ với Revision Number cao hơn vào Mạng (và nếu VTP Domain Name khớp), tất cả switch trong Domain sẽ đồng bộ hóa VLAN database với switch đó
- --
## 20.27 VTP CLIENT

## 20.28 Cấu hình: ```

switch(config)# vtp mode client
```
## 20.29 Đặc điểm: - **Không thể** Thêm/Sửa đổi/Xóa VLAN

- **KHÔNG lưu trữ** VLAN database trong NVRAM
- **VTP v3 CLIENT CÓ lưu trữ**
- Sẽ đồng bộ hóa VLAN database với SERVER có version number cao nhất trong VTP Domain
- Quảng bá VLAN database và chuyển tiếp VTP Advertisement đến CLIENT khác qua Trunk Port
- --
## 20.30 VTP TRANSPARENT MODE

## 20.31 Cấu hình: ```

switch(config)# vtp mode transparent
```
## 20.32 Đặc điểm: - **KHÔNG tham gia** VTP Domain (không đồng bộ VLAN database)

- **Duy trì** VLAN database riêng trong NVRAM
- **Có thể** Thêm/Sửa đổi/Xóa VLAN
- **Không quảng bá** đến switch khác
- **Sẽ chuyển tiếp** VTP advertisement đến switch trong cùng Domain
- --
## 20.33 VTP DOMAIN

## 20.34 Quy tắc tự động tham gia: - Nếu switch không có VTP Domain (Domain NULL) nhận VTP advertisement với VTP Domain name. nó sẽ **tự động tham gia** VTP Domain đó

- Nếu switch nhận VTP advertisement trong cùng VTP domain với revision number cao hơn, nó sẽ **cập nhật VLAN database** để khớp
- --
## 20.35 REVISION NUMBER

## 20.36 Hai cách RESET Revision Number về 0: 1. **Thay đổi VTP Domain** thành Domain chưa sử dụng

2. **Thay đổi VTP mode** thành TRANSPARENT
- --
## 20.37 VTP VERSION NUMBER

## 20.38 Cấu hình: ```

switch(config)# vtp version <version-number>
```
**Thay đổi Version Number sẽ buộc đồng bộ/cập nhật tất cả switch được kết nối lên Version Number mới nhất**
- --
## 20.39 TÓM TẮT VÀ KHUYẾN NGHỊ

## 20.40 Khuyến nghị bảo mật: 1. **Vô hiệu hóa DTP** trên tất cả switchport

2. **Cấu hình thủ công** access/trunk mode
3. **KHÔNG sử dụng VTP** trong môi trường sản xuất
4. **Sử dụng VTP Transparent mode** nếu bắt buộc phải dùng VTP
## 20.41 Lệnh quan trọng: ```

switch(config-if)# switchport nonegotiate // Vô hiệu hóa DTP
switch(config-if)# switchport mode access // Cấu hình access thủ công
switch(config-if)# switchport mode trunk // Cấu hình trunk thủ công
switch(config)# vtp mode transparent // VTP transparent mode
switch# show vtp status // Kiểm tra VTP
switch# show interfaces <int> switchport // Kiểm tra DTP
```