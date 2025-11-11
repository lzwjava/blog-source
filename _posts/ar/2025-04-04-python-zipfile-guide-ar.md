---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: دليل حزمة ZipFile في بايثون
translated: true
type: note
---

### نظرة عامة على حزمة ZipFile
وحدة `zipfile` في بايثون تتيح لك القراءة من والكتابة إلى ملفات أرشيف ZIP دون الحاجة إلى أدوات خارجية. وهي جزء من المكتبة القياسية، لذا لا حاجة لتثبيتها (بدءًا من بايثون 2.3+). استخدمها لضغط، أو فك ضغط، أو معالجة ملفات ZIP برمجيًا. وهي تدعم طرق ضغط مختلفة مثل DEFLATE.

استيرادها باستخدام: `import zipfile`

### قراءة ملفات ZIP
لاستخراج أو فحص ملفات ZIP الموجودة:

1. **فتح ملف ZIP للقراءة**:
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       # 'r' لوضع القراءة
   ```

2. **سرد المحتويات**:
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       file_list = zip_ref.namelist()  # تُرجع قائمة بأسماء الملفات
       print(file_list)
   ```

3. **استخراج الملفات**:
   - استخراج الكل: `zip_ref.extractall('destination_folder')`
   - استخراج ملف واحد: `zip_ref.extract('file_inside.zip', 'path')`

4. **قراءة محتوى الملف دون استخراجه**:
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       with zip_ref.open('file_inside.zip') as file:
           content = file.read()
           print(content.decode())  # إذا كان نصًا
   ```

ملاحظة: استخدم `with` دائمًا للإغلاق التلقائي. لملفات ZIP المحمية بكلمة مرور، أضف `pwd=b'password'` إلى `ZipFile()`.

### كتابة ملفات ZIP
لإنشاء أو الإضافة إلى ملفات ZIP جديدة أو موجودة:

1. **إنشاء ملف ZIP جديد**:
   ```python
   with zipfile.ZipFile('new_archive.zip', 'w') as zip_ref:
       # 'w' لوضع الكتابة (يستبدل الملف إذا كان موجودًا)
   ```

2. **إضافة الملفات**:
   - إضافة ملف واحد: `zip_ref.write('source_file.txt', 'arcname.txt')` (معلمة arcname اختيارية تعيد تسميته داخل الأرشيف)
   - إضافة ملفات متعددة: كرر العملية على قائمة من الملفات واستدع `write()`.

3. **الضغط أثناء الكتابة** (الافتراضي هو DEFLATE):
   ```python
   with zipfile.ZipFile('archive.zip', 'w', zipfile.ZIP_DEFLATED) as zip_ref:
       zip_ref.write('large_file.txt')
   ```
   الخيارات: `ZIP_STORED` (بدون ضغط)، `ZIP_DEFLATED`، `ZIP_BZIP2`، إلخ.

4. **الإضافة إلى ملف ZIP موجود** (استخدم الوضع 'a' بدلاً من 'w').

### العمليات الشائعة والنصائح
- **التحقق مما إذا كان الملف عبارة عن ZIP صالح**: استخدم `zipfile.is_zipfile('file.zip')`.
- **الحصول على معلومات الملف**: `zip_ref.getinfo('file.txt')` تُرجع كائن ZipInfo يحتوي على تفاصيل مثل الحجم، التاريخ.
- **التعامل مع الملفات الكبيرة**: قد يؤدي قراءة/استخراج الملفات الكبيرة إلى استهلاك الذاكرة؛ استخدم طريقة `open()` للتدفق.
- **معالجة الأخطاء**: امسك استثناءات `BadZipFile` أو `LargeZipFile`.
- **متعدد المنصات**: يعمل على Windows، وmacOS، وLinux، لكن كن حذرًا بشأن فواصل المسارات (استخدم `/`).
- **التشفير**: يتم دعم حماية كلمة المرور الأساسية، لكنها ضعيفة — استخدم أدوات أقوى للأمان.
- **مستوى أعلى**: للحصول على ميزات أكثر (مثل التكامل مع shutil)، اجمع مع `shutil.make_archive()` لإنشاء ملفات ZIP.

مثال على سكريبت كامل لضغط مجلد:
```python
import zipfile
import os

def zip_folder(source_dir, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file), os.path.join(source_dir, '..')))

zip_folder('my_folder', 'output.zip')
```

للحصول على الوثائق الكاملة، تحقق من [الوثائق الرسمية لبايثون](https://docs.python.org/3/library/zipfile.html). إذا كانت لديك مهمة محددة (مثل "كيفية الاستخراج إلى الذاكرة"), قدم المزيد من التفاصيل!