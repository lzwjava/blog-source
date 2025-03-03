---
audio: false
generated: true
lang: ar
layout: post
title: jdbc:mysql://localhost:3306/mydatabase
translated: true
---

لإنشاء رابط JDBC لاتصال بقاعدة بيانات DB2 بناءً على العنصر `properties.db2.jcc` في ملف `server.xml` من ملف WebSphere Liberty Profile، يجب استخدام القيم المقدمة لبعض السمة الرئيسية مثل `databaseName`، `serverName`، و `portNumber`. إليك كيفية القيام بذلك:

### صيغة رابط JDBC الأساسية لـ DB2
صيغة الرابط القياسية لجdbc باستخدام سائق JDBC من نوع 4 لـ DB2 (الذي يستخدم بشكل شائع في إعدادات ملف Liberty Profile) هي:

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

- **`jdbc:db2://`** - هذا هو معرف البروتوكول لقاعدة بيانات DB2 باستخدام السائق من النوع 4، مما يشير إلى اتصال شبكة مباشر.
- **`<serverName>`** - اسم المضيف أو عنوان IP للمخدم DB2، كما هو محدد في السمة `serverName` في `properties.db2.jcc`.
- **`<portNumber>`** - الميناء الذي يستمع إليه DB2، كما هو محدد في السمة `portNumber` (الافتراضي هو عادة `50000` إذا لم يتم تحديده).
- **`<databaseName>`** - اسم قاعدة البيانات التي تريد الاتصال بها، كما هو محدد في السمة `databaseName`.

### خطوات بناء الرابط
1. **تحديد السمة المطلوبة**: من العنصر `properties.db2.jcc` في `server.xml`، استخرج القيم لـ `serverName`، `portNumber`، و `databaseName`. هذه هي المكونات الأساسية المطلوبة للربط.
2. **تجميع الرابط**: قم بدمج هذه القيم في الصيغة أعلاه، مع التأكد من الفاصل الصحيح (`:` بين المضيف والميناء، `/` قبل اسم قاعدة البيانات).
3. **معالجة السمة الإضافية (إذا كانت موجودة)**: إذا كان `properties.db2.jcc` يحتوي على سمات إضافية (مثل `currentSchema`، `sslConnection`)، يمكن أن يتم إضافتها إلى الرابط، ولكن هذا يعتمد على طبيعتها. عادةً ما يتم تمرير السمة مثل `user` و `password` بشكل منفصل عند إنشاء الاتصال، وليس في الرابط، لأسباب أمنية.

### مثال
فرض أن ملف `server.xml` يحتوي على التكوين التالي لـ `properties.db2.jcc`:

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" user="dbuser" password="dbpass"/>
```

- `serverName="localhost"`
- `portNumber="50000"`
- `databaseName="SAMPLE"`

سيكون رابط JDBC:

```
jdbc:db2://localhost:50000/SAMPLE
```

- لا يتم تضمين `user` و `password` في الرابط؛ عادة ما يتم تقديمهما بشكل منفصل عند الحصول على اتصال عبر السائق JDBC (مثلًا، عبر `DataSource` أو `DriverManager`).

### تضمين السمة الإضافية (اختياري)
إذا كان هناك سمات إضافية محددة في `properties.db2.jcc` مثل `currentSchema` أو `sslConnection`، و إذا كنت تريد تضمينها في الرابط (على الرغم من أن بعضها قد يكون أفضل تعيينه في خواص الاتصال)، قم بإضافتها بعد اسم قاعدة البيانات مع فاصل (`:`) متبوعًا بزوجات `property=value` مفصولة بفاصلة (`;`). على سبيل المثال:

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" currentSchema="MYSCHEMA" sslConnection="true"/>
```

يمكن أن يصبح الرابط:

```
jdbc:db2://localhost:50000/SAMPLE:currentSchema=MYSCHEMA;sslConnection=true;
```

ومع ذلك:
- السمة مثل `sslConnection=true` عادة ما يتم تعيينها في كائن `Properties` أو تكوين مصدر البيانات بدلاً من الرابط.
- تحقق من وثائق السائق JDBC لـ DB2 لتأكيد أي سمات صالحة في الرابط مقابل تلك التي تتطلب تكوينًا منفصلًا.

### الإجابة النهائية
في سياق استفسارك، مع افتراض أن `properties.db2.jcc` يوفر على الأقل `databaseName`، `serverName`، و `portNumber`، يتم بناء رابط JDBC كما يلي:

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

قم بإستبدال `<serverName>`، `<portNumber>`، و `<databaseName>` بالقيم الفعلية من تكوين `properties.db2.jcc`. إذا كانت هناك سمات إضافية موجودة ومقصودة للربط، قم بإضافتها كـ `:property1=value1;property2=value2;`، ولكن عادةً ما يتم معالجة السمة مثل `user`، `password`، و `sslConnection` بشكل منفصل في إعداد الاتصال.