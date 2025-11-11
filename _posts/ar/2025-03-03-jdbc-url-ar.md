---
audio: false
generated: true
lang: ar
layout: post
title: بناء عنوان JDBC
translated: true
type: note
---

لبناء عنوان JDBC للاتصال بقاعدة بيانات DB2 استنادًا إلى عنصر `properties.db2.jcc` في ملف `server.xml` لملف تعريف WebSphere Liberty، تحتاج إلى استخدام القيم المقدمة لسمات رئيسية معينة، مثل `databaseName` و `serverName` و `portNumber`. إليك كيفية القيام بذلك:

### تنسيق عنوان JDBC الأساسي لـ DB2
التنسيق القياسي لعنوان JDBC باستخدام برنامج تشغيل JDBC من النوع 4 لـ DB2 (والذي يشيع استخدامه في إعدادات Liberty Profile) هو:

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

- **`jdbc:db2://`** - هذا هو معرف البروتوكول لقاعدة بيانات DB2 باستخدام برنامج التشغيل من النوع 4، مما يشير إلى اتصال شبكة مباشر.
- **`<serverName>`** - اسم المضيف أو عنوان IP لخادم DB2، محدد بواسطة سمة `serverName` في `properties.db2.jcc`.
- **`<portNumber>`** - المنفذ الذي يستمع عليه مثيل DB2، محدد بواسطة سمة `portNumber` (القيمة الافتراضية هي عادةً `50000` إذا لم يتم التحديد).
- **`<databaseName>`** - اسم قاعدة البيانات للاتصال بها، محدد بواسطة سمة `databaseName`.

### خطوات بناء العنوان
1. **تحديد الخصائص المطلوبة**: من عنصر `properties.db2.jcc` في `server.xml`، استخرج القيم لـ `serverName` و `portNumber` و `databaseName`. هذه هي المكونات الأساسية اللازمة للعنوان.
2. **تجميع العنوان**: اجمع هذه القيم في التنسيق أعلاه، مع التأكد من وجود فواصل مناسبة (`:` بين الخادم والمنفذ، `/` قبل اسم قاعدة البيانات).
3. **معالجة الخصائص الإضافية (إذا كانت موجودة)**: إذا كان `properties.db2.jcc` يتضمن سمات أخرى (مثل `currentSchema`، `sslConnection`)، فيمكن أحيانًا إلحاقها بالعنوان، لكن هذا يعتمد على طبيعتها. عادةً، يتم تمرير خصائص مثل `user` و `password` بشكل منفصل عند إنشاء الاتصال، وليس في العنوان، لأسباب أمنية.

### مثال
لنفترض أن ملف `server.xml` الخاص بك يحتوي على تكوين `properties.db2.jcc` التالي:

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" user="dbuser" password="dbpass"/>
```

- `serverName="localhost"`
- `portNumber="50000"`
- `databaseName="SAMPLE"`

سيكون عنوان JDBC هو:

```
jdbc:db2://localhost:50000/SAMPLE
```

- لا يتم تضمين `user` و `password` في العنوان؛ يتم توفيرهما عادةً بشكل منفصل عند الحصول على اتصال عبر برنامج تشغيل JDBC (على سبيل المثال، عبر `DataSource` أو `DriverManager`).

### تضمين خصائص إضافية (اختياري)
إذا تم تحديد خصائص إضافية في `properties.db2.jcc`، مثل `currentSchema` أو `sslConnection`، وأردت تضمينها في العنوان (على الرغم من أن بعضها قد يكون من الأفضل تعيينه في خصائص الاتصال)، فقم بإلحاقها بعد اسم قاعدة البيانات مع نقطتين (`:`) متبوعتين بأزواج `property=value` مفصولة بفاصلة منقوطة. على سبيل المثال:

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" currentSchema="MYSCHEMA" sslConnection="true"/>
```

يمكن أن يصبح العنوان:

```
jdbc:db2://localhost:50000/SAMPLE:currentSchema=MYSCHEMA;sslConnection=true;
```

ومع ذلك:
- غالبًا ما يتم تعيين خصائص مثل `sslConnection=true` في كائن `Properties` أو تكوين مصدر بيانات بدلاً من العنوان.
- راجع وثائق برنامج تشغيل JDBC لـ DB2 للتأكد من الخصائص الصالحة في العنوان مقابل تلك التي تتطلب تكوينًا منفصلاً.

### الإجابة النهائية
في سياق استفسارك، بافتراض أن `properties.db2.jcc` يوفر على الأقل `databaseName` و `serverName` و `portNumber`، يتم بناء عنوان JDBC على النحو التالي:

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

استبدل `<serverName>` و `<portNumber>` و `<databaseName>` بالقيم الفعلية من تكوين `properties.db2.jcc` الخاص بك. إذا كانت هناك خصائص إضافية موجودة ومخصصة للعنوان، فقم بإلحاقها كـ `:property1=value1;property2=value2;`، ولكن عادةً، يتم التعامل مع خصائص مثل `user` و `password` و `sslConnection` بشكل منفصل في إعداد الاتصال.