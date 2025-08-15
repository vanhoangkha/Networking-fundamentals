# 22. RAPID Spanning Tree Giao thức

*COMPARISON OF STP VERSIONS (Standard vs. Cisco)*

![image](https://github.com/psaumur/CCNA/assets/106411237/ca5ff85c-842e-4ed3-9b6a-f9d6ed546a78)


We are only concerned with 802.1w for MOST use cases.

MSTP (802.1s) is more useful for VERY LARGE networks.

là gì RAPID PER-VLAN Spanning Tree PLUS?

> RSTP is not a time-based Spanning Tree algorithm like 802.1D. Therefore, RSTP offers an improvment over teh 30 seconds or more 802.1D takes to move a link to forwarding. The heart of the Giao thức is a new Bridge-Bridge handshake mechanism, which allows ports to move directly to forwarding

---

SIMILARITIES BETWEEN STP AND RSTP:

- RSTP serves the same purpose as STP, blocking specific PORTS to prevent LAYER 2 LOOPS.
- RSTP elects a Bridge gốc with the same rules as STP
- RSTP elects ROOT PORTS with the same rules as STP
- RSTP elects DESIGNATED PORTS with the same rules as STP

---

DIFFERENCES BETWEEN STP AND RSTP:

**Cổng COSTS**

![image](https://github.com/psaumur/CCNA/assets/106411237/b250c6da-2579-4576-8e93-5a8f8e66d873)


(STUDY AND MEMORIZE Cổng COSTS OF STP AND RSTP)

RSTP Cổng STATES

![image](https://github.com/psaumur/CCNA/assets/106411237/054d5037-a60e-478e-986b-6f43825a0d1a)

- If a Cổng has been ADMINISTRATIVELY DISABLED (”shutdown” Lệnh) = DISCARDING STATE
- If a Cổng is ENABLED but BLOCKING traffic to prevent LAYER 2 LOOPS = DISCARDING STATE

---

RSTP ROLES

- The ROOT Cổng role remains unchanged in RSTP
    - The Cổng that is closest to the Bridge gốc becomes the ROOT Cổng for the Switch
    - The Bridge gốc is the only Switch that doesn’t have a ROOT Cổng
- The DESIGNATED Cổng role remains unchanged in RSTP
    - The Cổng on a Đoạn (Collision Domain) that sends the best BPDU is that Đoạn’s DESIGNATED Cổng (only one per Đoạn!)
- The NON-DESIGNATED Cổng role is split into TWO separate roles in RSTP:
    - The ALTERNATE Cổng role
    - The BACKUP Cổng role

**RSTP : ALTERNATE Cổng ROLE**

- The RSTP ALTERNATE Cổng ROLE is a DISCARDING Cổng that receives a superior BPDU from another Switch
- This is the same as what you’ve learned about BLOCKING PORTS in classic STP

![image](https://github.com/psaumur/CCNA/assets/106411237/7d81e70c-3b31-4448-9d45-9aadb738c74d)

- An ALTERNATE Cổng (labelled “A” above) functions as a backup to the ROOT Cổng
- If the ROOT Cổng fails, the Switch can immediately move it’s best alternate Cổng to FORWARDING

![image](https://github.com/psaumur/CCNA/assets/106411237/41f3be85-6225-4749-83b4-f76952c5756a)

💡 This immediate move to FORWARDING STATE functions like a classic STP optional feature called **UplinkFast.** Because it is built into RSTP, you do not need to activate UplinkFast when using RSTP/Rapid PVST+

One more STP optional feature that was built into RSTP is **BackboneFast**

![image](https://github.com/psaumur/CCNA/assets/106411237/c4cea7b7-599f-4ec8-b9d3-a5acba71a5f5)

- **BackboneFast** allows SW3 to expire the MAX AGE TIMERS on it’s Giao diện and rapidly FORWARD the superior BPDUs to SW2
- This FUNCTIONALITY is built into RSTP, so it does not need to be configured.

UPLINKFAST and BACKBONE FAST (SUMMARY)

💡 **UplinkFast** and **BackboneFast** are two optional features in Classic STP. They must be configured to operate on the Switch (not necessary to know for the CCNA)

- Both features are built into RSTP, so you do NOT have to configure them. They operate, by Mặc định
- You do NOT need to have a detailed understanding of them for the CCNA. Know their names and their BASIC purpose (to help BLOCKING / DISCARDING PORTS rapidly move to FORWARDING)

---

**RSTP : BACKUP Cổng ROLE**

- The RSTP BACKUP Cổng role is a DISCARDING Cổng that receives a superior BPDU from another Giao diện on the same Switch
- This only happens when TWO INTERFACES are connected to the SAME COLLISION DOMAIN (via a Hub)
- Hubs are NOT used in modern networks, so you will probably NOT encounter an RSTP BACKUP Cổng
- Hubs are NOT used in modern networks, so you will probably NOT encounter an RSTP BACKUP Cổng.
- Functions as a BACKUP for a DESIGNATED Cổng

💡 The Giao diện with the LOWERS Cổng ID will be selected as the DESIGNATED Cổng, and the other will be the BACKUP Cổng.

![image](https://github.com/psaumur/CCNA/assets/106411237/61aefc04-b3a9-484a-bbfa-1efe792c73c7)

WHICH Switch will be Bridge gốc?
What about the OTHER ports ?

![image](https://github.com/psaumur/CCNA/assets/106411237/be4d404d-829d-41ab-ba39-34e918ed7ea9)

![image](https://github.com/psaumur/CCNA/assets/106411237/b5dec396-d5fc-486b-9110-5dcc2c4dc4aa)

![image](https://github.com/psaumur/CCNA/assets/106411237/1930a17b-6c74-4756-b89d-4148008f586b)

💡 RAPID STP *is* compatible with CLASSIC STP.
💡 The Giao diện(S) on the RAPID STP-enabled Switch connected to the CLASSIC STP-enabled Switch will operate in CLASSIC STP MODE (Timers, BLOCKING >>> LISTENING >>> LEARNING >>> FORWARDING, etc.)

---

RAPID STP BPDU

CLASSIC RSTP (LEFT) vs RAPID STP BPDU (RIGHT)

![image](https://github.com/psaumur/CCNA/assets/106411237/2d2deb45-3f81-4c60-b9fa-0f6c3fe7c060)


💡 NOTE:

Classic STP BPDU has a “Giao thức Version Identifier: Spanning Tree (0)

BPDU Type: Cấu hình (0x00)

BPDU flags: 0x00

RAPID STP BPDU has a “Giao thức Version Identifier: Spanning Tree (2)

BPDU Type: Cấu hình (0x02)

BPDU flags: 0x3c


In CLASSIC STP, only the Bridge gốc originated BPDUs, and other SWITCHES just FORWARDED the BPDUs they received. 

In RAPID STP, ALL SWITCHES originate and send their own BPDUs from their DESIGNATED PORTS

---

RAPID Spanning Tree Giao thức

- ALL SWITCHES running RAPID STP send their own BPDUs every “hello” time (2 Seconds)
- SWITCHES “age” the BPDU information much more quickly
    - In CLASSIC STP, a Switch waits 10 “hello” intervals (20 seconds)
    - In RAPID STP, a Switch considers a neighbour lost if it misses 3 BPDUs (6 seconds). It will then “flush” ALL MAC ADDRESSES learned on that Giao diện

![image](https://github.com/psaumur/CCNA/assets/106411237/c03d2645-42d8-4d95-b486-999e82ac12a8)

---

RSTP LINK TYPES

![image](https://github.com/psaumur/CCNA/assets/106411237/e837a271-ad13-4d6a-a800-434a0eff2576)

```
<E> = EDGE

<P> = POINT-TO-POINT

<S> = SHARED
```

RSTP distinguishes between THREE different “link types” : **EDGE**, **POINT-TO-POINT**, and **SHARED**

EDGE PORTS

- Connected to END HOSTS
- Because there is NO RISK of creating a LOOP, they can move straight to the FORWARDING STATE without the negotiation process!
- They function like a CLASSIC STP Cổng with PORTFAST ENABLED

💡 SW1(config-if)# spanning-tree portfast

---

POINT-TO-POINT PORTS

- Connect directly to another Switch
- They function in FULL-DUPLEX
- You don’t need to configure the Giao diện as POINT-TO-POINT (it should be detected)

💡 SW1(config-if)# spanning-tree link-type point-to-point

---

SHARED PORTS

- Connect to another Switch (or SWITCHES) via a Hub
- They function in HALF-DUPLEX
- You don’t need to configure the Giao diện as SHARED (it should be detected)

💡 SW1(config-if)# spanning-tree link-type shared

---

QUIZ:

![image](https://github.com/psaumur/CCNA/assets/106411237/a7314f6f-55f0-4e62-bd24-b311b090afe8)

SW1 :

- **Bridge gốc**
- G0/0 - 0/3= DESIGNATED

SW2 : 

- G0/0 = ROOT Cổng
- G0/1 = DESIGNATED Cổng
- G0/2 = BACKUP Cổng
- G0/3 = DESIGNATED Cổng

SW3 :

- G0/0 = DESIGNATED Cổng
- G0/1 = ALTERNATE Cổng
- G0/2 = ROOT Cổng
- G0/3 = DESIGNATED Cổng

SW4:

- G0/0 = ROOT
- G0/1 = ALTERNATE Cổng
- G0/2 = DESIGNATED Cổng

Connection between SW1 G0/0 and SW2 G0/0 = POINT-TO-POINT

Connection between SW3 G0/0 and SW4 G0/0 = POINT-TO-POINT

Connection between SW1 G0/1 and G0/2 to SW3 G0/1 and G0/2 = POINT-TO-POINT

Connections to all the END HOSTS = EDGE 

Connection from SW4 to Hub = SHARED

Connections from SW2 to Hub = SHARED

ANSWER

![image](https://github.com/psaumur/CCNA/assets/106411237/b76eb7be-897a-4617-990e-f399ceaea5f2)
