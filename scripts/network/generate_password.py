#!/usr/bin/env python3
"""
WiFi Password Generator Script
Scans WiFi networks, lets user select one, generates suggested passwords using LLM, and saves to @tmp dir.
This script requires online access for LLM. Use a separate offline script to attempt connections with saved passwords.
"""

import os
import sys
from get_wifi_list import get_wifi_list
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from scripts.llm.openrouter_client import call_openrouter_api

# Ensure @tmp directory exists
TMP_DIR = 'tmp'
os.makedirs(TMP_DIR, exist_ok=True)

def parse_wifi_list(wifi_output):
    """
    Parse the output from get_wifi_list to extract SSIDs and BSSIDs.
    Returns a list of dicts with 'index', 'ssid', 'bssid', 'full_line'.
    Assumes format like 'SSID: name, BSSID: mac_address'
    """
    networks = []
    lines = wifi_output.split('\n')
    for i, line in enumerate(lines):
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
                networks.append({
                    'index': len(networks) + 1,
                    'ssid': ssid,
                    'bssid': bssid,
                    'full_line': line
                })
            # Handle potential sub-lines if needed
            while i + 1 < len(lines) and lines[i + 1].strip().startswith('  '):
                networks[-1]['full_line'] += '\n' + lines[i + 1]
                i += 1
    return networks

def generate_password_suggestions(ssid, num_suggestions=10, model="deepseek-v3.2"):
    """
    Use OpenRouter LLM to generate suggested passwords for the given SSID.
    """
    prompt = f"Suggest {num_suggestions} possible passwords for a WiFi network named '{ssid}'. Make them plausible based on common patterns, the name, or defaults. List them numbered, one per line, no explanations."
    try:
        response = call_openrouter_api(prompt, model=model)
        # Clean up response to extract just the list
        lines = [line.strip() for line in response.split('\n') if line.strip() and line[0].isdigit()]
        passwords = [line.split('.', 1)[1].strip() if '.' in line else line for line in lines[:num_suggestions]]
        return passwords
    except Exception as e:
        print(f"Error generating passwords: {e}")
        return []

def save_passwords_to_file(bssid, passwords):
    """
    Save the list of passwords to a file in @tmp dir using BSSID.
    """
    filename = os.path.join(TMP_DIR, f"{bssid}_passwords.txt")
    with open(filename, 'w') as f:
        for pwd in passwords:
            f.write(f"{pwd}\n")
    print(f"Passwords saved to: {filename}")
    return filename

def main():
    print("=== WiFi Password Generator ===")
    print()

    # Get WiFi list
    print("Scanning for available WiFi networks...")
    wifi_output = get_wifi_list()
    print("Available WiFi Networks:")
    if wifi_output.startswith("No WiFi"):
        print(f"  {wifi_output}")
        sys.exit(1)

    # Parse and display numbered list
    networks = parse_wifi_list(wifi_output)
    if not networks:
        print("No networks found.")
        sys.exit(1)

    for net in networks:
        print(f"{net['index']}. {net['full_line']}")

    # User input
    try:
        choice = int(input(f"\nSelect a network (1-{len(networks)}): "))
        if 1 <= choice <= len(networks):
            selected = networks[choice - 1]
            ssid = selected['ssid']
            bssid = selected['bssid']
            print(f"\nSelected: {ssid} (BSSID: {bssid})")
        else:
            print("Invalid choice.")
            sys.exit(1)
    except ValueError:
        print("Invalid input.")
        sys.exit(1)

    # Generate passwords
    print(f"\nGenerating 10 password suggestions for '{ssid}'...")
    passwords = generate_password_suggestions(ssid)

    if passwords:
        print("Suggested passwords:")
        for i, pwd in enumerate(passwords, 1):
            print(f"{i}. {pwd}")
        # Save to file using BSSID
        save_passwords_to_file(bssid, passwords)
    else:
        print("Failed to generate passwords.")

    print("\nUse a separate offline script to read this file and attempt connections.")

if __name__ == "__main__":
    main()