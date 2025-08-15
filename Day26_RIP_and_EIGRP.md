# 25. RIP AND EIGRP (IGP : DYNAMIC VECTOR)

Định tuyến INFORMATION Giao thức (RIP)

- Định tuyến Information Giao thức (Industry Standard)
- is a DISTANCE VECTOR IGP
    - uses Định tuyến-By-Rumor logic to learn/share routes
- Uses HOP COUNT as it’s Metric (One Router = One Hop)  Bandwidth is irrelevant
- MAX HOP COUNT is 15 (anything more is considered unreachable)
- Has THREE VERSIONS:
    - RIPv1 and RIPv2; used for IPv4
    - RIPng (RIP Next Generation) used for IPv6
- Uses TWO MESSAGE TYPES:
    - REQUEST :
        - To ask RIP-ENABLED neighbour ROUTERS to send their Định tuyến TABLE
    - RESPONSE:
        - To SEND the LOCAL Router’s Định tuyến TABLE to neighbouring ROUTERS

By Default, RIP-Enabled ROUTERS will share their Định tuyến TABLE every 30 seconds

RIPv1 and RIPv2

RIPv1:

- Only advertises *classful addresses* (Class A, Class B, Class C)
- Doesn’t support VLSM, CIDR
- Doesn’t include Network con MASK information in ADVERTISEMENTS (RESPONSE messages)
    - Example:
        - 10.1.1.0/24 will become 10.0.0.0 (Class A Address, so assumed to be /8)
        - 172.16.192.0/18 will become 172.16.0.0 (Class B Address, so assumed to be /16)
        - 192.168.1.40/30 will become 172.168.1.0 (Class C Address, so assumed to be /24)
- Messages are Broadcast to 255.255.255.255

RIPv2:

- Supports VLSM, CIDR
- Includes Network con MASK information in ADVERTISEMENTS
- Messages are **Multicast** to 224.0.0.9
    - Broadcast Messages are delivered to ALL devices on the local Network
    - Multicast Messages are delivered only to devices to have joined that specific ***Multicast group***

---

CONFIGURING RIP

![image](https://github.com/psaumur/CCNA/assets/106411237/1d14ec8b-121c-4666-b608-1e5d1889424c)

The **“Network”** Lệnh tells the Router to:

- Look for INTERFACES with an Địa chỉ IP that is in the specific RANGE
- ACTIVATES RIP on the INTERFACES that fall in the RANGE
- Form ADJACENCIES with connected RIP neighbors
- Advertise the **Network PREFIX of the Interface** (NOT the prefix in the “Network” Lệnh)

The OSPF and EIGRP **“Network”** commands operate in the same way

Because the RIP “Network” Lệnh is CLASSFUL. It will automatically convert to CLASSFUL networks

- 10.0.0.0 is assumed to be 10.0.0.0/8
- R1 will look for ANY INTERFACES with an Địa chỉ IP that matches 10.0.0.0/8 (because it is /8 it only needs to match the FIRST 8 bits)
- 10.0.12.1 and 10.0.13.1 both match SO RIP is ACTIVATED on G0/0 and G0/1
- R1 then forms ADJACENCIES with its neighbors R2 and R3
- R1 ADVERTISES 10.0.12.0/30 and 10.0.13.0/30 (NOT 10.0.0.0/8) to it’s RIP neighbors

![image](https://github.com/psaumur/CCNA/assets/106411237/2a9452f0-b48f-499d-938f-0a3db5ff6587)

- Because the “Network” Lệnh is CLASSFUL, 172.16.0.0 is assumed to be 172.16.0.0/16
- R1 will look for ANY INTERFACES that match 172.16.0.0/16
- 172.16.1.14 matches, so R1 will ACTIVATE RIP on G2/0
- There are NO RIP neighbors connected to G2/0 so no NEW ADJACENCIES are formed
    - Although there are NO RIP neighbors, R1 will still send ADVERTISEMENTS out of G2/0.
    - This is unnecessary traffic, so G2/0 should be configured as a **passive Interface**

![image](https://github.com/psaumur/CCNA/assets/106411237/634f4c6b-291c-4a21-8ae2-c8283044efce)

- the “passive-Interface” Lệnh tells the Router to stop sending RIP advertisements out of the specified Interface (G2/0)
- However, the Router will continue to ADVERTISE the Network prefix of the Interface (172.16.1.0/28) to it’s RIP neighbors (R2, R3)
- You should ALWAYS use this Lệnh on INTERFACES which don’t have any RIP neighbors
- EIGRP and OSPF both have the same passive Interface functionality, using the same Lệnh.

---

Cách ADVERTISE A Default Tuyến đường INTO RIP

![image](https://github.com/psaumur/CCNA/assets/106411237/57de003e-0e8e-48c7-bb72-fbe25208d847)

![image](https://github.com/psaumur/CCNA/assets/106411237/1c500efd-e96b-4e49-b1f4-f99c54b0e877)

To SHARE this Default Tuyến đường with R1’s RIP neighbors, using this Lệnh:

![image](https://github.com/psaumur/CCNA/assets/106411237/799d818a-06cc-4f29-8c74-c67639c9d014)

RIP doesn’t care about Interface AD cost (RIP cost is 120), only “hops”.

Since both have an equal number of “hops”, both paths appear in the Default Tuyến đường (Gateway of Last Resort)

![image](https://github.com/psaumur/CCNA/assets/106411237/1deccb54-02e0-4d3b-b203-277d656504b3)

---

“show ip protocols” (for RIP)

![image](https://github.com/psaumur/CCNA/assets/106411237/b7ab4046-b6eb-4e19-b7eb-2c5d2889293a)

“Maximum path: 4” is the Default but can be changed with this Lệnh:

![image](https://github.com/psaumur/CCNA/assets/106411237/35d524bd-055d-4c5e-a84b-f507a87738e0)

“Distance” (AD) can be changed with this Lệnh (Default is 120)

![image](https://github.com/psaumur/CCNA/assets/106411237/5247942b-1d6b-419f-a4c7-75bfcca43fe6)

---

ENHANCED INTERIOR Gateway Định tuyến Giao thức (EIGRP)

- Enhanced Interior Gateway Định tuyến Giao thức
- is a DISTANCE VECTOR IGP
- Was Cisco proprietary, but Cisco has now published it openly so other vendor can implement it on their equipment
- Considered an “advanced” / “hybrid” DISTANCE VECTOR Định tuyến Giao thức
- Much faster than RIP in reacting to changes in the Network
- Does NOT have the 15 ‘hop count’ limit of RIP
- Sends messages using Multicast ADDRESS **224.0.0.10 (Memorize this number)**
- Is the ONLY IGP that can perform **unequal**-cost load-balancing (by Default, it performs ECMP load-balancing over 4 paths like RIP)

---

Configuration OF EIGRP

![image](https://github.com/psaumur/CCNA/assets/106411237/f2b42631-bcb9-4f62-afe9-b7bb1e7e0d7e)

“Router EIGRP <Autonomous System number>”

- The AS (Autonomous System) number MUST MATCH between ROUTERS or they will NOT form an ADJACENCY and share Tuyến đường information
- Auto-summary might be ENABLED or DISABLED by Default; depending on the Router/IOS version. If ENABLED, Vô hiệu hóa it.
- The **“Network”** Lệnh will assume a CLASSFUL ADDRESS, if you don’t specify the Network con MASK
- EIGRP uses a *wildcard mask* instead of a regular Network con mask

A WILDCARD MASK is an “inverted” Network con MASK

- All 1’s in the Network con MASK are 0 in the equivalent WILDCARD MASK.
- All 0s in the Network con MASK are 1 in the equivalent WILDCARD MASK.

![image](https://github.com/psaumur/CCNA/assets/106411237/f64e06d3-75ad-4f4f-b7d6-26f27ffae541)

“0” in the WILDCARD MASK = BITS MUST MATCH !

“1” in the WILDCARD MASK = Do not have to match

![image](https://github.com/psaumur/CCNA/assets/106411237/13130e3c-de62-4f80-9c7d-256a2ed47e74)

![image](https://github.com/psaumur/CCNA/assets/106411237/1aa2cd2c-397f-4f3b-86ed-81eddf2677a6)

![image](https://github.com/psaumur/CCNA/assets/106411237/500ac3b0-5d83-4691-ab94-06fd330a9111)

---

“show ip protocols” (for EIGRP)

![image](https://github.com/psaumur/CCNA/assets/106411237/f3f169da-d733-4da9-8d8a-c90e2077d8a7)

“Router ID”

Router ID order of priority:

- Manual Configuration
- Highest Địa chỉ IP on a LOOPBACK Interface
- Highest Địa chỉ IP on a PHYSICAL Interface

![image](https://github.com/psaumur/CCNA/assets/106411237/29757624-9e79-4878-8724-36d5da43f39b)

“Distance” (AD)

EIGRP has TWO VALUES:

- Internal = 90
- External = 170

MEMORIZE THESE VALUES!

“show ip Tuyến đường” (for EIGRP)

![image](https://github.com/psaumur/CCNA/assets/106411237/8216ceb6-0d3f-42e7-8e5b-46e810097fb8)

NOTE the large Metric numbers. This is a DOWNSIDE to EIGRP - even on small networks!

---

EIGRP Metric

- By Default, EIGRP uses BANDWIDTH and DELAY to calculate Metric
- Default “K” values are:
    - K1 = 1, K2 = 0, K3 = 1, K4 = 0, K5 = 0

💡 Simplified calculation : Metric = BANDWIDTH (Slowest Link) + DELAY (of ALL LINKS)

---

EIGRP TERMINOLOGY

- **Feasible Distance** = This Router’s Metric value to the Tuyến đường’s DESTINATION
- **Reported Distance** (aka **Advertised Distance**) = The neighbor’s Metric value to the Tuyến đường’s DESTINATION

![image](https://github.com/psaumur/CCNA/assets/106411237/436ba2c2-43e7-4fea-a527-f88a8e4460bc)

- **Successor =** the Tuyến đường with the LOWEST Metric to the DESTINATION (the best Tuyến đường)
- **Feasible Successor** = An alternate Tuyến đường to the DESTINATION (not the best Tuyến đường) which meets the *feasibility condition*

**FEASIBILITY CONDITION** : A Tuyến đường is considered a ***Feasible Successor*** if it’s ***Reported Distance*** is LOWER than the Successor Tuyến đường’s ***Feasible distance***

![image](https://github.com/psaumur/CCNA/assets/106411237/206db633-3a7e-4d11-bb80-029ea8107503)

---

EIGRP : UNEQUAL-COST LOAD-BALANCED

![image](https://github.com/psaumur/CCNA/assets/106411237/23a2045b-a925-4f75-b0f8-78cbae2aa1e2)

“maximum Metric variance 1” = the Default value

Variance 1 = only ECMP (Equal-Cost Multiple Path) load-balancing will be performed

![image](https://github.com/psaumur/CCNA/assets/106411237/824dac1d-38dc-4e7e-bb48-b382918230ff)

Variance 2 = ***feasible successor*** routes with an FD up to 2x the ***successor*** Tuyến đường’s FD can be used to load-balance

💡 EIGRP will only perform UNEQUAL-COST LOAD-BALANCING over ***feasible successor*** ROUTES. If a Tuyến đường doesn’t meet the ***feasibility condition***, it will NEVER be selected for load-balancing, regardless of **variance**
