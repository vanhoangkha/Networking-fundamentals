# NGÀY 11: ROUTING FUNDAMENTALS PART1

## 11.1 ĐỊNH TUYẾN LÀ GÌ? Định tuyến là quá trình mà các router sử dụng để xác định đường đi mà các gói tin IP nên đi qua một Mạng để đến đích. - **router** lưu trữ các tuyến đường đến tất cả các đích đã biết trong một **BẢNG ĐỊNH TUYẾN**

- Khi **router** nhận **GÓI TIN**. chúng tìm trong **BẢNG ĐỊNH TUYẾN** để tìm **Tuyến đường** tốt nhất để chuyển tiếp Gói tin đó. ## 11. 2 HAI PHƯƠNG PHÁP ĐỊNH TUYẾN CHÍNH
Có hai phương pháp Định tuyến chính (phương pháp mà router sử dụng để học các tuyến đường): ## 11. 3 ĐỊNH TUYẾN ĐỘNG:**router** sử dụng Giao thức Định tuyến Động (ví dụ: OSPF) để chia sẻ thông tin Định tuyến với nhau một cách tự động và xây dựng bảng Định tuyến của chúng. ## 11. 4 ĐỊNH TUYẾN TĨNH: Kỹ sư Mạng / Quản trị viên cấu hình thủ công các tuyến đường trên router. ## 11. 5 TUYẾN ĐƯỜNG CHO router BIẾT: Một Tuyến đường cho router biết: - Để gửi một Gói tin đến Đích X. bạn nên gửi gói tin đến ***next-hop*** Y
- hoặc nếu Đích được kết nối trực tiếp với router, *gửi Gói tin trực tiếp đến đích. *
- hoặc nếu Đích là địa chỉ IP của chính router, *nhận Gói tin cho chính mình (không chuyển tiếp). *! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/8ceefb10-d70d-4530-969d-40347ed34297)
## 11.2 WAN (WIDE AREA NETWORK)

**WAN (Mạng Diện Rộng)** = Mạng mở rộng trên một khu vực địa lý lớn. ! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/b3555fdd-37a4-4bc8-b998-76e0b5455bb1)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/99e75230-de1c-4f48-acd0-3482bba256af)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/13a77d5c-497d-49ca-9717-ea3bb4a560d0)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/6e3a2b3b-1590-4625-9bcf-cdaed95738d2)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/891fcfbe-7dc5-4fb2-9b02-c6905236761e)