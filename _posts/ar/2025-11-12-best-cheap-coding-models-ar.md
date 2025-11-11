---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: أفضل نماذج البرمجة الاقتصادية عبر أوبن روتر
translated: true
type: note
---

### أفضل النماذج الاقتصادية للبرمجة باستخدام Codex CLI عبر OpenRouter

استنادًا إلى المعايير الحديثة ومناقشات المستخدمين وتصنيفات النماذج اعتبارًا من عام 2025، إليك بعض أفضل البدائل الاقتصادية لـ GPT-5-Codex لمهام البرمجة في Codex CLI. يعتبر GPT-5-Codex باهظ الثمن بالفعل (غالبًا في نطاق 20-50 دولارًا للإدخال / 60-150 دولارًا للإخراج لكل مليون رمز، اعتمادًا على المزود)، لذا تركز هذه القائمة على الخيارات الاقتصادية ذات الأداء القوي في البرمجة. يعني نموذج الدفع مقابل الاستخدام في OpenRouter أنك تدفع فقط مقابل الرموز المُعالجة، والعديد من النماذج لديها مستويات مجانية أو أسعار منخفضة جدًا (أقل من 1 دولار لكل مليون رمز مجتمعين للإدخال/الإخراج).

لقد أوليت الأولوية للنماذذج التي حصلت على درجات عالية في معايير البرمجة مثل SWE-Bench أو HumanEval أو Aider، مع كونها رخيصة أو مجانية. تم تنسيق معرفات النماذج لسهولة الاستخدام في ملف `config.toml` الخاص بك (مثال: `model = "provider/model-name"`). للاطلاع على الأسعار الحالية الدقيقة، تحقق من صفحة النماذج في OpenRouter، حيث يمكن أن تتقلب الأسعار قليلاً.

#### أفضل التوصيات:
- **Grok Code Fast (xAI)**
  معرف النموذج: `xai/grok-code-fast`
  السبب: يتصدر تصنيفات OpenRouter للبرمجة، ويتفوق في السرعة والمهام الوكيلة (مثل المركز الأول في الأولمبياد الدولي للمعلوماتية). غالبًا مجاني للاستخدام الأساسي، مما يجعله النموذج الأكثر استخدامًا على المنصة. رائع لسير عمل البرمجة التكراري.
  السعر: مجاني أو ~$0.50/$2.00 لكل 1M رمز (إدخال/إخراج). السياق: 128K رمز.

- **Kat Coder Pro (KwaiPilot)**
  معرف النموذج: `kwaipilot/kat-coder-pro:free`
  السبب: نموذج برمجة متخصص بنسبة 73.4% على SWE-Bench Verified، قريب من أفضل النماذج الاحتكارية. مجاني لفترة محدودة، مثالي للاستدلال المعقد وتوليد الكود.
  السعر: مجاني (ترويجي). السياق: 256K رمز، إخراج حتى 32K.

- **DeepSeek Coder V3 (DeepSeek)**
  معرف النموذج: `deepseek/deepseek-coder-v3`
  السبب: قيمة ممتازة بنسبة ~71% في نتائج برمجة Aider، قوي في التنفيذ والتdebug. يُوصى به frequently للمبرمجين محدودي الميزانية في المنتديات.
  السعر: رخيص جدًا (~$0.14/$0.28 لكل 1M). السياق: 128K رمز.

- **Llama 4 Maverick (Meta)**
  معرف النموذج: `meta/llama-4-maverick`
  السبب: الأفضل في المستوى المجاني لجودة البرمجة والتكامل مع VS Code (مثلًا مع أدوات مثل RooCode). يؤدي أداءً جيدًا في مهام الكود الواقعية.
  السعر: متاح مستوى مجاني، أو منخفض التكلفة (~$0.20/$0.80 لكل 1M). السياق: 128K رمز.

- **Mistral Devstral Small (Mistral)**
  معرف النموذج: `mistral/devstral-small`
  السبب: مُحسّن للسعر، وإنتاجية سريعة، وجيد في تنفيذ الكود. غالبًا ما يُقرن بنماذج أكبر لسير العمل الهجين.
  السعر: رخيص (~$0.25/$1.00 لكل 1M). السياق: 128K رمز.

- **Qwen3 235B (Qwen)**
  معرف النموذج: `qwen/qwen3-235b`
  السبب: أداء عالٍ في معايير البرمجة، موصى به للإعدادات المُحسّنة للتكلفة. يتعامل مع مشاريع الكود كبيرة النطاق بشكل جيد.
  السعر: معقول (~$0.50/$2.00 لكل 1M). السياق: 128K رمز.

- **Gemini 2.5 Flash (Google)**
  معرف النموذج: `google/gemini-2.5-flash`
  السبب: المركز الثالث في التصنيفات، سريع ومنخفض التكلفة للبرمجة التكرارية. جيد للمهام متعددة الوسائط إذا كان الكود الخاص بك يتضمن تصور البيانات.
  السعر: رخيص (~$0.35/$1.05 لكل 1M). السياق: 1M رمز.

هذه النماذج متوافقة مع OpenAI، لذا ستعمل بسلاسة في Codex CLI بعد تعيين المزود كـ "openrouter" ومفتاح API الخاص بك. ابدأ بالنماذج المجانية مثل Grok Code Fast أو Kat Coder للاختبار. للاستخدام المحدد للبرمجة، انظر إلى نتائج SWE-Bench — الدرجة الأعلى تعني أداءً أفضل في حل مشاكل GitHub الحقيقية. إذا كنت بحاجة إلى سياق أكبر أو سرعة، يمكنك الجمع مع التوجيه في OpenRouter للانتقال التلقائي إلى النماذج الأرخص.

للتكامل: في ملف `config.toml` الخاص بك، أضف ملف تعريف مثل `[profiles cheap-coder]` مع `model_provider = "openrouter"` و `model = "one-of-the-IDs-above"`.

[Top AI Models on OpenRouter 2025: Performance vs Cost Guide](https://www.teamday.ai/blog/top-ai-models-openrouter-2025)
[Best Budget Coding LLMs 2025: DeepSeek R1 vs Gemini vs GPT](https://llmx.de/blog/budget-coding-llms-2025/)
[What are the best LLMs available on OpenRouter to use for coding](https://medium.com/@okreitz/what-are-the-best-llms-available-on-openrouter-to-use-for-coding-with-kilo-ca04e75a84ee)
[Best Free AI Models You Can Use on OpenRouter](https://apidog.com/blog/free-ai-models/)
[Top AI Coding Models in 2025](https://www.veerotech.net/blog/top-ai-coding-models-in-2025-boost-your-development-workflow-with-these-game-changers/)
[LLM Rankings - OpenRouter](https://openrouter.ai/rankings)
[Top 5 AI Coding Models of March 2025](https://dev.to/apipie-ai/top-5-ai-coding-models-of-march-2025-5f04)
[Models - OpenRouter](https://openrouter.ai/models)
[whats the best coding model on openrouter? - Reddit](https://www.reddit.com/r/RooCode/comments/1kdu7we/whats_the_best_coding_model_on_openrouter/)