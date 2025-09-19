---
audio: false
generated: false
image: false
lang: ar
layout: post
title: إدارة عناوين IP المحجوزة في DigitalOcean
translated: true
---

من التحديات الشائعة أن عناوين IP الخاصة بالخوادم يمكن أن يتم حظرها بسهولة من خلال الجدار الناري العظيم (GFW). هذا ينطبق بشكل خاص على خوادم السحابة. للتخفيف من هذا، إحدى الاستراتيجيات هي استخدام عناوين IP المحجوزة من DigitalOcean وإعادة تعيينها إلى Droplet الخاص بك عندما يتم حظر العنوان الحالي. تقدم هذه المقالة نصًا برمجيًا بلغة Python لأتمتة هذه العملية. النص البرمجي متاح أيضًا كمصدر مفتوح على [GitHub](https://github.com/lzwjava/auto-ss-config).

النص البرمجي يسمح لك بـ:

*   التحقق مما إذا كان عنوان IP محجوزًا معينًا معينًا لـ Droplet معين.
*   إعادة تعيين عنوان IP محجوز جديد إلى Droplet إذا تم حظر العنوان الحالي.
*   التحقق مما إذا كان المنفذ 80 مفتوحًا على عنوان IP المحجوز (طريقة بسيطة للتحقق مما إذا كان العنوان يعمل).

إليك النص البرمجي بلغة Python:

```python
import socket
import os
import argparse
import json
import requests
import time

# دالة للحصول على رؤوس DigitalOcean API
def get_digitalocean_headers():
    api_key = os.environ.get("DO_API_KEY")
    if not api_key:
        print("Error: DO_API_KEY not found in environment variables.")
        return None
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

# دالة لجلب جميع عناوين IP المحجوزة من DigitalOcean
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
            json.dump(reserved_ips_data, f, indent=4) # حفظ الاستجابة في ملف لأغراض التصحيح
        return reserved_ips_data
    except requests.exceptions.RequestException as e:
        print(f"Error getting reserved IP address: {e}")
        return None

# دالة لإلغاء تعيين عنوان IP محجوز من Droplet
def unassign_ip_from_droplet(ip_address, droplet_id, droplet_name):
    headers = get_digitalocean_headers()
    if not headers:
        return False
    
    try:
        url = f"https://api.digitalocean.com/v2/reserved_ips/{ip_address}"
        resp = requests.delete(url, headers=headers)
        resp.raise_for_status()
        print(f"Successfully deleted IP {ip_address} from droplet {droplet_name}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error deleting IP {ip_address} from droplet {droplet_name}: {e}")
        return False

# دالة لتعيين عنوان IP محجوز إلى Droplet
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
        print(f"Successfully assigned IP {ip_address} to droplet {droplet_name}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error assigning IP {ip_address} to droplet {droplet_name}: {e}")
        return False

# دالة لمعالجة عناوين IP المحجوزة، والتحقق من التعيين، وإعادة التعيين إذا لزم الأمر
def process_reserved_ips(reserved_ips, droplet_name, only_check=False):
    if not reserved_ips:
        print("No reserved IPs found in your account.")
        return None

    for reserved_ip in reserved_ips:
        ip_address = reserved_ip.get("ip")
        if not ip_address:
            print("No IP address found for a reserved IP.")
            continue

        droplet = reserved_ip.get("droplet", None)
        if droplet_name:
            if droplet and droplet.get("name") == droplet_name:
                print(f"The reserved IP {ip_address} is assigned to droplet: {droplet_name}")
                if only_check:
                    if check_port_80(ip_address):
                        print(f"Port 80 is open on {ip_address} for droplet {droplet_name}")
                    else:
                        print(f"Port 80 is closed on {ip_address} for droplet {droplet_name}")
                    return ip_address
                droplet_id = droplet.get("id")
                if droplet_id:
                    if unassign_ip_from_droplet(ip_address, droplet_id, droplet_name):
                        # محاولة تعيين عنوان IP جديد بعد الإلغاء
                        
                        new_ip = create_new_reserved_ip(droplet_id)
                        if new_ip:
                            print("Sleeping for 10 seconds before assigning new IP...")
                            time.sleep(10)
                            if assign_ip_to_droplet(new_ip, droplet_id, droplet_name):
                                print(f"Successfully assigned new IP {new_ip} to droplet {droplet_name}")
                            else:
                                print(f"Failed to reassign new IP {new_ip} to droplet {droplet_name}")
                        else:
                            print("No available IP to assign")
                    
                else:
                    print(f"Could not unassign IP {ip_address} because droplet ID was not found.")
                return None
            elif droplet:
                print(f"The reserved IP {ip_address} is not assigned to droplet: {droplet_name}")
            else:
                print(f"No droplets are assigned to the reserved IP: {ip_address}")
        else:
            return ip_address
    return None

# دالة لإنشاء عنوان IP محجوز جديد
def create_new_reserved_ip(droplet_id):
    headers = get_digitalocean_headers()
    if not headers:
        print("Failed to get DigitalOcean headers.")
        return False
    try:
        url = "https://api.digitalocean.com/v2/reserved_ips"
        req = {
            "region": "sgp1", # يمكنك تغيير المنطقة إذا لزم الأمر
        }
        print(f"Attempting to create a new reserved IP for droplet ID: {droplet_id}")
        resp = requests.post(url, headers=headers, json=req)
        resp.raise_for_status()
        new_ip = resp.json().get("reserved_ip", {}).get("ip")
        print(f"Successfully created new reserved IP: {new_ip}")
        return new_ip
    except requests.exceptions.RequestException as e:
        print(f"Error creating new reserved IP: {e}")
        return False

# دالة للتحقق مما إذا كان المنفذ 80 مفتوحًا على عنوان IP معين
def check_port_80(ip_address):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((ip_address, 80))
            return True
    except Exception:
        return False

# الدالة الرئيسية للحصول على عنوان IP المحجوز
def get_reserved_ip(droplet_name=None, only_check=False):
    reserved_ips = fetch_reserved_ips()
    if reserved_ips is None:
        return None
    return process_reserved_ips(reserved_ips, droplet_name, only_check)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get DigitalOcean reserved IP address.")
    parser.add_argument("--droplet-name", required=True, help="Name of the droplet to check if the reserved IP is assigned to.")
    parser.add_argument("--only-check", action="store_true", help="Only check if the IP is assigned to the droplet, do not reassign.")
    args = parser.parse_args()

    reserved_ip = get_reserved_ip(args.droplet_name, args.only_check)
    if reserved_ip:
        print(f"The reserved IP address is: {reserved_ip}")
```

**شرح:**

1.  **استيراد المكتبات:** يتم استيراد المكتبات اللازمة لعمليات الشبكة، والمتغيرات البيئية، وتحليل الوسائط، ومعالجة JSON، وطلبات HTTP، وتأخير الوقت.
2.  **`get_digitalocean_headers()`:** تسترجع مفتاح API الخاص بـ DigitalOcean من المتغيرات البيئية وتقوم ببناء الرؤوس اللازمة لطلبات API.
3.  **`fetch_reserved_ips()`:** تجلب جميع عناوين IP المحجوزة المرتبطة بحساب DigitalOcean الخاص بك باستخدام API. كما تقوم بحفظ الاستجابة الخام في ملف `response.json` لأغراض التصحيح.
4.  **`unassign_ip_from_droplet()`:** تلغي تعيين عنوان IP محجوز معين من Droplet محدد.
5.  **`assign_ip_to_droplet()`:** تعين عنوان IP محجوز معين إلى Droplet محدد.
6.  **`process_reserved_ips()`:** هذه هي المنطق الأساسي:
    *   تقوم بالتكرار عبر جميع عناوين IP المحجوزة.
    *   إذا تم توفير `droplet_name`، فإنها تتحقق مما إذا كان العنوان معينًا لهذا Droplet.
    *   إذا كان `only_check` صحيحًا، فإنها تتحقق مما إذا كان المنفذ 80 مفتوحًا وتعيد العنوان.
    *   إذا لم يكن `only_check`، فإنها تلغي تعيين العنوان الحالي، وتنشئ عنوانًا جديدًا، وتعيّن العنوان الجديد إلى Droplet.
7.  **`create_new_reserved_ip()`:** تنشئ عنوان IP محجوز جديد في منطقة `sgp1` (يمكنك تغيير هذا).
8.  **`check_port_80()`:** تتحقق مما إذا كان المنفذ 80 مفتوحًا على عنوان IP معين. هذه طريقة بسيطة للتحقق مما إذا كان العنوان قابلاً للوصول.
9.  **`get_reserved_ip()`:** تقوم بتنظيم عملية جلب ومعالجة عناوين IP المحجوزة.
10. **`if __name__ == '__main__':`:** تقوم بتحليل وسائط سطر الأوامر (`--droplet-name` و `--only-check`) وتستدعي `get_reserved_ip` لتنفيذ النص البرمجي.

**كيفية الاستخدام:**

1.  **إعداد مفتاح DigitalOcean API:** قم بتعيين متغير البيئة `DO_API_KEY` بمفتاح API الخاص بـ DigitalOcean.
2.  **تشغيل النص البرمجي:**
    *   للتحقق مما إذا كان العنوان معينًا لـ Droplet وما إذا كان المنفذ 80 مفتوحًا:
        ```bash
        python your_script_name.py --droplet-name your_droplet_name --only-check
        ```
    *   لإعادة تعيين عنوان IP جديد إلى Droplet:
        ```bash
        python your_script_name.py --droplet-name your_droplet_name
        ```

يوفر هذا النص البرمجي إطارًا أساسيًا لإدارة عناوين IP المحجوزة. يمكنك توسيعه بناءً على احتياجاتك الخاصة.