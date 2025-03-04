---
audio: true
generated: true
lang: ar
layout: post
title: تكوين مصدر بيانات JNDI في WebSphere Liberty
translated: true
---

للتأكد من أن برنامج Java EAR يستخدم مصدر بيانات محدد في ملف `server.xml` في WebSphere Liberty، يجب عليك التحقق من أن التطبيق يتصل بمصدر بيانات عبر اسم JNDI (Java Naming and Directory Interface) يتوافق مع مصدر بيانات مكوّن في تكوين الخادم، بشكل خاص ملف `server.xml` أو أي ملفات يتضمنها. أدناه دليل خطوة بخطوة لمساعدتك على تأكيد ذلك:

### الخطوة 1: تحديد اسم JNDI المستخدم من قبل التطبيق
العمل الأول هو معرفة أي اسم JNDI يستخدمه تطبيق EAR للبحث عن مصدر بيانات. في تطبيق Java EE يتم نشره كملف EAR، يمكن تحديد ذلك في عدة أماكن:

- **وصفات التوزيع**: تحقق من وصفات توزيع التطبيق، مثل `web.xml` (للوحدات الويب) أو `ejb-jar.xml` (للوحدات EJB)، عن عنصر `<resource-ref>`. هذا العنصر يعلن عن مرجع الموارد الذي يستخدمه التطبيق للوصول إلى مصدر بيانات. على سبيل المثال:

  ```xml
  <resource-ref>
      <res-ref-name>jdbc/myDataSource</res-ref-name>
      <res-type>javax.sql.DataSource</res-type>
      <res-auth>Container</res-auth>
  </resource-ref>
  ```

  في هذا المثال، يبحث التطبيق عن مصدر البيانات باستخدام اسم JNDI `java:comp/env/jdbc/myDataSource`.

- **ملفات الارتباط**: في WebSphere Liberty، يمكن أن يكون مرجع الموارد من وصف التوزيع مرتبطًا باسم JNDI حقيقي محدد في الخادم عبر ملفات الارتباط مثل `ibm-web-bnd.xml` (للوحدات الويب) أو `ibm-ejb-jar-bnd.xml` (للوحدات EJB). ابحث عن ارتباط `<resource-ref>`، مثل:

  ```xml
  <resource-ref name="jdbc/myDataSource" binding-name="jdbc/actualDataSource"/>
  ```

  في هذا المثال، يتم Mapping مرجع التطبيق `jdbc/myDataSource` إلى اسم JNDI الخادم `jdbc/actualDataSource`.

- **كود التطبيق**: إذا كان لديك الوصول إلى كود المصدر، ابحث عن عمليات البحث JNDI أو التسميات:
  - **بحث JNDI**: ابحث عن كود مثل:

    ```java
    Context ctx = new InitialContext();
    DataSource ds = (DataSource) ctx.lookup("java:comp/env/jdbc/myDataSource");
    ```

    هذا يشير إلى اسم JNDI `java:comp/env/jdbc/myDataSource`.

  - **التسميات**: في تطبيقات Java EE الحديثة، قد يتم استخدام التسمية `@Resource`، مثل:

    ```java
    @Resource(name = "jdbc/myDataSource")
    private DataSource ds;
    ```

    هذا يشير أيضًا إلى `java:comp/env/jdbc/myDataSource`.

إذا لم يوجد ملف الارتباط، قد يكون اسم JNDI في الكود أو وصف التوزيع (مثل `jdbc/myDataSource`) يتوافق مباشرة مع الاسم المتوقع في تكوين الخادم.

### الخطوة 2: التحقق من تكوين `server.xml`
بعد تحديد اسم JNDI المستخدم من قبل التطبيق (بشكل مباشر أو عبر الارتباط)، تحقق من ملف WebSphere Liberty `server.xml` (وأي ملفات تكوين تتضمنها عن طريق عنصر `<include>`) عن تعريف مصدر بيانات متطابق. يُعرف مصدر البيانات في `server.xml` عادةً عن طريق عنصر `<dataSource>`، مثل هذا:

```xml
<dataSource id="myDataSource" jndiName="jdbc/myDataSource">
    <jdbcDriver libraryRef="myDBLib"/>
    <properties url="jdbc:mysql://localhost:3306/mydb" user="user" password="pass"/>
</dataSource>
```

- ابحث عن سمة `jndiName` (مثل `jdbc/myDataSource`).
- قارنها مع اسم JNDI المستخدم من قبل التطبيق (مثل `jdbc/myDataSource` أو الاسم المرتبط مثل `jdbc/actualDataSource`).

إذا كان اسم JNDI متطابقًا، فإن التطبيق يستخدم مصدر البيانات المحدد في `server.xml`.

### الخطوة 3: تفسير النتائج
- **تم العثور على تطابق**: إذا كان اسم JNDI المستخدم من قبل التطبيق يتطابق مع عنصر `<dataSource>` في `server.xml` (أو ملف مدمج)، فإن برنامج Java EAR يستخدم مصدر البيانات المحدد في `server.xml`.
- **لم يتم العثور على تطابق**: إذا لم يكن هناك اسم JNDI متطابق في `server.xml`، فإن التطبيق قد لا يستخدم مصدر بيانات محدد من قبل الخادم. قد يكون يخلق مصدر بيانات بنفسه بشكل برمجي (مثل استخدام سائق JDBC مباشرة مع URL واسم مستخدم وكلمة مرور)، على الرغم من أن هذا أقل شيوعًا ولا يُنصح به في بيئة مدارة مثل WebSphere Liberty.

### اعتبارات إضافية
- **ملفات التكوين المدمجة**: إذا استخدم `server.xml` عناصر `<include>` (مثل `<include location="datasources.xml"/>`)، تحقق من هذه الملفات عن تعريفات مصادر البيانات.
- **السلوك الافتراضي**: إذا لم يغير ملف الارتباط اسم JNDI، قد يتوقع التطبيق أن اسم مرجع الموارد (مثل `jdbc/myDataSource`) يتطابق مع مصدر بيانات في `server.xml`.
- **سجلات الخادم أو الأدوات**: على الرغم من أن هذا ليس جزءًا من التحقق من التكوين مباشرة، يمكنك أيضًا مراجعة سجلات الخادم أو استخدام مركز إدارة WebSphere Liberty لرؤية أي مصادر بيانات نشطة ومرتبطة بالتطبيق، على الرغم من أن هذا أكثر من التحقق في وقت التشغيل.

### الخاتمة
لتأكيد ما إذا كان برنامج Java EAR يستخدم مصدر بيانات `server.xml` في WebSphere Liberty:
1. تحديد اسم JNDI المستخدم من قبل التطبيق (عن طريق وصفات التوزيع، ملفات الارتباط، أو الكود).
2. التحقق من أن هذا اسم JNDI يتطابق مع مصدر بيانات محدد في `server.xml` أو ملفاته المدمجة.

إذا كان هناك تطابق، فإن التطبيق يعتمد على مصدر بيانات `server.xml`؛ وإلا، فإنه قد يستخدم طريقة بديلة.