---
audio: false
generated: true
image: false
lang: ar
layout: post
title: حظر المستويات المنخفضة وما فوق
translated: true
type: note
---

ترى هذا الخطأ:

```
Only block_low_and_above is supported for safetySetting.
```

يحدث هذا عندما تقوم بتعيين `safety_filter_level="BLOCK_MEDIUM_AND_ABOVE"` (أي أي قيمة أخرى) في `GenerateImagesConfig` لنماذج **Imagen‑4** — ولكن في وقت طلبك (أغسطس 2025)، **تسمح واجهة البرمجة فقط بـ `"BLOCK_LOW_AND_ABOVE"`** لتصفية الأمان للصور على تلك النماذج ([Google Cloud][1]).

---

### ✅ كيفية إصلاح الكود الخاص بك

ما عليك سوى تحديث `safety_filter_level` إلى القيمة المدعومة:

```python
from google import genai
from google.genai.types import GenerateImagesConfig

client = genai.Client()

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=GenerateImagesConfig(
        image_size="2K",
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

image.generated_images[0].image.save("output-image.png")
print(
    f"Created image using {len(image.generated_images[0].image.image_bytes)} bytes"
)
```

* `safety_filter_level="BLOCK_LOW_AND_ABOVE"`: هذه فقط هي المدعومة لـ **Imagen 4**. العتبات الأخرى مثل `"BLOCK_MEDIUM_AND_ABOVE"` ستتسبب في خطأ 400 INVALID\_ARGUMENT ([Medium][2], [Google AI for Developers][3]).
* `number_of_images=1` واضحة بحيث يكون من الواضح أنك تطلب صورة واحدة في كل استدعاء.

---

### 🧾 معلمات اختيارية أخرى:

* `person_generation="ALLOW_ADULT"` هو الإعداد الافتراضي، ولكن لا بأس من أن تكون صريحًا (يحظر الأطفال؛ يسمح بالصور ذات النطاق للبالغين) ([Google Cloud][1]).
* `image_size="2K"` صالح وفقًا للكود الخاص بك — فقط تأكد من أن إصدار SDK الذي تستخدمه يدعمه.

---

### TL;DR — قائمة مراجعة سريعة

| الخطوة | ما يجب فعله                                                   |
| ---- | ------------------------------------------------------------ |
| ✅ 1  | غيّر safety\_filter\_level إلى `"BLOCK_LOW_AND_ABOVE"`      |
| 🧾 2 | احتفظ بـ `person_generation="ALLOW_ADULT"` (أو احذفه للاستخدام الافتراضي) |
| 🚫 3 | لا تستخدم `"BLOCK_MEDIUM_AND_ABOVE"` أو `"BLOCK_ONLY_HIGH"`  |
| ⏱ 4  | لا تغير إعدادات الأمان مرة أخرى حتى تضيف Google مستويات أكثر      |

أعلمني إذا ظهر خطأ آخر — يسعدني المساعدة!

[1]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api?utm_source=chatgpt.com "Generate images | Generative AI on Vertex AI"
[2]: https://medium.com/generative-ai/3-ways-to-try-googles-imagen-4-image-generator-if-you-re-outside-the-us-ee2a1895ca9b?utm_source=chatgpt.com "3 Ways to Try Google's Imagen 4 Image Generator if You're ..."
[3]: https://ai.google.dev/gemini-api/docs/migrate?utm_source=chatgpt.com "Migrate to the Google GenAI SDK - Gemini API"