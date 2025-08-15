# 1. THIẾT BỊ MẠNG

## Network là gì??

Network máy tính là một mạng viễn thông số cho phép các NÚT (NODES) chia sẻ TÀI NGUYÊN (RESOURCES).

KHÁCH HÀNG (CLIENT) là thiết bị truy cập dịch vụ được cung cấp bởi MÁY CHỦ (SERVER).

MÁY CHỦ (SERVER) là thiết bị cung cấp chức năng hoặc dịch vụ cho KHÁCH HÀNG (CLIENTS).

- Lưu ý: Cùng một thiết bị có thể là KHÁCH HÀNG trong một số tình huống và là MÁY CHỦ trong các tình huống khác. Ví dụ: Network ngang hàng (Peer-to-Peer network).

SWITCH (Tầng 2):

- cung cấp kết nối cho các host trong cùng một LAN (Network Cục Bộ)
- Có nhiều giao diện mạng/cổng để các End Host kết nối.
- KHÔNG cung cấp kết nối giữa các LAN/qua Internet.

ROUTER (Tầng 3):

- có ít giao diện mạng hơn switch.
- được sử dụng để cung cấp kết nối GIỮA các LAN.
- được sử dụng để gửi dữ liệu qua Internet.

TƯỜNG LỬA (FIREWALL) (Có thể là Tầng 3, 4, và 7):

- Tường lửa là các thiết bị bảo mật mạng phần cứng chuyên dụng kiểm soát lưu lượng mạng vào/ra khỏi mạng của bạn.
- Có thể được đặt "bên trong" hoặc "bên ngoài" mạng.
- Giám sát và kiểm soát lưu lượng mạng dựa trên các quy tắc đã cấu hình.
- Được gọi là "Tường lửa Thế hệ Mới" khi chúng bao gồm các khả năng lọc hiện đại và tiên tiến hơn.
- Tường lửa dựa trên host là các ứng dụng phần mềm lọc lưu lượng vào và ra khỏi máy host, như PC.
