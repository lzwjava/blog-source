#!/usr/bin/env python3
"""
WiFi Command Utility Functions for Linux Systems
WiFi-specific command execution functions using iw, iwlist, and related tools.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import subprocess

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
        result = run_command("nmcli -f SSID,BSSID,MODE,CHAN,FREQ,RATE,BANDWIDTH,SIGNAL,BARS,SECURITY,WPA-FLAGS,RSN-FLAGS,ACTIVE,IN-USE device wifi list")
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