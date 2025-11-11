---
audio: false
generated: true
image: false
lang: ar
layout: post
title: شرح نماذج اللغة الآمرة مقابل المبرمجة
translated: true
type: note
---

حسنًا — إليك مقارنة أوضح وأكثر سهولة للقارئ (بدون استخدام الجداول) بين نماذج **Instruct** ونماذج **Coder** (أو النماذج المتخصصة في البرمجة) في عالم نماذج اللغة الكبيرة:

---

## نماذج Instruct

*   **الغرض والضبط**
    يتم ضبط نماذج Instruct من نموذج لغة أساسي باستخدام أزواج التعليمات والاستجابة، وغالبًا ما يتم تعزيزها عبر **الضبط الخاضع للإشراف** و**التعلم التعزيزي من التغذية الراجعة البشرية** لاتباع توجيهات المستخدم بفعالية ([Medium][1], [arXiv][2]).

*   **نقاط القوة**
    تتقن هذه النماذج فهم وتنفيذ المهام المباشرة واللحظية، مثل تلخيص النص، والترجمة، والإجابة على الأسئلة، أو كتابة التعليمات البرمجية بناءً على تعليمات واضحة ([Dynamic Code Blocks][3], [ScrapingAnt][4], [Elastic][5]).

*   **العيوب مقارنة بالنماذج الأساسية**
    النموذج الأساسي (بدون ضبط للإرشادات) يشبه طالبًا واسع المعرفة لكنه غير مركز — قوي في فهم اللغة لكنه يفتقر إلى التخصص في المهام أو الالتزام بتوجيهاتك ([Medium][1]).

*   **Chat مقابل Instruct**
    تركز نماذج Instruct على الاستجابات الموجهة نحو المهام، بينما نماذج **chat** (المضبوطة للمحادثة) تكون أفضل في التعامل مع المحادثات متعددة الجولات والحفاظ على السياق خلال الحوار ([Reddit][6]).

---

## نماذج Coder / النماذج المتخصصة في البرمجة

*   **التدريب والهدف**
    يتم ضبط نماذج Code خصيصًا على مجموعات بيانات البرمجة وتحسينها لمهام مثل توليد التعليمات البرمجية، وملء الفراغات فيها، وإكمالها، أو تحريرها. يستخدم العديد منها أيضًا هدف **"ملء-المنتصف"** لإكمال أجزاء التعليمات البرمجية الجزئية ([Thoughtbot][7]).

*   **أمثلة وإمكانيات**

    *   **Code Llama – الإصدارات Instruct**: هذه نماذج تركز على البرمجة وتتبع التعليمات أيضًا، وتوفر أداءً قويًا في معايير مثل HumanEval و MBPP ([arXiv][8]).
    *   **DeepSeek Coder**: يقدم إصدارات Base و Instruct، تم تدريبه على كميات هائلة من التعليمات البرمجية مع دعم سياق طويل (حتى 16K رمز) ([Wikipedia][9]).
    *   **WizardCoder**: نموذج لغة برمجة تم تحسينه further بضبط التعليمات، محققًا نتائج من الطراز الأول — متفوقًا حتى على بعض النماذج المغلقة المصدر — في مهام مثل HumanEval ([arXiv][10]).

*   **التحرير مقابل التوليد**
    لا تتقن نماذج Coder توليد التعليمات البرمجية فحسب، بل أيضًا في تعديل التعليمات البرمجية الحالية (مثل إعادة الهيكلة، إضافة توثيق) عند إعطائها تعليمات صريحة — وهذا أكثر تعقيدًا من مجرد إكمال التعليمات البرمجية بشكل مباشر ([Reddit][6], [ACL Anthology][11]).

---

## الاختلافات الرئيسية باختصار

1.  **التركيز المجالي**

    *   نماذج *Instruct* هي نماذج للأغراض العامة ومحاذاة للإرشادات عبر مجالات عديدة (لغة، رياضيات، برمجة، إلخ).
    *   نماذج *Coder* مصممة خصيصًا لمهام البرمجة، وفهم هيكل التعليمات البرمجية، وبنيتها النحوية، وسياقها.

2.  **محاذاة التعليمات**

    *   بعض نماذج Coder (مثل Code Llama – Instruct أو WizardCoder) هي أيضًا مضبوطة بالإرشادات — ولكن خصيصًا للبرمجة.
    *   إذا لم يكن نموذج Coder مضبوطًا بالإرشادات، فقد يبرع في الإكمال ولكن قد يواجه صعوبة في اتباع الأوامر الدقيقة مثل "أعد هيكلة هذه الدالة."

3.  **أفضل حالات الاستخدام**

    *   نماذج *Instruct* ممتازة عندما تحتاج إلى قدرة واسعة على المهام (مثل "اشرح هذا المفهوم"، "اكتب ملخصًا"، أو "أنشئ شفرة زائفة").
    *   نماذج *Coder* تتفوق عندما يتعلق الأمر بالعمل البرمجي الحقيقي — كتابة، تصحيح أخطاء، إعادة هيكلة، أو إكمال أجزاء التعليمات البرمجية في السياق.

---

## رؤى وأمثلة من العالم الحقيقي

> في مناقشة على Reddit حول نماذج Qwen، لاحظ أحدهم أن النموذج الأساسي يتعامل مع البرمجة بشكل جيد بالفعل — ولكن من المرجح أن النسخة Coder تتفوق في مهام البرمجة، خاصةً عند أحجام النماذج المكافئة ([Get Business Grants][12], [arXiv][8], [Reddit][13]).

من المعايير العملية:

*   نموذج **Llama** من Meta (العام) يتفوق أحيانًا على **CodeLlama** في مهام البرمجة الواقعية، على الرغم من عدم تخصصه في البرمجة ([TechRadar][14]).
*   نموذج **Claude** من Anthropic (مثل Claude Code) يتفوق في سير عمل البرمجة — فهو يحافظ على سياق المشروع ويدمج بيانات الطرفية بشكل فعال لتذكر خطوات متعددة عبر المشروع ([businessinsider.com][15]).

---

## ملخص

*   **استخدم نموذج Instruct** عندما تغطي مهامك نطاقًا واسعًا (نص، الإجابة على الأسئلة، برمجة).
*   **استخدم نموذج Coder** عندما يكون تركيزك على كتابة التعليمات البرمجية بدقة، مع الوعي بالسياق، أو إكمالها، أو تحريرها.
*   **أفضل ما في العالمين؟** ابحث عن نماذج Coder التي هي أيضًا مضبوطة بالإرشادات (مثل Code Llama – Instruct، WizardCoder) لاتباع التعليمات المستهدفة في سياقات البرمجة.

هل تريد توصيات لنماذج محددة أو مساعدة في اختيار واحد لسير العمل الخاص بك؟

[1]: https://medium.com/%40yananchen1116/clearance-of-the-confusion-llms-base-and-instruct-version-48d4ef402591?utm_source=chatgpt.com "Clearance of the Confusion: LLM's base and instruct version"
[2]: https://arxiv.org/abs/2203.02155?utm_source=chatgpt.com "Training language models to follow instructions with human feedback"
[3]: https://timwappat.info/instruct-chat-llms-what-are-the-differences/?utm_source=chatgpt.com "What are the Differences Between Instruct, Chat, and Chat ..."
[4]: https://scrapingant.com/blog/llm-instruct-vs-chat?utm_source=chatgpt.com "LLM Instruct vs Chat - A Comprehensive Analysis"
[5]: https://www.elastic.co/what-is/large-language-models?utm_source=chatgpt.com "Understanding large language models"
[6]: https://www.reddit.com/r/LocalLLaMA/comments/16qvh2o/noob_question_whats_the_difference_between_chat/?utm_source=chatgpt.com "What's the difference between chat and instruct (or other? ..."
[7]: https://thoughtbot.com/blog/understanding-open-source-llms?utm_source=chatgpt.com "Understanding open source LLMs"
[8]: https://arxiv.org/abs/2308.12950?utm_source=chatgpt.com "Code Llama: Open Foundation Models for Code"
[9]: https://en.wikipedia.org/wiki/DeepSeek?utm_source=chatgpt.com "DeepSeek"
[10]: https://arxiv.org/abs/2306.08568?utm_source=chatgpt.com "WizardCoder: Empowering Code Large Language Models with Evol-Instruct"
[11]: https://aclanthology.org/2024.acl-srw.52.pdf?utm_source=chatgpt.com "Instruction Tuning Large Language Models for Code Editing"
[12]: https://getbusinessgrants.com/large-language-models-chat-vs-instruct-whats-the-difference/?utm_source=chatgpt.com "Large Language Models – Chat vs Instruct. What's the ..."
[13]: https://www.reddit.com/r/LocalLLaMA/comments/1gaxz5n/how_superior_is_coder_versions_of_llms_compared/?utm_source=chatgpt.com "How superior is Coder versions of LLMs compared to the ..."
[14]: https://www.techradar.com/computing/artificial-intelligence/best-large-language-models-llms-for-coding?utm_source=chatgpt.com "Best Large Language Models (LLMs) for coding of 2025"
[15]: https://www.businessinsider.com/anthropic-ai-breakthrough-vibe-coding-revolution-2025-7?utm_source=chatgpt.com "'The Trillion-Dollar Question': How did Anthropic make AI so good at coding?"