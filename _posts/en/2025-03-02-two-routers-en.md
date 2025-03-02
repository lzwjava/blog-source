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