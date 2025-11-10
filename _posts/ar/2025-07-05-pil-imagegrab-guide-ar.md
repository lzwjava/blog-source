---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: دليل لقطة شاشة PIL ImageGrab
translated: true
type: note
---

### المتطلبات الأساسية
لاستخدام `ImageGrab` من مكتبة PIL (Pillow)، تأكد من تثبيت Pillow. على نظام Windows، قم بتثبيته عبر pip:

```
pip install Pillow
```

لا توجد عادةً حاجة لإعداد إضافي على Windows، لأن `ImageGrab` يستخدم واجهات برمجة تطبيقات Windows الأصلية.

### الاستخدام الأساسي
تقوم الدالة `ImageGrab.grab()` بالتقاط الشاشة بالكامل (جميع الشاشات) ككائن صورة PIL. إليك مثالًا بسيطًا لالتقاط لقطة شاشة وحفظها كملف PNG:

```python
from PIL import ImageGrab

# التقاط الشاشة بالكامل
screenshot = ImageGrab.grab()

# حفظ الصورة في ملف
screenshot.save("screenshot.png")
```

سيؤدي هذا إلى حفظ ملف باسم `screenshot.png` في دليل العمل الحالي الخاص بك.

### خيارات إضافية
- **التقاط منطقة محددة**: حدد مربعًا محددًا (يسار، أعلى، يمين، أسفل) كمجموعة من إحداثيات البكسل.
  ```python
  # التقاط مساحة 300x300 بكسل تبدأ عند (100, 100)
  region = (100, 100, 400, 400)  # اضبط الإحداثيات حسب الحاجة
  screenshot = ImageGrab.grab(bbox=region)
  screenshot.save("region_screenshot.png")
  ```
- **تضمين مؤشر الفأرة** (إذا كانت مدعومة؛ تحقق من وثائق Pillow للحصول على تفاصيل الإصدار):
  ```python
  # ملاحظة: قد يتطلب هذا include_layered_windows=True في بعض الأنظمة
  screenshot = ImageGrab.grab(include_layered_windows=True)
  ```
- **عرض الصورة**: استخدم `screenshot.show()` لفتحها في عارض الصور الافتراضي الخاص بك (لأغراض الاختبار).

### ملاحظات
- الإحداثيات بالبكسل، حيث (0, 0) في الزاوية العلوية اليسرى للشاشة الأساسية.
- في إعدادات multi-monitor، تلتقط الدالة `grab()` جميع الشاشات كصورة مركبة واحدة.
- إذا واجهت مشاكل (مثل أخطاء الصلاحيات في إصدارات Windows الأحدث)، تأكد من أن البرنامج النصي الخاص بك لديه أذونات التقاط الشاشة أو حاول تشغيله بصلاحيات المسؤول.
- الوثائق الكاملة: [Pillow ImageGrab docs](https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html). للاطلاع على المشاكل الخاصة بـ Windows، تحقق من المشكلات على GitHub إذا لزم الأمر.