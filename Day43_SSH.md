# 42. SSH (Secure Shell)

CONSOLE Cổng Bảo mật

- By Mặc định, no password us needed to Access the CLI of a CISCO IOS DEVICE via the CONSOLE Cổng
- You can CONFIGURE a PASSWORD on the *console line*
    - A USER will have to enter a PASSWORD to Access the CLI via the CONSOLE Cổng

![image](https://github.com/psaumur/CCNA/assets/106411237/9609b0af-0fb1-4563-89e4-82b58b29325e)

- Alternatively, you can configure the CONSOLE LINE to require USERS to LOGIN using one of the configured USERNAMES on the DEVICE

![image](https://github.com/psaumur/CCNA/assets/106411237/04588b3a-3640-41af-b19e-41768f63b2bc)

---

LAYER 2 Switch Quản lý IP

- LAYER 2 SWITCHES do not perform Gói tin Định tuyến and build a Định tuyến TABLE. They are NOT IP Định tuyến aware
- However, you CAN assign an Địa chỉ IP to an SVI to allow REMOTE CONNECTIONS to the CLI of the Switch (using Telnet or SSH)

![image](https://github.com/psaumur/CCNA/assets/106411237/64a9e983-f353-4670-8a99-1e22129eb661)

---

Telnet

- Telnet (Teletype Mạng) is a Giao thức used to REMOTELY Access the CLI of a REMOTE HOST
- Telnet was developed in 1969
- Telnet has been largely REPLACE by SSH, which is MORE Secure
- Telnet sends data in PLAIN TEXT. NO ENCRYPTION(!)

<aside>
💡 Telnet SERVERS listen for Telnet traffic on TCP Cổng 23

</aside>

![image](https://github.com/psaumur/CCNA/assets/106411237/9dffe7fb-4fa4-4ee9-90bf-d27461bb5190)

---

VERIFY Telnet Cấu hình

![image](https://github.com/psaumur/CCNA/assets/106411237/e077b5fd-3130-4fb0-9b17-d28bdef665df)

---

SSH

- SSH (Secure Shell) was developed in 1995 to REPLACE LESS SECURE PROTOCOLS, like Telnet
- SSHv2, a major revision of SSHv1, was released in 2006
- If a DEVICE supports both v1 and v2, it is said to run ‘version 1.99’
- Provides Bảo mật features; such as DATA ENCRYPTION and AUTHENTICATION

CHECK SSH SUPPORT

![image](https://github.com/psaumur/CCNA/assets/106411237/441c38b7-4b79-4c80-8eca-0463960124b6)

RSA KEYS

- To Kích hoạt and use SSH, you must first generate an RSA PUBLIC and PRIVATE KEY PAIR
- The KEYS are used for DATA ENCRYPTION / DECRYPTION, AUTHENTICATION, etc.

![image](https://github.com/psaumur/CCNA/assets/106411237/73bd5a86-32da-4ec6-b385-fe5425a72808)

VTY LINES

![image](https://github.com/psaumur/CCNA/assets/106411237/04e9072f-ccde-476d-a84d-3034e0b39d19)

---

SUMMARY ABOUT SSH CONFIGURATIONS

![image](https://github.com/psaumur/CCNA/assets/106411237/bb6d358f-e742-434b-835c-5c7cd762abdb)

![image](https://github.com/psaumur/CCNA/assets/106411237/bb2e760b-90c3-42a7-93f6-0ccc7e472d00)
