---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دليل معاينة جوجل إيماجن 4
translated: true
type: note
---

لاستخدام Google Imagen 4 Preview 0606، تحتاج إلى الوصول إليه من خلال منصة Vertex AI من جوجل، حيث أنه عرض معاينة للذكاء الاصطناعي التوليدي مصمم لتوليد الصور من النص. فيما يلي دليل خطوة بخطوة استنادًا إلى المعلومات المتاحة:

### كيفية استخدام Google Imagen 4 Preview 0606

1.  **الوصول إلى Vertex AI**:
    *   **المنصة**: Imagen 4 Preview 0606 متاح على Google Cloud’s Vertex AI. ستحتاج إلى حساب Google Cloud للبدء.
    *   **اشتراك**: إذا لم يكن لديك حساب، فاشترك في [cloud.google.com](https://cloud.google.com) وقم بإعداد مشروع. تأكد من تفعيل الفواتير، حيث أن هذا عرض معاينة قد يتضمن تكاليف (تفاصيل التسعير متاحة في قسم Imagen في صفحة تسعير Vertex AI).
    *   **انتقل إلى Vertex AI**: بمجرد تسجيل الدخول، انتقل إلى قسم Vertex AI في Google Cloud Console وابحث عن أدوات الذكاء الاصطناعي التوليدي.

2.  **إعداد البيئة**:
    *   **المصادقة**: قم بمصادقة حسابك باستخدام بيانات اعتماد Google Cloud. يمكنك إنشاء رمز وصول باستخدام الأمر:
        ```bash
        gcloud auth print-access-token
        ```
    *   **المشروع والموقع**: عيّن معرف مشروع Google Cloud والموقع (مثل `us-central1`). مثال:
        ```bash
        export GOOGLE_CLOUD_PROJECT=your-project-id
        export GOOGLE_CLOUD_LOCATION=us-central1
        ```

3.  **استخدام نموذج Imagen 4**:
    *   **الوصول إلى API**: يمكن الوصول إلى Imagen 4 Preview 0606 عبر Vertex AI API. استخدم نقطة النهاية للنموذج `imagen-4.0-generate-preview-06-06`. يمكنك التفاعل معه برمجيًا باستخدام أدوات مثل cURL أو Google Gen AI SDK لـ Python.
    *   **مثال لطلب cURL**:
        ```bash
        curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        "https://${GOOGLE_CLOUD_LOCATION}-aiplatform.googleapis.com/v1/projects/${GOOGLE_CLOUD_PROJECT}/locations/${GOOGLE_CLOUD_LOCATION}/publishers/google/models/imagen-4.0-generate-preview-06-06:predict" \
        -d '{"instances": [{"prompt": "A cat reading a book"}], "parameters": {"sampleCount": 1}}'
        ```
        هذا يعيد صورة مشفرة بـ base64.
    *   **مثال بـ Python SDK**:
        ```python
        from google import genai
        from google.genai.types import GenerateImagesConfig
        client = genai.Client()
        image = client.models.generate_images(
            model="imagen-4.0-generate-preview-06-06",
            prompt="A dog reading a newspaper",
            config=GenerateImagesConfig(image_size="2K")
        )
        image.generated_images[0].image.save("output-image.png")
        print(f"Created output image using {len(image.generated_images[0].image.image_bytes)} bytes")
        ```
        يولد هذا صورة ويحفظها كملف PNG.

4.  **صياغة Prompts فعالة**:
    *   **هيكل الـ Prompt**: للحصول على أفضل النتائج، استخدم prompts مفصلة ومحددة. قم بتضمين الموضوع، والبيئة، والأسلوب الفني (مثل التصوير الواقعي، التجريدي)، والحالة المزاجية، وعناصر التكوين (مثل زاوية الكاميرا). مثال: "رسم جرافيكي حيوي لمدينة مستقبلية عند غروب الشمس، بأسلوب الـ cyberpunk، مع أضواء النيون ومنظور منخفض درامي."
    *   **نصائح**:
        *   كن دقيقًا: الـ prompts الغامضة قد تؤدي إلى نتائج غير متوقعة.
        *   تجنب المدخلات غير المنطقية (مثل الرموز التعبيرة العشوائية)، لأنها يمكن أن تنتج مخرجات غير متسقة.
        *   حدد النص إذا لزم الأمر، حيث أن Imagen 4 لديه تحسين في عرض الطباعة.
    *   **الـ Prompts السلبية**: يمكنك استخدام الـ prompt السلبي لاستبعاد العناصر غير المرغوب فيها (مثل "لا نص" إذا كنت لا تريد نصًا في الصورة).

5.  **استكشاف المتغيرات**:
    *   يحتوي Imagen 4 Preview 0606 على متغيرات مثل **Fast** (أسرع حتى 10 مرات، مُحسّن للتوليد الجماعي) و **Ultra** (محاذاة أعلى مع الـ prompts للاستخدام الاحترافي). تحقق مما إذا كانت هذه المتغيرات متاحة في واجهة Vertex AI الخاصة بك واختر بناءً على احتياجاتك (مثل Fast للنماذج الأولية السريعة، Ultra للمخرجات عالية الجودة).

6.  **مراجعة المخرجات وميزات السلامة**:
    *   **تنسيقات المخرجات**: يتم إنشاء الصور بتنسيقات قياسية مثل PNG أو JPEG، بدقة تصل إلى 2K.
    *   **علامة مائية SynthID**: تحتوي جميع الصور على علامة مائية رقمية غير مرئية لتحديدها على أنها مولدة بالذكاء الاصطناعي، مما يضمن الشفافية.
    *   **قيود المحتوى**: يستخدم Imagen 4 التصفية لتقليل المحتوى الضار، ولكن قد يواجه صعوبة في التراكيب المعقدة، أو الوجوه الصغيرة، أو الصور المتمركزة تمامًا. راجع إرشادات الاستخدام من جوجل لمعرفة قيود المحتوى.

7.  **منصات بديلة**:
    *   Imagen 4 متاح أيضًا على منصات الطرف الثالث مثل Replicate، أو fal.ai، أو AI/ML API، والتي قد تقدم واجهات أبسط أو بيئات تجريبية للاختبار. على سبيل المثال:
        *   **Replicate**: شغّل Imagen 4 باستخدام prompt مثل "منظر جبلي هادئ عند غروب الشمس، بأسلوب فائق الواقعية." تحقق من وثائق Replicate للحصول على مفاتيح API والاستخدام.
        *   **fal.ai**: استخدم API الخاص بهم مع طلب مثل:
            ```javascript
            const result = await fal.subscribe("fal-ai/imagen4/preview", {
                input: { prompt: "A serene mountain landscape at sunset, hyperrealistic style" }
            });
            console.log(result.images[0].url);
            ```
            تختلف الأسعار (مثل 0.04 دولار للصورة لـ Standard، 0.04 دولار لـ Fast، 0.06 دولار لـ Ultra).
    *   **تطبيق Gemini أو Google Workspace**: تم دمج Imagen 4 في تطبيق Gemini، وGoogle Slides، وDocs، وVids لتوليد الصور مباشرة في سير العمل. على سبيل المثال، في Google Docs، يمكنك إنشاء الصور لتوضيح المستندات.

8.  **اختبار والتكرار**:
    *   جرب الـ prompts في بيئة تجريبية (مثل Google AI Studio للاختبار المجاني المحدود) قبل التكامل في الإنتاج.
    *   راقب استخدام API والتكاليف من خلال لوحة تحكم المنصة، حيث قد يكون لعروض المعاينة دعم محدود أو ميزات متغيرة.

### ملاحظات إضافية
*   **التسعير**: تحقق من صفحة تسعير Vertex AI لتكاليف Imagen 4 (مثل 0.04 دولار للصورة لـ Standard، 0.06 دولار للصورة لـ Ultra).
*   **القيود**: قد يواجه Imagen 4 صعوبة في الـ prompts الغامضة، أو الوجوه الصغيرة، أو التراكيب المتمركزة تمامًا. استخدم prompts واضحة ومنظمة للحصول على أفضل النتائج.
*   **التوفر**: كعرض معاينة، قد تتغير الميزات والدعم. تحقق من أوصاف مرحلة الإطلاق في Google Cloud للحصول على التحديثات.

للحصول على وثائق مفصلة، قم بزيارة [صفحة Vertex AI Imagen](https://cloud.google.com/vertex-ai/docs/generative-ai/image/overview) أو [مدونة مطوري جوجل](https://developers.googleblog.com). للوصول إلى API، راجع [x.ai/api](https://x.ai/api) للحصول على إرشادات API العامة للذكاء الاصطناعي، على الرغم من أن تفاصيل Imagen 4 المحددة موجودة على Google Cloud.

إذا كنت بحاجة إلى مساعدة بخصوص منصة أو حالة استخدام محددة، فأخبرني!