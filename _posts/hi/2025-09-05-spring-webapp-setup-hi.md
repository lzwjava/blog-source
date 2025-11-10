---
audio: false
generated: true
image: false
lang: hi
layout: post
title: स्प्रिंग वेब एप्लिकेशन सेटअप बूट के बिना
translated: true
type: note
---

ठीक है। चूंकि आप **Java 8** और **Spring 5.2.2** का उपयोग कर रहे हैं (यहाँ Spring Boot नहीं, बस core Spring + web), आपको मैन्युअल रूप से एक मिनिमल एप्लिकेशन सेटअप करना होगा। नीचे एक कंट्रोलर के साथ वेब ऐप बनाने का एक सरल उदाहरण दिया गया है।

---

### 1. आवश्यक डिपेंडेंसीज जोड़ें

आपके पास पहले से ही `spring-context`, `spring-web`, और `spring-core` हैं। रिक्वेस्ट्स को सर्व करने के लिए, आपको `spring-webmvc` की भी आवश्यकता होगी:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>5.2.2.RELEASE</version>
</dependency>
```

---

### 2. एक कंट्रोलर बनाएँ

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

* `@Controller` Spring को बताता है कि यह एक वेब कंट्रोलर है।
* `@RequestMapping("/hello")` इसे `http://localhost:8080/hello` पर मैप करता है।
* `@ResponseBody` इसे प्लेन टेक्स्ट रिटर्न करवाता है (JSP नहीं)।

---

### 3. Spring कॉन्फ़िगरेशन डिफाइन करें

चूंकि हम Spring Boot का उपयोग नहीं कर रहे हैं, हमें चीजों को मैन्युअल रूप से वायर करना होगा।

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

यह Spring MVC को एनेबल करता है और कंट्रोलर्स के लिए आपके पैकेज को स्कैन करता है।

---

### 4. `web.xml` सेटअप करें (Tomcat/Servlet कंटेनर के लिए)

यदि आप WAR के रूप में पैकेज कर रहे हैं:

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

यह `DispatcherServlet` सेटअप करता है और आपकी `AppConfig` को लोड करता है।

---

### 5. ऐप रन करें

* WAR के रूप में पैकेज करें और Tomcat (या Jetty) पर डिप्लॉय करें।
* Tomcat स्टार्ट करें और विजिट करें:

  ```
  http://localhost:8080/your-app/hello
  ```
* आपको यह देखना चाहिए:

  ```
  Hello, Spring Web!
  ```

---

👉 आपके लिए प्रश्न: क्या आप चाहते हैं कि यह ऐप **Tomcat (WAR deployment)** के अंदर रन करे, या क्या आप एक **स्टैंडअलोन `main()` लॉन्चर** (एम्बेडेड सर्वर, Spring Boot की तरह लेकिन मिनिमल) पसंद करेंगे? आपके सेटअप के आधार पर मैं दोनों तरीके दिखा सकता हूँ।