---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग एमवीसी
translated: true
---

**Spring MVC** को **Spring Boot** के बिना उपयोग करने के लिए, आपको Spring framework को manually configure करना होगा, क्योंकि Spring Boot typically setup का अधिकांश automation करता hai. नीचे एक step-by-step guide है जो XML-based configuration का उपयोग करके एक simple Spring MVC web application setup karne ke liye hai. Yeh example ek basic application setup karega jo ek single controller ke saath ek "Welcome" message ko ek JSP page par display karega.

---

## Step-by-Step Guide

### 1. Project Structure Setup Karna
Ek standard web application structure create karein. Aap ek IDE jaise IntelliJ ya Eclipse ka use kar sakte hain, ya manually folders create kar sakte hain. Structure yeh dikhna chahiye:

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
└── pom.xml  (agar Maven ka use kar rahe hain)
```

- **`src/main/java`**: Aapke Java source code (e.g., controllers) ko contain karta hai.
- **`src/main/webapp/WEB-INF`**: Configuration files (`web.xml`, `spring-mvc-config.xml`) aur JSP views ko contain karta hai.

### 2. Dependencies Add Karna
Agar aap Maven ka use kar rahe hain, to `pom.xml` mein required dependencies ko include karein. Ek simple Spring MVC application ke liye, aapko Spring Web MVC library aur Servlet API (container ke dwara provide kiya gaya) ki zaroorat hai.

`pom.xml` ko create ya edit karein yeh content ke saath:

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

- **Notes**:
  - `<packaging>war</packaging>`: Yeh ensure karta hai ki project ko ek WAR file ke roop mein deployment ke liye packaged kiya jaaye.
  - Agar aap Maven ka use nahi kar rahe hain, to manually Spring MVC JARs aur Servlet API JARs ko download karein aur unhe aapke project ke classpath mein add karein.

### 3. `web.xml` mein DispatcherServlet ko Configure Karna
`web.xml` file aapke web application ka deployment descriptor hai. Yeh `DispatcherServlet`, Spring MVC ka front controller, ko configure karta hai incoming requests ko handle karne ke liye.

`src/main/webapp/WEB-INF/web.xml` ko yeh content ke saath create karein:

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

- **Explanation**:
  - `<servlet-class>`: `DispatcherServlet` ko specify karta hai, jo requests ko controllers tak route karta hai.
  - `<init-param>`: Spring configuration file (`spring-mvc-config.xml`) ko point karta hai.
  - `<url-pattern>/</url-pattern>`: Servlet ko sabhi requests ko handle karne ke liye map karta hai.

### 4. Spring Configuration File Create Karna
`src/main/webapp/WEB-INF/spring-mvc-config.xml` ko create karein Spring MVC beans, jaise controllers aur view resolvers ko define karne ke liye.

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

- **Explanation**:
  - `<context:component-scan>`: `com.example.controllers` package ko scan karta hai annotated components (e.g., `@Controller`) ke liye.
  - `<mvc:annotation-driven>`: Annotation-based MVC features (e.g., `@GetMapping`) ko enable karta hai.
  - `InternalResourceViewResolver`: View names ko JSP files (`/WEB-INF/views/` mein) ke saath map karta hai ek `.jsp` suffix ke saath.

### 5. Ek Simple Controller Create Karna
Ek controller ko create karein HTTP requests ko handle karne ke liye. `HomeController.java` ko add karein `src/main/java/com/example/controllers/` mein:

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

- **Explanation**:
  - `@Controller`: Yeh class ko ek Spring MVC controller ke roop mein mark karta hai.
  - `@GetMapping("/")`: GET requests ko root URL (`/`) ko `home()` method tak map karta hai.
  - `return "home"`: View name `"home"` ko return karta hai, jo `/WEB-INF/views/home.jsp` tak resolve hota hai.

### 6. Ek JSP View Create Karna
Ek simple JSP file ko create karein output ko display karne ke liye. `home.jsp` ko add karein `src/main/webapp/WEB-INF/views/` mein:

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

### 7. Application ko Build aur Package Karna
Agar Maven ka use kar rahe hain, to project root se yeh command run karein WAR file ko build karne ke liye:

```bash
mvn clean package
```

Yeh `SimpleSpringMVCApp-1.0-SNAPSHOT.war` ko `target` directory mein generate karta hai.

- **Note**: Agar aap Maven ka use nahi kar rahe hain, to Java files ko compile karein aur project ko manually ek WAR file mein package karein, folder structure ko maintain karte hue.

### 8. Application ko Deploy Karna
WAR file ko ek servlet container jaise Apache Tomcat mein deploy karein:
- `SimpleSpringMVCApp-1.0-SNAPSHOT.war` ko aapke Tomcat installation ke `webapps` directory mein copy karein.
- Tomcat ko start karein (e.g., `startup.sh` ya `startup.bat` ko run karein Tomcat ke `bin` directory se).

### 9. Application ko Access Karna
Ek browser open karein aur navigate karein:

```
http://localhost:8080/SimpleSpringMVCApp-1.0-SNAPSHOT/
```

Aapko dekhna chahiye:
```
Welcome to Spring MVC without Spring Boot
```

- **Note**: Context path (`/SimpleSpringMVCApp-1.0-SNAPSHOT`) WAR file name par depend karta hai. Agar aap WAR ko `myapp.war` ke roop mein rename karein, to URL banega `http://localhost:8080/myapp/`.

---

## Summary
**Spring MVC ko Spring Boot ke bina use karne ke liye**:
1. **Ek web project setup karein** ek standard structure ke saath.
2. **Dependencies add karein** Spring MVC aur Servlet API ke liye.
3. **DispatcherServlet ko `web.xml` mein configure karein**.
4. **Spring configuration ko ek XML file mein define karein** (e.g., `spring-mvc-config.xml`).
5. **Ek controller create karein** requests ko handle karne ke liye.
6. **Ek JSP view add karein** response ke liye.
7. **WAR file ko build aur deploy karein** ek servlet container mein.

Yeh approach aapko configuration par poori control deta hai, isliye yeh Spring MVC fundamentals ko seekhne ka ek achha tarika hai!