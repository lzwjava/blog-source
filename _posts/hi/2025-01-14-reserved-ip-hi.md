---
audio: false
generated: false
image: false
lang: hi
layout: post
title: डिजिटलओशन रिजर्व्ड आईपी प्रबंधित करना
translated: true
type: post
---

यह एक सामान्य चुनौती है कि सर्वर के IP पते Great Firewall (GFW) द्वारा आसानी से ब्लॉक किए जा सकते हैं। यह विशेष रूप से क्लाउड सर्वर के लिए सच है। इससे निपटने के लिए एक रणनीति यह है कि DigitalOcean के आरक्षित IP का उपयोग किया जाए और जब वर्तमान IP ब्लॉक हो जाए तो इसे अपने droplet पर पुनः असाइन किया जाए। यह पोस्ट इस प्रक्रिया को स्वचालित करने के लिए एक Python स्क्रिप्ट का परिचय देती है। यह स्क्रिप्ट [GitHub](https://github.com/lzwjava/auto-ss-config) पर भी उपलब्ध है।

स्क्रिप्ट आपको यह करने की अनुमति देती है:

*   जांचें कि क्या एक आरक्षित IP किसी विशिष्ट droplet को असाइन किया गया है।
*   यदि वर्तमान IP ब्लॉक हो गया है तो एक नया आरक्षित IP droplet को पुनः असाइन करें।
*   जांचें कि आरक्षित IP पर पोर्ट 80 खुला है या नहीं (यह जांचने का एक सरल तरीका है कि IP काम कर रहा है या नहीं)।

यहां Python स्क्रिप्ट दी गई है:

```python
import socket
import os
import argparse
import json
import requests
import time

# DigitalOcean API हेडर प्राप्त करने के लिए फ़ंक्शन
def get_digitalocean_headers():
    api_key = os.environ.get("DO_API_KEY")
    if not api_key:
        print("Error: DO_API_KEY environment variables में नहीं मिला।")
        return None
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

# DigitalOcean से सभी आरक्षित IP प्राप्त करने के लिए फ़ंक्शन
def fetch_reserved_ips():
    headers = get_digitalocean_headers()
    if not headers:
        return None
    try:
        url = "https://api.digitalocean.com/v2/reserved_ips"
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        reserved_ips_data = resp.json().get("reserved_ips", [])
        with open('response.json', 'w') as f:
            json.dump(reserved_ips_data, f, indent=4) # डिबगिंग के लिए प्रतिक्रिया को एक फ़ाइल में सहेजें
        return reserved_ips_data
    except requests.exceptions.RequestException as e:
        print(f"आरक्षित IP पता प्राप्त करने में त्रुटि: {e}")
        return None

# एक droplet से आरक्षित IP को अनअसाइन करने के लिए फ़ंक्शन
def unassign_ip_from_droplet(ip_address, droplet_id, droplet_name):
    headers = get_digitalocean_headers()
    if not headers:
        return False
    
    try:
        url = f"https://api.digitalocean.com/v2/reserved_ips/{ip_address}"
        resp = requests.delete(url, headers=headers)
        resp.raise_for_status()
        print(f"IP {ip_address} को droplet {droplet_name} से सफलतापूर्वक हटा दिया गया।")
        return True
    except requests.exceptions.RequestException as e:
        print(f"IP {ip_address} को droplet {droplet_name} से हटाने में त्रुटि: {e}")
        return False

# एक droplet को आरक्षित IP असाइन करने के लिए फ़ंक्शन
def assign_ip_to_droplet(ip_address, droplet_id, droplet_name):
    headers = get_digitalocean_headers()
    if not headers:
        return False
    
    try:
        url = f"https://api.digitalocean.com/v2/reserved_ips/{ip_address}/actions"
        req = {
            "type": "assign",
            "droplet_id": droplet_id
        }
        resp = requests.post(url, headers=headers, json=req)
        resp.raise_for_status()
        print(f"IP {ip_address} को droplet {droplet_name} को सफलतापूर्वक असाइन किया गया।")
        return True
    except requests.exceptions.RequestException as e:
        print(f"IP {ip_address} को droplet {droplet_name} को असाइन करने में त्रुटि: {e}")
        return False

# आरक्षित IP को प्रोसेस करने, असाइनमेंट की जांच करने और यदि आवश्यक हो तो पुनः असाइन करने के लिए फ़ंक्शन
def process_reserved_ips(reserved_ips, droplet_name, only_check=False):
    if not reserved_ips:
        print("आपके खाते में कोई आरक्षित IP नहीं मिला।")
        return None

    for reserved_ip in reserved_ips:
        ip_address = reserved_ip.get("ip")
        if not ip_address:
            print("एक आरक्षित IP के लिए कोई IP पता नहीं मिला।")
            continue

        droplet = reserved_ip.get("droplet", None)
        if droplet_name:
            if droplet and droplet.get("name") == droplet_name:
                print(f"आरक्षित IP {ip_address} droplet: {droplet_name} को असाइन किया गया है।")
                if only_check:
                    if check_port_80(ip_address):
                        print(f"Port 80 {ip_address} पर droplet {droplet_name} के लिए खुला है।")
                    else:
                        print(f"Port 80 {ip_address} पर droplet {droplet_name} के लिए बंद है।")
                    return ip_address
                droplet_id = droplet.get("id")
                if droplet_id:
                    if unassign_ip_from_droplet(ip_address, droplet_id, droplet_name):
                        # अनअसाइन करने के बाद एक नया IP असाइन करने का प्रयास करें
                        
                        new_ip = create_new_reserved_ip(droplet_id)
                        if new_ip:
                            print("नया IP असाइन करने से पहले 10 सेकंड के लिए सो रहा है...")
                            time.sleep(10)
                            if assign_ip_to_droplet(new_ip, droplet_id, droplet_name):
                                print(f"नया IP {new_ip} को droplet {droplet_name} को सफलतापूर्वक असाइन किया गया।")
                            else:
                                print(f"नया IP {new_ip} को droplet {droplet_name} को असाइन करने में विफल।")
                        else:
                            print("असाइन करने के लिए कोई उपलब्ध IP नहीं है।")
                    
                else:
                    print(f"IP {ip_address} को अनअसाइन नहीं किया जा सका क्योंकि droplet ID नहीं मिला।")
                return None
            elif droplet:
                print(f"आरक्षित IP {ip_address} droplet: {droplet_name} को असाइन नहीं किया गया है।")
            else:
                print(f"आरक्षित IP: {ip_address} को कोई droplet असाइन नहीं किया गया है।")
        else:
            return ip_address
    return None

# एक नया आरक्षित IP बनाने के लिए फ़ंक्शन
def create_new_reserved_ip(droplet_id):
    headers = get_digitalocean_headers()
    if not headers:
        print("DigitalOcean हेडर प्राप्त करने में विफल।")
        return False
    try:
        url = "https://api.digitalocean.com/v2/reserved_ips"
        req = {
            "region": "sgp1", # यदि आवश्यक हो तो आप क्षेत्र बदल सकते हैं
        }
        print(f"Droplet ID: {droplet_id} के लिए एक नया आरक्षित IP बनाने का प्रयास कर रहा है।")
        resp = requests.post(url, headers=headers, json=req)
        resp.raise_for_status()
        new_ip = resp.json().get("reserved_ip", {}).get("ip")
        print(f"नया आरक्षित IP सफलतापूर्वक बनाया गया: {new_ip}")
        return new_ip
    except requests.exceptions.RequestException as e:
        print(f"नया आरक्षित IP बनाने में त्रुटि: {e}")
        return False

# एक IP पते पर पोर्ट 80 खुला है या नहीं, यह जांचने के लिए फ़ंक्शन
def check_port_80(ip_address):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((ip_address, 80))
            return True
    except Exception:
        return False

# आरक्षित IP प्राप्त करने के लिए मुख्य फ़ंक्शन
def get_reserved_ip(droplet_name=None, only_check=False):
    reserved_ips = fetch_reserved_ips()
    if reserved_ips is None:
        return None
    return process_reserved_ips(reserved_ips, droplet_name, only_check)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="DigitalOcean आरक्षित IP पता प्राप्त करें।")
    parser.add_argument("--droplet-name", required=True, help="यह जांचने के लिए droplet का नाम कि आरक्षित IP इस droplet को असाइन किया गया है या नहीं।")
    parser.add_argument("--only-check", action="store_true", help="केवल जांचें कि IP droplet को असाइन किया गया है या नहीं, पुनः असाइन न करें।")
    args = parser.parse_args()

    reserved_ip = get_reserved_ip(args.droplet_name, args.only_check)
    if reserved_ip:
        print(f"आरक्षित IP पता है: {reserved_ip}")
```

**व्याख्या:**

1.  **लाइब्रेरी आयात करें:** नेटवर्क ऑपरेशन, पर्यावरण चर, तर्क पार्सिंग, JSON हैंडलिंग, HTTP अनुरोध और समय विलंब के लिए आवश्यक लाइब्रेरी आयात करें।
2.  **`get_digitalocean_headers()`:** पर्यावरण चर से DigitalOcean API कुंजी प्राप्त करें और API अनुरोध के लिए आवश्यक हेडर बनाएं।
3.  **`fetch_reserved_ips()`:** API का उपयोग करके आपके DigitalOcean खाते से जुड़े सभी आरक्षित IP प्राप्त करें। यह डिबगिंग के लिए कच्ची प्रतिक्रिया को `response.json` में भी सहेजता है।
4.  **`unassign_ip_from_droplet()`:** एक निर्दिष्ट droplet से दिए गए आरक्षित IP को अनअसाइन करें।
5.  **`assign_ip_to_droplet()`:** एक निर्दिष्ट droplet को दिए गए आरक्षित IP को असाइन करें।
6.  **`process_reserved_ips()`:** यह मुख्य तर्क है:
    *   यह सभी आरक्षित IP के माध्यम से पुनरावृत्त करता है।
    *   यदि `droplet_name` प्रदान किया गया है, तो यह जांचता है कि IP उस droplet को असाइन किया गया है या नहीं।
    *   यदि `only_check` सत्य है, तो यह जांचता है कि पोर्ट 80 खुला है और IP लौटाता है।
    *   यदि `only_check` सत्य नहीं है, तो यह वर्तमान IP को अनअसाइन करता है, एक नया बनाता है और नए IP को droplet को असाइन करता है।
7.  **`create_new_reserved_ip()`:** `sgp1` क्षेत्र में एक नया आरक्षित IP बनाता है (आप इसे बदल सकते हैं)।
8.  **`check_port_80()`:** दिए गए IP पते पर पोर्ट 80 खुला है या नहीं, यह जांचता है। यह जांचने का एक सरल तरीका है कि IP पहुंच योग्य है या नहीं।
9.  **`get_reserved_ip()`:** आरक्षित IP प्राप्त करने और प्रोसेस करने की प्रक्रिया को संचालित करता है।
10. **`if __name__ == '__main__':`:** कमांड-लाइन तर्क (`--droplet-name` और `--only-check`) को पार्स करता है और स्क्रिप्ट को निष्पादित करने के लिए `get_reserved_ip` को कॉल करता है।

**उपयोग कैसे करें:**

1.  **DigitalOcean API कुंजी सेट करें:** अपने DigitalOcean API कुंजी को `DO_API_KEY` पर्यावरण चर में सेट करें।
2.  **स्क्रिप्ट चलाएं:**
    *   यह जांचने के लिए कि क्या एक IP droplet को असाइन किया गया है और पोर्ट 80 खुला है या नहीं:
        ```bash
        python your_script_name.py --droplet-name your_droplet_name --only-check
        ```
    *   एक नया IP droplet को पुनः असाइन करने के लिए:
        ```bash
        python your_script_name.py --droplet-name your_droplet_name
        ```

यह स्क्रिप्ट आरक्षित IP प्रबंधन के लिए एक बुनियादी ढांचा प्रदान करती है। आप इसे अपनी विशिष्ट आवश्यकताओं के आधार पर और विस्तारित कर सकते हैं।