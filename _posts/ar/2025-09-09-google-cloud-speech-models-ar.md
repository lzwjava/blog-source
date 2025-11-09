---
audio: false
date: 2025-09-09
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: مقارنة نماذج جوجل كلاود للتحويل من الكلام إلى النص
translated: true
type: note
---

إليك تفصيل واضح للاختلافات بين نماذج تحويل الكلام إلى نص المختلفة في Google Cloud's API V2 — مُنظمة حسب عائلة النموذج وحالة الاستخدام، بدون جداول لتبقى سهلة القراءة:

---

## عائلة Chirp (نماذج الكلام العالمية - USM)

### **`chirp`**

*   **ما هو**: نموذج الكلام العالمي الأصلي من جوجل، يدعم النقل متعدد اللغات المتنوع في السياقات غير المتدفقة.([Google Cloud][1])
*   **طريقة الاستخدام**: يعمل مع طرق المزامنة (`Recognize`) والمجموعة (`BatchRecognize`)؛ **لا** يدعم البث المباشر (الاستجابة الفورية).([Google Cloud][1])
*   **القيود**:
    *   لا يدعم البث المباشر (الاستجابة الفورية)
    *   يفتقر إلى درجات الثقة، والتعرف على المتحدثين، والتكيف، والتطبيع القسري، ودرجة الثقة على مستوى الكلمة([Google Cloud][1])

### **`chirp_2`**

*   **ما هو**: نموذج الكلام العالمي من الجيل التالي، أكثر دقة وكفاءة من الأصلي، مع دعم البث المباشر والمتزامن والمجموعة. يقدم نقلًا متعدد اللغات وترجمة، بالإضافة إلى تكيف النموذج.([Google Cloud][2], [Medium][3])

### **`chirp_3`**

*   **ما هو**: أحدث جيل مع تحسينات إضافية في الدقة والسرعة. يدعم التعرف عبر البث المباشر والمتزامن والمجموعة، بالإضافة إلى تعرف على المتحدثين والكشف التلقائي عن اللغة.([Google Cloud][4])
*   **الميزات المدعومة**:
    *   البث المباشر (`StreamingRecognize`)، والمتزامن (`Recognize`)، والمجموعة (`BatchRecognize`) جميعها مدعومة([Google Cloud][4])
    *   يدعم تعرف على المتحدثين والكشف عن اللغة([Google Cloud][4])
    *   لا يددمج الطوابع الزمنية على مستوى الكلمة أو التكيف([Google Cloud][4])

---

## النماذج التقليدية / ذات الأغراض العامة

هذه نماذج ذات بنية قديمة يتم الحفاظ عليها primarily للتوافق مع الإصدارات السابقة:

*   **`long`**: جيد للمحتوى طويل الشكل مثل الوسائط أو المحادثات العفوية.([Google Cloud][2])
*   **`short`**: مُحسّن للعبارات القصيرة جدًا (بضع ثوانٍ) — مثالي للأوامر.([Google Cloud][2])
*   **`telephony` / `telephony_short`**: مصمم خصيصًا للصوت عبر الهاتف (عادة 8 كيلوهرتز). المتغير "short" يتعامل مع العبارات القصيرة أو ذات الكلمة الواحدة.([Google Cloud][2])
*   **النماذج الطبية**:
    *   `medical_conversation`: للحوارات بين مقدم الرعاية والمريض، مع فصل المتحدثين.
    *   `medical_dictation`: للملاحظات التي يمليها متحدث واحد.([Google Cloud][2])

---

## ملخص اختلافات النماذج حسب حالة الاستخدام

*   **تريد أفضل دقة في غير المتدفق ومتعدد اللغات؟** → **`chirp`**
*   **تريد دعم البث المباشر + متعدد اللغات + التكيف؟** → **`chirp_2`**
*   **تريد البث المباشر، وتعرف على المتحدثين، والكشف التلقائي عن اللغة، وأعلى دقة؟** → **`chirp_3`**
*   **مجرد نقل بسيط لمحتوى طويل؟** → **`long`**
*   **تتعامل مع أوامر منطوقة قصيرة؟** → **`short`**
*   **تسجيلات مكالمات هاتفية؟** → **`telephony`** أو **`telephony_short`**
*   **حالات استخدام طبية؟** → **`medical_conversation`** أو **`medical_dictation`**

---

## السياق من وثائق جوجل

صفحة "Select a transcription model" من جوجل (المحدثة في 4 سبتمبر 2025) تتضمن جميع معرفات النماذج والوصف أعلاه. وتلاحظ أيضًا أن النماذج التقليدية لا يتم صيانتها بنشاط ولكنها محتفظ بها للتوافق مع الإصدارات السابقة.([Google Cloud][2])

وملاحظة سابقة حول "latest\_long" / "latest\_short" تشير إلى مجموعة أخرى من النماذج القائمة على Conformer — ولكن هذه خارج سلالة Chirp وليست ذات صلة إذا كنت تركز تحديدًا على نماذج Chirp أو النماذج التقليدية.([Google Cloud][5])

---

## باختصار — كيفية الاختيار:

*   **أعلى جودة + ميزات جديدة (تعرف على المتحدثين، بث مباشر، إلخ)** → **`chirp_3`**
*   **دعم البث المباشر وتكيف النموذج** → **`chirp_2`**
*   **خط أساس غير متدفق متعدد اللغات** → **`chirp`**
*   **عبارات قصيرة، صوت طويل، هاتف، طبي** → استخدم النموذج التقليدي المناسب (`short`, `long`, `telephony`, `medical_*`)

---

أعلمني إذا كنت تريد المساعدة في اختيار النموذج المناسب بناءً على نوع الصوت المحدد، أو اللغة، أو الحاجة إلى معالجة البث المباشر مقابل المعالجة المجمعة!

[1]: https://cloud.google.com/speech-to-text/v2/docs/chirp-model?utm_source=chatgpt.com "Chirp: Universal speech model"
[2]: https://cloud.google.com/speech-to-text/v2/docs/transcription-model?utm_source=chatgpt.com "Select a transcription model - Cloud Speech-to-Text"
[3]: https://medium.com/google-cloud/transcribe-everything-everywhere-all-at-once-with-chirp-2-615ac362947d?utm_source=chatgpt.com "Transcribe everything everywhere all at once with Chirp 2"
[4]: https://cloud.google.com/speech-to-text/v2/docs/chirp_3-model?utm_source=chatgpt.com "Chirp 3 Transcription: Enhanced multilingual accuracy"
[5]: https://cloud.google.com/speech-to-text/docs/latest-models?utm_source=chatgpt.com "Introduction to Latest Models | Cloud Speech-to-Text ..."