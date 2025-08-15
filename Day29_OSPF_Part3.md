# 28. OSPF : PART 3 (IGP: LINK STATE)

LOOPBACK INTERFACES

- A LOOPBACK Interface is a virtual Interface in the Router
- It is ALWAYS UP/UP - unless you manually shut it down
- It is NOT dependent on a PHYSICAL Interface
- So, it provides a consistent Địa chỉ IP that can be used to REACH / IDENTIFY the Router

![image](https://github.com/psaumur/CCNA/assets/106411237/697e7d43-b428-4fe3-a270-5fc1c9ad13d0)

---

OSPF Network TYPES

- The OSPF “Network TYPE” refers to the TYPES of connection between OSPF neighbors (Ethernet, etc.)

- There are THREE MAIN OSPF Network TYPES:

- Broadcast :
    - Enabled by Default on **Ethernet** and **FDDI** (Fiber Distributed Data Interfaces) INTERFACES

- POINT TO POINT :
    - Enabled by Default on **PPP** (Point-to-Point) and **HDLC** (High-Level Data Link Control) INTERFACES

- NON-Broadcast :
    - Enabled by Default on **Khung RELAY** and **X.25** INTERFACES

<aside>
💡  CCNA focuses on Broadcast and POINT-TO-POINT types

</aside>

---

OSPF Broadcast Network TYPE

![image](https://github.com/psaumur/CCNA/assets/106411237/8f99053d-3501-4d1d-86a2-f859c62c160d)

- Enabled on Ethernet and FDDI interfaces by Default
- ROUTERS *dynamically discover* neighbors by SENDING / LISTENING for OSPF “Hello” messages using the Multicast address 224.0.0.5
- A **DR (DESIGNATED Router)** and **BDR (BACKUP DESIGNATION Router)** must be elected on each Network con (only DR if there are no OSPF neighbors, ie: R1’s G1/0 Interface)
- ROUTERS which aren’t the DR or BDR become a **DROther**

![image](https://github.com/psaumur/CCNA/assets/106411237/1ba5b6e1-dd4a-4277-8f33-f806e21302bc)

The DR / BDR election order of priority:

1) Highest OSPF Interface PRIORITY

2) Highest OSPF Router ID

“First Place” becomes the DR for the Network con

“Second Place” because the BDR

<aside>
💡 Default OSPF Interface PRIORITY is “1” on ALL INTERFACES!

</aside>

The Lệnh to change the OSPF PRIORITY of an Interface is :

<aside>
💡 R2(config-if)# ip OSPF priority <priority number>

</aside>

![image](https://github.com/psaumur/CCNA/assets/106411237/cd98b06f-3730-4b2d-8dfe-a6387fdb66a1)

<aside>
💡 IF an OSPF PRIORITY is set to “0”, the Router CANNOT be the DR / BDR for the Network con!

</aside>

The DR / DBR ELECTION is “non-preemptive”.

Once the DR / DBR are selected, they will keep their role until OSPF is:

- Reset
- Interface fails
- Is shut down
- etc.

![image](https://github.com/psaumur/CCNA/assets/106411237/e59e6217-0404-476d-9bcf-49e82c380b84)

![image](https://github.com/psaumur/CCNA/assets/106411237/82eb1f11-4aed-456b-b2b1-1679cae06743)

<aside>
💡 In the Broadcast Network TYPE, ROUTERS will only form a FULL OSPF ADJACENCY with the DR and the BDR of the Đoạn!

</aside>

Therefore, ROUTERS only exchange LSAs with the DR and BDR.

DROthers will NOT exchange LSAs with each other.

ALL ROUTERS will still have the same LSDB but THIS reduces the amount of LSAs flooding the Network

<aside>
💡 MESSAGES to the DR / BDR are Multicast to 224.0.0.6

</aside>

The DR and BDR will form a FULL ADJACENCY with ALL ROUTERS in the Network con

DROthers will form a FULL ADJACENCY ONLY with the DR / BDR !

![image](https://github.com/psaumur/CCNA/assets/106411237/61e1c230-3926-40ae-917a-55fcf76caf64)

---

OSPF POINT-TO-POINT Network TYPE

![image](https://github.com/psaumur/CCNA/assets/106411237/51d7d486-a810-4a69-8be2-804f667fca03)

- ENABLED on **SERIAL** INTERFACES using the **PPP** and **HDLC** encapsulations, by Default
- ROUTERS dynamically discover neighbors by SENDING / LISTENING for OSPF “Hello” messages using the Multicast address 224.0.0.5
- A DR and BDR are NOT elected
- These ENCAPSULATIONS are used for “Point-To-Point” connections
    - Therefore, there is no point in electing  a DR and DBR
    - The TWO ROUTERS will form a FULL ADJACENCY with each other

---

(ASIDE)

SERIAL INTERFACES

![image](https://github.com/psaumur/CCNA/assets/106411237/02f6f3a8-dcbb-46cd-bb2e-47ceb84d10cc)

- One side of SERIAL CONNECTION functions as DCE (Data Communications Equipment)
- The OTHER side functions as DTE (Data Terminal Equipment)
- ONLY the DCE side needs to specify the *clock rate* (speed) of the connection

Ethernet INTERFACES use the “speed” Lệnh to configure the operating speed.

SERIAL INTERFACES use the “clock rate” Lệnh

![image](https://github.com/psaumur/CCNA/assets/106411237/c32af4a3-105c-451a-9641-0f7fc26e7f42)

If you change the Đóng gói, it must MATCH on BOTH ENDS or the Interface will go down.

![image](https://github.com/psaumur/CCNA/assets/106411237/8a448ef2-96f2-4371-bef1-520572ba5224)

R1 and R2 sharing the SAME Đóng gói Type 

![image](https://github.com/psaumur/CCNA/assets/106411237/6f934097-30fb-4605-935d-08a29e53a476)


SERIAL INTERFACES SUMMARY

- The Default Đóng gói is HDLC
- You can configure PPP Đóng gói with this Lệnh:
    
    <aside>
    💡 R1(config-if)# **Đóng gói ppp**
    
    </aside>
    
- One side is DCE, other side is DTE
- Identify which side is DCE / DTE :
    
    <aside>
    💡 R1# **show controllers** *Interface-id*
    
    </aside>
    
- You must configure the CLOCK RATE on the DCE side:
    
    <aside>
    💡 R1(config-if)# clock rate *bits-per-second*
    
    </aside>
    

---

![image](https://github.com/psaumur/CCNA/assets/106411237/bc5a756e-c65d-4585-ad3f-c0e29682c0eb)

![image](https://github.com/psaumur/CCNA/assets/106411237/232c8658-d129-49f4-9a37-76139ebe857e)

- You can configure the OSPF Network TYPE on an Interface with :

<aside>
💡 R1(config-if)# ip OSPF Network <Network type>

</aside>

Ví dụ, if TWO ROUTES are directly connected with an Ethernet link, there is no need for a DR / DBR. You can configure the POINT-TO-POINT Network type in this case

NOTE: Not all Network TYPES work on ALL LINK TYPES (Ví dụ, a serial link cannot use the Broadcast Network type)

![image](https://github.com/psaumur/CCNA/assets/106411237/8688e7ef-d166-4433-9f65-b918917f385f)

<aside>
💡 NON-Broadcast Network type Default Timers : Hello 30, Dead 120

</aside>

---

OSPF NEIGHBOUR / ADJACENCY REQUIREMENTS

1) AREA NUMBER MUST MATCH

2) INTERFACES must be in the SAME Network con

3) OSPF PROCESS must not be **SHUTDOWN**

![image](https://github.com/psaumur/CCNA/assets/106411237/80b626ac-f368-4d86-85f4-dc80e3be5259)

4) OSPF Router ID must be unique

![image](https://github.com/psaumur/CCNA/assets/106411237/8f089c68-96e9-4cbf-a9c0-c93f74de4888)

5) HELLO and DEAD Timers must MATCH

6) AUTHENTICATION settings must MATCH

![image](https://github.com/psaumur/CCNA/assets/106411237/06cab926-a458-4978-b754-b2253ee74762)

*** SPECIAL REQUIREMENTS *** 

7) IP MTU settings must MATCH

- IP MTU : Maximum size of an IP Gói tin that can be sent from an Interface
- If the settings DO NOT match, can still become OSPF Neighbors but OSPF WILL NOT operated properly

8) OSPF Network TYPE must match

- will appear to be working but NEIGHBOR won’t appear in Định tuyến information

---

OSPF LSA TYPES

- The OSPF LSDB is made up of LSAs
- There are 11 types of LSA but there are only 3 you should be aware of for the CCNA:
    - Type 1 (Router LSA)
    - Type 2 (Network LSA)
    - Type 5 (AS External LSA)

TYPE 1 (Router LSA)

- Every OSPF Router generates this type of LSA
- It identifies the Router using it’s Router ID
- It also lists NETWORKS attached to the Router’s OSPF-Activated INTERFACES

TYPE 2 (Network LSA)

- Generated by the DR of EACH “multi-Access” Network (ie: the Broadcast Network type)
- Lists the ROUTERS which are attached to the multi-Access Network

TYPE 5 (AS-External LSA)

- Generated by ASBRs to describe ROUTES to DESTINATIONS outside of the AS (OSPF Domain)
