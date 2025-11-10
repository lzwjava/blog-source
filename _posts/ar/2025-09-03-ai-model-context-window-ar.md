---
audio: false
generated: true
image: false
lang: ar
layout: post
title: سعات نافذة سياق النماذج الذكية الاصطناعية
translated: true
type: note
---

فيما يلي **السعات القصوى الحالية للرموز المميزة (أحجام النوافذ السياقية)** للنماذج التي أدرجتها، بناءً على الوثائق والإعلانات الحديثة:

---

### نماذج Anthropic

*   **Claude Opus 4 / Opus 4.1**
    يقدم نافذة سياقية تبلغ **200,000 رمز مميز**، مما يجعله مثالياً للاستدلال المستمر ومهام سير العمل المعقدة ([Anthropic][1]، [Amazon Web Services, Inc.][2]).

*   **Claude Sonnet 4**
    يدعم أيضاً **200,000 رمز مميز** من السياق بشكل أصلي ([Prompthub][3]).
    بالإضافة إلى ذلك، يتيح **ترقية تجريبية** الآن **مليون رمز مميز** ضخم من السياق لمستخدمي المؤسسات/واجهة برمجة التطبيقات (API) ([Anthropic][4]).

---

### نماذج Mistral AI

*   **Mistral Medium 3.1**
    يمتلك نافذة سياقية تبلغ **128,000 رمز مميز** ([OpenRouter][5]).

*   **Mistral Large 2**
    يدعم أيضاً طول سياق يبلغ **128,000 رمز مميز** ([Wikipedia][6]).

*   **Mistral Medium (الإصدارات السابقة)**
    سابقاً، كانت السعة القياسية هي **32,000 رمز مميز** للسياق ([Clarifai][7]، [Mistral AI][8]).

*   **Mistral Small 3.1**
    قام بترقية نافذة السياق الخاصة به **من 32 ألف إلى 128 ألف رمز مميز** في هذا الإصدار الأحدث ([Wikipedia][6]).

---

### ملاحظات إضافية

*   يؤكد ملخص على Wikipedia أن **Claude 3 Opus** كان يمتلك نافذة سياقية **بقدرة 200 ألف رمز مميز**، مع توسعات تصل إلى **مليون رمز مميز** في حالات معينة ([Wikipedia][9]).

*   **آلية الانتباه ذات النافذة المنزلقة من Mistral** تدعم نظرياً ما يصل إلى **131,072 رمز مميز = 32 × 4096**، وهو ما يتماشى بشكل وثيق مع الأرقام المبلغ عنها البالغة 128 ألف رمز ([Hugging Face][10]).

---

### ملخص (بتنسيق موجز)

*   **Claude Opus 4 / 4.1**: 200,000 رمز مميز
*   **Claude Sonnet 4**: 200,000 رمز مميز (قياسي)، حتى **مليون رمز مميز** (نسخة تجريبية/ للمؤسسات)
*   **Mistral Medium 3.1**: 128,000 رمز مميز
*   **Mistral Large 2**: 128,000 رمز مميز
*   **Mistral Small 3.1**: 128,000 رمز مميز (تمت ترقيته من 32 ألف)

---

أعلمني إذا كنت تريد المزيد من التفاصيل حول النماذج الأخرى أو الإمكانيات الخاصة بالهيكل المعماري!

* [The Verge](https://www.theverge.com/ai-artificial-intelligence/757998/anthropic-just-made-its-latest-move-in-the-ai-coding-wars?utm_source=chatgpt.com)
* [Tom's Guide](https://www.tomsguide.com/ai/anthropic-looks-to-beat-gpt-5-and-grok-4-with-this-one-major-upgrade?utm_source=chatgpt.com)

[1]: https://www.anthropic.com/claude/opus?utm_source=chatgpt.com "Claude Opus 4.1"
[2]: https://aws.amazon.com/bedrock/anthropic/?utm_source=chatgpt.com "Anthropic's Claude in Amazon Bedrock"
[3]: https://www.prompthub.us/blog/the-complete-guide-to-claude-opus-4-and-claude-sonnet-4?utm_source=chatgpt.com "The Complete Guide to Claude Opus 4 and Claude Sonnet 4"
[4]: https://www.anthropic.com/news/1m-context?utm_source=chatgpt.com "Claude Sonnet 4 now supports 1M tokens of context"
[5]: https://openrouter.ai/mistralai/mistral-medium-3.1?utm_source=chatgpt.com "Mistral Medium 3.1 - API, Providers, Stats"
[6]: https://en.wikipedia.org/wiki/Mistral_AI?utm_source=chatgpt.com "Mistral AI"
[7]: https://clarifai.com/mistralai/completion/models/mistral-medium?utm_source=chatgpt.com "mistral-medium model | Clarifai - The World's AI"
[8]: https://mistral.ai/news/mistral-large?utm_source=chatgpt.com "Au Large"
[9]: https://en.wikipedia.org/wiki/Claude_%28language_model%29?utm_source=chatgpt.com "Claude (language model)"
[10]: https://huggingface.co/docs/transformers/en/model_doc/mistral?utm_source=chatgpt.com "Mistral"