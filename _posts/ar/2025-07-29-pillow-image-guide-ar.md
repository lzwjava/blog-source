---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: دليل معالجة الصور بمكتبة PIL Pillow
translated: true
type: note
---

### ما هو PIL/Pillow؟
PIL كان يرمز في الأصل إلى مكتبة التصوير في Python، لكنه الآن محفوظ كحزمة Pillow (فرع حديث). تقوم باستيراده كـ `PIL` في الكود، لكنك تحتاج إلى تثبيت Pillow عبر pip. يتم استخدامه لفتح ومعالجة وحفظ ملفات الصور في Python. يدعم تنسيقات مثل JPEG، وPNG، وGIF، وBSP، والمزيد.

### التثبيت
لاستخدام PIL، قم بتثبيت Pillow:
```bash
pip install pillow
```

### الاستيراد الأساسي والاستخدام
بعد التثبيت، قم باستيراده هكذا في سكريبت Python الخاص بك:
```python
from PIL import Image
```
لا حاجة لـ `import PIL.Image` — هذا يستورد وحدة Image مباشرة.

### عمليات الصور الشائعة
إليك كيفية تنفيذ المهام الأساسية. افترض أن لديك ملف صورة باسم `example.jpg` في دليلك.

#### 1. فتح صورة
```python
image = Image.open('example.jpg')  # يفتح ملف الصورة
image.show()  # يعرضها (يعمل على الأنظمة التي تحتوي على عارض صور)
```

#### 2. الحصول على معلومات الصورة
```python
print(image.format)  # مثال: 'JPEG'
print(image.size)    # Tuple: (العرض, الارتفاع)
print(image.mode)    # مثال: 'RGB' للصور الملونة
```

#### 3. تغيير حجم الصورة
```python
resized = image.resize((800, 600))  # تغيير الحجم إلى 800x600 بكسل
resized.save('resized_example.jpg')  # حفظ الصورة التي تم تغيير حجمها
```

#### 4. تحويل التنسيقات
```python
image.convert('L').save('grayscale_example.png')  # تحويل إلى التدرج الرمادي وحفظ كـ PNG
```

#### 5. تدوير صورة
```python
rotated = image.rotate(90)  # تدوير 90 درجة في اتجاه عقارب الساعة
rotated.save('rotated_example.jpg')
```

#### 6. اقتصاص صورة
```python
left, top, right, bottom = 100, 100, 300, 300  # تعريف صندوق الاقتصاص (x1, y1, x2, y2)
cropped = image.crop((left, top, right, bottom))
cropped.save('cropped_example.jpg')
```

#### 7. تطبيق المرشحات (يتطلب استيرادات إضافية)
للمرشحات، استورد `ImageFilter`:
```python
from PIL import ImageFilter
blurred = image.filter(ImageFilter.BLUR)  # تطبيق مرشح طمس
blurred.save('blurred_example.jpg')
```

### مثال متقدم: معالجة دفعة من الصور المتعددة
```python
import os
from PIL import Image

# تغيير حجم جميع صور JPEG في مجلد إلى 200x200
input_folder = 'images/'
output_folder = 'resized_images/'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        image = Image.open(os.path.join(input_folder, filename))
        resized = image.resize((200, 200))
        resized.save(os.path.join(output_folder, filename))
```

### نصائح وملاحظات
- **معالجة الأخطاء**: استخدم try-except للملفات غير الصالحة، مثال: `try: image = Image.open('file.jpg')`.
- **كفاءة الذاكرة**: للصور الكبيرة، استخدم `image.close()` بعد العمليات لتحرير الذاكرة.
- **التوثيق**: تحقق من وثائق Pillow الكاملة على [pillow.readthedocs.io](https://pillow.readthedocs.io/en/stable/) للحصول على المزيد من الوظائف مثل الرسم، أو إضافة النص، أو معالجة بيانات EXIF.
- **التبعيات**: قد تحتاج Pillow إلى مكتبات نظام (مثل libjpeg) في بعض الإعدادات؛ راجع دليل التثبيت إذا واجهت مشاكل.

إذا كانت لديك مهمة محددة أو خطأ، قدم المزيد من التفاصيل للحصول على مساعدة مخصصة!