---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: بناء جيكل يفتقر إلى خاصية التنظيف التلقائي
translated: true
type: note
---

لا تحتوي Jekyll نفسها على علم `--replace` أو `--refresh`. كل تشغيل لأمر `jekyll build` سيكتب (أو يستبدل) الملفات المُنشأة في مجلد `--destination` الذي تحدده، لكنه **لا يزيل الملفات القديمة** تلقائيًا التي لم تعد موجودة في مصدرك. هذا يعني أن الملفات القديمة قد تبقى.

إذا كنت تريد إخراج بناء نظيف، فأنت بحاجة إلى مسح دليل الوجهة بنفسك قبل تشغيل `jekyll build`. هناك طريقتان شائعتان:

**١. تنظيف يدوي في السكريبت الخاص بك**
قبل استدعاء `jekyll build`، امسح دليل الوجهة:

```python
import shutil

def run_jekyll(destination: str, extra_args: list[str]) -> int:
    # إزالة الملفات القديمة
    dest_path = Path(destination)
    if dest_path.exists():
        shutil.rmtree(dest_path)

    command = [
        "jekyll",
        "build",
        "--destination",
        destination,
        *extra_args,
    ]
    completed = subprocess.run(command, check=False)
    return completed.returncode
```

**٢. استخدام `_site` الخاص بـ Jekyll نفسه**
إذا سمحت لـ Jekyll باستخدام `_site` الافتراضي تحت جذر مشروعك (بدلاً من `--destination` مخصص)، فإن `jekyll clean` متاح لمسح الإخراج قبل إعادة البناء:

```bash
jekyll clean && jekyll build
```

لكن `jekyll clean` يعرف فقط `_site`، وليس مجلدًا مخصصًا.

---

إذن:

* لا يوجد `--replace` مدمج.
* إذا كنت تستخدم وجهة مخصصة (كما في سكريبتك)، يجب عليك حذفها صراحة قبل البناء إذا كنت تريد إخراجًا جديدًا.

هل تريد مني ضبط السكريبت الخاص بك بحيث يحتوي على خيار `--clean` (مثل `jekyll clean`) يقوم تلقائيًا بمسح الوجهة قبل البناء؟