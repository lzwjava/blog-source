#!/usr/bin/env python3
"""
Save WiFi List Script
Scans WiFi networks and saves the parsed list to tmp/wifi_list.json.
"""

import os
import json
from get_wifi_list import get_wifi_list

# Ensure @tmp directory exists
TMP_DIR = 'tmp'
os.makedirs(TMP_DIR, exist_ok=True)

def parse_wifi_list(wifi_output):
    """
    Parse the output from get_wifi_list to extract SSIDs and BSSIDs.
    Returns a list of dicts with 'ssid', 'bssid', 'full_line'.
    Assumes format like 'SSID: name, BSSID: mac_address'
    """
    networks = []
    lines = wifi_output.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('SSID: '):
            parts = [p.strip() for p in line.split(',')]
            ssid = None
            bssid = None
            for part in parts:
                if part.startswith('SSID: '):
                    ssid = part.split('SSID: ', 1)[1]
                elif part.startswith('BSSID: '):
                    bssid = part.split('BSSID: ', 1)[1].replace(':', '_')
            if ssid:
                full_line = line
                # Handle potential sub-lines
                i += 1
                while i < len(lines) and lines[i].strip().startswith('  '):
                    full_line += '\n' + lines[i]
                    i += 1
                networks.append({
                    'ssid': ssid,
                    'bssid': bssid,
                    'full_line': full_line
                })
            continue
        i += 1
    return networks

def main():
    print("=== Save WiFi List ===")
    print()

    # Get WiFi list
    print("Scanning for available WiFi networks...")
    wifi_output = get_wifi_list()
    if wifi_output.startswith("No WiFi"):
        print(f"No WiFi networks found: {wifi_output}")
        return

    # Parse
    networks = parse_wifi_list(wifi_output)
    if not networks:
        print("No networks found.")
        return

    # Save to JSON
    filename = os.path.join(TMP_DIR, "wifi_list.json")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(networks, f, ensure_ascii=False, indent=2)
    print(f"WiFi list saved to: {filename}")
    print(f"Found {len(networks)} networks.")

if __name__ == "__main__":
    main()