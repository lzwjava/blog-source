---
audio: false
generated: true
image: false
lang: ar
layout: post
title: جسر كوبيلوت جيت هاب API
translated: true
type: note
---

لقد وصلت إلى **ericc-ch/copilot-api**، وهو مشروع على GitHub يحول **GitHub Copilot** إلى خادم API محلي متوافق مع واجهات برمجة تطبيقات **OpenAI** و **Anthropic** (مثل Claude).

إليك شرحًا أوضح — بدون جداول، فقط كلام مباشر:

---

### ما هذا؟

* إنه **وكيل عكسي الهندسة** يتيح لك التفاعل مع GitHub Copilot باستخدام نقاط نهاية مألوفة على غرار OpenAI مثل `/v1/chat/completions`، `/v1/models`، و `/v1/embeddings`. يمكنك أيضًا استخدام نقاط نهاية متوافقة مع Anthropic مثل `/v1/messages` ([GitHub][1]).

* في الأساس، هذا يسمح للأدوات التي تدعم واجهات برمجة تطبيقات OpenAI أو Anthropic — مثل Claude Code — باستخدام GitHub Copilot كخلفية لها ([GitHub][1]).

---

### الميزات الرئيسية

* **التوافق مع OpenAI و Anthropic**: يعمل مثل واجهة برمجة تطبيقات OpenAI أو Anthropic الحقيقية ([GitHub][1]).
* **التكامل مع Claude Code**: جاهز للتوصيل مع Claude Code باستخدام علم `--claude-code` ([GitHub][1]).
* **لوحة مراقبة الاستخدام**: راقب استخدامك لواجهة برمجة تطبيقات Copilot والحصص المسموحة عبر واجهة ويب مدمجة ([GitHub][1]).
* **التحكم في معدل الطلبات والموافقات**: يتضمن خيارات لتحديد معدل الطلبات (`--rate-limit`)، الانتظار التلقائي (`--wait`)، الموافقة اليدوية (`--manual`)، والتdebugging (عرض الرموز) — رائع لتجنب أنظمة إساءة الاستخدام من GitHub ([GitHub][1]).
* **يدعم خطط Copilot المختلفة**: تعمل جميع الحسابات الفردية والتجارية والمؤسسية ([GitHub][1]).

---

### الإعداد والاستخدام

* **المتطلبات الأساسية**: ستحتاج إلى Bun (الإصدار ١.٢.x أو أحدث) واشتراك في GitHub Copilot ([GitHub][1]).
* **خيارات التثبيت**:

  * **Docker**:

    ```bash
    docker build -t copilot-api .
    docker run -p 4141:4141 -v $(pwd)/copilot-data:/root/.local/share/copilot-api copilot-api
    ```

    أو يمكنك تمرير رمز GitHub الخاص بك مباشرة عبر `GH_TOKEN` ([GitHub][1]).
  * **npx**:

    ```bash
    npx copilot-api@latest start --port 8080
    ```

    أو `npx copilot-api@latest auth` للمصادقة فقط ([GitHub][1]).
* **هيكل الأمر**:

  * `start`: يُطلق خادم واجهة برمجة التطبيقات (يتعامل مع المصادقة إذا لزم الأمر).
  * `auth`: يُطلق عملية تسجيل الدخول إلى GitHub دون تشغيل الخادم.
  * `check-usage`: يُخرج استخدام Copilot الحالي في طرفيتك.
  * `debug`: يعرض معلومات تشخيصية (الإصدارات، حالة المصادقة، إلخ)، مع خيار output `--json` اختياري ([GitHub][1]).

---

### ملاحظات من الواقع

علّق مستخدمو Reddit:

> "هذا المشروع يتيح لك تحويل copilot إلى نهاية نقطية متوافقة مع openai." ([Reddit][2])
> "إنه مشروع رائع لصنع ..." ([Reddit][3])

---

### محاذير مهمة

* **غير رسمي وبدون دعم**: هذا **ليس** منتجًا رسميًا من GitHub وقد يتعطل في أي وقت ([GitHub][1]).
* **خطر اكتشاف إساءة الاستخدام**: الاستخدام المكثف أو الآلي قد يُطلق حماية إساءة الاستخدام من GitHub وقد يؤدي إلى تعليق وصولك إلى Copilot ([GitHub][1]).
* **مشاكل محتملة في معدل الطلبات**: أبلغ بعض المستخدمين عن أخطاء مثل `421 Misdirected Request`، وقد أوقف الحافظ على المشروع التطوير أثناء التحقيق ([GitHub][4]).

---

### الملخص (لا حاجة لجداول)

* **ما يفعله**: يعرض GitHub Copilot كما لو كان واجهة برمجة تطبيقات OpenAI/Anthropic.
* **سبب أهمية ذلك**: يجعل Copilot قابلاً للاستخدام في الأدوات التي تتوقع تلك الواجهات — مثل Claude Code.
* **كيفية استخدامه**: ثبّت عبر Docker أو npx؛ شغّل الأوامر للبدء أو المصادقة أو مراقبة الاستخدام.
* **تابع بحذر**: إنه مفيد، لكنه غير رسمي، وقد تعترض حدود معدل الطلبات أو الضوابط الأمنية لـ GitHub الاستخدام المكثف.

---

أعلمني إذا كنت تريد المساعدة في إعداده، أو كنت فضوليًا بشأن دمجه في مشروع أو أداة معينة!

[1]: https://github.com/ericc-ch/copilot-api?utm_source=chatgpt.com "ericc-ch/copilot-api"
[2]: https://www.reddit.com/r/ChatGPTCoding/comments/1m6cqac/how_to_use_your_github_copilot_subscription_with/?utm_source=chatgpt.com "How to use your GitHub Copilot subscription with Claude ..."
[3]: https://www.reddit.com/r/ClaudeAI/comments/1lc21gk/using_github_copilot_as_a_provider_for_claude_code/?utm_source=chatgpt.com "Using GitHub Copilot as a provider for Claude Code"
[4]: https://github.com/ericc-ch/copilot-api/issues/7?utm_source=chatgpt.com "Issue #7 · ericc-ch/copilot-api - 421 Misdirected Request"