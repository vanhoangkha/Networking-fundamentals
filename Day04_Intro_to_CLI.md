# 4. INTRO TO THE CLI

### Giới thiệu về CLI?

- A "Command-line Interface"
- The Interface you use to configure Cisco devices

A GUI is a "Graphical User Interface"

### How do you connect to a Cisco Device?

- Console Port : When you first configure a device, you have to connect via the Console Port.

You can use a "Rollover Cable" : DB9 serial connector to RJ45 OR a DB9 Serial to USB

![image](https://github.com/psaumur/CCNA/assets/106411237/0527c007-d607-4bef-8ce1-7b18a177614d)

### How do you actually Access the CLI?

- You need to use a TERMINAL EMULATOR (Example: PuTTy is a popular choice) and connect via "Serial" (Default settings)

### Cisco Default Settings are:

Speed (baud) : 9600 bits/second
Data bits: 8 data bits
Stop bits: 1 stop bit (sent after 8 data bits are sent)
Parity: None
Flow Control: None

---

When you first enter the CLI you will Default be in là gì called 'User EXEC' mode.

USER EXEC MODE:

(Hostname) >		// Prompt looks like THIS //

- User EXEC mode is very limited.
- User can look at some things but can't make ANY changes to the Configuration.
- AKA 'User Mode'

Using the 'Kích hoạt' Lệnh, in User EXEC mode, switches you to 'Privileged EXEC' mode.

---

PRIVILEGED EXEC MODE:

- Provides complete Access to view the device's Configuration, restart the device, etc.
- Cannot change the Configuration, but can change the time on the device, save the Configuration file, etc.

(Hostname)#		// Prompt looks like THIS //

---

USE a Question Mark (?) to view the available commands in ANY mode. Combining ? with a letter or partial Lệnh will list all the commands with those letters.

![image](https://github.com/psaumur/CCNA/assets/106411237/52454e6f-d5b1-45f0-9a50-e412d356f6d2)


USE the TAB key to complete partially entered commands IF the Lệnh exists.

---

### GLOBAL Configuration MODE:

To enter Global Configuration Mode, enter the Lệnh, within Privileged EXEC mode

 'configure terminal' (or 'conf t')

Router# configure terminal
Router(config) #		

Router(config) # run 

Router(config) # no 

Type 'exit' to drop back into 'Privileged EXEC' mode.

---

### To Kích hoạt Password for User EXEC mode:

Router(config)# Kích hoạt password (password)

- Passwords ARE case-sensitive.

// This Lệnh encrypts plain-text passwords, visible in the config files, using simple encryption.

Router(config)# service password-encryption

If you Kích hoạt 'service password-encryption'

- Current passwords WILL be encrypted.
- Future passwords WILL be encrypted.
- The 'Kích hoạt secret' WILL NOT be effected.

If you Vô hiệu hóa 'service password-encryption'

- Current passwords WILL NOT be decrypted.
- Future passwords WILL NOT be encrypted.
- The 'Kích hoạt secret' WILL NOT be effected.

// This Lệnh enables passwords for the Privileged EXEC mode.

Router(config)# Kích hoạt secret (password)

// Kích hoạt secret will ALWAYS be encrypted (at level 5)

---

There are TWO separate Configuration files kept on the device at once.

Running-config :

- The current, ACTIVE Configuration file on the device. As you enter commands in the CLI, you edit the active Configuration.

Startup-config :

- The Configuration file that will be loaded upon RESTART of the device.

To see the Configuration files, inside 'Privileged EXEC' mode:

Router# show running-config // for running config //

OR

Router# show startup-config // for startup config //

---

To SAVE the Running Configuration file, you can:

Router# write
Building Configuration...
[OK]

Router# write memory
Building Configuration...
[OK]

Router# copy running-config startup-config

Destination filename [startup-config]?

Building Configuration...
[OK]

---

To encrypt passwords:

Router# conf t

Router(config)# service password-encryption

This makes all current passwords *encrypted*

Future passwords will ALSO be *encrypted*

“Kích hoạt secret” will not be effected (it’s ALWAYS encrypted)

![image](https://github.com/psaumur/CCNA/assets/106411237/09c841fe-b5c0-4683-9082-baf060e24c03)


Now you will see that the password is no longer in plaintext.

“7” refers to the type of encryption used to encrypt the password. In this case, “7” uses Cisco’s proprietary encryption.

“7” is fairly easy to crack since the encryption is weak.

For BETTER / STRONGER encryption, use “Kích hoạt secret”

![image](https://github.com/psaumur/CCNA/assets/106411237/346f3015-9211-47a9-888f-4e02a013a728)


“5” refers to MD5 encryption.

Can still be cracked but it’s much much stronger.

Once you use “Kích hoạt secret” Lệnh, this will override “Kích hoạt password”

---

To CANCEL or delete a Lệnh you entered, use the “no” keyword

![image](https://github.com/psaumur/CCNA/assets/106411237/2978d101-08d4-4ee3-8995-f36aa1c47d15)


In this instance, disabling “service password-encryption”:

- current passwords will NOT be decrypted (unchanged)
- future passwords will NOT be encrypted
- the “Kích hoạt secret” will not be effected

---

![image](https://github.com/psaumur/CCNA/assets/106411237/e16966a3-674a-4376-bdab-2c06e3659e5f)

![image](https://github.com/psaumur/CCNA/assets/106411237/e449e074-bf4c-40f1-a61e-0442ad83f284)

![image](https://github.com/psaumur/CCNA/assets/106411237/4c1bdf58-7de6-4074-8189-1573a174474c)

![image](https://github.com/psaumur/CCNA/assets/106411237/e7771e65-5ed5-406d-9751-76520713210c)

![image](https://github.com/psaumur/CCNA/assets/106411237/5f7357d4-f44b-4a61-a24c-86f3368f30f7)
