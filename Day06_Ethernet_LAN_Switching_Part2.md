# 6. ETHERNET LAN SWITCHING : PART 2

An Ethernet Khung looks like:

Ethernet Header --- DATA (Gói tin) --- Ethernet Trailer

![image](https://github.com/psaumur/CCNA/assets/106411237/27c1877f-57d7-44ea-8c64-b0ec2b308ad0)


The Ethernet Header contains 5 Fields:

Preamble -- SFD -- Destination -- Source -- Type/Length
7 bytes  -- 1 byte -- 6 bytes -- 6 bytes --   2 bytes

Ethernet Trailer contains 1 Field:

FCS (Khung Check Sequence) = 4 bytes

- The PREAMBLE + SFD is not usually considered part of the Ethernet Header.

THEREFORE the size of the Ethernet Header + Trailer is 18 bytes

(6 + 6 + 2 + 4 bytes for the Khung CHECK SEQUENCE)

---

The MINIMUM size for an Ethernet Khung (Header + Payload [Gói tin] + Trailer) is 64 BYTES.

64 BYTES - 18 BYTES (Header + Trailer size) = 46 BYTES

THEREFORE the MINIMUM DATA PAYLOAD (Gói tin) size is 46 BYTES!

IF the PAYLOAD is LESS than 46 BYTES then PADDING BYTES are added (padding bytes are a series of 0's) until it equals to 46 BYTES.

---

When a PC sends a Gói tin to a device with an unknown Địa chỉ IP, it uses an ARP Request.

![image](https://github.com/psaumur/CCNA/assets/106411237/e2d0e5d2-7c98-4671-b356-903132fd7525)


- ARP stands for 'Address Resolution Giao thức'.
- It is used to discover the Layer 2 address (Địa chỉ MAC) of a known Layer 3 address (Địa chỉ IP)
- Consists of two messages:
    - ARP REQUEST (Source message)
    - ARP REPLY (Destination message)
- ARP REQUEST is Broadcast = sent to all hosts on Network, except the one it received the request from.

An ARP REQUEST Khung has:

- Source Địa chỉ IP
- Destination Địa chỉ IP
- Source Địa chỉ MAC
- Broadcast Địa chỉ MAC - FFFF.FFFF.FFFF

An ARP REPLY Khung has:

- Source Địa chỉ IP
- Destination Địa chỉ IP
- Source Địa chỉ MAC
- Destination Địa chỉ MAC

ARP REPLY is a known Unicast Khung = Sent only to the host that sent the ARP REQUEST.

![image](https://github.com/psaumur/CCNA/assets/106411237/914cdf2a-c631-47e5-80f9-46e32ebed311)


---

PING

- A Network utility that is used to test reachability
- Measures round-trip time
- Uses two messages:
    - ICMP Echo REQUEST
    - ICMP Echo REPLY
- Is Unicast
- Lệnh to use ping:
    - ping <ip-address>

By Default, a CISCO IOS sends 5 ICMP requests/replies
(Default size is 100-bytes)

- A period (.) is a failed ping
- An exclamation mark (!) is a successful ping

---

USEFUL CISCO IOS COMMANDS (from Privileged EXEC mode)

PC1# show arp // shows hosts ARP table

![image](https://github.com/psaumur/CCNA/assets/106411237/da199d21-4f41-485e-8917-ca8e3d789617)


---

SW1#show Địa chỉ MAC-table // show the switches MAC table

![image](https://github.com/psaumur/CCNA/assets/106411237/c1cd95dd-7742-4703-9487-946652c95485)


Will show:

VLAN --- Địa chỉ MAC --- Type --- Ports(interfaces)

(VLAN = Virtual Local Area Network)

---

![image](https://github.com/psaumur/CCNA/assets/106411237/657b054b-a90c-4e5f-8544-2a51082cb631)


SW1# clear Địa chỉ MAC-table dynamic <optional Địa chỉ MAC>

// clears the entire switches MAC table.
// IF the optional Địa chỉ MAC is used, it will clear the SPECFIC Địa chỉ MAC.

SW1 #clear Địa chỉ MAC-table dynamic Interface <optional Interface>

// clears the MAC table entry of the Switch by it's **Interface n**ame.
