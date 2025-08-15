# 21. SPANNING TREE GIAO THỨC (STP) : PART 2

STP STATES

![image](https://github.com/psaumur/CCNA/assets/106411237/5c9a17ff-b0d6-455c-8677-5144dd5a0048)


- ROOT / DESIGNATED PORTS remain STABLE in a FORWARDING state
- NON-DESIGNATED PORTS remain STABLE in a BLOCKING state
- LISTENING and LEARNING are TRANSITIONAL states which are passed through when an Interface is activated, or when a BLOCKING Port must transition to a FORWARDING state due to a change in Network Cấu trúc mạng.

**1) BLOCKING / STABLE**

- NON-DESIGNATED PORTS are in a BLOCKING state
- Interfaces in a BLOCKING state are effectively disabled to prevent loops
- Interfaces in a BLOCKING state do NOT Send/Receive regular Network traffic
- Interfaces in a BLOCKING state do NOT forward STP BPDUs
- Interfaces in a BLOCKING state do NOT learn MAC ADDRESSES

**2) LISTENING / TRANSITIONAL**

- After the BLOCKING state, interfaces with the DESIGNATED or ROOT role enter the LISTENING state
- ONLY DESIGNATED or ROOT PORTS enter the LISTENING state (NON-DESIGNATED PORTS are ALWAYS BLOCKING)
- The LISTENING state is 15 seconds long by Default. This is determined by the FORWARD DELAY TIMER
- Interfaces in a LISTENING state do NOT Send / Receive regular Network traffic
- Interfaces in a LISTENING state ONLY Forward/Receive STP BPDUs
- Interfaces in a LISTENING state does NOT learn MAC ADDRESSES from regular traffic that arrives on the Interface

**3) LEARNING / TRANSITIONAL**

- After the LISTENING state, a DESIGNATED or ROOT Port will enter the LEARNING state
- The LEARNING state is 15 seconds long by Default. This is determined by the FORWARD DELAY TIMER (same one used for both LISTENING and LEARNING states)
- Interfaces in a LEARNING state do NOT Send / Receive regular Network traffic
- Interfaces in a LEARNING state ONLY Sends/Receives STP BPDUs
- Interfaces in a LEARNING state **learns** MAC ADDRESSES from regular traffic that arrives on the Interface

4) FORWARDING / STABLE

- ROOT and DESIGNATED PORTS are in a FORWARDING state
- A Port in the FORWARDING state operate as NORMAL
- A Port in the FORWARDING state Sends/Receives regular Network traffic
- A Port in the FORWARDING state Sends/Receives STP BPDUs
- A Port in the FORWARDING state **learns** MAC ADDRESSES

SUMMARY : 

![image](https://github.com/psaumur/CCNA/assets/106411237/f4cea5ca-b90a-423e-9160-f206b8b1621d)


---

STP TIMERS

![image](https://github.com/psaumur/CCNA/assets/106411237/a174469f-9e75-4645-aff8-d4bfe46fb207)


💡 SWITCHES do NOT forward the BPDUs out of their ROOT PORTS and NON-DESIGNATED PORTS - ONLY their DESIGNATED PORTS !!!


MAX AGE TIMER:

- If another BPDU is received BEFORE MAX AGE TIMER counts down to 0, the TIME will RESET to 20 Seconds and no changes will occur.
- If another BPDU is not received, the MAX AGE TIMER counts down to 0 and the Switch will re-evaluate it’s STP choices, including Bridge gốc, LOCAL ROOT, DESIGNATED, and NON-DESIGNATED PORTS.
- If a NON-DESIGNATED Port is selected to become a DESIGNATED or ROOT Port, it will transition from the BLOCKING state to the LISTENING state (15 Seconds), LEARNING state (15 Seconds), and then finally the FORWARDING state.
    - So… it can take 50 Seconds for a BLOCKING Interface to transition to FORWARDING! (MAX AGE TIMER  + (LISTENING + LEARNING 15 Second timers))
- These TIMERS and TRANSITIONAL STATES are to make sure that LOOPS are not accidentally created by an Interface moving to FORWARDING STATE too soon

 HOWEVER …

💡 A FORWARDING Interface can move DIRECTLY to a BLOCKING state (there is no worry about creating a loop)

💡 A BLOCKING Interface can NOT move DIRECTLY to a FORWARDING state. It MUST go through the LISTENING and LEARNING states first!


---

STP BPDU (Bridge Giao thức DATA UNIT)

Ethernet Header of a BPDU

![image](https://github.com/psaumur/CCNA/assets/106411237/0e68839f-c4ec-448b-8876-791212462009)


💡 PVST+ uses the Địa chỉ MAC : 

01 : 00 : 0c : cc : cc : cd

PVST = ONLY ISL Trunk Đóng gói

PVST+ = Supports 802.1Q

💡 Regular STP (not Cisco’s PVST+) uses the Địa chỉ MAC : 

01 : 80 : c2 : 00 : 00 : 00

💡 The STP TIMERS on the Bridge gốc determine ALL STP TIMERS for the entire Network!

---

STP OPTIONAL FEATURES (STP TOOLKIT)

PORTFAST:

- Can be Enabled on INTERFACES which are connected to END HOSTS

💡 PORTFAST allows a Port to move immediately to the FORWARDING state, bypassing LISTENING and LEARNING

- If used, it MUST be ENABLED only on PORTS connected to END HOSTS
- If ENABLED on a Port connected to another Switch, it could cause a LAYER 2 LOOP

![image](https://github.com/psaumur/CCNA/assets/106411237/43c91f09-0d9f-4b81-b5a2-f02003e25b88)


You can also Kích hoạt PORTFAST with the following Lệnh:

💡 SW1(config)# spanning-tree portfast Default

This ENABLES PORTFAST on ALL Access PORTS (not Trunk PORTS)

BPDU GUARD:

- If an Interface with BPDU GUARD ENABLED receives a BPDU from another Switch, the Interface will be SHUT DOWN to prevent loops from forming.

![image](https://github.com/psaumur/CCNA/assets/106411237/00c61767-72b4-4d51-b964-f76b6f4f6ae9)


You can also Kích hoạt BPDU GUARD with the following Lệnh:

💡 SW1(config)# spanning-tree portfast bpduguard Default


This ENABLES BPDU GUARD on all PORTFAST-enabled INTERFACES

ROOT GUARD / LOOP GUARD:

![image](https://github.com/psaumur/CCNA/assets/106411237/bb38aedc-df38-4d76-b6cb-30319e74ecc1)


You probably do NOT have to know these STP optional features (or others such as UplinkFast, Backbone Fast, etcetera) for the CCNA. 

BUT…

💡 Make sure you know PORTFAST and BPDU GUARD.

---

STP Configuration

Lệnh to CONFIGURE Spanning-Tree mode on a Switch

![image](https://github.com/psaumur/CCNA/assets/106411237/f29e2f41-3fac-463c-ab14-bb2d2f49816d)


Modern Cisco SWITCHES run **rapid-pvst**, by Default

---

CONFIGURE THE PRIMARY Bridge gốc

Lệnh to CONFIGURE Spanning-Tree PRIMARY Bridge gốc on a Switch

![image](https://github.com/psaumur/CCNA/assets/106411237/e90f16ad-c85c-4868-bbf4-9095c0abd581)


Confirm with “(do) show spanning-tree”

Can see in the above example, SW3 has become the “root”

- The “spanning-tree VLAN <VLAN-number> root primary” Lệnh sets the STP PRIORITY to 24576. If another Switch already has a priority number lower than 24576, it sets this Switch’s priority to 4096 LESS THAN the other Switch’s Priority (remember STP PART 1 lecture)

---

SECONDARY ROOT BRIGE (backup Bridge gốc)

Lệnh to CONFIGURE Spanning-Tree SECONDARY Bridge gốc on a Switch

![image](https://github.com/psaumur/CCNA/assets/106411237/7d28f782-4673-4bc8-9aae-999aeac90685)



- The “spanning-tree VLAN <VLAN-number> root secondary” Lệnh sets the STP PRIORITY to 28672 (exactly 4096 higher than 24576).

---

VLAN 1 Cấu trúc mạng running PVST+

![image](https://github.com/psaumur/CCNA/assets/106411237/880a4cc7-e472-4764-a68b-a62288066796)


SW1 WAS the PRIMARY Bridge gốc but : 

- We have configured SW3 to be the PRIMARY
- We have configured SW2 to be the SECONDARY

The Cấu trúc mạng for VLAN 2, however, won’t be the same. It will be the OLD Cấu trúc mạng.

![image](https://github.com/psaumur/CCNA/assets/106411237/2cedeb36-27f1-4984-96e7-28ab70957c51)


WHY?
Because we made changes ONLY to the Cấu trúc mạng found in VLAN 1 (see the commands we used)

---

CONFIGURE STP Port SETTINGS

![image](https://github.com/psaumur/CCNA/assets/106411237/58af0a8d-eeb4-4c34-8b54-6b8ff511695c)


“cost” = “ROOT COST”

“Port-priority” = “Port PRIORITY”
