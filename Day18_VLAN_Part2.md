# 17. VLANS : PART 2

Basic VLAN Cấu trúc mạng from PART 1

![image](https://github.com/psaumur/CCNA/assets/106411237/f6df37e0-d494-4e46-b6e8-6d2ba0cd0ff6)


What about THIS Network Cấu trúc mạng ?

![image](https://github.com/psaumur/CCNA/assets/106411237/e6aff877-3792-469f-8955-0f3e17c6f1ed)


Notice this one has TWO Switches (SW1 and SW2) and ENGINEERING (VLAN 10) has two separate locations on the Network.

---

Trunk PORTS

- In a small Network with few VLANS, it’s possible to use a separate Interface for EACH VLAN when connecting SWITCHES to SWITCHES, and SWITCHES to ROUTERS

- HOWEVER, when the number of VLANS increases, this is not viable. It will result in wasted interfaces, and often ROUTERS won’t have enough INTERFACES for each VLAN

- You can use Trunk PORTS to carry traffic from multiple VLANS over a single Interface

A Trunk Port carrying multiple VLAN connections over single Interface

![image](https://github.com/psaumur/CCNA/assets/106411237/5cb7c933-689a-499b-9f30-51fe63d8b059)


![image](https://github.com/psaumur/CCNA/assets/106411237/8ea9a799-cf0d-4b1d-9706-db002772fe6d)


How does a Gói tin know WHICH VLAN to send traffic to over the Trunk Port ?

VLAN TAGS !

SWITCHES will “tag” all frames that they send over a Trunk LINK. This allows the receiving Switch to know which VLAN the Khung belongs to.

Trunk Port = “Tagged” ports

Access Port = “Untagged” ports

---

VLAN TAGGING

- There are TWO main Trunk protocols:
    - ISL (Inter-Switch Link)
    - IEEE 802.1Q (also known as “dot1q”)

ISL is an old Cisco proprietary Giao thức created before industry standard IEEE 802.1Q

IEEE 802.1Q is an industry standard Giao thức created by the IEEE (Institute of Electrical and Electronics Engineers)

You will probably NEVER use ISL in the real world; even modern Cisco equipment doesn’t use it.

For the CCNA, you will only need to learn 802.1Q

---

Ethernet Header with 802.1Q

![image](https://github.com/psaumur/CCNA/assets/106411237/00e817cd-1cac-44c5-a5f6-5459d383236d)


- The 802.1Q TAG Is inserted between the SOURCE and TYPE/LENGTH fields in the Ethernet Khung
- The TAG is 4 bytes (32 bits) in length
- The TAG consists of TWO main fields:
    - Tag Giao thức Identifier (TPID)
    - Tag Control Information (TCI)
        - TCI consists of THREE sub-fields:

![image](https://github.com/psaumur/CCNA/assets/106411237/8e52856b-58b9-448e-a007-254973fe707e)


TPID (TAG Giao thức Identifier) :

- 16 bits (2 bytes) in length
- Always set to a value of 0x8100. This indicates that the Khung is 802.1Q TAG

TCI / PCP (Priority Code Point) :

- 3 bits in length
- Used for Class of Service (CoS), which prioritizes important traffic in congested networks

TCI / DEI (Drop Eligible Indicator) :

- 1 bit in length
- Used to indicated frames that can be dropped if the Network is congested

TCI / VID (VLAN ID) :

- 12 bits in length
- Identifies the VLAN the Khung belongs to
- 12 bits in length = 4096 total VLANS (2^12), range of 0 - 4095
- VLANs 0 and 4095 are reserved and can’t be used
- Therefore, the actual range of VLANs is 1 - 4094

NOTE : Cisco’s ISL also had a VLAN range of 1 - 4094

---

VLAN RANGES

![image](https://github.com/psaumur/CCNA/assets/106411237/1c55a830-bfdd-423a-9688-334a3dd2bfa3)


---

VLAN gốc

![image](https://github.com/psaumur/CCNA/assets/106411237/8b1e09a1-e9c5-410e-ad87-581b95eaca81)


![image](https://github.com/psaumur/CCNA/assets/106411237/f8145795-b3f7-4766-9507-4fba7c743a14)


![image](https://github.com/psaumur/CCNA/assets/106411237/a1811276-c043-4035-9957-800873068615)

---

Trunk Configuration

![image](https://github.com/psaumur/CCNA/assets/106411237/d73b8f0b-2154-4e7f-8057-7c5b3f5078cc)


![image](https://github.com/psaumur/CCNA/assets/106411237/29313a87-cf16-439c-8a9e-90b518326954)

Many modern switches do not support Cisco’s ISL at all. They only support 802.1Q (dot1q)

However, SWITCHES that do support both (like the one I am using in this example) have a Trunk Đóng gói of “AUTO” by Default

To MANUALLY configure the Interface as a Trunk Port, you must first set the Đóng gói to “802.1Q” or “ISL”. On SWITCHES that only support 802.1Q, this is not necessary

After you set the Đóng gói type, you can then configure the Interface as a Trunk

1) Select the Interface to configure

2) Use “#switchport Trunk Đóng gói dot1q” to set the Đóng gói mode to 802.1Q

3) Use “#switchport mode Trunk” to manually configure the Interface to Trunk

![image](https://github.com/psaumur/CCNA/assets/106411237/6b897fb0-14a3-4e6a-b4e8-e278a6aec08e)


Use the “#show interfaces Trunk” Lệnh to confirm INTERFACES on Trunk

![image](https://github.com/psaumur/CCNA/assets/106411237/d3e144c7-90e3-4ab0-8021-7eb4d1420282)


Commands to allow a VLAN on a given Trunk

![image](https://github.com/psaumur/CCNA/assets/106411237/6a60f6ce-55be-4df5-a715-b871e5e461f4)


![image](https://github.com/psaumur/CCNA/assets/106411237/b39b091d-1ea9-4f72-b592-1eeb8ef25f90)


Lệnh to change the VLAN gốc

![image](https://github.com/psaumur/CCNA/assets/106411237/5109becb-27dd-4c63-9c7b-74b6f55e9d5f)


![image](https://github.com/psaumur/CCNA/assets/106411237/36abc437-69cb-4c56-8a59-87479ce01a7f)


---

Setting up our TRUNKS for this Network

![image](https://github.com/psaumur/CCNA/assets/106411237/892b5322-807b-4d76-91cb-a039766794c5)


We will need to configure :

SW1 : g0/0 Interface (already configure above this section)

SW2: g0/0, and g0/1 Interface

SW2 g0/0

![image](https://github.com/psaumur/CCNA/assets/106411237/7b313959-b710-4bb6-a281-727ec9477c3e)


SW2 g0/1

![image](https://github.com/psaumur/CCNA/assets/106411237/c26f17c8-0ec9-4406-ab66-83adf28c8550)


What about the Router, R1 ? 

---

Router ON A STICK (ROAS)

![image](https://github.com/psaumur/CCNA/assets/106411237/66c4ace0-8341-4c9c-8ff5-7c171034df53)


![image](https://github.com/psaumur/CCNA/assets/106411237/b409165d-39e6-4fba-ade1-2451f7e2fa8c)


![image](https://github.com/psaumur/CCNA/assets/106411237/112a2089-5a9e-4b13-945c-6be7f188d6a8)


NOTE the Sub-Interface names (like the Network diagram) of 0.10, 0.20 and 0.30

You assign them IP addresses identically like you would a regular Interface (using the last usable Địa chỉ IP of a given VLAN Network con)

Sub-interfaces will appear with the “show ip Interface brief” Lệnh

![image](https://github.com/psaumur/CCNA/assets/106411237/9b7ecbd1-c5f4-4ed0-9988-8fd17e16c9ae)


They also appear in the “show ip Tuyến đường” Lệnh (Tuyến đường Table)

![image](https://github.com/psaumur/CCNA/assets/106411237/1e9bb3fa-5aca-4883-8aff-52a554dcfba6)


ROAS is used to Tuyến đường between multiple VLANs using a SINGLE Interface on a Router and Switch

The Switch Interface is configured as a regular Trunk

The Router Interface is configured using SUB-INTERFACES. You configure the VLAN tag and Địa chỉ IP on EACH SUB-Interface

The Router will behave as if frames arriving with a certain VLAN tag have arrived on the SUB-Interface configured with that VLAN tag

The Router will TAG frames sent out of EACH SUB-Interface with the VLAN TAG configured on the SUB-Interface
