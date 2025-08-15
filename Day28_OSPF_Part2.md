# 27. OSPF : PART 2 (IGP : LINK STATE)

OSPF Metric (Cost)

- OSPFs Metric is called **COST**
- It is automatically calculated based on the bandwidth (SPEED) of the Interface
- It is calculated by DIVIDING a REFERENCE BANDWIDTH value by the Interface bandwidth
- The Default REFERENCE BANDWIDTH is 100 mbps
    - REFERENCE: 100 mbps / Interface: 10 mbps = COST (10)
    - REFERENCE: 100 mbps / Interface: 100 mbps = COST (1)
    - REFERENCE: 100 mbps / Interface: 1000 mbps = COST (1)
    - REFERENCE: 100 mbps / Interface: 10000 mbps = COST (1)
- ALL COST values less than 1 will be CONVERTED to 1
- Therefore FastEthernet (100 mbps), Gigabit Ethernet (1000 mbps), 10 Gig Ethernet, etc. are EQUAL and all have a COST of 1

FastEthernet COST

![image](https://github.com/psaumur/CCNA/assets/106411237/453258a2-e724-4bf5-b07c-6c533dcef46c)

Gigabit Ethernet COST

![image](https://github.com/psaumur/CCNA/assets/106411237/17adfd0e-8944-4016-93bd-98b82ceb8a66)

You can (and SHOULD) change the REFERENCE BANDWIDTH with this Lệnh:

💡 R1(config-Router)# **auto-cost reference-bandwidth** *megabits-per-second*

The Lệnh is entered in “megabits per second” (Default is “100”)

Example: using a value of “100000”

- 100000 / 100 = COST of 1000 for FastEthernet
- 100000 / 1000 = COST of 100 for Gig Ethernet

You should configure a reference bandwidth GREATER than the FASTEST links in your Network (to allow for future upgrades)

Changing the REFERENCE BANDWIDTH needs to be done on ALL OSPF ROUTERS in the Network

---

THE OSPF COST to a DESTINATION is the TOTAL COST of the ‘outgoing/exit INTERFACES’

LOOPBACK INTERFACES have a COST of 1

![image](https://github.com/psaumur/CCNA/assets/106411237/ef8de0f8-c22d-4259-bf4c-6fc9894bae29)

To CHANGE the OSPF COST of an Interface, you use the Lệnh :

<aside>
💡 R1(config-if)# ip OSPF cost <cost>
</aside>

MANUAL COSTS take precedent over AUTOMATIC CALCULATED COST

One more option to change the OSPF COST of an Interface is to change the BANDWIDTH of the Interface with the **“bandwidth”** Lệnh

The FORMULA to CALCULATE OSPF COST is :

<aside>
💡 **reference bandwidth / Interface bandwidth**

</aside>

- Although the BANDWIDTH matches the Interface SPEED (by Default), changing the Interface BANDWIDTH **doesn’t actually change the speed at which the Interface operates**
- The BANDWIDTH is just a VALUE that is used to calculate OSPF COST, EIGRP Metric, etcetera…
- To CHANGE the SPEED at which the Interface operates, use the **“speed”** Lệnh
- Because the BANDWIDTH VALUE is used in other calculations, it is NOT recommended to change this VALUE to alter the Interface’s OSPF COST

It is RECOMMENDED that you CHANGE the REFERENCE BANDWIDTH

THEN use the **“ip OSPF cost”** Lệnh to change the COST of the individual INTERFACES, if you want.

![image](https://github.com/psaumur/CCNA/assets/106411237/00196380-4452-4ec9-8cd9-b1949665a5d8)

---

SUMMARY:

THREE WAYS to modify the OSPF COST:

1) Change the ***reference bandwidth***

<aside>
💡 R1(config-Router)# **auto-cost reference-bandwidth** *megabits-per-second*
</aside>

2) Manual Configuration:

<aside>
💡 R1(config-Router)# ip OSPF cost <cost>
</aside>

3) Change the ***Interface bandwidth***

<aside>
💡 R1(config-Router)# **bandwidth <***kilobits-per-second>*
</aside>

![image](https://github.com/psaumur/CCNA/assets/106411237/aba02fbc-174c-41a1-a8e3-0ffdda3a6cbd)

---

BECOMING OSPF NEIGHBORS

- Making sure that ROUTERS successfully become OSPF NEIGHBORS is the MAIN task in configuring and Khắc phục sự cố OSPF.
- Once ROUTERS become NEIGHBORS, they AUTOMATICALLY do the work of sharing Network information, calculating routes, etc.
- When OSPF is activated on an Interface, the Router starts sending OSPF **“hello”** messages out of the Interface at regular intervals (determined by the **“hello timer”).** These are used to introduce the Router to potential OSPF NEIGHBORS
- The Default “**hello timer**” is **10 SECONDS** on an Ethernet connection
- **Hello** messages are Multicast to **224.0.0.5** (Multicast address for ALL OSPF ROUTERS)
- OSPF messages are ENCAPSULATED in an IP Header, with a **value of “89”** in the Giao thức field.

DOWN STATE

- OSPF is activated on R1s G0/0 Interface
- It sends an OSPF “hello” message to 224.0.0.5
- It doesn’t know about any OSPF neighbors yet, so the current neighbor state is DOWN

![image](https://github.com/psaumur/CCNA/assets/106411237/fa9b91da-e0c3-42d9-8c0a-eb47991b1894)

INIT STATE

- When R2 receives the “hello” Gói tin, it will add an entry for R1 to its OSPF neighbor table
- In R2’s neighbor table, the relationship with R1 is now in the INIT state
- INIT state = “hello” Gói tin received, but own Router ID is not in the “hello” Gói tin

![image](https://github.com/psaumur/CCNA/assets/106411237/70f3474f-f4bf-4194-b479-d7a65ad82505)

2-WAY STATE

- R2 will send a “hello” Gói tin containing the RID of BOTH ROUTERS
- R1 will insert R2 into its OSPF neighbor table in the 2-WAY state
- R1 will send another “hello” message, this time containing R2’s RID
- Both ROUTERS are now in the 2-WAY state

![image](https://github.com/psaumur/CCNA/assets/106411237/4d5e5310-4680-4176-94ab-2d8015032d18)

- The 2-WAY state means the Router has received a “hello” Gói tin with its own RID in it
- If both ROUTERS reach the 2-WAY state, it means that ALL of the conditions have been met for them to become OSPF neighbors.
- They are now READY to SHARE LSAs to build a common LSDB.
- In SOME Network types, a DR (Designated Router) and BDR (Backup Designated Router) will be elected at this point (OSPF Network Types and DR/DBR elections will be discussed in Day 28)

EXSTART STATE

- The TWO ROUTERS will now prepare to exchange information about their LSDB
- Before that, they have to choose which one will START the exchange
- They do THIS in the EXSTART state
    - The Router with the higher RID will become the MASTER and initiate the exchange.
    - The Router with the lower RID will become the SLAVE
- To decide the MASTER and SLAVE, they exchange DBD (Database Description) packets

![image](https://github.com/psaumur/CCNA/assets/106411237/34fa7cca-f837-432b-9296-d1be69a8869c)

EXCHANGE STATE

- In the EXCHANGE state, the ROUTERS exchange DBDs which contain a LIST of the LSAs in their LSDB
- These DBDs do NOT include detailed information about the LSAs, just BASIC INFORMATION
- The ROUTERS compare the information in the DBD they received to the information in their OWN LSDB to determine which LSAs they must receive from their neighbor

![image](https://github.com/psaumur/CCNA/assets/106411237/600722df-4737-4a69-867e-662c03a6b4b4)

LOADING STATE

- In the LOADING state, ROUTERS send **Link State Requests (LSR)** messages to request that their neighbors SEND them any LSAs they don’t have
- LSAs are sent in **Link State Update (LSU)** messages
- The ROUTERS send **LSAck** messages to acknowledge that they received the LSAs

![image](https://github.com/psaumur/CCNA/assets/106411237/4fc0fc23-ce00-4381-afef-259091b8f8ef)

FULL STATE

- In the FULL state, the ROUTERS have a FULL OSPF adjacency and identical LSDBs
- They continue to SEND and LISTEN for “hello” packets (every 10 seconds by Default) to maintain the neighbor adjacency
- Every time a “hello” Gói tin is received, the “DEAD” timer (40 seconds by Default) is reset
- If the DEAD timer counts down to 0 and no “hello” message is received, the neighbor is REMOVED
- The ROUTERS will continue to share LSAs as the Network changes to make sure each Router has a COMPLETE and ACCURATE map of the Network (LSDB)

![image](https://github.com/psaumur/CCNA/assets/106411237/daaa3a7b-ddd0-4ad0-ace7-056cbf2fbe32)

---

OSPF NEIGHBORS SUMMARY:

![image](https://github.com/psaumur/CCNA/assets/106411237/0d9f9d7e-04fd-472c-8449-a4f12172c055)

1 ) BECOME NEIGHBORS

- DOWN STATE
- INIT STATE
- 2-WAY STATE
- (DR/BDR ELECTION)

2) EXCHANGE LSAs

- EXSTART STATE
- EXCHANGE STATE
- LOADING STATE

---

SUMMARY OF OSPF MESSAGE TYPES

![image](https://github.com/psaumur/CCNA/assets/106411237/05b6d3ee-8fdb-4f25-9214-557eeb9a53a6)

---

MORE OSPF CONFIGURATIONS

Activate OSPF DIRECTLY on an Interface with this Lệnh:

<aside>
💡 R1(config-if)# ip OSPF *process-id* area *area*

</aside>

![image](https://github.com/psaumur/CCNA/assets/106411237/ad7aafd6-9cd8-4259-bd32-aff7b5893b46)

Configure ALL INTERFACES as OSPF Passive Interfaces

<aside>
💡 R1(config-Router) #passive-Interface Default

</aside>

![image](https://github.com/psaumur/CCNA/assets/106411237/e953696d-283f-4676-8df2-9aff0418d78d)

Can then REMOVE specific INTERFACES from being passive using:

<aside>
💡 R1(config-Router) #no passive-Interface *Interface-id*

</aside>

Activating OSPF DIRECTLY on INTERFACES will show a different output in “show ip protocols”

![image](https://github.com/psaumur/CCNA/assets/106411237/915e31ee-4fee-455b-a947-229e0af4b182)

They will appear under “Định tuyến on Interfaces Configured Explicitly (Area #) :” (as above)

Showing the OSPF LSDB of a Device

![image](https://github.com/psaumur/CCNA/assets/106411237/75c941ca-b6bd-45f0-9a85-c7e5baff4654)
