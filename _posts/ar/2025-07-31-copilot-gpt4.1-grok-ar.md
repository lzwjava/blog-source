---
audio: false
generated: true
image: false
lang: ar
layout: post
title: تهيئة Copilot للنماذج المخصصة
translated: true
type: note
---

عندما تختار "النماذج المدارة" في GitHub Copilot ولا تزال ترى GPT-4.1 كالإعداد الافتراضي، أو لا يمكنك استخدام نماذج Grok أو Kimi من OpenRouter كما هو متوقع، هناك بعض الأسباب المحتملة والخطوات لمعالجة هذا الأمر. إليك تحليلًا للمشكلة وكيفية تكوين Copilot لاستخدام نماذج Grok أو Kimi عبر OpenRouter:

### لماذا لا يزال GPT-4.1 مستخدمًا
1.  **إعداد النموذج الافتراضي**: GitHub Copilot يستخدم GPT-4.1 افتراضيًا لـ Copilot Chat وEdits وAgent Mode ما لم يتم تغييره صراحةً. حتى عند اختيار "النماذج المدارة"، قد يظل النموذج الافتراضي ساريًا إذا لم تقم بتكوين تكامل OpenRouter بالكامل أو تحديد نموذج معين.
2.  **استخدام النموذج حسب السياق**: "صندوق الإصلاح" (الدردشة المضمنة أو إكمال الكود) في Copilot قد لا يدعم التبديل إلى نماذج مخصصة مثل Grok أو Kimi في سياقات معينة. على سبيل المثال، قد تستخدم لوحة Copilot Chat أو الاقتراحات المضمنة النموذج الافتراضي (GPT-4.1) ما لم تنتقل صراحةً إلى نموذج مخصص في الوضع الغامر أو Agent Mode.
3.  **قيود تكامل OpenRouter**: يسمح OpenRouter بالوصول إلى نماذج مثل Grok (المطور من xAI) وKimi (من Moonshot AI)، لكن تكامل Copilot مع OpenRouter يتطلب إعدادًا محددًا، وقد لا تكون جميع النماذج متاحة فورًا بسبب قيود API أو مشاكل في التكوين. على سبيل المثال، قد لا تعلن واجهة برمجة تطبيقات OpenRouter عن دعم الأدوات لجميع النماذج، مما قد يمنع Agent Mode أو بعض الميزات من العمل مع Grok أو Kimi.
4.  **قيود الاشتراك أو التكوين**: إذا كنت تستخدم الطبقة المجانية أو اشتراك Copilot غير Pro/Business، فقد تكون مقيدًا بالنماذج الافتراضية مثل GPT-4.1. بالإضافة إلى ذلك، قد تتطلب بعض النماذج (مثل Grok أو Kimi) تكوينات محددة أو وصولاً متميزًا عبر OpenRouter.

### كيفية استخدام نماذج Grok أو Kimi في Copilot عبر OpenRouter
لاستخدام نماذج Grok أو Kimi من OpenRouter في Copilot، خاصةً لـ "صندوق الإصلاح" (الدردشة المضمنة أو إكمال الكود)، اتبع هذه الخطوات:

1.  **إعداد OpenRouter مع Copilot**:
    *   **احصل على مفتاح OpenRouter API**: سجل الدخول في [openrouter.ai](https://openrouter.ai) واحصل على مفتاح API. تأكد من أن لديك رصيدًا أو خطة تدعم الوصول إلى نماذج Grok (xAI) وKimi (Moonshot AI K2).
    *   **قم بتكوين OpenRouter في VS Code**:
        *   افتح Visual Studio Code (VS Code) وتأكد من تثبيت أحدث إضافة لـ GitHub Copilot (الإصدار v1.100.2 أو أحدث).
        *   انتقل إلى لوحة تحكم Copilot في شريط الحالة، أو افتح Command Palette (`Ctrl+Shift+P` أو `Command+Shift+P` على نظام Mac) واكتب `GitHub Copilot: Manage Models`.
        *   أضف مفتاح OpenRouter API وقم بتكوين endpoint لتضمين نماذج OpenRouter. قد تحتاج إلى اتباع وثائق OpenRouter للتكامل مع إضافة Copilot في VS Code.
    *   **تحقق من توفر النموذج**: بعد إضافة endpoint الخاص بـ OpenRouter، تحقق من قسم "Manage Models" في Copilot. يجب أن تظهر نماذج مثل `openrouter/xai/grok` أو `openrouter/moonshotai/kimi-k2` في منتقي النماذج. إذا لم تظهر، فتأكد من أن حساب OpenRouter الخاص بك لديه حق الوصول إلى هذه النماذج وأنه لا توجد قيود (مثل قيود الطبقة المجانية).

2.  **تبديل النماذج لصندوق الإصلاح**:
    *   **للدردشة المضمنة (صندوق الإصلاح)**: يشير "صندوق الإصلاح" على الأرجح إلى ميزة الدردشة المضمنة أو إكمال الكود في Copilot. لتغيير النموذج للدردشة المضمنة:
        *   افتح واجهة Copilot Chat في VS Code (عبر الأيقونة في شريط العنوان أو الشريط الجانبي).
        *   في عرض الدردشة، حدد القائمة المنسدلة `CURRENT-MODEL` (عادةً في أسفل اليمين) واختر `openrouter/xai/grok` أو `openrouter/moonshotai/kimi-k2` إذا كانت متاحة.
        *   إذا لم تعرض القائمة المنسدلة Grok أو Kimi، فقد يكون السبب هو أن واجهة برمجة تطبيقات OpenRouter لا تعلن عن دعم الأدوات لهذه النماذج، مما قد يحد من استخدامها في ميزات معينة في Copilot مثل Agent Mode أو الإصلاحات المضمنة.
    *   **لإكمال الكود**: لتغيير النموذج لإكماليات الكود (وليس الدردشة فقط):
        *   افتح Command Palette (`Ctrl+Shift+P` أو `Command+Shift+P`) واكتب `GitHub Copilot: Change Completions Model`.
        *   حدد نموذج OpenRouter المطلوب (مثل Grok أو Kimi) من القائمة. لاحظ أنه قد لا تدعم جميع نماذج OpenRouter إكمال الكود بسبب القيد الحالي في VS Code الذي يدعم فقط نقاط نهاية Ollama للنماذج المخصصة، على الرغم من أن OpenRouter يمكن أن يعمل مع حل بديل باستخدام proxy.

3.  **حل بديل لنماذج OpenRouter**:
    *   **حل الـ Proxy**: نظرًا لأن واجهة برمجة تطبيقات OpenRouter لا تعلن دائمًا عن دعم الأدوات (المطلوب لـ Agent Mode أو الميزات المتقدمة)، يمكنك استخدام proxy مثل `litellm` لتمكين Grok أو Kimi في Copilot. قم بتحرير ملف `config.yaml` لتضمين:
        ```yaml
        model_list:
          - model_name: grok
            litellm_params:
              model: openrouter/xai/grok
          - model_name: kimi-k2
            litellm_params:
              model: openrouter/moonshotai/kimi-k2
        ```
        *   اتبع تعليمات الإعداد من مصادر مثل [Bas codes](https://bas.codes) أو [DEV Community](https://dev.to) للحصول على خطوات مفصلة حول تكوين الـ proxy.
    *   **أعد تشغيل VS Code**: بعد تكوين الـ proxy، أعد تشغيل VS Code لضمان توفر النماذج الجديدة في منتقي النماذج.

4.  **تحقق من الاشتراك والصلاحيات**:
    *   **اشتراك Copilot**: تأكد من أن لديك اشتراك Copilot Pro أو Business، حيث قد لا يكون لمستخدمي الطبقة المجانية خيار إضافة نماذج مخصصة.
    *   **قيود العمل**: إذا كنت تستخدم اشتراك Copilot Business، فيجب على مؤسستك تمكين تبديل النماذج. تحقق من مسؤولك أو راجع وثائق GitHub حول إدارة سياسات Copilot.
    *   **رصيد OpenRouter**: تحقق من أن حساب OpenRouter الخاص بك لديه رصيد كافٍ للوصول إلى النماذج المتميزة مثل Grok أو Kimi، حيث قد تستهلك هذه النماذج رصيدًا أكثر من غيرها.

5.  **استكشاف أخطاء صندوق الإصلاح وإصلاحها**:
    *   إذا كان صندوق الإصلاح لا يزال يستخدم GPT-4.1، فقد يكون ذلك لأن ميزة الدردشة المضمنة مقيدة بالنموذج الافتراضي في سياقات معينة (مثل العرض غير الغامر). حاول التبديل إلى الوضع الغامر لـ Copilot Chat (`https://github.com/copilot`) لتحديد Grok أو Kimi صراحةً.
    *   إذا لم تظهر Grok أو Kimi في منتقي النماذج، فتحقق مرة أخرى من تكامل OpenRouter في `Manage Models`. قد تحتاج إلى تحديث قائمة النماذج أو إعادة إضافة مفتاح OpenRouter API.
    *   إذا استمرت المشكلة، فاختبر النماذج في Agent Mode أو واجهة الدردشة في Copilot أولاً للتأكد من أنها تعمل، ثم حاول تطبيقها على الإصلاحات المضمنة.

6.  **أدوات بديلة**:
    *   إذا ظل تكامل OpenRouter مع Copilot إشكاليًا، ففكر في استخدام Grok مباشرة عبر [grok.com](https://grok.com) أو تطبيقات Grok لنظام iOS/Android، والتي تقدم وصولاً مجانيًا مع حصص استخدام. يمكن أيضًا اختبار نماذج Kimi عبر واجهة الدردشة في OpenRouter للتأكد من إمكانية الوصول إليها.
    *   للحصول على تجربة أكثر سلاسة، يمكنك استكشاف بيئات التطوير المتكاملة أو الأدوات الأخرى مثل Cursor، والتي لوحظ أنها تعمل بشكل جيد مع نموذج Kimi K2 من OpenRouter.

### ملاحظات إضافية
*   **أداء النموذج**: تم تحسين Grok للاستدلال والسعي وراء الحقيقة، مما يجعله مناسبًا لمهام تصحيح الأخطاء المعقدة أو المهام المعمارية، بينما قد يتفوق Kimi (K2) في سيناريوهات البرمجة المحددة. اختبر كليهما لترى أيهما يعمل بشكل أفضل لحالة استخدامك.
*   **ملاحظات المجتمع**: يبلغ بعض المستخدمين عن مشاكل في عدم ظهور نماذج OpenRouter في منتقي نماذج Copilot، خاصةً مع الحسابات ذات الطبقة المجانية. قد يتطلب هذا الحصول على خطة OpenRouter مدفوعة أو اشتراك Copilot Pro لحلها.
*   **القيود المستمرة**: هناك مناقشة مفتوحة حول تمكين نقاط نهاية API المخصصة مباشرة في Copilot. حتى يتم تنفيذ ذلك، يظل حل الـ proxy البديل هو الطريقة الأكثر موثوقية لاستخدام Grok أو Kimi.

### الاستشهادات
*   [Changing the AI model for Copilot Chat - GitHub Docs](https://docs.github.com/en/copilot/managing-copilot/changing-the-ai-model-for-copilot-chat)
*   [How to Use Third Party Models in GitHub Copilot Agent Mode - Bas codes](https://bas.codes)
*   [Openrouter - openrouter.ai](https://openrouter.ai)
*   [Agent Mode With Third-Party Models in Copilot - DEV Community](https://dev.to)
*   [r/LocalLLaMA on Reddit: Github Copilot now supports Ollama and OpenRouter Models](https://www.reddit.com)
*   [Which AI model should I use with GitHub Copilot? - The GitHub Blog](https://github.blog)
*   [OpenAI GPT-4.1 is now generally available in GitHub Copilot - GitHub Changelog](https://github.blog)
*   [OpenRouter (free) Models Missing from Manage Models - GitHub Issues](https://github.com/microsoft/vscode-copilot-release/issues/10193)

إذا واجهت أخطاء محددة أو تحتاج إلى مزيد من المساعدة في الإعداد، يرجى تقديم المزيد من التفاصيل (على سبيل المثال، رسائل الخطأ، إصدار VS Code، أو نوع الاشتراك)، ويمكنني تخصيص الحل بشكل أكبر!