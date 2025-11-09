---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: بدائل الكوبايلوت المحلية المُستضافة ذاتياً
translated: true
type: note
---

تطلب أدوات مفتوحة المصدر لاستضافة تجربة "شبيهة بـ Copilot" محليًا — أدوات يمكنك تشغيلها بنفسك (باستخدام الرمز المميز أو النموذج الخاص بك)، ربما تكون مدمجة في VS Code أو بيئات التطوير المتكاملة الأخرى. لا توجد جداول، فقط تفسيرات واضحة. إليك الخيارات الأكثر شهرة:

---

### **Tabby**

مساعد ترميز ذكي يعمل بالذكاء الاصطناعي ويتم استضافته محليًا، مكتوب بلغة Rust. إنه مفتوح المصدر، ولا يتطلب خدمات خارجية، ويوفر واجهة على غرار OpenAPI — مما يجعل التكامل مع بيئات التطوير المتكاملة المحلية والبنية التحتية مباشرًا. كما أنه يدعم وحدات معالجة الرسومات من الفئة الاستهلاكية وتكاملات المحرر بما في ذلك Vim/Neovim. ([GitHub][1], [Software Recommendations Stack Exchange][2])

---

### **FauxPilot**

مشروع مفتوح المصدر مصمم كبديل محلي الاستضافة لـ GitHub Copilot. يستفيد من نماذج CodeGen من Salesforce التي تعمل عبر NVIDIA’s Triton Inference Server (وFasterTransformer). يمكن نشره عبر Docker، وهو متوافق مع عملاء شبيهة بـ Copilot ويعمل بشكل أفضل مع وحدة معالجة رسومات قادرة. ([GitHub][3])

---

### **Privy**

أداة أخرى مرخصة بترخيص MIT ومفتوحة المصدر تعمل محليًا. تقدم إكمالًا تلقائيًا للكود في الوقت الفعلي ووظيفة دردشة شبيهة بـ GitHub Copilot. يمكنها التكامل مع أنظمة تشغيل نماذج اللغة الكبيرة مثل Ollama أو llama.cpp أو llamafile، وتدعم نماذج الترميز الشهيرة (مثل متغيرات CodeLlama) اعتمادًا على أجهزتك. ([GitHub][4])

---

### **GPT4All, Continue, LocalPilot** *(وما شابهها)*

تم ذكرها من بين عدة أدوات محلية الاستضافة إلى جانب Tabby وFauxPilot؛ توفر هذه الأدوات مساعدة في الترميز تراعي الخصوصية محليًا. على الرغم من أنها ليست دائمًا بنفس مستوى الإتقان، إلا أنها قابلة للتطبيق إذا كانت قيود الأجهزة أو مهام العمل المحددة تتطلبها. ([Virtualization Howto][5])

---

### **Ollama (مع Docker)**

ليس بديلاً كاملاً لـ Copilot بمفرده، ولكنه أداة قوية مفتوحة المصدر لتشغيل نماذج اللغة الكبيرة محليًا. يمكنك استضافة نماذج مثل Phi-2 باستخدام Ollama عبر Docker، ثم الاتصال بها عبر VS Code باستخدام ملحق لنماذج اللغة الكبيرة (مثل `llm-vscode` من Hugging Face). هذا يسمح لك بشكل أساسي بالدردشة مع نموذج محلي أو الحصول على مساعدة في الترميز منه. ([Tommaso Colella][6], [Reddit][7])

---

### **الضجة المجتمعية**

من مناقشات Reddit:

* "استضف نسختك الخاصة من 'Copilot' مجانًا باستخدام Ollama AI على خادم docker" — تسلط الضوء على فعالية Ollama وتكامله مع VS Code. ([Reddit][7])
* "Tabby هو (الآن) الأداة 'مفتوحة المصدر والمحلية' الأكثر شيوعًا" — مشيرة إلى تبنيه المتزايد. ([Reddit][8])

---

### **التوصيات الملخصة**

* **إذا كنت تبحث عن بديل مفتوح المصدر ومتقن لـ Copilot:** ابدأ مع **Tabby**.
* **إذا كنت تريد شيئًا أقرب إلى بنية Copilot التحتية (ولديك وحدة معالجة رسومات جيدة):** تحقق من **FauxPilot**.
* **إذا كنت تريد ميزات كود + دردشة مع مرونة في النماذج/وقت التشغيل:** جرب **Privy**.
* **هل تريد تحكمًا كاملاً في نقاط النهاية والنماذج؟** زوج **Ollama** مع نموذج اللغة الكبيرة الخاص بك، ثم اتصل باستخدام واجهات نماذج اللغة الكبيرة القياسية.

---

### **الخطوات التالية لك**

1. **قياس إمكانيات الأجهزة:** قد يتطلب FauxPilot وPrivy وحدة معالجة رسومات جيدة؛ بينما Tabby أخف وزنًا.
2. **اختر إطار عمل/وقت تشغيل:**

   * **Tabby**: اختيار رائع شامل مع دعم للمحرر.
   * **FauxPilot**: شبيه بـ Copilot مع Docker وTriton.
   * **Privy**: إعداد مرن، لا يرتبط بنموذج محدد.
   * **Ollama + نموذج لغة كبيرة**: افعلها بنفسك بحتة — رائع إذا كنت مرتاحًا لبناء نقاط النهاية بنفسك.
3. **الاتصال ببيئة التطوير المتكاملة الخاصة بك:** يدعم VS Code (وغيرها) استخدام هذه الأدوات عبر نقاط النهاية المحلية، تمامًا مثل Copilot.

دعني أعرف إذا كنت تريد مساعدة للبدء مع أي أداة محددة أو إرشادات خطوة بخطوة للإعداد!

[1]: https://github.com/TabbyML/tabby?utm_source=chatgpt.com "TabbyML/tabby: Self-hosted AI coding assistant"
[2]: https://softwarerecs.stackexchange.com/questions/90507/foss-alternative-to-github-copilot?utm_source=chatgpt.com "FOSS alternative to GitHub Copilot?"
[3]: https://github.com/fauxpilot/fauxpilot?utm_source=chatgpt.com "FauxPilot - an open-source alternative to ..."
[4]: https://github.com/srikanth235/privy?utm_source=chatgpt.com "srikanth235/privy: An open-source alternative to ..."
[5]: https://www.virtualizationhowto.com/2025/05/best-self-hosted-github-copilot-ai-coding-alternatives/?utm_source=chatgpt.com "Best Self-hosted GitHub Copilot AI Coding Alternatives"
[6]: https://gioleppe.github.io/posts/diy-copilot-phi/?utm_source=chatgpt.com "DIY self-hosted Copilot using Phi-2 and Ollama"
[7]: https://www.reddit.com/r/vscode/comments/1by7njo/self_host_your_own_copilot_for_free_with_ollama/?utm_source=chatgpt.com "Self host your own \"Copilot\" for FREE with Ollama AI on a ..."
[8]: https://www.reddit.com/r/LocalLLaMA/comments/12m8fnm/best_local_equivalent_of_github_copilot/?utm_source=chatgpt.com "Best local equivalent of GitHub Copilot? : r/LocalLLaMA"