---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: دليل التعبيرات النمطية في بايثون
translated: true
type: note
---

### استيراد وحدة `re`
وحدة `re` (اختصارًا للتعبيرات النمطية) هي جزء من المكتبة القياسية لبايثون. إنها ليست "حزمة regex" منفصلة ولكنها وحدة مدمجة. قم باستيرادها في أعلى السكريبت الخاص بك:

```python
import re
```

### المفاهيم الأساسية
التعبيرات النمطية (regex) هي أنماط تُستخدم لمطابقة والبحث في النصوص ومعالجتها. تستخدم أحرفًا خاصة مثل:
- `.` (أي حرف)
- `*` (صفر أو أكثر من التكرارات)
- `+` (واحد أو أكثر من التكرارات)
- `[]` (فئات الأحرف، مثل `[a-z]` للأحرف الصغيرة)
- `^` (بداية النص)، `$` (نهاية النص)

الأمثلة مبنية على وثائق `re` الخاصة ببايثون. دائمًا قم بتجميع الأنماط المعقدة للكفاءة باستخدام `re.compile()`.

### الدوال الرئيسية وطريقة الاستخدام

#### 1. **مطابقة نمط في البداية**
   - `re.match(pattern, string)`: يتحقق مما إذا كان النمط يطابق من بداية النص.
   - يُرجع كائن مطابقة أو `None`.

   مثال:
   ```python
   import re
   result = re.match(r"Hello", "Hello world")
   print(result.group())  # الإخراج: Hello
   ```

#### 2. **البحث في أي مكان في النص**
   - `re.search(pattern, string)`: يجد أول ظهور للنمط في أي مكان.
   - يُرجع كائن مطابقة أو `None`.

   مثال:
   ```python
   result = re.search(r"world", "Hello world")
   print(result.group())  # الإخراج: world
   ```

#### 3. **إيجاد جميع المطابقات**
   - `re.findall(pattern, string)`: يُرجع قائمة بجميع المطابقات غير المتداخلة.

   مثال:
   ```python
   matches = re.findall(r"\d+", "I have 3 cats and 42 dogs")
   print(matches)  # الإخراج: ['3', '42']
   ```

#### 4. **تقسيم النصوص**
   - `re.split(pattern, string)`: يقسم النص عند ظهور النمط.

   مثال:
   ```python
   parts = re.split(r"\s+", "Hello    world   example")
   print(parts)  # الإخراج: ['Hello', 'world', 'example']
   ```

#### 5. **استبدال المطابقات**
   - `re.sub(pattern, replacement, string)`: يستبدل المطابقات بسلسلة الاستبدال.

   مثال:
   ```python
   new_string = re.sub(r"bad", "good", "This is bad")
   print(new_string)  # الإخراج: This is good
   ```

#### 6. **تجميع الأنماط لإعادة الاستخدام**
   - للاستخدام المتكرر، قم بتجميع regex إلى كائن نمط لأداء أفضل.

   مثال:
   ```python
   pattern = re.compile(r"\d+")
   matches = pattern.findall("Room 101 and 102")
   print(matches)  # الإخراج: ['101', '102']
   ```

### أفضل الممارسات
- استخدم النصوص الخام (`r""`) لأنماط regex لتجنب مشاكل الهروب بشرطة مائلة للخلف.
- تعامل مع كائنات المطابقة: استخدم `.group()` للحصول على المطابقة، و `.span()` للحصول على المؤشرات.
- للمهام المعقدة، اختبر الأنماط باستخدام الأدوات عبر الإنترنت أو shell بايثون التفاعلي.
- راجع الوثائق الرسمية لبايثون: https://docs.python.org/3/library/re.html لمزيد من الأمثلة والإشارات (مثل `re.IGNORECASE`).

إذا كان لديك حالة استخدام محددة أو خطأ، قدم المزيد من التفاصيل!