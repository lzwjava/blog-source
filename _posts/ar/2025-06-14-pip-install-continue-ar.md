---
audio: false
generated: true
lang: ar
layout: post
title: تثبيت Pip مع تجاهل الإخفاقات
translated: true
type: note
---

اعتذر عن الالتباس؛ العلم `--skip-existing` ليس خيارًا صالحًا في `pip`. لمتابعة تثبيت الحزم من ملف المتطلبات رغم الفشل، يمكنك استخدام العلم `--no-dependencies` لتجنب تعارضات التبعيات أو معالجة الأخطاء يدويًا. ومع ذلك، فإن أفضل نهج لتخطي الحزم الفاشلة ومتابعة تثبيت الأخرى هو استخدام حلقة في سكريبت shell. إليك أمر سطر واحد لمحاولة تثبيت كل حزمة من `requirements.top.txt` بشكل فردي، متجاهلاً الإخفاقات:

```bash
while read -r package; do pip install --ignore-installed "$package" || true; done < scripts/requirements/requirements.top.txt
```

### الشرح:
- `while read -r package`: يقرأ كل سطر (حزمة) من ملف المتطلبات.
- `pip install --ignore-installed "$package"`: يحاول تثبيت كل حزمة، متجاهلاً الإصدارات المثبتة مسبقًا.
- `|| true`: يضمن استمرار الحلقة حتى إذا فشل تثبيت حزمة ما (على سبيل المثال، بسبب عدم توافق الإصدارات مثل `tensorflow` مع Python 3.13).
- `< scripts/requirements/requirements.top.txt`: يحدد المسار إلى ملف المتطلبات الخاص بك.

### ملاحظات:
- **مشكلة TensorFlow**: الخطأ الذي واجهته سابقًا يشير إلى أن `tensorflow` غير متوافق مع Python 3.13. قد تحتاج إلى استخدام Python 3.12 أو إصدار أقدم لـ `tensorflow`. للمتابعة:
  1. أنشئ بيئة افتراضية بـ Python 3.12:
     ```bash
     python3.12 -m venv venv
     source venv/bin/activate
     ```
  2. شغل الأمر أعلاه في البيئة المفعلة.
- **التبعيات**: يمكن إضافة `--no-dependencies` إلى أمر `pip install` داخل الحلقة (`pip install --ignore-installed --no-dependencies "$package" || true`) لتجنب تعارضات التبعيات، ولكن هذا قد يسبب مشاكل إذا كانت الحزم تعتمد على تبعيات محددة.
- **بديل**: إذا كنت تريد استبعاد الحزم الإشكالية مثل `tensorflow`، قم بتحرير `requirements.top.txt` لإزالتها أو تحديد إصدارات متوافقة (مثل `tensorflow==2.17.0` لـ Python 3.12).

إذا واجهت المزيد من المشاكل أو تحتاج إلى مساعدة في تعديل ملف المتطلبات، دعني أعلم!