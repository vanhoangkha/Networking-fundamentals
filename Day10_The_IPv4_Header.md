# 10. THE IPv4 Header

Internet Giao thức version 4 Header or IPv4 Header

Header is used at LAYER 3 to help send data between devices on separate networks, even on other sides of the world over the Internet.

This is known as Định tuyến.

THE IPv4 Header is used to ENCAPSULATE a TCP or UDP Đoạn.

To Review:

![image](https://github.com/psaumur/CCNA/assets/106411237/64906e3c-0bae-4c2c-96ca-4e6850f3844a)


---

FIELDS OF THE IPv4 Header

![image](https://github.com/psaumur/CCNA/assets/106411237/f2667488-2769-4e62-bee7-eddbf9e00058)


| FIELD | # OF BITS |
| --- | --- |
| VERSION | 4 |
| IHL | 4 |
| DSCP | 6 |
| ECN | 2 |
| TOTAL LENGTH | 16 |
| IDENTIFICATION | 16 |
| FLAGS | 3 |
| FRAGMENT OFFSET | 13 |
| TIME TO LIVE | 8 |
| Giao thức | 8 |
| Header CHECKSUM | 16 |
| SOURCE ADDRESS | 32 |
| DESTINATION ADDRESS | 32 |
| OPTIONS | 320 Max |

---

VERSION:

- LENGTH is 4 bits.
- IDs version of IP used (IPv4 or IPv6)
    - IPv4 = 0100 in Binary (Decimal 4)
    - IPv6 = 0110 in Binary (Decimal 6)

---

Internet Header LENGTH (IHL):

- LENGTH is 4 bits.
- Final field of IPv4 Header (Options) is variable in length so this field is necessary to indicate the total length of the Header.
- IDs the length of the Header in 4-BYTE INCREMENTS.
- The MINIMUM value is 5 (5 * 4-bytes = 20 bytes) - Empty OPTIONS Field
- The MAXIMUM value is 15 (15 * 4-bytes = 60 bytes)

MINIMUM IPv4 Header LENGTH = 20 Bytes!
MAXIMUM IPv4 Header LENGTH = 60 Bytes!

---

DSCP (Differentiated Services Code Point):

- LENGTH is 6 bits.
- Used for QoS (Chất lượng dịch vụ)
- Used to prioritize delay-sensitive data (streaming voice, video, etc.)

---

ECN (Explicit Congestion Notification):

- LENGTH is 2 bits.
- Provides end-to-end (between two endpoints) notification of Mạng congestion WITHOUT dropping packets.
- Optional feature that requires both endpoints, as well as the underlying Mạng Hạ tầng to support it.

---

TOTAL LENGTH:

- LENGTH is 16 bits.
- Indicates the TOTAL length of the Gói tin (L3 Header + L4 Đoạn)
- Measured in bytes (not 4-byte increments like IHL)
- Minimum value of 20 Bytes (IPv4 Header with NO encapsulated data)
- Maximum value of 65,535 (MAXIMUM 16-bit value) = 2^16

---

IDENTIFICATION:

- LENGTH is 16 bits.
- If a Gói tin is fragmented due to being too large, this field is used to identify which Gói tin the fragment belongs to.
- All fragments of the same Gói tin will have their own IPv4 Header with the same value in this field.
- Packets are fragmented, if larger than the MTU (Maximum Transmission Unit)
- The MTU is usually 1500 bytes (Max size of an Ethernet Khung)
- Fragments are reassembled by the receiving host.

---

FLAGS:

- LENGTH is 3 bits
- Used to control/identify fragments.
- Bit 0: Reserved, always set to 0.
- Bit 1: Don't Fragment (DF bit), used to indicate a Gói tin that should not be fragmented.
- Bit 2: More Fragments (MF bit), set to 1 if there are more fragments in the Gói tin, set to 0 for the last fragment or NO fragments.

---

FRAGMENT OFFSET:

- LENGTH is 13 bits
- Used to indicated the position of the fragment within the original, unfragmented IP Gói tin.
- Allows fragmented packets to be reassembled even if the fragments arrive out of order.

---

TIME TO LIVE (TTL):

- LENGTH is 8 bits
- A Router will drop a Gói tin with a TTL of 0
- Used to prevent infinite loops
- Originally designed to indicated a packets maximum lifetime in seconds.
- In practice, indicates a 'hop count': each time the Gói tin arrives at a Router, the Router decreases the TTL by 1.
- Recommended Mặc định TTL is 64.

---

Giao thức:

- LENGTH is 8 bits
- Indicates the Giao thức of the encapsulated Layer 4 PDU
- Value of 1 : ICMP
- Value of 6 : TCP
- Value of 17 : UDP
- Value of 89 : OSPF (Dynamic Định tuyến Giao thức)
- List of Giao thức numbers on Wikipedia : List of IP Giao thức Numbers

Header CHECKSUM:

- LENGTH is 16 bits
- A calculated checksum used to check for errors in the IPv4 Header.
- When a Router receives a Gói tin, it calculates the checksum of the Header and compares it to the one in this field of a Header.
- If they do not match, the Router drops the Gói tin.
- Used to check for ERRORS only in the IPv4 Header.
- IP relies on the encapsulated Giao thức to detect errors in the encapsulated data.
- Both TCP and UDP have their own checksum fields to detect errors in the encapsulated data.

---

SOURCE and DESTINATION:

- LENGTH is 32 bits each
- SOURCE IP = IPv4 ADDRESS of the Sender of the Gói tin.
- DESTINATION IP = IPv4 ADDRESS of the intended Receiver of the Gói tin.

---

OPTIONS:

- LENGTH is 0-320 bits
- Optional / Rarely Used
- If the IHL field is greater than 5, it means that Options are present.
