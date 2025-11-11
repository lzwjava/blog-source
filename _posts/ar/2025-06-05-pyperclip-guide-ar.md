---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: 'دليل إدارة الحافظة في بايثون: Pyperclip'
translated: true
type: note
---

### ما هو Pyperclip؟
Pyperclip هي مكتبة Python خفيفة الوزن للوصول إلى الحافظة النظامية (وظيفة النسخ واللصق) والتعامل معها. تعمل عبر المنصات (Windows، macOS، Linux) وتدعم نسخ النص إلى الحافظة ولصق النص منها. ملاحظة: هي تتعامل مع النص فقط؛ للملفات أو الصور، استخدم مكتبات أخرى.

### التثبيت
ثبّت Pyperclip عبر pip:
```
pip install pyperclip
```

على Linux، قد تحتاج إلى تبعيات إضافية للوصول إلى الحافظة (مثل `xclip` أو `xsel`). ثبّتها باستخدام مدير الحزم الخاص بك (مثل `sudo apt-get install xclip` على Ubuntu).

### الاستخدام الأساسي
1. **استيراد المكتبة**:
   ```python
   import pyperclip
   ```

2. **نسخ نص إلى الحافظة**:
   ```python
   pyperclip.copy("Hello, world!")
   ```
   يضع هذا السلسلة النصية "Hello, world!" في الحافظة.

3. **لصق نص من الحافظة**:
   ```python
   text = pyperclip.paste()
   print(text)  # يُخرج محتوى الحافظة الحالي
   ```
   يسترجع هذا النص من الحافظة ويطبعه.

### مثال: نسخ إدخال المستخدم إلى الحافظة
```python
import pyperclip

user_input = input("أدخل النص لنسخه: ")
pyperclip.copy(user_input)
print("تم نسخ النص إلى الحافظة!")
```

### مثال: اللصق والتعديل
```python
import pyperclip

pyperclip.copy("Original text")
modified = pyperclip.paste().upper()  # الصق، ثم عدل (مثال: أحرف كبيرة)
pyperclip.copy(modified)
print("تم نسخ النص المعدل.")
```

### نصائح إضافية
- **معالجة الأخطاء**: في بعض الأنظمة (مثل الخوادم بدون واجهة رسومية أو بعض توزيعات Linux)، قد يفشل الوصول إلى الحافظة. ضع الكود في try-except:
  ```python
  try:
      pyperclip.copy("text")
  except pyperclip.PyperclipException as e:
      print(f"خطأ في الحافظة: {e}")
  ```
- **التحقق من التوفر**: استخدم `pyperclip.paste()` مباشرة بعد تشغيل السكربت، حيث أن محتويات الحافظة تبقى بين مرات التشغيل.
- **القيود**: غير مناسب للبيانات الثنائية؛ للنص فقط. للاستخدام المتقدم، راجع [التوثيق الرسمي](https://github.com/asweigart/pyperclip).

هذا يغطي الأساسيات—ابدأ بنسخ ولصق سلسلة نصية بسيطة للاختبار. إذا واجهت مشاكل محددة بالمنصة، تحقق من مستودع GitHub الخاص بالمكتبة.