---
audio: false
generated: true
lang: ar
layout: post
title: إنشاء قاعدة بيانات PostgreSQL
translated: true
type: note
---

أنت بالفعل في طرفية PostgreSQL التفاعلية (`psql`) كمستخدم `postgres`، وهذا رائع! لإنشاء قاعدة بيانات في PostgreSQL، يمكنك استخدام أمر `CREATE DATABASE`. إليك دليل خطوة بخطوة:

1. **تأكد من أنك في `psql`**:
   أنت بالفعل فيها، كما يظهر في موجه `postgres=#`.

2. **أنشئ قاعدة بيانات**:
   استخدم الأمر التالي لإنشاء قاعدة بيانات جديدة. استبدل `mydatabase` باسم قاعدة البيانات الذي تريده:

   ```sql
   CREATE DATABASE mydatabase;
   ```

   هذا ينشئ قاعدة بيانات باسم `mydatabase`.

3. **تحقق من إنشاء قاعدة البيانات**:
   اذكر جميع قواعد البيانات للتأكد:

   ```sql
   \l
   ```

   هذا سيعرض جدولاً بجميع قواعد البيانات، بما في ذلك `mydatabase`.

4. **اتصل بقاعدة البيانات الجديدة**:
   لبدء العمل في قاعدة البيانات الجديدة، اتصل بها باستخدام:

   ```sql
   \c mydatabase
   ```

   هذا يحول جلستك العملية إلى `mydatabase`.

5. **اختياري: أنشئ مستخدماً وامنحه الصلاحيات**:
   إذا كنت تريد مستخدماً محدداً لإدارة قاعدة البيانات هذه، فأنشئ واحداً وامنحه الامتيازات:

   ```sql
   CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
   GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
   ```

   استبدل `myuser` و `mypassword` باسم المستخدم وكلمة المرور اللذين تريدهما.

6. **اخرج من `psql`**:
   عند الانتهاء، اخرج باستخدام:

   ```sql
   \q
   ```

### ملاحظات:
- خطأ `Permission denied` الذي رأيته (`could not change directory to "/home/lzw/projects/lzwjava.github.io"`) حدث لأن المستخدم `postgres` ليس لديه حق الوصول إلى دليل المنزل الخاص بك. هذا لا يؤثر على إنشاء قاعدة البيانات ولكن قد يظهر عند تشغيل `psql` من دليل مقيد. يمكنك تجنب هذا بتشغيل `psql` من دليل يمكن للمستخدم `postgres` الوصول إليه أو بعدم تغيير الأدلة (على سبيل المثال، شغل `sudo -u postgres psql` من `/tmp`).
- الأمر `ls` الذي جربته في `psql` غير صالح. استخدم `\l` لسرد قواعد البيانات أو `\dt` لسرد الجداول داخل قاعدة بيانات.
- تأكد من أن خدمة PostgreSQL قيد التشغيل (`sudo systemctl start postgresql.service`)، وهو ما قمت به بالفعل.

### مثال على جلسة العمل:
```sql
postgres=# CREATE DATABASE mydatabase;
CREATE DATABASE
postgres=# \l
                                  List of databases
   Name      |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-------------+----------+----------+-------------+-------------+-----------------------
 mydatabase  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres    | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
 template1   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
(4 rows)

postgres=# \c mydatabase
You are now connected to database "mydatabase" as user "postgres".
mydatabase=# \q
```

إذا كنت بحاجة إلى مزيد من المساعدة (مثل إعداد الجداول، أو المستخدمين، أو الاتصال من تطبيق)، فأعلمني!