---
audio: false
generated: false
lang: ar
layout: post
title: تحسين OpenWRT باستخدام OpenClash و Shadowsocks
translated: true
---

### تحديث قوائم الحزم

عند العمل مع مدير الحزم `apt` في أنظمة لينكس المستندة إلى دبيان مثل أوبونتو، من المهم تحديث قوائم الحزم بشكل دوري. هذا يضمن أن النظام يعرف بأحدث الإصدارات المتاحة للحزم من المستودعات المحددة.

لتنفيذ ذلك، يمكنك استخدام الأمر التالي:

```bash
sudo apt update
```

هذا الأمر يقوم بتحميل أحدث قوائم الحزم من المستودعات المحددة في ملف `/etc/apt/sources.list` وملفات الإعدادات الأخرى في `/etc/apt/sources.list.d/`. بعد تنفيذ هذا الأمر، يمكنك تثبيت أو تحديث الحزم بأحدث الإصدارات المتاحة.

```bash
root@OpenWrt:~# opkg update
جارٍ تنزيل https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt7621/packages/Packages.gz
تم تحديث قائمة الحزم المتاحة في /var/opkg-lists/openwrt_core
جارٍ تنزيل https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt7621/packages/Packages.sig
تم التحقق من التوقيع بنجاح.
جارٍ تنزيل https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/base/Packages.gz
تم تحديث قائمة الحزم المتاحة في /var/opkg-lists/openwrt_base
جارٍ تنزيل https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/base/Packages.sig
تم التحقق من التوقيع بنجاح.
جارٍ تنزيل https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/Packages.gz
تم تحديث قائمة الحزم المتاحة في /var/opkg-lists/openwrt_luci
جارٍ تنزيل https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/Packages.sig
تم التحقق من التوقيع بنجاح.
root@OpenWrt:~#
```

### تثبيت إضافة Shadowsocks

لقد قمت بتثبيت Shadowsocks باستخدام `pip`، لكنني واجهت مشكلة في تشغيل البرنامج. بعد البحث، اكتشفت أنني بحاجة إلى تثبيت إضافات معينة لـ Shadowsocks. إليك الخطوات التي اتبعتها لتثبيت الإضافات:

1. **تثبيت `shadowsocks-v2ray-plugin`:**

   ```bash
   pip install shadowsocks-v2ray-plugin
   ```

2. **تثبيت `shadowsocks-simple-obfs`:**

   ```bash
   pip install shadowsocks-simple-obfs
   ```

3. **تثبيت `shadowsocks-libev`:**

   ```bash
   sudo apt-get install shadowsocks-libev
   ```

بعد تثبيت هذه الإضافات، أصبح بإمكاني تشغيل Shadowsocks بسلاسة. تأكد من أن لديك أحدث إصدار من `pip` لتجنب أي مشاكل متعلقة بالتثبيت.

لتركيب إضافة `luci-app-shadowsocks-libev`:

```bash
root@OpenWrt:~# opkg install luci-app-shadowsocks-libev
جارٍ تثبيت luci-app-shadowsocks-libev (git-22.066.30464-cea4277) إلى root...
جارٍ التحميل من https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/luci-app-shadowsocks-libev_git-22.066.30464-cea4277_all.ipk
جارٍ تهيئة luci-app-shadowsocks-libev.
```

### تثبيت OpenClash

راجع [مستودع OpenClash على GitHub](https://github.com/vernesong/OpenClash?tab=readme-ov-file) لمزيد من التفاصيل. فيما يلي الخطوات لتثبيت المكونات اللازمة.

1. تثبيت خادم OpenSSH SFTP:

```bash
opkg install openssh-sftp-server
```

2. استخدم الأمر `scp` لنسخ حزمة OpenClash إلى الراوتر:

```bash
scp luci-app-openclash_0.46.050-beta_all.ipk root@192.168.1.1:~/
```

### نموذج تكوين OpenClash

```yaml
# OpenClash Configuration Example
# This is a sample configuration file for OpenClash

# Proxy Settings
proxy-providers:
  provider1:
    type: http
    url: "https://example.com/provider1.yaml"
    interval: 3600
    health-check:
      enable: true
      interval: 600
      url: "http://www.google.com/generate_204"

# Rule Settings
rules:
  - DOMAIN-SUFFIX,google.com,DIRECT
  - DOMAIN-SUFFIX,youtube.com,PROXY
  - IP-CIDR,192.168.1.0/24,DIRECT
  - GEOIP,CN,DIRECT
  - MATCH,PROXY

# DNS Settings
dns:
  enable: true
  listen: 0.0.0.0:53
  enhanced-mode: redir-host
  nameserver:
    - 8.8.8.8
    - 8.8.4.4
  fallback:
    - 1.1.1.1
    - 1.0.0.1

# Log Settings
log-level: info
log-file: /var/log/openclash.log
```

**ملاحظة:** هذا مجرد نموذج تكوين أساسي. قد تحتاج إلى تعديله وفقًا لاحتياجاتك الخاصة.

فيما يلي نموذج إعدادات لـ OpenClash:

```yaml
port: 7890
socks-port: 7891
mixed-port: 7892
allow-lan: true
mode: Rule
log-level: info
external-controller: 0.0.0.0:9090
experimental:
  ignore-resolve-fail: true
```

```yaml
dns:
  enable: true
  # ipv6: false
  listen: 0.0.0.0:53
  fake-ip-range: 198.18.0.1/16
  default-nameserver:
    - 119.29.29.29
    - 223.5.5.5
    #- 223.6.6.6
  nameserver:
    - https://223.5.5.5/dns-query
    - https://1.12.12.12/dns-query
    #- https://doh.pub/dns-query
    #- https://dns.alidns.com/dns-query
  fake-ip-filter:
    - "*.lan"
    - "*.localdomain"
    - "*.example"
    - "*.invalid"
    - "*.localhost"
    - "*.test"
    - "*.local"
```

```yaml
proxies:
  - name: "My SS Proxy"
    type: ss
    server: 209.97.0.0
    port: 57500
    cipher: chacha20-ietf-poly1305
    password: "jHLE54zNC000000"
    udp: true
    plugin: ""
    plugin-opts: {}
```

تمت ترجمة الكود أعلاه إلى العربية مع الحفاظ على الأسماء الإنجليزية كما هي.

```yaml
proxy-groups:
  - name: "الوكيل"
    type: select
    proxies:
      - "وكيل SS الخاص بي"
```

```yaml
rules:
  - GEOIP,CN,DIRECT
  - MATCH,Proxy
```

باتباع هذه الخطوات، يمكنك تحسين جهاز OpenWRT لديك لدعم تكوينات الشبكات المتقدمة ووظائف الوكيل. دائمًا ما يُنصح بالرجوع إلى الوثائق الرسمية للحصول على التحديثات وأفضل الممارسات.