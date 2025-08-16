# NGÀY 27: OSPF PART1

## 27.1 CÁC GIAO THỨC ĐỊNH TUYẾN LINK STATE

- Khi sử dụng một GIAO THỨC ĐỊNH TUYẾN LINK STATE. mỗi router tạo ra một 'bản đồ kết nối' của Mạng
- Để cho phép điều này, mỗi router QUẢNG CÁO thông tin về các GIAO DIỆN của nó (các MẠNG được kết nối) đến các LÁNG GIỀNG của nó. Những QUẢNG CÁO này được chuyển tiếp đến các ROUTERS khác, cho đến khi tất cả ROUTERS trong Mạng phát triển cùng một bản đồ của Mạng
- Mỗi router độc lập sử dụng BẢN ĐỒ này để tính toán CÁC TUYẾN ĐƯỜNG TỐT NHẤT đến mỗi ĐÍCH
- CÁC GIAO THỨC LINK STATE sử dụng nhiều tài nguyên hơn (CPU) trên router. vì NHIỀU thông tin hơn được chia sẻ
- Tuy nhiên, CÁC GIAO THỨC LINK STATE có xu hướng NHANH HƠN trong việc phản ứng với CÁC THAY ĐỔI trong Mạng so với CÁC GIAO THỨC DISTANCE VECTOR
- --
## 27.2 CÁC HOẠT ĐỘNG CƠ BẢN CỦA OSPF

- Viết tắt của **Open Shortest Path First**
- Sử dụng thuật toán **Shortest Path First**
- Được tạo ra bởi nhà khoa học máy tính Hà LAN - Edsger Dijkstra
- còn gọi là **Thuật toán Dijkstra** (Có thể là câu hỏi thi)
**BA Phiên bản:**
- OSPFv1 (1989): CŨ, không còn được sử dụng nữa
- OSPFv2 (1998): Được sử dụng cho IPv4
- OSPFv3 (2008): Được sử dụng cho IPv6 (có thể sử dụng cho IPv4. nhưng v2 thường được sử dụng)
- Routers lưu trữ thông tin về Mạng trong LSAs (Link State Advertisements), được tổ chức trong một cấu trúc gọi là LSDB (Link State Database)
- Routers sẽ **FLOOD** LSAs cho đến khi tất cả ROUTERS trong *area* OSPF phát triển cùng một bản đồ của Mạng (LSDB)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/2a6a126b-74f1-49e2-96be-fc411c8812fd)
💡 LSA có một BỘ ĐẾM THỜI GIAN LÃO HÓA là 30 Phút, theo Mặc định. LSA sẽ được FLOOD lại sau khi bộ đếm thời gian hết hạn
Trong OSPF. có BA BƯỚC CHÍNH trong quá trình chia sẻ LSAs và xác định TUYẾN ĐƯỜNG TỐT NHẤT đến mỗi ĐÍCH trong Mạng: 1) **TRỞ THÀNH LÁNG GIỀNG** với các ROUTERS khác được kết nối với cùng Segment
2) **TRAO ĐỔI LSAs** với các ROUTERS láng giềng
3) **TÍNH TOÁN CÁC TUYẾN ĐƯỜNG TỐT NHẤT** đến mỗi ĐÍCH, và chèn chúng vào BẢNG ĐỊNH TUYẾN
- --
## 27.3 CÁC AREA OSPF

- OSPF sử dụng **AREAS** để chia nhỏ Mạng
- CÁC MẠNG NHỎ có thể là *single-area* mà không có bất kỳ tác động tiêu cực nào đến hiệu suất
- CÁC MẠNG LỚN. thiết kế *single-area* có thể có CÁC TÁC ĐỘNG TIÊU CỰC: - THUẬT TOÁN SPF mất nhiều thời gian hơn để tính toán CÁC TUYẾN ĐƯỜNG
- THUẬT TOÁN SPF yêu cầu sức mạnh xử lý tăng theo cấp số nhân trên CÁC ROUTERS
- LSDB lớn hơn chiếm nhiều BỘ NHỚ hơn trên CÁC ROUTERS
- Những thay đổi nhỏ trong Mạng khiến mọi router FLOOD LSAs và chạy lại thuật toán SPF
- Bằng cách chia một Mạng OSPF lớn thành nhiều ***areas*** NHỎ HƠN, bạn có thể tránh các TÁC ĐỘNG TIÊU CỰC trên (nghe tương tự như VLANs về Broadcast domains)
## 27.4 OSPF AREA là gì? ! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/0f5084fe-f7fb-4b33-a8d0-2ed0155d7502)

- Một **AREA** là tập hợp các ROUTERS và LINKS chia sẻ cùng một LSDB
- **BACKBONE AREA** (Area 0) là AREA mà tất cả các AREAS khác phải kết nối đến
- CÁC ROUTERS với TẤT CẢ CÁC GIAO DIỆN trong CÙNG MỘT AREA được gọi là INTERNAL ROUTERS
- CÁC ROUTERS với CÁC GIAO DIỆN trong NHIỀU AREAS được gọi là **AREA BORDER ROUTERS** (ABRs)
💡 ABRs duy trì một LSDB RIÊNG BIỆT cho mỗi AREA mà chúng được kết nối đến. 💡 Được khuyến nghị rằng bạn kết nối một ABR đến TỐI ĐA HAI AREAS. 💡 Kết nối một ABR đến 3+ AREAS có thể làm quá tải router
- CÁC ROUTERS được kết nối với BACKBONE AREA (Area 0) được gọi là **BACKBONE ROUTERS**
- Một **TUYẾN ĐƯỜNG INTRA-AREA** là tuyến đường đến một ĐÍCH bên trong cùng OSPF AREA
- Một **TUYẾN ĐƯỜNG INTER-AREA** là tuyến đường đến một ĐÍCH trong một OSPF AREA KHÁC
- --
## 27.5 CÁC QUY TẮC OSPF

- CÁC OSPF AREAS nên là LIỀN KỀ (không có AREAS bị tách)
- Tất cả CÁC OSPF AREAS phải có *ít nhất* MỘT ABR được kết nối với BACKBONE AREA
- CÁC GIAO DIỆN OSPF trong CÙNG MỘT Mạng con *phải* nằm trong CÙNG MỘT AREA
- --
## 27.6 CẤU HÌNH OSPF CƠ BẢN

**OSPF AREA 0**! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/ad9648f4-736a-43b5-96de-8a30f6f800c8)
**Các lệnh để cấu hình OSPF**! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/38fcce32-8d15-4db0-9a0c-170d6083a534)
- **Process ID** của OSPF là **có ý nghĩa cục bộ. ** CÁC ROUTERS với Process IDs khác nhau có thể trở thành OSPF Neighbors
- Lệnh "network" của OSPF yêu cầu bạn chỉ định AREA (khi này. là "area 0")
- Đối với CCNA, bạn chỉ cần cấu hình single-area OSPF (AREA 0)
Lệnh "network" yêu cầu OSPF: - Tìm kiếm BẤT KỲ GIAO DIỆN nào với Địa chỉ IP nằm trong PHẠM VI được chỉ định trong lệnh "network"
- Kích hoạt OSPF trên Giao diện trong AREA được chỉ định
- router sau đó sẽ cố gắng trở thành OSPF neighbors với các ROUTERS láng giềng đã kích hoạt OSPF khác! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/41da3fe8-f24a-468c-beeb-91cc12066c70)
- Biết lệnh này từ RIP và EIGRP
- Lệnh "passive-interface" yêu cầu ROUTERS ngừng gửi thông điệp 'hello' OSPF ra khỏi Giao diện
- Tuy nhiên. router sẽ tiếp tục gửi LSA thông báo cho các láng giềng của nó về Mạng con được cấu hình trên Giao diện
- Bạn nên LUÔN SỬ DỤNG lệnh này trên các láng giềng không có bất kỳ OSPF neighbors nào! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/a0422f88-dbd9-4965-8c73-16cfd438b05e)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/aaa1daaa-8ab7-441a-bec2-9f0391a82ecc)
## 27.7 "show IP protocols"! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/f02c3838-c9ad-4836-8c89-ecad42e205b2)

LƯU Ý "no" trong dấu ngoặc vuông - điều này cho biết đây là lựa chọn Mặc định! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/c222d290-4d10-4e63-b7d5-8317ae5ccdfc)
DISTANCE (AD) cho OSPF là 110 (Mặc định) nhưng có thể thay đổi bằng lệnh "distance"! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/849a7fd3-457e-4310-be08-b4c8b4c8a8a2)