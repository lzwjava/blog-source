---
audio: false
generated: true
lang: ar
layout: post
title: استخدام كلمة مرور مشفرة باستخدام AES في WebSphere Liberty
translated: true
---

لاستخدام كلمة مرور مشفرة باستخدام AES من WebSphere Liberty's `server.xml` في Squirrel SQL Client، اتبع هذه الخطوات:

---

### **1. فك تشفير كلمة المرور باستخدام أدوات WebSphere Liberty**
يجب فك تشفير كلمة المرور المشفرة (مثل `password="{aes}ABC123..."`) أولاً. يمكن أن يفعل ذلك أداة `securityUtility` من Liberty إذا كنت تمتلك الوصول إلى خزنة المفتاح المستخدمة في التشفير.

#### **أمر فك التشفير:**
```bash
# الانتقال إلى مجلد bin من Liberty
cd /path/to/wlp/bin

# تشغيل أمر فك التشفير securityUtility
./securityUtility decode \
  --server=<LibertyServerPath> \
  --key=<KeyAlias> \
  --keyPassword=<KeystorePassword> \
  --source="{aes}ABC123..."
```

استبدل:
- `<LibertyServerPath>`: مسار إلى خادم Liberty الخاص بك (مثل `usr/servers/defaultServer`).
- `<KeyAlias>`: اسم مستعار المفتاح في الخزنة (الافتراضي: `default`).
- `<KeystorePassword>`: كلمة مرور الخزنة (الافتراضي: `KeystorePass` إذا لم يتم تغييرها).
- `{aes}ABC123...`: كلمة المرور المشفرة من `server.xml`.

---

### **2. استخدام كلمة المرور المفسرة في Squirrel**
1. افتح Squirrel SQL Client.
2. انشئ مستعار اتصال جديد.
3. في خصائص الاتصال:
   - **Driver**: اختر سائق Oracle JDBC الخاص بك.
   - **URL**: استخدم URL JDBC من `server.xml` من Liberty (مثل `jdbc:oracle:thin:@//host:port/service`).
   - **Username**: اسم المستخدم من `<dataSource>` في Liberty.
   - **Password**: أدخل **كلمة المرور المفسرة** التي حصلت عليها من الخطوة 1.

---

### **ملاحظات مهمة**
- **وصول إلى الخزنة**: تحتاج إلى ملف الخزنة (`key.jks` أو `key.p12`) وكلمة مرورها. عادةً ما يوجد في مجلد `resources/security` من Liberty.
- **الأمن**: لا تخزن كلمة المرور المفسرة في نص عادي. أدخلها مباشرة في Squirrel دون حفظها في ملف.
- **مساعدة الإداري**: إذا لم تمتلك بيانات اعتماد الخزنة، اتصل بإداري Liberty لفك تشفير كلمة المرور بأمان.

---

### **طريقة بديلة (غير موصى بها)**
إذا لم يكن فك التشفير ممكنًا، قم بإعادة كلمة المرور المشفرة في `server.xml` بكلمة مرور نصية عادية (**للاختبار فقط**). أعيد تشغيل Liberty واستخدم كلمة المرور النصية في Squirrel. استرجع إلى كلمة المرور المشفرة لاحقًا.

```xml
<!-- مثال: كلمة مرور نصية عادية (تجنبها في الإنتاج) -->
<dataSource ...>
  <properties password="plaintextPassword" />
</dataSource>
```

---

بالتالي، يمكنك استخدام كلمة المرور المفسرة في Squirrel بأمان بينما تظل متوافقة مع أفضل الممارسات الأمنية.

---

لإتصال Squirrel SQL Client إلى قاعدة بيانات Oracle باستخدام التكوين المحدد في ملف `server.xml` من ملف WebSphere Liberty Profile، خاصة عندما تتضمن خصائص سائق JDBC Oracle كلمة مرور مشفرة باستخدام AES، اتبع هذه الخطوات. يتضمن العملية استخراج تفاصيل الاتصال من ملف `server.xml`، معالجة كلمة المرور المشفرة، وتكوين Squirrel SQL بشكل مناسب. أدناه دليل شامل:

### الخطوة 1: فهم التكوين في `server.xml`
في WebSphere Liberty Profile، يتم تعريف اتصالات قاعدة البيانات في ملف `server.xml` باستخدام عنصر `<dataSource>`. يحتوي هذا العنصر على خصائص مصدر البيانات، بما في ذلك تلك الخاصة بقاعدة بيانات Oracle عبر عنصر `<properties.oracle>` المضمن. قد يبدو التكوين مثل هذا:

```xml
<dataSource jndiName="jdbc/myOracleDS">
    <jdbcDriver libraryRef="OracleLib"/>
    <properties.oracle url="jdbc:oracle:thin:@//localhost:1521/orcl" user="scott" password="{aes}encrypted_password"/>
</dataSource>
<library id="OracleLib">
    <fileset dir="${server.config.dir}/lib" includes="ojdbc6.jar"/>
</library>
```

هنا:
- **`url`**: URL JDBC للاتصال إلى قاعدة بيانات Oracle (مثل `jdbc:oracle:thin:@//localhost:1521/orcl`).
- **`user`**: اسم المستخدم في قاعدة البيانات (مثل `scott`).
- **`password`**: كلمة المرور المشفرة باستخدام AES، مع إضافة `{aes}` (مثل `{aes}encrypted_password`).
- **`<jdbcDriver>`**: يشير إلى ملف JAR سائق JDBC Oracle.

لأن Squirrel SQL هو عميل مستقل ولا يمكن أن يفتح مصدر البيانات الذي يديره WebSphere (مثلًا عبر lookup JNDI)، عليك تكوينه يدويًا باستخدام نفس تفاصيل الاتصال.

### الخطوة 2: استخراج تفاصيل الاتصال من `server.xml`
ابحث عن العنصر `<dataSource>` في ملف `server.xml` الخاص بك الذي ينتمي إلى قاعدة بيانات Oracle الخاصة بك. من العنصر `<properties.oracle>`، لاحظ التالي:
- **URL JDBC**: موجود في سمة `url` (مثل `jdbc:oracle:thin:@//localhost:1521/orcl`).
- **Username**: موجود في سمة `user` (مثل `scott`).
- **كلمة المرور المشفرة**: موجود في سمة `password` (مثل `{aes}encrypted_password`).

URL JDBC يحدد كيفية الاتصال إلى قاعدة بيانات Oracle، عادةً في أحد هذه الأشكال:
- `jdbc:oracle:thin:@//hostname:port/service_name` (استخدام اسم الخدمة)
- `jdbc:oracle:thin:@hostname:port:SID` (استخدام SID)

تحقق من `server.xml` لتأكيد URL الدقيق.

### الخطوة 3: فك تشفير كلمة المرور المشفرة باستخدام AES
كلمة المرور في `server.xml` مشفرة باستخدام AES، كما يشير إلى ذلك إضافة `{aes}`. WebSphere Liberty Profile تشفير كلمات المرور لأغراض الأمن، ولكن Squirrel SQL يتطلب كلمة المرور النصية العادية لإقامة الاتصال. لفك تشفير كلمة المرور المشفرة:

1. **استخدام أداة `securityUtility` من WebSphere**:
   - هذه الأداة مدمجة مع تثبيت WebSphere Liberty الخاص بك، عادةً ما توجد في مجلد `bin` (مثل `<liberty_install_dir>/bin/`).
   - قم بتشغيل الأمر التالي في نافذة الأوامر أو شاشة الأوامر من مجلد `bin`:
     ```
     securityUtility decode --encoding=aes <encrypted_password>
     ```
     استبدل `<encrypted_password>` بالسلسلة المشفرة الفعلية من سمة `password` (كل شيء بعد `{aes}`). على سبيل المثال:
     ```
     securityUtility decode --encoding=aes encrypted_password
     ```
   - ستخرج الأداة كلمة المرور النصية العادية.

2. **البديل**:
   - إذا لم تمتلك الوصول إلى تثبيت WebSphere Liberty أو الأداة `securityUtility`، عليك الحصول على كلمة المرور النصية العادية من مدير النظام الخاص بك أو الشخص الذي قام بتكوين مصدر البيانات.

احفظ كلمة المرور المفسرة بأمان، لأنك ستحتاج إليها في Squirrel SQL.

### الخطوة 4: تكوين سائق JDBC Oracle في Squirrel SQL
Squirrel SQL يتطلب سائق JDBC Oracle للاتصال إلى قاعدة البيانات. عليك الحصول على نفس ملف JAR السائق الذي يُشير إليه في العنصر `<library>` في `server.xml` (مثل `ojdbc6.jar`).

1. **الحصول على ملف JAR السائق**:
   - ابحث عن ملف JAR سائق JDBC Oracle الذي يُشير إليه في العنصر `<fileset>` في `server.xml` (مثل `ojdbc6.jar` في `${server.config.dir}/lib`).
   - إذا لم تمتلكه، قم بتنزيل النسخة المناسبة من موقع Oracle (مثل `ojdbc6.jar` أو `ojdbc8.jar`، متوافقًا مع إصدار قاعدة البيانات الخاصة بك).

2. **إضافة السائق إلى Squirrel SQL**:
   - افتح Squirrel SQL.
   - انتقل إلى علامة التبويب **Drivers** على اليسار.
   - انقر على زر **+** لإضافة سائق جديد.
   - قم بتكوين السائق:
     - **Name**: أدخل اسمًا (مثل “Oracle JDBC Driver”).
     - **Example URL**: أدخل URL مثال (مثل `jdbc:oracle:thin:@//localhost:1521/orcl`).
     - **Class Name**: أدخل `oracle.jdbc.OracleDriver`.
     - **Extra Class Path**: انقر على **Add**، ثم ابحث عن ملف JAR سائق JDBC Oracle.
   - انقر على **OK** لحفظ السائق.

### الخطوة 5: إنشاء اتصال (مستعار) في Squirrel SQL
الآن، قم بإنشاء مستعار اتصال باستخدام التفاصيل المستخرجة:

1. **إضافة مستعار جديد**:
   - انتقل إلى علامة التبويب **Aliases** في Squirrel SQL.
   - انقر على زر **+** لإضافة مستعار جديد.
   - قم بتكوين المستعار:
     - **Name**: أدخل اسمًا للاتصال (مثل “Oracle DB via WebSphere”).
     - **Driver**: اختر سائق JDBC Oracle الذي قمت بتكوينه.
     - **URL**: أدخل URL JDBC من العنصر `<properties.oracle>` في `server.xml` (مثل `jdbc:oracle:thin:@//localhost:1521/orcl`).
     - **Username**: أدخل اسم المستخدم من `server.xml` (مثل `scott`).
     - **Password**: أدخل كلمة المرور النصية العادية المفسرة من الخطوة 3.

2. **خصائص إضافية (اختياري)**:
   - إذا كان العنصر `<properties.oracle>` في `server.xml` يحتوي على سمات إضافية (مثل `ssl="true"` أو `connectionTimeout="30000"`)، انقر على علامة التبويب **Properties** في تكوين المستعار وأضفها كعناوين مفتاح-قيمة.

3. **اختبار الاتصال**:
   - انقر على **Test Connection** لتأكيد أن Squirrel SQL يمكن أن يتصل إلى قاعدة البيانات.
   - إذا كان النجاح، انقر على **OK** لحفظ المستعار.

### URL JDBC
URL الذي يجب استخدامه في Squirrel SQL هو القيمة المحددة في سمة `url` في العنصر `<properties.oracle>` في ملف `server.xml`. على سبيل المثال:
- إذا كان `server.xml` يحتوي على `<properties.oracle url="jdbc:oracle:thin:@//localhost:1521/orcl" .../>`، فاستخدم:
  ```
  jdbc:oracle:thin:@//localhost:1521/orcl
  ```

هذه URL، مع اسم المستخدم وكلمة المرور المفسرة، تسمح لـ Squirrel SQL بالاتصال إلى قاعدة بيانات Oracle.

### ملاحظات
- **كلمة المرور المشفرة**: لا يمكنك استخدام كلمة المرور المشفرة مباشرة في Squirrel SQL؛ يجب فك تشفيرها إلى نص عادي.
- **نطاق DataSource**: العنصر `<dataSource>` في `server.xml` مصمم لأتمتة تشغيل WebSphere Liberty. Squirrel SQL، كعميل خارجي، يتطلب تكوينًا يدويًا يعكس هذه الإعدادات.
- **توافق JAR**: تأكد من أن نسخة ملف JAR سائق JDBC Oracle متوافق مع إصدار قاعدة البيانات الخاصة بك.

بالتالي، يمكنك تكوين Squirrel SQL بنجاح للاتصال إلى قاعدة بيانات Oracle باستخدام الخصائص المحددة في ملف WebSphere Liberty Profile’s `server.xml`.