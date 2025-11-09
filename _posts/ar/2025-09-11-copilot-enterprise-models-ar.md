---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: نظرة عامة على خيارات نموذج المؤسسة في Copilot
translated: true
type: note
---

تسأل عن النموذج الذي يمكن استخدامه لـ **Copilot Enterprise**، وتحديدًا ما إذا كان GPT-4.1 أم GPT-4o أم شيء آخر. إليك ما هو حالي وذو صلة اعتبارًا من **سبتمبر 2025**:

---

### ما النماذج المتاحة لـ Copilot Enterprise؟

#### GitHub Copilot Enterprise و Copilot Chat

* **بشكل افتراضي**، يعمل GitHub Copilot Enterprise (و Copilot Chat) **على نموذج GPT-4o**، مما يقدم استجابات أسرع وجودة محسنة. ([Reddit][1])
* مؤخرًا، أصبح **GPT-4.1** متاحًا — ولكن يجب على المسؤولين **تمكينه صراحةً عبر السياسة** في إعدادات Copilot. بمجرد التمكين، يمكن للمستخدمين اختيار GPT-4.1 من منتقي النماذج في كل من VS Code وعلى موقع github.com. ([The GitHub Blog][2])

#### Visual Studio Copilot

* اعتبارًا من **يونيو 2025**، أصبح **GPT-4.1 هو النموذج الافتراضي** لـ Copilot في Visual Studio، بدلاً من GPT-4o. أظهرت اختبارات Microsoft أن GPT-4.1 يقدم **استجابات أسرع، واقتراحات ذات جودة أعلى، وكفاءة أكبر**. ([Visual Studio Magazine][3], [Microsoft Learn][4])

#### Microsoft 365 Copilot (أدوات إنتاجية Office)

* بدأت Microsoft في دمج **GPT-5** في نظام Copilot البيئي الأوسع — بما في ذلك Microsoft 365 Copilot و GitHub Copilot و Copilot Studio والمزيد — عبر "**الوضع الذكي**" الجديد الذي يُوجِه المهام تلقائيًا إلى النموذج الأنسب بناءً على الحاجة، مما يحسن التفكير والاحتفاظ بالسياق وجودة التفاعل. ([The Verge][5])
* بالإضافة إلى ذلك، أعلنت Microsoft عن دمج **Claude Sonnet 4** من Anthropic للمهام المتقدمة مثل تصميم العروض التقديمية وأتمتة جداول البيانات، مع الاستمرار في استخدام **GPT-5** (إلى جانب المسارات المتبقية القائمة على GPT) للوظائف الأخرى. ([New York Post][6])

---

### ملخص — أي نموذج مناسب لـ **Copilot Enterprise**؟

* **GitHub Copilot Enterprise / Copilot Chat**:

  * الافتراضي: **GPT-4o**
  * اختياري: **GPT-4.1** (إذا تم تمكينه من قبل المسؤول)
* **Visual Studio Copilot**: الافتراضي الآن هو **GPT-4.1**
* **Microsoft 365 Copilot**: يستفيد من **وضع GPT-5 الذكي**، مع توجيه وقدرات عالية الأداء — ويدمج أيضًا **Claude Sonnet 4** للمهام الانتقائية في المؤسسات.

---

### عرض سريع (بدون جداول عريضة، حسب تفضيلك):

* **GPT-4o**: الافتراضي في GitHub Copilot Enterprise؛ معروف بالسرعة والجودة في الدردشة على مستوى المؤسسات.
* **GPT-4.1**: الخليف الأكثر قوة — أفضل في التعامل مع الكود، واتباع التعليمات، والسياقات الطويلة. متاح في GitHub Copilot إذا تم تمكينه، وهو الآن الافتراضي في Visual Studio Copilot. ([OpenAI][7])
* **GPT-5**: أحدث نموذج، مُدمج في M365 Copilot عبر الوضع الذكي عبر جميع منصات Copilot لاختيار نموذج أكثر ذكاءً. ([The Verge][5])
* **Claude Sonnet 4**: أُضيف mainly لمهام Office مثل أتمتة PowerPoint و Excel، إلى جانب GPT-5. ([New York Post][6])

---

### ما الخطوة التالية؟

* إذا كنت **مسؤولاً** تدير GitHub Copilot Enterprise، فتحقق من إعداداتك **لتمكين GPT-4.1** إذا كنت تريد أن يستفيد المستخدمون من تحسينات أدائه.
* إذا كنت تستخدم **Visual Studio Copilot**، فأنت بالفعل على **GPT-4.1** بشكل افتراضي.
* بالنسبة إلى **Microsoft 365 Copilot**، ستستفيد من طرح **وضع GPT-5 الذكي** ودمج **Claude Sonnet 4**. لا требуется أي إجراء — فهو جزء من طبقات الخدمة بالفعل.

دعني أعلم إذا كنت تريد المساعدة في تكوين هذه الإعدادات أو التنقل بين خيارات النماذج في بيئة مؤسستك المحددة!

[1]: https://www.reddit.com/r/GithubCopilot/comments/1dx2iq1/github_copilot_enterprise_on_gpt4o/?utm_source=chatgpt.com "GitHub Copilot Enterprise on GPT-4o : r/GithubCopilot"
[2]: https://github.blog/changelog/2025-04-14-openai-gpt-4-1-now-available-in-public-preview-for-github-copilot-and-github-models/?utm_source=chatgpt.com "OpenAI GPT-4.1 now available in public preview for GitHub ..."
[3]: https://visualstudiomagazine.com/articles/2025/06/26/new-default-model-for-visual-studio-copilot-so-how-do-you-choose.aspx?utm_source=chatgpt.com "New Default Model for Visual Studio Copilot, So How Do ..."
[4]: https://learn.microsoft.com/en-us/visualstudio/ide/copilot-select-add-models?view=vs-2022&utm_source=chatgpt.com "Using AI models in Copilot Chat - Visual Studio (Windows)"
[5]: https://www.theverge.com/news/753984/microsoft-copilot-gpt-5-model-update?utm_source=chatgpt.com "Microsoft brings GPT-5 to Copilot with new smart mode"
[6]: https://nypost.com/2025/09/10/business/microsoft-to-add-anthropic-ai-models-as-rift-with-openai-grows-report/?utm_source=chatgpt.com "Microsoft to add Anthropic AI models - as rift with OpenAI grows: report"
[7]: https://openai.com/index/gpt-4-1/?utm_source=chatgpt.com "Introducing GPT-4.1 in the API"