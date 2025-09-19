---
audio: false
generated: false
image: false
lang: ar
layout: post
title: العناوين العائمة وإدارة واجهة الشبكة
translated: true
---

### جدول المحتويات

1. [عناوين IP العائمة في Hetzner Cloud](#عناوين-ip-العائمة-في-hetzner-cloud)
   - أوامر تكوين IP
   - إعداد تكوين Netplan
   - ملفات تكوين الشبكة

2. [إدارة واجهة الشبكة](#إدارة-واجهة-الشبكة)
   - حذف واجهات TUN
   - مراقبة حالة الواجهة
   - استكشاف أخطاء الشبكة وإصلاحها

3. [ماسح عناوين IP في الشبكة المحلية](#ماسح-عناوين-ip-في-الشبكة-المحلية)
   - نص برمجي لمسح الشبكة بلغة Python
   - اكتشاف المضيفات باستخدام خيوط متعددة
   - قدرات مسح المنافذ
   - تحديد أجهزة الشبكة المحلية

4. [تجاوز العناوين المحلية](#تجاوز-العناوين-المحلية)
   - تكوين الوكيل للشبكات المحلية
   - حسابات قناع الشبكة الفرعية
   - تخطيط نطاق الشبكة

5. [اتصال SSH باستخدام عنوان IPv6](#اتصال-ssh-باستخدام-عنوان-ipv6)
   - تكوين SSH لـ IPv6
   - إدارة ملف تكوين SSH
   - إعداد أوامر الوكيل لأنواع العناوين المختلفة
   - تحسين الأداء

6. [تحسين سرعة الواي فاي](#تحسين-سرعة-الواي-فاي)
   - أداء المودم القديم مقابل الجديد
   - تكوينات إعداد الشبكة
   - وضع الجسر السلكي مقابل اللاسلكي
   - استكشاف الاختناقات في الشبكة

7. [إعادة تعيين OpenWrt](#إعادة-تعيين-openwrt)
   - طرق إعادة التعيين عبر واجهة الويب
   - إجراءات إعادة التعيين عبر سطر الأوامر
   - استعادة الإعدادات الافتراضية للمصنع

---

## عناوين IP العائمة في Hetzner Cloud

### IP

```bash
sudo ip addr add 78.47.144.0 dev eth0
```

### Netplan

```bash
touch /etc/netplan/60-floating-ip.yaml
nano /etc/netplan/60-floating-ip.yaml
```

```yaml
network:
   version: 2
   renderer: networkd
   ethernets:
     eth0:
       addresses:
       - 78.47.144.0/32
```

```bash
sudo netplan apply
```

---

## إدارة واجهة الشبكة

حذف واجهة `tun`.

```bash
$ ipconfig

outline-tun0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.0.85.1  netmask 255.255.255.255  destination 10.0.85.1
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 500  (UNSPEC)
        RX packets 208  bytes 8712 (8.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 385  bytes 23322 (23.3 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

$ sudo ip link delete outline-tun0
```

---

## ماسح عناوين IP في الشبكة المحلية

يقوم هذا النص البرمجي بلغة Python بمسح الشبكة المحلية بحثًا عن عناوين IP النشطة. يستخدم الأمر `ping` للتحقق مما إذا كان المضيف متاحًا ويستخدم الخيوط المتعددة لتسريع عملية المسح. يستخدم السيمافور لتحديد عدد الخيوط المتزامنة لمنع إرباك النظام. يستقبل النص البرمجي عنوان شبكة (مثل "192.168.1.0/24") كمدخل ويطبع ما إذا كان كل عنوان IP في الشبكة نشطًا أو غير نشط.

يساعد هذا النص البرمجي في تحديد الأجهزة الموجودة على الشبكة، مثل جهاز التوجيه TP-LINK الذي يعمل في وضع الجسر السلكي، عن طريق مسح عناوين IP النشطة.

```python
import subprocess
import ipaddress
import threading
import os
import socket
import argparse

MAX_THREADS = 50  # الحد الأقصى لعدد الخيوط المستخدمة

def is_host_up(host, port=None):
    """
    يتحقق مما إذا كان المضيف نشطًا باستخدام ping أو telnet.
    إذا تم تحديد المنفذ، يستخدم telnet للتحقق مما إذا كان المنفذ مفتوحًا.
    وإلا، يستخدم ping.
    يعيد True إذا كان المضيف نشطًا، False خلاف ذلك.
    """
    if port:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                return True
            else:
                return False
        except socket.error as e:
            return False
        finally:
            sock.close()
    else:
        try:
            # -c 1: إرسال حزمة واحدة فقط
            # -W 1: الانتظار ثانية واحدة للاستجابة
            subprocess.check_output(["ping", "-c", "1", "-W", "1", host], timeout=1)
            return True
        except subprocess.CalledProcessError:
            return False
        except subprocess.TimeoutExpired:
            return False

def scan_ip(ip_str, up_ips, port=None):
    """
    يقوم بمسح عنوان IP واحد ويطبع حالته.
    """
    if is_host_up(ip_str, port):
        print(f"{ip_str} نشط")
        up_ips.append(ip_str)
    else:
        print(f"{ip_str} غير نشط")

def scan_network(network, port=None):
    """
    يقوم بمسح الشبكة بحثًا عن المضيفات النشطة باستخدام الخيوط، مع تحديد الحد الأقصى لعدد الخيوط المتزامنة.
    """
    print(f"جاري مسح الشبكة: {network}")
    threads = []
    semaphore = threading.Semaphore(MAX_THREADS)  # تحديد عدد الخيوط المتزامنة
    up_ips = []

    def scan_ip_with_semaphore(ip_str):
        semaphore.acquire()
        try:
            scan_ip(ip_str, up_ips, port)
        finally:
            semaphore.release()

    for ip in ipaddress.IPv4Network(network):
        ip_str = str(ip)
        thread = threading.Thread(target=scan_ip_with_semaphore, args=(ip_str,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return up_ips

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="مسح الشبكة بحثًا عن المضيفات النشطة.")
    parser.add_argument("network", nargs='?', default="192.168.1.0/24", help="الشبكة المراد مسحها (على سبيل المثال، 192.168.1.0/24)")
    parser.add_argument("-p", "--port", type=int, help="المنفذ المراد التحقق منه (اختياري)")
    args = parser.parse_args()

    network_to_scan = args.network
    port_to_scan = args.port

    up_ips = scan_network(network_to_scan, port_to_scan)
    print("\nعناوين IP النشطة:")
    for ip in up_ips:
        print(ip)
```

---

## تجاوز العناوين المحلية

يحدد النص البرمجي عناوين IP النشطة. للتأكد من الاتصال الصحيح بالشبكة، تأكد من تكوين إعدادات الوكيل لتجاوز هذه العناوين المحلية.

```bash
192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,127.0.0.1,localhost,*.local,timestamp.apple.com,sequoia.apple.com,seed-sequoia.siri.apple.com, 192.168.1.0/16
```

---

## أقنعة الشبكة الفرعية

عادةً ما يكون جهازي الثاني على العنوان 192.168.1.16.

لذلك يعمل باستخدام الأمر التالي:

```bash
python scripts/ip_scan.py 192.168.1.0/27 -p 22
```

لأن 32 - 27 = 5، 2^5 = 32، لذا سيحاول من `192.168.1.0` إلى `192.168.1.31`.

لكنه لا يعمل عند استخدام `192.168.1.0/28`، لأن 2^4 = 16، لذا سيحاول من `192.168.1.0` إلى `192.168.1.15`، مما لا يشمل `192.168.1.16`.

---

## اتصال SSH باستخدام عنوان IPv6

أحاول الاتصال بجهاز في Hetzner Cloud باستخدام IPv6. الأمر `ssh 2a01:4f8:c17:2000::/64` لا يعمل، لكن `ssh root@2a01:4f8:c17:2000::1` يعمل.

تم نسخ عنوان IPv6 من وحدة تحكم Hetzner Cloud.

يمكن تكوين ملف `~/.ssh/config` لتطبيق قواعد وكيل مختلفة لعناوين IPv4 و IPv6. يسمح هذا الإعداد بتحديد أمر وكيل لعناوين IPv4 مع التعامل مع عناوين IPv6 بشكل مختلف.

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host *.*.*.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```

عند تشغيل `ssh root@192.168.1.3`، يظهرخرج التالي الذي يبين تطبيق عميل SSH لخيارات التكوين من ملف `~/.ssh/config`:

```bash
debug1: قراءة بيانات التكوين /Users/lzwjava/.ssh/config
debug1: /Users/lzwjava/.ssh/config السطر 1: تطبيق الخيارات لـ 192.168.1.*
debug1: /Users/lzwjava/.ssh/config السطر 5: تطبيق الخيارات لـ *.*.*.*
debug2: add_identity_file: تجاهل المفتاح المكرر ~/.ssh/id_rsa
debug1: /Users/lzwjava/.ssh/config السطر 10: تطبيق الخيارات لـ *
debug2: add_identity_file: تجاهل المفتاح المكرر ~/.ssh/id_rsa
debug1: قراءة بيانات التكوين /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config السطر 21: include /etc/ssh/ssh_config.d/* لم يطابق أي ملفات
debug1: /etc/ssh/ssh_config السطر 54: تطبيق الخيارات لـ *
debug2: resolve_canonicalize: اسم المضيف 192.168.1.3 هو عنوان
debug3: توسيع UserKnownHostsFile '~/.ssh/known_hosts' -> '/Users/lzwjava/.ssh/known_hosts'
debug3: توسيع UserKnownHostsFile '~/.ssh/known_hosts2' -> '/Users/lzwjava/.ssh/known_hosts2'
debug1: لم يتم حل مزود المصادقة $SSH_SK_PROVIDER؛ تعطيل
debug3: channel_clear_timeouts: مسح الوقت المحدد
debug1: تنفيذ أمر الوكيل: exec corkscrew localhost 7890 192.168.1.3 22
```

كانت سرعة اتصال SSH بطيئة بشكل ملحوظ، لذلك عدت إلى التكوين البسيط التالي:

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
```

تنشأ المشكلة عند استخدام عناوين IPv6 مع التوجيه `ProxyCommand corkscrew localhost 7890 %h %p`، حيث قد لا يتعامل أمر الوكيل هذا مع عناوين IPv6 بشكل صحيح.

التكوين أعلاه لا يزال لا يعمل. ومع ذلك، يعمل التكوين التالي بشكل جيد:

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host !192.*.*.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```

---

## تحسين سرعة الواي فاي

### مشاكل المودم القديم

في منزل والدي، المودم قديم جدًا، ربما يبلغ عمره حوالي 10 سنوات. كان إعداد الشبكة الأولي كما يلي:

مودم -> 3م لاسلكي -> TP-Link AX3000 (وضع الجسر اللاسلكي) -> 2م، جدار، لاسلكي -> لابتوب

نتج عن ذلك سرعة تحميل منخفضة، حيث كانت نتيجة اختبار السرعة 10 ميجابت في الثانية فقط.

تم تحسين الإعداد باستخدام اتصال سلكي:

مودم -> كابل 2م -> TP-Link AX3000 (وضع الجسر السلكي) -> 4م لاسلكي، جدار -> لابتوب

تحسنت سرعة التحميل إلى 90 ميجابت في الثانية.

### أداء المودم الجديد

في منزلي، المودم جديد، وأداء جهاز التوجيه TP-Link جيد في وضع الجسر اللاسلكي. إعداد الشبكة كما يلي:

مودم -> 4م لاسلكي -> TP-Link AX3000 (وضع الجسر اللاسلكي) -> 2م لاسلكي -> لابتوب

جودة الشبكة جيدة.

### نصائح استكشاف الأخطاء

لا يوجد حل واحد لتحسين سرعة الواي فاي. من الجيد استخدام كابل لاختبار كل جزء من الشبكة لتحديد الاختناقات. قارن بين السرعات عند استخدام اتصال سلكي مقابل لاسلكي. كما يمكنك تجربة توصيل الأجهزة مباشرة بكابل لمعرفة ما إذا كان ذلك يحسن الأداء.

---

## إعادة تعيين OpenWrt

### إعادة التعيين عبر واجهة الويب

من المستحسن الاتصال بالموجه عبر كابل إيثرنت. بعد إعادة التعيين، سيعود اسم SSID للواي فاي إلى الإعدادات الافتراضية، والتي قد لا تكون كما تتوقع.

### إعادة التعيين عبر سطر الأوامر (SSH)

يمكنك إعادة تعيين OpenWrt إلى الإعدادات الافتراضية باستخدام واجهة سطر الأوامر (SSH). إليك الطريقة:

1. اتصل بموجه OpenWrt عبر SSH.
2. قم بتشغيل الأمر التالي:

    ```bash
    root@OpenWrt:~# firstboot
    This will erase all settings and remove any installed packages. Are you sure? [N/y]
    y
    /dev/ubi0_1 is mounted as /overlay, only erasing files
    root@OpenWrt:~# reboot
    ```
3. سيقوم الموجه بإعادة التشغيل بالإعدادات الافتراضية.

**شرح الأوامر:**

* `firstboot`: هذا الأمر يبدأ عملية إعادة التعيين، حيث يمسح جميع التكوينات والحزم المثبتة.
* `reboot`: هذا الأمر يعيد تشغيل الموجه، مطبقًا إعادة التعيين.