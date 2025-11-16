---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: تنزيل جزء من أوبن ويب تكست
translated: true
type: note
---

آه، فهمت — تريد التمسك بـ **Hugging Face CLI** ولكنك لا تزال ترغب في الحصول على جزء صغير فقط. المشكلة هي: أن أداة CLI مصممة لتنزيل **الملفات كاملة**، وليس شرائح منها. مجموعة OpenWebText مقسمة إلى 21 ملف `.tar` فرعي؛ إذا استخدمت أداة CLI، سيقوم بتنزيل أرشيفات tar كاملة، لذا لا يمكنك الحصول على "1%" بالضبط دون تنزيل أجزاء كبيرة.

إليك نهج عملي:

---

### 1. تنزيل مجموعة فرعية من الملفات فقط

بدلاً من الملفات الـ 21 كاملة، اختر فقط بضعة أرشيفات tar:

```bash
huggingface-cli download \
  --repo-type dataset openwebtext/subsets/urlsf_subset00.tar \
  --local-dir ./openwebtext
huggingface-cli download \
  --repo-type dataset openwebtext/subsets/urlsf_subset01.tar \
  --local-dir ./openwebtext
```

* كل ملف tar بحجم ~625 ميجابايت، لذا إذا قمت بتنزيل 1–2 منها، فهذا يمثل تقريبًا 1–2% من مجموعة البيانات.
* يمكنك ضبط المجموعات الفرعية التي تختارها؛ Hugging Face لا تفرض ترتيبًا تسلسليًا.

---

### 2. استخراج ما تحتاجه فقط

بعد التنزيل:

```bash
cd ./openwebtext
tar -xvf urlsf_subset00.tar
tar -xvf urlsf_subset01.tar
```

ثم يمكنك معالجة بضعة مستندات فقط من هذه المجموعات الفرعية.

---

### 3. اختياري: الدمج مع HF Transfer

لتسريع تنزيلات CLI:

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
```

ثم أعد تجربة أوامر CLI — ستصبح التنزيلات أسرع بكثير.

---

إذا كنت تريد، يمكنني إنشاء **مقتطف أوامر صغير يختار تلقائيًا حوالي 1% من OpenWebText باستخدام CLI فقط**، حتى لا تضطر إلى اختيار أرشيفات tar يدويًا. هل تريد مني فعل ذلك؟