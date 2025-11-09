---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast:free
title: إصلاح خطأ استيراد بايثون في طرفية جنوم
translated: true
type: note
---

### تشخيص المشكلة
محرّك GNOME Terminal لا يعمل بسبب خطأ في استيراد مكتبة Python في مكتبة GObject Introspection (GI). يُظهر التتبع أن المشكلة تحدث عند `from gi.repository import GLib, Gio`، وتحديداً في السطر 40 في الملف `/usr/lib/python3/dist-packages/gi/__init__.py`. الخطأ الكامل (بناءً على التقارير الشائعة) هو على الأرجح:

```
ImportError: cannot import name '_gi' from partially initialized module 'gi' (most likely due to a circular import)
```

يحدث هذا عادة بسبب عدم التطابق بين إصدار Python الموجود على نظامك وروابط GI (حزمة python3-gi)، غالباً بعد ترقيات Python اليدوية، أو استخدام بيئات Python الافتراضية، أو تلف الحزم. سجلات UFW BLOCK في ناتج `journalctl` لا علاقة لها بالمشكلة—فهي مجرد جدار الحماية الخاص بك يرفض حركة مرور البث المجموعي غير الضارة (مثل اكتشاف mDNS/UPnP من أجهزة أخرى على 192.168.1.x). تجاهل هذه السجلات في الوقت الحالي.

### إصلاحات سريعة يمكن تجربتها
بما أن لديك موجه طرفية يعمل (يبدو أنك في `~/projects`)، يمكنك تشغيل هذه الأوامر مباشرة. ابدأ بأبسطها:

1. **إعادة تثبيت حزمة GI وGNOME Terminal** (الإصلاح الأكثر شيوعاً):
   ```
   sudo apt update
   sudo apt install --reinstall python3-gi gir1.2-glib-2.0 gnome-terminal
   ```
   ثم اختبر التشغيل بتشغيل `gnome-terminal` من طرفيتك الحالية.

2. **إذا لم ينجح ذلك، تحقق من روابط Python أو أصلحها** (إذا كنت قد عدلت يدوياً على إصدارات Python مؤخراً):
   - تحقق من إصدار Python الخاص بنظامك: `ls -l /usr/bin/python3` (يجب أن يشير إلى شيء مثل python3.10 أو 3.12، اعتماداً على إصدار التوزيعة لديك).
   - إذا كانت الرابط معطلاً، أعد تثبيت Python الافتراضي:
     ```
     sudo apt install --reinstall python3-minimal
     ```
   - أو اضبط الرابط يدوياً (استبدل `3.10` بالإصدار الافتراضي لتوزيعتك):
     ```
     sudo ln -sf /usr/bin/python3.10 /usr/bin/python3
     ```

3. **إعادة ضبط GNOME كلياً** (إذا فشلت الحلول أعلاه—سيؤدي هذا إلى إعادة تعيين تفضيلات الطرفية ولكن ليس البيانات):
   ```
   dconf reset -f /org/gnome/terminal/
   gnome-terminal --reset-config
   ```

4. **الخيار الجذري: إزالة وتثبيت GNOME Terminal من جديد**:
   ```
   sudo apt purge gnome-terminal
   sudo apt install gnome-terminal
   ```

بعد أي إصلاح، سجّل الخروج ثم الدخول أو أعد تشغيل النظام لضمان أن بيئة المكتب تلتقط التغييرات. إذا كنت تستخدم توزيعة مبنية على Ubuntu/Debian (تخميناً من المسارات)، يجب أن تعمل هذه الحلول. إذا كنت تستخدم توزيعة أخرى (مثل Fedora)، استبدل `apt` بـ `dnf`.

إذا لم يحل أي من هذا المشكلة، شغّل الأمر `python3 -c "from gi.repository import GLib; print('OK')"` في طرفيتك الحالية وشارك الناتج للحصول على مزيد من الأدلة.

### المراجع
- [Gnome terminal will not start after trying to install newer version of Python](https://askubuntu.com/questions/880188/gnome-terminal-will-not-start-after-trying-to-install-newer-version-of-python-3)
- [Why won't terminal open?](https://www.reddit.com/r/Ubuntu/comments/1f9qh0a/why_wont_terminal_open/)
- [ImportError: cannot import name '_gi' from partially initialized module](https://stackoverflow.com/questions/59838238/importerror-cannot-import-name-gi-from-partially-initialized-module-gi-mo)
- [Some applications not working on Zorin 17 Core](https://forum.zorin.com/t/some-applications-not-working-on-zorin-17-core/43391)