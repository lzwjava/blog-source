---
audio: true
generated: true
lang: ar
layout: post
title: Netplan
translated: true
---

حاولت التكوين أدناه لتخصيص عنوان IP ثابت لماكينة تعمل بنظام Ubuntu. أتنفذ OpenWebUI و llama.cpp على ذلك الخادم.

```
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.128/32
      gateway4: 192.168.1.1
```

بعد تنفيذ `sudo netplan apply`، لم يعد يمكن الوصول إلى الماكينة عبر `ssh lzw@192.168.1.128`.

استخدمت لوحة المفاتيح والفأرة لتسجيل الدخول إلى الماكينة، وإزالة الملفات، وإعادة التكوين.

تم تغيير `/etc/resolv.conf`.