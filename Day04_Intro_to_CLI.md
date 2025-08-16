# NGÀY 04: INTRO TO CLI

## 04.1 CLI là gì? - *CLI** (Command-Line Interface) là **giao diện dòng lệnh** dùng để cấu hình và quản lý các thiết bị Cisco. - *So sánh với GUI: **

- **CLI**: Giao diện dòng lệnh - sử dụng các lệnh văn bản
- **GUI**: Giao diện đồ họa người dùng (Graphical User Interface) - sử dụng chuột và giao diện trực quan
## 04.2 Cách kết nối với thiết bị Cisco

**Cổng Console** là phương pháp kết nối **bắt buộc** khi lần đầu cấu hình thiết bị. **Loại cáp sử dụng:**
- **Cáp Rollover**: Kết nối từ cổng console thiết bị đến máy tính
- **Đầu nối**: DB9 Serial sang RJ45 HOẶC DB9 Serial sang USB! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/0527c007-d607-4bef-8ce1-7b18a177614d)
**Yêu cầu phần mềm:**
- Sử dụng **Terminal Emulator** (Trình giả lập terminal)
- **PuTTY** là lựa chọn phổ biến
- Kết nối qua giao thức **Serial**
| Thông số | Giá trị |
| ------- | ------- |
| **Tốc độ (Baud rate)** | 9600 bit/giây |
| **Bit dữ liệu** | 8 bit |
| **Bit dừng** | 1 bit |
| **Parity** | Không (None) |
| **Kiểm soát luồng** | Không (None) |
## 04.3 Các chế độ CLI

**Dấu nhắc:** `(Hostname)>`
**Đặc điểm:**
- Chế độ mặc định khi đăng nhập lần đầu
- **Quyền hạn hạn chế** - chỉ có thể xem một số thông tin cơ bản
- **KHÔNG thể thực hiện** bất kỳ thay đổi cấu hình nào
- Còn gọi là **"User Mode"**
**Chuyển chế độ:**
```
router> enable
```
**Dấu nhắc:** `(Hostname)#`
**Đặc điểm:**
- **Quyền truy cập hoàn toàn** để xem cấu hình thiết bị
- Có thể khởi động lại thiết bị. lưu file cấu hình
- **KHÔNG thể thay đổi cấu hình** nhưng có thể thực hiện các tác vụ quản trị
- Có thể thay đổi thời gian hệ thống
**Chuyển chế độ:**
```
router# configure terminal
```
hoặc
```
router# conf t
```
**Dấu nhắc:** `router(config)#`
**Đặc điểm:**
- Cho phép **thay đổi cấu hình toàn cục** của thiết bị
- Truy cập từ chế độ Privileged EXEC
- Có thể truy cập các chế độ cấu hình con khác
**Thoát chế độ:**
```
router(config)# exit
```
## 04.4 Các lệnh hỗ trợ CLI

**Dấu hỏi chấm (? )**: Hiển thị danh sách lệnh có sẵn
```
router>? router#? router(config)#? ```
**Trợ giúp theo từ khóa:**
```
router# sh? # Hiển thị tất cả lệnh bắt đầu bằng "sh"
router# show? # Hiển thị tất cả tùy chọn của lệnh "show"
```! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/52454e6f-d5b1-45f0-9a50-e412d356f6d2)
**Phím TAB**: Tự động hoàn thành lệnh khi chỉ có một lựa chọn duy nhất
```
router# conf<TAB> # Tự động thành "configure"
router# sh<TAB> # Tự động thành "show"
```
## 04.5 Cấu hình mật khẩu

**Cấu hình:**
```
router(config)# enable password <mật_khẩu>
```
**Đặc điểm:**
- Mật khẩu **phân biệt chữ hoa chữ thường**
- Được lưu dưới dạng **văn bản thuần túy** trong cấu hình
- **Bảo mật thấp**
**Cấu hình:**
```
router(config)# enable secret <mật_khẩu>
```
**Đặc điểm:**
- **LUÔN được mã hóa** (sử dụng MD5 - cấp độ 5)
- **Bảo mật cao hơn** enable password
- **Ghi đè** enable password khi cả hai được cấu hình
**Kích hoạt mã hóa:**
```
router(config)# service password-encryption
```
**Tác dụng:**
- Mã hóa **tất cả mật khẩu hiện tại** trong cấu hình
- **Mật khẩu tương lai** cũng sẽ được mã hóa tự động
- **KHÔNG ảnh hưởng** đến enable secret (đã được mã hóa sẵn)
- Sử dụng mã hóa Cisco độc quyền (cấp độ 7) - **bảo mật thấp**
**Vô hiệu hóa mã hóa:**
```
router(config)# no service password-encryption
```
**Kết quả khi vô hiệu hóa:**
- Mật khẩu hiện tại **KHÔNG được giải mã**
- Mật khẩu tương lai **KHÔNG được mã hóa**
- Enable secret **KHÔNG bị ảnh hưởng**
## 04.6 Quản lý file cấu hình

**Running Configuration:**
- File cấu hình **hiện tại đang hoạt động**
- Lưu trong **RAM** (bộ nhớ tạm)
- **Mất khi tắt nguồn** thiết bị
- Được chỉnh sửa khi nhập lệnh CLI
**Startup Configuration:**
- File cấu hình được **tải khi khởi động**
- Lưu trong **NVRAM** (bộ nhớ không bay hơi)
- **Không mất khi tắt nguồn**
- Cần lưu thủ công từ running-config
**Xem Running Configuration:**
```
router# show running-config
```
**Xem Startup Configuration:**
```
router# show startup-config
```
**Phương pháp 1:**
```
router# write
Building Configuration. . . [OK]
```
**Phương pháp 2:**
```
router# write memory
Building Configuration. . . [OK]
```
**Phương pháp 3 (khuyến nghị):**
```
router# copy running-config startup-config
Destination filename [startup-config]? Building Configuration. . . [OK]
```
## 04.7 Ví dụ thực tế về mã hóa mật khẩu! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/09c841fe-b5c0-4683-9082-baf060e24c03)

**Kích hoạt mã hóa:**
```
router# conf t
router(config)# service password-encryption
```
**Kết quả:**
- Mật khẩu không còn hiển thị dưới dạng văn bản thuần túy
- Số **"7"** chỉ loại mã hóa Cisco độc quyền (bảo mật thấp)
- Có thể dễ dàng bị crack! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/346f3015-9211-47a9-888f-4e02a013a728)
**Enable Secret:**
- Số **"5"** chỉ mã hóa MD5
- **Bảo mật cao hơn** nhiều so với mã hóa cấp độ 7
- Vẫn có thể bị crack nhưng **khó hơn đáng kể**
## 04.8 Hủy bỏ lệnh cấu hình

**Sử dụng từ khóa "no":**
```
router(config)# no service password-encryption
router(config)# no enable password
router(config)# no enable secret
```! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/2978d101-08d4-4ee3-8995-f36aa1c47d15)
## 04.9 Các hình ảnh minh họa bổ sung! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/e16966a3-674a-4376-bdab-2c06e3659e5f)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/e449e074-bf4c-40f1-a61e-0442ad83f284)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/4c1bdf58-7de6-4074-8189-1573a174474c)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/e7771e65-5ed5-406d-9751-76520713210c)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/5f7357d4-f44b-4a61-a24c-86f3368f30f7)