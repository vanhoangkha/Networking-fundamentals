# 36. CDP AND LLDP (LAYER 2 DISCOVERY GIAO THỨC)

INTRO TO LAYER 2 DISCOVERY PROTOCOLS

- LAYER 2 DISCOVERY Giao thức, such as CDP and LLDP share information WITH and DISCOVER information about NEIGHBORING (Connected) DEVICES

- The SHARED INFORMATION includes:
    - Hostname
    - Địa chỉ IP
    - Device Type
    - etcetera.

- **CDP** is a Cisco Proprietary Giao thức
- **LLDP** is an Industry Standard Giao thức (IEEE 802.1AB)

- Because they SHARE INFORMATION about the DEVICES in the Network, they can be considered a Security risk and are often NOT used. It is up to the Network ENGINEER / ADMIN to decide if they want to use them in the Network or not.

![image](https://github.com/psaumur/CCNA/assets/106411237/65f39e9f-ae1a-42c6-8afb-5e79f939fe5d)

---

CISCO DISCOVERY Giao thức (CDP)

- CDP is a Cisco proprietary Giao thức
- It is enabled on Cisco devices (routers, switches, firewalls, IP Phones, etc) by Default

<aside>
💡 CDP Messages are periodically sent to Multicast Địa chỉ MAC `0100.0CCC.CCCC`

</aside>


- When a DEVICE receives a CDP message, it PROCESSES and DISCARDS the message. It does NOT forward it to other devices.
- By Default, CDP Messages are sent once every **60 seconds**
- By Default, the CDP hold-time is **180 seconds.** If a message isn’t received from a neighbor for 180 seconds, the neighbor is REMOVED from the CDP Neighbor Table
- CDPv2 messages are sent by Default

![image](https://github.com/psaumur/CCNA/assets/106411237/8a0552be-dbc7-4c7b-b011-e32dff75a57e)

![image](https://github.com/psaumur/CCNA/assets/106411237/26e180ec-da08-44d2-bb55-325fdc0c234f)

---

CDP NEIGHBOR TABLES

![image](https://github.com/psaumur/CCNA/assets/106411237/00cd814e-0255-4fac-ac71-3e50054f813c)

“Device ID” = What devices were DISCOVERED by CDP

“Local Intrface” = What LOCAL device Interface the neighbors are connected to

“Holdtime” = Hold-time countdown in seconds (0 = device removed from table)

“Capabilities” = Refers to Capability Codes table (located above output)

“Platform” = Displays the MODEL of the Neighbor Device

“Port ID” = Neighbor ports that LOCAL device is connected to

---

MORE DETAILED OUTPUT

![image](https://github.com/psaumur/CCNA/assets/106411237/cd4fbedb-c12f-4e1e-8582-8db16985121f)

“Version” = shows what version of Cisco’s IOS is running on the device

---

SHOW SPECIFIC CDP NEIGHBOR ENTRY

![image](https://github.com/psaumur/CCNA/assets/106411237/83ef9488-e82c-4453-ae6e-02575039d0f9)

---

CDP Configuration COMMANDS

![image](https://github.com/psaumur/CCNA/assets/106411237/393b2680-2304-4c8e-9180-88cc5fefbfd8)

- CDP is GLOBALLY ENABLED, by Default
- CDP is also ENABLED on each Interface, by Default
- To Kích hoạt / Vô hiệu hóa CDP globally: `R1(config)# [no] cdp run`
- To Kích hoạt / Vô hiệu hóa CDP on specific interfaces : `R1(config-if)# [no] cdp enable`
- Configure the CDP timer: `R1(config)# cdp time *seconds*`
- Configure the CDP holdtime: `R1(config)# cdp holdtime *seconds*`
- Kích hoạt / Vô hiệu hóa CDPv2: `R1(config)# [no] cdp advertise-v2`

 

---

LINK LAYER DISCOVERY Giao thức (LLDP)

- LLDP is an INDUSTRY STANDARD Giao thức (IEEE 802.1AB)
- It is usually DISABLED on Cisco devices, by Default, so it must be manually ENABLED
- A device can run CDP and LLDP at the same time

<aside>
💡 LLDP Messages are periodically sent to Multicast Địa chỉ MAC `0180.c200.000E`

</aside>

- When a DEVICE receives an LLDP message, it PROCESSES and DISCARDS the message. It does NOT forward it to OTHER DEVICES
- By Default, LLDP Messages are sent once every **30 seconds**
- By Default, LLDP Holdtime is **120 seconds**
- LLDP has an additional timer called the ‘reinitialization delay’
    - If LLDP is ENABLED (Globally or on an Interface), this TIMER will DELAY the actual initialization of LLDP (**2 seconds,** by Default)

---

LLDP Configuration COMMANDS

- LLDP is usually GLOBALLY DISABLED by Default
- LLDP is also DISABLED on each Interface, by Default

- To Kích hoạt LLDP GLOBALLY : `R1(config)# lldp run`

- To Kích hoạt LLDP on specific INTERFACES (tx): `R1(config-if)# lldp transmit`
- To Kích hoạt LLDP on specific INTERFACES (rx): `R1(config-if)# lldp receive`

YOU NEED TO Kích hoạt BOTH TO SEND AND RECEIVE (Unless you want to only Kích hoạt SEND or RECEIVE LLDP Messages)

 

- Configure the LLDP timer: `R1(config)# lldp timer *seconds*`
- Configure the LLDP holdtime: `R1(config)# lldp holdtime *seconds*`
- Configure the LLDP reinit timer: `R1(config)# lldp reinit *seconds*`

![image](https://github.com/psaumur/CCNA/assets/106411237/25afc5ad-4d82-4472-b282-31ed2a65eae7)

![image](https://github.com/psaumur/CCNA/assets/106411237/78fab926-9fda-4c83-91eb-eda4bf4ec005)

SHOW LLDP STATUS

![image](https://github.com/psaumur/CCNA/assets/106411237/32b11d7b-4050-422e-afd4-bec23e8db3a1)

SHOW ALL LLDP NEIGHBORS

![image](https://github.com/psaumur/CCNA/assets/106411237/85a46d24-5574-4400-bc03-6b0568294940)

SHOW LLDP NEIGHBORS in DETAIL

![image](https://github.com/psaumur/CCNA/assets/106411237/26751ca8-ed54-4e5c-9927-8c6eb0e2e3f7)

SHOW SPECIFIC LLDP DEVICE ENTRY

![image](https://github.com/psaumur/CCNA/assets/106411237/b5332838-d112-4556-bee0-c3716a3d4f89)

![image](https://github.com/psaumur/CCNA/assets/106411237/2dd16e33-75a9-4e11-91aa-b507ed490e9b)
