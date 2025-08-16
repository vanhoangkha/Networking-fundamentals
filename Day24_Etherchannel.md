# NGÀY 24: ETHERCHANNEL

## 24.1 ETHERCHANNEL LÀ GÌ?
**EtherChannel** cho phép bạn **NHÓM nhiều INTERFACE vật lý** thành một nhóm hoạt động như **MỘT INTERFACE LOGIC duy nhất** - vì vậy chúng **HOẠT ĐỘNG như thể chúng là một interface duy nhất**

## 24.2 Phân loại EtherChannel:
**LAYER 2 EtherChannel:**
- Là một nhóm **Switch PORT** hoạt động như **MỘT INTERFACE duy nhất**

**LAYER 3 EtherChannel:**
- Là một nhóm **ROUTED PORT** hoạt động như **MỘT INTERFACE duy nhất** mà bạn gán **một địa chỉ IP**

- --

## 24.3 VẤN ĐỀ OVERSUBSCRIPTION
![image](https://github.com/psaumur/CCNA/assets/106411237/86cecd4a-1554-4ece-8a88-6f97e24788f1)

Khi **băng thông của INTERFACE kết nối với END HOST** lớn hơn **băng thông kết nối đến DISTRIBUTION Switch**, điều này được gọi là **OVERSUBSCRIPTION.**

- Một số **OVERSUBSCRIPTION có thể chấp nhận được**, nhưng quá nhiều sẽ gây tắc nghẽn

- --

## 24.4 VẤN ĐỀ VỚI SPANNING TREE
![image](https://github.com/psaumur/CCNA/assets/106411237/6ada996f-8fd4-4339-9ad7-d52e51a3553e)

- Nếu bạn kết nối **HAI SWITCH** với nhau bằng **nhiều link**, **TẤT CẢ trừ MỘT** sẽ bị **VÔ HIỆU HÓA bởi Spanning Tree Protocol** (Đèn Xanh vs. Đèn Cam ở trên ASW1)

## 24.5 TẠI SAO?
- Nếu **TẤT CẢ INTERFACE của ASW1** đều **FORWARDING**, **VÒNG LẶP TẦNG 2** sẽ hình thành giữa ASW1 và DSW1, dẫn đến **Broadcast STORM** (Xấu!)
- **Các link khác sẽ không được sử dụng** trừ khi link đang hoạt động bị lỗi. Trong trường hợp đó, một trong các link không hoạt động sẽ bắt đầu forwarding

- --

## 24.6 GIẢI PHÁP: ETHERCHANNEL
## 24.7 Biểu diễn trong sơ đồ mạng:
EtherChannel (trong sơ đồ Cấu trúc mạng) được biểu diễn như THẾ NÀY (vòng tròn quanh multi-connection)

![image](https://github.com/psaumur/CCNA/assets/106411237/4c2cfcf8-57f2-4907-8322-2f26cc7dc7e4)

## 24.8 Cách hoạt động:
- **EtherChannel nhóm nhiều channel** lại với nhau để hoạt động như **MỘT INTERFACE duy nhất**
- **STP sẽ coi NHÓM này** như **MỘT INTERFACE duy nhất**

![image](https://github.com/psaumur/CCNA/assets/106411237/a48bed14-11b4-42ba-965a-9724598d3b69)

**(Tất cả INTERFACE đều Xanh!)**

## 24.9 Load Balancing:
**LƯU LƯỢNG sử dụng EtherChannel sẽ được cân bằng tải** giữa các INTERFACE vật lý trong nhóm.

**Một thuật toán được sử dụng** để xác định **LƯU LƯỢNG NÀO sẽ sử dụng INTERFACE vật lý NÀO**

## 24.10 Tên khác cho EtherChannel:
- **Port Channel**
- **LAG (Link Aggregation Group)**

- --

## 24.11 ETHERCHANNEL LOAD-BALANCE NHU THẾ NÀO?
![image](https://github.com/psaumur/CCNA/assets/106411237/bc257ff8-bf91-4744-a6cb-8f603ee9d294)

## 24.12 Nguyên tắc Load Balancing:
- **EtherChannel cân bằng tải dựa trên "flows"**
- **"Flow"** là một giao tiếp giữa **HAI NODE** trong Mạng
- **FRAME trong cùng "flow"** sẽ được **CHUYỂN TIẾP sử dụng cùng INTERFACE vật lý**
- Nếu **FRAME trong cùng "flow"** được **CHUYỂN TIẾP sử dụng các INTERFACE vật lý khác nhau**, một số FRAME có thể **đến ĐÍCH không đúng thứ tự**, có thể gây ra vấn đề

## 24.13 Các INPUT có thể sử dụng:
Bạn có thể **THAY ĐỔI INPUT** được sử dụng trong tính toán **CHỌN INTERFACE** (cho "flows"):

- **SOURCE MAC Address**
- **DESTINATION MAC Address**
- **SOURCE và DESTINATION MAC Address**
- **SOURCE IP Address**
- **DESTINATION IP Address**
- **SOURCE và DESTINATION IP Address**

- --

## 24.14 KIỂM TRA VÀ CẤU HÌNH LOAD-BALANCING
## 24.15 Xem cấu hình Load-Balancing method:
![image](https://github.com/psaumur/CCNA/assets/106411237/571623bf-b96b-4382-ada5-f14f93ec1a6a)

```
Switch# show etherchannel load-balance
```

## 24.16 Thay đổi Load-Balancing method:
![image](https://github.com/psaumur/CCNA/assets/106411237/5919f2fd-80bb-4b10-bfa0-ce403f52c710)

```
Switch(config)# port-channel load-balance src-dst-ip
```

![image](https://github.com/psaumur/CCNA/assets/106411237/bc30e17e-716a-41cd-a57a-69a661b5d58e)

- --

## 24.17 CÁCH CẤU HÌNH LAYER 2 / LAYER 3 ETHERCHANNEL
Có **BA phương pháp** cấu hình EtherChannel trên Cisco SWITCH:

## 24.18 PAgP (Port Aggregation Protocol)
- **Giao thức độc quyền của Cisco**
- **Thương lượng động** việc tạo/duy trì EtherChannel (như DTP làm cho trunk)

## 24.19 LACP (Link Aggregation Control Protocol) 💡
- **Giao thức tiêu chuẩn công nghiệp** (IEEE 802.3ad)
- **Thương lượng động** việc tạo/duy trì EtherChannel (như DTP làm cho trunk)

## 24.20 Static EtherChannel
- **Không sử dụng giao thức** để xác định có nên tạo EtherChannel hay không
- **Interface được cấu hình tĩnh** để tạo EtherChannel

## 24.21 Giới hạn:
- **Tối đa 8 INTERFACE** có thể được tạo thành một EtherChannel duy nhất
- **LACP cho phép tối đa 16** nhưng chỉ **8 sẽ ACTIVE**, **8 khác sẽ ở chế độ STANDBY**, chờ một Interface active bị lỗi

- --

## 24.22 CẤU HÌNH PAgP
![image](https://github.com/psaumur/CCNA/assets/106411237/d0c734e2-79ad-43ad-a50b-c17ced608021)

💡 **Lưu ý rằng "auto" và "desirable" là các chế độ DUY NHẤT có sẵn cho PAgP**

## 24.23 Bảng thương lượng PAgP:
![image](https://github.com/psaumur/CCNA/assets/106411237/9eabb76a-1846-48d3-abb1-bd6898a432e7)

| PAgP Mode 1 | PAgP Mode 2 | Kết quả |
|-------------|-------------|---------|
| Auto | Auto | ❌ Không tạo EtherChannel |
| Auto | Desirable | ✅ Tạo EtherChannel |
| Desirable | Desirable | ✅ Tạo EtherChannel |

## 24.24 Cấu hình PAgP:
```
Switch(config-if-range)# channel-group 1 mode desirable
Creating a Port-channel interface Port-channel1
```

![image](https://github.com/psaumur/CCNA/assets/106411237/bc0c1190-9e39-4ea2-923c-b29e03e9d40a)

**Số "channel-group" phải KHỚP cho các INTERFACE thành viên trên cùng Switch. Nó KHÔNG phải KHỚP số "channel-group" trên Switch KHÁC!**

💡 **(channel-group 1 trên AWS1 có thể tạo EtherChannel với channel-group 2 trên DSW1)**

- --

## 24.25 CẤU HÌNH LACP
![image](https://github.com/psaumur/CCNA/assets/106411237/ba4adcf6-dec5-456f-b8d7-ab4e6b722cbf)

💡 **Lưu ý rằng "active" và "passive" là các chế độ DUY NHẤT có sẵn cho LACP**

## 24.26 Bảng thương lượng LACP:
![image](https://github.com/psaumur/CCNA/assets/106411237/0a314613-d398-49f1-a4d3-1b50fb96ab7d)

| LACP Mode 1 | LACP Mode 2 | Kết quả |
|-------------|-------------|---------|
| Passive | Passive | ❌ Không tạo EtherChannel |
| Passive | Active | ✅ Tạo EtherChannel |
| Active | Active | ✅ Tạo EtherChannel |

## 24.27 Cấu hình LACP:
```
Switch(config-if-range)# channel-group 1 mode active
```

**Số "channel-group" phải KHỚP cho các INTERFACE thành viên trên cùng Switch. Nó KHÔNG phải KHỚP số "channel-group" trên Switch KHÁC!**

- --

## 24.28 CẤU HÌNH STATIC ETHERCHANNEL
![image](https://github.com/psaumur/CCNA/assets/106411237/92db26e7-21ae-40c6-89ee-abe0197ed8ad)

💡 **Lưu ý rằng "on" là chế độ DUY NHẤT có sẵn cho STATIC EtherChannel**

## 24.29 Quy tắc Static EtherChannel:
- **ON mode chỉ hoạt động với ON Mode**
- **ON + desirable = KHÔNG HOẠT ĐỘNG**
- **ON + active = KHÔNG HOẠT ĐỘNG**

## 24.30 Cấu hình Static:
```
Switch(config-if-range)# channel-group 1 mode on
```

- --

## 24.31 CẤU HÌNH GIAO THỨC THƯƠNG LƯỢNG
![image](https://github.com/psaumur/CCNA/assets/106411237/83ef9bc8-4bd4-4dd3-b28e-83439ba96860)

## 24.32 HAI TÙY CHỌN:
- **LACP Protocol**
- **PAgP Protocol**

## 24.33 Lỗi không khớp giao thức:
Hình trên hiển thị lỗi không khớp giao thức vì **LACP không hỗ trợ "desirable"** - chỉ PAgP mới hỗ trợ

**("channel-group 1 mode active" hoạt động vì LACP hỗ trợ "active")**

- --

## 24.34 CẤU HÌNH SAU KHI TẠO ETHERCHANNEL
## 24.35 Cấu hình Port Interface:
![image](https://github.com/psaumur/CCNA/assets/106411237/c485cdf1-f0ed-44b8-8c91-c0553bf6d82d)

```
Switch(config)# interface port-channel 1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 1,10,20,30
```

## 24.36 Kiểm tra cấu hình:
![image](https://github.com/psaumur/CCNA/assets/106411237/6adda3dd-6408-445f-bb3f-61847b3920b6)

💡 **LưU Ý: Các INTERFACE VẬT LÝ (g0/0-g0/3) được tự động cấu hình bởi cấu hình Port-channel1!**

- --

## 24.37 LƯU Ý QUAN TRỌNG VỀ CẤU HÌNH ETHERCHANNEL
## 24.38 Các Interface thành viên phải có CẤU HÌNH KHỚP:
- **Cùng DUPLEX** (Full / Half)
- **Cùng SPEED**
- **Cùng SWITCHPORT mode** (Access / Trunk)
- **Cùng allowed VLAN / Native VLAN** (cho Trunk interface)

**Nếu cấu hình của Interface KHÔNG KHỚP với các interface khác, nó sẽ bị LOẠI KHỎI EtherChannel**

- --

## 24.39 KIỂM TRA TRẠNG THÁI ETHERCHANNEL
## 24.40 Lệnh kiểm tra chính:
```
Switch# show etherchannel summary
```

![image](https://github.com/psaumur/CCNA/assets/106411237/9e0edb15-2806-4d51-afc9-ad67ed465a97)

**Thông tin ở dưới cùng: ("SU" có nghĩa S - Layer2 + U - đang sử dụng)**

- **Protocol** = Giao thức mà EtherChannel đang sử dụng (trong trường hợp này, LACP)
- **"Ports"** = danh sách interface trong EtherChannel (P = bundled trong Port-channel)

## 24.41 Các FLAG khác:
![image](https://github.com/psaumur/CCNA/assets/106411237/23d92ae1-9cc6-4f3a-9ddf-2ead59705c1c)

**"D" = Down**

![image](https://github.com/psaumur/CCNA/assets/106411237/b1b3ce70-d9a6-4bd2-be4d-976077438c85)

Thay đổi một trong các Interface thành viên bằng "switchport mode access" đã làm cho nó khác với các thành viên khác nên bây giờ nó xuất hiện là **"s" = suspended**

## 24.42 Lệnh hữu ích khác:
```
Switch# show etherchannel port-channel
```

![image](https://github.com/psaumur/CCNA/assets/106411237/61731b0c-1cc5-4a7e-b92c-d0afbea0ac2d)

```
Switch# show spanning-tree
```

![image](https://github.com/psaumur/CCNA/assets/106411237/df0b9cc8-0448-4bbd-aefa-62fadf2b6089)

💡 **"show spanning-tree" sẽ hiển thị Port Interface EtherChannel duy nhất**

- --

## 24.43 LAYER 3 ETHERCHANNEL
![image](https://github.com/psaumur/CCNA/assets/106411237/c553ad64-1d8e-4a2a-a741-3102c89dc030)

## 24.44 Cách cấu hình Layer 3 EtherChannel (từ cấu hình sạch):
![image](https://github.com/psaumur/CCNA/assets/106411237/c4520b2f-1e3b-49b8-85b1-458cdb6fc865)

```
Switch(config-if-range)# no switchport
Switch(config-if-range)# channel-group 1 mode active
```

## 24.45 Kiểm tra cấu hình:
![image](https://github.com/psaumur/CCNA/assets/106411237/8638f32d-47c3-4c64-b68e-a9e2e0070ac9)

**LƯU Ý: Không có SWITCHPORT và không có IP Interface. Chúng ta cấu hình địa chỉ IP ở đâu?**

**Trực tiếp trên Port Interface!**

![image](https://github.com/psaumur/CCNA/assets/106411237/3ec55a24-1de5-44a7-926c-f85500042115)

```
Switch(config)# interface port-channel 1
Switch(config-if)# ip address 10.0.0.1 255.255.255.252
```

## 24.46 Kiểm tra Layer 3 EtherChannel:
![image](https://github.com/psaumur/CCNA/assets/106411237/f99ea2a6-82fb-494a-b80d-a171732d5786)

**("RU" - "R" = Layer 3, "U" = đang sử dụng)**

![image](https://github.com/psaumur/CCNA/assets/106411237/acfe62c5-6908-4782-9440-1f75f842c2c9)

- --

## 24.47 CÁC LỆNH ĐÃ HỌC TRONG CHƯƠNG NÀY
## 24.48 Cấu hình Load Balancing:
```
Switch(config)# port-channel load-balance <mode>
```
Cấu hình phương pháp cân bằng tải EtherChannel trên Switch

## 24.49 Hiển thị thông tin Load Balancing:
```
Switch# show etherchannel load-balance
```
Hiển thị thông tin về cài đặt cân bằng tải

## 24.50 Cấu hình Channel Group:
```
Switch(config-if)# channel-group <number> mode {desirable | auto | active | passive | on}
```
Cấu hình Interface là PHẦN của EtherChannel

## 24.51 Hiển thị tóm tắt EtherChannel:
```
Switch# show etherchannel summary
```
Hiển thị tóm tắt EtherChannel trên Switch

## 24.52 Hiển thị thông tin Port-channel:
```
Switch# show etherchannel port-channel
```
Hiển thị thông tin về các virtual Port-channel interface trên Switch

- --

## 24.53 TÓM TẮT ETHERCHANNEL
## 24.54 Lợi ích chính:
- **Tăng băng thông** - Kết hợp nhiều link
- **Redundancy** - Backup tự động khi link lỗi
- **Load balancing** - Phân phối lưu lượng
- **STP friendly** - Được coi là một link duy nhất

## 24.55 Các giao thức:
- **PAgP** - Cisco proprietary (auto/desirable)
- **LACP** - Industry standard (passive/active) - **Khuyến nghị**
- **Static** - Không thương lượng (on)

## 24.56 Yêu cầu cấu hình:
- **Cùng speed và duplex**
- **Cùng switchport mode**
- **Cùng VLAN configuration** (nếu trunk)
- **Tối đa 8 interface active**

![image](https://github.com/psaumur/CCNA/assets/106411237/6cae87f0-0226-40cc-92ba-b839c7a5ff53)