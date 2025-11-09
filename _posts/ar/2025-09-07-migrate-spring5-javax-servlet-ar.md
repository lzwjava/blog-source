---
audio: false
date: 2025-09-07
generated: true
image: false
lang: ar
layout: post
title: ترحيل تطبيق Spring 5 من WAR إلى javax.servlet
translated: true
type: note
---

أنت على وشك الوصول. نظرًا لأن هذا المشروع يعتمد على Spring 5 (عصر javax.\*) وهو WAR، فإن أنظف طريقة هي: **استخدم `javax.servlet-api` 4.x**، وأضف `web.xml` بسيطًا، وتهيئة Java، ووحدة تحكم صغيرة.

### 0) إصلاح Servlet API (مهم)

Spring 5.2.x يستخدم `javax.servlet.*`، لكن الـ POM الخاص بك يسحب **`jakarta.servlet-api:5.0.0`**. استبدلها بـ `javax`:

```xml
<!-- استبدل تبعية jakarta بهذا -->
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>
```

(احتفظ بـ Jetty 9.4 — فهو متوافق مع Servlet 3.1/4.0 مع javax.)

### 1) `web.xml` (بما أنك عينت `failOnMissingWebXml=true`)

أنشئ `src/main/webapp/WEB-INF/web.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                             http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

  <!-- سياق Spring الجذري (الخدمات/Mخازن البيانات إذا أضفتها لاحقًا) -->
  <listener>
    <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
  </listener>
  <context-param>
    <param-name>contextClass</param-name>
    <param-value>org.springframework.web.context.support.AnnotationConfigWebApplicationContext</param-value>
  </context-param>
  <context-param>
    <param-name>contextConfigLocation</param-name>
    <param-value>com.lzw.config.RootConfig</param-value>
  </context-param>

  <!-- DispatcherServlet لـ MVC -->
  <servlet>
    <servlet-name>dispatcher</servlet-name>
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
    <init-param>
      <param-name>contextClass</param-name>
      <param-value>org.springframework.web.context.support.AnnotationConfigWebApplicationContext</param-value>
    </init-param>
    <init-param>
      <param-name>contextConfigLocation</param-name>
      <param-value>com.lzw.config.WebConfig</param-value>
    </init-param>
    <load-on-startup>1</load-on-startup>
  </servlet>

  <servlet-mapping>
    <servlet-name>dispatcher</servlet-name>
    <url-pattern>/</url-pattern>
  </servlet-mapping>

</web-app>
```

### 2) تهيئة Java

أنشئ فئتي تهيئة.

`src/main/java/com/lzw/config/RootConfig.java`:

```java
package com.lzw.config;

import org.springframework.context.annotation.Configuration;

@Configuration
public class RootConfig {
    // أضف تعريفات @Bean للخدمات/مخازن البيانات إذا/عندما تمتلكها.
}
```

`src/main/java/com/lzw/config/WebConfig.java`:

```java
package com.lzw.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

@Configuration
@EnableWebMvc
@ComponentScan(basePackages = "com.lzw.web")
public class WebConfig {
    // اتركها فارغة لوظيفة REST فقط. أضف محللي عرض/معالجي الموارد الثابتة لاحقًا إذا لزم الأمر.
}
```

### 3) وحدة التحكم Hello

`src/main/java/com/lzw/web/HelloController.java`:

```java
package com.lzw.web;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello, Spring MVC!";
    }
}
```

### 4) فحص سلامة تخطيط الدليل

* `src/main/webapp/WEB-INF/web.xml`
* `src/main/java/com/lzw/config/{RootConfig,WebConfig}.java`
* `src/main/java/com/lzw/web/HelloController.java`

### 5) تشغيله

بما أن لديك بالفعل Jetty في الـ POM:

```bash
mvn clean package
mvn jetty:run
```

افتح: `http://localhost:8080/hello` → يجب أن تعرض `Hello, Spring MVC!`.

---

#### ملاحظات ومزالق

* إذا كنت **مضطرًا** للاحتفاظ بـ `jakarta.servlet-api:5.x`، فستحتاج إلى Spring 6 / Spring Boot 3+ (نطاق Jakarta) وحاوية Servlet أحدث. لمكدسك الحالي (Spring 5.2.2)، **استخدم `javax.servlet-api:4.0.1`**.
* لأنك عينت `maven-war-plugin` مع `failOnMissingWebXml=true`، فإن `web.xml` مطلوب حتى though Spring 3.1+ يمكنه العمل بدونه.
* للعروض (JSP/Thymeleaf) لاحقًا، أضف محلل عرض في `WebConfig`؛ للـ JSON الخالص، نهج `@RestController` أعلاه كافٍ.