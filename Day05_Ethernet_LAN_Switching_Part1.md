# 5. Ethernet LAN SWITCHING : PART 1

![image](https://github.com/psaumur/CCNA/assets/106411237/a40e81d9-c008-4fb4-8580-2eaf63003e63)

![image](https://github.com/psaumur/CCNA/assets/106411237/2db46525-98b8-4211-aeb3-efc34bd84222)


LAN's

- A LAN is a Mạng contained in a relatively small area.
- Routers are used to connect separate LAN's

![image](https://github.com/psaumur/CCNA/assets/106411237/2a4de9d4-3408-49b9-9492-42b7eb56fe27)


An Ethernet Khung looks like:

![image](https://github.com/psaumur/CCNA/assets/106411237/ad579917-f9a0-4cd8-be25-351ecbfc87af)


Ethernet Trailer --- Gói tin --- Ethernet Header

The Ethernet Header contains 5 Fields:

Preamble -- SFD -- Destination -- Source -- Type
7 bytes  -- 1 byte -- 6 bytes -- 6 bytes -- 2 bytes

---

PREAMBLE:

- Length: 7 bytes (56 bits)
- Alternating 1's and 0's
- 10101010 * 7x
- Allows devices to synchronize their receiver clocks

SFD : ‘Start Khung Delimiter’

- Length: 1 byte(8 bits)
- 10101011
- Marks end of the PREAMBLE and beginning of REST of Khung.

---

DESTINATION AND SOURCE

- Layer 2 Address
- Indicates the devices sending / receiving the Khung
- MAC = ’Media Access Control’
- = 6 byte (48-bit) address of the physical device

---

TYPE / LENGTH

- 2 bytes (16-bit) field
- A value of 1**500 or less** in this field indicates the LENGTH of the encapsulated Gói tin (in bytes)
- A value of **1536 or greater** in this field indicates the TYPE of the encapsulated Gói tin and length is determined via other methods.
- IPv4 = 0x0800 (hexadecimal) = 2048 in decimal
- IPv6 = 0x86DD (hexadecimal) = 34525 in decimal
- Layer 3 Giao thức used in the encapsulated Gói tin, which is almost always Internet Giao thức (IP) version 4 or version 6.

---

The Ethernet Trailer contains:

FCS

- ‘Khung CHECK SEQUENCE’
- 4 bytes (32 bits) in length
- Detects corrupted data by running a 'CRC' algorithm over the received data
- CRC = "Cyclic Redundancy Check"

---

Altogether the Ethernet Khung = 26 bytes (Header + Trailer)

![image](https://github.com/psaumur/CCNA/assets/106411237/c8c1a143-0675-4aa4-83bc-6031d10cc0b8)


---

Địa chỉ MAC (48 bits long)

- 6-bytes (48-bits) physical address assigned to the device when it is made.
- AKA 'Burned-In Address' (BIA)
- Is globally unique
- First 3 bytes are the OUI (Organizationally Unique Identifier) which is assigned to the company making the device
- The last 3 bytes are unique to the device itself
- Written as 12 hexadecimal characters

Example:

E8:BA:70 // 11:28:74
OUI    // Unique Device ID

HEXADECIMAL

![image](https://github.com/psaumur/CCNA/assets/106411237/65a5e84a-b8db-46f5-b288-518139e99453)


Giao diện NAMES

F0/1, F0/2, F0/3... F stands for "Fast Ethernet" or 100 Mbps interfaces.

---

Địa chỉ MAC TABLE

Each Switch stores a DYNAMICALLY LEARNED Địa chỉ MAC TABLE, using the SOURCE Địa chỉ MAC of frames it receives.

![image](https://github.com/psaumur/CCNA/assets/106411237/582421a9-6351-48b7-bfe1-c2153520920c)


When a Switch doesn't know the DESTINATION Địa chỉ MAC of a Khung (UNKNOWN Unicast Khung), it is forced to FLOOD the Khung - Forward the Khung out of ALL it's interfaces, except the one it received the Gói tin from.

When a KNOWN Unicast Khung is known (Địa chỉ MAC is recognized by the entry in the Địa chỉ MAC TABLE), the Khung is FORWARDED like normal.

![image](https://github.com/psaumur/CCNA/assets/106411237/ff731ab3-fad2-4e10-9fa7-ce583a6a0bb2)

- Note: Dynamic MAC Addresses are removed from the Địa chỉ MAC TABLE every 5 minutes of inactivity.
