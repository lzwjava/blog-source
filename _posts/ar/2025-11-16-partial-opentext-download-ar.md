---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: شرح تنزيل Partial OpenWebText
translated: true
type: note
---

إجابة قصيرة: **لا، لا يقوم بتنزيل مجموعة OpenWebText بأكملها.** إنه يحضر فقط الشريحة التي تطلبها. ونعم، يمكنك رؤية تقدم التنزيل — حيث يعرضه Hugging Face تلقائيًا ما لم تقم بكتم السجلات.

إليك التفصيل:

---

## هل `load_dataset("openwebtext", split="train[:10000]")` يقوم بتنزيل مجموعة البيانات كاملة؟

**يقوم بتنزيل الأجزاء (shards) المطلوبة لتلك الشريحة فقط، وليس المجموعة الكاملة.**

يتم تخزين OpenWebText على Hugging Face في *أجزاء متعددة* (عشرات من ملفات `.jsonl.zst` مثلاً). عندما تقوم بتحميل أول 10,000 صف فقط، تقوم المكتبة بتنزيل عدد كافٍ من الأجزاء لتغطية هذه الأمثلة فقط.
إنها **لا** تقوم بتنزيل جميع الأجزاء.

لذا فإن حجم التنزيل يتناسب مع كمية البيانات التي تقوم بتحميلها فعليًا.

---

## كيف ترى تقدم التنزيل

عادةً ما ترى أشرطة تقدم في وحدة التحكم مثل:

```
Downloading (…)arrow…: 100%
Downloading (…)nload: 100%
Extracting…: 100%
Generating train split…: 100%
```

إذا كانت السجلات مكتومة أو كنت تريد رؤية أكثر، استخدم:

```python
from datasets import load_dataset
import datasets

datasets.logging.set_verbosity_info()

dataset = load_dataset("openwebtext", split="train[:10000]")
```

هذا يضمن ظهور أشرطة التقدم دائمًا.

---

## كيف ترى **كمية** البيانات التي تم تنزيلها

بعد التحميل:

```python
dataset._info
```

أو:

```python
dataset.info
```

أيضًا، يقوم Hugging Face بتخزين الملفات في المسار:

```
~/.cache/huggingface/datasets/
```

يمكنك التحقق من استخدام المساحة باستخدام:

```bash
du -sh ~/.cache/huggingface/datasets
```

---

## اختياري: فرض سجلات التصحيح التفصيلية

إذا كنت تريد سجلات مفصلة للغاية:

```python
datasets.logging.set_verbosity_debug()
```

---

## لماذا هذا مهم لـ NanoGPT

مقتطفات تدريب NanoGPT تستخدم:

```python
dataset = load_dataset("openwebtext", split="train[:10000]")
```

لتجنب التنزيلات الضخمة أثناء الاختبار.
الأخبار الجيدة: السلوك يتطابق تمامًا مع ما تريده — **تنزيل جزئي وسريع**.

---

إذا كنت ترغب، يمكنني أن أوضح:

* كيفية معاينة البيانات قبل التنزيل
* كيفية تحميل OpenWebText محليًا
* كيفية التحقق من عدد الأجزاء التي تتعامل معها شريحتك