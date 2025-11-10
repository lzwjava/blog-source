---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إزالة العرض والارتفاع
translated: true
type: note
---

الخطأ الذي تراه:

```
Extra inputs are not permitted [type=extra_forbidden, input_value=1200, input_type=int]
```

سببه هو تمرير `width` و `height` إلى `GenerateImagesConfig`، والذي **لا يدعم** هذين الحقلين. وفقًا لرسالة الخطأ وتصميم واجهة برمجة تطبيقات Gemini، يجب أن تكون `image_size` واحدة من **قيم التعداد المحددة مسبقًا**، كما أن `CUSTOM` **غير مدعومة** لواجهة برمجة تطبيقات Gemini العامة (حتى الآن).

---

### ✅ الإصلاح

يجب عليك **إزالة** `width` و `height`، واستخدام قيمة تعداد صالحة لـ `image_size` مثل `"1024x1024"` أو `"512x512"`.

إليك النسخة المصححة:

```python
from google import genai
from google.genai.types import GenerateImagesConfig
import os

# إعداد عميل Vertex AI
client = genai.Client(
    vertexai=True,
    project=os.getenv('GOOGLE_CLOUD_PROJECT'),
    location=os.getenv('GOOGLE_CLOUD_LOCATION')
)

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=GenerateImagesConfig(
        image_size="1024x1024",  # استخدام قيمة مسموح بها بدلاً من CUSTOM
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

print(f"Created OG image using {len(image.generated_images[0].image.image_bytes)} bytes")
```

---

### 🔍 لإنشاء صورة **بحجم مخصص** مثل `1200x630`:

واجهات برمجة تطبيقات Gemini/Imagen العامة الحالية **لا تدعم** الأحجام التعسفية للصور. إذا كنت بحاجة إلى 1200×630 (على سبيل المثال، لصور OG)، فخياراتك هي:

1. **معالجة الصورة لاحقًا** بعد الإنشاء لتغيير حجمها/قصها إلى الأبعاد المطلوبة.
2. استخدام **نموذج/واجهة برمجة تطبيقات مختلفة** تدعم الأبعاد المخصصة (مثل Stability AI's SDXL، أو Midjourney، أو نقاط النهاية الخاصة).
3. إذا كنت تستخدم وصولاً داخليًا (داخل Google على سبيل المثال)، فقم بالتأكد من الوثائق الداخلية أو مدير حساب Vertex AI الخاص بك.

أعلمني إذا كنت تريد المساعدة في تغيير حجم الصورة بعد إنشائها.