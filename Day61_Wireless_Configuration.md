# 58. KHÔNG DÂY CONFIGURATION

Cấu trúc mạng INTRODUCTION

![image](https://github.com/psaumur/CCNA/assets/106411237/1e8ed6b8-1183-42e7-9584-d5504c52987a)

INTERNAL PC (VLAN 100) ACCESSING Default Gateway via Internal CAPWAP tunnel

![image](https://github.com/psaumur/CCNA/assets/106411237/4dec4c60-945e-4f2c-b7db-3028269ec441)

REACHING External GUEST PC  via Default Gateway + Internal and External CAPWAP tunnels

![image](https://github.com/psaumur/CCNA/assets/106411237/3b1c79a6-f8c5-496b-a0b8-d561ff87880f)

---

LAYER 3 Switch Configuration (SW1)

![image](https://github.com/psaumur/CCNA/assets/106411237/eae43f12-aa95-41a3-8a5d-26ffc5e83262)

PART 2 of Configuration

Note DHCP “Option 43”

![image](https://github.com/psaumur/CCNA/assets/106411237/ade4dc29-3017-4d79-99d2-d895968bf741)

WLC SETUP

This helps set up the WLC to allow GUI Configuration

![image](https://github.com/psaumur/CCNA/assets/106411237/3a2c00c0-eda3-4b72-af07-b07e820365c5)

![image](https://github.com/psaumur/CCNA/assets/106411237/313e030b-add3-4384-bdf0-96306e3663b1)

Why Jeremy chose FRANCE for Country Code (has to do with regulatory domain of equipment)

![image](https://github.com/psaumur/CCNA/assets/106411237/c3a21043-c4fc-47fb-9294-953700fbd8ed)

![image](https://github.com/psaumur/CCNA/assets/106411237/80dce78b-3a7e-4c93-a5f1-47eefb6e28b0)

---

ACCESSING THE WLC GUI

![image](https://github.com/psaumur/CCNA/assets/106411237/a5b44611-af07-4bf6-94b3-957ee342bb24)

![image](https://github.com/psaumur/CCNA/assets/106411237/7924d814-35f2-40d0-ac3c-a2f8022df2bc)

![image](https://github.com/psaumur/CCNA/assets/106411237/45432356-9b45-43dd-99c7-701984d541c1)

![image](https://github.com/psaumur/CCNA/assets/106411237/f097e29c-c7f6-4045-9451-9fdd5035b4b4)

![image](https://github.com/psaumur/CCNA/assets/106411237/b6ec70b7-d628-422b-b693-d9f0af9d1e78)

---

WLC Configuration

![image](https://github.com/psaumur/CCNA/assets/106411237/fbc3b9fd-c0db-48f3-9ce8-270812e00008)

WLC PORTS

- WLC PORTS are the PHYSICAL PORTS that cables connect to
- WLC INTERFACES are the logical interfaces within the WLC (ie: SVIs on a Switch)
- WLCs have a few different PORTS:
    - SERVICE Port
        - A dedicated Management Port
        - Used for OUT-OF-BAND Management
        - Must connected to a Switch Access Port because it only supports one VLAN
        - This Port can be used to connect to the DEVICE while it is booting, performing system recovery, etc.
    - DISTRIBUTION SYSTEM Port
        - These are the standard Network PORTS that connect to the “DISTRIBUTION SYSTEM” (WIRED Network) and are used for DATA traffic.
        - These PORTS usually connect to Switch Trunk PORTS, and if multiple distribution PORTS are used they can form a LAG
    - CONSOLE Port
        - This is a standard CONSOLE Port, either RJ45 or USB
    - REDUNDANCY Port
        - This Port is used to connect to another WLC to form a HIGH AVAILABILITY (HA) pair

![image](https://github.com/psaumur/CCNA/assets/106411237/cec94d93-d58b-43b1-8e5e-f4c07ee430fd)

---

WLC INTERFACES

- Management INTERFACES
    - Used for Management traffic such as Telnet, SSH, HTTP, HTTPS, RADIUS authentication, NTP, SYSLOG, etc.
    - CAPWAP TUNNELS are also formed to / from the WLC’s Management Interface
- REDUNDANCY Management Interface
    - When TWO WLCs are connected by their REDUNDANCY PORTS, one WLC is “ACTIVE” and the other is “STANDBY”
    - This Interface can be used to connect to and manage the “STANDBY” WLC

- VIRTUAL Interface
    - This Interface is used when communicating with Không dây CLIENTS to relay DHCP requests, perform CLIENT WEB AUTHENTICATION, etc.

- SERVICE Port Interface
    - If the SERVICE Port is used, this Interface is bound to it and used for OUT-OF-BAND Management

- DYNAMIC Interface
    - These are the INTERFACES used to map a WLAN to a VLAN
    - Ví dụ :
        - TRAFFIC from the “INTERNAL” WLAN will be sent to the WIRED Network from the WLCs “INTERNAL” DYNAMIC Interface

---

WLAN Configuration

Click “NEW”

![image](https://github.com/psaumur/CCNA/assets/106411237/b20dbb39-fac6-4cf3-926b-869e75c04e15)

Fill in details of the Interface and click “APPLY”

![image](https://github.com/psaumur/CCNA/assets/106411237/48a4810d-a56c-4aef-8cfd-d2474d42cbb1)

Fill out details (IP, Netmask, Gateway…) and then click “APPLY”

![image](https://github.com/psaumur/CCNA/assets/106411237/6d11036b-3d82-4c2f-a20a-4367eb18ca8a)

INTERNAL Interface has now been created

![image](https://github.com/psaumur/CCNA/assets/106411237/80a91b22-c4fa-43e2-b035-05ac6199c6f3)

Now, repeat the above steps for the GUEST Interface

![image](https://github.com/psaumur/CCNA/assets/106411237/80d5a300-a3ef-4e46-ae1a-7b7afb6a5078)

Fill out details (IP, Netmask, Gateway…) and then click “APPLY”

![image](https://github.com/psaumur/CCNA/assets/106411237/43f70936-4b10-4647-8f57-a086e3f0b7bc)

![image](https://github.com/psaumur/CCNA/assets/106411237/3a98ae1c-13a4-4bde-ab8c-398f8d16da43)

Now that all the INTERFACES are created, we can start WLAN Configuration

![image](https://github.com/psaumur/CCNA/assets/106411237/d80eff95-41c7-43c6-a31e-0ebde3a7cd81)

![image](https://github.com/psaumur/CCNA/assets/106411237/960f24e5-efb9-4a15-9f5f-2a8e45b2d425)

INTERNAL WLAN is set to “Management”, it needs to be changed to “INTERNAL”

![image](https://github.com/psaumur/CCNA/assets/106411237/a3cb544c-3ce4-43b5-b054-e52e8388ab83)

Security will also need to be changed from [WPA2] to [WPA2 PSK]

![image](https://github.com/psaumur/CCNA/assets/106411237/4cb2783e-26db-4584-8daa-feba124e9966)

(Need to CHECK the PSK “Kích hoạt” box at the bottom)

Change the PSK FORMAT to “ASCII” and enter a PASSWORD (at least 8 chars in length)

![image](https://github.com/psaumur/CCNA/assets/106411237/220202e1-222f-4966-81a6-aafa81727c33)

![image](https://github.com/psaumur/CCNA/assets/106411237/8cd2c63a-aa10-48c3-b826-fe107d04666d)

- WEB AUTHENTICATION
    - After the Không dây CLIENTS gets an Địa chỉ IP and tries to Access a WEB PAGE, they will have to enter a USERNAME and PASSWORD to AUTHENTICATE

- WEB PASSTHROUGH
    - Similar to the above, but NO USERNAME or PASSWORD are required
    - A warning or statement is displayed and the CLIENT simply has to agree to gain Access to the Internet
    
- CONDITIONAL and SPLASH PAGE web redirect options are similar but additionally require 802.1x LAYER 2 AUTHENTICATION

---

QoS

![image](https://github.com/psaumur/CCNA/assets/106411237/957336a3-d81c-4914-b35f-99925a316ad3)

Default QoS setting is “SILVER” (Best Effort). This can be changed depending on the class of traffic being sent through the WLAN

---

ADVANCED SETTINGS

![image](https://github.com/psaumur/CCNA/assets/106411237/ed70b1b9-b0b6-4b37-b4a5-4492a0cb9120)

![image](https://github.com/psaumur/CCNA/assets/106411237/12bcb065-78af-47b9-810c-fbe7ad739260)

---

CONFIGURING A NEW WLAN (GUEST)

![image](https://github.com/psaumur/CCNA/assets/106411237/4782e82e-4545-458e-917c-42d40e08748d)

Change STATUS to “ENABLED” and Interface GROUP to “GUEST”

![image](https://github.com/psaumur/CCNA/assets/106411237/7a84ce73-0250-404b-896c-695ac5b9d05a)

![image](https://github.com/psaumur/CCNA/assets/106411237/2ca8357b-7564-4ef9-8f36-cb730a4b415f)

Now, we need to change the Security POLICY to [WPA2][Auth(PSK)]

Returning to Giám sát, we can see the changes we made to the Configuration

![image](https://github.com/psaumur/CCNA/assets/106411237/5a06ae8b-cad0-46ec-bf34-adab0960fc41)

Current number of CLIENTS is now 0. By connecting to the WLANS, these numbers should change.
To SEE a list of the CLIENTS connected, click the left-hand side “CLIENTS” tab

![image](https://github.com/psaumur/CCNA/assets/106411237/b6eefbd8-f79e-4dc6-90e6-95a8c0c17849)

![image](https://github.com/psaumur/CCNA/assets/106411237/75d359fe-dc41-4d87-9351-e1da0ebbb8c7)

---

ADDTIONAL WLC FEATURES

Không dây tab showing a list of the APs currently in the Network

![image](https://github.com/psaumur/CCNA/assets/106411237/29f5608e-9edb-4c6e-9382-998deedd4c72)

Clicking on an AP shows information and Configuration settings for it

![image](https://github.com/psaumur/CCNA/assets/106411237/7d87bbcc-ed95-47b6-b966-fb95f5bb7f29)

---

Management tab allows you change the ways you can MANAGE the WLC

Clicking “Mgmt Via Không dây” allows you change if you can Access Management via WI-FI

![image](https://github.com/psaumur/CCNA/assets/106411237/605361a0-c8da-47fc-bca3-af09751838dd)

![image](https://github.com/psaumur/CCNA/assets/106411237/e13bdcea-cb87-4e38-9dd4-711079761987)

---

Security tab can allow us to create Access LISTS

![image](https://github.com/psaumur/CCNA/assets/106411237/7eddccfb-07cd-4ba9-914e-54161a4b10f3)

First, NAME the ACL and what kind of Địa chỉ IP it’s for

![image](https://github.com/psaumur/CCNA/assets/106411237/e9f303bc-9078-4ff2-be86-f63fb9877008)

CLICK “Add New Rule” to specify the ACL Rules (What traffic can pass)

![image](https://github.com/psaumur/CCNA/assets/106411237/4637053c-042d-4afc-acf8-27e914698c00)

![image](https://github.com/psaumur/CCNA/assets/106411237/c9d26aa3-c277-45ac-8f74-1dbd11e1bda5)

![image](https://github.com/psaumur/CCNA/assets/106411237/afbdb580-5383-4f32-9713-708f0a4ebb7e)

We now need to APPLY the ACL (just like applying it to an Interface on a Router)

Click “CPU ACL” from the left-hand menu

![image](https://github.com/psaumur/CCNA/assets/106411237/3eeee534-2071-47df-97f6-639e46d54b94)

Select the new ACL from the pull-down list and then click “APPLY”

![image](https://github.com/psaumur/CCNA/assets/106411237/7c18a89c-cad3-4f54-b6e5-6d5956edbd37)

![image](https://github.com/psaumur/CCNA/assets/106411237/6319e0ad-4c65-418d-920b-3c1f43ae4b55)
