# 20. SPANNING TREE GIAO THỨC (STP) : PART 1

REDUNDANCY IN NETWORKS

- Essential in Network design
- Modern networks are expected to run 24/7/265; even a short downtime can be disastrous for business.
- If one Network component fails, you must ensure that other components will take over with little or no downtime.
- As much as possible, you must implement REDUNDANCY at every possible point in the Network

AN EXAMPLE OF A POORLY DESIGNED Network

![image](https://github.com/psaumur/CCNA/assets/106411237/b3b76af5-11e6-495b-8c40-40eb5800704b)


NOTE the many single-point failures that could occur (single connections)

A BETTER Network DESIGN

![image](https://github.com/psaumur/CCNA/assets/106411237/01c20d92-2cf6-4d1f-a193-ded7753aeb38)


UNFORTUNATELY : 

- Most PCS only have a single Network Interface card (NIC), so they can only be plugged into a single Switch. However, important SERVERS typically have multiple NICs, so they can be plugged into multiple SWITCHES for redundancy!

So HOW can all this redundancy be a BAD thing?

Broadcast STORMS

![image](https://github.com/psaumur/CCNA/assets/106411237/a0bf91be-a463-45df-bfc5-df471d0544b5)


![image](https://github.com/psaumur/CCNA/assets/106411237/d13b6ab5-5298-4166-bdfa-3315f05a2961)


![image](https://github.com/psaumur/CCNA/assets/106411237/f719de69-df9e-4549-b3cb-914d7c5aabc4)


FLOODED WITH ARP REQUESTS (Red = Clockwise Loops // Purple = Counter-Clockwise Loops)

Network Congestion isn’t the only problem.

Each time a Khung arrives on a SWITCHPORT, the Switch uses the SOURCE Địa chỉ MAC field to “learn” the Địa chỉ MAC and update it’s Địa chỉ MAC TABLE.

When frames with the same SOURCE Địa chỉ MAC repeatedly arrive on different interfaces, the Switch is continuously updating the Interface in it’s Địa chỉ MAC TABLE.

This is called Địa chỉ MAC FLAPPING

So how we design a Network, with redundant paths, that doesn’t result in LAYER 2 LOOPS.

Spanning Tree Giao thức is one solution

---

STP (Spanning Tree Giao thức) : 802.1D

- “Classic Spanning Tree Giao thức” is IEEE **802.1D**
- SWITCHES from ALL vendors run STP by Default
- STP prevents LAYER 2 loops by placing redundant PORTS in a BLOCKING state, essentially disabling the Interface
- These INTERFACES act as backups that can enter a FORWARDING state if an active (=currently forwarding) Interface fails.
- INTERFACES in a BLOCKING state only send or receive STP messages (called BPDUs = Bridge Giao thức Data Units)

💡 Spanning Tree Giao thức still uses the term “Bridge”. However, when use the term “Bridge”, we really mean “Switch”. BRIDGES are not used in modern networks.

![image](https://github.com/psaumur/CCNA/assets/106411237/f253770d-22fa-4e3f-91b0-8f2b4c2f1a61)


ORANGE Interface is “BLOCKED” causing a break in the loops

![image](https://github.com/psaumur/CCNA/assets/106411237/45125471-da23-4753-b5b1-16c23a2bfeff)


If changes occur in the connections, the traffic will adjust the Cấu trúc mạng.

- By selecting WHICH ports are FORWARDING and which ports are BLOCKING, STP creates a single path TO / FROM each point in the Network. This prevents LAYER 2 Loops.
- There is a set process that STP uses to determine which ports should be FORWARDING and which should be BLOCKING
- STP-enabled SWITCHES send / receive “Hello BPDUs” out of all INTERFACES
    - The Default timer is : ONCE every TWO seconds per Interface!
- If a Switch receives a “Hello BPDU” on an Interface, it knows that Interface is connected to another Switch (ROUTERS, PCs, etc. do NOT use STP so do not send “Hello BPDUs”)

---

WHAT ARE BPDUs USED FOR?

- SWITCHES use one field in the STP BPDU, the Bridge ID field, to elect a Bridge gốc for the Network
- The Switch with the lowest Bridge ID becomes the Bridge gốc
- ALL PORTS on the Bridge gốc are put in a FORWARDING state, and other SWITCHES in the Cấu trúc mạng must have a path to reach the Bridge gốc

![image](https://github.com/psaumur/CCNA/assets/106411237/05177f47-882e-47ea-8bec-22e073392e1c)

![image](https://github.com/psaumur/CCNA/assets/106411237/17f921f6-0583-4070-9493-5f5d80ad4866)

![image](https://github.com/psaumur/CCNA/assets/106411237/bb49a034-9f6d-4e92-9ea0-8bc71c4f2ec8)


To REDUCE the Bridge PRIORITY, we can only change it in units of 4096 !

![image](https://github.com/psaumur/CCNA/assets/106411237/39fe6239-1217-4885-b07b-8f368dad0e28)


In THIS Cấu trúc mạng, SW1 becomes the Bridge gốc due to it’s Địa chỉ MAC being LOWEST

(Hex “A” = 10)

![image](https://github.com/psaumur/CCNA/assets/106411237/b1e1a69d-4b9c-46bf-9b77-f30b9f7c3933)


ALL INTERFACES on the Bridge gốc are DESIGNATED PORTS.

DESIGNATED PORTS ARE IN A FORWARDING STATE!

Bridge gốc

- When a Switch is powered on, it assumes it is the Bridge gốc
- It will only give up its position if it receives a “SUPERIOR” BPDU (lower Bridge ID)
- Once the Cấu trúc mạng has converged and all SWITCHES agree on the Bridge gốc, only the Bridge gốc sends BPDUs
- Other SWITCHES in the Network will forward these BPDUs, but will not generate their own original BPDUs

---

Spanning Tree Giao thức STEPS

1) One Switch is elected as Bridge gốc. All PORTS on the Bridge gốc are DESIGNATED PORTS (FORWARDING STATE)

- Bridge gốc selection order:
    - 1) Lowest Bridge ID
    - 2) Lowest Địa chỉ MAC (in case of Bridge ID tie)

2) Each remaining Switch will select ONE of its INTERFACES to be it’s ROOT Port (FORWARDING STATE). PORTS across from the ROOT Port are always DESIGNATED PORTS.

- ROOT Port selection order:
    - 1) LOWEST ROOT COST (see STP COST CHART)
    - 2) LOWEST NEIGHBOUR Bridge ID
    - 3) LOWEST NEIGHBOUR Port ID

3) Each remaining COLLISION DOMAIN will select ONE Interface to be a DESIGNATION Port (FORWARDING STATE). The other Port in the COLLISION DOMAIN will NON-DESIGNATED (BLOCKING)

- DESIGNATED Port SELECTION:
    - 1) Interface on Switch with LOWEST ROOT COST
    - 2) Interface on Switch with LOWEST Bridge ID

---

STP COST CHART

💡 Only OUTGOING INTERFACES toward the Bridge gốc have a STP COST; not RECEIVING INTERFACES. Add up all the OUTGOING Port costs until you reach the Bridge gốc

![image](https://github.com/psaumur/CCNA/assets/106411237/0ee95883-aed8-42a3-ba82-11209ef8cd40)


SW1 is the Bridge gốc so has a STP COST of 0 on ALL INTERFACES

![image](https://github.com/psaumur/CCNA/assets/106411237/35037ae9-3430-44ac-be6d-c8d2a2a42c24)


The PORTS connected to another Switch’s ROOT Port MUST be DESIGNATED (D). 

Because the ROOT Port Is the Switch’s path to the Bridge gốc, another Switch must not block it.

STP Port ID (in case of a tie-breaker)

![image](https://github.com/psaumur/CCNA/assets/106411237/63d2fb87-31fa-4b57-a2c3-a203feded8ba)


NEIGHBOUR Switch Port ID (in case of a tie-breaker)

(D) = DESIGNATED Port

(R) = ROOT Port

![image](https://github.com/psaumur/CCNA/assets/106411237/c3fcc32b-e95f-4d4b-a241-f9f3080e858f)


Cách DETERMINE WHICH Port WILL BE BLOCKED TO PREVENT LAYER 2 LOOPS

![image](https://github.com/psaumur/CCNA/assets/106411237/1b69a092-4150-44c3-b605-5916fdea91d6)


QUIZ

Identify the Bridge gốc and the ROLE of EACH Interface on the Network (ROOT / DESIGNATED / NON-DESIGNATED)

#1

![image](https://github.com/psaumur/CCNA/assets/106411237/62bcf349-dd89-48be-92f6-d6a184edeb6f)


ALL SWITCHES have the same PRIORITY NUMBER (32769)

Tie-breaker goes to the LOWEST Địa chỉ MAC

SW3 has the LOWEST so it’s the Bridge gốc and ALL it’s INTERFACES become DESIGNATED

Connections from SW1 (G0/1) and S4 (G0/0) to SW3 become ROOT INTERFACES

Because SW2 has TWO connections to SW1, both of SW1’s INCOMING interfaces become DESIGNATED.

SW2 G0/2 Interface becomes a ROOT Interface because the G0/0 Interface of SW1 is LOWER than it’s G0/2 Interface

The remaining interfaces on SW2 become NON-DESIGNATED because it has the HIGHEST ROOT COST (12 = 4x 1 GB connection). INTERFACES they are attached to on other SWITCHES become DESIGNATED

#2

![image](https://github.com/psaumur/CCNA/assets/106411237/ae382ec2-9c0f-4673-94b5-5d1411c8db6b)


SW4 has the LOWEST Priority Number so it is designated Bridge gốc

All of SW4 INTERFACES become DESIGNATED

SW2 G0/0 becomes ROOT Port because SW4 G0/0 connection is a LOWER NUMBER than G0/1. 

SW3 G0/1 becomes ROOT Port

SW1 G0/1 becomes ROOT Port because G0/1 cost is LESS than Fa1/0 and 2/0

EACH remaining Port will be either DESIGNATED or NON-DESIGNATED

SW1 Fa1/0 and 2/0 become NON-DESIGNATED since they have a HIGHER STP COST (38) than SW2 outbound ports (8) making SW2 Fa1/0 and 2/0 DESIGNATED

SW2 remaining connection, G0/1, NON-DESIGNATED
