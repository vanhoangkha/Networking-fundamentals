# NGÀY 03: OSI MODEL TCPSUITE

## 03.1 Mô hình mạng là gì? - *Mô hình mạng** là khung lý thuyết phân loại và cung cấp cấu trúc cho các giao thức và tiêu chuẩn mạng. > **Giao thức** là tập hợp các quy tắc logic xác định cách các thiết bị mạng và phần mềm hoạt động và giao tiếp với nhau. ## 03. 2 Mô hình OSI (Open Systems Interconnection)

**Mô hình OSI** (Open Systems Interconnection Model) là: - Mô hình khái niệm phân loại và chuẩn hóa các chức năng mạng
- Được phát triển bởi **ISO** (International Organization for Standardization)
- Chia các chức năng mạng thành **7 tầng** (layers)
- Các tầng làm việc phối hợp để đảm bảo hoạt động mạng! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/bbf46de2-e025-4ddd-b52b-614b280598da)
**Đóng gói (Encapsulation)**: Dữ liệu di chuyển từ tầng trên xuống tầng dưới
**Mở gói (De-encapsulation)**: Dữ liệu di chuyển từ tầng dưới lên tầng trên
**Tương tác cùng tầng (Same-layer interaction)**: Các tương tác xảy ra giữa cùng một tầng trên các thiết bị khác nhau! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/b7cf4900-993c-49f0-b6ea-70f4f0719633)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/01f532f6-b636-4b7c-99d0-a67f7e483a99)
## 03.2 Chi tiết 7 tầng của mô hình OSI

**Chức năng chính:**
- Tầng gần nhất với người dùng cuối
- Tương tác trực tiếp với các ứng dụng phần mềm
- Cung cấp giao diện mạng cho ứng dụng
**Các giao thức tiêu biểu:**
- HTTP và HTTPS (Web browsing)
- FTP (File transfer)
- SMTP (Email)
**Chức năng cụ thể:**
- Xác định các đối tác giao tiếp
- Đồng bộ hóa giao tiếp
- Kiểm soát tài nguyên mạng
**Chức năng chính:**
- Dịch dữ liệu giữa định dạng ứng dụng và định dạng mạng
- Mã hóa/giải mã dữ liệu
- Nén/giải nén dữ liệu
- Chuyển đổi định dạng dữ liệu
**Chức năng chính:**
- Kiểm soát các cuộc đối thoại (phiên) giữa các host
- Thiết lập. quản lý và kết thúc kết nối
- Đồng bộ hóa phiên làm việc
- Quản lý checkpoint và recovery
> **Lưu ý quan trọng**: Các kỹ sư mạng thường không làm việc trực tiếp với 3 tầng trên cùng (5-7). Các nhà phát triển ứng dụng chủ yếu làm việc với các tầng này để kết nối ứng dụng qua mạng. **Chức năng chính:**
- Phân đoạn và tái lắp ráp dữ liệu
- Cung cấp giao tiếp **host-to-host** (đầu cuối đến đầu cuối)
- Kiểm soát luồng dữ liệu
- Kiểm soát lỗi end-to-end
**Quá trình xử lý:**
- Nhận dữ liệu từ tầng 5-7
- Thêm **Header tầng 4**
- Tạo ra **SEGMENT** (đoạn)
```
<< DỮ LIỆU + Header L4 >>
```
**Lợi ích của phân đoạn:**
- Chia dữ liệu lớn thành các đoạn nhỏ
- Dễ dàng truyền qua mạng
- Giảm thiểu vấn đề khi có lỗi xảy ra
**Chức năng chính:**
- Cung cấp kết nối giữa các host trên **các mạng khác nhau**
- Cung cấp **địa chỉ logic** (địa chỉ IP)
- Thực hiện **định tuyến** (routing) - lựa chọn đường đi tối ưu
- **router** hoạt động ở tầng này
**Quá trình xử lý:**
- Nhận Segment từ tầng 4
- Thêm **Header tầng 3**
- Tạo ra **PACKET** (gói tin)
```
<< DỮ LIỆU + Header L4 + Header L3 >>
```
**Chức năng chính:**
- Cung cấp kết nối **node-to-node** (nút đến nút)
- Định nghĩa cách định dạng dữ liệu cho phương tiện vật lý
- Phát hiện và sửa lỗi từ tầng vật lý
- Sử dụng **địa chỉ tầng 2** (MAC address)
- **switch** hoạt động ở tầng này
**Quá trình xử lý:**
- Nhận Packet từ tầng 3
- Thêm **Header và Trailer tầng 2**
- Tạo ra **FRAME** (khung)
```
<< Trailer L2 + DỮ LIỆU + Header L4 + Header L3 + Header L2 >>
```
**Ví dụ kết nối node-to-node:**
- PC đến switch
- switch đến router
- router đến router
**Chức năng chính:**
- Định nghĩa các đặc tính vật lý của phương tiện truyền
- Chuyển đổi bit số thành tín hiệu vật lý
- Xác định thông số kỹ thuật phần cứng
**Các đặc tính được định nghĩa:**
- Mức điện áp
- Khoảng cách truyền tối đa
- Đầu nối vật lý
- Thông số kỹ thuật cáp
**Chuyển đổi tín hiệu:**
- **Kết nối có dây**: Bit số → Tín hiệu điện
- **Kết nối không dây**: Bit số → Tín hiệu radio
> **Lưu ý**: Tất cả nội dung trong Ngày 2 (Giao diện và Cáp mạng) đều liên quan đến tầng vật lý. ## 03. 4 PDU (Protocol Data Unit) - Đơn vị dữ liệu giao thức! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/9b885a51-91cd-4fe6-b1be-e7fa7aa220b5)
| Tầng OSI | Tên PDU | Dữ liệu được thêm |
| ------- | ------- | ------- |
| 7-5 | **DATA** (Dữ liệu) | Dữ liệu gốc |
| 4 | **SEGMENT** (Đoạn) | Header tầng 4 |
| 3 | **PACKET** (Gói tin) | Header tầng 3 |
| 2 | **FRAME** (Khung) | Header và Trailer tầng 2 |
| 1 | **BIT** | Tín hiệu vật lý (0 và 1) |
```
<< Trailer L2 + DỮ LIỆU + Header L4 + Header L3 + Header L2 >>
```
## 03.3 Bộ giao thức TCP/IP

**Bộ giao thức TCP/IP** là: - Mô hình khái niệm và tập hợp giao thức thực tế được sử dụng trên Internet
- Được đặt tên theo hai giao thức nền tảng:**TCP** và **IP**
- Được phát triển bởi **DARPA** (Defense Advanced Research Projects Agency) - Bộ Quốc phòng Hoa Kỳ
- **Mô hình thực sự được sử dụng** trong các mạng hiện đại
**Điểm tương đồng:**
- Cấu trúc phân tầng tương tự mô hình OSI
- Cùng nguyên lý đóng gói/mở gói
**Điểm khác biệt:**
- **Ít tầng hơn** (4 tầng thay vì 7 tầng)
- **Thực tế hơn** - được triển khai trong mạng thực
- **Linh hoạt hơn** trong việc ánh xạ giao thức! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/e9593c06-46a3-4ff9-aa01-863e0aeb5df3)
> **Lưu ý quan trọng**: Mặc dù TCP/IP là mô hình thực tế được sử dụng. mô hình OSI vẫn có ảnh hưởng lớn đến cách các kỹ sư mạng suy nghĩ và thảo luận về mạng. ## 03. 6 Tương tác giữa các tầng! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/372c45a0-bb3e-4342-af2b-79d3606384ec)
**Định nghĩa**: Tương tác giữa các tầng khác nhau của mô hình OSI trên **cùng một host**. **Ví dụ thực tế:**
- Tầng 5-7 gửi dữ liệu xuống tầng 4
- Tầng 4 thêm header tầng 4 → tạo ra SEGMENT
- Tầng 4 gửi SEGMENT xuống tầng 3
- Tầng 3 thêm header tầng 3 → tạo ra PACKET
**Định nghĩa**: Tương tác giữa **cùng một tầng** trên các **host khác nhau**. **Lợi ích của khái niệm này:**
- Cho phép tập trung vào tương tác của một tầng cụ thể
- Bỏ qua các tầng khác không liên quan
- Đơn giản hóa việc phân tích và troubleshooting
**Ví dụ thực tế:**
- Tầng ứng dụng của máy chủ web YouTube ↔ Tầng ứng dụng của trình duyệt PC
- Tầng vận chuyển của server ↔ Tầng vận chuyển của client
- Tầng mạng của router A ↔ Tầng mạng của router B