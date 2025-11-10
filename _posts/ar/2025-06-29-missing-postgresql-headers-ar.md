---
audio: false
generated: true
lang: ar
layout: post
title: غياب ملف libpq-fe.h لـ psycopg2
translated: true
type: note
---

عند محاولة تثبيت حزمة Python `psycopg2`، واجهت خطأ يشير إلى أن wheel لم يمكن بناؤه بنجاح. الجزء الرئيسي من رسالة الخطأ هو:

```
In file included from psycopg/adapter_asis.c:28:
./psycopg/psycopg.h:36:10: fatal error: libpq-fe.h: No such file or directory
   36 | #include <libpq-fe.h>
      |          ^~~~~~~~~~~~
compilation terminated.
```

يحدث هذا الخطأ لأن الملف `libpq-fe.h`، وهو ملف رأس من مكتبة عميل PostgreSQL، مفقود على نظامك. تتطلب الحزمة `psycopg2` هذا الملف للبناء من المصدر، حيث أنه يوفر الواجهة للاتبق بين Python وقواعد بيانات PostgreSQL. أدناه، سأشرح سبب حدوث هذا وسأقدم حلاً خطوة بخطوة لإصلاحه.

---

### لماذا يحدث هذا الخطأ
حزمة `psycopg2` هي محول PostgreSQL لـ Python، وعند تثبيتها باستخدام `pip`، تحاول compile امتداداتها C. تعتمد هذه الامتدادات على مكتبة عميل PostgreSQL، وتحديداً رؤوس التطوير مثل `libpq-fe.h`. تؤكد رسالة الخطأ هذا:

```
It appears you are missing some prerequisite to build the package from source.
```

نظامك، الذي يبدو أنه توزيعة Linux مبنية على Debian (استنادًا إلى استخدام `x86_64-linux-gnu-gcc`)، يفتقر إلى ملفات تطوير PostgreSQL الضرورية. بدون هذه الملفات، تفشل عملية compilation، مما يمنع بناء wheel لـ `psycopg2`.

كما يقترح الخطأ خيارين:
1.  تثبيت الحزمة الثنائية المسبقة الصنع `psycopg2-binary` عبر PyPI.
2.  تثبيت المتطلبات الأساسية المفقودة وبناء `psycopg2` من المصدر.

نظرًا لأن مشروعك يحدد `psycopg2` (وليس `psycopg2-binary`) في ملف المتطلبات، ولأن البناء من المصدر قد يكون ضروريًا للتوفيق أو التخصيص، سنركز على إصلاح عملية البناء. ومع ذلك، سأذكر خيار الحزمة الثنائية لاحقًا للإكمال.

---

### كيفية إصلاح الخطأ
لحل هذه المشكلة، تحتاج إلى تثبيت حزمة تطوير عميل PostgreSQL، والتي توفر `libpq-fe.h` وملفات أخرى ضرورية. إليك الطريقة:

#### الخطوة 1: تحديد نظامك
يحتوي ناتج البناء الخاص بك على `x86_64-linux-gnu-gcc`، مما يشير إلى أنك على الأرجح تستخدم نظامًا مبنيًا على Debian مثل Ubuntu. سيتم تخصيص الحل لهذا، ولكن سأذكر بدائل للتوزيعات الأخرى لاحقًا.

#### الخطوة 2: تثبيت حزمة تطوير PostgreSQL
في الأنظمة المبنية على Debian (مثل Ubuntu)، تحتوي الحزمة `libpq-dev` على رؤوس مكتبة عميل PostgreSQL، بما في ذلك `libpq-fe.h`. قم بتثبيتها باستخدام الأمر التالي:

```bash
sudo apt-get update
sudo apt-get install libpq-dev
```

- **`sudo apt-get update`**: يضمن أن قائمة الحزم لديك محدثة.
- **`sudo apt-get install libpq-dev`**: يقوم بتثبيت ملفات التطوير لمكتبة عميل PostgreSQL.

تضع هذه الحزمة الملف `libpq-fe.h` في موقع قياسي (عادة `/usr/include/postgresql`)، والذي تبحث عنه عملية البناء (كما يظهر في مسار include الخاص بك: `-I/usr/include/postgresql`).

#### الخطوة 3: إعادة محاولة التثبيت
بمجرد تثبيت `libpq-dev`، أعد محاولة تثبيت المتطلبات الخاصة بك:

```bash
pip install -r scripts/requirements/requirements.local.txt
```

يجب أن ينجح هذا الآن، حيث سيصبح ملف `libpq-fe.h` المفقود متاحًا، مما يسمح لـ `psycopg2` ببناء wheel الخاص به.

---

### التحقق من الإصلاح
إذا فشل التثبيت مرة أخرى، تحقق من تثبيت رؤوس PostgreSQL بشكل صحيح:
- قم بتشغيل `pg_config --includedir` لمعرفة مكان وجود الرؤوس (مثال: `/usr/include/postgresql`).
- تأكد من أن هذا يتطابق مع مسار include في أمر البناء (`-I/usr/include/postgresql`).

يظهر ناتج البناء الخاص بك `-DPG_VERSION_NUM=140018`، مما يشير إلى أنه يستهدف PostgreSQL 14. يجب أن تعمل حزمة `libpq-dev` مع رؤوس PostgreSQL 14.

---

### بديل: استخدام الحزمة الثنائية
إذا كنت لا تحتاج إلى بناء `psycopg2` من المصدر (على سبيل المثال، لتحسينات أو توافق معين)، يمكنك تثبيت الحزمة المسبقة الصنع `psycopg2-binary` بدلاً من ذلك:

```bash
pip install psycopg2-binary
```

لاستخدام هذا في مشروعك، قم بتحديث `scripts/requirements/requirements.local.txt` لاستبدال `psycopg2` بـ `psycopg2-binary`. ومع ذلك، لاحظ أن `psycopg2-binary` قد يكون لها قيود (مثل مشاكل التوافق المحتملة مع إصدارات معينة من PostgreSQL)، لذا فإن البناء من المصدر هو الأفضل إذا كان مشروعك يتطلبه.

---

### للتوزيعات الأخرى
إذا لم تكن على نظام مبني على Debian، قم بتثبيت الحزمة المكافئة:
- **Red Hat/CentOS/Fedora**: `sudo yum install postgresql-devel` أو `sudo dnf install postgresql-devel`
- **Arch Linux**: `sudo pacman -S postgresql-libs`
- **macOS (مع Homebrew)**: `brew install libpq`

ثم، أعد تشغيل أمر `pip install`.

---

### الملخص
يحدث الخطأ لأن `libpq-fe.h` مفقود، وهو جزء من ملفات تطوير عميل PostgreSQL. بالنسبة لنظامك المبني على Debian، يجب أن يحل تثبيت `libpq-dev` باستخدام `sudo apt-get install libpq-dev` المشكلة. بعد ذلك، أعد تشغيل أمر `pip install` الخاص بك، ويجب أن يبني `psycopg2` بنجاح. إذا كنت تفضل إصلاحًا أسرع ولا تحتاج إلى compilation من المصدر، فاستخدم `psycopg2-binary` بدلاً من ذلك.