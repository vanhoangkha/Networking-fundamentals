# 4. GIỚI THIỆU VỀ CLI

### CLI là gì?

- Một "Giao diện dòng lệnh" (Command-line Interface)
- Giao diện mà bạn sử dụng để cấu hình các thiết bị Cisco

GUI là "Giao diện đồ họa người dùng" (Graphical User Interface)

### Làm thế nào để kết nối với thiết bị Cisco?

- Cổng Console: Khi bạn lần đầu cấu hình thiết bị, bạn phải kết nối qua Cổng Console.

Bạn có thể sử dụng "Cáp Rollover": Đầu nối serial DB9 sang RJ45 HOẶC DB9 Serial sang USB

![image](https://github.com/psaumur/CCNA/assets/106411237/0527c007-d607-4bef-8ce1-7b18a177614d)

### Làm thế nào để thực sự truy cập CLI?

- Bạn cần sử dụng TRÌNH GIẢ LẬP TERMINAL (Ví dụ: PuTTy là lựa chọn phổ biến) và kết nối qua "Serial" (Cài đặt mặc định)

### Cài đặt mặc định của Cisco:

Tốc độ (baud): 9600 bit/giây
Bit dữ liệu: 8 bit dữ liệu
Bit dừng: 1 bit dừng (được gửi sau khi 8 bit dữ liệu được gửi)
Parity: Không
Kiểm soát luồng: Không

---

Khi bạn lần đầu vào CLI, bạn sẽ mặc định ở chế độ được gọi là 'User EXEC'.

CHẾ ĐỘ USER EXEC:

(Hostname) >		// Dấu nhắc trông như THẾ NÀY //

- Chế độ User EXEC rất hạn chế.
- Người dùng có thể xem một số thứ nhưng không thể thực hiện BẤT KỲ thay đổi nào đối với Cấu hình.
- Còn gọi là 'Chế độ User'

Sử dụng lệnh 'enable', trong chế độ User EXEC, chuyển bạn sang chế độ 'Privileged EXEC'.

---

CHẾ ĐỘ PRIVILEGED EXEC:

- Cung cấp quyền truy cập hoàn toàn để xem Cấu hình của thiết bị, khởi động lại thiết bị, v.v.
- Không thể thay đổi Cấu hình, nhưng có thể thay đổi thời gian trên thiết bị, lưu file Cấu hình, v.v.

(Hostname)#		// Dấu nhắc trông như THẾ NÀY //

---

SỬ DỤNG dấu hỏi chấm (?) để xem các lệnh có sẵn trong BẤT KỲ chế độ nào. Kết hợp ? với một chữ cái hoặc lệnh một phần sẽ liệt kê tất cả các lệnh có những chữ cái đó.

![image](https://github.com/psaumur/CCNA/assets/106411237/52454e6f-d5b1-45f0-9a50-e412d356f6d2)

SỬ DỤNG phím TAB để hoàn thành các lệnh được nhập một phần NẾU lệnh tồn tại.

---

### CHẾ ĐỘ CẤU HÌNH TOÀN CỤC:

Để vào Chế độ Cấu hình Toàn cục, nhập lệnh trong chế độ Privileged EXEC

'configure terminal' (hoặc 'conf t')

Router# configure terminal
Router(config) #		

Router(config) # run 

Router(config) # no 

Gõ 'exit' để quay lại chế độ 'Privileged EXEC'.

---

### Để kích hoạt Mật khẩu cho chế độ User EXEC:

Router(config)# enable password (mật khẩu)

- Mật khẩu PHÂN BIỆT chữ hoa chữ thường.

// Lệnh này mã hóa mật khẩu văn bản thuần túy, hiển thị trong các file cấu hình, sử dụng mã hóa đơn giản.

Router(config)# service password-encryption

Nếu bạn kích hoạt 'service password-encryption'

- Mật khẩu hiện tại SẼ được mã hóa.
- Mật khẩu tương lai SẼ được mã hóa.
- 'enable secret' SẼ KHÔNG bị ảnh hưởng.

Nếu bạn vô hiệu hóa 'service password-encryption'

- Mật khẩu hiện tại SẼ KHÔNG được giải mã.
- Mật khẩu tương lai SẼ KHÔNG được mã hóa.
- 'enable secret' SẼ KHÔNG bị ảnh hưởng.

// Lệnh này kích hoạt mật khẩu cho chế độ Privileged EXEC.

Router(config)# enable secret (mật khẩu)

// enable secret sẽ LUÔN được mã hóa (ở cấp độ 5)

---

Có HAI file Cấu hình riêng biệt được lưu trên thiết bị cùng một lúc.

Running-config:

- File Cấu hình hiện tại, ĐANG HOẠT ĐỘNG trên thiết bị. Khi bạn nhập lệnh trong CLI, bạn chỉnh sửa Cấu hình đang hoạt động.

Startup-config:

- File Cấu hình sẽ được tải khi KHỞI ĐỘNG LẠI thiết bị.

Để xem các file Cấu hình, trong chế độ 'Privileged EXEC':

Router# show running-config // cho running config //

HOẶC

Router# show startup-config // cho startup config //

---

Để LƯU file Running Configuration, bạn có thể:

Router# write
Building Configuration...
[OK]

Router# write memory
Building Configuration...
[OK]

Router# copy running-config startup-config

Destination filename [startup-config]?

Building Configuration...
[OK]

---

Để mã hóa mật khẩu:

Router# conf t

Router(config)# service password-encryption

Điều này làm cho tất cả mật khẩu hiện tại được *mã hóa*

Mật khẩu tương lai cũng sẽ được *mã hóa*

"enable secret" sẽ không bị ảnh hưởng (nó LUÔN được mã hóa)

![image](https://github.com/psaumur/CCNA/assets/106411237/09c841fe-b5c0-4683-9082-baf060e24c03)

Bây giờ bạn sẽ thấy rằng mật khẩu không còn ở dạng văn bản thuần túy.

"7" đề cập đến loại mã hóa được sử dụng để mã hóa mật khẩu. Trong trường hợp này, "7" sử dụng mã hóa độc quyền của Cisco.

"7" khá dễ bị crack vì mã hóa yếu.

Để có mã hóa TỐT HỠN / MẠNH HƠN, sử dụng "enable secret"

![image](https://github.com/psaumur/CCNA/assets/106411237/346f3015-9211-47a9-888f-4e02a013a728)

"5" đề cập đến mã hóa MD5.

Vẫn có thể bị crack nhưng mạnh hơn rất nhiều.

Khi bạn sử dụng lệnh "enable secret", điều này sẽ ghi đè "enable password"

---

Để HỦY BỎ hoặc xóa một lệnh bạn đã nhập, sử dụng từ khóa "no"

![image](https://github.com/psaumur/CCNA/assets/106411237/2978d101-08d4-4ee3-8995-f36aa1c47d15)

Trong trường hợp này, vô hiệu hóa "service password-encryption":

- mật khẩu hiện tại sẽ KHÔNG được giải mã (không thay đổi)
- mật khẩu tương lai sẽ KHÔNG được mã hóa
- "enable secret" sẽ không bị ảnh hưởng

---

![image](https://github.com/psaumur/CCNA/assets/106411237/e16966a3-674a-4376-bdab-2c06e3659e5f)

![image](https://github.com/psaumur/CCNA/assets/106411237/e449e074-bf4c-40f1-a61e-0442ad83f284)

![image](https://github.com/psaumur/CCNA/assets/106411237/4c1bdf58-7de6-4074-8189-1573a174474c)

![image](https://github.com/psaumur/CCNA/assets/106411237/e7771e65-5ed5-406d-9751-76520713210c)

![image](https://github.com/psaumur/CCNA/assets/106411237/5f7357d4-f44b-4a61-a24c-86f3368f30f7)
