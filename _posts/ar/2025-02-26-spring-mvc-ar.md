---
audio: false
generated: true
lang: ar
layout: post
title: سبرينغ إم في سي
translated: true
type: note
---

لاستخدام **Spring MVC** بدون **Spring Boot**، تحتاج إلى تكوين إطار عمل Spring يدويًا، حيث أن Spring Boot يقوم عادةً بأتمتة الكثير من الإعدادات. فيما يلي دليل خطوة بخطوة لإنشاء تطبيق ويب بسيط باستخدام Spring MVC باستخدام التكوين القائم على XML. سيؤسس هذا المثال تطبيقًا أساسيًا مع وحدة تحكم واحدة تعرض رسالة "مرحبًا" على صفحة JSP.

---

## دليل خطوة بخطوة

### 1. إعداد هيكل المشروع
قم بإنشاء هيكل تطبيق ويب قياسي. يمكنك استخدام بيئة تطوير متكاملة مثل IntelliJ أو Eclipse، أو إنشاء المجلدات يدويًا. يجب أن يبدو الهيكل كالتالي:

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

- **`src/main/java`**: يحتوي على كود المصدر Java (مثل وحدات التحكم).
- **`src/main/webapp/WEB-INF`**: يحتوي على ملفات التكوين (`web.xml`، `spring-mvc-config.xml`) وعروض JSP.

### 2. إضافة التبعيات
إذا كنت تستخدم Maven، قم بتضمين التبعيات المطلوبة في ملف `pom.xml` الخاص بك. لتطبيق Spring MVC بسيط، تحتاج إلى مكتبة Spring Web MVC و Servlet API (التي يوفرها الحاوية).

قم بإنشاء أو تعديل `pom.xml` بالمحتوى التالي:

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
  - `<packaging>war</packaging>`: يضمن تعبئة المشروع كملف WAR للنشر في حاوية Servlet.
  - إذا كنت لا تستخدم Maven، قم بتنزيل Spring MVC JARs و Servlet API JARs يدويًا وإضافتها إلى classpath المشروع.

### 3. تكوين DispatcherServlet في `web.xml`
ملف `web.xml` هو واصف النشر لتطبيق الويب الخاص بك. يقوم بتكوين `DispatcherServlet`، وحدة التحكم الأمامية لـ Spring MVC، للتعامل مع الطلبات الواردة.

قم بإنشاء `src/main/webapp/WEB-INF/web.xml` بالمحتوى التالي:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

    <!-- Define the DispatcherServlet -->
    <servlet>
        <servlet-name>spring-mvc</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>/WEB-INF/spring-mvc-config.xml</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>

    <!-- Map the DispatcherServlet to handle all requests -->
    <servlet-mapping>
        <servlet-name>spring-mvc</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>
</web-app>
```

- **الشرح**:
  - `<servlet-class>`: يحدد `DispatcherServlet`، الذي يقوم بتوجيه الطلبات إلى وحدات التحكم.
  - `<init-param>`: يشير إلى ملف تكوين Spring (`spring-mvc-config.xml`).
  - `<url-pattern>/</url-pattern>`: يعين الـ servlet للتعامل مع جميع الطلبات إلى التطبيق.

### 4. إنشاء ملف تكوين Spring
قم بإنشاء `src/main/webapp/WEB-INF/spring-mvc-config.xml` لتحديد beans لـ Spring MVC، مثل وحدات التحكم وحلالل العرض.

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

    <!-- Enable component scanning for controllers -->
    <context:component-scan base-package="com.example.controllers" />

    <!-- Enable annotation-driven MVC -->
    <mvc:annotation-driven />

    <!-- Configure view resolver for JSP files -->
    <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix" value="/WEB-INF/views/" />
        <property name="suffix" value=".jsp" />
    </bean>
</beans>
```

- **الشرح**:
  - `<context:component-scan>`: يفحص الحزمة `com.example.controllers` للعثور على المكونات المشروحة (مثل `@Controller`).
  - `<mvc:annotation-driven>`: يمكّن ميزات MVC القائمة على الشرح (مثل `@GetMapping`).
  - `InternalResourceViewResolver`: يعين أسماء العروض إلى ملفات JSP في `/WEB-INF/views/` مع لاحقة `.jsp`.

### 5. إنشاء وحدة تحكم بسيطة
قم بإنشاء وحدة تحكم للتعامل مع طلبات HTTP. أضف `HomeController.java` في `src/main/java/com/example/controllers/`:

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

- **الشرح**:
  - `@Controller`: يحدد هذه الفئة كوحدة تحكم Spring MVC.
  - `@GetMapping("/")`: يعين طلبات GET لرابط الجذر (`/`) إلى طريقة `home()`.
  - `return "home"`: يُرجع اسم العرض `"home"`، والذي يحل إلى `/WEB-INF/views/home.jsp`.

### 6. إنشاء عرض JSP
قم بإنشاء ملف JSP بسيط لعرض الناتج. أضف `home.jsp` في `src/main/webapp/WEB-INF/views/`:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>مرحبًا بك في Spring MVC بدون Spring Boot</h1>
</body>
</html>
```

### 7. بناء وتعبئة التطبيق
إذا كنت تستخدم Maven، قم بتشغيل الأمر التالي من جذر المشروع لبناء ملف WAR:

```bash
mvn clean package
```

هذا يولد `SimpleSpringMVCApp-1.0-SNAPSHOT.war` في دليل `target`.

- **ملاحظة**: إذا كنت لا تستخدم Maven، قم بتجميع ملفات Java وتعبئة المشروع يدويًا في ملف WAR، مع الحفاظ على هيكل المجلدات.

### 8. نشر التطبيق
انشر ملف WAR إلى حاوية Servlet مثل Apache Tomcat:
- انسخ `SimpleSpringMVCApp-1.0-SNAPSHOT.war` إلى دليل `webapps` في تثبيت Tomcat الخاص بك.
- ابدأ تشغيل Tomcat (على سبيل المثال، شغل `startup.sh` أو `startup.bat` من دليل `bin` في Tomcat).

### 9. الوصول إلى التطبيق
افتح متصفحًا وانتقل إلى:

```
http://localhost:8080/SimpleSpringMVCApp-1.0-SNAPSHOT/
```

يجب أن ترى:
```
مرحبًا بك في Spring MVC بدون Spring Boot
```

- **ملاحظة**: مسار السياق (`/SimpleSpringMVCApp-1.0-SNAPSHOT`) يعتمد على اسم ملف WAR. إذا قمت بإعادة تسمية ملف WAR إلى `myapp.war`، يصبح الرابط `http://localhost:8080/myapp/`.

---

## الملخص
لاستخدام **Spring MVC بدون Spring Boot**:
1. **قم بإعداد مشروع ويب** بهيكل قياسي.
2. **أضف التبعيات** لـ Spring MVC و Servlet API.
3. **قم بتكوين DispatcherServlet** في `web.xml`.
4. **حدد تكوين Spring** في ملف XML (مثل `spring-mvc-config.xml`).
5. **قم بإنشاء وحدة تحكم** للتعامل مع الطلبات.
6. **أضف عرض JSP** للاستجابة.
7. **قم ببناء ونشر** ملف WAR إلى حاوية Servlet.

هذا الأسلوب يمنحك تحكمًا كاملاً في التكوين، مما يجعله طريقة رائعة لتعلم أساسيات Spring MVC!