---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح خطأ تقسيم مجموعة البيانات
translated: true
type: note
---

يحدث الخطأ لأن ملف مجموعة البيانات المحلي الخاص بك (`/home/lzw/projects/nanoGPT/data/openwebtext_local/openwebtext.txt`) يحتوي على عينة واحدة فقط (على الأرجح سطر واحد أو محتوى فارغ تقريبًا)، لكن البرنامج النصي يحاول تقسيمه إلى مجموعات تدريب/اختبار باستخدام `test_size=0.1`. سيخصص هذا حوالي 0.1 عينة لمجموعة الاختبار (يتم تقريبها إلى عينة واحدة) ويترك 0 للتدريب، وهو ما يرفضه `datasets.train_test_split()` لتجنب مجموعة تدريب فارغة.

### إصلاحات سريعة
1. **استخدم مجموعة بيانات أكبر/أكثر اكتمالاً**:
   - يتوقع إعداد nanoGPT لـ OpenWebText مجموعة نصية كبيرة (ملايين المستندات). يبدو أن ملفك المحلي `openwebtext.txt` غير مكتمل — ربما يكون مجرد ملف بديل أو أن التحميل فشل.
   - قم بتنزيل عينة أو مجموعة فرعية مناسبة من OpenWebText:
     - استنسخ مستودع OpenWebText: `git clone https://github.com/jcpeterson/openwebtext.git` في المجلد `data/openwebtext_local/`.
     - أو استخدم نسخة معالجة مسبقًا من Hugging Face: قم بتثبيت `datasets` إذا لم يكن مثبتًا (`pip install datasets`)، ثم عدل `prepare.py` لتحميل البيانات عبر `load_dataset("openwebtext", split="train")` بدلاً من ملف محلي.
     - لأغراض الاختبار، أنشئ ملفًا بديلًا متعدد الأسطر في `openwebtext.txt` يحتوي على 10+ سطر على الأقل من نص عينة (مثل تكرار "Hello world." عدة مرات) لتجاوز عملية التقسيم.

2. **عدل التقسيم في `prepare.py`** (حوالي السطر 50):
   - إذا كان يجب عليك استخدام هذا الملف الصغير لأغراض التصحيح، فغيّر معلمات التقسيم:
     ```python
     # النسخة الأصلية (تسبب الخطأ):
     split_dataset = dataset.train_test_split(test_size=0.1, seed=2357, shuffle=True)

     # الخيار أ: تخطي التقسيم تمامًا (لا توجد مجموعة اختبار، التدريب على الكل):
     split_dataset = {"train": dataset}  # أو اضبط test_size=0

     # الخيار ب: استخدم test_size أصغر يعمل مع n=1 (مثل 0، أو تعامل مع مجموعات البيانات الصغيرة):
     if len(dataset) <= 1:
         split_dataset = {"train": dataset}
     else:
         split_dataset = dataset.train_test_split(test_size=0.1, seed=2357, shuffle=True)
     ```
   - أعد التشغيل: `python data/openwebtext_local/prepare.py`.

3. **تحقق من حجم مجموعة البيانات الخاصة بك**:
   - أضف أمر طباعة قبل التقسيم في `prepare.py` (حوالي السطر 45):
     ```python
     print(f"Dataset size: {len(dataset)}")
     ```
   - أعد التشغيل للتأكيد — يجب أن ينتج `1`. إذا كان الملف فارغًا أو تالفًا، أعد إنشاءه أو تحقق من أذونات الملف/الترميز (المتوقع هو UTF-8).

### الخطوات التالية الموصى بها لـ nanoGPT
- للتدريب الكامل، اتبع الإعداد الرسمي للبيانات في nanoGPT: راجع [ملف nanoGPT README](https://github.com/karpathy/nanoGPT#data) لتنزيل وإعداد Shakespeare أو OpenWebText بشكل صحيح. يتطلب OpenWebText مساحة تخزين كبيرة (~40 GB غير مضغوطة).
- إذا كان هذا لأغراض الاختبار المحلي، فانتقل إلى مجموعة بيانات Shakespeare المدمجة (أصغر حجمًا، لا تحتاج لتنزيلات خارجية): عدل `prepare.py` لتحميل `load_dataset("tiny_shakespeare")` أو استخدم `data/shakespeare_char/prepare.py` الموجود في nanoGPT.
- تأكد من الاعتماديات: `pip install datasets torch` (وغيرها من `requirements.txt` الخاص بـ nanoGPT).

إذا شاركت المزيد من `prepare.py` أو محتويات الملف، يمكنني تقديم نسخة مصححة.