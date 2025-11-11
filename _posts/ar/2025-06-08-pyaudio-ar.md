---
audio: false
generated: true
lang: ar
layout: post
title: بورت أوديو و باي أوديو
translated: true
type: note
---

يحدث هذا الخطأ لأن **pyaudio** يتطلب رؤوس تطوير PortAudio للتجميع، وهي مفقودة على نظامك. إليك كيفية إصلاح ذلك:

### الحل خطوة بخطوة:

1. **تثبيت رؤوس تطوير PortAudio** (مطلوبة لـ pyaudio):
```bash
sudo apt update && sudo apt install portaudio19-dev
```

2. **تثبيت أدوات تطوير Python** (إذا لم تكون مثبتة مسبقًا):
```bash
sudo apt install python3-dev
```

3. **إعادة محاولة التثبيت**:
```bash
pip install -r requirements.local.txt
```

### إذا ما زلت تواجه مشاكل مع pycrypto:
الحزمة pycrypto قديمة وقد يكون لديها مشاكل توافق. استبدلها بـ **pycryptodome** عن طريق تعديل ملف `requirements.local.txt` الخاص بك:

1. افتح ملف المتطلبات:
```bash
nano requirements.local.txt
```

2. استبدل `pycrypto` بـ:
```
pycryptodome
```

3. احفظ الملف وأعد تشغيل التثبيت:
```bash
pip install -r requirements.local.txt
```

### لماذا هذا الحل يعمل:
- `portaudio19-dev` يوفر رؤوس PortAudio المفقودة اللازمة لتجميع pyaudio
- `python3-dev` يتضمن رؤوس تطوير Python الضرورية
- `pycryptodome` هو بديل محافظ عليه لـ pycrypto القديم

### بديل لـ pycrypto (إذا كنت مضطرًا للاحتفاظ به):
إذا كنت تحتاج تحديدًا إلى pycrypto، فقم بتثبيت تبعيات البناء أولاً:
```bash
sudo apt install build-essential libgmp-dev
pip install pycrypto
```
ولكن لاحظ أن pycrypto لديه مشاكل توافق مع إصدارات Python الأحدث.

بعد هذه الخطوات، يجب أن يتم تثبيت جميع الحزم بشكل صحيح. تحذيرات DEPRECATION حول عمليات البناء القديمة هي للإعلام ولن تمنع التثبيت - وهي تشير إلى أن الحزم ستحتاج إلى الانتقال إلى بناءات PEP 517 في المستقبل.