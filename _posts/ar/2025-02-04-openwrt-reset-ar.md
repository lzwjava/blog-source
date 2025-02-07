---
audio: true
lang: ar
layout: post
title: إعادة ضبط OpenWrt
translated: true
---

## إعادة الضبط عبر واجهة الويب

يُنصح بالاتصال بالراوتر عبر كابل إيثرنت. بعد إعادة الضبط، سيعود SSID  واي فاي إلى إعداداته الافتراضية، والتي قد لا تكون ما تتوقعه.

## إعادة الضبط عبر سطر الأوامر (SSH)

يمكنك إعادة ضبط OpenWrt إلى إعداداته الافتراضية باستخدام واجهة سطر الأوامر (SSH). إليك الطريقة:

1.  اتصل بجهاز توجيه OpenWrt الخاص بك عبر SSH.
2.  شغّل الأمر التالي:

    ```bash
    root@OpenWrt:~# firstboot
    This will erase all settings and remove any installed packages. Are you sure? [N/y]
    y
    /dev/ubi0_1 is mounted as /overlay, only erasing files
    root@OpenWrt:~# reboot
    ```
3.  سوف يعيد الراوتر التشغيل مع الإعدادات الافتراضية.

**شرح الأوامر:**

*   `firstboot`: هذا الأمر يبدأ عملية إعادة الضبط، ويمسح جميع التكوينات والحزم المثبتة.
*   `reboot`: هذا الأمر يعيد تشغيل جهاز التوجيه، ويطبق عملية إعادة الضبط.
