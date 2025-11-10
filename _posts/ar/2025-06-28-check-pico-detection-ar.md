---
audio: false
generated: true
lang: ar
layout: post
title: التحقق من اكتشاف راسبيري باي بيكو على أوبونتو
translated: true
type: note
---

للتحقق مما إذا كان نظام Ubuntu يكتشف جهاز Raspberry Pi Pico الخاص بك بعد توصيله، اتبع الخطوات التالية:

1. **التحقق من أجهزة USB**:
   - افتح طرفية وقم بتشغيل الأمر:
     ```bash
     lsusb
     ```
   - ابحث عن إدخال مثل `Raspberry Pi Pico` أو جهاز بمعرف بائع `2E8A` (معرف بائع Raspberry Pi). على سبيل المثال:
     ```
     Bus XXX Device XXX: ID 2e8a:0003 Raspberry Pi Pico
     ```

2. **التحقق من المنافذ التسلسلية**:
   - إذا كان Pico في وضع BOOTSEL (لتحميل البرامج الثابتة) أو يشغل برنامج MicroPython/Arduino مع إخراج تسلسلي، تحقق من وجود منفذ تسلسلي:
     ```bash
     ls /dev/tty*
     ```
   - ابحث عن جهاز مثل `/dev/ttyACM0` أو `/dev/ttyUSB0`. يظهر Pico عادةً كـ `/dev/ttyACM0` عند تشغيل MicroPython.

3. **التحقق من أجهزة التخزين (وضع BOOTSEL)**:
   - إذا كان Pico في وضع BOOTSEL (الضغط على زر BOOTSEL أثناء التوصيل)، فيجب أن يظهر كجهاز تخزين جماعي. قم بتشغيل:
     ```bash
     lsblk
     ```
   - ابحث عن جهاز مثل `/dev/sdb` (أو مشابه) بنقطة تركيب، غالبًا ما يحمل التسمية `RPI-RP2`.

4. **استخدم `dmesg` لسجلات النواة**:
   - قم بتشغيل:
     ```bash
     dmesg | tail -n 20
     ```
   - تحقق من الرسائل التي تشير إلى اكتشاف Pico، مثل:
     ```
     [1234.567890] usb 1-1: New USB device found, idVendor=2e8a, idProduct=0003
     [1234.567891] usb 1-1: Product: Pico
     [1234.567892] cdc_acm 1-1:1.0: ttyACM0: USB ACM device
     ```
   - يؤكد هذا أن Pico معترف به وتم تعيين منفذ له (مثل `ttyACM0`).

5. **الاختبار باستخدام MicroPython (إذا كان مثبتًا)**:
   - إذا كنت تستخدم MicroPython، قم بتثبيت أداة مثل `picocom` أو `minicom`:
     ```bash
     sudo apt install picocom
     ```
   - اتصل بالمنفذ التسلسلي لـ Pico:
     ```bash
     picocom /dev/ttyACM0
     ```
   - إذا تم اكتشافه، يجب أن ترى موجه REPL الخاص بـ MicroPython (>>>). اضغط على `Ctrl+C` للخروج.

**ملاحظات**:
- تأكد من أن Pico متصل بشكل صحيح عبر كابل USB جيد (نقل بيانات، وليس طاقة فقط).
- إذا كان في وضع BOOTSEL، يظهر Pico كجهاز تخزين وليس كجهاز تسلسلي.
- إذا لم يتم اكتشافه، جرب منفذ USB مختلف، أو كابل مختلف، أو تحقق مما إذا كانت برامج التشغيل (مثل `cdc_acm` للتسلسل) محملة:
  ```bash
  lsmod | grep cdc_acm
  ```

إذا لم ترَ Pico في أي من هذه الفحوصات، أعطني المزيد من التفاصيل (مثل: وضع Pico، ما الذي تحاول القيام به)، وسأكون ساعدك في استكشاف الأخطاء وإصلاحها بشكل أكبر!