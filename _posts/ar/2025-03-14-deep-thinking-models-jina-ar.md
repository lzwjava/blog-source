---
audio: false
generated: true
lang: ar
layout: post
title: نماذج التفكير العميق
translated: true
type: note
---

هذه المعلومات مبنية على استعلام من https://search.jina.ai.

---

إليك تفصيلًا لنماذج التفكير العميق وتوفر واجهات برمجة التطبيقات (API) الخاصة بها، مصممة لتوفير فهم أعمق ومساعدتك في اختيار النموذج المناسب لاحتياجاتك:

*   **نماذج سلسلة o من OpenAI (o1، o3-mini، إلخ)**: هذه النماذج، المتاحة عبر خدمة Azure OpenAI [^1]， مصممة للتفكير المعقد، وتتفوق في العلوم والبرمجة والرياضيات. يتميز نموذج `o1`، على سبيل المثال، بنافذة سياق بقدرة 200,000 رمز ويمكن تحسين ضبطه باستخدام معلمة `reasoning_effort` لضبط وقت المعالجة [^2].

    *   **الوصول لواجهة برمجة التطبيقات (API):** يمكن الوصول إليه عبر واجهة برمجة تطبيقات خدمة Azure OpenAI مع إصدار واجهة برمجة التطبيقات `2024-12-01-preview` [^1].
    *   **التسعير:** يختلف تسعير Azure OpenAI بناءً على النموذج والاستخدام. تحقق من صفحة تسعير خدمة Azure OpenAI للحصول على معلومات مفصلة.
    *   **حدود المعدل:** تعتمد حدود المعدل على مستوى Azure OpenAI والمنطقة. راجع وثائق Azure OpenAI للحصول على التفاصيل.
    *   **الميزات المدعومة:** استدعاء الدالة (Function calling)، وضع JSON، إعدادات السلامة القابلة للتعديل [^3].
    *   **مثال برمجي (Python):**
        ```python
        from openai import AzureOpenAI
        client = AzureOpenAI(
          azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
          api_key=os.getenv("AZURE_OPENAI_API_KEY"),
          api_version="2024-12-01-preview"
        )
        response = client.chat.completions.create(
            model="o1-new", # استبدل باسم نشر النموذج o1 الخاص بك.
            messages=[
                {"role": "user", "content": "What steps should I think about when writing my first Python API?"},
            ],
            max_completion_tokens = 5000
        )
        print(response.model_dump_json(indent=2))
        ```
*   **DeepSeek R1**: معروف بمنافسته لنموذج o1 من OpenAI في معايير التفكير، تقدم DeepSeek نموذجها R1 عبر واجهة برمجة التطبيقات [^4]. توفر واجهة برمجة التطبيقات الوصول إلى محتوى سلسلة الأفكار (Chain of Thought - CoT) الذي يولده النموذج، مما يسمح للمستخدمين بمراقبة عملية التفكير الخاصة بالنموذج [^5]. توفر DeepSeek أيضًا بديلاً فعالاً من حيث التكلفة لـ OpenAI، حيث تقدم واجهة برمجة التطبيقات الكاملة لـ R1 بجزء بسيط من التكلفة [^6]. تتوفر واجهة برمجة تطبيقات DeepSeek-V3 أيضًا، بأداء يماثل النماذج المغلقة المصدر الرائدة [^7].

    *   **الوصول لواجهة برمجة التطبيقات (API):** واجهة برمجة تطبيقات DeepSeek، متوافقة مع تنسيق واجهة برمجة تطبيقات OpenAI [^8].
    *   **التسعير:** الرموز المدخلة \$0.14 لكل مليون رمز، الرموز المخرجة \$0.55 لكل مليون رمز [^9].
    *   **حدود المعدل:** راجع وثائق واجهة برمجة تطبيقات DeepSeek للحصول على حدود المعدل المحددة.
    *   **الميزات المدعومة:** إكمال الدردشة (Chat Completion)، إكمال بادئة الدردشة (Chat Prefix Completion) (Beta) [^10].
    *   **مثال برمجي (Python):**
        ```python
        from openai import OpenAI
        client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")
        messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=messages
        )
        print(response.choices[0].message.content)
        ```
        
*   **Grok (xAI)**: نماذج Grok من xAI، بما في ذلك Grok-3 وGrok-3 mini، مصممة بقدرات تفكير قوية. بينما كان Grok-1.5 متاحًا للمختبرين الأوائل، فإن Grok 3 قادم قريبًا عبر واجهة برمجة التطبيقات [^11]. تم تدريب نماذج Grok 3 (Think) وGrok 3 mini (Think) باستخدام التعلم المعزز لصقل عملية سلسلة الأفكار الخاصة بها، مما يمكنها من التفكير المتقدم بطريقة فعالة في استخدام البيانات [^12].

    *   **الوصول لواجهة برمجة التطبيقات (API):** من المتوقع إطلاق واجهة برمجة تطبيقات Grok 3 قريبًا [^11].
    *   **التسعير:** تفاصيل التسعير غير متاحة للعلن بعد. تحقق من موقع xAI للحصول على التحديثات.
    *   **حدود المعدل:** حدود المعدل غير متاحة للعلن بعد. تحقق من موقع xAI للحصول على التحديثات.
    *   **الميزات المدعومة:** استخدام الأدوات (Tool use)، تنفيذ التعليمات البرمجية (code execution)، وقدرات الوكيل المتقدمة (advanced agent capabilities) مخططة لواجهة برمجة التطبيقات Enterprise [^12].
*   **Gemini 1.5 Pro**: كونه نموذجًا من Google، يتفوق Gemini 1.5 Pro في التفكير عبر كميات كبيرة من المعلومات وهو مُحسّن لمجموعة واسعة من مهام التفكير [^13]. إنه نموذج متعدد الوسائط ويوفر قدرات تفكير أقوى، بما في ذلك عملية التفكير في الردود [^14]. تمنح واجهة برمجة تطبيقات Gemini المطورين الوصول إلى نافذة سياق بقدرة 2 مليون رمز [^15].

    *   **الوصول لواجهة برمجة التطبيقات (API):** متاح عبر واجهة برمجة تطبيقات Gemini [^15].
    *   **التسعير:** تحقق من صفحة تسعير Google AI Studio للحصول على معلومات مفصلة.
    *   **حدود المعدل:** 1,500 طلب في الدقيقة لتضمين النص (text embedding) [^16]. تحقق من وثائق Google AI Studio للحصول على حدود المعدل الأخرى.
    *   **الميزات المدعومة:** استدعاء الدالة (Function calling)، تنفيذ التعليمات البرمجية (code execution)، إعدادات السلامة القابلة للتعديل، وضع JSON [^17].

**رؤى مقارنة:**

| الميزة           | OpenAI o-series | DeepSeek R1      | Grok (xAI)       | Gemini 1.5 Pro   |
| :---------------- | :-------------- | :--------------- | :--------------- | :--------------- |
| الأداء       | قوي في STEM   | يماثل/يتفوق على o1-mini | تفكير قوي  | قوي بشكل عام   |
| الوصول لواجهة برمجة التطبيقات | Azure OpenAI    | DeepSeek API     | قريبًا          | Gemini API       |
| التكلفة              | يختلف          | فعال من حيث التكلفة     | غير متوفر بعد | تحقق من Google AI Studio |
| نافذة السياق    | 200K رمز      | 64K رمز          | 1M رمز          | 2M رمز           |
| حالات الاستخدام المقصودة | المهام المعقدة   | الرياضيات، البرمجة         | التفكير الواسع   | تحليل البيانات      |

**القيود:**

*   **OpenAI o-series:** قد لا ينتج تنسيق markdown افتراضيًا [^1].
*   **DeepSeek R1:** قد يتدهور الأداء للاستعلامات غير الإنجليزية/الصينية [^18].
*   **Grok (xAI):** واجهة برمجة التطبيقات غير مُطلقة بعد؛ معلومات محدودة حول القدرات المحددة.
*   **Gemini 1.5 Pro:** النماذج التجريبية ليست مخصصة للاستخدام في الإنتاج [^19].

[^1]: تم تصميم نماذج سلسلة o من Azure OpenAI لمعالجة مهام التفكير وحل المشكلات بتركيز وقدرة متزايدين [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/reasoning)

[^2]: تحتوي نماذج التفكير على رموز تفكير كجزء من رموز الإكمال التفاصيل في استجابة النموذج [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/reasoning)

[^3]: وضع JSON مدعوم [ai.google.dev](https://ai.google.dev/models/gemini)

[^4]: توفر واجهة برمجة التطبيقات الخاصة بنا للمستخدمين الوصول إلى محتوى CoT الذي يولده DeepSeek Reasoner مما يمكنهم من عرضه وعرضه وتقطيره [searchenginejournal.com](https://www.searchenginejournal.com/googles-ai-search-is-improving-but-still-lags-behind-human-quality-results/508459/)

[^5]: بتكلفة أقل بكثير وبأداء أعلى تقدم DeepSeek واجهة برمجة التطبيقات الكاملة لـ R1 مقارنة بـ OpenAI بجزء بسيط من التكلفة [seo-kueche.de](https://www.seo-kueche.de/blog/google-stellt-gemini-vor-das-kann-der-neue-ki-chatbot/)

[^6]: 全系模型均经过高精度微调 指令遵循强化 对于复杂语言理解 深度推理 文本生成 均有优秀的结果表现 [cloud.baidu.com](https://cloud.baidu.com/doc/wenxinworkshop/s/jlil5u56k)

[^7]: سيتم إطلاق واجهة برمجة تطبيقات xAI Grok 3 في الأسابيع القادمة [t.me](https://t.me/s/GPT4Telegram)

[^8]: اليوم نعلن عن نموذجين تجريبيين للتفكير Grok 3 Think وGrok 3 mini Think [x.ai](https://x.ai/blog/grok-3)

[^9]: Gemini 1.5 Pro هو نموذج متعدد الوسائط متوسط الحجم محسن لمجموعة واسعة من مهام التفكير [ai.google.dev](https://ai.google.dev/models/gemini)

[^10]: يوفر قدرات تفكير أقوى ويتضمن عملية التفكير في الردود [youtube.com](https://www.youtube.com/watch?v=YQAydVlHV7c)

[^11]: حد رمز الإدخال 2,097,152 [ai.google.dev](https://ai.google.dev/models/gemini)

[^12]: مع إيقاف تشغيل التفكير، يقدم Grok 3 ردودًا فورية عالية الجودة [x.ai](https://x.ai/blog/grok-3)

[^13]: Gemini 1.5 Pro هو نموذج متعدد الوسائط متوسط الحجم محسن لمجموعة واسعة من مهام التفكير يمكن لـ 1.5 Pro معالجة كميات كبيرة من البيانات مرة واحدة [ai.google.dev](https://ai.google.dev/models/gemini)

[^14]: افتراضيًا، لن تحاول نماذج o3 mini و o1 إنتاج مخرجات تتضمن تنسيق markdown [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/reasoning)

[^15]: تم تحسين DeepSeek R1 للغة الإنجليزية والصينية ولكن قد يتدهور أداؤه للاستعلامات بلغات أخرى [datacamp.com](https://datacamp.com/blog/deepseek-r1)

[^16]: تقدم واجهة برمجة التطبيقات نماذج تجريبية متاحة في المعاينة كما هو محدد في الشروط، مما يعني أن النماذج ليست مخصصة للاستخدام في الإنتاج [ai.google.dev](https://ai.google.dev/models/gemini)

[^17]: الوصول لواجهة برمجة التطبيقات: تطوير الذكاء الاصطناعي المخصص للمطورين تخطط xAI لإطلاق الوصول لواجهة برمجة التطبيقات لـ Grok 3، مما يسمح للمطورين بدمج [medium.com](https://medium.com/@gerardnico/a-timeline-to-grok-3-the-race-to-catch-up-54e0c0d1886c)

[^18]: نقدم DeepSeek R1، الذي يتضمن بيانات بدء باردة قبل RL يحقق DeepSeek R1 أداءً مماثلاً لـ OpenAI o1 عبر الرياضيات والبرمجة و [api-docs.deepseek.com](https://api-docs.deepseek.com/guides/reasoning_model)

[^19]: Gemini 1.5 Pro هو نموذج متعدد الوسائط متوسط الحجم محسن لمجموعة واسعة من مهام التفكير [ai.google.dev](https://ai.google.dev/models/gemini)