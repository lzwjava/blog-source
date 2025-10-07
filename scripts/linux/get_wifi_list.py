#!/usr/bin/env python3
"""
WiFi Scanner Script for Linux Systems
Scans and displays available WiFi networks with signal strength, security information, and other details.
"""

import subprocess
import sys

def run_command(cmd, fallback=None):
    """Run a command and return its output, or fallback if it fails."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return fallback
    except (subprocess.SubprocessError, FileNotFoundError, subprocess.TimeoutExpired):
        return fallback

def get_wifi_interfaces():
    """Get available WiFi network interfaces."""
    interfaces = []
    
    # Common WiFi interface commands
    commands = [
        "iw dev | grep Interface | awk '{print $2}'",
        "nmcli device | grep wifi | awk '{print $1}'",
        "ls /sys/class/net | xargs -I {} sh -c 'test -d /sys/class/net/{}/wireless && echo {}'"
    ]
    
    for cmd in commands:
        output = run_command(cmd)
        if output:
            interfaces.extend([iface.strip() for iface in output.split('\n') if iface.strip()])
    
    return list(set(interfaces))  # Remove duplicates

def scan_wifi_with_nmcli():
    """Scan WiFi networks using nmcli."""
    try:
        # Rescan and list networks
        run_command("nmcli device wifi rescan", "")
        result = run_command("nmcli -f SSID,BSSID,MODE,CHAN,RATE,SIGNAL,SECURITY device wifi list")
        if result and "SSID" in result:
            return result
    except:
        pass
    return None

def scan_wifi_with_iw():
    """Scan WiFi networks using iw command."""
    interfaces = get_wifi_interfaces()
    if not interfaces:
        return None
    
    nets = []
    for interface in interfaces:
        try:
            scan_result = run_command(f"sudo iw dev {interface} scan")
            if scan_result:
                nets.append(f"Interface: {interface}\n{scan_result}")
        except:
            continue
    
    return '\n\n'.join(nets) if nets else None

def scan_wifi_with_iwlist():
    """Scan WiFi networks using iwlist (legacy)."""
    interfaces = get_wifi_interfaces()
    if not interfaces:
        return None
    
    nets = []
    for interface in interfaces:
        try:
            scan_result = run_command(f"sudo iwlist {interface} scan")
            if scan_result:
                nets.append(f"Interface: {interface}\n{scan_result}")
        except:
            continue
    
    return '\n\n'.join(nets) if nets else None

def parse_nmcli_output(output):
    """Parse nmcli output into structured format."""
    lines = output.strip().split('\n')
    if len(lines) < 2:
        return []
    
    header = lines[0].lower()
    networks = []
    
    for line in lines[1:]:
        if not line.strip():
            continue
        
        # Split by multiple spaces and clean up
        parts = [part.strip() for part in line.split() if part.strip()]
        if len(parts) >= 6:
            network = {
                'ssid': parts[0],
                'bssid': parts[1] if len(parts) > 1 else 'N/A',
                'mode': parts[2] if len(parts) > 2 else 'N/A',
                'channel': parts[3] if len(parts) > 3 else 'N/A',
                'rate': parts[4] if len(parts) > 4 else 'N/A',
                'signal': parts[5] if len(parts) > 5 else 'N/A',
                'security': ' '.join(parts[6:]) if len(parts) > 6 else 'N/A'
            }
            networks.append(network)
    
    return networks

def get_wifi_list():
    """Get comprehensive WiFi network information."""
    wifi_info = []
    
    # Try nmcli first (most modern and user-friendly)
    nmcli_result = scan_wifi_with_nmcli()
    if nmcli_result:
        networks = parse_nmcli_output(nmcli_result)
        if networks:
            for net in networks:
                wifi_info.append(
                    f"SSID: {net['ssid']}, BSSID: {net['bssid']}, "
                    f"Mode: {net['mode']}, Channel: {net['channel']}, "
                    f"Rate: {net['rate']}, Signal: {net['signal']}%, "
                    f"Security: {net['security']}"
                )
    
    # Fallback to iw command if nmcli fails
    if not wifi_info:
        iw_result = scan_wifi_with_iw()
        if iw_result:
            wifi_info.append(f"Raw IW scan output:\n{iw_result}")
    
    # Final fallback to iwlist
    if not wifi_info:
        iwlist_result = scan_wifi_with_iwlist()
        if iwlist_result:
            wifi_info.append(f"Raw IWLIST scan output:\n{iwlist_result}")
    
    interfaces = get_wifi_interfaces()
    if interfaces:
        wifi_info.append(f"Detected WiFi interfaces: {', '.join(interfaces)}")
    
    if not wifi_info:
        return "No WiFi scanning method available or no networks found"
    
    return '\n'.join(wifi_info)

def check_current_connection():
    """Check current WiFi connection status."""
    try:
        # Check current connection with nmcli
        status = run_command("nmcli device status | grep wifi | head -3")
        if status:
            return f"Network Status:\n{status}"
        
        # Alternative with iwconfig
        iwconfig = run_command("iwconfig")
        if iwconfig:
            return f"IW Config:\n{iwconfig}"
    except:
        pass
    
    return None

def main():
    """Main function to scan and display WiFi networks."""
    print("=== WiFi Network Scanner ===")
    print()
    
    # Check current connection
    current = check_current_connection()
    if current:
        print(current)
        print()
    
    # Scan available networks
    print("Scanning for available WiFi networks...")
    wifi_list = get_wifi_list()
    
    print("Available WiFi Networks:")
    if wifi_list.startswith("No WiFi"):
        print(f"  {wifi_list}")
    else:
        # Indent multi-line output
        for line in wifi_list.split('\n'):
            print(f"  {line}")
    print()

if __name__ == "__main__":
    main()