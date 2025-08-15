# 63. ANSIBLE, PUPPET, AND CHEF

Configuration DRIFT

- Configuration DRIFT is when individual changes made over time causes a device’s Configuration to deviate from the standard / correct configurations as defined by the company
    - Although each device will have unique parts of its configurations (IP Addresses, hostname, etc) most of a device’s Configuration is usually defined in standard templates designed by the Network architects / engineers of the company
    - As individual engineers make changes to devices (Ví dụ, to troubleshoot and fix Network issues, test configurations, etc), the Configuration of a device can drift away from the standard.
    - Records of these individual changes and their reasons aren’t kept
    - This can lead to future issues
- Even without Tự động hóa tools, it is best to have standard Configuration Management practices.
    - When a change is made, save the config as a text file and place it in a shared folder
        - A standard naming system like (*hostname_yyyymmdd)* might be used.
        - There are flaws to this system, as an engineer might forget to place the new config in the folder after making changes. Which one should be considered the “CORRECT” config?
        - Even if configurations are properly saved like this, it doesn’t guarantee that the configurations actually match the standard
---

Configuration PROVISIONING

- Configuration PROVISIONING refers to how Configuration changes are applied to devices
    - This includes configuring new devices, too
- Traditionally, Configuration provisioning is done by connecting to devices one-by-one via SSH
    - This is not practical in large networks
- Configuration Management tools like Ansible, Puppet, and Chef allow us to make changes to devices on a mass scale with a fraction of time and effort.

- TWO ESSENTIAL COMPONENTS:
    - Templates
    - Variables

![image](https://github.com/psaumur/CCNA/assets/106411237/0c74b2a6-1ce7-4758-b6b8-340594d567c3)

---

INTRO TO Configuration Management TOOLS

- Configuration Management TOOLS are Network Tự động hóa tools that facilitate the centralized control of large numbers of Network devices
- The option you need to be aware of for the CCNA are Ansible, Puppet, and Chef
- These tools were originally developed after the rise of VMs, to Kích hoạt server system admins to automate the process of creating, configuring, and removing VMs
    - However, they are also widely used to manage Network devices
    
- These tools can be used to perform tasks such as :
    - Generate configurations for new devices on a large scale
    - Perform Configuration changes on devices (all devices in your Network, or certain subset of devices)
    - Check device configurations for compliance with defined standards
    - Compare configurations between devices, and between different versions of configurations on the same device

![image](https://github.com/psaumur/CCNA/assets/106411237/f9eb7783-5e42-4cfe-aec8-8b57cd316f4d)

---

Ansible 

- Ansible is a Configuration Management tool owned by Red Hat
- Ansible itself is written in Python
- Ansible is *agentless*
    - It doesn’t require any special software to run on the managed devices
- Ansible uses SSH to connect to devices, make Configuration changes, extract info, etc
- Ansible uses a *push* model. The Ansible server (Control node) uses SSH to connect to managed devices and *push* Configuration changes to them
    - Puppet and Chef use a *pull* model
    
- After installing Ansible itself, you must create several text files:
    - PLAYBOOKS :
        - These files are “blueprints of Tự động hóa tasks”
        - They outline the logic and actions of the tasks that Ansible should do
        - Written in YAML
    - INVENTORY :
        - These files list the devices that will be managed by Ansible, as well as characteristics of each device such as their device role (Access Switch, Core Switch, WAN Router, Tường lửa, etc.)
        - Written in INI, YAML, or other formats
    - TEMPLATES :
        - These files represent a device’s Configuration file, but specific values for variables are not provided.
        - Written in JINJA2 format
    - VARIABLES :
        - These files list variables and their values.
        - These values are substituted into the templates to create complete Configuration files.
        - Written in YAML

![image](https://github.com/psaumur/CCNA/assets/106411237/ba2a68b5-7661-4eff-bd5f-8c32bde354da)

---

Puppet 

- Puppet is a Configuration Management tool written in RUBY
- Puppet is typically agent-based
    - Specific software must be installed on the managed devices
    - Not all Cisco devices support a Puppet agent
    
- It CAN be run *agentless,* in which a proxy agent runs on an external host, and a proxy agent uses SSH to connect to the managed devices and communicate with them
- The Puppet server is called the “Puppet master”
- Puppet uses a PULL model (clients “pull” configurations from the Puppet master)
    - Clients use TCP 8140 to communicate with the Puppet master
- Instead of YAML, it uses a proprietary language for files
- Text files required on the Puppet master include:
    - MANIFEST :
        - The file defines the desired Configuration state of a Network device
    - TEMPLATES :
        - Similar to Ansible templates.
        - Used to generate MANIFESTS

![image](https://github.com/psaumur/CCNA/assets/106411237/ec26ad33-7534-4f15-93f0-4557337bfaec)

---

Chef

- Chef is a Configuration Management tool written in RUBY
- Chef is Agent-Based
    - Specific software must be installed on the managed devices
    - Not all Cisco devices support a Chef agent
- Chef uses a PULL model
- The server uses TCP 10002 to send configurations to clients
- Files use a DSL (Domain-Specific Language) based on Ruby
- Text files used by Chef include:
    - RESOURCES :
        - The “ingredients” in a RECIPE.
        - Configuration objects managed by Chef
    - RECIPES :
        - The “recipes” in a COOKBOOK.
        - Outlines the logic and actions of the tasks performed on the resources
    - COOKBOOKS :
        - A set of related RECIPES grouped together
    - RUN-LIST :
        - An ordered list of RECIPES that are run to bring a device to the desired Configuration state

![image](https://github.com/psaumur/CCNA/assets/106411237/eaf5be1b-3635-4806-bb7a-f397ffa1b411)

---

MEMORIZE THIS CHART FOR THE CCNA

![image](https://github.com/psaumur/CCNA/assets/106411237/a4d212e6-df46-45d1-a2ca-3e55220c4b5c)
