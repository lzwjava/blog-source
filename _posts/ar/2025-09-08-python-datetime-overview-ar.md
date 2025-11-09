---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: نظرة عامة على وحدة التاريخ والوقت في بايثون
translated: true
type: note
---

### نظرة عامة على وحدة datetime في بايثون

توفر وحدة `datetime` في بايثون فئات للتعامل مع التواريخ، الأوقات، والطوابع الزمنية. وهي موجودة في المكتبة القياسية، لذا لا حاجة لتثبيتها. تشمل الفئات الرئيسية:
- `date`: تتعامل مع التواريخ (السنة، الشهر، اليوم).
- `time`: تتعامل مع الأوقات (الساعة، الدقيقة، الثانية، الجزء من المليون من الثانية).
- `datetime`: تجمع بين التاريخ والوقت.
- `timedelta`: تمثل مدة زمنية (مثلًا، لإجراء العمليات الحسابية على التواريخ).

هي مفيدة لمهام مثل تسجيل الطوابع الزمنية، حساب المدد، أو تنسيق التواريخ للعرض/الإخراج.

### استيراد الوحدة

استورد الوحدة كاملة أو الفئات المحددة حسب الحاجة:

```python
import datetime  # الوحدة كاملة

# أو استورد فئات محددة
from datetime import datetime, date, time, timedelta
```

### الحصول على التاريخ والوقت الحاليين

استخدم `datetime.now()` للحصول على التاريخ والوقت المحليين الحاليين ككائن `datetime`.

```python
import datetime

now = datetime.datetime.now()
print(now)  # الإخراج: مثلًا، 2023-10-05 14:30:45.123456
print(type(now))  # <class 'datetime.datetime'>
```

للحصول على وقت UTC، استخدم `datetime.utcnow()` (ويفضل استخدام `datetime.now(timezone.utc)` مع الاستيراد من `datetime.timezone` لدعم النطاقات الزمنية).

### إنشاء كائنات التاريخ والوقت

أنشئ الكائنات يدويًا باستخدام منشئها.

```python
# التاريخ: سنة، شهر، يوم
d = datetime.date(2023, 10, 5)
print(d)  # 2023-10-05

# الوقت: ساعة، دقيقة، ثانية، جزء من المليون من الثانية (اختياري)
t = datetime.time(14, 30, 45)
print(t)  # 14:30:45

# Datetime: تجمع بين التاريخ والوقت
dt = datetime.datetime(2023, 10, 5, 14, 30, 45)
print(dt)  # 2023-10-05 14:30:45
```

احذف الأجزاء غير المطلوبة (مثلًا، `datetime.datetime(2023, 10, 5)` ينشئ كائن datetime عند منتصف الليل).

### تنسيق التواريخ (strftime)

حول التواريخ إلى سلاسل نصية باستخدام `strftime` مع رموز التنسيق (مثلًا، `%Y` للسنة، `%m` للشهر).

```python
now = datetime.datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # مثلًا، 2023-10-05 14:30:45

# التنسيقات الشائعة:
# %A: اسم اليوم الكامل (مثل Thursday)
# %B: اسم الشهر الكامل (مثل October)
# %Y-%m-%d: التاريخ بصيغة ISO
```

### تحليل التواريخ من السلاسل النصية (strptime)

حول السلاسل النصية إلى كائنات `datetime` باستخدام `strptime` مع تنسيق مطابق.

```python
date_str = "2023-10-05 14:30:45"
parsed = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(parsed)  # 2023-10-05 14:30:45
print(type(parsed))  # <class 'datetime.datetime'>
```

يجب أن يطابق التنسيق تمامًا، وإلا سيرفع `ValueError`.

### العمليات الحسابية على التواريخ باستخدام timedelta

أضف أو اطرح فترات زمنية باستخدام `timedelta`.

```python
now = datetime.datetime.now()
one_day = datetime.timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)  # التاريخ الحالي + 1 يوم

# الطرح
yesterday = now - one_day

# الأجزاء: أيام، ثوان، أجزاء من المليون من الثانية، أجزاء من الألف من الثانية، دقائق، ساعات، أسابيع
one_week = datetime.timedelta(weeks=1)
```

لحساب الفرق بين التواريخ:

```python
date1 = datetime.datetime(2023, 10, 5)
date2 = datetime.datetime(2023, 10, 10)
delta = date2 - date1
print(delta.days)  # 5
```

### النطاقات الزمنية (استخدام متقدم)

للعمليات التي تراعي النطاقات الزمنية، استخدم `timezone` (بايثون 3.3+). الوحدة لا تتعامل مع تحويلات النطاقات الزمنية بشكل أساسي؛ استخدمها مع مكتبة `pytz` للتعامل القوي.

```python
from datetime import datetime, timezone

# كائن datetime بسيط (بدون نطاق زمني)
naive = datetime.now()

# كائن مدرك لـ UTC
utc = datetime.now(timezone.utc)

# نطاق زمني مخصص (يتطلب tzinfo)
import pytz  # قد تحتاج pip install pytz
eastern = pytz.timezone("US/Eastern")
eastern_time = naive.astimezone(eastern)
```

### نصائح ومزالق شائعة
- **كائنات غير قابلة للتعديل**: كائنات `datetime` لا يمكن تعديلها مباشرة؛ العمليات الحسابية تنشئ كائنات جديدة.
- **أيام الشهر**: استخدم 29 لشهر فبراير في السنوات الكبيسة؛ الوحدة تتعامل مع هذا باستخدام `calendar` أو `dateutil` للتحقق من السنوات الكبيسة.
- **الأداء**: تجنب استدعاء `now()` بشكل متكرر في الحلقات التكرارية؛ خزن القيمة.
- **الأخطاء**: انتبه للتواريخ غير الصالحة (مثلًا، `date(2023, 2, 30)` سيرفع `ValueError`).
- **امتدادات المكتبات**: للتحليل المتقدم، فكر في استخدام حزم مثل `dateutil` أو `arrow`.

للحصول على الوثائق الكاملة، راجع الوثائق الرسمية لبايثون على [docs.python.org](https://docs.python.org/3/library/datetime.html). جرب هذه الأمثلة في مترجم بايثون.