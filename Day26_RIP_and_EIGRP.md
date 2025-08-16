# NGÀY 26: RIP AND EIGRP

## 26.1 GIAO THỨC THÔNG TIN ĐỊNH TUYẾN (RIP)

- Routing Information Protocol (Tiêu chuẩn Công nghiệp)
- Là một IGP DISTANCE VECTOR
- Sử dụng logic Định tuyến-Theo-Tin đồn để học/chia sẻ tuyến đường
- Sử dụng SỐ HOP làm Metric (Một router = Một Hop)
- Băng thông không liên quan
- SỐ HOP TỐI ĐA là 15 (bất cứ thứ gì nhiều hơn được coi là không thể đạt được)
- Có BA PHIÊN BẢN: - RIPv1 và RIPv2; được sử dụng cho IPv4
- RIPng (RIP Next Generation) được sử dụng cho IPv6
- Sử dụng HAI LOẠI THÔNG ĐIỆP: - **REQUEST**: Để yêu cầu các ROUTERS láng giềng có RIP gửi BẢNG ĐỊNH TUYẾN của chúng
- **RESPONSE**: Để GỬI BẢNG ĐỊNH TUYẾN của router CỤC BỘ đến các ROUTERS láng giềng
Theo mặc định. các ROUTERS có RIP sẽ chia sẻ BẢNG ĐỊNH TUYẾN của chúng mỗi 30 giây
## 26.2 RIPv1 và RIPv2

**RIPv1: **
- Chỉ quảng cáo *địa chỉ classful* (Class A, Class B. Class C)
- Không hỗ trợ VLSM, CIDR
- Không bao gồm thông tin MASK Mạng con trong CÁC QUẢNG CÁO (thông điệp RESPONSE)
- Ví dụ: - 10. 1. 1. 0/24 sẽ trở thành 10. 0. 0. 0 (Địa chỉ Class A, nên được giả định là /8)
- 172. 16. 192. 0/18 sẽ trở thành 172. 16. 0. 0 (Địa chỉ Class B, nên được giả định là /16)
- 192. 168. 1. 40/30 sẽ trở thành 192. 168. 1. 0 (Địa chỉ Class C, nên được giả định là /24)
- Thông điệp được Broadcast đến 255. 255. 255. 255
**RIPv2: **
- Hỗ trợ VLSM, CIDR
- Bao gồm thông tin MASK Mạng con trong CÁC QUẢNG CÁO
- Thông điệp được **Multicast** đến 224. 0. 0. 9
- Thông điệp Broadcast được gửi đến TẤT CẢ thiết bị trên mạng cục bộ
- Thông điệp Multicast chỉ được gửi đến các thiết bị đã tham gia ***nhóm Multicast*** cụ thể đó
- --
## 26.3 CÂU HÌNH RIP! [image](https: //github. com/psaumur/CCNA/assets/106411237/1d14ec8b-121c-4666-b608-1e5d1889424c)

Lệnh **"network"** yêu cầu router: - Tìm kiếm CÁC GIAO DIỆN với Địa chỉ IP nằm trong PHẠM VI cụ thể
- KÍCH HOẠT RIP trên các GIAO DIỆN nằm trong PHẠM VI
- Tạo ADJACENCIES với các láng giềng RIP được kết nối
- Quảng cáo **PREFIX MẠNG của Giao diện** (KHÔNG phải prefix trong lệnh "network")
Các lệnh **"network"** của OSPF và EIGRP hoạt động theo cách tương tự
Vì lệnh "network" của RIP là CLASSFUL. nó sẽ tự động chuyển đổi thành mạng CLASSFUL: - 10. 0. 0. 0 được giả định là 10. 0. 0. 0/8
- R1 sẽ tìm kiếm BẤT KỲ GIAO DIỆN nào với Địa chỉ IP khớp với 10. 0. 0. 0/8 (vì nó là /8, nó chỉ cần khớp 8 bit ĐẦU TIÊN)
- 10. 0. 12. 1 và 10. 0. 13. 1 đều khớp NÊN RIP được KÍCH HOẠT trên G0/0 và G0/1
- R1 sau đó tạo ADJACENCIES với các láng giềng R2 và R3
- R1 QUẢNG CÁO 10. 0. 12. 0/30 và 10. 0. 13. 0/30 (KHÔNG phải 10. 0. 0. 0/8) đến các láng giềng RIP của nó! [image](https: //github. com/psaumur/CCNA/assets/106411237/2a9452f0-b48f-499d-938f-0a3db5ff6587)
- Vì lệnh "network" là CLASSFUL, 172. 16. 0. 0 được giả định là 172. 16. 0. 0/16
- R1 sẽ tìm kiếm BẤT KỲ GIAO DIỆN nào khớp với 172. 16. 0. 0/16
- 172. 16. 1. 14 khớp, nên R1 sẽ KÍCH HOẠT RIP trên G2/0
- KHÔNG có láng giềng RIP được kết nối với G2/0 nên không có ADJACENCIES MỚI được tạo
- Mặc dù KHÔNG có láng giềng RIP. R1 vẫn sẽ gửi CÁC QUẢNG CÁO ra khỏi G2/0
- Đây là traffic không cần thiết, nên G2/0 nên được cấu hình như một **giao diện passive**! [image](https: //github. com/psaumur/CCNA/assets/106411237/634f4c6b-291c-4a21-8ae2-c8283044efce)
- Lệnh "passive-interface" yêu cầu router ngừng gửi quảng cáo RIP ra khỏi Giao diện được chỉ định (G2/0)
- Tuy nhiên. router sẽ tiếp tục QUẢNG CÁO prefix mạng của Giao diện (172. 16. 1. 0/28) đến các láng giềng RIP của nó (R2. R3)
- Bạn nên LUÔN sử dụng lệnh này trên CÁC GIAO DIỆN không có láng giềng RIP nào
- EIGRP và OSPF đều có chức năng giao diện passive tương tự, sử dụng cùng lệnh
- --
## 26.4 CÁCH QUẢNG CÁO TUYẾN ĐƯỜNG MẶC ĐỊNH VÀO RIP! [image](https: //github. com/psaumur/CCNA/assets/106411237/57de003e-0e8e-48c7-bb72-fbe25208d847)! [image](https: //github. com/psaumur/CCNA/assets/106411237/1c500efd-e96b-4e49-b1f4-f99c54b0e877)

Để CHIA SẺ Tuyến đường Mặc định này với các láng giềng RIP của R1, sử dụng lệnh này: ! [image](https: //github. com/psaumur/CCNA/assets/106411237/799d818a-06cc-4f29-8c74-c67639c9d014)
RIP không quan tâm đến chi phí AD của Giao diện (chi phí RIP là 120), chỉ quan tâm "hops". Vì cả hai đều có số "hops" bằng nhau, cả hai đường đi đều xuất hiện trong Tuyến đường Mặc định (Gateway of Last Resort)! [image](https: //github. com/psaumur/CCNA/assets/106411237/1deccb54-02e0-4d3b-b203-277d656504b3)
- --
## 26.5 "show IP protocols" (cho RIP)! [image](https: //github. com/psaumur/CCNA/assets/106411237/b7ab4046-b6eb-4e19-b7eb-2c5d2889293a)

"Maximum path: 4" là giá trị Mặc định nhưng có thể thay đổi bằng lệnh này: ! [image](https: //github. com/psaumur/CCNA/assets/106411237/35d524bd-055d-4c5e-a84b-f507a87738e0)
"Distance" (AD) có thể thay đổi bằng lệnh này (Mặc định là 120): ! [image](https: //github. com/psaumur/CCNA/assets/106411237/5247942b-1d6b-419f-a4c7-75bfcca43fe6)
- --
## 26.6 GIAO THỨC ĐỊNH TUYẾN GATEWAY NỘI BỘ NÂNG CAO (EIGRP)

- Enhanced Interior Gateway Routing Protocol
- Là một IGP DISTANCE VECTOR
- Trước đây là độc quyền của Cisco. nhưng Cisco hiện đã công bố công khai để các nhà cung cấp khác có thể triển khai trên thiết bị của họ
- Được coi là GIAO THỨC ĐỊNH TUYẾN DISTANCE VECTOR "nâng cao" / "lai"
- Nhanh hơn nhiều so với RIP trong việc phản ứng với các thay đổi trong mạng
- KHÔNG có giới hạn 15 'hop count' của RIP
- Gửi thông điệp sử dụng Địa chỉ Multicast **224. 0. 0. 10 (Ghi nhớ số này)**
- Là IGP DUY NHẤT có thể thực hiện cân bằng tải chi phí **không bằng nhau** (Theo mặc định, nó thực hiện cân bằng tải ECMP trên 4 đường đi như RIP)
- --
## 26.7 CẤU HÌNH EIGRP! [image](https: //github. com/psaumur/CCNA/assets/106411237/f2b42631-bcb9-4f62-afe9-b7bb1e7e0d7e)

"router EIGRP <Số Autonomous System>"
- Số AS (Autonomous System) phải KHỚP giữa các ROUTERS hoặc chúng sẽ KHÔNG tạo ADJACENCY và chia sẻ thông tin Tuyến đường
- Auto-summary có thể BẬT hoặc TẮT theo Mặc định; tùy thuộc vào phiên bản router/IOS. Nếu được BẬT, hãy Vô hiệu hóa nó. - Lệnh **"network"** sẽ giả định một Địa chỉ CLASSFUL. nếu bạn không chỉ định MASK Mạng con
- EIGRP sử dụng *wildcard mask* thay vì mask Mạng con thông thường
**WILDCARD MASK** là MASK Mạng con "đảo ngược": - Tất cả số 1 trong MASK Mạng con là 0 trong WILDCARD MASK tương đương
- Tất cả số 0 trong MASK Mạng con là 1 trong WILDCARD MASK tương đương! [image](https: //github. com/psaumur/CCNA/assets/106411237/f64e06d3-75ad-4f4f-b7d6-26f27ffae541)
"0" trong WILDCARD MASK = CÁC BIT phải KHỚP! "1" trong WILDCARD MASK = Không cần khớp! [image](https: //github. com/psaumur/CCNA/assets/106411237/13130e3c-de62-4f80-9c7d-256a2ed47e74)! [image](https: //github. com/psaumur/CCNA/assets/106411237/1aa2cd2c-397f-4f3b-86ed-81eddf2677a6)! [image](https: //github. com/psaumur/CCNA/assets/106411237/500ac3b0-5d83-4691-ab94-06fd330a9111)
- --
## 26.8 "show IP protocols" (cho EIGRP)! [image](https: //github. com/psaumur/CCNA/assets/106411237/f3f169da-d733-4da9-8d8a-c90e2077d8a7)

**"router ID"**
Thứ tự ưu tiên của router ID: - Cấu hình Thủ công
- Địa chỉ IP Cao nhất trên GIAO DIỆN LOOPBACK
- Địa chỉ IP Cao nhất trên GIAO DIỆN VẬT LÝ! [image](https: //github. com/psaumur/CCNA/assets/106411237/29757624-9e79-4878-8724-36d5da43f39b)
**"Distance" (AD)**
EIGRP có HAI GIÁ TRỊ: - Internal = 90
- External = 170
GHI NHỚ NHỮNG GIÁ TRỊ NÀY! **"show IP route" (cho EIGRP)**! [image](https: //github. com/psaumur/CCNA/assets/106411237/8216ceb6-0d3f-42e7-8e5b-46e810097fb8)
LƯU Ý các số Metric lớn. Đây là NHƯỢC ĐIỂM của EIGRP - ngay cả trên các mạng nhỏ! - --
## 26.9 EIGRP METRIC

- Theo mặc định, EIGRP sử dụng BANDWIDTH và DELAY để tính toán Metric
- Các giá trị "K" mặc định là: - K1 = 1, K2 = 0. K3 = 1, K4 = 0, K5 = 0
💡 **Tính toán đơn giản**: Metric = BANDWIDTH (Liên kết Chậm nhất) + DELAY (của TẤT CẢ CÁC LIÊN KẾT)
- --
## 26.10 THUẬT NGỮ EIGRP

- **Feasible Distance** = Giá trị Metric của router này đến ĐÍCH của tuyến đường
- **Reported Distance** (còn gọi là **Advertised Distance**) = Giá trị Metric của láng giềng đến ĐÍCH của tuyến đường! [image](https: //github. com/psaumur/CCNA/assets/106411237/436ba2c2-43e7-4fea-a527-f88a8e4460bc)
- **Successor** = tuyến đường với Metric THẤP NHẤT đến ĐÍCH (tuyến đường tốt nhất)
- **Feasible Successor** = Tuyến đường thay thế đến ĐÍCH (không phải tuyến đường tốt nhất) đáp ứng *điều kiện khả thi*
**ĐIỀU KIỆN KHẢ THI**: Một tuyến đường được coi là ***Feasible Successor*** nếu ***Reported Distance*** của nó THẤP HƠN ***Feasible distance*** của tuyến đường Successor! [image](https: //github. com/psaumur/CCNA/assets/106411237/206db633-3a7e-4d11-bb80-029ea8107503)
- --
## 26.11 EIGRP: CÂN BẰNG TẢI CHI PHÍ KHÔNG BẰNG NHAU! [image](https: //github. com/psaumur/CCNA/assets/106411237/23a2045b-a925-4f75-b0f8-78cbae2aa1e2)

"maximum-paths 4" = giá trị Mặc định
Variance 1 = chỉ cân bằng tải ECMP (Equal-Cost Multiple Path) sẽ được thực hiện! [image](https: //github. com/psaumur/CCNA/assets/106411237/824dac1d-38dc-4e7e-bb48-b382918230ff)
Variance 2 = các tuyến đường ***feasible successor*** với FD lên đến 2x FD của tuyến đường ***successor*** có thể dùng để cân bằng tải
💡 EIGRP sẽ chỉ thực hiện CÂN BẰNG TẢI CHI PHÍ KHÔNG BẰNG NHAU trên các TUYẾN ĐƯỜNG ***feasible successor***. Nếu một tuyến đường không đáp ứng ***điều kiện khả thi***, nó sẽ KHÔNG BAO GIỜ được chọn cho cân bằng tải, bất kể **variance**