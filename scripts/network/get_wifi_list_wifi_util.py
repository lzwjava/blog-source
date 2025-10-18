#!/usr/bin/env python3
"""
WiFi Command Utility Functions for Linux Systems
WiFi-specific command execution functions using iw, iwlist, and related tools.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.network.get_wifi_list_util import run_command, get_wifi_interfaces

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