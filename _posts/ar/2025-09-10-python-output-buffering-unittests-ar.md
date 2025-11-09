---
audio: false
date: 2025-09-10
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: حل مشكلة تخزين الإخراج المؤقت في بايثون أثناء الاختبارات
translated: true
type: note
---

نعم — هذا التأخير يكون في الغالب بسبب **مخزن مؤقت للإخراج**، وقد يجعل Git-Bash/mintty على Windows هذا أكثر وضوحًا. لا تحتاج إلى قائمة انتظار إلا إذا كنت تستخدم التسجيل متعدد العمليات؛ أولاً اجعل stdout/stderr غير مخزنين مؤقتًا وتجنب التخزين المؤقت الخاص بـ unittest.

### افعل هذا عند التشغيل

```bash
# PowerShell / CMD:
py -3.11 -u -m unittest -v

# Git-Bash:
PYTHONUNBUFFERED=1 py -3.11 -u -m unittest -v
# أو
PYTHONUNBUFFERED=1 python -u -m unittest -v
```

* `-u` = stdio غير مخزن مؤقتًا
* `PYTHONUNBUFFERED=1` = نفس التأثير، ويؤثر أيضًا على العمليات الفرعية

إذا كنت تستخدم `xx.py` مباشرة:

```bash
python -u xx.py -v
```

### اجعل الإخراج فوريًا داخل الكود الخاص بك (جاهز للإسقاط)

ضع هذا في أعلى جزء من تهيئة الاختبار (أو كتلة `if __name__ == "__main__":`):

```python
import os, sys
os.environ.setdefault("PYTHONUNBUFFERED", "1")

# Python 3.7+
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True, write_through=True)
    sys.stderr.reconfigure(line_buffering=True, write_through=True)

print("booting tests...", flush=True)
```

وعندما تستخدم `print(...)`، أضف `flush=True` للنقاط الحرجة.

### إذا كنت تستخدم وحدة `logging`

```python
import logging, sys
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
    force=True,  # 3.8+
)
# StreamHandler يقوم بتفريغ كل سجل؛ هذا يضمن أنه يشير إلى stdout
```

### انتبه للتخزين المؤقت في unittest

إذا قمت أنت (أو إطار العمل) بتمكينه، فسيتم حجز الإخراج حتى نهاية الاختبار:

* **تجنب**: `unittest.main(buffer=True)` أو `python -m unittest -b`
* استخدم الوضع الافتراضي (بدون `-b`) حتى تتم طباعة السجلات كما تحدث.

### نصائح خاصة بـ Git-Bash

* أحيانًا يجعل Mintty البرامج تعتقد أن stdout ليس TTY → المزيد من التخزين المؤقت. أفضل حلين لديك هما **مجموعة `-u`/`PYTHONUNBUFFERED`** المذكورة أعلاه أو simplement قم بالتشغيل من **Windows Terminal/PowerShell/CMD** للمقارنة.
* إذا قمت بإنشاء عمليات فرعية، فستقوم هي أيضًا بالتخزين المؤقت ما لم ترث البيئة. مع تصدير `PYTHONUNBUFFERED=1`، ستتصرف عمليات Python الفرعية بشكل صحيح.

### متى تكون قائمة الانتظار *مفيدة*

فقط إذا كنت تقوم بالتسجيل **متعدد العمليات**: استخدم `logging.handlers.QueueHandler/QueueListener` لنقل السجلات من العمال إلى العملية الرئيسية؛ وإلا فقد يعاني الطفل من مخازن مؤقتة أو تشابك.

إذا قمت بلصق snippet صغير لكيفية تشغيل الاختبارات (الأمر + أي وسائط `unittest.main(...)`) وكيف تقوم بالتسجيل/الطباعة، سأقوم بتخصيص أقل تغيير لجعل كل الإخراج فوريًا.