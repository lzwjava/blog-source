---
audio: false
generated: true
lang: ar
layout: post
title: إصلاح خطأ دعم صيغة HEIC في الوسائد
translated: true
type: note
---

يشير الخطأ `cannot identify image file` إلى أن Pillow غير قادر على قراءة ملفات HEIC، ويرجع ذلك على الأرجح إلى أحد الأسباب التالية:
1. **مكتبة `libheif` مفقودة**: يحتاج Pillow إلى `libheif` للتعامل مع ملفات HEIC، وقد لا تكون مثبتة أو مُهيأة بشكل صحيح على نظامك.
2. **ملفات HEIC تالفة أو غير متوافقة**: قد تكون ملفات HEIC تالفة أو بصيغة لا يستطيع Pillow معالجتها.
3. **مشكلة في إصدار Pillow**: على الرغم من أن Pillow 9.0.0+ يدعم HEIC، فقد تكون هناك مشكلة في التهيئة أو إصدار قديم.

بما أنك تستخدم نظام macOS (بناءً على الناتج السابق)، سأقدم نصًا برمجيًا ثابتًا في Python يتضمن معالجة أخطاء إضافية وتسجيلًا للأحداث لتشخيص المشكلة. سأرشدك أيضًا خلال عملية تثبيت `libheif` والتحقق من دعم Pillow لـ HEIC. إذا استمر فشل Pillow، يتضمن النص البرمجي خيارًا احتياطيًا لاستخدام `ImageMagick` (إذا كان مثبتًا) لتحويل HEIC.

### خطوات إصلاح المشكلة

#### 1. تثبيت `libheif`
يعتمد Pillow على `libheif` لدعم HEIC. قم بتثبيته باستخدام Homebrew:
```bash
brew install libheif
```
بعد التثبيت، أعد تثبيت Pillow لضمان ارتباطه بـ `libheif`:
```bash
pip uninstall pillow
pip install pillow
```

#### 2. التحقق من دعم Pillow لـ HEIC
تحقق مما إذا كان Pillow يستطيع التعامل مع ملفات HEIC:
```bash
python -c "from PIL import features; print(features.check_feature('heic'))"
```
- إذا أظهر الناتج `True`، فإن Pillow يدعم HEIC.
- إذا أظهر الناتج `False` أو خطأ، فإن `libheif` غير مهيأة بشكل صحيح، أو تم بناء Pillow بدون دعم HEIC.

#### 3. التحقق من سلامة الملفات
تأكد من أن ملفات HEIC غير تالفة. حاول فتح أحد الملفات (مثل `IMG_5988.HEIC`) في عارض مثل Preview على نظام macOS. إذا لم يفتح، فقد تكون الملفات تالفة، وسوف تحتاج إلى إعادة تصديرها أو الحصول على نسخ جديدة.

#### 4. النص البرمجي المحدث لـ Python
النص البرمجي المحدث:
- يستخدم Pillow لتحويل HEIC مع تحسين معالجة الأخطاء.
- يلجأ إلى `ImageMagick` (إذا كان مثبتًا) عندما يفشل Pillow في قراءة ملف HEIC.
- يسجل الأخطاء التفصيلية في ملف (`conversion_errors.log`) لتصحيح الأخطاء.
- يدعم كل من الامتدادات `.heic` و `.heif`.
- يضغط صور JPG الناتجة إلى حوالي 500 كيلوبايت.

```python
import os
import argparse
import subprocess
import logging
from PIL import Image
from datetime import datetime

# إعداد تسجيل الأحداث
logging.basicConfig(
    filename="conversion_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# تحليل وسيطات سطر الأوامر
parser = argparse.ArgumentParser(description="Convert HEIC images to JPG and compress to ~500KB.")
parser.add_argument("input_dir", help="Directory containing HEIC files")
args = parser.parse_args()

# تعريف مجلدي الإدخال والإخراج
input_dir = args.input_dir.rstrip(os.sep)
output_dir = input_dir + "_compressed"
target_size_kb = 500  # حجم الملف المستهدف بالكيلوبايت

# إنشاء مجلد الإخراج إذا لم يكن موجودًا
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def get_file_size(file_path):
    """إرجاع حجم الملف بالكيلوبايت."""
    return os.path.getsize(file_path) / 1024

def convert_with_imagemagick(heic_path, jpg_path):
    """اللجوء إلى ImageMagick لتحويل HEIC إلى JPG."""
    try:
        subprocess.run(
            ["magick", heic_path, "-quality", "85", jpg_path],
            check=True, capture_output=True, text=True
        )
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"ImageMagick failed for {heic_path}: {e.stderr}")
        return False
    except FileNotFoundError:
        logging.error("ImageMagick not installed. Install it with 'brew install imagemagick'.")
        return False

def convert_heic_to_jpg(heic_path, jpg_path, quality=85):
    """تحويل HEIC إلى JPG وضغطه للحجم المستهدف التقريبي."""
    try:
        # حاول استخدام Pillow أولاً
        image = Image.open(heic_path)
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        # احفظ كـ JPG بجودة أولية
        image.save(jpg_path, "JPEG", quality=quality)
        
        # اضبط الجودة للاقتراب من الحجم المستهدف
        current_size = get_file_size(jpg_path)
        low, high = 10, 100
        while low <= high and abs(current_size - target_size_kb) > 10:
            quality = (low + high) // 2
            image.save(jpg_path, "JPEG", quality=quality)
            current_size = get_file_size(jpg_path)
            if current_size > target_size_kb:
                high = quality - 1
            else:
                low = quality + 1
        return True
    except Exception as e:
        logging.error(f"Pillow failed for {heic_path}: {e}")
        # اللجوء إلى ImageMagick
        return convert_with_imagemagick(heic_path, jpg_path)

# معالجة جميع ملفات HEIC في مجلد الإدخال
for filename in os.listdir(input_dir):
    if filename.lower().endswith((".heic", ".heif")):
        heic_path = os.path.join(input_dir, filename)
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpg_path = os.path.join(output_dir, jpg_filename)

        try:
            if convert_heic_to_jpg(heic_path, jpg_path):
                print(f"Converted {filename} to {jpg_filename}, size: {get_file_size(jpg_path):.2f} KB")
            else:
                print(f"Error processing {filename}: Conversion failed (check conversion_errors.log)")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            logging.error(f"General error for {heic_path}: {e}")

print("Batch conversion complete! Check conversion_errors.log for any issues.")
```

### طريقة الاستخدام
1. **احفظ النص البرمجي**:
   احفظ الكود كـ `photo_compress.py` في مجلد `scripts/media/` الخاص بك.

2. **ثبت التبعيات**:
   - تأكد من تثبيت Pillow:
     ```bash
     pip install --upgrade pillow
     ```
   - ثبت `libheif`:
     ```bash
     brew install libheif
     ```
   - اختياريًا، ثبت ImageMagick للخيار الاحتياطي:
     ```bash
     brew install imagemagick
     ```

3. **شغل النص البرمجي**:
   ```bash
   python scripts/media/photo_compress.py ./assets/images/yuebei
   ```
   - هذا يعالج جميع ملفات `.heic` و `.heif` في `assets/images/yuebei`.
   - يتم حفظ صور JPG الناتجة في `assets/images/yuebei_compressed`.
   - يتم تسجيل الأخطاء في `conversion_errors.log` في المجلد الحالي.

4. **تحقق من سجل الأخطاء**:
   إذا فشل تحويل أي ملفات، تحقق من `conversion_errors.log` للحصول على رسائل الخطأ التفصيلية.

### استكشاف الأخطاء وإصلاحها الإضافي
- **إذا استمر فشل Pillow**:
  - تحقق من تثبيت `libheif` بشكل صحيح وارتباطه:
    ```bash
    pkg-config --modversion libheif
    ```
    إذا فشل هذا، أعد تثبيت `libheif` و Pillow.
  - اختبر ملفًا واحدًا يدويًا:
    ```python
    from PIL import Image
    img = Image.open("./assets/images/yuebei/IMG_5988.HEIC")
    print("Image opened successfully")
    ```
    إذا فشل هذا، فقد يكون الملف تالفًا أو من نوع HEIC غير مدعوم.

- **الملفات التالفة**:
  - حاول تحويل ملف واحد باستخدام ImageMagick يدويًا:
    ```bash
    magick ./assets/images/yuebei/IMG_5988.HEIC test.jpg
    ```
    إذا فشل هذا، فمن المرجح أن الملف تالف.

- **الخيار الاحتياطي ImageMagick**:
  - إذا استمر فشل Pillow باستمرار، ستحاول البرنامج النصي استخدام ImageMagick (إذا كان مثبتًا).
  - ثبت `jpegoptim` للتحكم الأفضل في الضغط:
    ```bash
    brew install jpegoptim
    ```
    ثم، بعد تشغيل البرنامج النصي، اضغط المخرجات:
    ```bash
    for i in ./assets/images/yuebei_compressed/*.jpg; do jpegoptim --size=500k "$i"; done
    ```

### المراجع
- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
- [ImageMagick](https://imagemagick.org/)
- [libheif](https://github.com/strukturag/libheif)
- [jpegoptim](https://github.com/tjko/jpegoptim)

إذا كنت لا تزال تواجه مشاكل، شارك محتويات `conversion_errors.log` أو أي رسائل خطأ جديدة، ويمكنني تقديم المزيد من المساعدة!