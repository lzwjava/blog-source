---
audio: false
generated: true
lang: ar
layout: post
title: Spring MVC
translated: true
---

لاستخدام **Spring MVC** بدون **Spring Boot**، عليك أن تقم بتكوين إطار عمل Spring يدويًا، حيث أن Spring Boot يوفر تلقائيًا الكثير من الإعدادات. أدناه دليل خطوة بخطوة لإنشاء تطبيق ويب بسيط باستخدام Spring MVC باستخدام تكوين XML. ستقوم هذه المثال بتكوين تطبيق أساسي يحتوي على موجه واحد يعرض رسالة "مرحبًا" على صفحة JSP.

---

## دليل خطوة بخطوة

### 1. إعداد بنية المشروع
إنشاء بنية تطبيق ويب قياسية. يمكنك استخدام بيئة تطوير مثل IntelliJ أو Eclipse، أو إنشاء المجلدات يدويًا. يجب أن تبدو البنية كما يلي:

```
SimpleSpringMVCApp/
├── src/
│   └── main/
│       └── java/
│           └── com/
│               └── example/
│                   └── controllers/
│                       └── HomeController.java
│       └── webapp/
│           └── WEB-INF/
│               ├── web.xml
│               ├── spring-mvc-config.xml
│               └── views/
│                   └── home.jsp
└── pom.xml  (إذا كنت تستخدم Maven)
```

- **`src/main/java`**: يحتوي على كود المصدر Java (مثل الموجهات).
- **`src/main/webapp/WEB-INF`**: يحتوي على ملفات التكوين (`web.xml`, `spring-mvc-config.xml`) ومشاهدات JSP.

### 2. إضافة الاعتماديات
إذا كنت تستخدم Maven، أضف الاعتماديات المطلوبة في ملف `pom.xml`. لبرنامج Spring MVC البسيط، تحتاج إلى مكتبة Spring Web MVC وAPI Servlet (توفيرها الحاوية).

إنشاء أو تعديل `pom.xml` بالملف التالي:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>SimpleSpringMVCApp</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <dependencies>
        <!-- Spring Web MVC -->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-webmvc</artifactId>
            <version>5.3.10</version>
        </dependency>
        <!-- Servlet API (provided by the container) -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.1</version>
            </plugin>
        </plugins>
    </build>
</project>
```

- **ملاحظات**:
  - `<packaging>war</packaging>`: يضمن أن المشروع يتم تجميعه كملف WAR للتوزيع إلى حاوية Servlet.
  - إذا كنت لا تستخدم Maven، قم بتنزيل JARs Spring MVC وJARs Servlet API يدويًا وأضفهم إلى مسار تصنيف المشروع.

### 3. تكوين DispatcherServlet في `web.xml`
ملف `web.xml` هو الوصف التوزيع لتطبيقك ويب. يحدد `DispatcherServlet`، الذي هو الموجه الأمامي لـSpring MVC، لمعالجة الطلبات الواردة.

إنشاء `src/main/webapp/WEB-INF/web.xml` بالملف التالي:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

    <!-- تعريف DispatcherServlet -->
    <servlet>
        <servlet-name>spring-mvc</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>/WEB-INF/spring-mvc-config.xml</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>

    <!-- خريطة DispatcherServlet لمعالجة جميع الطلبات -->
    <servlet-mapping>
        <servlet-name>spring-mvc</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>
</web-app>
```

- **شرح**:
  - `<servlet-class>`: يحدد `DispatcherServlet`، الذي يوجه الطلبات إلى الموجهات.
  - `<init-param>`: يشير إلى ملف التكوين لـSpring (`spring-mvc-config.xml`).
  - `<url-pattern>/</url-pattern>`: يحدد servlet لمعالجة جميع الطلبات إلى التطبيق.

### 4. إنشاء ملف التكوين لـSpring
إنشاء `src/main/webapp/WEB-INF/spring-mvc-config.xml` لتحديد beans لـSpring MVC، مثل الموجهات ومحلل المشاهدات.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:mvc="http://www.springframework.org/schema/mvc"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
           http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd
           http://www.springframework.org/schema/mvc http://www.springframework.org/schema/mvc/spring-mvc.xsd">

    <!-- تمكين فحص المكونات للموجهات -->
    <context:component-scan base-package="com.example.controllers" />

    <!-- تمكين MVC القائم على التسمية -->
    <mvc:annotation-driven />

    <!-- تكوين محلل المشاهدات للملفات JSP -->
    <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix" value="/WEB-INF/views/" />
        <property name="suffix" value=".jsp" />
    </bean>
</beans>
```

- **شرح**:
  - `<context:component-scan>`: يجرى فحص حزمة `com.example.controllers` للبحث عن المكونات المسماة (مثل `@Controller`).
  - `<mvc:annotation-driven>`: يتيح ميزات MVC القائم على التسمية (مثل `@GetMapping`).
  - `InternalResourceViewResolver`: يحدد أسماء المشاهدات إلى ملفات JSP في `/WEB-INF/views/` مع إضافة `.jsp`.

### 5. إنشاء موجه بسيط
إنشاء موجه لمعالجة طلبات HTTP. أضف `HomeController.java` في `src/main/java/com/example/controllers/`:

```java
package com.example.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @GetMapping("/")
    public String home() {
        return "home";
    }
}
```

- **شرح**:
  - `@Controller`: يحدد هذا الفئة كموجه لـSpring MVC.
  - `@GetMapping("/")`: يحدد طلبات GET إلى URL الجذر (`/`) إلى طريقة `home()`.
  - `return "home"`: يعيد اسم المشاهدة `"home"`, الذي يحدد إلى `/WEB-INF/views/home.jsp`.

### 6. إنشاء مشاهدة JSP
إنشاء ملف JSP بسيط لعرض الإخراج. أضف `home.jsp` في `src/main/webapp/WEB-INF/views/`:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>مرحبًا بكم في Spring MVC بدون Spring Boot</h1>
</body>
</html>
```

### 7. بناء وتعبئة التطبيق
إذا كنت تستخدم Maven، قم بتشغيل الأمر التالي من جذر المشروع لبناء ملف WAR:

```bash
mvn clean package
```

هذا يخلق `SimpleSpringMVCApp-1.0-SNAPSHOT.war` في مجلد `target`.

- **ملاحظة**: إذا كنت لا تستخدم Maven، قم بتجميع ملفات Java وتعبئة المشروع إلى ملف WAR يدويًا، مع الحفاظ على بنية المجلدات.

### 8. نشر التطبيق
نشر ملف WAR إلى حاوية Servlet مثل Apache Tomcat:
- نسخ `SimpleSpringMVCApp-1.0-SNAPSHOT.war` إلى مجلد `webapps` من تثبيت Tomcat.
- بدء تشغيل Tomcat (مثل تشغيل `startup.sh` أو `startup.bat` من مجلد `bin` لـTomcat).

### 9. الوصول إلى التطبيق
فتح متصفح ويب وذهاب إلى:

```
http://localhost:8080/SimpleSpringMVCApp-1.0-SNAPSHOT/
```

يجب أن ترى:
```
مرحبًا بكم في Spring MVC بدون Spring Boot
```

- **ملاحظة**: مسار السياق (`/SimpleSpringMVCApp-1.0-SNAPSHOT`) يعتمد على اسم ملف WAR. إذا قمت بتغيير اسم WAR إلى `myapp.war`، يصبح URL هو `http://localhost:8080/myapp/`.

---

## ملخص
لاستخدام **Spring MVC بدون Spring Boot**:
1. **إعداد مشروع ويب** مع بنية قياسية.
2. **إضافة الاعتماديات** لـSpring MVC وAPI Servlet.
3. **تكوين DispatcherServlet** في `web.xml`.
4. **تحديد التكوين لـSpring** في ملف XML (مثل `spring-mvc-config.xml`).
5. **إنشاء موجه** لمعالجة الطلبات.
6. **إضافة مشاهدة JSP** للإجابة.
7. **بناء وتعبئة** ملف WAR إلى حاوية Servlet.

هذا النهج يمنحك التحكم الكامل على التكوين، مما يجعله طريقة جيدة لتعلم أساسيات Spring MVC!