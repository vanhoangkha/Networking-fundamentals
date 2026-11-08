# NGÀY 21: SPANNING TREE PROTOCOL PART1

## 21.1 DƯ THỪA TRONG MẠNG

## 21.2 Tầm quan trọng của Redundancy: - **Thiết yếu** trong thiết kế Mạng

- **Mạng hiện đại** được mong đợi chạy 24/7/365; ngay cả thời gian ngừng hoạt động ngắn cũng có thể **thảm khốc cho doanh nghiệp**
- Nếu một thành phần Mạng bị lỗi. bạn phải đảm bảo các thành phần khác sẽ **tiếp quản với ít hoặc không có thời gian ngừng hoạt động**
- Càng nhiều càng tốt, bạn phải **triển khai DƯ THỪA tại mọi điểm có thể** trong Mạng
- --
## 21.3 VÍ DỤ VỀ MẠNG THIẾT KẾ KÉM! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/b3b76af5-11e6-495b-8c40-40eb5800704b)

**Chú ý nhiều điểm lỗi đơn có thể xảy ra (kết nối đơn)**
- --
## 21.4 THIẾT KẾ MẠNG TỐT HƠN! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/01c20d92-2cf6-4d1f-a193-ded7753aeb38)

## 21.5 Lưu ý: - **Hầu hết PC** chỉ có **một card giao diện mạng (NIC)** duy nhất, vì vậy chúng chỉ có thể cắm vào một switch duy nhất

- Tuy nhiên. **SERVER quan trọng** thường có **nhiều NIC**, vì vậy chúng có thể cắm vào nhiều switch để dự phòng! - --
## 21.6 TẠI SAO DƯ THỪA CÓ THỂ LÀ ĐIỀU XẤU? ## 21. 7 BROADCAST STORM! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/a0bf91be-a463-45df-bfc5-df471d0544b5)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/d13b6ab5-5298-4166-bdfa-3315f05a2961)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/f719de69-df9e-4549-b3cb-914d7c5aabc4)

**NGẬP LỤT với ARP REQUEST** (Đỏ = Vòng lặp Thuận chiều kim đồng hồ // Tím = Vòng lặp Ngược chiều kim đồng hồ)
- --
## 21.7 VẤN ĐỀ MAC ADDRESS FLAPPING

**Tắc nghẽn Mạng không phải là vấn đề duy nhất. **
Mỗi khi một Khung đến trên SWITCHPORT, switch sử dụng trường **SOURCE MAC Address** để "học" địa chỉ MAC và cập nhật **MAC ADDRESS TABLE**. Khi các khung với cùng **SOURCE MAC Address** liên tục đến trên các interface khác nhau, switch liên tục cập nhật Interface trong **MAC ADDRESS TABLE**. **Điều này được gọi là MAC ADDRESS FLAPPING**
- --
## 21.8 GIẢI PHÁP: SPANNING TREE PROTOCOL

**Làm thế nào chúng ta thiết kế một Mạng với đường dẫn dự phòng mà không dẫn đến VÒNG LẶP TẦNG 2? **
**Spanning Tree Protocol là giải pháp**
- --
## 21.9 STP (SPANNING TREE PROTOCOL): 802. 1D

## 21.10 Đặc điểm cơ bản: - **"Classic Spanning Tree Protocol"** là IEEE **802. 1D**

- **switch từ TẤT CẢ nhà cung cấp** chạy STP theo Mặc định
- **STP ngăn chặn VÒNG LẶP TẦNG 2** bằng cách đặt các PORT dự phòng trong trạng thái **BLOCKING**. về cơ bản vô hiệu hóa Interface
- Những **INTERFACE này hoạt động như bản sao lưu** có thể vào trạng thái **FORWARDING** nếu Interface đang hoạt động (=hiện đang forwarding) bị lỗi
- **INTERFACE trong trạng thái BLOCKING** chỉ gửi hoặc nhận thông điệp STP (gọi là **BPDU = Bridge Protocol Data Units**)
**Spanning Tree Protocol vẫn sử dụng thuật ngữ "Bridge". Tuy nhiên, khi sử dụng thuật ngữ "Bridge", chúng ta thực sự có nghĩa là "switch". BRIDGE không được sử dụng trong mạng hiện đại. **! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/f253770d-22fa-4e3f-91b0-8f2b4c2f1a61)
**Interface MÀU CAM bị "BLOCKED" gây ra sự gián đoạn trong vòng lặp**! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/45125471-da23-4753-b5b1-16c23a2bfeff)
**Nếu có thay đổi trong kết nối, lưu lượng sẽ điều chỉnh Cấu trúc mạng. **
- --
## 21.11 CÁCH HOẠT ĐỘNG CỦA STP

## 21.12 Nguyên tắc cơ bản: - Bằng cách chọn port nào **FORWARDING** và port nào **BLOCKING**. STP tạo ra **một đường dẫn duy nhất ĐẾN/TỪ mỗi điểm** trong Mạng

- Điều này **ngăn chặn VÒNG LẶP TẦNG 2**
- Có một **quy trình cố định** mà STP sử dụng để xác định port nào nên **FORWARDING** và port nào nên **BLOCKING**
## 21.13 Hello BPDU: - **switch hỗ trợ STP** gửi/nhận **"Hello BPDU"** ra khỏi tất cả INTERFACE

- **Timer mặc định:** **MỖI HAI GIÂY một lần** trên mỗi Interface! - Nếu switch nhận **"Hello BPDU"** trên Interface, nó biết Interface đó được kết nối với switch khác (**router, PC, v. v. KHÔNG sử dụng STP** nên không gửi "Hello BPDU")
- --
## 21.14 BPDU ĐƯỢC SỬ DỤNG ĐỂ LÀM GÌ? ## 21. 16 Bầu chọn Root Bridge: - **switch sử dụng một trường** trong STP BPDU, **trường Bridge ID**. để bầu chọn **Root Bridge** cho Mạng

- **switch có Bridge ID thấp nhất** trở thành **Root Bridge**
- **TẤT CẢ PORT trên Root Bridge** được đặt trong trạng thái **FORWARDING**, và các switch khác trong Cấu trúc mạng phải có đường dẫn để đến **Root Bridge**! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/05177f47-882e-47ea-8bec-22e073392e1c)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/17f921f6-0583-4070-9493-5f5d80ad4866)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/bb49a034-9f6d-4e92-9ea0-8bc71c4f2ec8)
**Để GIẢM Bridge PRIORITY, chúng ta chỉ có thể thay đổi nó theo đơn vị 4096! **! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/39fe6239-1217-4885-b07b-8f368dad0e28)
**Trong Cấu trúc mạng NÀY, SW1 trở thành Root Bridge do địa chỉ MAC của nó THẤP NHẤT (Hex "A" = 10)**! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/b1e1a69d-4b9c-46bf-9b77-f30b9f7c3933)
- --
## 21.15 DESIGNATED PORT

**TẤT CẢ INTERFACE trên Root Bridge là DESIGNATED PORT. DESIGNATED PORT ở trạng thái FORWARDING! **
## 21.16 Quá trình bầu chọn Root Bridge: - Khi switch được bật, nó **giả định mình là Root Bridge**

- Nó sẽ chỉ **từ bỏ vị trí** nếu nhận được **"SUPERIOR" BPDU** (Bridge ID thấp hơn)
- Khi Cấu trúc mạng đã **hội tụ** và tất cả switch đồng ý về Root Bridge. **chỉ Root Bridge gửi BPDU**
- Các switch khác trong Mạng sẽ **chuyển tiếp những BPDU này**, nhưng sẽ **không tạo BPDU gốc riêng**
- --
## 21.17 CÁC BƯỚC CỦA SPANNING TREE PROTOCOL

## 21.18 Bước 1: Bầu chọn Root Bridge

**Một switch được bầu làm Root Bridge. TẤT CẢ PORT trên Root Bridge là DESIGNATED PORT (TRẠNG THÁI FORWARDING)**
**Thứ tự chọn Root Bridge:**
1. **Bridge ID thấp nhất**
2. **Địa chỉ MAC thấp nhất** (khi Bridge ID bằng nhau)
## 21.19 Bước 2: Chọn Root Port

**Mỗi switch còn lại sẽ chọn MỘT trong các INTERFACE của nó làm ROOT PORT (TRẠNG THÁI FORWARDING). PORT đối diện với ROOT PORT luôn là DESIGNATED PORT. **
**Thứ tự chọn Root Port:**
1. **ROOT COST THẤP NHẤT** (xem BẢNG STP COST)
2. **NEIGHBOR Bridge ID THẤP NHẤT**
3. **NEIGHBOR Port ID THẤP NHẤT**
## 21.20 Bước 3: Chọn Designated Port

**Mỗi COLLISION DOMAIN còn lại sẽ chọn MỘT Interface làm DESIGNATED PORT (TRẠNG THÁI FORWARDING). Port khác trong COLLISION DOMAIN sẽ là NON-DESIGNATED (BLOCKING)**
**Chọn DESIGNATED Port:**
1. **Interface trên switch có ROOT COST THẤP NHẤT**
2. **Interface trên switch có Bridge ID THẤP NHẤT**
- --
## 21.21 BẢNG STP COST

**Chỉ có INTERFACE RA NGOÀI hướng về Root Bridge mới có STP COST; không phải INTERFACE NHẬN VÀO. Cộng tất cả chi phí Port RA NGOÀI cho đến khi bạn đến Root Bridge**! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/0ee95883-aed8-42a3-ba82-11209ef8cd40)
| Tốc độ Link | STP Cost |
| ------- | ------- |
| 10 Mbps | 100 |
| 100 Mbps | 19 |
| 1 Gbps | 4 |
| 10 Gbps | 2 |
**SW1 là Root Bridge nên có STP COST là 0 trên TẤT CẢ INTERFACE**! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/35037ae9-3430-44ac-be6d-c8d2a2a42c24)
**PORT kết nối với ROOT PORT của switch khác phải là DESIGNATED (D). Vì ROOT PORT là đường dẫn của switch đến Root Bridge, switch khác không được chặn nó. **
- --
## 21.22 STP PORT ID! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/63d2fb87-31fa-4b57-a2c3-a203feded8ba)

**NEIGHBOR switch Port ID (khi tie-breaker)**
**(D) = DESIGNATED Port**
**(R) = ROOT Port**! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/c3fcc32b-e95f-4d4b-a241-f9f3080e858f)
- --
## 21.23 XÁC ĐỊNH PORT NÀO SẼ BỊ CHẶN! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/1b69a092-4150-44c3-b605-5916fdea91d6)

- --
## 21.24 BÀI TẬP THỰC HÀNH

## 21.25 Xác định Root Bridge và VAI TRÒ của MỖI Interface trên Mạng (ROOT / DESIGNATED / NON-DESIGNATED)

## 21.26 Bài tập #1: ! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/62bcf349-dd89-48be-92f6-d6a184edeb6f)

**Giải:**
- **TẤT CẢ switch có cùng PRIORITY NUMBER (32769)**
- **Tie-breaker** đến **địa chỉ MAC THẤP NHẤT**
- **SW3 có THẤP NHẤT** nên là Root Bridge và **TẤT CẢ INTERFACE của nó trở thành DESIGNATED**
- Kết nối từ SW1 (G0/1) và SW4 (G0/0) đến SW3 trở thành **ROOT INTERFACE**
- Vì SW2 có **HAI kết nối** đến SW1. cả hai interface INCOMING của SW1 trở thành **DESIGNATED**
- SW2 G0/2 Interface trở thành **ROOT Interface** vì G0/0 Interface của SW1 **THẤP HƠN** G0/2 Interface của nó
- Các interface còn lại trên SW2 trở thành **NON-DESIGNATED** vì nó có **ROOT COST CAO NHẤT** (12 = 4 × kết nối 1 GB)
## 21.27 Bài tập #2: ! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/ae382ec2-9c0f-4673-94b5-5d1411c8db6b)

**Giải:**
- **SW4 có Priority Number THẤP NHẤT** nên được chỉ định làm Root Bridge
- **Tất cả INTERFACE của SW4** trở thành **DESIGNATED**
- **SW2 G0/0** trở thành **ROOT Port** vì kết nối SW4 G0/0 có **SỐ THẤP HƠN** G0/1
- **SW3 G0/1** trở thành **ROOT Port**
- **SW1 G0/1** trở thành **ROOT Port** vì chi phí G0/1 **ÍT HƠN** Fa1/0 và 2/0
- **Mỗi Port còn lại** sẽ là **DESIGNATED** hoặc **NON-DESIGNATED**
- **SW1 Fa1/0 và 2/0** trở thành **NON-DESIGNATED** vì chúng có **STP COST CAO HƠN** (38) so với port outbound của SW2 (8) làm cho **SW2 Fa1/0 và 2/0** là **DESIGNATED**
- **Kết nối còn lại của SW2. G0/1**, là **NON-DESIGNATED**