---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: إصلاح بطء تحميلات هاجينج فيس
translated: true
type: note
---

هذه مشكلة شائعة عند تنزيل مجموعات بيانات HF الضخمة عبر وكيل. مزيج من:

* العديد من الملفات بحجم مئات الميغابايت
* Python `requests` / `huggingface_hub`
* وكيل HTTP محلي (خاصة Clash أو V2Ray أو tun2socks)

غالبًا ما يؤدي إلى إنتاجية بطيئة للغاية أو إعادة تعيين الاتصال.

فيما يلي أهم الإصلاحات.

---

## 1. **أفضل إصلاح: استخدم `hf_transfer`**

تمتلك Hugging Face أداة تنزيل معجلة تمنح سرعات **أسرع من 10× إلى 50×** وأكثر استقرارًا.

التثبيت:

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
```

شغل أمرك مرة أخرى.

هذا وحده عادةً ما يصلح مشكلة التنزيلات البطيئة عبر الوكلاء.

---

## 2. استخدم `aria2c` مع Hugging Face CLI (الأسرع للملفات الضخمة)

إذا كنت تقوم بالتنزيل يدويًا:

```bash
pip install huggingface_hub[cli]
sudo apt install aria2
```

ثم قم بالتنزيل:

```bash
huggingface-cli download --repo-type dataset openwebtext --local-dir ./openwebtext --local-dir-use-symlinks False
```

يستخدم HF CLI تلقائيًا aria2، الذي يتعامل مع:

* اتصالات متوازية
* استئناف التنزيل
* الوكلاء غير المستقرين

بشكل أفضل بكثير من `requests`.

---

## 3. إصلاح بطء الوكيل المحلي: استخدم SOCKS على مستوى النظام بدلاً من HTTP

إذا كنت تستخدم شيئًا مثل:

```
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
```

قم بالتبديل إلى SOCKS5 إذا كان وكيلك يدعمه:

```bash
export ALL_PROXY=socks5://127.0.0.1:7891
```

بروتوكول SOCKS **أكثر استقرارًا بكثير** لبث الملفات الكبيرة.

---

## 4. تعطيل الوكيل للملفات الكبيرة

إذا كانت شبكتك الأساسية جيدة ولكن الوكيل يبطئ السرعة:

```bash
unset HTTP_PROXY
unset HTTPS_PROXY
unset ALL_PROXY
```

ثم أعد المحاولة. بعض خوادم HF سريعة حتى بدون وكيل اعتمادًا على المنطقة.

---

## 5. استخدم مرآة HF (الصين القارية / تايوان أحيانًا بطيئة)

يمكنك إجبار استخدام CDN:

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

ثم شغل الأمر مرة أخرى.
هذا يحسن السرعات بشكل كبير لبعض المناطق.

---

## 6. استئناف التنزيلات المتقطعة

يتم تخزين مجموعات بيانات HF مؤقتًا هنا:

```
~/.cache/huggingface/datasets/
```

إذا تم تنزيل أي ملف جزئيًا، فإن HF يستأنف تلقائيًا — لا حاجة للبدء من الصفر.

---

## 7. إذا كانت لا تزال بطيئة: تجنب مجموعة البيانات الكاملة، استخدم جزءًا صغيرًا

OpenWebText أكبر من 40 جيجابايت.
يمكنك تحميل جزء صغير فقط:

```python
from datasets import load_dataset
ds = load_dataset("openwebtext", split="train[:1%]")
```

---

## توصية سريعة

الأسرع + الأسهل:

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
python data/openwebtext_10k/prepare.py
```

يجب أن ترى فورًا قفزة في سرعات التنزيل.

---

إذا أردت، يمكنني أن أوضح لك كيفية تعديل `prepare.py` الخاص بك لاستخدام أداة تنزيل مخصصة تمامًا مع إعادة المحاولة/التراجع والجلب المتوازي، بحيث يكون خط الأنابيب الخاص بك دائمًا سريع التنزيل ولا يتوقف أبدًا.