---
audio: false
generated: true
image: false
lang: ar
layout: post
title: نقاط قوة DeepSeek V3.1 ومقايضاته
translated: true
type: note
---

سألت عن مدى جودة DeepSeek V3.1 — إليك ما هو معروف公开ًا حتى الآن (اعتبارًا من **21–23 أغسطس 2025**):

---

### ما الجديد في DeepSeek V3.1

* **بنية استدلال هجينة ("فكر و لا تفكر")**: يدعم النموذج وضعين متميزين — وضع "عدم التفكير" السريع للردود السريعة، ووضع "التفكير" الأكثر تباطؤًا للاستدلال الأعمق واستخدام الأدوات. ([رويترز][1]، [وثائق DeepSeek API][2])
* **استدلال أسرع**: يستجيب وضع "التفكير" بشكل أسرع بكثير من الإصدارات السابقة مثل DeepSeek‑R1-0528، مع الحفاظ على جودة إجابة عالية. ([وثائق DeepSeek API][2])
* **تحسين قدرات الوكيل**: تعزز مرحلة ما بعد التدريب استخدام الأدوات، والاستدلال متعدد الخطوات، والسلوك الشبيه بالوكيل. ([وثائق DeepSeek API][2])
* **نافذة سياق موسعة**: لا تزال تحتفظ بطول سياق طويل جدًا يصل إلى **128 ألف رمز**، مما يمكنها من معالجة المستندات الواسعة. ([Hugging Face][3])

---

### لمحات عن الأداء

* **المعايير (مصدرها المجتمع)**: على Reddit، شارك أحد المساهمين درجات معيارية مجمعة تقارن DeepSeek V3.1 (وضع التفكير) مع **gpt‑oss‑120b**:

  * **مؤشر الذكاء**: 60 مقابل 61
  * **مؤشر البرمجة**: 59 مقابل 50
  * ومع ذلك، فإن **DeepSeek V3.1 أبطأ بكثير** — 127.8 ثانية مقابل 11.5 ثانية لتوليد إجابة من 500 رمز، وبمعدل إنتاج رموز أقل بكثير (20 رمز/ثانية مقابل 228 رمز/ثانية). أيضًا، كانت تكلفة DeepSeek أعلى بشكل ملحوظ: **\$0.32 للإدخال / \$1.15 للإخراج** مقابل **\$0.072 / \$0.28** لـ gpt‑oss‑120b. ([Reddit][4])

* **معايير البرمجة**:

  * حقق **71.6%** في معيار البرمجة Aider، **متجاوزًا Claude Opus 4**، بسرعات استدلال/استجابة أسرع. ([36Kr][5])
  * تشير تحليلات أخرى إلى أنه يوفر أداءً قويًا في البرمجة والرياضيات بتكلفة تصل إلى **98% أقل** من المنافسين الرئيسيين. ([Creole Studios][6])

---

### ملخص: نقاط القوة والمفاضلات

* **الإيجابيات**:

  * وضع مزدوج مرن ("فكر" مقابل "لا تفكر") لأحمال العمل المختلفة
  * ممتاز في استخدام الأدوات، والاستدلال متعدد الخطوات، ومهام البرمجة
  * دعم سياق طويل جدًا (128 ألف رمز)

* **السلبيات**:

  * في وضع "التفكير"، زمن استجابة مرتفع (بطيء)
  * أغلى لكل رمز مقارنة ببعض النماذج مثل gpt-oss-120b
  * لا تزال المعايير القياسية في طور الظهور — بعضها يقوده المجتمع؛ المزيد من التقييمات الرسمية سيساعد

---

باختصار، **يمثل DeepSeek V3.1 ترقية قوية** مقارنة بـ V3 و R1، خاصةً لمهام الاستدلال المعقدة والبرمجة والمهام ذات السياق الطويل. لكن **وضعه للاستدلال يضحي بالسرعة وكفاءة التكلفة**، مما يجعله أكثر ملاءمة للتطبيقات عالية القيمة بدلاً من حالات الاستخدام السريعة التي تراعي الميزانية.

هل تريد المساعدة في مقارنته مباشرةً بنماذج مثل GPT-5 أو Claude 4.1؟ أو اقتراحات حول كيفية الاستفادة بشكل أفضل من DeepSeek V3.1 بناءً على احتياجاتك؟

* [رويترز](https://www.reuters.com/world/china/chinese-startup-deepseek-releases-upgraded-ai-model-2025-08-21/?utm_source=chatgpt.com)

[1]: https://www.reuters.com/world/china/chinese-startup-deepseek-releases-upgraded-ai-model-2025-08-21/?utm_source=chatgpt.com "Chinese startup DeepSeek releases upgraded AI model"
[2]: https://api-docs.deepseek.com/news/news250821?utm_source=chatgpt.com "DeepSeek-V3.1 Release"
[3]: https://huggingface.co/deepseek-ai/DeepSeek-V3.1?utm_source=chatgpt.com "deepseek-ai/DeepSeek-V3.1"
[4]: https://www.reddit.com/r/LocalLLaMA/comments/1mwexgd/deepseek_v31_thinking_aggregated_benchmarks_vs/?utm_source=chatgpt.com "DeepSeek V3.1 (Thinking) aggregated benchmarks (vs. ..."
[5]: https://eu.36kr.com/en/p/3430524032372096?utm_source=chatgpt.com "DeepSeek V3.1 Base Suddenly Launched"
[6]: https://www.creolestudios.com/deepseek-v3-1-vs-gpt-5-vs-claude-4-1-compared/?utm_source=chatgpt.com "DeepSeek V3.1 vs GPT-5 vs Claude 4.1 Compared"