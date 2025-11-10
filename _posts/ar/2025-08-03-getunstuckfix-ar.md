---
audio: false
generated: true
image: false
lang: ar
layout: post
title: مقتطف بايثون الرسمي الثابت لـ إماجين
translated: true
type: note
---

لقد نفذت المنطق الصحيح بشكل أساسي، لكن تعليمات **get‑unstuck** غير دقيقة قليلاً. إليك نسخة منقحة مأخوذة من المثال الرسمي في الوثائق:

```python
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# ← اضبط مفتاح API الخاص بك أو استخدم متغير البيئة GOOGLE_API_KEY / GEMINI_API_KEY
client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=types.GenerateImagesConfig(
        number_of_images=1,
        # image_size="2K",  # اختياري لدقة 2K؛ يتطلب إصدار مكتبة fast-preview الأحدث
        aspect_ratio="1:1",
        safety_filter_level="BLOCK_MEDIUM_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    )
)

for i, generated in enumerate(response.generated_images):
    raw = generated.image.image_bytes
    pil = Image.open(BytesIO(raw))  # تحويل البايتات الخام إلى صورة PIL
    pil.save(f"output-image-{i+1}.png")
    print(f"تم حفظ الصورة {i+1}, حجمها {len(raw):,} بايت")
```

بينما استخدمت مقتطفات كود Google لـ Python أيضًا `image_size="2K"` لنموذجها 4‑preview، كن على علم بأن:

* يجب أن تستخدم `google-genai` الإصدار v1.28 أو أحدث لدعم `image_size` على نماذج Imagen 4؛
* وإلا قم بحذف هذا الحقل (القيمة الافتراضية هي 1,024×1,024 بدقة مربعة ثابتة) ([GitHub][1]).

---

### 🚩 الأخطاء الشائعة والإصلاحات

1.  **عدم تثبيت PIL**
    إذا قمت بتثبيت `google-genai` ولكنك لم تقم بإضافة `Pillow`، فقد تفشل استدعاءات `.image.save()` بصمت (أو ترفع `AttributeError`). تأكد من:

    ```bash
    pip install pillow
    ```

2.  **عدم وجود مفتاح API أو خدمة خاطئة محددة**
    إذا استدعيت `genai.Client()` بدون مفتاح API وبدون بيانات اعتماد السحابة، فسيفشل العميل في وقت الاستدعاء بخطأ في المصادقة (مثل `"401 UNAUTHENTICATED"`). إما قم بتمرير `api_key="…"` أو اضبط `GOOGLE_API_KEY` في الطرفية الخاصة بك، لـ Gemini Developer API ([GitHub][1]).

3.  **عدم تطابق إصدار المكتبة**
    الإصدارات القديمة من المكتبة أو الوحدة القديمة `google.generativeai` لا تعرض دالة `generate_images()` وقد تظل تستخدم الواجهة *المهملة* generative-ai. تأكد دائمًا من:

    ```bash
    pip install --upgrade google-genai
    ```

    كانت مشكلة "لا يمكن فتح الصور الناتجة" في المستودعات القديمة (`deprecated-generative-ai-python`) ناتجة عن عدم التطابق هذا، وعادة ما كانت تظهر `UnidentifiedImageError` أو `FileNotFoundError` بعد كتابة بيانات بايت تالفة ([GitHub][1]).

4.  **خطأ UnidentifiedImageError عند الفتح باستخدام PIL**
    إذا رأيت:

    ```
    PIL.UnidentifiedImageError: cannot identify image file <_io.BytesIO …>
    ```

    فهذا يعني عادةً أن buffer الاستجابة تالف أو غير مكتمل. راجع مرة أخرى أن:

    * الـ prompt الخاص بك لم يتم حظره (مثلًا بواسطة RAI)؛
    * أنك لا تقوم بفك تشفير base64 للبايتات (حيث أن SDK يُرجع بيانات PNG/JPEG خام بالفعل)؛
    * أن تنزيل الملف الخاص بك لم ينقطع قبل اكتماله.

---

### ✅ لماذا يعمل هذا الإصلاح

* المقتطف الرسمي في وثائق Google بتاريخ 2025‑08‑01 يستخدم بالضبط:

  ```python
  types.GenerateImagesConfig(image_size="2K")
  ```

  قبل الحفظ عبر `result.image.save(...)` ([Google Cloud][2]).

* لكن الأدلة الأخرى التي تستخدم نماذج Imagen 3 تحدد فقط `number_of_images`، `aspect_ratio`، وإعدادات السلامة – بدون `image_size` – لأن Imagen 3 لا تدعمه ([GitHub][1]).

اتباع التدفقة أعلاه يجب أن يساعدك على تجاوز المشكلة. إذا واجهت رسالة خطأ محددة (مثل HTTP 403، أو فقدان مفتاح JSON في الاستجابة، إلخ)، فلا تتردد في لصقها هنا وسأساعدك في استكشاف الخطوة التالية.

[1]: https://github.com/google-gemini/generative-ai-python/issues/674?utm_source=chatgpt.com "can not open the output images from imagen API · Issue #674 · google-gemini/deprecated-generative-ai-python · GitHub"
[2]: https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview?utm_source=chatgpt.com "Imagen on Vertex AI | AI Image Generator"