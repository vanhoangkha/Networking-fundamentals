# 59. INTRODUCTION TO Mạng Tự động hóa

WHY Mạng Tự động hóa

- Previous versions of the CCNA focused on the traditional model of managing / controlling networks
- The current version focuses on the traditional model as well, but CCNA candidates are expected to have a basic understanding of various topics related to Mạng Tự động hóa
- In the traditional model, engineers manage devices one at a time by connecting to their CLI via SSH

---

DOWNSIDES OF CONFIGURING DEVICES ONE-BY-ONE

- Typos and other small mistakes are common
- It is time-consuming and very inefficient in large-scale networks
- It is difficult to ensure that all devices ADHERE to the organization’s STANDARD Cấu hình

---

BENEFITS OF Mạng Tự động hóa

- Human Error (Typos, etc) is reduced
- Networks become much more scalable and implemented in a fraction of the time
    - New deployments
    - Mạng-wide changes
    - Khắc phục sự cố
- Mạng-wide policy compliance can be assured
    - Standard configurations
    - Software versioning

- The improved efficiency of Mạng operations reduces the OP-EX (operating expenses) of the Mạng. Each task requires fewer MAN-hours

```
There are various tools / methods that can be used to automate tasks in the network

- SDN (Software-Defined Networking)
- Ansible
- Puppet
- Python scripts
- etc…
```

---

LOGICAL “PLANES” OF Mạng FUNCTIONS

**What does a Router do?**

- It forwards messages between networks by examining information in the Layer 3 Header
- It uses a Định tuyến Giao thức like OSPF to share Tuyến đường information with other routers and build a Định tuyến table
- It uses ARP to build an ARP table, mapping IP Addresses to MAC Addresses
- It uses Syslog to keep logs of events that occur
- and MUCH more…

**What does a Switch do?**

- It forwards messages within a LAN by examining information in the Layer 2 Header
- It uses STP to ensure there are no Layer 2 loops in the Mạng
- It builds a Địa chỉ MAC table by examining the Source Địa chỉ MAC of frames
- It uses Syslog to keep logs of events that occur
- It allows a user to connect to it via SSH and manage it

---

The various functions of Mạng devices can be logically divided up (categorized) into *PLANES*

```
- DATA PLANE
- CONTROL PLANE
- MANAGEMENT PLANE
```


- The operations of the Quản lý PLANE and the CONTROL PLANE are usually managed by the CPU
- However, this is not desirable for DATA PLANE operations because CPU processing is slow (relatively speaking)
- Instead, a specialized hardware ASIC (Application-Specific Integrated Circuit) is used.
    - ASICs are chips built for a specific purpose
- Using a Switch, as an example:
    - When a Khung is received, the ASIC (not the CPU) is responsible for the switching logic
    - The Địa chỉ MAC table is stored in a kind of memory called TCAM (Ternary Content-Addressable Memory)
        - Another common name for the Địa chỉ MAC table is CAM TABLE
    - The ASIC feeds the DESTINATION Địa chỉ MAC of the Khung into the TCAM which returns the matching Địa chỉ MAC table entry
    - The Khung is then forwarded out of the appropriate DEVICE
- Modern ROUTERS also use a similar hardware DATA PLANE: An ASIC designed for forwarding logic, and tables store in TCAM

---

A SIMPLE SUMMARY:

>- When a DEVICE receives CONTROL / Quản lý traffic (destined for itself), it will be processed in the CPU
>- When a DEVICE receives DATA traffic which should pass through the DEVICE, it is processed by the ASIC for maximum speed

---

DATA PLANE

- All tasks involved in forwarding USER  DATA / TRAFFIC from one Giao diện to another are part of the DATA PLANE
- A Router receives a message, looks for the most specific matching Router in its Định tuyến TABLE, and forwards it out of the appropriate Giao diện to the next hop
    - It also de-encapsulates the original LAYER 2 Header, and re-encapsulates with a new Header destined for the next hop’s Địa chỉ MAC
- A Switch receives a message, looks at the DESTINATION Địa chỉ MAC, and forwards it out of the appropriate Giao diện (or FLOODS it)
    - This includes functions like adding / removing 802.1q VLAN tags
- NAT (changing the SRC / DST addresses before forwarding) is part of the DATA PLANE
- Deciding to forward / discard messages due to ACL’s, Cổng-Bảo mật, etc. is part of the DATA PLANE
- The DATA PLANE is also called the ‘FORWARDING PLANE’

![image](https://github.com/psaumur/CCNA/assets/106411237/6a72186b-2956-45f6-8643-801caa2cb28e)

---

CONTROL PLANE

- How does a DEVICE’s DATA PLANE make its forwarding decisions?
    - Định tuyến TABLE
    - Địa chỉ MAC table
    - ARP table
    - STP
    - etc…
    
- Functions that build THESE tables (and other functions that influence the DATA PLANE) are part of the CONTROL PLANE

- The CONTROL PLANE *controls* what the DATA PLANE does, Ví dụ by building the Router’s Định tuyến TABLE

- The CONTROL PLANE performs *overhead* work
    - OSPF itself doesn’t forward user data packets, but it informs the DATA PLANE about HOW packets should be forwarded
    - STP itself isn’t directly involved in the process of forwarding FRAMES, but it informs the DATA PLANE about which INTERFACES should and shouldn’t be used to forward FRAMES
    - ARP messages aren’t user data but they are used to build an ARP TABLE which is used in the process of forwarding data

![image](https://github.com/psaumur/CCNA/assets/106411237/4c21b082-5d6e-4388-94c5-bebf33b50c8d)

---

Quản lý PLANE

- Like the CONTROL PLANE, the Quản lý PLANE performs overhead work
    - However, the Quản lý PLANE doesn’t directly affect the forwarding of messages in the DATA PLANE
- The MANAGMENT PLANE consists of PROTOCOLS that are used to manage devices
    - SSH / Telnet : Used to connect to the CLI of a DEVICE to configure / manage it
    - SYSLOG : Used to keep logs of events that occur on the device
    - SNMP : Used to monitor the operations of the device
    - NTP : Used to maintain accurate time on the device

![image](https://github.com/psaumur/CCNA/assets/106411237/3cfffa40-f4cb-4042-8778-139605c2eb26)

---

SOFTWARE-DEFINED NETWORKING (SDN)

- SOFTWARE-DEFINED NETWORKING (SDN) is an approach to networking that centralizes the CONTROL PLANE into an application called a *CONTROLLER*
- SDN is also called SOFTWARE-DEFINED-Kiến trúc (SDA) or CONTROLLER-BASED NETWORKING
- Traditional CONTROL PLANES use a distributed Kiến trúc
    - Ví dụ:
        - Each Router in the Mạng runs OSPF and the ROUTERS share Định tuyến information and then calculate their preferred routes to each destination
- An SDN CONTROLLER centralized CONTROL PLANE functions like calculation routes
    - That is just an example and how much of the CONTROL PLANE is centralized varies greatly
- The CONTROLLER can interact programmatically with the Mạng DEVICE using APIs (Application Programming Giao diện)

![image](https://github.com/psaumur/CCNA/assets/106411237/05c4c5d9-5ba4-480c-9c13-72fa1f7937db)

---

SOUTHBOUND Giao diện (SBI)

- The SBI is used for communications between the CONTROLLER and the Mạng DEVICES it controls
- It typically consists of a COMMUNICATION Giao thức and API (Application Programming Giao diện)

- APIs facilitate data exchanges between programs
    - DATA is exchanged between the CONTROLLER and the Mạng DEVICES
    - An API on the Mạng DEVICES allows the CONTROLLER to Access information on the DEVICES, control their DATA PLANE TABLES, etc.
- Some examples of SBIs :
    - OpenFlow
    - Cisco OpFlex
    - Cisco OnePK (Open Mạng Environment Platform Kit)
    - NETCONF

---

 NORTHBOUND Giao diện (NBI)

- Using the SBI, the CONTROLLER communicates with the managed DEVICES and gathers information about them:
    - The DEVICES in the Mạng
    - The Cấu trúc mạng (how the DEVICES are connected together)
    - The available INTERFACES on each DEVICE
    - Their CONFIGURATIONS
- The NORTHBOUND Giao diện (NBI) is what allows us to:
    - Interact with the CONTROLLER
    - Access the DATA it gathers about the Mạng
    - Program the Mạng
    - Make changes to the Mạng via the SBI

- A REST API (Representational State Transfer) is used on the controller as an Giao diện for APPS to interact with it
- OSGi (Java Open Services Gateway Initiative) - Java based NBI API

- DATA is sent in a structured (*serialized*) format such as JSON or XML
    - This makes it easier for programs to use the DATA

![image](https://github.com/psaumur/CCNA/assets/106411237/d980626f-f731-46a4-ba14-72c3d21f2fd3)

---

Tự động hóa IN TRADITIONAL NETWORKS VS SDN

- Networking tasks can be automated in traditional Mạng architectures too:
    - SCRIPTS can be written (ie: using Python) to push commands to many DEVICES at once
    - Python with good use of REGULAR EXPRESSIONS can parse through “show” commands to gather information about Mạng devices
    
- However, the robust and centralized DATA collected by SDN CONTROLLERS greatly facilitates these functions
    - The CONTROLLER collects information about all DEVICES in the Mạng
    - NORTHBOUND APIs allow APPS to Access information in a format that is easy for programs to understand (ie: JSON and XML)
    - The centralized DATA facilitates Mạng-wide analytics
- SDN Tools can provide the benefits of Tự động hóa without the requirement of third-party scripts and apps.
    - You don’t need expertise in Tự động hóa to make use of SDN Tools
    - However, APIs allow third-party applications to interact with the CONTROLLER, which can be very powerful


>💡 Although SDN and Tự động hóa aren’t the same thing, the SDN Kiến trúc greatly facilitates the Tự động hóa of various tasks in the Mạng via the SDN CONTROLLER and APIs
