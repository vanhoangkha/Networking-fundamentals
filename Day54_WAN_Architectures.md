# 53.  WAN ARCHITECTURES

INTRODUCTION TO WANS

- WAN stands for WIDE AREA Network
- A WAN is a Network that extends over a large geographic area
- WANs are used to connect geographically separate LANs
- Although the Internet can be considered a WAN, the term “WAN” is typically used to refer to an Doanh nghiệp’s private connections that connect their offices, data centers, and other sites together
- Over public/shared networks like the Internet, VPNs (Virtual Private Networks) can be used to create private WAN connections
- There have been many different WAN technologies over the years. Depending on the location, some will be available and some will not be
- Technologies which are considered “legacy” (old) in one country, might still be used in other countries

---

WAN OVER DEDICATED CONNECTION (LEASED LINE)

Hub-and-SPOKE Cấu trúc mạng

![image](https://github.com/psaumur/CCNA/assets/106411237/57575fad-883d-4999-a56d-a77fa1542976)

![image](https://github.com/psaumur/CCNA/assets/106411237/cfc23064-a133-445a-b854-e044828eca7d)

WAN CONNECTION VIA Ethernet (FIBER)

![image](https://github.com/psaumur/CCNA/assets/106411237/022ccdbd-7ce9-41fd-9f99-9e9c6dcb9f76)

WAN OVER SHARED Hạ tầng (Internet VPN)

![image](https://github.com/psaumur/CCNA/assets/106411237/38eff264-7ed4-43fd-943b-47e9e1ce995e)

---

LEASED LINES

- A LEASED LINE is a dedicated physical link, typically connecting two sites
- LEASED LINES use serial connections (PPP or HDLC Đóng gói)
- There are various standards that provide different speeds and different standards are available in different countries.
- Due to the HIGHER cost, HIGHER installation lead time, and SLOWER speeds of LEASED LINES, Ethernet WAN technologies are becoming MORE popular

![image](https://github.com/psaumur/CCNA/assets/106411237/77dd5503-8b29-4919-8747-6dd80eec28fa)

MPLS VPNs

- MPLS stands for “Multi Giao thức Label Switching”
- Similar to the Internet, service providers’ MPLS NETWORKS are shared Hạ tầng because many customer enterprises connect to and share the same Hạ tầng to make WAN connections
- However, the “label switching” in the name of MPLS allows VPNs to be created over the MPLS Hạ tầng through the use of LABELS
- IMPORTANT terms:
    - CE Router = Customer Edge Router
    - PE Router = Provider Edge Router
    - P Router = Provider Core Router

![image](https://github.com/psaumur/CCNA/assets/106411237/166bff5b-d977-48dc-9a74-b9a523b91e1b)

- When the PE ROUTERS receive FRAMES from the CE ROUTERS, they add a LABEL to the Khung
- These LABELS are used to make forwarding decisions within the SERVICE PROVIDER Network - NOT the DESTINATION IP
- The CE ROUTERS do NOT USE MPLS, it is only used by the PE/P ROUTERS
- When using a LAYER 3 MPLS VPN, the CE and PE ROUTERS peer using OSPF, Ví dụ, to share Định tuyến information

EXAMPLE: 

OFFICE A’s CE will peer with one PE

OFFICE B’s CE will peer with the other PE

OFFICE A’s CE will learn about OFFICE B’s ROUTES via this OSPF peering

OFFICE B’s CE will learn about OFFICE A’s ROUTES as well

![image](https://github.com/psaumur/CCNA/assets/106411237/2b3d8d6e-3501-4d54-a6f8-5a05c9140d24)

- When using a LAYER 2 MPLS VPN, the CE and PE ROUTERS do NOT form PEERINGS
- The SERVICE PROVIDER Network is entirely *transparent* to the CE ROUTERS
- In effect, it is like the TWO CE ROUTERS are directly connected.
    - Their WAN INTERFACES will be in the SAME Network con
- If a Định tuyến Giao thức is used, the TWO CE ROUTERS will peer directly with each other

CE ROUTERS connected via LAYER 2 MPLS VPN

![image](https://github.com/psaumur/CCNA/assets/106411237/b0b19dfd-e417-40ce-ac36-ce0ace8484cc)

![image](https://github.com/psaumur/CCNA/assets/106411237/cc5c9508-a2b0-4fe7-9c83-6c03e7d2d861)

---

MPLS 

- Many different technologies can be used to connect to a SERVICE PROVIDER’s MPLS Network for WAN Service

![image](https://github.com/psaumur/CCNA/assets/106411237/c6e6e60d-2a96-415e-82a2-a090c38a68a3)

Internet CONNECTIVITY

- There are countless ways for an Doanh nghiệp to connect to the Internet
- Ví dụ, PRIVATE WAN technologies such as LEASED LINES and MPLS VPNs can be used to connect to a SERVICE PROVIDER’s Internet Hạ tầng
- In addition, technologies such as CATV and DSL commonly used by consumers (Home Internet Access) can also be used by an Doanh nghiệp
- These days for both Doanh nghiệp and consumer Internet Access, FIBER OPTIC Ethernet connections are growing in popularity due to high speeds they provide over long distances
- Let’s briefly look at TWO Internet Access technologies mentioned above:
    - Cable (CATV)
    - DSL

---

DIGITAL SUBSCRIBER LINE (DSL)

- DSL provides Internet connectivity to customers over phone lines and can share the same phone line that is already installed in most homes
- A DSL MODEM (Modulator / Demodulator) is required to convert DATA into a format suitable to be sent over the phone lines
    - The MODEM might be a separate DEVICE or it might be incorporated in to a “HOME Router”

![image](https://github.com/psaumur/CCNA/assets/106411237/a708b6b4-6de5-4a72-8c77-13f569f4c2d5)

Cable Internet

- Cable Internet provides Internet Access via the same CATV (Cable Television) lines used for TV service
- Like DLS, a Cable MODEM is required to convert DATA into a format suitable to be sent over the CATV CABLES.
    - Like a DSL MODEM, this can be a separate device or built into the HOME Router

![image](https://github.com/psaumur/CCNA/assets/106411237/a33bb999-83bc-49a8-ad37-e7ca91fcb954)

---

REDUNDANT Internet CONNECTIONS

![image](https://github.com/psaumur/CCNA/assets/106411237/af770f82-a55c-4af5-af7b-5708b39833c4)

---

Internet VPNs

- PRIVATE WAN SERVICES such as LEASED LINES and MPLS provide Security because each customer’s TRAFFIC is separated by using dedicated physical connections (LEASED LINE) or by MPLS TAGS
- When using the Internet as a WAN to connect SITES together, there is no built-in Security by Default
- To provide secure communications over the Internet, VPNs (Virtual Private Networks) are used
- We will cover two kinds of Internet VPNs:
    - SITE-TO-SITE VPNS using IPSec
    - REMOTE-Access VPNs using TLS

SITE-TO-SITE VPNs (IPSec)

- A “SITE-TO-SITE” VPN is a VPN between two DEVICES and is used to connect TWO SITES together over the Internet
- A VPN “TUNNEL” is created between the TWO DEVICES by ENCAPSULATING the original IP Gói tin with a VPN Header and a new IP Header
    - When using IPSec, the original Gói tin is encrypted before its ENCAPSULATED with the new Header

![image](https://github.com/psaumur/CCNA/assets/106411237/b17c6149-90b2-4bc7-beb7-c53698d588a0)

![image](https://github.com/psaumur/CCNA/assets/106411237/d41295a9-af54-4cd5-acc8-4b60c39c40c2)

PROCESS SUMMARY:

1) The SENDING DEVICE combines the original Gói tin and SESSION KEY (ENCRYPTION KEY) and runs them through an ENCRYPTION FORMULA

2) The SENDING DEVICE encapsulates the ENCRYPTED Gói tin with a VPN Header and a new IP Header

3) The SENDING DEVICE sends the NEW Gói tin to the DEVICE on the other side of the TUNNEL

4) The RECEIVING DEVICE decrypts the DATA to get the original Gói tin and then forwards the original Gói tin to it’s DESTINATION

- In a “SITE-TO-SITE” VPN, a TUNNEL is formed only between TWO TUNNEL ENDPOINTS (Ví dụ, the TWO ROUTERS connected to the Internet)
- All OTHER DEVICES in each site DO NOT need to create a VPN for themselves. They can send unencrypted DATA to their site’s Router, which will ENCRYPT it and FORWARD it in the TUNNEL as described above.

---

LIMITATIONS OF STANDARD IPSec

1) IPSec doesn’t support Broadcast or Multicast TRAFFIC, only Unicast.

- This means that Định tuyến PROTOCOLS such as OSPF cannot be used over the TUNNELS because they rely on Multicast TRAFFIC
    - This can be SOLVED with “GRE over IPSec”

2) Configuring a full mesh of TUNNELS between many sites is a labor-intensive task

Let’s look at each of the above SOLUTIONS

---

GRE over IPSec

- GRE (GENERIC Định tuyến Đóng gói) creates TUNNELS like IPSec, however it does not ENCRYPT the original Gói tin, so it is NOT SECURE
- However, it has the advantage of being able to encapsulate a WIDE variety of a LAYER 3 PROTOCOLS as well as Broadcast and Multicast messages
- To get the FLEXIBILITY of GRE with the Security of IPSec, “GRE over IPSec” can be used
- The original Gói tin will be ENCAPSULATED by a GRE Header and a new IP Header, and then the GRE Gói tin will be ENCRYPTED and ENCAPSULATED within an IPSec VPN Header and a NEW IP Header

![image](https://github.com/psaumur/CCNA/assets/106411237/09c7da0c-debe-453e-822c-b97c0b8658ef)

![image](https://github.com/psaumur/CCNA/assets/106411237/3dfd6b86-28bb-489d-931b-5cc74669c1ac)

![image](https://github.com/psaumur/CCNA/assets/106411237/939ce5af-5ffc-44da-96fc-def2ca99ecae)

---

DMVPN

- DMVPN (Dynamic Multipoint VPN) is a Cisco-Developed solution that allows ROUTERS to dynamically create a FULL MESH of IPSec TUNNELS without having to manually configure every SINGLE TUNNEL

1) CONFIGURE IPSec TUNNELS to a Hub SITE

![image](https://github.com/psaumur/CCNA/assets/106411237/00c33e7f-2b28-4a33-908d-7aceff1e4092)

2) The Hub Router gives each Router information about Cách form an IPSec TUNNEL with the OTHER ROUTERS

![image](https://github.com/psaumur/CCNA/assets/106411237/7a621160-10d4-4e14-868b-3c23f6bb0a64)

DMVPN provides the Configuration simplicity of Hub-AND-SPOKE (each SPOKE Router only needs one TUNNEL configured) and the EFFICIENCY of DIRECT SPOKE-TO-SPOKE communication (SPOKE ROUTERS can communicate directly without TRAFFIC passing through the Hub)

---

REMOTE-Access VPNs

- Whereas SITE-TO-SITE VPNs are used to make a POINT-TO-POINT connection between TWO SITES over the Internet, REMOTE-Access VPNs are used to allow END DEVICES (PCs, Mobile Phone) to Access the company’s internal resources securely over the Internet
- REMOTE-Access VPNs typically use TLS (TRANSPORT LAYER Security)
    - TLS is also what provides Security for HTTPS (HTTP SECURE)
    - TLS was formerly known as SSL (Secure Socket Layer) and developed by Netscape, but it was renamed to TLS when it was standardized by the IETF
- VPN client software  (Ví dụ Cisco AnyConnect) is installed on END DEVICES (Ví dụ company-provided laptops that employees use to work from home)
- These END DEVICES then form SECURE TUNNELS to one of the company’s ROUTERS / FIREWALLS acting as a TLS SERVER
- This allows the END USERS to securely Access RESOURCES on the company’s INTERNAL Network without being directly connected to the company Network

![image](https://github.com/psaumur/CCNA/assets/106411237/f4a77cb7-9d42-4daa-9a25-630c0fb260cf)

---

SITE-TO-SITE versus REMOTE-Access VPN

- SITE-TO-SITE VPNs typically use IPSec
- REMOTE-Access VPNs typically use TLS
- SITE-TO-SITE VPNs provide SERVICE to many DEVICES within the SITES they are connecting
- REMOTE-Access VPNs provide SERVICE to the ONE END DEVICE the VPN CLIENT SOFTWARE is installed on

- SITE-TO-SITE VPNs are typically used to permanently connect TWO SITES over the Internet
- REMOTE-Access VPNs are typically used to provide ON-DEMAND Access for END DEVICES that want to securely Access company resources while connected to a Network which is not SECURE

---

LAB COMMANDS

Create the Tunnel Interface

`R1(config)#int tunnel <tunnel number>`

This changes the mode to the Tunnel Interface

The exit Interface for the tunnel

`tunnel source <interface>` 

IP of the Tunnel Destination Interface

`tunnel destination <destination ip address>`

Set the IP of the Source Tunnel Interface (from step 1)

`ip address <tunnel IP> <netmask>`

Configure a Default Tuyến đường to the Service Provider Network

`R1(config)#ip route 0.0.0.0 0.0.0.0 <next hop interface>`

This will now bring the Tunnel Interface Administratively Up / Up

================================================

Now you need to set up the TUNNEL ROUTERS as OSPF Neighbors for the Service Provider Network so they can share routes

`R1(config)router ospf <ospf process ID>`

This switches to the OSPF Router Configuration mode

`network <tunnel interface IP> <wildcard mask> area <area #>`

Since the tunnel is a single HOST, you would use 0.0.0.0 for the Wildcard Mask

`network <router gateway IP> <wildcard mask> area <area #>`

Since the Router Gateway is also a single HOST, you would use 0.0.0.0 for the Wildcard Mask

`passive-interface <router gateway IP interface>`

This removes the Router Gateway from broadcasting over OSPF
