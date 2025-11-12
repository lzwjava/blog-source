---
audio: false
generated: true
lang: ar
layout: post
title: تطبيق سيرفليت جافا باستخدام مافن
translated: true
type: note
---

إليك دليلًا كاملًا لإنشاء ونشر تطبيق Java Servlet بسيط على WebSphere Liberty Profile (WLP) باستخدام Maven لبناء المشروع و Liberty Maven plugin للنشر. يوضح هذا المثال إنشاء Servlet أساسي يعيد "Hello World!" عند الوصول إليه، ويبنيه في ملف WAR باستخدام Maven، وينشره على WLP. سنفترض أنك قمت بالفعل بإعداد WLP مع تمكين ميزة `servlet-4.0`، حيث توفر هذه الميزة دعم Servlet اللازم.

---

## دليل خطوة بخطوة

### 1. إنشاء هيكل مشروع Maven
ابدأ بإعداد هيكل تطبيق ويب قياسي لـ Maven. يمكنك إنشاء هذا يدويًا أو استخدام Maven لإنشائه.

- **هيكل الدليل:**
  ```
  SimpleServletApp/
  ├── pom.xml
  └── src/
      └── main/
          ├── java/
          │   └── com/
          │       └── example/
          │           └── HelloServlet.java
          └── webapp/
              └── WEB-INF/
                  └── web.xml
  ```

- **الإنشاء باستخدام Maven (اختياري):**
  قم بتشغيل هذا الأمر لإنشاء الهيكل، ثم قم بالتعديل حسب الحاجة:
  ```bash
  mvn archetype:generate -DgroupId=com.example -DartifactId=simple-servlet-app -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
  ```
  ينشئ هذا هيكل تطبيق ويب أساسي، ستقوم بتعديله في الخطوات التالية.

### 2. كتابة كود الـ Servlet
أنشئ ملفًا باسم `HelloServlet.java` في المسار `src/main/java/com/example/` بالمحتوى التالي:

```java
package com.example;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        resp.setContentType("text/plain");
        resp.getWriter().write("Hello World!");
    }
}
```

- **الشرح:** يستجيب هذا الـ Servlet لطلبات HTTP GET بعبارة "Hello World!" كنص عادي. يستخدم طريقة `doGet` بسيطة ويتجنب استخدام التعليقات التوضيحية Annotation للتكامل مع تكوين `web.xml` الصريح.

### 3. إنشاء واصف النشر `web.xml`
أنشئ ملفًا باسم `web.xml` في المسار `src/main/webapp/WEB-INF/` بالمحتوى التالي:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
    <servlet>
        <servlet-name>HelloServlet</servlet-name>
        <servlet-class>com.example.HelloServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>HelloServlet</servlet-name>
        <url-pattern>/hello</url-pattern>
    </servlet-mapping>
</web-app>
```

- **الشرح:** يحدد ملف `web.xml` فئة `HelloServlet` ويعينها لنمط عنوان URL `/hello`. هذا ضروري لأننا لا نستخدم تعليقات `@WebServlet` التوضيحية.

### 4. تكوين ملف Maven `pom.xml`
أنشئ أو حدّث ملف `pom.xml` في دليل `SimpleServletApp/` بالمحتوى التالي:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>simple-servlet-app</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <properties>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
    </properties>

    <dependencies>
        <!-- Servlet API (provided by WLP) -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Maven WAR Plugin to build the WAR file -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.1</version>
                <configuration>
                    <finalName>myapp</finalName>
                </configuration>
            </plugin>
            <!-- Liberty Maven Plugin for deployment -->
            <plugin>
                <groupId>io.openliberty.tools</groupId>
                <artifactId>liberty-maven-plugin</artifactId>
                <version>3.3.4</version>
                <configuration>
                    <installDirectory>/opt/ibm/wlp</installDirectory>
                    <serverName>myServer</serverName>
                    <appsDirectory>dropins</appsDirectory>
                    <looseApplication>false</looseApplication>
                    <stripVersion>true</stripVersion>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

- **الشرح:**
  - **الإحداثيات:** يحدد المشروع بـ `groupId`، `artifactId`، و `version`. تم تعيين `packaging` إلى `war` لتطبيق ويب.
  - **الخصائص:** يضبط الإصدار 8 من Java كإصدار المصدر والهدف.
  - **التبعيات:** تتضمن Servlet API بنطاق `provided`، حيث يتم توفيرها بواسطة WLP في وقت التشغيل.
  - **إضافة Maven WAR Plugin:** يضبط اسم ملف WAR ليكون `myapp.war` باستخدام `<finalName>`.
  - **إضافة Liberty Maven Plugin:** يضبط النشر على خادم Liberty في المسار `/opt/ibm/wlp`، باسم الخادم `myServer`، مع النشر في دليل `dropins`.

### 5. بناء المشروع
من دليل `SimpleServletApp/`، قم ببناء ملف WAR باستخدام Maven:

```bash
mvn clean package
```

- **النتيجة:** يقوم هذا بترجمة الـ Servlet، وتعبئته مع `web.xml` في `target/myapp.war`، ويجهزه للنشر.

### 6. النشر والتشغيل على WebSphere Liberty
تأكد من إعداد خادم Liberty الخاص بك (`myServer`) مع تمكين ميزة `servlet-4.0`. تحقق من ملف `server.xml` للتأكد من وجود:
```xml
<featureManager>
    <feature>servlet-4.0</feature>
</featureManager>
```

انشر وشغّل التطبيق باستخدام إضافة Liberty Maven:

```bash
mvn liberty:run
```

- **ما يحدث:**
  - يبدأ تشغيل خادم Liberty في المقدمة (إذا لم يكن قيد التشغيل بالفعل).
  - ينشر `myapp.war` تلقائيًا في دليل `dropins`.
  - يبقي الخادم قيد التشغيل حتى يتم إيقافه.

- **التحقق من النشر:** ابحث عن رسالة سجل مثل:
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  توجد السجلات عادةً في `/opt/ibm/wlp/usr/servers/myServer/logs/console.log`.

### 7. الوصول إلى التطبيق
افتح متصفحًا وانتقل إلى:

```
http://localhost:9080/myapp/hello
```

- **الناتج المتوقع:**
  ```
  Hello World!
  ```

- **تحليل عنوان URL:**
  - `9080`: منفذ HTTP الافتراضي لـ WLP.
  - `/myapp`: جذر السياق من اسم ملف WAR (`myapp.war`).
  - `/hello`: نمط عنوان URL من `web.xml`.

### 8. إيقاف الخادم
بما أن `mvn liberty:run` يشغل الخادم في المقدمة، أوقفه بالضغط على `Ctrl+C` في الطرفية.

---

## ملاحظات
- **المتطلبات الأساسية:**
  - يجب تثبيت Maven وتكوينه على نظامك.
  - يجب تثبيت Liberty في المسار `/opt/ibm/wlp`، ويجب أن تكون نسخة الخادم `myServer` موجودة. اضبط `installDirectory` و `serverName` في `pom.xml` إذا كان إعدادك مختلفًا (مثل `/usr/local/wlp` أو `defaultServer`).
  - يجب تمكين ميزة `servlet-4.0` في `server.xml`.

- **النشر البديل:**
  - للبناء والنشر بشكل منفصل:
    ```bash
    mvn clean package
    mvn liberty:deploy
    ```
    ابدأ تشغيل الخادم يدويًا إذا لزم الأمر:
    ```bash
    /opt/ibm/wlp/bin/server start myServer
    ```

- **تكوين المنفذ:** إذا كان خادم Liberty الخاص بك يستخدم منفذ HTTP مختلفًا، فتحقق من `<httpEndpoint>` في `server.xml` وضبط عنوان URL وفقًا لذلك.

- **جذر السياق:** غيّر اسم `<finalName>` في `pom.xml` (مثل `<finalName>app</finalName>`) لتغيير جذر السياق إلى `/app`.

- **استكشاف الأخطاء وإصلاحها:**
  - إذا فشل النشر، تحقق من `installDirectory` و `serverName` في `pom.xml`.
  - افحص السجلات في `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` للبحث عن أخطاء.
  - تأكد من استخدام Java 8 أو إصدار لاحق، بما يتطابق مع إعدادات `maven.compiler`.

---

## الملخص
يوضح هذا الدليل كيفية:
1. إعداد مشروع Maven مع Servlet بسيط (`HelloServlet.java`) و `web.xml`.
2. تكوين `pom.xml` مع Servlet API، وإضافة Maven WAR plugin، وإضافة Liberty Maven plugin.
3. بناء التطبيق في `myapp.war` باستخدام `mvn clean package`.
4. نشره وتشغيله على WLP باستخدام `mvn liberty:run`.
5. الوصول إلى "Hello World!" على الرابط `http://localhost:9080/myapp/hello`.

يوفر هذا نهجًا مبسطًا قائمًا على Maven لتطوير ونشر تطبيق Servlet على WebSphere Liberty Profile.

---