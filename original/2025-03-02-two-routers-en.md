---
audio: false
lang: en
layout: post
title: Using Two Routers
translated: false
---

To set up your two TP-Link AX3000 (TL-XDR 3050) routers with your modem in the configuration **Modem → Cable → Router1 → Wireless → Router2**, follow this step-by-step guide. Your modem already has WiFi functionality and an IP address of `192.168.1.1`. We'll configure Router1 as the main router connected to the modem via a cable and Router2 to extend the network wirelessly.

Here’s how to achieve this:

---

### **Step 1: Understand the Setup**
- **Modem**: Provides internet access and has its own WiFi (IP: `192.168.1.1`).
- **Router1**: Will connect to the modem with a cable and act as the primary router for your network.
- **Router2**: Will connect wirelessly to Router1 to extend the network coverage.

You’ve mentioned several modes (Wired AP Bridge, Wireless AP Bridge, DHCP, Broadband Connect). We’ll use **DHCP** for Router1 to get an internet connection from the modem and **Wireless AP Bridge** (or a similar mode like WDS/Repeater) for Router2 to connect wirelessly to Router1.

---

### **Step 2: Set Up Router1**
1. **Connect Router1 to the Modem**:
   - Take an Ethernet cable and plug one end into a **LAN port** on your modem.
   - Plug the other end into the **WAN (Internet) port** on Router1.

2. **Access Router1’s Web Interface**:
   - Connect a computer or smartphone to Router1’s default WiFi network (check the label on the router for the default SSID and password) or use an Ethernet cable.
   - Open a web browser and type `http://tplinkwifi.net` or `192.168.0.1` (the default IP for TP-Link routers).
   - Log in with the default credentials (usually `admin` for both username and password) unless you’ve changed them.

3. **Configure Router1**:
   - **Internet Connection**:
     - Go to **Quick Setup** or the **Internet** settings section.
     - Select **DHCP** mode. This allows Router1 to automatically get an IP address from the modem (likely in the `192.168.1.x` range).
   - **WiFi Settings**:
     - Set a unique **SSID** (network name) and a strong **password** for Router1’s WiFi.
     - Save these details, as Router2 will need them to connect wirelessly.
   - **LAN Settings**:
     - Ensure Router1’s LAN IP is different from the modem’s IP. By default, it’s likely `192.168.0.1`, which is fine since the modem is `192.168.1.1`.
     - Confirm that **DHCP** is enabled on Router1. This allows Router1 to assign IP addresses (e.g., `192.168.0.x`) to devices connected to it, including Router2.
   - Save the settings and reboot Router1 if prompted.

---

### **Step 3: Set Up Router2 as a Wireless Bridge**
1. **Access Router2’s Web Interface**:
   - Connect a computer or smartphone to Router2’s default WiFi network or via Ethernet.
   - Open a web browser and type `http://tplinkwifi.net` or `192.168.0.1`.
   - Log in with the default credentials (or your custom ones).

2. **Configure Router2 in Wireless Bridge Mode**:
   - Look for a mode like **Wireless AP Bridge**, **WDS**, or **Repeater** in the settings (likely under **Operation Mode** or **Wireless** settings).
   - Select **Wireless AP Bridge** (or WDS/Repeater if that’s what’s available).
   - **Connect to Router1’s WiFi**:
     - Scan for available networks and select Router1’s SSID.
     - Enter Router1’s WiFi password.
     - Ensure Router2 uses the same wireless channel as Router1 for compatibility (e.g., if Router1 is on Channel 6, set Router2 to Channel 6).
   - **LAN IP Setting**:
     - Change Router2’s LAN IP to avoid conflicts with Router1. For example, set it to `192.168.0.2` (since Router1 is likely `192.168.0.1`).
     - **Disable DHCP** on Router2. Router1 will handle IP assignments for all devices.
   - Save the settings and reboot Router2. It should now connect wirelessly to Router1.

---

### **Step 4: Test the Setup**
1. **Verify Router2’s Connection**:
   - After rebooting, check Router2’s interface to confirm it’s connected to Router1’s WiFi.
2. **Connect a Device to Router2**:
   - Use a smartphone, laptop, or other device to connect to Router2’s WiFi (it may use the same SSID as Router1, depending on the mode).
   - Check that the device gets an IP address from Router1 (e.g., `192.168.0.x`).
   - Test internet access by browsing a website.

---

### **Final Configuration Summary**
- **Modem**: IP `192.168.1.1`, provides internet and WiFi.
- **Router1**: 
  - WAN: Connected to modem via cable, set to **DHCP** (gets IP from modem, e.g., `192.168.1.x`).
  - LAN: IP `192.168.0.1`, **DHCP enabled** to assign IPs to devices.
  - WiFi: Custom SSID and password.
- **Router2**: 
  - Mode: **Wireless AP Bridge** (or WDS/Repeater), connected wirelessly to Router1’s WiFi.
  - LAN IP: `192.168.0.2`, **DHCP disabled**.

---

### **Troubleshooting Tips**
- **Router2 Not Connecting Wirelessly**:
  - Double-check Router1’s SSID, password, and channel settings in Router2’s configuration.
  - If **Wireless AP Bridge** isn’t available, try **WDS** or **Repeater** mode. Refer to the TP-Link AX3000 manual for supported modes.
- **No Internet on Router2**:
  - Ensure Router1’s DHCP is working and Router2’s DHCP is off.
  - Verify Router2 is successfully bridging to Router1.
- **Double NAT Concerns**:
  - Since your modem has WiFi and Router1 acts as a router, you might have double NAT (modem and Router1 both assigning IPs). This is usually fine for basic use but could affect some applications (e.g., gaming). If needed, set the modem to **bridge mode** (consult your modem’s manual), though this may disable its WiFi.

With this setup, Router2 will extend your network wirelessly from Router1, and devices connected to either router should access the internet through the modem. Let me know if you need further assistance!

---

If you decide to use a fixed (static) IP address for the first router (Router1) instead of relying on DHCP, you'll need to manually configure its WAN settings to communicate with your modem. Here’s what you should configure for the IP address, DNS, subnet mask, and gateway:

---

### **Assumptions**
- Your modem has an IP address of `192.168.1.1` and uses the subnet `192.168.1.0/24` (subnet mask `255.255.255.0`).
- The modem has a DHCP range (e.g., `192.168.1.2` to `192.168.1.100`) that assigns IP addresses to connected devices.

If your modem uses a different IP or subnet, adjust the values accordingly.

---

### **WAN Settings for Router1**
These settings configure how Router1 connects to the modem:

1. **IP Address**
   - Choose a static IP within the modem’s subnet (`192.168.1.0/24`) but **outside the modem’s DHCP range** to avoid conflicts.
   - Example: If the modem’s DHCP range is `192.168.1.2` to `192.168.1.100`, you can use **`192.168.1.101`**.
   - This ensures Router1 has a unique, fixed address on the modem’s network.

2. **Subnet Mask**
   - Set this to match the modem’s subnet mask, which is typically **`255.255.255.0`**.
   - This defines the network range as `192.168.1.0` to `192.168.1.255`.

3. **Default Gateway**
   - Set this to the modem’s IP address, which is **`192.168.1.1`**.
   - The gateway is the device (your modem) that Router1 uses to access the internet.

4. **DNS Servers**
   - You have two options:
     - Use the modem’s IP: **`192.168.1.1`**. This lets the modem handle DNS requests.
     - Use public DNS servers: **`8.8.8.8`** (Google) and **`8.8.4.4`** (Google secondary). These are reliable and often faster.
   - Recommendation: Start with `192.168.1.1`. If you experience DNS issues, switch to `8.8.8.8` and `8.8.4.4`.

---

### **Example Configuration**
Here’s what your Router1 WAN settings might look like:

- **IP Address**: `192.168.1.101`
- **Subnet Mask**: `255.255.255.0`
- **Default Gateway**: `192.168.1.1`
- **DNS Server**: `192.168.1.1` (or `8.8.8.8` and `8.8.4.4`)

---

### **Additional Notes**
- **Check Modem Settings**: Log into your modem (usually at `192.168.1.1`) to confirm its IP, subnet mask, and DHCP range. Adjust Router1’s static IP if needed.
- **LAN Settings for Router1**: To avoid conflicts, configure Router1’s LAN network on a different subnet, like `192.168.0.1` with a subnet mask of `255.255.255.0`. Enable DHCP on Router1 to assign IPs (e.g., `192.168.0.2` to `192.168.0.254`) to devices connected to it.
- **Testing**: After applying these settings, ensure Router1 can access the internet. If not, double-check the IP (no conflicts), gateway, and DNS values.

This configuration gives Router1 a fixed IP on the modem’s network, ensuring consistent connectivity. Let me know if you need help with additional routers or specific modem details!