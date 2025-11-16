---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تنزيل مجموعة بيانات OpenWebText الفرعية عبر Hugging Face
translated: true
type: note
---

مجموعة البيانات التي تشير إليها مستضافة على Hugging Face تحت معرف المستودع `Skylion007/openwebtext`. الملف المحدد `subsets/urlsf_subset00.tar` يمكن الوصول إليه بشكل علني (لا يلزم مصادقة)، لذا يمكنك تنزيله باستخدام أداة Hugging Face CLI (`huggingface-cli`). إليك الطريقة:

### المتطلبات الأساسية
- قم بتثبيت Hugging Face Hub CLI إذا لم تكن قد قمت بذلك بالفعل:
  ```
  pip install huggingface_hub
  ```
- (اختياري) إذا كان لديك أمر `huggingface-cli` مختصر كـ `hf` (شائع في بعض الأنظمة)، يمكنك استخدام هذا الاختصار. وإلا، استخدم البادئة الكاملة `huggingface-cli`.

### أمر التحميل
شغّل هذا في طرفيتك:
```
huggingface-cli download Skylion007/openwebtext subsets/urlsf_subset00.tar --local-dir ./openwebtext
```
- سيؤدي هذا إلى تنزيل الملف إلى `./openwebtext/subsets/urlsf_subset00.tar` (سيتم إنشاء المجلد الفرعي `subsets` إذا لزم الأمر).
- الملف كبير جدًا (~1.5 جيجابايت غير مضغوط، ولكنه أرشيف tar)، لذا تأكد من وجود مساحة تخزين كافية واتصال مستقر بالإنترنت.
- إذا كنت تريد تنزيله بدون هيكل المستودع (مباشرة إلى المجلد الحالي)، أضف `--repo-type dataset` (على الرغم من أنه مُضمّن هنا implicitly) أو اضبط `--local-dir`.

### استخدام Python (بديل)
إذا كنت تفضل كتابته كبرنامج نصي في Python (عبر مكتبة `huggingface_hub` على سبيل المثال):
```python
from huggingface_hub import hf_hub_download

# التنزيل إلى المجلد الحالي
hf_hub_download(
    repo_id="Skylion007/openwebtext",
    filename="subsets/urlsf_subset00.tar",
    local_dir="./openwebtext",  # اختياري: يحدد المجلد الأساسي
    repo_type="dataset"
)
```
قم بتثبيت المكتبة أولاً: `pip install huggingface_hub`.

### ملاحظات
- هذه مجموعة فرعية من OpenWebText (مجموعة كبيرة من بيانات الويب). بعد التنزيل، ستحتاج إلى استخراج ملف `.tar` (على سبيل المثال: `tar -xvf subsets/urlsf_subset00.tar`).
- إذا فشل التحميل (بسبب مشاكل في الشبكة على سبيل المثال)، أعد المحاولة أو استخدم `--cache-dir` لتحديد موقع ذاكرة تخزين مؤقت مخصص.
- لمجموعة البيانات الكاملة أو المجموعات الفرعية الأخرى، تحقق من صفحة المستودع: https://huggingface.co/datasets/Skylion007/openwebtext.

إذا واجهت أخطاء، شارك الناتج (output) لمساعدتنا في تصحيحها!