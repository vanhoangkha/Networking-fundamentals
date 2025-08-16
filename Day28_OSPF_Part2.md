# NGÀY 28: OSPF PART2

## 28.1 OSPF METRIC (CHI PHÍ)

- Metric của OSPF được gọi là **CHI PHÍ**
- Nó được tính toán tự động dựa trên băng thông (TỐC ĐỘ) của Giao diện
- Nó được tính toán bằng cách CHIA một giá trị BĂNG THÔNG THAM CHIẾU cho băng thông Giao diện
- BĂNG THÔNG THAM CHIẾU mặc định là 100 mbps
- THAM CHIẾU: 100 mbps / Giao diện: 10 mbps = CHI PHÍ (10)
- THAM CHIẾU: 100 mbps / Giao diện: 100 mbps = CHI PHÍ (1)
- THAM CHIẾU: 100 mbps / Giao diện: 1000 mbps = CHI PHÍ (1)
- THAM CHIẾU: 100 mbps / Giao diện: 10000 mbps = CHI PHÍ (1)
- TẤT CẢ các giá trị CHI PHÍ nhỏ hơn 1 sẽ được CHUYỂN ĐỔI thành 1
- Do đó FastEthernet (100 mbps), Gigabit Ethernet (1000 mbps). 10 Gig Ethernet, v. v. đều BẰNG NHAU và tất cả đều có CHI PHÍ là 1
**CHI PHÍ FastEthernet**! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/453258a2-e724-4bf5-b07c-6c533dcef46c)
**CHI PHÍ Gigabit Ethernet**! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/17adfd0e-8944-4016-93bd-98b82ceb8a66)
Bạn có thể (và NÊN) thay đổi BĂNG THÔNG THAM CHIẾU bằng lệnh này: 💡 `R1(config-router)# auto-cost reference-bandwidth megabits-per-second`
Lệnh được nhập bằng "megabits per second" (Mặc định là "100")
Ví dụ: sử dụng giá trị "100000"
- 100000 / 100 = CHI PHÍ 1000 cho FastEthernet
- 100000 / 1000 = CHI PHÍ 100 cho Gig Ethernet
Bạn nên cấu hình băng thông tham chiếu LỚN HƠN các liên kết NHANH NHẤT trong mạng của bạn (để cho phép nâng cấp trong tương lai)
Thay đổi BĂNG THÔNG THAM CHIẾU cần được thực hiện trên TẤT CẢ CÁC ROUTERS OSPF trong mạng
- --
## 28.2 CHI PHÍ OSPF ĐẾN MỘT ĐÍCH

CHI PHÍ OSPF đến một ĐÍCH là TỔNG CHI PHÍ của các 'GIAO DIỆN outgoing/exit'
CÁC GIAO DIỆN LOOPBACK có CHI PHÍ là 1! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/ef8de0f8-c22d-4259-bf4c-6fc9894bae29)
Để THAY ĐỔI CHI PHÍ OSPF của một Giao diện, bạn sử dụng lệnh: 💡 `R1(config-if)# IP ospf cost <cost>`
CHI PHÍ THỦ CÔNG có ưu tiên hơn CHI PHÍ TÍNH TOÁN TỰ ĐỘNG
Một tùy chọn khác để thay đổi CHI PHÍ OSPF của một Giao diện là thay đổi BĂNG THÔNG của Giao diện bằng lệnh **"bandwidth"**
CÔNG THỨC TÍNH TOÁN CHI PHÍ OSPF là: 💡 **băng thông tham chiếu / băng thông giao diện**
- Mặc dù BĂNG THÔNG khớp với TỐC ĐỘ Giao diện (theo Mặc định). việc thay đổi BĂNG THÔNG Giao diện **không thực sự thay đổi tốc độ mà Giao diện hoạt động**
- BĂNG THÔNG chỉ là GIÁ TRỊ dùng để tính toán CHI PHÍ OSPF, Metric EIGRP, v. v. - Để THAY ĐỔI TỐC ĐỘ mà Giao diện hoạt động, sử dụng lệnh **"speed"**
- Vì GIÁ TRỊ BĂNG THÔNG được sử dụng trong các tính toán khác. KHÔNG được khuyến nghị thay đổi GIÁ TRỊ này để thay đổi CHI PHÍ OSPF của Giao diện
Được KHUYẾN NGHỊ rằng bạn THAY ĐỔI BĂNG THÔNG THAM CHIẾU SAU ĐÓ sử dụng lệnh **"IP ospf cost"** để thay đổi CHI PHÍ của các GIAO DIỆN riêng lẻ, nếu bạn muốn. ! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/00196380-4452-4ec9-8cd9-b1949665a5d8)
- --
## 28.3 TÓM TẮT: BA CÁCH ĐỂ THAY ĐỔI CHI PHÍ OSPF: 1) Thay đổi ***băng thông tham chiếu***

💡 `R1(config-router)# auto-cost reference-bandwidth megabits-per-second`
2) Cấu hình Thủ công: 💡 `R1(config-if)# IP ospf cost <cost>`
3) Thay đổi ***băng thông giao diện***
💡 `R1(config-if)# bandwidth kilobits-per-second`! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/aba02fbc-174c-41a1-a8e3-0ffdda3a6cbd)
- --
## 28.4 TRỞ THÀNH LÁNG GIỀNG OSPF

- Đảm bảo rằng các ROUTERS thành công trở thành LÁNG GIỀNG OSPF là nhiệm vụ CHÍNH trong việc cấu hình và Khắc phục sự cố OSPF
- Một khi các ROUTERS trở thành LÁNG GIỀNG, chúng TỰ ĐỘNG thực hiện công việc chia sẻ thông tin Mạng. tính toán tuyến đường, v. v. - Khi OSPF được kích hoạt trên một Giao diện, router bắt đầu gửi thông điệp **"hello"** OSPF ra khỏi Giao diện theo khoảng thời gian đều đặn (được xác định bởi **"hello timer"**). Những thông điệp này dùng để giới thiệu router với các LÁNG GIỀNG OSPF tiềm năng
- **"hello timer"** mặc định là **10 GIÂY** trên kết nối Ethernet
- Thông điệp **Hello** được Multicast đến **224. 0. 0. 5** (Địa chỉ Multicast cho TẤT CẢ CÁC ROUTERS OSPF)
- Thông điệp OSPF được ĐÓNG GÓI trong IP Header, với **giá trị "89"** trong trường Protocol
## 28.5 TRẠNG THÁI DOWN

- OSPF được kích hoạt trên Giao diện G0/0 của R1
- Nó gửi một thông điệp "hello" OSPF đến 224. 0. 0. 5
- Nó chưa biết về bất kỳ láng giềng OSPF nào, vì vậy trạng thái láng giềng hiện tại là DOWN! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/fa9b91da-e0c3-42d9-8c0a-eb47991b1894)
## 28.6 TRẠNG THÁI INIT

- Khi R2 nhận được gói tin "hello", nó sẽ thêm một mục cho R1 vào bảng láng giềng OSPF của nó
- Trong bảng láng giềng của R2. mối quan hệ với R1 hiện đang ở trạng thái INIT
- Trạng thái INIT = gói tin "hello" đã nhận, nhưng router ID riêng không có trong gói tin "hello"! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/70f3474f-f4bf-4194-b479-d7a65ad82505)
## 28.7 TRẠNG THÁI 2-WAY

- R2 sẽ gửi một gói tin "hello" chứa RID của CẢ HAI ROUTERS
- R1 sẽ chèn R2 vào bảng láng giềng OSPF của nó ở trạng thái 2-WAY
- R1 sẽ gửi một thông điệp "hello" khác. lần này chứa RID của R2
- Cả hai ROUTERS hiện đang ở trạng thái 2-WAY! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/4d5e5310-4680-4176-94ab-2d8015032d18)
- Trạng thái 2-WAY có nghĩa là router đã nhận được một gói tin "hello" với RID riêng của nó trong đó
- Nếu cả hai ROUTERS đạt đến trạng thái 2-WAY. điều đó có nghĩa là TẤT CẢ các điều kiện đã được đáp ứng để chúng trở thành láng giềng OSPF
- Chúng hiện đã SẴN SÀNG CHIA SẺ LSAs để xây dựng một LSDB chung
- Trong MỘT SỐ loại Mạng, một DR (Designated router) và BDR (Backup Designated router) sẽ được bầu chọn tại thời điểm này (Các loại Mạng OSPF và bầu chọn DR/BDR sẽ được thảo luận trong Day 29)
## 28.8 TRẠNG THÁI EXSTART

- HAI ROUTERS hiện sẽ chuẩn bị trao đổi thông tin về LSDB của chúng
- Trước đó. chúng phải chọn cái nào sẽ BẮT ĐẦU việc trao đổi
- Chúng thực hiện ĐIỀU NÀY trong trạng thái EXSTART
- router với RID cao hơn sẽ trở thành MASTER và khởi tạo việc trao đổi
- router với RID thấp hơn sẽ trở thành SLAVE
- Để quyết định MASTER và SLAVE, chúng trao đổi các gói tin DBD (Database DescrIPtion)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/34fa7cca-f837-432b-9296-d1be69a8869c)
## 28.9 TRẠNG THÁI EXCHANGE

- Trong trạng thái EXCHANGE. các ROUTERS trao đổi DBDs chứa DANH SÁCH các LSAs trong LSDB của chúng
- Những DBDs này KHÔNG bao gồm thông tin chi tiết về các LSAs, chỉ THÔNG TIN CƠ BẢN
- Các ROUTERS so sánh thông tin trong DBD mà chúng nhận được với thông tin trong LSDB RIÊNG của chúng để xác định LSAs nào chúng phải nhận từ láng giềng của mình! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/600722df-4737-4a69-867e-662c03a6b4b4)
## 28.10 TRẠNG THÁI LOADING

- Trong trạng thái LOADING. các ROUTERS gửi thông điệp **Link State Requests (LSR)** để yêu cầu láng giềng của chúng GỬI cho chúng bất kỳ LSAs nào mà chúng không có
- LSAs được gửi trong thông điệp **Link State Update (LSU)**
- Các ROUTERS gửi thông điệp **LSAck** để xác nhận rằng chúng đã nhận được các LSAs! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/4fc0fc23-ce00-4381-afef-259091b8f8ef)
## 28.11 TRẠNG THÁI FULL

- Trong trạng thái FULL, các ROUTERS có một adjacency OSPF ĐẦY ĐỦ và các LSDBs giống hệt nhau
- Chúng tiếp tục GỬI và LẮNG NGHE các gói tin "hello" (mỗi 10 giây theo Mặc định) để duy trì adjacency láng giềng
- Mỗi khi một gói tin "hello" được nhận. bộ đếm thời gian "DEAD" (40 giây theo Mặc định) được đặt lại
- Nếu bộ đếm thời gian DEAD đếm ngược về 0 và không có thông điệp "hello" nào được nhận, láng giềng sẽ bị LOẠI BỎ
- Các ROUTERS sẽ tiếp tục chia sẻ LSAs khi Mạng thay đổi để đảm bảo mỗi router có một bản đồ HOÀN CHỈNH và CHÍNH XÁC của Mạng (LSDB)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/daaa3a7b-ddd0-4ad0-ace7-056cbf2fbe32)
- --
## 28.12 TÓM TẮT LÁNG GIỀNG OSPF: ! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/0d9f9d7e-04fd-472c-8449-a4f12172c055)

**1) TRỞ THÀNH LÁNG GIỀNG**
- TRẠNG THÁI DOWN
- TRẠNG THÁI INIT
- TRẠNG THÁI 2-WAY
- (BẦU CHỌN DR/BDR)
**2) TRAO ĐỔI LSAs**
- TRẠNG THÁI EXSTART
- TRẠNG THÁI EXCHANGE
- TRẠNG THÁI LOADING
- TRẠNG THÁI FULL
- --
## 28.13 TÓM TẮT CÁC LOẠI THÔNG ĐIỆP OSPF! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/05b6d3ee-8fdb-4f25-9214-557eeb9a53a6)

- --
## 28.14 CẤU HÌNH OSPF NÂNG CAO

**Kích hoạt OSPF TRỰC TIẾP trên một Giao diện bằng lệnh này:**
💡 `R1(config-if)# IP ospf process-id area area`! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/ad7aafd6-9cd8-4259-bd32-aff7b5893b46)
**Cấu hình TẤT CẢ CÁC GIAO DIỆN làm OSPF Passive Interfaces**
💡 `R1(config-router)# passive-interface default`! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/e953696d-283f-4676-8df2-9aff0418d78d)
Sau đó có thể LOẠI BỎ các GIAO DIỆN cụ thể khỏi việc là passive bằng cách sử dụng: 💡 `R1(config-router)# no passive-interface interface-id`
Kích hoạt OSPF TRỰC TIẾP trên CÁC GIAO DIỆN sẽ hiển thị đầu ra khác trong "show IP protocols"! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/915e31ee-4fee-455b-a947-229e0af4b182)
Chúng sẽ xuất hiện dưới "Routing on Interfaces Configured Explicitly (Area #): " (như trên)
**Hiển thị OSPF LSDB của một Thiết bị**! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/75c941ca-b6bd-45f0-9a85-c7e5baff4654)