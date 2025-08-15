# 22. GIAO THỨC SPANNING TREE (STP): PHẦN 2

## CÁC TRẠNG THÁI STP

![image](https://github.com/psaumur/CCNA/assets/106411237/5c9a17ff-b0d6-455c-8677-5144dd5a0048)

### Trạng thái ổn định:
- **ROOT / DESIGNATED PORT** duy trì **STABLE** trong trạng thái **FORWARDING**
- **NON-DESIGNATED PORT** duy trì **STABLE** trong trạng thái **BLOCKING**

### Trạng thái chuyển tiếp:
- **LISTENING và LEARNING** là các trạng thái **TRANSITIONAL** được đi qua khi Interface được kích hoạt, hoặc khi **BLOCKING Port** phải chuyển sang trạng thái **FORWARDING** do thay đổi trong Cấu trúc mạng.

---

## CHI TIẾT CÁC TRẠNG THÁI

### 1) BLOCKING / STABLE
- **NON-DESIGNATED PORT** ở trạng thái **BLOCKING**
- Interface trong trạng thái **BLOCKING** bị **vô hiệu hóa hiệu quả** để ngăn chặn vòng lặp
- Interface trong trạng thái **BLOCKING** **KHÔNG** Gửi/Nhận lưu lượng Mạng thông thường
- Interface trong trạng thái **BLOCKING** **KHÔNG** chuyển tiếp STP BPDU
- Interface trong trạng thái **BLOCKING** **KHÔNG** học địa chỉ MAC

### 2) LISTENING / TRANSITIONAL
- Sau trạng thái **BLOCKING**, interface với vai trò **DESIGNATED hoặc ROOT** vào trạng thái **LISTENING**
- **CHỈ DESIGNATED hoặc ROOT PORT** vào trạng thái **LISTENING** (NON-DESIGNATED PORT **LUÔN BLOCKING**)
- Trạng thái **LISTENING** dài **15 giây** theo Mặc định. Được xác định bởi **FORWARD DELAY TIMER**
- Interface trong trạng thái **LISTENING** **KHÔNG** Gửi/Nhận lưu lượng Mạng thông thường
- Interface trong trạng thái **LISTENING** **CHỈ** Chuyển tiếp/Nhận STP BPDU
- Interface trong trạng thái **LISTENING** **KHÔNG** học địa chỉ MAC từ lưu lượng thông thường đến trên Interface

### 3) LEARNING / TRANSITIONAL
- Sau trạng thái **LISTENING**, **DESIGNATED hoặc ROOT Port** sẽ vào trạng thái **LEARNING**
- Trạng thái **LEARNING** dài **15 giây** theo Mặc định. Được xác định bởi **FORWARD DELAY TIMER** (cùng timer được sử dụng cho cả trạng thái LISTENING và LEARNING)
- Interface trong trạng thái **LEARNING** **KHÔNG** Gửi/Nhận lưu lượng Mạng thông thường
- Interface trong trạng thái **LEARNING** **CHỈ** Gửi/Nhận STP BPDU
- Interface trong trạng thái **LEARNING** **học** địa chỉ MAC từ lưu lượng thông thường đến trên Interface

### 4) FORWARDING / STABLE
- **ROOT và DESIGNATED PORT** ở trạng thái **FORWARDING**
- Port trong trạng thái **FORWARDING** hoạt động **BÌNH THƯỜNG**
- Port trong trạng thái **FORWARDING** Gửi/Nhận lưu lượng Mạng thông thường
- Port trong trạng thái **FORWARDING** Gửi/Nhận STP BPDU
- Port trong trạng thái **FORWARDING** **học** địa chỉ MAC

---

## TÓM TẮT TRẠNG THÁI

![image](https://github.com/psaumur/CCNA/assets/106411237/f4cea5ca-b90a-423e-9160-f206b8b1621d)

| Trạng thái | Gửi/Nhận Data | Gửi/Nhận BPDU | Học MAC | Thời gian |
|------------|---------------|---------------|---------|-----------|
| **Blocking** | ❌ | ❌ | ❌ | Stable |
| **Listening** | ❌ | ✅ | ❌ | 15 giây |
| **Learning** | ❌ | ✅ | ✅ | 15 giây |
| **Forwarding** | ✅ | ✅ | ✅ | Stable |

---

## STP TIMER

![image](https://github.com/psaumur/CCNA/assets/106411237/a174469f-9e75-4645-aff8-d4bfe46fb207)

💡 **SWITCH KHÔNG chuyển tiếp BPDU ra khỏi ROOT PORT và NON-DESIGNATED PORT - CHỈ DESIGNATED PORT của chúng!!!**

### MAX AGE TIMER (20 giây):
- Nếu BPDU khác được nhận **TRƯỚC KHI** MAX AGE TIMER đếm xuống 0, **TIMER sẽ RESET** về 20 Giây và không có thay đổi nào xảy ra
- Nếu BPDU khác **không được nhận**, MAX AGE TIMER đếm xuống 0 và Switch sẽ **đánh giá lại** các lựa chọn STP, bao gồm **Root Bridge, LOCAL ROOT, DESIGNATED, và NON-DESIGNATED PORT**
- Nếu **NON-DESIGNATED Port** được chọn trở thành **DESIGNATED hoặc ROOT Port**, nó sẽ chuyển từ trạng thái **BLOCKING** sang trạng thái **LISTENING** (15 Giây), trạng thái **LEARNING** (15 Giây), và cuối cùng là trạng thái **FORWARDING**

### Tổng thời gian chuyển đổi:
**Có thể mất 50 Giây để BLOCKING Interface chuyển sang FORWARDING!**
**(MAX AGE TIMER + (LISTENING + LEARNING 15 Second timer))**

### Mục đích của Timer:
Những **TIMER và TRẠNG THÁI CHUYỂN TIẾP** này để đảm bảo rằng **VÒNG LẶP không được tạo ra một cách tình cờ** bởi Interface chuyển sang **FORWARDING STATE** quá sớm

### Lưu ý quan trọng:
💡 **FORWARDING Interface có thể chuyển TRỰC TIẾP sang trạng thái BLOCKING** (không lo lắng về việc tạo vòng lặp)

💡 **BLOCKING Interface KHÔNG THỂ chuyển TRỰC TIẾP sang trạng thái FORWARDING. Nó phải đi qua trạng thái LISTENING và LEARNING trước!**

---

## STP BPDU (BRIDGE PROTOCOL DATA UNIT)

### Ethernet Header của BPDU:

![image](https://github.com/psaumur/CCNA/assets/106411237/0e68839f-c4ec-448b-8876-791212462009)

### Địa chỉ MAC đặc biệt:

💡 **PVST+** sử dụng địa chỉ MAC: **01:00:0c:cc:cc:cd**
- **PVST** = CHỈ ISL Trunk Encapsulation
- **PVST+** = Hỗ trợ 802.1Q

💡 **Regular STP** (không phải PVST+ của Cisco) sử dụng địa chỉ MAC: **01:80:c2:00:00:00**

💡 **STP TIMER trên Root Bridge xác định TẤT CẢ STP TIMER cho toàn bộ Mạng!**

---

## TÍNH NĂNG TÙY CHỌN STP (STP TOOLKIT)

### PORTFAST:
- Có thể được **Kích hoạt trên INTERFACE** được kết nối với **END HOST**

💡 **PORTFAST cho phép Port chuyển ngay lập tức sang trạng thái FORWARDING, bỏ qua LISTENING và LEARNING**

#### Lưu ý quan trọng:
- Nếu sử dụng, nó **phải được BẬT chỉ trên PORT** kết nối với **END HOST**
- Nếu **BẬT trên Port** kết nối với Switch khác, nó **có thể gây ra VÒNG LẶP TẦNG 2**

![image](https://github.com/psaumur/CCNA/assets/106411237/43c91f09-0d9f-4b81-b5a2-f02003e25b88)

#### Cấu hình PORTFAST:
```
Switch(config-if)# spanning-tree portfast
```

**Hoặc bật cho tất cả Access Port:**
```
Switch(config)# spanning-tree portfast default
```
💡 Lệnh này **BẬT PORTFAST trên TẤT CẢ Access PORT** (không phải Trunk PORT)

---

### BPDU GUARD:
- Nếu Interface với **BPDU GUARD ENABLED** nhận BPDU từ Switch khác, **Interface sẽ bị SHUT DOWN** để ngăn chặn vòng lặp hình thành

![image](https://github.com/psaumur/CCNA/assets/106411237/00c61767-72b4-4d51-b964-f76b6f4f6ae9)

#### Cấu hình BPDU GUARD:
```
Switch(config-if)# spanning-tree bpduguard enable
```

**Hoặc bật cho tất cả PORTFAST interface:**
```
Switch(config)# spanning-tree portfast bpduguard default
```
💡 Lệnh này **BẬT BPDU GUARD trên tất cả INTERFACE có PORTFAST**

---

### ROOT GUARD / LOOP GUARD:

![image](https://github.com/psaumur/CCNA/assets/106411237/bb38aedc-df38-4d76-b6cb-30319e74ecc1)

**Bạn có thể KHÔNG cần biết những tính năng STP tùy chọn này (hoặc các tính năng khác như UplinkFast, Backbone Fast, v.v.) cho CCNA.**

💡 **Nhưng... Hãy chắc chắn bạn biết PORTFAST và BPDU GUARD.**

---

## CẤU HÌNH STP

### Lệnh cấu hình Spanning-Tree mode trên Switch:

![image](https://github.com/psaumur/CCNA/assets/106411237/f29e2f41-3fac-463c-ab14-bb2d2f49816d)

```
Switch(config)# spanning-tree mode ?
  mst        Multiple spanning tree mode
  pvst       Per-Vlan spanning tree mode
  rapid-pvst Rapid per-Vlan spanning tree mode
```

**Cisco SWITCH hiện đại chạy rapid-PVST theo mặc định**

---

## CẤU HÌNH PRIMARY ROOT BRIDGE

### Lệnh cấu hình Spanning-Tree PRIMARY Root Bridge trên Switch:

![image](https://github.com/psaumur/CCNA/assets/106411237/e90f16ad-c85c-4868-bbf4-9095c0abd581)

```
Switch(config)# spanning-tree vlan 1 root primary
```

**Xác nhận bằng:** `(do) show spanning-tree`

Có thể thấy trong ví dụ trên, SW3 đã trở thành "root"

#### Cách hoạt động:
- Lệnh **"spanning-tree vlan <vlan-number> root primary"** đặt **STP PRIORITY thành 24576**
- Nếu Switch khác đã có priority number **thấp hơn 24576**, nó đặt priority của Switch này **thấp hơn 4096** so với Switch kia

---

## SECONDARY ROOT BRIDGE (Root Bridge dự phòng)

### Lệnh cấu hình Spanning-Tree SECONDARY Root Bridge trên Switch:

![image](https://github.com/psaumur/CCNA/assets/106411237/7d28f782-4673-4bc8-9aae-999aeac90685)

```
Switch(config)# spanning-tree vlan 1 root secondary
```

- Lệnh **"spanning-tree vlan <vlan-number> root secondary"** đặt **STP PRIORITY thành 28672** (chính xác cao hơn 4096 so với 24576)

---

## PVST+ VÀ NHIỀU VLAN

### VLAN 1 Topology chạy PVST+:

![image](https://github.com/psaumur/CCNA/assets/106411237/880a4cc7-e472-4764-a68b-a62288066796)

**SW1 ĐÃ LÀ PRIMARY Root Bridge nhưng:**
- Chúng ta đã cấu hình **SW3 làm PRIMARY**
- Chúng ta đã cấu hình **SW2 làm SECONDARY**

### VLAN 2 Topology:

![image](https://github.com/psaumur/CCNA/assets/106411237/2cedeb36-27f1-4984-96e7-28ab70957c51)

**Topology cho VLAN 2 sẽ KHÔNG giống nhau. Nó sẽ là topology CŨ.**

**TẠI SAO?** Vì chúng ta chỉ thay đổi topology được tìm thấy trong **VLAN 1** (xem các lệnh chúng ta đã sử dụng)

---

## CẤU HÌNH STP PORT SETTINGS

![image](https://github.com/psaumur/CCNA/assets/106411237/58af0a8d-eeb4-4c34-8b54-6b8ff511695c)

### Các lệnh cấu hình:
```
Switch(config-if)# spanning-tree cost <cost>
Switch(config-if)# spanning-tree port-priority <priority>
```

**Trong đó:**
- **"cost"** = **"ROOT COST"**
- **"port-priority"** = **"PORT PRIORITY"**

---

## TÓM TẮT LỆNH STP QUAN TRỌNG

### Cấu hình cơ bản:
```
spanning-tree mode rapid-pvst                    // Đặt chế độ STP
spanning-tree vlan <vlan> root primary          // Đặt primary root
spanning-tree vlan <vlan> root secondary        // Đặt secondary root
```

### Cấu hình interface:
```
spanning-tree portfast                           // Bật portfast
spanning-tree bpduguard enable                  // Bật BPDU guard
spanning-tree cost <cost>                       // Đặt cost
spanning-tree port-priority <priority>          // Đặt port priority
```

### Cấu hình global:
```
spanning-tree portfast default                  // Portfast cho tất cả access port
spanning-tree portfast bpduguard default       // BPDU guard cho portfast port
```

### Lệnh kiểm tra:
```
show spanning-tree                              // Hiển thị STP info
show spanning-tree vlan <vlan>                 // STP cho VLAN cụ thể
show spanning-tree interface <interface>       // STP cho interface cụ thể
```
