---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إعدادات الصور من جوجل جين الذكاء الاصطناعي
translated: true
type: note
---

إليك نظرة سريعة: معلمة `image_size` غير مدعومة في Google Gen AI (Gemini/Imagen) Python SDK. بدلاً من ذلك، تختار من بين متغيرات النموذج (التي لكل منها دقة افتراضية ضمنية)، تتحكم في **النسبة الجانبية**، وإذا كنت بحاجة إلى عدد بكسلات أعلى، تطبق **تحسين الدقة**. يمكنك أيضًا ضبط **الضغط** و**تنسيق الإخراج**، بالإضافة إلى الإعدادات المعتادة مثل "عدد الصور"، و"المطالبة السلبية"، و"السلامة"، و"الإعدادات الشخصية".

## متغيرات النموذج

تختار اسم النموذج – لكل متغير دقته الافتراضية وملف أدائه الخاص:

* عائلة **imagen-3.0**:

  * `imagen-3.0-generate-002`
  * `imagen-3.0-generate-001`
  * `imagen-3.0-fast-generate-001`
  * `imagen-3.0-capability-001`
* عائلة **imagen-4.0 (معاينة)**:

  * `imagen-4.0-generate-preview-06-06`
  * `imagen-4.0-fast-generate-preview-06-06`
  * `imagen-4.0-ultra-generate-preview-06-06`
* **الإصدارات القديمة**: `imagegeneration@002`, `@005`, `@006` ([Google Cloud][1])

## الدقة الافتراضية

بشكل افتراضي، يكون الإخراج مربعًا ("1:1") من هذه النماذج هو **1024 × 1024 بكسل**. إذا كنت بحاجة إلى ملف أصغر، يمكنك تقليل الدقة محليًا؛ إذا كنت بحاجة إلى دقة أعلى، راجع **تحسين الدقة** أدناه. ([raymondcamden.com][2])

## النسب الجانبية

بدلاً من تحديد الأبعاد المطلقة، استخدم حقل `aspect_ratio` في `GenerateImagesConfig` الخاص بك. القيم المدعومة:

* `1:1` (مربع)
* `3:4` (أطول، صورة عمودية لوسائل التواصل الاجتماعي)
* `4:3` (التصوير الكلاسيكي / التلفزيون)
* `16:9` (المشاهد الطبيعية ذات الشاشة العريضة)
* `9:16` (طويل/عمودي، خلفيات الهاتف على سبيل المثال) ([Google Cloud][1], [Google AI for Developers][3])

ستجد نفس القائمة موثقة في البرامج التعليمية للمجتمع:

* تشير DataCamp إلى هذه النسب الخمسة نفسها لـ Imagen 3 ([DataCamp][4])
* يعدد دليل CodeSignal أيضًا لـ Gemini/Imagen ([CodeSignal][5])

## تحسين الدقة

إذا كنت بحاجة إلى مخرجات حقيقية بدقة "2K" أو "4K"، فاستدع وضع **تحسين الدقة**:

```python
from google.genai import types
config = types.GenerateImagesConfig(
    mode="upscale",
    upscale_config=types.UpscaleConfig(upscale_factor="x2"),
)
```

* `"x2"` يضاعف كل بُعد (مثال: 1024 → 2048، تقريبًا 2K)
* `"x4"` يضاعف أربع مرات (مثال: 1024 → 4096، تقريبًا 4K) ([Google Cloud][1])

## الضغط والتنسيقات

* **جودة JPEG**: استخدم `compression_quality` (0-100، الافتراضي 75) للمفاضلة بين حجم الملف والتفاصيل ([Google Cloud][1])
* **أنواع MIME**: عبر `output_options.mime_type`، يمكنك الاختيار من بين
  `image/jpeg`, `image/png`, `image/gif`, `image/webp`, `image/bmp`, `image/tiff`, أو `image/vnd.microsoft.icon` ([Google Cloud][6])

## خيارات التهيئة الإضافية

كل شيء آخر موجود في `GenerateImagesConfig`:

```python
config = types.GenerateImagesConfig(
    number_of_images=1,           # عدد الصور المراد إنشاؤها
    seed=1234,                    # للحصول على مخرجات حتمية
    enhance_prompt=True,          # إعادة كتابة المطالبة باستخدام LLM
    negative_prompt="exclude dogs",
    language="en",
    safety_filter_level="block_medium_and_above",  
    person_generation="allow_adult",
)
```

هذه تتيح لك التحكم في العشوائية، وتحسين المطالبة، وعتبات الأمان، وما إذا كان النموذج يمكنه تضمين الأشخاص. ([Google Cloud][1])

## التوصية

احذف سطر `image_size="2K"` الخاص بك – لا يوجد مثل هذا الخيار. بدلاً من ذلك:

1. **اختر النموذج المناسب** للمفاضلة بين السرعة والجودة.
2. استخدم **`aspect_ratio`** للتأطير.
3. إذا كنت بحاجة حقًا إلى عدد بكسلات أعلى، قم بإنشاء الصورة بالدقة الأساسية ثم طبق **تحسين الدقة** المدمج ("x2" أو "x4").
4. اضبط **compression\_quality** أو قلل الدقة محليًا للحصول على ملفات أصغر.

باستخدام هذه المقابض، يمكنك تحقيق تأطير مربع أو سينمائي، ومخرجات صغيرة أو عالية الدقة، دون الحاجة إلى معلمة `image_size` غير المدعومة.

[1]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api "Generate images  |  Generative AI on Vertex AI  |  Google Cloud"
[2]: https://www.raymondcamden.com/2025/01/30/generative-ai-images-with-gemini-and-imagen-an-introduction?utm_source=chatgpt.com "Generative AI Images with Gemini and Imagen"
[3]: https://ai.google.dev/gemini-api/docs/imagen?utm_source=chatgpt.com "Generate images using Imagen | Gemini API | Google AI for ..."
[4]: https://www.datacamp.com/tutorial/imagen-3 "Imagen 3: A Guide With Examples in the Gemini API | DataCamp"
[5]: https://codesignal.com/learn/courses/creating-images-with-geminis-imagen-and-flask/lessons/generating-a-simple-image-with-geminis-imagen-and-flask?utm_source=chatgpt.com "Generating a Simple Image with Gemini's Imagen and Flask"
[6]: https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images?utm_source=chatgpt.com "Generate images using text prompts"