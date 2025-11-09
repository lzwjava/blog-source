---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: نص اختبار اتصال الواي فاي الآلي
translated: true
type: note
---

```python
import subprocess
import time
import os

def get_wifi_interfaces():
    """دالة مساعدة للعثور على واجهات الواي فاي."""
    try:
        result = subprocess.run("nmcli dev status | grep wifi | awk '{print $1}'", shell=True, capture_output=True, text=True)
        interfaces = [iface.strip() for iface in result.stdout.split('\n') if iface.strip()]
        return interfaces
    except:
        return []

def test_wifi_connection(ssid, password="88888888", timeout=30):
    """اختبار اتصال الواي فاي بدون تفاعل. يُرجع tuple(success: bool, error: str)."""
    interfaces = get_wifi_interfaces()
    if not interfaces:
        return False, "لا توجد واجهة واي فاي متاحة"
    interface = interfaces[0]  # استخدام أول واجهة متاحة
    con_name = f"test-{ssid}"  # اسم فريد لملف تعريف الاختبار
    
    # الأوامر
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
        # حذف أي ملف تعريف موجود (قم بقمع الأخطاء إذا كان مفقودًا)
        subprocess.run(delete_cmd, shell=True, capture_output=True, timeout=5)
        time.sleep(1)
        
        # إنشاء ملف تعريف جديد بكلمة مرور مضمنة (بدون تفاعل)
        add_result = subprocess.run(add_cmd, shell=True, capture_output=True, text=True, timeout=10)
        if add_result.returncode != 0:
            error = add_result.stderr.strip() or add_result.stdout.strip() or "فشل في إنشاء ملف تعريف الاتصال"
            return False, f"خطأ في إنشاء الملف الشخصي: {error}"
        
        # تفعيل الملف الشخصي (بدون تفاعل)
        up_result = subprocess.run(up_cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        if up_result.returncode != 0:
            error = up_result.stderr.strip() or up_result.stdout.strip() or "فشل التفعيل"
            if "secrets were required" in error.lower():
                error = "كلمة مرور خاطئة أو فشل المصادقة"
            elif "activation failed" in error.lower():
                error = f"فشل تفعيل الاتصال: {error}"
            return False, f"خطأ nmcli: {error}"
        
        # الانتظار للاستقرار
        time.sleep(2)
        
        # اختبار الإنترنت مع ping
        ping_test = subprocess.run("ping -c 1 -W 3 8.8.8.8", shell=True, capture_output=True, text=True, timeout=5)
        if ping_test.returncode == 0:
            return True, None
        else:
            error = ping_test.stderr.strip() or "فشل ping"
            return False, f"متصل ولكن بدون إنترنت: {error}"
        
    except subprocess.TimeoutExpired:
        return False, f"انتهت مهلة العملية بعد {timeout} ثانية"
    except subprocess.SubprocessError as e:
        return False, f"خطأ في الأمر: {str(e)}"
    finally:
        # التنظيف: إيقاف الاتصال وحذف الملف الشخصي
        try:
            subprocess.run(f"nmcli connection down '{con_name}'", shell=True, capture_output=True, timeout=5)
            subprocess.run(delete_cmd, shell=True, capture_output=True, timeout=5)
            subprocess.run(disconnect_cmd, shell=True, capture_output=True, timeout=5)
        except subprocess.SubprocessError:
            pass  # تجاهل مشاكل التنظيف
```