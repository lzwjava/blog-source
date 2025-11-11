---
audio: false
generated: true
lang: ar
layout: post
title: برنامج تشغيل أوراكل لجيه دي بي
translated: true
type: note
---

تتيح برامج تشغيل Oracle JDBC (اتصال قاعدة بيانات Java) للتطبيقات المكتوبة بلغة Java الاتصال بقواعد بيانات Oracle والتفاعل معها. دعني أوضح المكونات الرئيسية وكيفية استخدامها.

الفئة الرئيسية لاتصالات Oracle JDBC هي `oracle.jdbc.driver.OracleDriver`، على الرغم من أنه في الإصدارات الأحدث، غالبًا ما ستستخدم `oracle.jdbc.OracleDriver` (وهي الفئة الموصى بها منذ Oracle 10g).

إليك كيفية استخدام Oracle JDBC في تطبيق Java:

1. أولاً، تحتاج إلى تضمين برنامج تشغيل Oracle JDBC (عادةً ملف ojdbc.jar) في مشروعك.

2. تحميل فئة برنامج التشغيل:
```java
Class.forName("oracle.jdbc.OracleDriver");
```

3. إنشاء اتصال باستخدام عنوان URL للاتصال:
```java
String url = "jdbc:oracle:thin:@hostname:port:SID";
// أو للاتصال القائم على اسم الخدمة
// String url = "jdbc:oracle:thin:@//hostname:port/service_name";
String username = "your_username";
String password = "your_password";

Connection connection = DriverManager.getConnection(url, username, password);
```

4. إنشاء وتنفيذ البيانات:
```java
Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery("SELECT * FROM employees");

while (resultSet.next()) {
    // معالجة كل صف
    String name = resultSet.getString("name");
    System.out.println(name);
}
```

5. إغلاق الموارد دائمًا عند الانتهاء:
```java
resultSet.close();
statement.close();
connection.close();
```

يأتي برنامج تشغيل Oracle JDBC بعدة أنواع:
- برنامج التشغيل Thin: تنفيذ بلغة Java بحتة لا يتطلب تثبيت عميل Oracle
- برنامج التشغيل OCI: يستخدم Oracle Call Interface ويتطلب برنامج عميل Oracle
- برنامج تشغيل Kerberos: للمصادقة باستخدام Kerberos
- برنامج تشغيل JDBC-OCI: مزيج من JDBC و OCI

برنامج التشغيل Thin هو الأكثر استخدامًا لأنه لا يتطلب برامج إضافية لعميل Oracle على جهاز العميل.

هل تريد معلومات أكثر تحديدًا حول تجميع الاتصالات، أو البيانات الجاهزة، أو أي جوانب أخرى لاستخدام Oracle JDBC؟