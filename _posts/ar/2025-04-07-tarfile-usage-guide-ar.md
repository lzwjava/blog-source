---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: دليل استخدام وحدة tarfile في بايثون
translated: true
type: note
---

### استيراد وحدة tarfile
لاستخدام مكتبة `tarfile` في Python، قم أولاً باستيرادها:
```python
import tarfile
```
هذه الوحدة جزء من المكتبة القياسية لـ Python، لذا لا حاجة للتثبيت. تعتمد على تنسيق tar الخاص بـ POSIX وتدعم القراءة من أرشيفات tar والكتابة إليها سواء كانت مضغوطة أو غير مضغوطة.

### فتح وإنشاء أرشيفات Tar
- **فتح ملف tar موجود**: استخدم `tarfile.open()` مع وضع معين. تشمل الأوضاع `'r'` (قراءة)، `'w'` (كتابة فارغ)، `'a'` (إلحاق)، أو متغيرات مع ضغط مثل `'r:gz'` لـ gzip.
  ```python
  import tarfile
  
  # فتح للقراءة (غير مضغوط)
  with tarfile.open('example.tar', 'r') as tar:
      # العمل مع الأرشيف هنا
      pass
  ```
- **إنشاء ملف tar جديد**: استخدم وضع `'w'` لإنشاء أرشيف فارغ. أضف بادئات الضغط مثل `'w:gz'` لـ gzip أو `'w:bz2'` لـ bzip2.
  ```python
  # إنشاء ملف مضغوط tar.gz
  with tarfile.open('archive.tar.gz', 'w:gz') as tar:
      pass
  ```

### إضافة الملفات إلى الأرشيف
- **إضافة ملف واحد**: استدعِ الدالة `add()` على كائن ملف tar، مرراً مسار الملف. يمكنك تحديد arcname لاسم مختلف داخل الأرشيف.
  ```python
  with tarfile.open('archive.tar.gz', 'w:gz') as tar:
      tar.add('file.txt')  # يضيف file.txt كما هو
      tar.add('data.csv', arcname='renamed_data.csv')  # إعادة التسمية داخل الأرشيف
  ```
- **إضافة ملفات متعددة أو مجلد**: استخدم `add()` في حلقة أو أضف مجلدات كاملة بشكل متكرر.
  ```python
  import os
  
  with tarfile.open('backup.tar', 'w') as tar:
      for root, dirs, files in os.walk('my_folder'):
          for file in files:
              tar.add(os.path.join(root, file))
  ```

### استخراج الملفات من الأرشيف
- **استخراج جميع الملفات**: استخدم `extractall()` للاستخراج إلى مجلد محدد (الإعداد الافتراضي هو المجلد الحالي).
  ```python
  with tarfile.open('archive.tar.gz', 'r:gz') as tar:
      tar.extractall(path='extracted_folder')  # ينشئ المجلد إذا لزم الأمر
  ```
- **استخراج ملفات محددة**: اذكر الأعضاء أولاً باستخدام `getmembers()`، ثم استخدم `extract()`.
  ```python
  with tarfile.open('example.tar', 'r') as tar:
      members = tar.getmembers()
      for member in members:
          if 'important' in member.name:  # مثال للتصفية
              tar.extract(member, path='output_dir')
  ```
- ملاحظة: للأمان، قم بتصفية المسارات (مثل تجنب `..`) لمنع هجمات اختراق المسار. تقوم `tarfile` ببعض الفحوصات، ولكن يُنصح بالتصفية اليدوية للأرشيفات غير الموثوقة.

### سرد محتويات الأرشيف
- **التكرار عبر الملفات**: استخدم `getmembers()` أو كرر مباشرة على كائن tar للحصول على كائنات TarInfo.
  ```python
  with tarfile.open('example.tar', 'r') as tar:
      for member in tar.getmembers():
          print(f"{member.name}: {member.size} bytes")
  ```

### الأوضاع الرئيسية والضغط
- `'r'`: قراءة tar غير مضغوط.
- `'r:gz'`, `'r:bz2'`, `'r:xz'`: قراءة الأنواع المضغوطة.
- `'w'`: كتابة tar غير مضغوط جديد (يكتب فوق الموجود).
- `'a'`: الإلحاق بملف tar موجود.
- الكشف التلقائي عن الضغط عند القراءة؛ التحديد عند الكتابة.

### نصائح وأفضل الممارسات
- استخدم دائماً مديري السياق (عبارات `with`) لضمان إغلاق الملفات بشكل صحيح.
- للأرشيفات الكبيرة، فكر في التصفية أو الاستخراج الانتقائي لتوفير الذاكرة.
- لا تتعامل `tarfile` مع الأرشيفات المشفرة مباشرة—استخدم أدوات خارجية أو ادمج مع `gzip` يدوياً إذا لزم الأمر.
- معالجة الأخطاء: امسك `tarfile.TarError` لمشاكل الأرشيف.
- الوثائق الكاملة: راجع [الوثائق الرسمية لـ Python الخاصة بـ tarfile](https://docs.python.org/3/library/tarfile.html) للحصول على ميزات متقدمة مثل المرشحات المخصصة.