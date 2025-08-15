# 24. DYNAMIC ĐỊNH TUYẾN

là gì DYNAMIC Định tuyến?

![image](https://github.com/psaumur/CCNA/assets/106411237/8acc17ee-5d4b-4725-b5e4-18dc5743340e)

- LAYER 3
- Involves configuring a DYNAMIC Định tuyến Giao thức on the Router and letting the Router take care of finding the best routes to DESTINATION NETWORKS.
- Not Fixed (will adapt to changes in the LAN)

![image](https://github.com/psaumur/CCNA/assets/106411237/deb9abf6-6e21-4c94-a407-bfc501a1d739)


💡 A Network Tuyến đường :  A Tuyến đường to a Network or Network con (Mask Length < /32)

Ex: **10.0.12.0/30** and **10.0.13.0/30** (above) are Network ROUTES

💡 A HOST Tuyến đường : A Tuyến đường to a specific HOST (/32 Mask)

Ex: **10.0.12.1/32** and **10.0.13.1/32** (above) are HOST ROUTES

These two ROUTES were AUTOMATICALLY added to R1’s G0/0 and G1/0s INTERFACES

---

HOW DYNAMIC Định tuyến WORKS ?

![image](https://github.com/psaumur/CCNA/assets/106411237/9d2d7f88-a325-461f-99fd-0dc88ee23749)

(R4 ADVERTISES to R2 who ADVERTISES to R1 who ADVERTISES to R3 - They add the Network Tuyến đường to R4 in their Tuyến đường TABLE)

If the Network Tuyến đường breaks, the Tuyến đường is DYNAMICALLY REMOVED from the Tuyến đường TABLE

![image](https://github.com/psaumur/CCNA/assets/106411237/a477d438-f6cb-4a09-b66d-e07826755bd1)

(R1 removing the Tuyến đường to R4 from it’s Tuyến đường TABLE)

IN STATIC Định tuyến, a downed Router will still have traffic passed to it. The Tuyến đường TABLES are unchanged.

![image](https://github.com/psaumur/CCNA/assets/106411237/e689a88a-7275-489c-80b4-18894a7ce4c9)

(R1 has a STATIC Tuyến đường to R4 and passes traffic destined to it’s Network regardless of status)

DYNAMIC Định tuyến is good but still requires REDUNDANCY so we add another connection between R3 and R4

![image](https://github.com/psaumur/CCNA/assets/106411237/8a7cb9cb-beea-4522-87f7-7fd11df9f745)

(Secondary DYNAMIC Tuyến đường added to R4 from R1 via R3. Tuyến đường TABLE updated appropriately)

A failure in the Tuyến đường, via R2 to R4’s G0/0 Interface, automatically reroutes traffic via R3

![image](https://github.com/psaumur/CCNA/assets/106411237/d4509ce2-07f1-4fb0-8e31-cf58c049c355)

Why does the path prefer using R2’s path versus R3? 

Because of COST !  This is similar to how SPANNING-TREE works (with SWITCHES)

---

INTRODUCTION TO DYNAMIC Định tuyến PROTOCOLS

- ROUTERS can use DYNAMIC Định tuyến PROTOCOLS to ADVERTISE information about the ROUTES they know to OTHER ROUTES
- They form ‘ADJACENCIES’ / ‘NEIGHBOR RELATIONSHIPS’ / ‘NEIGHBORSHIPS’ with ADJACENT ROUTERS to exchange this information
- If multiple ROUTES to a DESTINATION are learned, the Router determines which Tuyến đường is SUPERIOR and adds it to the Định tuyến TABLE. It uses the ‘Metric’ of the Tuyến đường to decide which is superior (lower Metric = superior)

---

TYPES OF DYNAMIC Định tuyến PROTOCOLS

DYNAMIC Định tuyến PROTOCOLS can be divided into TWO main categories:

- IGP (Interior Gateway Giao thức)
- EGP (Exterior Gateway Giao thức)

IGP

- Used to SHARE ROUTES within a single *autonomous system* (AS), which is a single organization (ie: a company)

![image](https://github.com/psaumur/CCNA/assets/106411237/06af6c77-3a03-44fa-8c55-9382347d3f5e)

EGP

- Used to SHARE ROUTES *between* different *autonomous systems (AS)*

![image](https://github.com/psaumur/CCNA/assets/106411237/37680a4b-caab-4e1d-ac64-00a799bd965f)

Algorithms used for IGP and EGP and the Giao thức for each

![image](https://github.com/psaumur/CCNA/assets/106411237/36729569-0e56-4eb2-91ee-e7cd25a8c234)

💡 YOU MUST MEMORIZE WHICH ALGORITHM IS USED FOR EACH Giao thức FOR THE CCNA!

---

DISTANCE VECTOR Định tuyến PROTOCOLS

- Called DISTANCE VECTOR because the ROUTERS only learn the ‘distance’ (Metric) and ‘vector’ (DIRECTION, NEXT-HOP Router) of each Tuyến đường

- DISTANCE VECTOR PROTOCOLS were invented before LINK STATE PROTOCOLS
- Early examples are RIPv1 and Cisco’s IGRP (which was updated to EIGRP)
- DISTANCES VECTOR PROTOCOLS operate by sending the following to their directly connection neighbors:
    - Their KNOWN DESTINATION networks
    - Their Metric to reach their KNOWN DESTINATION networks
- This METHOD of sharing Tuyến đường information is often called ***‘Định tuyến by rumor’***
    - ***‘Định tuyến by rumor’*** = because the Router doesn’t know about the Network beyond it’s NEIGHBOURS. It only knows the information that the NEIGHBOURS tell it.

![image](https://github.com/psaumur/CCNA/assets/106411237/773eb20d-7983-4da4-ae66-e97e421e83ba)

---

DYNAMIC Định tuyến Giao thức METRICS

- A Router’S Tuyến đường TABLE contains the BEST Tuyến đường to each DESTINATION Network it knows about

If a Router using a DYNAMIC Định tuyến Giao thức learns TWO different routes to the same DESTINATION, how does it determine which is **‘best’** ?

It uses the Metric value of the ROUTES to determine which is BEST.

A lower Metric = BETTER! (just like STP)

EACH Định tuyến Giao thức uses a different Metric to determine which Tuyến đường is best

![image](https://github.com/psaumur/CCNA/assets/106411237/bf324652-f4b8-482e-af17-03da590ac85d)

The above choose the RED PATH because the “cost”, using R3 F2/0 and R4 F2/0 (FastEthernet) is HIGHER than the  R2 G1/0 and R4 G0/0 (GigabyteEthernet)

What if BOTH connections were GigabyteEthernet? (ie: the same Metric value)

![image](https://github.com/psaumur/CCNA/assets/106411237/3f8437cc-5b38-4f1e-b185-c5e9fce6c5f1)

BOTH ROUTES are added to the Tuyến đường TABLE

So …

💡 If a Router learns TWO (or more) ROUTES via the same ****Định tuyến Giao thức to the same DESTINATION (same Network address, same Network con mask) with the same Metric, both will be added to the Định tuyến table. Traffic will be LOAD-BALANCED over both ROUTES

![image](https://github.com/psaumur/CCNA/assets/106411237/79662f99-a847-457b-8080-76f77c25c5e6)

“O” = OSPF Giao thức (next to ROUTES)

[110/3] :

- the “3” part is the Metric.
- the “110” part is Khoảng cách quản trị (covered later)


💡 Since BOTH ROUTES share the same Metric, this is called ECMP (EQUAL COST MULTI-PATH)

You can have ECMP with STATIC ROUTES, as well (they don’t use Metric, however)

---

SUMMARY OF DIFFERENT METRICS

![image](https://github.com/psaumur/CCNA/assets/106411237/7b8390aa-46d4-49d3-83a4-03ba095bf927)

(IS-IS won’t be covered in detail)

EXAMPLE

![image](https://github.com/psaumur/CCNA/assets/106411237/d0c6c9f2-3526-46b2-b520-1f4b6b28ea8f)

Using RIP, both ROUTES would be put in R1’s Tuyến đường TABLE

Using OSPF, only the Tuyến đường from R1 > R2 > R4 would be added to R1’s Tuyến đường TABLE because of the TOTAL COST of each link.

However, BOTH METRICS are trying to achieve the same thing :

To let the Router select the BEST Tuyến đường to the DESTINATION

---

Khoảng cách quản trị

- In MOST cases, a company will only use a single IGP - usually OSPF or EIGRP
- However, in some RARE cases, they might use TWO.
    - Ex: If TWO companies connect their networks to share information, TWO different Định tuyến PROTOCOLS might be in use.

- Metric is used to compare ROUTES learned via the same Định tuyến Giao thức

- Different Định tuyến PROTOCOLS use totally different METRICS, so they cannot be compared
    - An OSPF Tuyến đường to 192.168.4.0/24 might have a Metric of 30, while an EIGRP Tuyến đường to the same DESTINATION has a Metric of 33280. Which Tuyến đường is better? Which Tuyến đường should the Router put in the Tuyến đường TABLE ?

- The **Khoảng cách quản trị (AD)**, is used to determine which Định tuyến Giao thức is preferred.
    - A LOWER AD is preferred, and indicates that the Định tuyến Giao thức is considered more ‘trustworthy’ (more likely to select good ROUTES)

---

Khoảng cách quản trị NUMBERS

![image](https://github.com/psaumur/CCNA/assets/106411237/0f5ea405-d321-41bc-b2c0-2185874d07db)

(USE THE FLASHCARDS TO MEMORIZE THESE)

💡 IF the Khoảng cách quản trị is 255, the Router does not believe the SOURCE of that Tuyến đường and does not install the Tuyến đường in the Định tuyến TABLE!

![image](https://github.com/psaumur/CCNA/assets/106411237/33dbbe2b-7471-4c17-ae27-4d363d115a4c)

Metric is used to COMPARE ROUTES learned from the SAME Định tuyến Giao thức

However, before comparing METRICS, AD is used to select the BEST Tuyến đường

Therefore, the BEST Tuyến đường is :

“next hop 192.168.3.1, learned via OSPF (lower AD than RIP), Metric 10”

- You can CHANGE the AD of a Định tuyến Giao thức (This will be demonstrated in the lecture for OSPF Configuration)
- You can also change the AD of a STATIC Tuyến đường:

![image](https://github.com/psaumur/CCNA/assets/106411237/ec167f95-e5d7-49c8-aff7-1957e51934b1)

![image](https://github.com/psaumur/CCNA/assets/106411237/db6bef3b-ed82-49f0-b094-804c82f67f8d)

WHY WOULD YOU WANT TO DO THIS?

FLOATING STATIC ROUTES

- By CHANGING the AD of a STATIC Tuyến đường, you can make it less preferred than ROUTES learned by a DYNAMIC Định tuyến Giao thức to the same DESTINATION (make sure the AD is HIGHER than the Định tuyến Giao thức’s AD!)
- This kind of Tuyến đường is called a ‘FLOATING STATIC Tuyến đường’
- The Tuyến đường will be inactive (not in the Định tuyến TABLE) unless the Tuyến đường learned by the DYNAMIC Định tuyến Giao thức is removed.
    - **Ex:** The remote Router stops ADVERTISING it for some reason, or an Interface failure causes an ADJACENCY with a NEIGHBOR to be lost.

---

LINK STATE Định tuyến PROTOCOLS

- When using a LINK STATE Định tuyến Giao thức, every Router creates a ‘connectivity map’ of the Network
- To allow this, each Router ADVERTISES information about its INTERFACES (connected NETWORKS) to its NEIGHBOURS. These ADVERTISEMENTS are passed along to the other ROUTERS, until all ROUTERS in the Network develop the same map of the Network
- Each Router independently uses this MAP to calculate the BEST ROUTES to each DESTINATION
- LINK STATE PROTOCOLS use more resources (CPU) on the Router, because MORE information is shared.
- However, LINK STATE PROTOCOLS tend to be FASTER in reacting to CHANGES in the Network than DISTANCES VECTOR PROTOCOLS
