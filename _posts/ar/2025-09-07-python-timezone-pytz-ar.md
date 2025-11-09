---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: التعامل مع المناطق الزمنية في بايثون باستخدام pytz
translated: true
type: note
---

### تثبيت pytz
pytz هي مكتبة Python من جهات خارجية للتعامل مع كائنات datetime المدركة للوحدة الزمنية. لاحظ أنه بدءًا من Python 3.9+، فإن الوحدة المضمنة `zoneinfo` هي المفضلة للكود الجديد (إنها في المكتبة القياسية وتتعامل مع التحديثات تلقائيًا)، لكن pytz لا تزال مستخدمة على نطاق واسع.

لتثبيت pytz، استخدم pip:
```
pip install pytz
```

### الاستخدام الأساسي مع pytz
تعمل pytz مع وحدة `datetime` في Python. المفاهيم الأساسية:
- **كائنات الوحدة الزمنية**: استخدم `pytz.timezone()` لإنشاء كائنات مدركة للوحدة الزمنية (على سبيل المثال، لـ "UTC" أو "America/New_York").
- **التوطين**: أرفق وحدة زمنية بكائن `datetime` غير المدرك للوحدة الزمنية باستخدام `.localize()`.
- **التحويل**: استخدم `.astimezone()` للتحويل بين الوحدات الزمنية.
- **المزالق**: تجنب استخدام منشئات `pytz` مباشرة على كائنات `datetime`؛ قم دائمًا بالتوطين أولاً للتعامل مع التوقيت الصيفي (DST) بشكل صحيح.

استورد الوحدات المطلوبة:
```python
import datetime
import pytz
```

### أمثلة

#### 1. الحصول على الوقت الحالي في وحدة زمنية محددة
استخدم `pytz.utc` أو وحدات زمنية محددة. اعمل دائمًا مع UTC داخليًا كأفضل الممارسات.

```python
# الحصول على الوقت الحالي بالتوقيت العالمي المنسق (UTC)
utc_now = datetime.datetime.now(pytz.utc)
print(utc_now)  # على سبيل المثال: 2023-10-15 14:30:00+00:00

# الحصول على الوقت الحالي بتوقيت شرق الولايات المتحدة
eastern = pytz.timezone('US/Eastern')
eastern_now = datetime.datetime.now(eastern)
print(eastern_now)  # على سبيل المثال: 2023-10-15 10:30:00-04:00 (يضبط لمراعاة التوقيت الصيفي)
```

#### 2. توطين وقت غير مدرك للوحدة الزمنية
تحويل datetime غير المدرك للوحدة الزمنية إلى datetime مدرك للوحدة الزمنية.

```python
# إنشاء datetime غير مدرك للوحدة الزمنية (على سبيل المثال، 15 أكتوبر 2023، 12:00)
naive_dt = datetime.datetime(2023, 10, 15, 12, 0)
print(naive_dt)  # 2023-10-15 12:00:00

# توطينه إلى توقيت شرق الولايات المتحدة
eastern = pytz.timezone('US/Eastern')
aware_dt = eastern.localize(naive_dt)
print(aware_dt)  # 2023-10-15 12:00:00-04:00
```

#### 3. التحويل بين الوحدات الزمنية
قم أولاً بتوطين datetime، ثم قم بالتحويل.

```python
# ابدأ بالوقت العالمي المنسق (UTC)
utc_dt = pytz.utc.localize(datetime.datetime(2023, 10, 15, 14, 0))
print(utc_dt)  # 2023-10-15 14:00:00+00:00

# التحويل إلى توقيت المحيط الهادئ
pacific = pytz.timezone('US/Pacific')
pacific_dt = utc_dt.astimezone(pacific)
print(pacific_dt)  # 2023-10-15 07:00:00-07:00
```

#### 4. التعامل مع قوائم الوحدات الزمنية
تدعم pytz أسماء الوحدات الزمنية الشائعة من قاعدة بيانات أولسون.

```python
# عرض الوحدات الزمنية المتاحة
print(pytz.all_timezones[:10])  # عينة: ['Africa/Abidjan', 'Africa/Accra', ...]

# أو وحدات زمنية خاصة ببلد معين
print(pytz.country_timezones['US'])  # ['America/New_York', 'America/Los_Angeles', ...]
```

### الانتقال إلى zoneinfo (مُوصى به لـ Python 3.9+)
لإصدارات Python الأحدث، استخدم الوحدة المضمنة `zoneinfo` بدلاً من pytz للبساطة:
```python
from zoneinfo import ZoneInfo
import datetime

# مكافئ لأمثلة pytz
eastern_now = datetime.datetime.now(ZoneInfo('US/Eastern'))
aware_dt = datetime.datetime(2023, 10, 15, 12, 0).replace(tzinfo=ZoneInfo('US/Eastern'))
```

### المشاكل الشائعة والنصائح
- **الأوقات الغامضة**: أثناء انتقالات التوقيت الصيفي، استخدم `is_dst` في `.localize()` (على سبيل المثال، `eastern.localize(naive_dt, is_dst=False)`).
- **تطبيع UTC**: قم بالتحويل إلى UTC قبل إجراء العمليات الحسابية لتجنب الأخطاء.
- **تحديث pytz**: تستخدم بيانات IANA tzdata؛ حافظ على تحديثها عبر pip.
- للمزيد، راجع [توثيق pytz](https://pythonhosted.org/pytz/). إذا واجهت أخطاء، الصق مقاطع الكود للحصول على مساعدة في التصحيح.