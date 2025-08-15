# 3. MÔ HÌNH OSI & BỘ GIAO THỨC TCP/IP

## Mô hình mạng là gì?

Các mô hình mạng phân loại và cung cấp cấu trúc cho các giao thức và tiêu chuẩn mạng.

(Giao thức là một tập hợp các quy tắc logic xác định cách các thiết bị mạng và phần mềm nên hoạt động)

## MÔ HÌNH OSI

- Mô Hình Kết Nối Hệ Thống Mở (Open Systems Interconnection Model)
- Mô hình khái niệm phân loại và chuẩn hóa các chức năng khác nhau trong mạng.
- Được tạo ra bởi "Tổ Chức Tiêu Chuẩn Hóa Quốc Tế" (ISO)
- Các chức năng được chia thành 7 "Tầng"
- Những tầng này làm việc cùng nhau để làm cho mạng hoạt động.

![image](https://github.com/psaumur/CCNA/assets/106411237/bbf46de2-e025-4ddd-b52b-614b280598da)

Khi dữ liệu di chuyển từ tầng trên xuống dưới, quá trình này được gọi là "đóng gói" (encapsulation)

Khi dữ liệu di chuyển từ tầng dưới lên trên, quá trình này được gọi là "mở gói" (de-encapsulation)

Khi các tương tác xảy ra trên cùng một tầng, nó được gọi là "tương tác cùng tầng" (same-layer interaction)

![image](https://github.com/psaumur/CCNA/assets/106411237/b7cf4900-993c-49f0-b6ea-70f4f0719633)

Câu ghi nhớ để giúp nhớ Tên/Thứ tự các Tầng Dữ liệu

![image](https://github.com/psaumur/CCNA/assets/106411237/01f532f6-b636-4b7c-99d0-a67f7e483a99)

### Các tầng là:

### 7 - ỨNG DỤNG (APPLICATION)

- Tầng này gần nhất với người dùng cuối.
- Tương tác với các ứng dụng phần mềm.
- HTTP và HTTPS là các giao thức Tầng 7

Chức năng của Tầng 7 bao gồm:

- Xác định các đối tác giao tiếp
- Đồng bộ hóa giao tiếp

---

### 6 - TRÌNH BÀY (PRESENTATION)

- Dịch dữ liệu sang định dạng thích hợp (giữa định dạng Ứng dụng và Mạng) để gửi qua mạng.

---

### 5 - PHIÊN (SESSION)

- Kiểm soát các cuộc đối thoại (phiên) giữa các host giao tiếp.
- Thiết lập, quản lý và kết thúc kết nối giữa ứng dụng cục bộ và ứng dụng từ xa.

---

Các kỹ sư mạng thường không làm việc với 3 tầng trên cùng.
Các nhà phát triển ứng dụng làm việc với các tầng trên của mô hình OSI để kết nối ứng dụng của họ qua mạng.

---

### 4 - VẬN CHUYỂN (TRANSPORT)

- Phân đoạn và tái lắp ráp dữ liệu để giao tiếp giữa các host cuối.
- Chia các phần dữ liệu lớn thành các đoạn nhỏ hơn có thể được gửi dễ dàng hơn qua mạng và ít có khả năng gây ra vấn đề truyền tải nếu có lỗi xảy ra.
- Cung cấp giao tiếp HOST-ĐẾN-HOST (đầu cuối đến đầu cuối)

Khi Dữ liệu từ Tầng 7-5 đến, nó nhận được Header Tầng 4 trong tầng Vận chuyển.

<< DỮ LIỆU + Header L4 >>

Điều này được gọi là ĐOẠN (SEGMENT).

---

### 3 - MẠNG (NETWORK)

- Cung cấp kết nối giữa các host cuối trên các mạng khác nhau (tức là: bên ngoài LAN).
- Cung cấp địa chỉ logic (Địa chỉ IP).
- Cung cấp lựa chọn đường đi giữa nguồn và đích
- **ROUTER** hoạt động ở Tầng 3.

Khi Dữ liệu và Header Tầng 4 đến trong Tầng Mạng, nó nhận được Header Tầng 3.

<< DỮ LIỆU + Header L4 + Header L3 >>

Điều này được gọi là **GÓI TIN (PACKET)**.

---

### 2 - LIÊN KẾT DỮ LIỆU (DATA LINK)

- Cung cấp kết nối NÚT-ĐẾN-NÚT và truyền dữ liệu (ví dụ: PC đến Switch, Switch đến Router, Router đến Router)
- Định nghĩa cách dữ liệu được định dạng để truyền qua phương tiện vật lý (ví dụ: cáp UTP đồng)
- Phát hiện và (có thể) sửa lỗi Vật lý (Tầng 1).
- Sử dụng địa chỉ Tầng 2, tách biệt với địa chỉ Tầng 3.
- **SWITCH** hoạt động ở Tầng 2

Khi Gói tin Tầng 3 đến, Header và Trailer Tầng 2 được thêm vào.

<< Trailer L2 + DỮ LIỆU + Header L4 + Header L3 + Header L2 >>

Điều này được gọi là KHUNG (FRAME).

Tất cả các bước dẫn đến việc truyền được gọi là ĐÓNG GÓI (ENCAPSULATION).
Khi khung được gửi đến người nhận, nó sau đó trải qua quá trình ngược lại, MỞ GÓI (DE-ENCAPSULATION), loại bỏ các tầng trong khi di chuyển từ Tầng OSI 1 đến Tầng 7.

---

### 1 - VẬT LÝ (PHYSICAL)

- Định nghĩa các đặc tính vật lý của phương tiện được sử dụng để truyền dữ liệu giữa các thiết bị. Ví dụ: mức điện áp, khoảng cách truyền tối đa, đầu nối vật lý, thông số kỹ thuật cáp.
- Các bit số được chuyển đổi thành tín hiệu điện (cho kết nối có dây) hoặc radio (cho kết nối không dây).
- Tất cả thông tin trong PHẦN 2 (THIẾT BỊ MẠNG) liên quan đến Tầng Vật lý

---

### MÔ HÌNH OSI - PDU

![image](https://github.com/psaumur/CCNA/assets/106411237/9b885a51-91cd-4fe6-b1be-e7fa7aa220b5)

PDU là Đơn vị Dữ liệu Giao thức (Protocol Data Unit). Mỗi bước của quá trình là một PDU.

| SỐ TẦNG OSI | TÊN PDU | DỮ LIỆU GIAO THỨC ĐƯỢC THÊM |
| --- | --- | --- |
| 7-5 | DỮ LIỆU (DATA) | Dữ liệu |
| 4 | ĐOẠN (SEGMENT) | Header Tầng 4 Được Thêm |
| 3 | GÓI TIN (PACKET) | Header Tầng 3 Được Thêm |
| 2 | KHUNG (FRAME) | Trailer và Header Tầng 2 Được Thêm |
| 1 | BIT | Truyền 0 và 1 |

<< Trailer L2 + DỮ LIỆU + Header L4 + Header L3 + Header L2 >>

---

### BỘ GIAO THỨC TCP/IP

- Mô hình khái niệm và tập hợp các giao thức giao tiếp được sử dụng trong Internet và các mạng khác.
- Được biết đến là TCP/IP vì đó là hai trong số các giao thức nền tảng trong bộ giao thức.
- Được phát triển bởi Bộ Quốc phòng Hoa Kỳ thông qua DARPA (Cơ quan Dự án Nghiên cứu Tiên tiến Quốc phòng).
- Cấu trúc tương tự như Mô hình OSI, nhưng ít tầng hơn.
- ĐÂY là mô hình thực sự được sử dụng trong các mạng hiện đại.
- * Lưu ý: Mô hình OSI vẫn ảnh hưởng đến cách các kỹ sư mạng suy nghĩ và nói về mạng.

![image](https://github.com/psaumur/CCNA/assets/106411237/e9593c06-46a3-4ff9-aa01-863e0aeb5df3)

---

### Tương Tác Giữa Các Tầng

![image](https://github.com/psaumur/CCNA/assets/106411237/372c45a0-bb3e-4342-af2b-79d3606384ec)

Tương Tác Tầng Liền Kề:

- Tương tác giữa các tầng khác nhau của Mô hình OSI trên cùng một host.

Ví dụ:

Tầng 5-7 gửi Dữ liệu đến Tầng 4, sau đó thêm header tầng 4 (tạo ra một ĐOẠN).

Tương Tác Cùng Tầng:

- Tương tác giữa cùng một Tầng trên các host khác nhau.
- Khái niệm Tương tác Cùng tầng cho phép bạn bỏ qua các tầng khác liên quan và tập trung vào tương tác giữa một tầng duy nhất trên các thiết bị khác nhau.

Ví dụ:

Tầng Ứng dụng của máy chủ web YouTube và trình duyệt PC của bạn.
