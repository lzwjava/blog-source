---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hi
layout: post
title: स्प्रिंग 5 WAR का जावाक्स सर्वलेट में स्थानांतरण
translated: true
type: note
---

आप लगभग पहुंच गए हैं। क्योंकि यह प्रोजेक्ट Spring 5 (javax.* युग) और एक WAR है, सबसे साफ-सुथरा तरीका है: **`javax.servlet-api` 4.x का उपयोग करें**, एक न्यूनतम `web.xml` जोड़ें, एक Java कॉन्फ़िगरेशन, और एक छोटा सा कंट्रोलर।

### 0) Servlet API को ठीक करें (महत्वपूर्ण)

Spring 5.2.x `javax.servlet.*` का उपयोग करता है, लेकिन आपका POM **`jakarta.servlet-api:5.0.0`** खींच रहा है। इसे `javax` से बदलें:

```xml
<!-- jakarta डिपेंडेंसी को इससे बदलें -->
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>
```

(Jetty 9.4 रखें — यह javax के साथ Servlet 3.1/4.0 अनुकूल है।)

### 1) `web.xml` (चूंकि आपने `failOnMissingWebXml=true` सेट किया है)

`src/main/webapp/WEB-INF/web.xml` बनाएं:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                             http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

  <!-- रूट Spring कॉन्टेक्स्ट (सर्विसेज/रिपोजिटरीज अगर आप बाद में जोड़ते हैं) -->
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

  <!-- MVC के लिए DispatcherServlet -->
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

### 2) Java कॉन्फ़िगरेशन

दो कॉन्फ़िगरेशन क्लासेज बनाएं।

`src/main/java/com/lzw/config/RootConfig.java`:

```java
package com.lzw.config;

import org.springframework.context.annotation.Configuration;

@Configuration
public class RootConfig {
    // सर्विसेज/रिपोजिटरीज के लिए @Bean डेफिनिशन जोड़ें अगर/जब आपके पास हों।
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
    // REST-ओनली के लिए खाली रखें। जरूरत पड़ने पर बाद में व्यू रिजॉल्वर/स्टैटिक रिसोर्स हैंडलर जोड़ें।
}
```

### 3) Hello कंट्रोलर

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

### 4) डायरेक्टरी लेआउट की जांच

* `src/main/webapp/WEB-INF/web.xml`
* `src/main/java/com/lzw/config/{RootConfig,WebConfig}.java`
* `src/main/java/com/lzw/web/HelloController.java`

### 5) इसे रन करें

चूंकि आपके पास पहले से ही POM में Jetty है:

```bash
mvn clean package
mvn jetty:run
```

खोलें: `http://localhost:8080/hello` → `Hello, Spring MVC!` प्रिंट होना चाहिए।

---

#### नोट्स और समस्याएं

* अगर आपको **`jakarta.servlet-api:5.x` रखना *ही* है**, तो आपको Spring 6 / Spring Boot 3+ (Jakarta नेमस्पेस) और एक नए सर्वलेट कंटेनर की जरूरत होगी। आपके मौजूदा स्टैक (Spring 5.2.2) के लिए, **`javax.servlet-api:4.0.1` का उपयोग करें**।
* क्योंकि आपने `maven-war-plugin` को `failOnMissingWebXml=true` के साथ सेट किया है, `web.xml` जरूरी है भले ही Spring 3.1+ इसके बिना चल सकता है।
* व्यूज (JSP/Thymeleaf) के लिए बाद में, `WebConfig` में एक व्यू रिजॉल्वर जोड़ें; शुद्ध JSON के लिए, ऊपर दिया गया `@RestController` तरीका काफी है।