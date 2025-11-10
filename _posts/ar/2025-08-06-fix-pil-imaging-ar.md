---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إصلاح خطأ خلفية التصوير PIL
translated: true
type: note
---

هذا الخطأ يعني أن تثبيت PIL إما يفتقر إلى الوحدة الخلفية الثنائية (`_imaging`) أو أنك تستخدم عن طريق الخطأ حزمة "PIL" القديمة بدلاً من "Pillow" الحديثة. إليك كيفية إصلاحه:

1. **تأكد من استخدامك Python 3**
   إذا كان الأمر `python` يشير إلى Python 2، فانتقل إلى Python 3:

   ```bash
   python3 --version
   python3 scripts/content/avatar.py
   ```

2. **أزل أي حزمة PIL قديمة**

   ```bash
   # هذا يزيل PIL القديم إذا كان مثبتًا عبر pip
   python3 -m pip uninstall -y PIL
   ```

3. **(أعد) تثبيت Pillow**

   ```bash
   python3 -m pip install --upgrade --force-reinstall pillow
   ```

4. **ثبت مكتبات النظام المطلوبة**
   على Ubuntu ستحتاج إلى رؤوس التضمين (headers) الخاصة بالتصوير حتى تتمكن Pillow من بناء امتداد `_imaging` الخاص بها:

   ```bash
   sudo apt update
   sudo apt install -y libjpeg-dev zlib1g-dev
   # ثم أعد تثبيت Pillow حتى تعيد التجميع مقابل تلك المكتبات
   python3 -m pip install --upgrade --force-reinstall pillow
   ```

5. **استخدم بيئة افتراضية (اختياري ولكنه موصى به)**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install pillow
   python scripts/content/avatar.py
   ```

بعد ذلك، يجب أن يعمل الأمر `from PIL import Image` دون خطأ استيراد `_imaging`.