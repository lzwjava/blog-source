---
audio: false
generated: true
lang: ar
layout: post
title: قاعدة بيانات أوراكل - حساب المستخدم
translated: true
type: note
---

يحدث خطأ `ORA-28000: The account is locked` عند محاولة الاتصال بقاعدة بيانات Oracle (على سبيل المثال، عبر برنامج تشغيل JDBC من النوع Thin) وكان حساب المستخدم الذي تحاول استخدامه مغلقًا. يحدث هذا عادةً بسبب كثرة محاولات تسجيل الدخول الفاشلة، أو القفل اليدوي من قبل المسؤول، أو سياسة انتهاء صلاحية الحساب. لحل هذه المشكلة، تحتاج إلى فتح الحساب، وإذا لزم الأمر، إعادة تعيين كلمة المرور أو التحقق من حالة الحساب. فيما يلي الخطوات لإصلاح هذه المشكلة عند الاتصال بقاعدة بيانات Oracle.

---

### خطوات إصلاح خطأ ORA-28000

#### 1. **التحقق من الخطأ**
   عندما تواجه هذا الخطأ في اتصال JDBC، قد يبدو كما يلي:
   ```
   java.sql.SQLException: ORA-28000: The account is locked
   ```
   هذا يؤكد أن المشكلة متعلقة بحساب قاعدة البيانات، وليس بتكوين JDBC نفسه (مثل إعدادات عنوان URL، أو برنامج التشغيل، أو مصدر البيانات في WebSphere).

#### 2. **تسجيل الدخول كمستخدم مميز**
   لفتح الحساب، تحتاج إلى الوصول إلى مستخدم قاعدة بيانات لديه صلاحيات إدارية (مثل `SYS`، أو `SYSTEM`، أو مستخدم لديه دور `DBA`). اتصل بقاعدة البيانات باستخدام أداة مثل SQL*Plus أو SQL Developer أو عميل JDBC:
   ```bash
   sqlplus / as sysdba
   ```
   أو
   ```bash
   sqlplus system/<password>@<service_name>
   ```
   استبدل `<password>` و `<service_name>` ببيانات الاعتماد الفعلية واسم خدمة قاعدة البيانات (مثل `ORCL`).

#### 3. **التحقق من حالة الحساب**
   قم بتشغيل استعلام SQL التالي للتحقق من حالة الحساب المغلق:
   ```sql
   SELECT username, account_status, lock_date 
   FROM dba_users 
   WHERE username = 'YOUR_USERNAME';
   ```
   - استبدل `YOUR_USERNAME` باسم المستخدم الذي تحاول الاتصال به (مثل `myuser`).
   - انظر إلى عمود `ACCOUNT_STATUS`. إذا كان يظهر `LOCKED` أو `LOCKED(TIMED)`، فهذا يعني أن الحساب مغلق.

   مثال على الناتج:
   ```
   USERNAME   ACCOUNT_STATUS   LOCK_DATE
   ---------- ---------------- -------------------
   MYUSER     LOCKED           24-MAR-25 10:00:00
   ```

#### 4. **فتح الحساب**
   لفتح الحساب، نفذ أمر SQL التالي كمستخدم مميز:
   ```sql
   ALTER USER your_username ACCOUNT UNLOCK;
   ```
   مثال:
   ```sql
   ALTER USER myuser ACCOUNT UNLOCK;
   ```

#### 5. **(اختياري) إعادة تعيين كلمة المرور**
   إذا كانت كلمة المرور قد انتهت صلاحيتها أو تشك في أنها غير صحيحة، يمكنك إعادة تعيينها أثناء ذلك:
   ```sql
   ALTER USER your_username IDENTIFIED BY new_password;
   ```
   مثال:
   ```sql
   ALTER USER myuser IDENTIFIED BY mynewpass123;
   ```
   - بعد إعادة التعيين، قم بتحديث كلمة المرور في ملف `server.xml` الخاص بـ WebSphere (أو حيثما تم تكوين مصدر بيانات JDBC) وقم بتشفيرها مرة أخرى إذا لزم الأمر (راجع سؤالك السابق لخطوات التشفير باستخدام AES).

#### 6. **تنفيذ التغييرات (إذا لزم الأمر)**
   في معظم الحالات، تأتي أوامر `ALTER USER` فعالة على الفور ولا تتطلب `COMMIT`. ومع ذلك، إذا كنت في بيئة كثيرة المعاملات، تأكد من عدم حدوث تراجع عن طريق إعادة بدء الجلسة أو قاعدة البيانات إذا لزم الأمر.

#### 7. **اختبار الاتصال**
   حاول الاتصال مرة أخرى باستخدام تطبيق JDBC الخاص بك أو عن طريق اختبار بسيط:
   ```java
   import java.sql.Connection;
   import java.sql.DriverManager;

   public class TestJDBC {
       public static void main(String[] args) throws Exception {
           String url = "jdbc:oracle:thin:@//localhost:1521/ORCL";
           String user = "myuser";
           String password = "mynewpass123";
           Connection conn = DriverManager.getConnection(url, user, password);
           System.out.println("Connection successful!");
           conn.close();
       }
   }
   ```
   - قم بتحديث `url`، `user`، و `password` لتطابق بيئتك.
   - إذا نجح هذا، قم بتحديث تكوين مصدر البيانات في WebSphere وفقًا لذلك.

#### 8. **التحقق من سياسات الملف الشخصي (لمنع الإقفال المستقبلي)**
   قد يكون الحساب قد أغلق بسبب سياسة أمان في الملف الشخصي للمستخدم (مثل `FAILED_LOGIN_ATTEMPTS` أو `PASSWORD_LOCK_TIME`). تحقق من الملف الشخصي المعين للمستخدم:
   ```sql
   SELECT profile 
   FROM dba_users 
   WHERE username = 'YOUR_USERNAME';
   ```
   ثم افحص حدود الملف الشخصي:
   ```sql
   SELECT resource_name, limit 
   FROM dba_profiles 
   WHERE profile = 'YOUR_PROFILE_NAME';
   ```
   ابحث عن:
   - `FAILED_LOGIN_ATTEMPTS`: عدد المحاولات الفاشلة قبل الإقفال (مثال: `10`).
   - `PASSWORD_LOCK_TIME`: مدة الإقفال (مثال: `1` يوم).

   لتخفيف هذه الإعدادات (إذا كان ذلك مناسبًا)، قم بتعديل الملف الشخصي:
   ```sql
   ALTER PROFILE your_profile_name LIMIT 
       FAILED_LOGIN_ATTEMPTS UNLIMITED 
       PASSWORD_LOCK_TIME UNLIMITED;
   ```
   مثال:
   ```sql
   ALTER PROFILE DEFAULT LIMIT FAILED_LOGIN_ATTEMPTS UNLIMITED;
   ```

#### 9. **إعادة تشغيل WebSphere (إذا لزم الأمر)**
   إذا كنت تستخدم WebSphere وقمت بتحديث كلمة مرور مصدر البيانات، أعد تشغيل خادم التطبيقات لضمان تفعيل التغييرات:
   - بالنسبة لـ Liberty: `./bin/server stop` ثم `./bin/server start`.
   - بالنسبة لـ WebSphere التقليدي: استخدم وحدة التحكم الإدارية أو `stopServer.sh` / `startServer.sh`.

---

### الأسباب الشائعة لخطأ ORA-28000
- **كثرة محاولات تسجيل الدخول الفاشلة**: تحقق من سجلات التطبيق أو سجلات WebSphere (مثل `SystemOut.log`) للبحث عن أخطاء اتصال سابقة.
- **قفل يدوي**: ربما قام المسؤول بإقفال الحساب عمدًا (`ALTER USER myuser ACCOUNT LOCK`).
- **حساب منتهي الصلاحية**: بعض البيئات تقفل الحسابات عند انتهاء صلاحية كلمات المرور. تحقق من `EXPIRY_DATE` في `dba_users`.

---

### نصائح لاستكشاف الأخطاء وإصلاحها
- إذا لم يكن لديك حق الوصول إلى `SYS` أو `SYSTEM`، اتصل بمسؤول قاعدة البيانات لفتح الحساب.
- تأكد من صحة عنوان URL لـ JDBC واسم المستخدم وكلمة المرور في `server.xml` قبل إعادة المحاولة.
- إذا استمرت المشكلة، تحقق من أن مستمع Oracle قيد التشغيل:
  ```bash
  lsnrctl status
  ```

أعلمني إذا واجهت أخطاء إضافية أو تحتاج إلى مساعدة في خطوة محددة!