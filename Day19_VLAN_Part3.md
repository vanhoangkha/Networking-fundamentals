# 18. VLANS : PART 3

VLAN gốc ON A Router (ROAS)

![image](https://github.com/psaumur/CCNA/assets/106411237/838b9835-d17d-4d57-bac1-52f7e3adfd77)

VLAN gốc untagged frames are faster and more efficient (smaller) than tagged ones.

Let’s reset all SWITCHES (SW1 and SW2) to VLAN gốc 10

![image](https://github.com/psaumur/CCNA/assets/106411237/1e903c1b-b814-40b5-aaea-1ba9f3f192c8)



There are **TWO methods** of configuring the VLAN gốc on a Router:

- Use the Lệnh “Đóng gói dot1q <VLAN-id>” on a Sub-Interface

![image](https://github.com/psaumur/CCNA/assets/106411237/2ea65208-6b2a-4cac-a463-982a731c9e24)


OR

- Configure the Địa chỉ IP for the VLAN gốc on the Router’s physical Interface (the “**Đóng gói dot1q** <VLAN-id> Lệnh is not necessary”

![image](https://github.com/psaumur/CCNA/assets/106411237/dabcc3b4-13c3-4d60-abe2-c7cbb5edd4c2)


Output of “show running-config” of G0/0 Interface

![image](https://github.com/psaumur/CCNA/assets/106411237/37ce4f0f-0ac0-45ce-802f-5fd11057f69d)


---

LAYER 3 (MULTILAYER) SWITCHES

ICON APPEARANCE

![image](https://github.com/psaumur/CCNA/assets/106411237/0d63f5f9-5efe-4c61-a8e6-3cd6a1161d2a)


- A MULTILAYER Switch is capable of both SWITCHING and Định tuyến
- It is LAYER 3 AWARE
- You can assign IP Addresses to its L3 Virtual Interface, like a Router
- You can create Virtual Interfaces for each VLAN, and assign IP addresses to those interfaces
- You can configure routes on it, just like a Router
- It can be used for inter-VLAN Định tuyến

![image](https://github.com/psaumur/CCNA/assets/106411237/af59481b-d0cb-41d7-9eba-7c8d47131c28)


SW2 Replaced with a Layer 3 Switch

Multi-VLAN connections to R1 removed and replaced with a point-to-point Layer 3 connection

![image](https://github.com/psaumur/CCNA/assets/106411237/8f3ad167-d774-4fcb-96a5-66e568edead8)


- SVIs (Switch Virtual Interfaces) are the virtual interfaces you can assign IP addresses to in a MULTILAYER Switch.
- Configure each HOST to use the SVI (NOT the Router R1) as their Gateway Address
- To send traffic to different SUBNETS / VLANS, the PCs will send traffic to the Switch, and the Switch will Tuyến đường the traffic.

![image](https://github.com/psaumur/CCNA/assets/106411237/5409b2cc-f876-4754-afe3-33298930fd7a)


![image](https://github.com/psaumur/CCNA/assets/106411237/953372de-579a-4803-9418-0bd1aeef229d)


Clearing R1 Configuration to set to work with the Layer 3 Point-to-Point connection

![image](https://github.com/psaumur/CCNA/assets/106411237/40354cbe-df39-4a78-97cd-bbb0bc10549c)


#no Interface <sub-Interface id> : removes the VLAN Interface

#Default Interface g0/0 : resets the g0/0 Interface to it’s Default settings

Then configure the Default R1 G0/0 Interface’s to Địa chỉ IP : 192.168.1.194 (as per the Network diagram)

Configuration of SW2 to use SVI and the Layer 3 Point-to-Point connection with R1

![image](https://github.com/psaumur/CCNA/assets/106411237/24d64087-f98c-4a1e-a07f-3f93f06f93a9)


“Default Interface <Interface-id>” : resets settings on specified Interface to defaults

“ip Định tuyến” : **IMPORTANT** Lệnh to Kích hoạt Layer 3 Định tuyến on the Switch

“no switchport” : configures the Interface from a Layer 2 Switchport to a Layer 3 “routed Port” 

The sets the Default Tuyến đường to R1 (192.168.1.194) so that all traffic leaving the Network gets routed through R1’s Gateway of Last Resort (aka The Default Gateway)

![image](https://github.com/psaumur/CCNA/assets/106411237/7a682a2f-3ae3-420b-8f68-9e1050dd82c6)


![image](https://github.com/psaumur/CCNA/assets/106411237/c0b544b7-8f32-49ae-9a46-d09390a3d08c)


SVI Configuration ON SW2 (Virtual LAYER 3 Định tuyến INTERFACES)

![image](https://github.com/psaumur/CCNA/assets/106411237/7c1710fb-40d7-44a4-8336-b037e1c2ea77)



SVIs are **shut down** by Default, so remember to use “no shutdown”

![image](https://github.com/psaumur/CCNA/assets/106411237/2b5b13c3-1364-4296-886c-0bd9b00b4167)


Creating an unknown SVI (VLAN 40) and the Status/Giao thức is “down/down”

What are the conditions for a SVI to be “up/up” ? 

- The VLAN must exist on the Switch
- The Switch must have at least ONE Access Port in the VLAN in an “up/up” state AND/OR one Trunk Port that allows the VLAN that is in an “up/up” state
- The VLAN must not be shutdown (you can use the “shutdown” Lệnh to Vô hiệu hóa a VLAN)
- The SVI must not be shutdown (SVIs are disabled, by Default)

![image](https://github.com/psaumur/CCNA/assets/106411237/558ef418-5902-42d0-b4a5-cce14b56b77e)


The VLAN Trunk has been successfully replaced by an Layer 3 Switch SVI.

All hosts should be able to connect with each other (tested with “ping”) as well as reach the external Internet (via the Cloud symbol attached to R1)
