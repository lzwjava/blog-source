---
audio: false
generated: true
image: false
lang: ar
layout: post
title: 'ميون: محسن المصفوفات الواعي للهيكل'
translated: true
type: note
---

يشير "Muon" في كيمي إلى محسن متقدم—بتحديد **محسن مدرك للبنية وموجه للمصفوفات** مستخدم في تدريب نموذج اللغة كيمي K2.

---

### ما هو محسن Muon؟

1.  **تحسين مدرك لبنية المصفوفة**
    على عكس AdamW أو SGD، تعامل Muon مصفوفات الأوزان ككيانات هندسية بدلاً من معاملات عددية مستقلة. فهو يطبق **تكرارات نيوتن-شولتز** لتعامد التدرج متوسط الزخم، مما ينتج تحديثات متوازنة وحسنة التكييف تحترم بنية الصفوف والأعمدة في المصفوفة ([Medium][1], [kellerjordan.github.io][2]).

2.  **التعامد عبر طريقة نيوتن-شولتز**
    بدلاً من إجراء تحليل القيمة المفردة (SVD) المكلف، يستخدم Muon طريقة تكرارية سريعة (نيوتن-شولتز) لتقريب أقرب مصفوفة متعامدة للتدرج. هذا يبقي التحديث تحت **قيود القيمة الطيفية**، محافظًا على الطاقة وناشرًا التعلم عبر جميع الاتجاهات بالتساوي ([Medium][1], [kellerjordan.github.io][2]).

3.  **تعديل خط المعالجة**
    تم استبدال تدفق التحديث القياسي—**التدرج → الزخم → تحديث المعامل** بـ:
    **التدرج → الزخم → تعامد نيوتن-شولتز → تحديث المعامل**.
    هذا التعديل يعزز كفاءة واستقرار التدريب لمصفوفات المعاملات ثنائية الأبعاد ([Medium][3], [kellerjordan.github.io][2]).

4.  **فعال عملياً**
    على الرغم من إضافة حمل حسابي بسيط، يوفر Muon تسريعًا كبيرًا:

    *   أرقام قياسية في NanoGPT speedrunning، محسنًا وقت التدريب بنسبة ~35% ([kellerjordan.github.io][2]).
    *   يتوسع جيدًا في تدريب نماذج اللغة الكبيرة عند دمجه مع تناقص الوزن (weight decay) وتعديلات RMS لكل معلمة ([arXiv][4]).

5.  **أسس نظرية قوية**
    تؤكد الأبحاث الحديثة خصائص تقارب Muon، وفوائد تناقص الوزن، والحجم الأمثل للدفعة. تؤكد الدراسات حدودًا نظرية أكثر إحكامًا والكفاءة عبر السيناريوهات العملية ([arXiv][5]).

---

### دور Muon في **كيمي K2**

كيمي K2 هو **نموذج خليط الخبراء (MoE)** من Moonshot AI، بإجمالي **تريليون معلمة** (32 مليار مُفعلة) مُحسّن لقدرات الوكالة. حقق أداءً استثنائيًا في معايير المعرفة والاستدلال والبرمجة، ويرجع ذلك جزئيًا إلى التدريب باستخدام Muon (ونسخة varient تسمى **MuonClip**) ([Hugging Face][6], [Poe][7]).

*   يشير **محسن MuonClip** إلى تطبيق Muon على نطاق هائل مع معالجة تحديات الاستقرار المتأصلة في مثل هذه النماذج الضخمة ([Hugging Face][6], [Poe][7]).
*   كان المحسن مفتاحًا لتمكين **عدم استقرار تدريبي صفري** على مجموعة بيانات رموز كبيرة (~15.5 تريليون رمز) وتقديم نتائج على أحدث المستويات ([Hugging Face][6]).

---

### باختصار (بدون جدول، كما هو مطلوب)

*   **Muon** = "الزخم المعامد بطريقة نيوتن-شولتز"—محسن يستبدل تحديثات التدرج الخام بتحديثات معامدة، محسنًا ديناميكيات التعلم لمعاملات المصفوفة.
*   يحافظ على البنية، يضمن تحديثات متوازنة، ويبقى فعالاً من خلال التعامد التكراري بدلاً من عمليات التحليل المكلفة.
*   **كيمي K2** يستفيد من Muon (و MuonClip) لدفع حدود التدريب واسع النطاق لنماذج MoE، محققًا أفضل أداء مع الاستقرار وكفاءة الحوسبة.

---

أعلمني إذا كنت ترغب في الغوص أعمق—ربما كيف يقارن Muon بـ AdamW في مسارات التدريب، أو كيف يعدل MuonClip الخوارزمية لنماذج MoE، أو كيف تعمل طريقة نيوتن-شولتز في الكود!

[1]: https://medium.com/%40gauritr01/the-truth-about-kimi-k2-pretraining-muon-optimizer-moe-unpacked-43554527d94a?utm_source=chatgpt.com "The Truth About KIMI K2 Pretraining: Muon Optimizer ..."
[2]: https://kellerjordan.github.io/posts/muon/?utm_source=chatgpt.com "Muon: An optimizer for hidden layers in neural networks"
[3]: https://medium.com/%40jenwei0312/going-beyond-adamw-a-practical-guide-to-the-muon-optimizer-93d90e91dbd3?utm_source=chatgpt.com "Going Beyond AdamW: A Practical Guide to the Muon ..."
[4]: https://arxiv.org/html/2502.16982v1?utm_source=chatgpt.com "Muon is Scalable for LLM Training"
[5]: https://arxiv.org/abs/2507.01598?utm_source=chatgpt.com "Convergence Bound and Critical Batch Size of Muon Optimizer"
[6]: https://huggingface.co/moonshotai/Kimi-K2-Base?utm_source=chatgpt.com "moonshotai/Kimi-K2-Base"
[7]: https://poe.com/Kimi-K2?utm_source=chatgpt.com "Kimi-K2"