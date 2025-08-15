# 49. Cổng Bảo mật

INTRO TO Cổng Bảo mật

- Cổng Bảo mật is a Bảo mật feature of Cisco SWITCHES
- It allows you to control WHICH SOURCE Địa chỉ MAC(ES) are allowed to enter the SWITCHPORT
- If an unauthorized SOURCE Địa chỉ MAC enters the Cổng, an ACTION will be TAKEN
    - The Mặc định action is to place the Giao diện in an “err-disabled” state

![image](https://github.com/psaumur/CCNA/assets/106411237/92f4ce9b-8fb4-4d57-b200-f41c7d5236ee)

- When you Kích hoạt Cổng Bảo mật on an Giao diện with the Mặc định settings, one Địa chỉ MAC is allowed
    - You can configure the ALLOWED Địa chỉ MAC manually
    - If you DO NOT configure it manually, the Switch will allow the first SOURCE Địa chỉ MAC that enters the Giao diện
- You can CHANGE the MAXIMUM number of MAC ADDRESSES allowed
- A COMBINATION of manually configured MAC ADDRESSES and DYNAMICALLY LEARNED ADDRESSES is possible

![image](https://github.com/psaumur/CCNA/assets/106411237/0b6e8053-6819-4e02-ae28-4699a5c9c92d)

---

WHY USE Cổng Bảo mật?

- Cổng Bảo mật allows Mạng admins to control which DEVICES are allowed to Access the Mạng
- However, Địa chỉ MAC SPOOFING is a simple task
    - It is easy to configure a DEVICE to send FRAMES with a different SOURCE Địa chỉ MAC
- Rather than manually specifying the MAC ADDRESSES allowed on each Cổng, Cổng Bảo mật’S ability to limit the number of MAC ADDRESSES allowed on an Giao diện is more useful
- Think of the DHCP STARVATION ATTACK (DAY 48 LAB video)
    - The ATTACKER spoofed thousands of fake MAC ADDRESSES
    - The DHCP SERVER assigned IP ADDRESSES to these fake MAC ADDRESSES, exhausting the DHCP POOL
    - The Switch’S Địa chỉ MAC table can also become full due to such an attack
- Limiting the NUMBER of MAC ADDRESSES on an Giao diện can protect against those attacks

ENABLING Cổng Bảo mật

![image](https://github.com/psaumur/CCNA/assets/106411237/b00765c2-f3a1-45be-8ed4-0a8dab68e43e)

`show port-security interface`

![image](https://github.com/psaumur/CCNA/assets/106411237/787959b1-ffad-451d-ac65-11ea9a99db2d)

![image](https://github.com/psaumur/CCNA/assets/106411237/9a6dd39d-130e-411b-be46-ecfe93420813)

![image](https://github.com/psaumur/CCNA/assets/106411237/f071f447-a6ef-4ee6-8a40-2bde94030993)

RE-ENABLING AN Giao diện (MANUALLY)

![image](https://github.com/psaumur/CCNA/assets/106411237/706736d4-ee7c-42b2-b424-6cc30eb50905)

RE-ENABLING AN Giao diện (ERR-Vô hiệu hóa RECOVERY)

![image](https://github.com/psaumur/CCNA/assets/106411237/6eb0d808-a989-4261-9b39-1ac9e1bf1460)

![image](https://github.com/psaumur/CCNA/assets/106411237/41d54ef0-7391-473e-9b51-87f44b9e3f3c)

---

VIOLATION MODES

- There are THREE DIFFERENT VIOLATION MODES that determine what the Switch will do if an unauthorized Khung enters an Giao diện configured with Cổng Bảo mật
    - SHUTDOWN
        - Effectively shuts down the Cổng by placing it in an ‘err-disabled` state
        - Generates a SYSLOG and / or SNMP message when the INTERFACE is ‘disabled’
        - The VIOLATION counter is set to 1 when the INTERFACE is ‘disabled’
    - RESTRICT
        - The SWITCH discards traffic from unauthorized MAC ADDRESSES
        - The INTERFACE is NOT disabled
        - Generates a SYSLOG and / or SNMP message each time an unauthorized MAC is detected
        - The VIOLATION counter is incremented by 1 for each unauthorized FRAME
    
    - PROTECT
        - The SWITCH discards traffic from unauthorized MAC ADDRESSES
        - The INTERFACE is NOT disabled
        - It does NOT generate a SYSLOG / SNMP message for unauthorized traffic
        - It does NOT increment the VIOLATION counter
    
---

VIOLATION MODE - RESTRICT

![image](https://github.com/psaumur/CCNA/assets/106411237/819f00b9-9694-442d-8459-8018f4277e45)


VIOLATION MODE - PROTECT

![image](https://github.com/psaumur/CCNA/assets/106411237/20d17f97-056e-4e76-8566-bb49c10bb9e1)

---

SECURE MAC ADDRESS AGING

![image](https://github.com/psaumur/CCNA/assets/106411237/4454fedf-f942-4b0d-9b6f-074765de653d)

- By DEFAULT, SECURE MAC ADDRESSES will not ‘age out’ (Aging Time : 0 mins)
    - Can be configured with `switchport Cổng-Bảo mật aging time *minutes*`

- The DEFAULT Aging Type is ABSOLUTE
    - ABSOLUTE
        - After the SECURE MAC ADDRESS is learned, the AGING TIMER starts and the MAC is removed after the TIMER expires, even if the SWITCH continues receiving FRAMES from that SOURCE MAC ADDRESS.
    - INACTIVITY
        - After the SECURE MAC ADDRESS is learned, the AGING TIMER starts but is RESET every time a FRAME from that SOURCE MAC ADDRESS is received on the INTERFACE
            - Aging type is configured with:  `switchport Cổng-Bảo mật aging type {absolute | inactivity}`
- Secure Static MAC AGING (address configured with `switchport Cổng-Bảo mật mac-address x.x.x`) is DISABLED by DEFAULT

![image](https://github.com/psaumur/CCNA/assets/106411237/93f11517-9d97-4e52-89ad-a0e590bca702)

---

STICKY SECURE MAC ADDRESSES 

- ‘STICKY’ SECURE MAC ADDRESS learning can be enabled with the following command:
    - `SW(config-if)# switchport Cổng-Bảo mật mac-address sticky`

- When enabled, dynamically-learned SECURE MAC ADDRESSES will be added to the running configuration, like this:
    - `switchport Cổng-Bảo mật mac-address sticky *mac-address*`

- The ‘STICKY’ SECURE MAC ADDRESSES will NEVER age out
    - You need to SAVE the `running-config` to `startup-config` to make them TRULY permanent (or else they will not be kept if the SWITCH restarts)
- When you issue the `switchport Cổng-Bảo mật mac-address sticky` command, all current dynamically-learned secure MAC addresses will be converted to STICKY SECURE MAC ADDRESSES
- If you issue the `no switchport Cổng-Bảo mật mac-address sticky` command, all current STICKY SECURE MAC ADDRESSES will be converted to regular dynamically-learned SECURE MAC ADDRESSES

![image](https://github.com/psaumur/CCNA/assets/106411237/10d591f9-334c-4e3b-889e-16030c36c445)

---

MAC ADDRESS TABLE

- SECURE MAC ADDRESSES will be added to the MAC ADDRESS TABLE like any other MAC ADDRESS
    - STICKY and STATIC SECURE MAC ADDRESSES will have a type of STATIC
    - Dynamically-Learned SECURE MAC ADDRESSES will have a type of DYNAMIC
    - You can view all SECURE MAC ADDRESSES with `show Địa chỉ MAC-table secure`
    

![image](https://github.com/psaumur/CCNA/assets/106411237/c9123729-541c-4363-ba19-d8e49f75c6c5)

---

Lệnh REVIEW

![image](https://github.com/psaumur/CCNA/assets/106411237/716ce91d-d1bb-4f12-a8fd-226b65f22569)
