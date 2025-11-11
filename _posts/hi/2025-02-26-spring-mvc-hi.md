---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग एमवीसी
translated: true
type: note
---

**Spring Boot** के बिना **Spring MVC** का उपयोग करने के लिए, आपको Spring फ्रेमवर्क को मैन्युअल रूप से कॉन्फ़िगर करना होगा, क्योंकि Spring Boot आमतौर पर अधिकांश सेटअप को स्वचालित कर देता है। नीचे XML-आधारित कॉन्फ़िगरेशन का उपयोग करके एक साधारण Spring MVC वेब एप्लिकेशन बनाने के लिए चरण-दर-चरण मार्गदर्शिका दी गई है। यह उदाहरण एक बेसिक एप्लिकेशन सेट अप करेगा जिसमें एक सिंगल कंट्रोलर होगा जो एक JSP पेज पर "Welcome" संदेश प्रदर्शित करता है।

---

## चरण-दर-चरण मार्गदर्शिका

### 1. प्रोजेक्ट संरचना सेट करें
एक मानक वेब एप्लिकेशन संरचना बनाएं। आप IntelliJ या Eclipse जैसे IDE का उपयोग कर सकते हैं, या मैन्युअल रूप से फ़ोल्डर्स बना सकते हैं। संरचना कुछ इस प्रकार दिखनी चाहिए:

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
└── pom.xml  (यदि Maven का उपयोग कर रहे हैं)
```

- **`src/main/java`**: आपका Java सोर्स कोड (जैसे, कंट्रोलर) रखता है।
- **`src/main/webapp/WEB-INF`**: कॉन्फ़िगरेशन फ़ाइलें (`web.xml`, `spring-mvc-config.xml`) और JSP व्यू रखता है।

### 2. डिपेंडेंसीज जोड़ें
यदि आप Maven का उपयोग कर रहे हैं, तो अपने `pom.xml` में आवश्यक डिपेंडेंसीज शामिल करें। एक साधारण Spring MVC एप्लिकेशन के लिए, आपको Spring Web MVC लाइब्रेरी और Servlet API (कंटेनर द्वारा प्रदान की गई) की आवश्यकता होती है।

`pom.xml` को निम्नलिखित सामग्री के साथ बनाएं या संपादित करें:

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
        <!-- Servlet API (कंटेनर द्वारा प्रदान की गई) -->
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

- **नोट्स**:
  - `<packaging>war</packaging>`: सुनिश्चित करता है कि प्रोजेक्ट एक WAR फ़ाइल के रूप में पैकेज किया जाता है ताकि इसे एक सर्वलेट कंटेनर पर डिप्लॉय किया जा सके।
  - यदि आप Maven का उपयोग नहीं कर रहे हैं, तो Spring MVC JARs और Servlet API JARs को मैन्युअल रूप से डाउनलोड करें और उन्हें अपने प्रोजेक्ट की क्लासपाथ में जोड़ें।

### 3. `web.xml` में DispatcherServlet कॉन्फ़िगर करें
`web.xml` फ़ाइल आपके वेब एप्लिकेशन के लिए डिप्लॉयमेंट डिस्क्रिप्टर है। यह आने वाले रिक्वेस्ट्स को हैंडल करने के लिए `DispatcherServlet` (Spring MVC का फ्रंट कंट्रोलर) को कॉन्फ़िगर करती है।

`src/main/webapp/WEB-INF/web.xml` को निम्नलिखित सामग्री के साथ बनाएं:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

    <!-- DispatcherServlet को परिभाषित करें -->
    <servlet>
        <servlet-name>spring-mvc</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>/WEB-INF/spring-mvc-config.xml</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>

    <!-- सभी रिक्वेस्ट्स को हैंडल करने के लिए DispatcherServlet को मैप करें -->
    <servlet-mapping>
        <servlet-name>spring-mvc</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>
</web-app>
```

- **स्पष्टीकरण**:
  - `<servlet-class>`: `DispatcherServlet` को निर्दिष्ट करता है, जो रिक्वेस्ट्स को कंट्रोलर तक रूट करता है।
  - `<init-param>`: Spring कॉन्फ़िगरेशन फ़ाइल (`spring-mvc-config.xml`) की ओर इशारा करता है।
  - `<url-pattern>/</url-pattern>`: सर्वलेट को एप्लिकेशन की सभी रिक्वेस्ट्स को हैंडल करने के लिए मैप करता है।

### 4. Spring कॉन्फ़िगरेशन फ़ाइल बनाएँ
Spring MVC बीन्स को परिभाषित करने के लिए `src/main/webapp/WEB-INF/spring-mvc-config.xml` बनाएं, जैसे कि कंट्रोलर और व्यू रिज़ॉल्वर।

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

    <!-- कंट्रोलर के लिए कंपोनेंट स्कैनिंग सक्षम करें -->
    <context:component-scan base-package="com.example.controllers" />

    <!-- एनोटेशन-ड्रिवन MVC सक्षम करें -->
    <mvc:annotation-driven />

    <!-- JSP फ़ाइलों के लिए व्यू रिज़ॉल्वर कॉन्फ़िगर करें -->
    <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix" value="/WEB-INF/views/" />
        <property name="suffix" value=".jsp" />
    </bean>
</beans>
```

- **स्पष्टीकरण**:
  - `<context:component-scan>`: `com.example.controllers` पैकेज को एनोटेटेड कंपोनेंट्स (जैसे, `@Controller`) के लिए स्कैन करता है।
  - `<mvc:annotation-driven>`: एनोटेशन-आधारित MVC फीचर्स (जैसे, `@GetMapping`) को सक्षम करता है।
  - `InternalResourceViewResolver`: व्यू नामों को `/WEB-INF/views/` में `.jsp` एक्सटेंशन वाली JSP फ़ाइलों से मैप करता है।

### 5. एक साधारण कंट्रोलर बनाएँ
HTTP रिक्वेस्ट्स को हैंडल करने के लिए एक कंट्रोलर बनाएं। `src/main/java/com/example/controllers/` में `HomeController.java` जोड़ें:

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

- **स्पष्टीकरण**:
  - `@Controller`: इस क्लास को एक Spring MVC कंट्रोलर के रूप में चिह्नित करता है।
  - `@GetMapping("/")`: रूट URL (`/`) पर GET रिक्वेस्ट्स को `home()` मेथड से मैप करता है।
  - `return "home"`: व्यू नाम `"home"` लौटाता है, जो `/WEB-INF/views/home.jsp` पर रिज़ॉल्व होता है।

### 6. एक JSP व्यू बनाएँ
आउटपुट प्रदर्शित करने के लिए एक साधारण JSP फ़ाइल बनाएं। `src/main/webapp/WEB-INF/views/` में `home.jsp` जोड़ें:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Spring MVC without Spring Boot</h1>
</body>
</html>
```

### 7. एप्लिकेशन बिल्ड और पैकेज करें
यदि Maven का उपयोग कर रहे हैं, तो WAR फ़ाइल बनाने के लिए प्रोजेक्ट रूट से निम्न कमांड चलाएं:

```bash
mvn clean package
```

यह `target` डायरेक्टरी में `SimpleSpringMVCApp-1.0-SNAPSHOT.war` जनरेट करता है।

- **नोट**: यदि Maven का उपयोग नहीं कर रहे हैं, तो Java फ़ाइलों को कंपाइल करें और फ़ोल्डर संरचना को बनाए रखते हुए प्रोजेक्ट को मैन्युअल रूप से एक WAR फ़ाइल में पैकेज करें।

### 8. एप्लिकेशन डिप्लॉय करें
WAR फ़ाइल को Apache Tomcat जैसे सर्वलेट कंटेनर पर डिप्लॉय करें:
- `SimpleSpringMVCApp-1.0-SNAPSHOT.war` को अपने Tomcat इंस्टॉलेशन की `webapps` डायरेक्टरी में कॉपी करें।
- Tomcat स्टार्ट करें (उदाहरण के लिए, Tomcat की `bin` डायरेक्टरी से `startup.sh` या `startup.bat` चलाएं)।

### 9. एप्लिकेशन एक्सेस करें
एक ब्राउज़र खोलें और निम्न URL पर नेविगेट करें:

```
http://localhost:8080/SimpleSpringMVCApp-1.0-SNAPSHOT/
```

आपको यह देखना चाहिए:
```
Welcome to Spring MVC without Spring Boot
```

- **नोट**: कॉन्टेक्स्ट पाथ (`/SimpleSpringMVCApp-1.0-SNAPSHOT`) WAR फ़ाइल के नाम पर निर्भर करता है। यदि आप WAR का नाम बदलकर `myapp.war` कर देते हैं, तो URL बन जाता है `http://localhost:8080/myapp/`।

---

## सारांश
**Spring Boot के बिना Spring MVC** का उपयोग करने के लिए:
1. **एक वेब प्रोजेक्ट सेट अप करें** जिसमें एक मानक संरचना हो।
2. Spring MVC और Servlet API के लिए **डिपेंडेंसीज जोड़ें**।
3. **`web.xml` में DispatcherServlet कॉन्फ़िगर करें**।
4. **Spring कॉन्फ़िगरेशन** एक XML फ़ाइल (जैसे, `spring-mvc-config.xml`) में **परिभाषित करें**।
5. रिक्वेस्ट्स को हैंडल करने के लिए **एक कंट्रोलर बनाएँ**।
6. प्रतिक्रिया के लिए **एक JSP व्यू जोड़ें**।
7. WAR फ़ाइल को बिल्ड करें और इसे एक सर्वलेट कंटेनर पर **डिप्लॉय करें**।

यह दृष्टिकोण आपको कॉन्फ़िगरेशन पर पूर्ण नियंत्रण देता है, जिससे Spring MVC के मूल सिद्धांतों को सीखने का यह एक शानदार तरीका बन जाता है!