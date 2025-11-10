---
audio: false
generated: true
image: false
lang: ar
layout: post
title: ترقية كود كلود بسرعة الآن
translated: true
type: note
---

إذا كنت تبحث عن **ترقية Claude Code**، وكيل البرمجة عبر سطر الأوامر من Anthropic، فإليك كيفية القيام بذلك — والحصول على أحدث الإمكانيات مثل أوضاع التعلم والعوامل الفرعية المخصصة لتعمل بسلاسة.

---

### كيفية ترقية Claude Code

1.  **تحقق من إصدارك الحالي**
    قم بتشغيل:

    ```
    claude --version
    ```

    هذا يتيح لك رؤية الإصدار الذي تستخدمه حاليًا.

2.  **التحديث عبر npm**
    أبسط طريقة للترقية هي:

    ```
    npm install -g @anthropic-ai/claude-code@latest
    ```

    هذا يقوم بتحميل أحدث إصدار من npm.
    يذكر مستخدمو Reddit أن هذا الإصلاح أصلح الأخطاء وحسن من سرعة الاستجابة. كتب أحدهم:

    > "بعد التحديث إلى أحدث إصدار (1.0.18)، يبدو الفرق شاسعًا — يشعر بأنه أكثر ذكاءً واستجابة."
    > ([Reddit][1], [Anthropic][2])

3.  **بديلاً، استخدم برنامج التثبيت الأصلي (Beta)**
    إذا كنت تفضل ملفًا ثنائيًا قائمًا بذاته (بدلاً من npm)، جرب:

    ```
    curl -fsSL https://claude.ai/install.sh | bash -s latest
    ```

    (على Windows، استخدم إصدار PowerShell)
    ([Anthropic][3])

4.  **تحقق من التحديث**
    بعد التثبيت، أعد تشغيل طرفيتك وقم بتشغيل `claude --version` مرة أخرى لتأكيد أن الإصدار الجديد نشط.

5.  **استكشاف أخطاء التثبيت وإصلاحها**
    إذا واجهت مشاكل، حاول إلغاء التثبيت أولاً:

    ```
    npm uninstall -g @anthropic-ai/claude-code
    npm install -g @anthropic-ai/claude-code
    ```

    وجد بعض المستخدمين أن هذه السلسلة حلت مشاكل التحديث. ([Anthropic][4], [Reddit][1], [Anthropic][5], [The Verge][6])

---

### ما الجديد في التحديثات الأخيرة؟

#### أوضاع التعلم

أضافت Anthropic مؤخرًا أسلوبين جديدين للتعلم داخل Claude Code: **"Explanatory"** و **"Learning"**. يساعدانك على فهم المنطق وراء الكود المُنشأ بدلاً من مجرد منحك الحلول. لتمكينها:

1.  تأكد من أنك قمت بتحديث Claude Code.
2.  قم بتشغيل `/output-styles` في جلسة Claude Code الخاصة بك.
3.  اختر بين أسلوب **Default**، أو **Explanatory**، أو **Learning**.
    أُطلقت هذه الميزة في **14 أغسطس 2025**. ([Tom's Guide][7])

#### العوامل الفرعية المخصصة

يدعم Claude Code الآن **subagents** — مساعدات ذكية متخصصة مصممة لمهام محددة (مثل إصلاح الأخطاء، إعادة الهيكلة، التوثيق). يمكنك تعيين أوامر نظام مختلفة، أذونات أدوات، ونوافذ سياق لكل منها.
لإعداد واحد:

1.  قم بتشغيل `/agents`
2.  اختر "Create New Agent" (إما على مستوى المستخدم أو مستوى المشروع)
3.  حدد سلوكه، الأدوات المسموح بها، واحفظه
    تساعدك العوامل الفرعية على الحفاظ على سير عملك أكثر تنظيماً، تركيزاً، ووعياً بالسياق. ([Anthropic][8])

---

### ملخص سريع (بدون جداول، مجرد خطوات واضحة)

*   **لترقية**:

    ```
    npm install -g @anthropic-ai/claude-code@latest
    ```

    أو استخدم التثبيت الأصلي مع `curl | bash -s latest`.

*   **تمكين أوضاع التعلم**:

    *   قم بالتحديث.
    *   داخل Claude Code: شغل `/output-styles` واختر وضعك.

*   **إنشاء عوامل فرعية**:

    *   داخل Claude Code: شغل `/agents`.
    *   خصص وصول الأدوات، أوامر النظام، والسلوك.

---

### الأفكار الختامية

ترقية Claude Code أمر مباشر — استخدم npm أو المثبت الأصلي، تحقق من أنك على أحدث إصدار، ثم استكشف ميزات **أوضاع التعلم** و **subagent** الجديدة. تنقل هذه الإضافات Claude Code من كونه مجرد مساعد برمجة إلى شيء أشبه بشريك تدريبي ومتعاون فاعل في سير عمل التطوير الخاص بك.

إذا كنت ترغب في المساعدة في صياغة أول عامل فرعي لك أو استخدام وضع التعلم بفعالية، سأكون سعيدًا بأن أرشدك خلال ذلك!

[1]: https://www.reddit.com/r/ClaudeAI/comments/1l8gbfo/dont_forget_to_update_your_claude_cli_it_makes_a/?utm_source=chatgpt.com "Don't forget to update your Claude CLI! It makes a huge ..."
[2]: https://www.anthropic.com/solutions/agents?utm_source=chatgpt.com "Claude Agents | Intelligent AI Solutions \ Anthropic"
[3]: https://docs.anthropic.com/en/docs/claude-code/quickstart?utm_source=chatgpt.com "Quickstart - Claude Code"
[4]: https://docs.anthropic.com/en/docs/claude-code/settings?utm_source=chatgpt.com "Claude Code settings"
[5]: https://docs.anthropic.com/en/docs/claude-code/overview?utm_source=chatgpt.com "Claude Code overview"
[6]: https://www.theverge.com/2024/11/25/24305774/anthropic-model-context-protocol-data-sources?utm_source=chatgpt.com "Anthropic launches tool to connect AI systems directly to datasets"
[7]: https://www.tomsguide.com/ai/claudes-new-learning-modes-take-on-chatgpts-study-mode-heres-what-they-do?utm_source=chatgpt.com "Claude's new 'learning modes' take on ChatGPT's Study Mode - here's what they do"
[8]: https://docs.anthropic.com/en/docs/claude-code/sub-agents?utm_source=chatgpt.com "Subagents"