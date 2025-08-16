# NGÀY 13: LIFE OF A PACKET

## 13.1 KHÁI NIỆM CƠ BẢN! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/ec16b9fd-4d90-4b73-b930-cd825ff13b00)

**MỖI giao diện của Thiết bị Mạng có một địa chỉ MAC DUY NHẤT. **
**Điểm quan trọng về thứ tự địa chỉ:**
- Trong **TCP Header**: địa chỉ IP NGUỒN đến trước địa chỉ IP ĐÍCH
- Trong **Ethernet Header**: địa chỉ MAC ĐÍCH đến trước địa chỉ MAC NGUỒN
- --
## 13.2 QUÁ TRÌNH TRUYỀN GÓI TIN

## 13.3 Bước 1: Host gửi gói tin! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/5eb94811-32f3-47f6-884e-f45a71456e84)

Host nguồn tạo gói tin với: - **IP Header**: Chứa địa chỉ IP nguồn và đích
- **Ethernet Header**: Chứa địa chỉ MAC nguồn và đích (của hop tiếp theo)
## 13.4 Bước 2: Gói tin đến router đầu tiên! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/dc0d05cc-9b76-4921-895d-bfbe78ceb0a7)

router nhận gói tin và: 1. Kiểm tra địa chỉ IP đích trong IP Header
2. Tra cứu bảng định tuyến để tìm next-hop
3. Thay đổi Ethernet Header (MAC nguồn và đích mới)
4. Giữ nguyên IP Header
## 13.5 Bước 3: Gói tin đi qua các router trung gian! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/884f7113-21a9-407f-a38e-44489ae3b47e)

Mỗi router trên đường đi: - **Giữ nguyên**: IP Header (địa chỉ IP nguồn và đích)
- **Thay đổi**: Ethernet Header (địa chỉ MAC cho hop tiếp theo)
- **Giảm**: TTL trong IP Header đi 1! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/36459aeb-e802-4347-b626-0c9cc168c624)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/163bfaf6-15c7-4f7d-9429-4c62a28f0292)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/1f7e5683-00e6-4ce0-b52a-ca8fdb24c87b)
## 13.6 Bước 4: Gói tin đến mạng đích! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/18d04c9d-3734-44e7-995d-b53ab3aaa2a1)

router cuối cùng: 1. Nhận diện mạng đích là directly connected
2. Thay đổi Ethernet Header với MAC của host đích
3. Chuyển tiếp gói tin đến host đích! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/07c44007-a208-47a2-a0e8-ca289f86be75)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/4bcbdba0-234a-4cfa-aa25-cbc3c3c061e1)
## 13.7 Bước 5: Host đích nhận gói tin! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/81c2e8ad-be55-487c-b9da-02540f70b0d9)

Host đích: 1. Kiểm tra địa chỉ MAC đích (phải khớp với MAC của mình)
2. Loại bỏ Ethernet Header
3. Xử lý IP Header và dữ liệu! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/91cfe407-28b5-48e8-b5f8-a60b324e0706)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/4bf8c10b-1240-4e7d-8db4-85ea5f3f619f)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/f938e440-ebdb-444c-b4c7-705d8fd2a4e9)! [image](HTTPS: //github. com/psaumur/CCNA/assets/106411237/1f236bda-d2cf-4252-af3b-bdc5ec5c2aca)
- --
## 13.8 ĐIỂM QUAN TRỌNG CẦN NHỚ

**Khi một HOST gửi gói tin đến HOST khác:**
✅ **KHÔNG THAY ĐỔI:**
- Địa chỉ IP nguồn và đích trong IP Header
- Dữ liệu gốc
⚠️ **THAY ĐỔI TẠI MỖI HOP:**
- Địa chỉ MAC nguồn và đích trong Ethernet Header
- TTL (Time To Live) giảm đi 1
- --
## 13.9 TÓM TẮT QUÁ TRÌNH

1. **Tầng 3 (IP)**: Định tuyến từ nguồn đến đích (không đổi địa chỉ IP)
2. **Tầng 2 (Ethernet)**: Chuyển tiếp từng hop (thay đổi địa chỉ MAC)
3. **Mỗi router**: Tra bảng định tuyến → Tìm next-hop → Cập nhật Ethernet Header
4. **TTL**: Ngăn chặn vòng lặp vô hạn bằng cách giảm dần về 0
**Đây là cơ sở của việc định tuyến trong mạng IP! **