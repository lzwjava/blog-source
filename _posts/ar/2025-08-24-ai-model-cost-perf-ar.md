---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دليل تكلفة وأداء النماذج الذكية
translated: true
type: note
---

إليك تفصيلًا أوضح لـ **نتائج المعايير** و**تسعير واجهة برمجة التطبيقات API** لكل نموذج — Claude 4 Opus (المشار إليه أيضًا باسم Claude Opus 4)، وGPT‑5 (القياسي/الكامل)، وGPT‑5 Mini، وGPT‑5 Nano، بالإضافة إلى o3 (OpenAI)، وClaude 4 Sonnet — دون استخدام الجداول، للحفاظ على الشكل مرتبًا وسهل القراءة.

---

## أداء المعايير (SWE-bench)

يعكس هذا مدى جودة أداء النماذج في مهام هندسة البرمجيات:

*   **Claude 4 Opus (14 مايو 2025)**: 67.60
*   **GPT‑5 (7 أغسطس 2025، استدلال متوسط)**: 65.00
*   **Claude 4 Sonnet (14 مايو 2025)**: 64.93 ([SWE-bench][1])

**الخلاصة**: يتصدر Claude 4 Opus الأداء في معيار SWE-bench بفارق طفيف، يليهما عن كثب كل من GPT-5 وClaude-Sonnet.

---

## تسعير واجهة برمجة التطبيقات API (لكل مليون رمز token)

### **Claude 4 Opus**

*   الإدخال: **15 دولارًا**
*   الإخراج: **75 دولارًا** ([Anthropic][2], [LaoZhang AI][3], [Simon Willison’s Weblog][4])

### **GPT-5 (القياسي/الكامل)**

*   الإدخال: **1.25 دولارًا**
*   الإدخال المخبأ (عند إعادة الاستخدام): **0.125 دولارًا**
*   الإخراج: **10 دولارات** ([OpenAI][5])

### **GPT-5 Mini**

*   الإدخال: **0.25 دولارًا**
*   الإخراج: **2 دولاران** ([OpenAI][5], [WIRED][6])

### **GPT-5 Nano**

*   الإدخال: **0.05 دولارًا**
*   الإخراج: **0.40 دولارًا** ([OpenAI][5], [WIRED][6])

### **o3-mini** (للتوضيح)

*   التسعير متاح عبر مرجع o4‑mini:
*   الإدخال: **1.10 دولارًا**، الإخراج: **4.40 دولارات** ([Simon Willison’s Weblog][4])

### **Claude 4 Sonnet**

*   الإدخال: **3 دولارات**، الإخراج: **15 دولارًا** ([LaoZhang AI][3])

---

## أبرز نقاط المقارنة السريعة

*   **أفضل أداء**: يتفوق Claude 4 Opus بشكل طفيف على كل من GPT-5 وClaude Sonnet في معايير الترميز.
*   **أقل تكلفة لكل رمز token**:
    *   **GPT-5 Nano** هو الأرخص على الإطلاق — مثالي للمهام الخفيفة مثل التلخيص.
    *   **GPT-5 Mini** يوفر توازنًا بين السرعة وبأسعار معقولة.
    *   **GPT-5 القياسي** يظل فعالاً من حيث التكلفة، خاصة مع ذاكرة التخزين المؤقت الرخيصة.
*   **نماذج Claude**، كل من Opus وSonnet، أغلى بكثير لكل رمز token لكنها تبرر تسعيرها من خلال قدرات استدلالية ووكيل agent أقوى.

---

## ملخص (واضح وموجز):

*   **Claude 4 Opus**: أفضل أداء، تكلفة عالية (15 دولارًا للإدخال / 75 دولارًا للإخراج).
*   **GPT-5 (الكامل)**: أداء رائع (يأتي مباشرة بعد Opus)، تكلفة أقل بكثير (1.25 دولارًا للإدخال / 10 دولارات للإخراج).
*   **GPT-5 Mini**: خيار متوسط الفئة مناسب للميزانية (0.25 دولارًا للإدخال / 2 دولاران للإخراج).
*   **GPT-5 Nano**: مثالي للمهام الخفيفة أو الاستخدام واسع النطاق منخفض التكلفة (0.05 دولارًا للإدخال / 0.40 دولارًا للإخراج).
*   **Claude 4 Sonnet**: تكلفة/أداء في منطقة وسطى (3 دولارات للإدخال / 15 دولارًا للإخراج)، لكن أداؤه في المعايير أقل قليلاً من الآخرين.

---

أعلمني إذا كنت تريد المساعدة في تقدير **التكلفة الشهرية** لنمط استخدام معين، أو تحتاج إلى مقارنات تأخذ في الاعتبار التخزين المؤقت للمطالبات prompt caching وخصومات الدُفعات batch discounts!

[1]: https://www.swebench.com/?utm_source=chatgpt.com "SWE-bench Leaderboards"
[2]: https://www.anthropic.com/pricing?utm_source=chatgpt.com "Pricing"
[3]: https://blog.laozhang.ai/ai-tools/claude-4-pricing-guide-2025/?utm_source=chatgpt.com "Claude 4.0 Pricing Guide: Complete Cost Analysis & Best ..."
[4]: https://simonwillison.net/2025/Aug/7/gpt-5/?utm_source=chatgpt.com "GPT-5: Key characteristics, pricing and model card"
[5]: https://openai.com/api/pricing/?utm_source=chatgpt.com "API Pricing"
[6]: https://www.wired.com/story/openais-gpt-5-is-here/?utm_source=chatgpt.com "OpenAI Finally Launched GPT-5. Here's Everything You ..."