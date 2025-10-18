#!/usr/bin/env python3
"""
WiFi Utility Functions for Linux Systems
Utility functions for scanning, parsing, and managing WiFi connections.
"""

import subprocess
import csv
import os
import time
from datetime import datetime

from scripts.network.wifi_util import scan_wifi_with_iw, scan_wifi_with_iwlist




def parse_nmcli_output(output):
    """Parse nmcli output into structured format."""
    lines = output.strip().split('\n')
    if len(lines) < 2:
        return []

    networks = []

    for line in lines[1:]:
        if not line.strip():
            continue

        # More robust parsing to handle multi-word field values
        # Fields: SSID BSSID MODE CHAN FREQ RATE BANDWIDTH SIGNAL BARS SECURITY WPA-FLAGS RSN-FLAGS ACTIVE IN-USE

        # Use regex to split on multiple spaces while preserving quotes and handling special characters
        import re
        # Split on 2 or more spaces to separate fields
        parts = re.split(r'\s{2,}', line.strip())

        try:
            network = {
                'ssid': parts[0] if len(parts) > 0 else 'N/A',
                'bssid': parts[1] if len(parts) > 1 else 'N/A',
                'mode': parts[2] if len(parts) > 2 else 'N/A',
                'channel': parts[3] if len(parts) > 3 else 'N/A',
                'frequency': parts[4] if len(parts) > 4 else 'N/A',
                'rate': parts[5] if len(parts) > 5 else 'N/A',
                'bandwidth': parts[6] if len(parts) > 6 else 'N/A',
                'signal': parts[7] if len(parts) > 7 else 'N/A',
                'bars': parts[8] if len(parts) > 8 else 'N/A',
                'security': parts[9] if len(parts) > 9 else 'N/A',
                'wpa_flags': parts[10] if len(parts) > 10 else 'N/A',
                'rsn_flags': parts[11] if len(parts) > 11 else 'N/A',
                'active': parts[12] if len(parts) > 12 else 'N/A',
                'in_use': parts[13] if len(parts) > 13 else 'N/A'
            }
            networks.append(network)
        except IndexError:
            # If parsing fails, skip this network
            continue

    return networks

def get_wifi_list():
    """Get comprehensive WiFi network information as parsed dictionaries."""
    # Try nmcli first (most modern and user-friendly)
    nmcli_result = scan_wifi_with_nmcli()
    if nmcli_result:
        networks = parse_nmcli_output(nmcli_result)
        if networks:
            return networks

    # Fallback to iw command if nmcli fails - currently not parsed
    iw_result = scan_wifi_with_iw()
    if iw_result:
        # For now, return empty list for iw (could be enhanced to parse later)
        return []

    # Final fallback to iwlist - currently not parsed
    iwlist_result = scan_wifi_with_iwlist()
    if iwlist_result:
        # For now, return empty list for iwlist (could be enhanced to parse later)
        return []

    # No WiFi available
    return []

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

def test_wifi_connection(ssid, password="88888888", timeout=10):
    """Test WiFi connection with given password."""
    interface = get_wifi_interfaces()
    if not interface:
        return False
    interface = interface[0]  # Use first available interface
    
    try:
        # Try to connect using nmcli
        cmd = f"nmcli dev wifi connect '{ssid}' password '{password}' iface {interface}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        
        if result.returncode == 0:
            # Connection successful
            time.sleep(2)  # Wait for connection to stabilize
            # Test connectivity by pinging google
            ping_test = subprocess.run("ping -c 1 -W 3 8.8.8.8", shell=True, capture_output=True, text=True)
            if ping_test.returncode == 0:
                return True
        
        return False
    except (subprocess.SubprocessError, subprocess.TimeoutExpired):
        return False
    finally:
        # Always disconnect after test
        try:
            subprocess.run(f"nmcli dev disconnect {interface}", shell=True, capture_output=True, timeout=5)
        except:
            pass

def save_successful_connections(networks, output_file="tmp/wifi.csv"):
    """Save successful WiFi connections to CSV file."""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Check if file exists to write header only if new file
    is_new_file = not os.path.exists(output_file)
    
    with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['ssid', 'bssid', 'mode', 'channel', 'frequency', 'rate', 'bandwidth', 'signal', 'bars', 'security', 'active', 'in_use', 'password', 'test_time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if is_new_file:
            writer.writeheader()
        
        for net in networks:
            row = net.copy()
            row['password'] = '88888888'
            row['test_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow(row)