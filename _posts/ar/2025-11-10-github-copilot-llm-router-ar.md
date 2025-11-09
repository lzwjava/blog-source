---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تهيئة موجه نموذج اللغة الضخم لـ GitHub Copilot
translated: true
type: note
---

لتكوين موجه LLM الخاص بك لاستخدام حصريًا لواجهة برمجة تطبيقات LLM الخاصة بـ GitHub Copilot في بيئة المؤسسة، أضف موفرًا مخصصًا له وضبط إعدادات الموجه لتوجيه كل الحركة عبر ذلك الموفر.

- **إضافة موفر GitHub Copilot**: قم بتضمين إدخال جديد في مصفوفة "الموفرين" مع عنوان URL الأساسي المناسب لواجهة برمجة التطبيقات، ورمز الوصول الشخصي (PAT) الخاص بـ GitHub كـ "مفتاح واجهة برمجة التطبيقات"، والنماذج المدعومة.
- **تحديث الإعدادات الافتراضية للموجه**: قم بتغيير جميع حقول الموجه (مثل "default", "think") للإشارة فقط إلى اسم الموفر الجديد، مما يضمن عدم استدعاء أي موفرين آخرين.
- **معالجة قيود المؤسسة**: استخدم رمز الوصول الشخصي (PAT) لحساب المؤسسة الخاص بـ GitHub مع النطاقات المطلوبة، واستخدم "PROXY_URL" الموجود إذا كانت بيئتك تتطلب توجيه الوكيل للامتثال.
- **الاختيار والتحقق**: بعد التحديثات، تحقق من توجيه جميع استدعاءات واجهة برمجة التطبيقات فقط إلى نقطة نهاية Copilot لمواءمتها مع السياسات التي تسمح فقط بتفاعلات واجهة برمجة تطبيقات Copilot.

### التكوين خطوة بخطوة
1. **إنشاء رمز وصول شخصي (PAT) لـ GitHub**: سجل الدخول إلى حساب المؤسسة الخاص بك على GitHub وأنشئ رمز وصول شخصي بنطاقات مثل `copilot` للوصول إلى الدردشة أو `models:read` لاستدلال النموذج الأوسع. يضمن هذا المصادقة الآمنة دون الكشف عن أذونات أوسع.
2. **تعديل مصفوفة الموفرين**: أضف كائنًا جديدًا إلى قائمة "الموفرين" في ملف التكوين JSON الخاص بك. عيّن "name" لشيء وصفي مثل "github_copilot"، و "api_base_url" إلى "https://api.githubcopilot.com/chat/completions" (لوكلاء Copilot) أو "https://models.github.ai/inference/chat/completions" (لاستدلال GitHub Models العام)، و "api_key" إلى رمز PAT الخاص بك، واذكر النماذج المتوافقة.
3. **ضبط قسم الموجه**: استبدل جميع القيم في كائن "Router" باسم الموفر الجديد (مثل "github_copilot") لفرض الاستخدام الحصري. هذا يمنع الرجوع إلى موفرين آخرين مثل OpenRouter.
4. **اعتبارات المؤسسة**: في البيئات المقيدة، تأكد من أن سياسات الشبكة الخاصة بك تسمح بالمكالمات الصادرة إلى نطاقات GitHub. إذا لزم الأمر، قم بتحديث "PROXY_URL" للتوجيه عبر وكيل المؤسسة المعتمد. قم بتمكين التسجيل ("LOG": true) لمراجعة المكالمات وضمان الامتثال.

### مثال على التكوين المحدث
إليك كيف قد يبدو التكوين الخاص بك بعد التعديلات (استبدل العناصر النائبة برمز PAT الفعلي ونقطة النهاية المفضلة):

```json
{
  "PROXY_URL": "http://127.0.0.1:7890",
  "LOG": true,
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "",
      "models": [
        "moonshotai/kimi-k2",
        "anthropic/claude-sonnet-4",
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-3.7-sonnet:thinking",
        "anthropic/claude-opus-4",
        "google/gemini-2.5-flash",
        "google/gemini-2.5-pro",
        "deepseek/deepseek-chat-v3.1",
        "deepseek/deepseek-r1",
        "mistralai/mistral-medium-3.1",
        "qwen/qwen3-coder",
        "openai/gpt-oss-120b",
        "openai/gpt-5",
        "z-ai/glm-4.6",
        "x-ai/grok-code-fast-1",
        "x-ai/grok-4-fast",
        "minimax/minimax-m2",
        "moonshotai/kimi-k2-thinking"
      ],
      "transformer": {
        "use": [
          "openrouter"
        ]
      }
    },
    {
      "name": "github_copilot",
      "api_base_url": "https://api.githubcopilot.com/chat/completions",
      "api_key": "ghp_YourPersonalAccessTokenHere",
      "models": [
        "gpt-4o",
        "gpt-4o-mini",
        "claude-3-5-sonnet-20240620"
      ],
      "transformer": {
        "use": [
          "github_copilot"
        ]
      }
    }
  ],
  "Router": {
    "default": "github_copilot",
    "background": "github_copilot",
    "think": "github_copilot",
    "longContext": "github_copilot",
    "longContextThreshold": 30000,
    "webSearch": "github_copilot"
  }
}
```

يضمن هذا الإعداد تفاعل الموجه فقط مع واجهة برمجة تطبيقات Copilot، مما يتوافق مع سياسات المؤسسة التي تقيد المكالمات إلى نقاط النهاية المعتمدة.

---

في بيئات المؤسسات، يتطلب دمج واجهات برمجة تطبيقات LLM مثل GitHub Copilot تكوينًا دقيقًا للامتثال لسياسات الأمان، مما يحد في كثير من الأحيان من المكالمات الصادرة إلى خدمات معتمدة محددة. يبدو تكوين الموجه المقدم عبارة عن إعداد مخصص لتوجيه طلبات LLM عبر الموفرين، على غرار أدوات مثل OpenRouter أو LiteLLM، حيث تحدد "الموفرون" نقاط نهاية واجهة برمجة التطبيقات والنماذج، ويحدد "الموجه" التوجيه الاحتياطي أو الخاص بفئة معينة. للتكيف مع الاستخدام الحصري لواجهة برمجة تطبيقات LLM الخاصة بـ GitHub Copilot - مما يضمن عدم استدعاء أي خدمات خارجية أخرى - ستحتاج إلى دمج Copilot كموفر وفرضه عبر جميع مسارات الموجه. يدعم هذا النهج السيناريوهات التي تسمح فيها جدران الحماية الخاصة بالمؤسسة أو قواعد الامتثال فقط بواجهات برمجة التطبيقات المستضافة على GitHub، مستفيدةً من واجهة Copilot المتوافقة مع OpenAI لإكمال المحادثات.

يوفر GitHub Copilot الوصول إلى LLM بشكل أساسي من خلال قناتين: نقطة نهاية LLM المخصصة لـ Copilot لبناء الوكلاء والإضافات، وواجهة برمجة تطبيقات GitHub Models الأوسع للاستدلال العام. تم تصميم نقطة النهاية الخاصة بـ Copilot على `https://api.githubcopilot.com/chat/completions` خصيصًا لتطوير الوكلاء من مستوى المؤسسة، حيث تدعم طلبات POST بتنسيق إكمال محادثة OpenAI. تستخدم المصادقة رمز Bearer المشتق من رمز الوصول الشخصي (PAT) لـ GitHub، يتم تمريره عادةً عبر رأس `Authorization`. على سبيل المثال، قد يتضمن طلب عينة رؤوسًا مثل `Authorization: Bearer <your-pat>` و `Content-Type: application/json`، مع نص يحتوي على `messages` (مصفوفة من مطالبات المستخدم/النظام) ومعلمات اختيارية مثل `stream: true` للردود في الوقت الفعلي. لا يتم سرد النماذج صراحةً في الوثائق ولكنها تتماشى مع موفري Copilot الأساسيين، مثل متغيرات GPT-4 ونماذج Claude، مع تطبيق حدود معدل صارمة على الوكلاء الخارجيين لمنع إساءة الاستخدام.

بدلاً من ذلك، تقدم واجهة برمجة تطبيقات GitHub Models على `https://models.github.ai/inference/chat/completions` خدمة استدلال أكثر تنوعًا، مما يسمح بالوصول إلى كتالوج من النماذج باستخدام بيانات اعتماد GitHub فقط. هذا مثالي لوضع النماذج الأولية والتكامل في سير العمل مثل GitHub Actions. تتطلب المصادقة رمز PAT بنطاق `models:read`، يتم إنشاؤه عبر إعدادات GitHub (https://github.com/settings/tokens). في إعدادات المؤسسة، يمكن توسيع هذا ليشمل الرموز على مستوى المؤسسة أو استخدامه في خطوط أنابيب CI/CD عن طريق إضافة `permissions: models: read` إلى ملفات YAML لسير العمل. تشمل النماذج المتاحة المعايير الصناعية مثل `openai/gpt-4o`، `openai/gpt-4o-mini`، `anthropic/claude-3-5-sonnet-20240620`، وسلسلة Llama 3.1 من Meta، ومتغيرات Mistral، وكلها يمكن استدعاؤها من خلال نفس تنسيق واجهة برمجة التطبيقات المتوافقة مع OpenAI. يجعل هذا التوافق من السهل إدخاله في تكوين الموجه الخاص بك دون تغييرات كبيرة في الكود اللاحق.

للتكوينات الخاصة بالمؤسسة، يعزز GitHub Copilot Enterprise Copilot القياسي باستخدام عناصر تحكم على مستوى المؤسسة، مثل النماذج المضبوطة بدقة بناءً على قاعدة الكود الخاصة بك، لكن الوصول إلى واجهة برمجة التطبيقات يتبع نفس الأنماط. إدارة الشبكة أمر بالغ الأهمية: يمكنك تكوين التوجيه القائم على الاشتراك لضمان استخدام حركة مرور Copilot للمسارات المعتمدة، مما يتطلب من المستخدمين تحديث امتدادات IDE الخاصة بهم (مثل VS Code) إلى الحد الأدنى من الإصدارات التي تدعم هذا. إذا كانت بيئتك تفرض استخدام الوكيل، فقم بتحديث "PROXY_URL" في التكوين للإشارة إلى خادم الوكيل الخاص بمؤسستك، وفكر في الشهادات المخصصة لفحص SSL. يمكن لأدوات مثل LiteLLM أن تعمل كوسيط وكيل لمزيد من التحكم - قم بالتثبيت عبر `pip install litellm[proxy]`، وحدد النماذج في تكوين YAML، وابدأ الخادم على منفذ محلي، وأعد توجيه طلبات Copilot عبره للتسجيل والحد من المعدل ومعالجة الاحتياط. ومع ذلك، في حالتك، نظرًا لأن الهدف هو الحصرية، تجنب الاحتياطيات في الموجه للامتثال لسياسات "مسموح بالاتصال بـ Copilot فقط".

لتنفيذ هذا في التكوين الخاص بك، ابدأ بإلحاق كائن موفر جديد. اختر نقطة النهاية بناءً على حالة الاستخدام الخاصة بك: استخدم نقطة نهاية وكيل Copilot إذا كنت تبني امتدادات، أو GitHub Models لتوجيه LLM العام. اذكر النماذج التي تتداخل مع النماذج الموجودة لديك (مثل متغيرات Claude وGPT) للحفاظ على التوافق. ثم، استبدل جميع حقول "Router" للإشارة فقط إلى هذا الموفر الجديد، مما يزيل الفواصل أو الاحتياطيات مثل ",minimax/minimax-m2". قم بتمكين التسجيل لمراقبة الامتثال، واختبر من خلال محاكاة الطلبات للتحقق من عدم الوصول إلى نقاط نهاية غير مصرح بها. إذا كنت تقوم بالتكامل مع VS Code أو IDEs أخرى، فاضبط الإعدادات مثل `github.copilot.advanced.debug.overrideProxyUrl` للتوجيه عبر الوكيل الذي قمت بتكوينه إذا لزم الأمر.

إليك جدول مقارنة لخيارات واجهة برمجة تطبيقات LLM الرئيسيين في GitHub للمساعدة في تحديد نقطة النهاية التي يجب استخدامها في تكوين الموفر الخاص بك:

| الجانب                  | واجهة برمجة تطبيقات LLM لـ GitHub Copilot (للعملاء)        | واجهة برمجة تطبيقات GitHub Models                        |
|-------------------------|-----------------------------------------------------|-----------------------------------------------------|
| نقطة النهاية           | https://api.githubcopilot.com/chat/completions      | https://models.github.ai/inference/chat/completions |
| الاستخدام الأساسي       | بناء امتدادات ووكلاء Copilot                       | وضع النماذج الأولية العام، والاستدلال، وسير العمل       |
| المصادقة               | Bearer PAT (عبر رأس Authorization)                 | PAT مع نطاق models:read                             |
| النماذج المدعومة       | ضمني (مثل GPT-4، متغيرات Claude)                   | كتالوج صريح: gpt-4o, claude-3-5-sonnet, Llama 3.1، إلخ. |
| ميزات المؤسسة          | حدود معدل للجهات الخارجية؛ يتكامل مع Copilot Enterprise | قابل للاستخدام في GitHub Actions؛ دعم إحضار مفتاحك الخاص |
| حدود المعدل / الحصص    | صارم للوكلاء غير التابعين لـ GitHub                | طبقة مجانية لوضع النماذج الأولية؛ قابل للتطوير للمؤسسة  |
| التوافق                | تنسيق دردشة OpenAI                                 | متوافق مع OpenAI؛ تكامل موجه سهل                     |

يسلط هذا الجدول الضوء على سبب تفضيل GitHub Models لاستخدام الموجه الواسع، حيث إنه يوفر اختيار نموذج أكثر وضوحًا وتكامل سير عمل المؤسسة.

تشمل التحديات المحتملة انتهاء صلاحية الرمز المميز (عادةً ما تدوم PATs لمدة 30-90 يومًا)، لذا قم بأتمتة التجديد في نصوص المؤسسة. إذا كانت بيئتك تستخدم GitHub Enterprise Cloud، فقم بتمكين Copilot على مستوى المؤسسة للوصول السلس. للإعدادات المتقدمة، استكشف إحضار مفاتيح واجهة برمجة التطبيقات الخاصة بك (BYOK) في GitHub Models للتوجيه عبر الموفرين المفضلين مع البقاء داخل نظام GitHub البيئي. دائمًا ما تُعطي الأولوية للوثائق الأساسية لـ GitHub للحصول على أحدث النطاقات ونقاط النهاية، حيث تتطور الميزات بسرعة. إذا فشلت استدعاءات واجهة برمجة التطبيقات المباشرة بسبب قيود الشبكة، ففكر في استخدام خيارات تكوين الوكيل في GitHub أو التكامل مع Azure للنشرات الهجينة للمؤسسة.

باختصار، يحول هذا التكوين الموجه الخاص بك إلى نظام حصري لـ Copilot، متوافقًا مع سياسات المؤسسة مع الحفاظ على الوظائف للمهام المتعلقة بالكود أو مهام LLM العامة.

**الاستشهادات الرئيسية:**
- [Using GitHub Copilot's LLM for your agent](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-extensions/build-a-copilot-agent/use-copilots-llm)
- [Quickstart for GitHub Models](https://docs.github.com/en/github-models/quickstart)
- [GitHub Copilot | liteLLM](https://docs.litellm.ai/docs/tutorials/github_copilot_integration)
- [Managing GitHub Copilot access to your enterprise's network](https://docs.github.com/enterprise-cloud%40latest/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-access/manage-network-access)
- [Configuring network settings for GitHub Copilot](https://docs.github.com/copilot/configuring-github-copilot/configuring-network-settings-for-github-copilot)
- [Prototyping with AI models](https://docs.github.com/github-models/prototyping-with-ai-models)
- [Using your own API keys in GitHub Models](https://docs.github.com/en/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)