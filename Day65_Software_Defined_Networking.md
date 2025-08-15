# 62. NETWORK ĐỊNH NGHĨA BẰNG PHẦN MỀM (SDN)

SD REVIEW

- Network định nghĩa bằng phần mềm (SDN) is an approach to networking that centralizes the control plane into an application called a *controller*
- Traditional control planes use a distributed Kiến trúc
- A SDN controller centralizes control plane functions like calculating routes
- The controller can interact programmatically with the Network devices using APIs
- The SBI (South Bound Interface) is used for communications between the controller and the Network device it controls
- The NBI (North Bound Interface) is what allows us to interact with the controller with our scripts and applications

SDN Kiến trúc

![image](https://github.com/psaumur/CCNA/assets/106411237/9d7e1a89-3537-48cc-a410-cef352b6a2cb)

---

CISCO SD-Access

- Cisco SD-Access is Cisco’s SDN solution for automating Campus LANs
    - ACI (Application Centric Hạ tầng) is their SDN solution for automating data center networks
    - SD-WAN is their SDN solution for automating WANs
- Cisco DNA (Digital Network Kiến trúc) Center is the controller at the center of SD-Access

![image](https://github.com/psaumur/CCNA/assets/106411237/4c1662ee-490c-4eee-8970-550ca60feabb)

- The UNDERLAY is the underlying physical Network of devices and connections (including wired and Không dây) which provide IP connectivity (ie: using IS-IS)
    - Multilayer Switches and their connections

![image](https://github.com/psaumur/CCNA/assets/106411237/41bb11dd-31c9-493e-9fec-af847f0732dc)

- The OVERLAY is the virtual Network built on top of the physical underlay Network

![image](https://github.com/psaumur/CCNA/assets/106411237/99f48b9e-ed68-4c11-b456-d0f6ccf13fed)

- The FABRIC is the combination of the OVERLAY and UNDERLAY; the physical and virtual Network as a whole

![image](https://github.com/psaumur/CCNA/assets/106411237/35cf981c-337d-4117-9124-9f210e85bff3)

---

SD-Access UNDERLAY

- The UNDERLAY’s purpose is to support the VXLAN tunnels of the OVERLAY
- There are THREE different ROLES for switches in SD-Access:
    - EDGE NODES : Connect to End HOSTS
    - BORDER NODES : Connect to devices outside of the SD-Access Domain ; ie: WAN routers
    - CONTROL NODES : Uses LISP (Locator ID Separation Giao thức) to perform various control plane functions
    
- You can add SD-Access on top of the existing Network (*brownfield deployment*) if your Network hardware and software supports it
    - Google ‘Cisco SD-Access compatibility matrix’ if you are curious
    - In this case DNA CENTER won’t configure the UNDERLAY

- A NEW deployment (*greenfield deployment)* will be configured by DNA CENTER to use the optimal SD-Access UNDERLAY:
    - ALL Switches are LAYER 3 and use IS-IS as their Định tuyến Giao thức
    - All Links between Switches are ROUTED PORTS. This means STP is not needed
    - EDGE NODES (Access SWITCHES) act as the the Default Gateway of END HOSTS *(Routed Access Layer)*

![image](https://github.com/psaumur/CCNA/assets/106411237/0315f1e5-d9c6-47ce-acf2-1de6f14ac89c)

![image](https://github.com/psaumur/CCNA/assets/106411237/84d48992-30f9-45cf-856a-089ce00d0641)

---

SD-Access OVERLAY

- LISP (Locator ID Separation Giao thức) provides the control plane of SD-Access
    - A list of mappings of EIDs (endpoint identifiers) to RLOCs (Định tuyến locators) is kept
    - EIDs identify END HOSTS connected to EDGE SWITCHES
    - RLOCS identify the EDGE Switch which can be used to reach the END HOST
    - There is a LOT more detail to cover about LISP but I think you can see how it differs from traditional CONTROL PLANE
    
- Cisco TrustSec (CTS) provides policy control (QoS, Security Policy, etc.)

- VXLAN provides the DATA PLANE of SD-Access

![image](https://github.com/psaumur/CCNA/assets/106411237/8fd0bb65-31df-4db5-a79c-044c68c37b01)

![image](https://github.com/psaumur/CCNA/assets/106411237/b4c017b1-cc59-4305-9924-f25a5445a36b)

![image](https://github.com/psaumur/CCNA/assets/106411237/5adcaf16-4caf-4de2-9b8f-3e777c841bc6)

---

CISCO DNA CENTER

- Cisco DNA Center has TWO MAIN ROLES:
    - The SDN Controller in SD-Access
    - A Network manager in a traditional Network (non-SD-Access)
- DNA Center is an application installed on Cisco UCS server hardware
- It has a REST API which can be used to interact with DNA Center
- The SBI supports protocols such as NETCONF and RESTCONF (as well as traditional protocols like Telnet, SSH, and SNMP)
- DNA Center enables *Intent-Based Networking* (IBN)
    - The goal is to allow the engineer to communicate their intent for Network behavior to DNA Center, and then DNA Center will take care of the details of the actual configurations and policies on devices

- Traditional Security policies using ACLs can become VERY cumbersome
    - ACLs can have thousands of entries
    - The intent of entries is forgotten with time and as engineers leave and new engineers take over

- DNA Center allows the engineer to specify the intent of the policy
    - Examples :
        - THIS group of users can’t communicate with THAT group
        - THIS group can Access THIS server but not THAT server
    - DNA CENTER will take care of the exact details of implementing this policy

![image](https://github.com/psaumur/CCNA/assets/106411237/30773f46-3564-4d66-a175-20962d1569dd)

---

>For more details, you can check out [sandboxdnac.cisco.com](HTTP://sandboxdnac.cisco.com) (User: devnetuser, Password: Cisco123!)

---

DNA CENTER Network Management VS. TRADITIONAL

Traditional Management :

- DEVICES are configured one-by-one via SSH or Console connection
- DEVICES are manually configured via Console connection before being deployed
- Configurations and polices are managed per-device
- New Network deployments can take a long time due to the manual labor required
- Errors and failures are more likely due to increased manual effort

DNA CENTER-based Network Management :

- DEVICES are centrally managed and monitored from the DNA CENTER GUI or other applications using it’s REST API
- The Administrator communicates their intended Network behavior to DNA CENTER, which changes those intentions into configurations on the managed Network devices
- Configurations and policies are centrally managed
- Software versions are also centrally managed. DNA CENTER can monitor cloud servers for new versions and then update the managed devices
- New Network deployments are much quicker. New devices can automatically receive their configurations from DNA CENTER without manual Configuration

![image](https://github.com/psaumur/CCNA/assets/106411237/cb9e0184-6b45-4dcc-85ae-cef3245c1629)
