---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: ربط بايثون بـ آي بي إم دي بي ٢
translated: true
type: note
---

### نظرة عامة
IBM DB2 هو نظام إدارة قواعد بيانات علائقية، ويمكن لـ Python التفاعل معه باستخدام حزمة `ibm_db` التي توفر واجهة منخفضة المستوى، و`ibm_db_dbi`، وهي غلاف متوافق مع معيار DB-API 2.0 مبني فوق `ibm_db` لاستخدام أسهل وأكثر "بايثونية". `ibm_db` أكثر مباشرة وقوة ولكنه يتطلب معرفة أعمق، بينما `ibm_db_dbi` يحاكي وحدة `sqlite3` في Python، مما يجعله أبسط لإجراء عمليات قواعد البيانات القياسية. كلاهما جزء من برامج Python لـ IBM DB2.

### التثبيت
قم بتثبيت الحزم باستخدام pip:
```
pip install ibm_db
pip install ibm_db_dbi
```
ملاحظة: تتطلب هذه الحزم وجود مكتبة عميل DB2. لأنظمة Windows/Linux، قم بتنزيل وتثبيت IBM Data Server Driver Package من موقع IBM. على نظام macOS، قد يحتاج إلى إعداد إضافي. تأكد من إمكانية الوصول إلى خادم DB2 الخاص بك (على سبيل المثال، يعمل على مضيف مع بيانات الاعتماد).

### استخدام ibm_db
`ibm_db` يوفر دوال للاتصال، تنفيذ العبارات، والتعامل مع النتائج. إنه غير متوافق مع DB-API ولكنه يوفر تحكمًا أكبر.

#### الاتصال الأساسي والاستعلام
```python
import ibm_db

# تنسيق سلسلة الاتصال: DATABASE=<db_name>;HOSTNAME=<host>;PORT=<port>;PROTOCOL=TCPIP;UID=<user>;PWD=<password>;
conn_str = "DATABASE=mydb;HOSTNAME=192.168.1.100;PORT=50000;PROTOCOL=TCPIP;UID=myuser;PWD=mypassword;"

# الاتصال
conn = ibm_db.connect(conn_str, "", "")

# تنفيذ استعلام
stmt = ibm_db.exec_immediate(conn, "SELECT * FROM MYTABLE")

# جلب النتائج (واحدة تلو الأخرى)
row = ibm_db.fetch_assoc(stmt)
while row:
    print(row)  # يُرجع قاموسًا
    row = ibm_db.fetch_assoc(stmt)

# الإغلاق
ibm_db.close(conn)
```
- **الدوال الرئيسية**: `connect()`, `exec_immediate()` للاستعلامات البسيطة، `prepare()` و `execute()` للاستعلامات ذات المعاملات لمنع الاختراق.
- **العبارات المُعدة مسبقًا**: استخدم `prepare()` لتحضير استعلام و `execute()` مع المعاملات.

#### معالجة الأخطاء
```python
try:
    conn = ibm_db.connect(conn_str, "", "")
except Exception as e:
    print(f"فشل الاتصال: {str(e)}")
```

### استخدام ibm_db_dbi
`ibm_db_dbi` ينفذ معيار DB-API 2.0، مما يجعله قابلاً للتبادل مع وحدات مثل `sqlite3` أو `psycopg2`.

#### الاتصال الأساسي والاستعلام
```python
import ibm_db_dbi

# سلسلة اتصال مشابهة لـ ibm_db
conn_str = "DATABASE=mydb;HOSTNAME=192.168.1.100;PORT=50000;PROTOCOL=TCPIP;UID=myuser;PWD=mypassword;"

# الاتصال
conn = ibm_db_dbi.connect(conn_str)

# إنشاء مؤشر
cursor = conn.cursor()

# تنفيذ استعلام
cursor.execute("SELECT * FROM MYTABLE")

# جلب النتائج
rows = cursor.fetchall()  # يُرجع قائمة من tuples
for row in rows:
    print(row)

# الإغلاق
cursor.close()
conn.close()
```
- **الاستعلامات ذات المعاملات**: `cursor.execute("SELECT * FROM MYTABLE WHERE ID = ?", (id_value,))` – يستخدم ? كعناصر نائبة.
- **المعاملات**: `conn.commit()` أو `conn.rollback()`; الالتزام التلقائي معطل افتراضيًا.

### الاختلافات الرئيسية ومتى تستخدم أيهما

| الميزة              | ibm_db                          | ibm_db_dbi                      |
|----------------------|---------------------------------|---------------------------------|
| التوافق             | غير متوافق مع DB-API (منخفض المستوى) | متوافق مع DB-API 2.0           |
| سهولة الاستخدام      | يتطلب المزيد من الكود؛ وصول مباشر | بناء جملة أبسط، يشبه Python    |
| الأداء              | أسرع محتمل للعمليات المعقدة     | حمل إضافي من الغلاف            |
| الوظائف            | ميزات DB2 الكاملة               | مجموعة فرعية عبر واجهة DB-API  |
| حالة الاستخدام      | تطبيقات مخصصة تحتاج تحكمًا خامًا | عمليات CRUD القياسية           |

استخدم `ibm_db_dbi` للتعود إذا كنت معتادًا على برامج أخرى لـ DB-API. انتقل إلى `ibm_db` للحصول على ميزات متقدمة خاصة بـ DB2 مثل الإجراءات المخزنة أو العمليات المجمعة.

### أفضل الممارسات
- تعامل دائمًا مع الاستثناءات وأغلق الاتصالات في كتلة `try-finally` أو `with` لتجنب تسرب الموارد.
- لمجموعات النتائج الكبيرة، استخدم `fetchmany(size)` بدلاً من `fetchall()` للحد من استخدام الذاكرة.
- تحقق من توافق إصدار DB2؛ الحزم تدعم DB2 LUW, z/OS, iSeries.
- راجع وثائق IBM للمواضيع المتقدمة مثل اتصالات SSL أو التكامل مع CLPPlus.

لمزيد من الأمثلة، قم بزيارة [مستودع برنامج Python لـ IBM db2](https://github.com/ibmdb/python-ibmdb). إذا واجهت مشاكل، تأكد من أن نسخة DB2 الخاصة بك قيد التشغيل وأن بيانات الاعتماد صحيحة.