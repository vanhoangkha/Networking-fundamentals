# 26.  OSPF : PART 1 (IGP : LINK STATE)

![image](https://github.com/psaumur/CCNA/assets/106411237/f58477d1-f574-4195-8f6c-851823dedfbf)

LINK STATE Định tuyến PROTOCOLS

- When using a LINK STATE Định tuyến Giao thức, every Router creates a ‘connectivity map’ of the Network
- To allow this, each Router ADVERTISES information about its INTERFACES (connected NETWORKS) to its NEIGHBOURS. These ADVERTISEMENTS are passed along to the other ROUTERS, until all ROUTERS in the Network develop the same map of the Network
- Each Router independently uses this MAP to calculate the BEST ROUTES to each DESTINATION
- LINK STATE PROTOCOLS use more resources (CPU) on the Router, because MORE information is shared.
- However, LINK STATE PROTOCOLS tend to be FASTER in reacting to CHANGES in the Network than DISTANCES VECTOR PROTOCOLS

---

BASIC OSPF OPERATIONS

- Stands for **Open Shortest Path First**
- Uses the **Shortest Path First** algorithm
    - Created by Dutch comp. scientist - Edsger Dijkstra
    - aka **Dijkstra’s Algorithm** (Could be Exam Question)

THREE Versions:

- OSPFv1 (1989) : OLD, not in use anymore
- OSPFv2 (1998) : Used for IPv4
- OSPFv3 (2008) : Used for IPv6 (can be used for IPv4, but v2 is usually used)

- Routers store information about the Network in LSAs (Link State Advertisements), which are organized in a structure called the LSDB (Link State Database)
- Routers will **FLOOD** LSAs until all ROUTERS in the OSPF *area* develop the same map of the Network (LSDB)

![image](https://github.com/psaumur/CCNA/assets/106411237/2a6a126b-74f1-49e2-96be-fc411c8812fd)

💡 LSA’s have an AGING TIMER of 30 Minutes, by Default). The LSA will be FLOODED again after the timer expires

In OSPF, there are THREE MAIN STEPS in the process of sharing LSAs and determining the BEST Tuyến đường to each DESTINATION in the Network

1) **BECOME NEIGHBORS** with other ROUTERS connected to same Đoạn

2) **EXCHANGE LSAs** with neighbor ROUTERS

3) **CALCULATE THE BEST ROUTES** to each DESTINATION, and insert them into the Định tuyến TABLE

---

OSPF AREAS

- OSPF uses **AREAS** to divide up the Network
- SMALL NETWORKS can be *single-area* without any negative effects on performance
- LARGE NETWORKS, *single-area* design can have NEGATIVE effects:
    - SPF ALGORITHM takes more time to calculate ROUTES
    - SPF ALGORITHM requires exponentially more processing power on ROUTERS
    - Larger LSDB takes up more MEMORY on ROUTERS
    - Small changes in Network cause every Router to FLOOD LSAs and run the SPF algorithm again
- By dividing up a large OSPF Network into several SMALLER ***areas***, you can avoid the above NEGATIVE effects (sounds similar to VLANs re: Broadcast domains)

là gì AN OSPF AREA?

![image](https://github.com/psaumur/CCNA/assets/106411237/0f5084fe-f7fb-4b33-a8d0-2ed0155d7502)

- An **AREA is** a set of ROUTERS and LINKS that share the same LSDB
- The **BACKBONE AREA** (Area 0) is an AREA that all other AREAS must connect to
- ROUTERS with ALL INTERFACES in the SAME AREA are called INTERNAL ROUTERS
- ROUTERS with INTERFACES in MULTIPLE AREAS are called **AREA BORDER ROUTERS** (ABRs)
    

💡 ABRs maintain a SEPARATE LSDB for each AREA they are connected to.

💡 It is recommended that you connect an ABR to a MAXIMUM of TWO AREAS.

💡 Connecting an ABR to 3+ AREAS can overburden the Router

- ROUTERS connected to the BACKBONE AREA (Area 0) are called **BACKBONE ROUTERS**
- An **INTRA-AREA Tuyến đường** is a Tuyến đường to a DESTINATION inside the same OSPF AREA
- An INTER-AREA Tuyến đường is a Tuyến đường to a DESTINATION in a DIFFERENT OSPF AREA

--- 

OSPF RULES

- OSPF AREAS should be CONTIGUOUS (no split AREAS)
- All OSPF AREAS must have *at least* ONE ABR connected to the BACKBONE AREA
- OSPF INTERFACES in the SAME Network con *must* be in the SAME AREA

---
BASIC OSPF Configuration

OSPF AREA 0

![image](https://github.com/psaumur/CCNA/assets/106411237/ad9648f4-736a-43b5-96de-8a30f6f800c8)

Commands for configuring an OSPF 

![image](https://github.com/psaumur/CCNA/assets/106411237/38fcce32-8d15-4db0-9a0c-170d6083a534)

- The OSPF **Process ID** is **locally significant.** ROUTERS with different Process IDs can become OSPF Neighbors
- The OSPF “Network” Lệnh requires you to specify the AREA (in this case, it’s “area 0”)
- For the CCNA, you only need to configure single-area OSPF (AREA 0)

The “Network” Lệnh tells OSPF to:

- Look for ANY INTERFACES with an Địa chỉ IP contained in the RANGE specified in the “Network” Lệnh
- Activate OSPF on the Interface in the specified AREA
- The Router will then try to become OSPF neighbors with other OSPF-Activated neighbor ROUTERS

![image](https://github.com/psaumur/CCNA/assets/106411237/41da3fe8-f24a-468c-beeb-91cc12066c70)

- Know this Lệnh from RIP and EIGRP
- The “passive-Interface” Lệnh tells the ROUTERS to stop sending OSFP ‘hello’ messages out of the Interface
- However, the Router will continue to send LSA’s informing it’s neighbors about the Network con configured on the Interface
- You should ALWAYS USE this Lệnh on neighbors which don’t have any OSPF neighbors

![image](https://github.com/psaumur/CCNA/assets/106411237/a0422f88-dbd9-4965-8c73-16cfd438b05e)

![image](https://github.com/psaumur/CCNA/assets/106411237/aaa1daaa-8ab7-441a-bec2-9f0391a82ecc)

“show ip protocols”

![image](https://github.com/psaumur/CCNA/assets/106411237/f02c3838-c9ad-4836-8c89-ecad42e205b2)

NOTE the "no" in square brackets - this indicates this is the Default choice

![image](https://github.com/psaumur/CCNA/assets/106411237/c222d290-4d10-4e63-b7d5-8317ae5ccdfc)

DISTANCE (AD) for OSPF is 110 (Default) but can be changed with the “distance” Lệnh

![image](https://github.com/psaumur/CCNA/assets/106411237/849a7fd3-457e-4310-be08-b4c8b4c8a8a2)
