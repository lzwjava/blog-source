---
audio: true
lang: ar
layout: post
title: جرب Netplan
translated: true
---

حاولت التكوين أدناه لتخصيص عنوان IP ثابت لماكينة Ubuntu. أتعمل على OpenWebUI و llama.cpp على ذلك الخادم.

```yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.128/32
      gateway4: 192.168.1.1
```

بعد تشغيل `sudo netplan apply`، لم أستطع الوصول إلى الماكينة عبر `ssh lzw@192.168.1.128`.

كان علي استخدام لوحة مفاتيح وفأرة لتسجيل الدخول إلى الماكينة، وإزالة الملفات، وإعادة الإعدادات.

لاحظت أن `/etc/resolv.conf` قد تغير.