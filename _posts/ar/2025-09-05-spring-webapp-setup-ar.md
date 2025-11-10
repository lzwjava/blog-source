---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إعداد تطبيق ويب الربيعي بدون بوت
translated: true
type: note
---

فهمت. بما أنك تستخدم **Java 8** مع **Spring 5.2.2** (لا يوجد Spring Boot هنا، فقط Spring الأساسي + web)، ستحتاج إلى إعداد تطبيق بسيط يدويًا. فيما يلي مثال بسيط يوضح كيفية بناء تطبيق ويب مع وحدة تحكم واحدة.

---

### 1. أضف التبعيات المطلوبة

لديك بالفعل `spring-context`، `spring-web`، و `spring-core`. لتقديم الطلبات، ستحتاج أيضًا إلى `spring-webmvc`:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>5.2.2.RELEASE</version>
</dependency>
```

---

### 2. إنشاء وحدة تحكم

```java
package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
public class HelloController {

    @ResponseBody
    @RequestMapping("/hello")
    public String hello() {
        return "Hello, Spring Web!";
    }
}
```

* `@Controller` تخبر Spring أن هذه وحدة تحكم ويب.
* `@RequestMapping("/hello")` تربط العنوان `http://localhost:8080/hello`.
* `@ResponseBody` تجعلها تُرجع نصًا عاديًا (وليست JSP).

---

### 3. تحديد تكوين Spring

بما أننا لا نستخدم Spring Boot، يجب علينا توصيل الأشياء يدويًا.

```java
package com.example.demo;

import org.springframework.context.annotation.*;
import org.springframework.web.servlet.config.annotation.*;

@Configuration
@EnableWebMvc
@ComponentScan(basePackages = "com.example.demo")
public class AppConfig implements WebMvcConfigurer {
}
```

هذا يُفعّل Spring MVC ويفحص حزمة `com.example.demo` للعثور على وحدات التحكم.

---

### 4. إعداد `web.xml` (لـ Tomcat / حاوية Servlet)

إذا كنت تقوم بالتعبئة كـ WAR:

```xml
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         version="3.1">

    <servlet>
        <servlet-name>dispatcher</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextClass</param-name>
            <param-value>org.springframework.web.context.support.AnnotationConfigWebApplicationContext</param-value>
        </init-param>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>com.example.demo.AppConfig</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>

    <servlet-mapping>
        <servlet-name>dispatcher</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>

</web-app>
```

هذا يُعدّد `DispatcherServlet` ويحمّل `AppConfig` الخاص بك.

---

### 5. تشغيل التطبيق

* عبّئ التطبيق كـ WAR ونشره على Tomcat (أو Jetty).
* ابدأ تشغيل Tomcat وقم بزيارة:

  ```
  http://localhost:8080/your-app/hello
  ```
* يجب أن ترى:

  ```
  Hello, Spring Web!
  ```

---

👉 سؤال لك: هل تريد تشغيل هذا التطبيق داخل **Tomcat (نشر WAR)**، أم تفضل **برنامج إطلاق قائم بذاته (`main()` مضمن)** (خادم مضمن، مثل Spring Boot ولكن بشكل بسيط)؟ يمكنني عرض الطريقتين حسب إعداداتك.