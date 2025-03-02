---
audio: false
generated: false
lang: ar
layout: post
title: تطبيق خادم Servlets باستخدام Maven
translated: true
---

هنا دليل شامل لإنشاء وتوزيع تطبيق Servlet بسيط Java على WebSphere Liberty Profile (WLP) باستخدام Maven لبناء المشروع و Liberty Maven Plugin لتوزيعه. يخلق هذا المثال Servlet أساسي يعيد "Hello World!" عند الوصول إليه، ويبنيه إلى ملف WAR باستخدام Maven، ويوزعه إلى WLP. سنفترض أنك قمت بالفعل بتكوين WLP مع الميزة `servlet-4.0` مفعلة، حيث توفر الدعم اللازم ل Servlet.

---

## دليل خطوة بخطوة

### 1. إنشاء بنية المشروع Maven
ابدأ بتكوين بنية تطبيق ويب قياسية باستخدام Maven. يمكنك إنشاء هذه البنية يدويًا أو استخدام Maven لإنشائها.

- **بنية المجلدات:**
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

- **إنشاء مع Maven (اختياري):**
  قم بتشغيل هذا الأمر لإنشاء البنية، ثم قم بتعديلها حسب الحاجة:
  ```bash
  mvn archetype:generate -DgroupId=com.example -DartifactId=simple-servlet-app -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
  ```
  هذا يخلق بنية ويب، والتي ستعدلها في الخطوات القادمة.

### 2. كتابة كود Servlet
إنشاء ملف باسم `HelloServlet.java` في `src/main/java/com/example/` مع المحتوى التالي:

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

- **شرح:** هذا Servlet يستجيب لطلبات HTTP GET بـ "Hello World!" بنص عادي. يستخدم طريقة `doGet` البسيطة ويجنب استخدام التعليقات للتوافق مع تكوين `web.xml` الصريح.

### 3. إنشاء ملف `web.xml` الوصف التوزيع
إنشاء ملف باسم `web.xml` في `src/main/webapp/WEB-INF/` مع المحتوى التالي:

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

- **شرح:** يحدد ملف `web.xml` فئة `HelloServlet` ويخبرها إلى نمط URL `/hello`. هذا ضروري لأننا لا نستخدم تعليقات `@WebServlet`.

### 4. تكوين ملف `pom.xml` Maven
إنشاء أو تحديث `pom.xml` في `SimpleServletApp/` مع المحتوى التالي:

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

- **شرح:**
  - **المعلمات:** يحدد المشروع مع `groupId`, `artifactId`, و `version`. يتم تعيين `packaging` إلى `war` لبرنامج ويب.
  - **الخصائص:** يحدد Java 8 كنسخة المصدر والموجهة.
  - **الاعتماديات:** يتضمن API Servlet مع نطاق `provided`، حيث يوفرها WLP في وقت التشغيل.
  - **Maven WAR Plugin:** يحدد اسم ملف WAR إلى `myapp.war` باستخدام `<finalName>`.
  - **Liberty Maven Plugin:** يحدد توزيعه إلى خادم Liberty في `/opt/ibm/wlp`, اسم الخادم `myServer`, و توزيعه إلى مجلد `dropins`.

### 5. بناء المشروع
من `SimpleServletApp/`, قم ببناء ملف WAR باستخدام Maven:

```bash
mvn clean package
```

- **النتيجة:** هذا يجمع Servlet، ويغلفه مع `web.xml` إلى `target/myapp.war`, ويعده للتوزيع.

### 6. توزيعه وتشغيله على WebSphere Liberty
تأكد من أن خادم Liberty (`myServer`) قد تم تهيئته مع الميزة `servlet-4.0` مفعلة. تحقق من `server.xml`:
```xml
<featureManager>
    <feature>servlet-4.0</feature>
</featureManager>
```

قم بتوزيعه وتشغيل التطبيق باستخدام Liberty Maven plugin:

```bash
mvn liberty:run
```

- **ما يحدث:**
  - يبدأ الخادم Liberty في المقدمة (إذا لم يكن يعمل بالفعل).
  - يوزع `myapp.war` إلى مجلد `dropins` تلقائيًا.
  - يظل الخادم يعمل حتى يتم إيقافه.

- **تحقق من التوزيع:** ابحث عن رسالة سجل مثل:
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  سجلات عادة في `/opt/ibm/wlp/usr/servers/myServer/logs/console.log`.

### 7. الوصول إلى التطبيق
افتح متصفح ويب واذهب إلى:

```
http://localhost:9080/myapp/hello
```

- **الخروج المتوقع:**
  ```
  Hello World!
  ```

- **تفصيل URL:**
  - `9080`: الميناء الافتراضي لـ HTTP لـ WLP.
  - `/myapp`: الجذر السياق من اسم ملف WAR (`myapp.war`).
  - `/hello`: نمط URL من `web.xml`.

### 8. إيقاف الخادم
لأن `mvn liberty:run` يعمل الخادم في المقدمة، قم بإيقافه بالضغط على `Ctrl+C` في الواجهة.

---

## ملاحظات
- **المتطلبات الأساسية:**
  - يجب أن يكون Maven مثبتًا ومُكوّنًا على نظامك.
  - يجب أن يكون Liberty مثبتًا في `/opt/ibm/wlp`, و يجب أن يكون هناك مثال الخادم `myServer`. قم بتعديل `installDirectory` و `serverName` في `pom.xml` إذا كان إعدادك مختلفًا (مثل `/usr/local/wlp` أو `defaultServer`).
  - يجب أن تكون الميزة `servlet-4.0` مفعلة في `server.xml`.

- **توزيع بديل:**
  - لبناء وتوزيع بشكل منفصل:
    ```bash
    mvn clean package
    mvn liberty:deploy
    ```
    قم بتشغيل الخادم يدويًا إذا لزم الأمر:
    ```bash
    /opt/ibm/wlp/bin/server start myServer
    ```

- **تكوين الميناء:** إذا كان خادم Liberty يستخدم ميناء HTTP مختلفًا، تحقق من `server.xml` لـ `<httpEndpoint>` و قم بتعديل URL وفقًا لذلك.

- **جذر السياق:** قم بتغيير `<finalName>` في `pom.xml` (مثل `<finalName>app</finalName>`) لتغيير الجذر السياق إلى `/app`.

- **إصلاح الأخطاء:**
  - إذا فشل التوزيع، تحقق من `installDirectory` و `serverName` في `pom.xml`.
  - تحقق من السجلات في `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` عن الأخطاء.
  - تأكد من استخدام Java 8 أو أحدث، متوافقًا مع إعدادات `maven.compiler`.

---

## ملخص
يوضح هذا الدليل كيفية:
1. تكوين مشروع Maven مع Servlet بسيط (`HelloServlet.java`) و `web.xml`.
2. تكوين `pom.xml` مع API Servlet, Maven WAR plugin, و Liberty Maven plugin.
3. بناء التطبيق إلى `myapp.war` باستخدام `mvn clean package`.
4. توزيعه وتشغيله على WLP باستخدام `mvn liberty:run`.
5. الوصول إلى "Hello World!" في `http://localhost:9080/myapp/hello`.

يوفر هذا نهجًا مبسطًا ومُكوّنًا باستخدام Maven لتطوير وتوزيع تطبيق Servlet على WebSphere Liberty Profile.