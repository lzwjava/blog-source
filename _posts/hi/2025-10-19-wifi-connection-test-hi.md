---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: स्वचालित वाई-फ़ाई कनेक्शन परीक्षण स्क्रिप्ट
translated: true
type: note
---

```python
import subprocess
import time
import os

def get_wifi_interfaces():
    """वाईफाई इंटरफेस खोजने में सहायक।"""
    try:
        result = subprocess.run("nmcli dev status | grep wifi | awk '{print $1}'", shell=True, capture_output=True, text=True)
        interfaces = [iface.strip() for iface in result.stdout.split('\n') if iface.strip()]
        return interfaces
    except:
        return []

def test_wifi_connection(ssid, password="88888888", timeout=30):
    """वाईफाई कनेक्शन को गैर-इंटरैक्टिव तरीके से टेस्ट करें। टपल लौटाता है (सफलता: बूल, त्रुटि: स्ट्र)।"""
    interfaces = get_wifi_interfaces()
    if not interfaces:
        return False, "कोई वाईफाई इंटरफेस उपलब्ध नहीं"
    interface = interfaces[0]  # पहला उपलब्ध इंटरफेस उपयोग करें
    con_name = f"test-{ssid}"  # टेस्ट प्रोफाइल के लिए अद्वितीय नाम
    
    # कमांड्स
    delete_cmd = f"nmcli connection delete '{con_name}'"
    add_cmd = (
        f"nmcli connection add type wifi con-name '{con_name}' "
        f"ifname {interface} ssid '{ssid}' "
        f"wifi-sec.key-mgmt wpa-psk wifi-sec.psk '{password}' "
        f"-- autoconnect no"
    )
    up_cmd = f"nmcli connection up '{con_name}'"
    disconnect_cmd = f"nmcli device disconnect {interface}"
    
    try:
        # कोई भी मौजूदा प्रोफाइल हटाएं (अनुपस्थित होने पर एरर दबाएं)
        subprocess.run(delete_cmd, shell=True, capture_output=True, timeout=5)
        time.sleep(1)
        
        # एम्बेडेड पासवर्ड के साथ नई प्रोफाइल बनाएं (गैर-इंटरैक्टिव)
        add_result = subprocess.run(add_cmd, shell=True, capture_output=True, text=True, timeout=10)
        if add_result.returncode != 0:
            error = add_result.stderr.strip() or add_result.stdout.strip() or "कनेक्शन प्रोफाइल बनाने में विफल"
            return False, f"प्रोफाइल निर्माण त्रुटि: {error}"
        
        # प्रोफाइल सक्रिय करें (गैर-इंटरैक्टिव)
        up_result = subprocess.run(up_cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        if up_result.returncode != 0:
            error = up_result.stderr.strip() or up_result.stdout.strip() or "सक्रियकरण विफल"
            if "secrets were required" in error.lower():
                error = "गलत पासवर्ड या प्रमाणीकरण विफल"
            elif "activation failed" in error.lower():
                error = f"कनेक्शन सक्रियकरण विफल: {error}"
            return False, f"nmcli त्रुटि: {error}"
        
        # स्थिरीकरण के लिए प्रतीक्षा करें
        time.sleep(2)
        
        # पिंग के साथ इंटरनेट टेस्ट करें
        ping_test = subprocess.run("ping -c 1 -W 3 8.8.8.8", shell=True, capture_output=True, text=True, timeout=5)
        if ping_test.returncode == 0:
            return True, None
        else:
            error = ping_test.stderr.strip() or "पिंग विफल"
            return False, f"कनेक्टेड लेकिन इंटरनेट नहीं: {error}"
        
    except subprocess.TimeoutExpired:
        return False, f"ऑपरेशन टाइमआउट {timeout} सेकंड के बाद"
    except subprocess.SubprocessError as e:
        return False, f"कमांड त्रुटि: {str(e)}"
    finally:
        # क्लीनअप: कनेक्शन डाउन करें और प्रोफाइल हटाएं
        try:
            subprocess.run(f"nmcli connection down '{con_name}'", shell=True, capture_output=True, timeout=5)
            subprocess.run(delete_cmd, shell=True, capture_output=True, timeout=5)
            subprocess.run(disconnect_cmd, shell=True, capture_output=True, timeout=5)
        except subprocess.SubprocessError:
            pass  # क्लीनअप समस्याओं को नजरअंदाज करें
```