---
audio: false
date: 2025-09-07
generated: true
image: false
lang: de
layout: post
title: Migration von Spring 5 WAR zu javax.servlet
translated: true
type: note
---

Du bist fast am Ziel. Da es sich bei diesem Projekt um Spring 5 (javax.\*-Ära) und ein WAR handelt, ist der sauberste Weg: **verwende `javax.servlet-api` 4.x**, füge eine minimale `web.xml` hinzu, eine Java-Konfiguration und einen kleinen Controller.

### 0) Korrigiere die Servlet-API (wichtig)

Spring 5.2.x verwendet `javax.servlet.*`, aber deine POM zieht **`jakarta.servlet-api:5.0.0`** ein. Tausche sie gegen `javax` aus:

```xml
<!-- Ersetze die jakarta-Abhängigkeit durch diese -->
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>
```

(Behalte Jetty 9.4 — es ist Servlet 3.1/4.0-freundlich mit javax.)

### 1) `web.xml` (da du `failOnMissingWebXml=true` gesetzt hast)

Erstelle `src/main/webapp/WEB-INF/web.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                             http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

  <!-- Root Spring context (services/repos if you add them later) -->
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

  <!-- DispatcherServlet for MVC -->
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

### 2) Java-Konfiguration

Erstelle zwei Konfigurationsklassen.

`src/main/java/com/lzw/config/RootConfig.java`:

```java
package com.lzw.config;

import org.springframework.context.annotation.Configuration;

@Configuration
public class RootConfig {
    // Add @Bean definitions for services/repositories if/when you have them.
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
    // Keep empty for REST-only. Add view resolvers/static resource handlers later if needed.
}
```

### 3) Hallo-Controller

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

### 4) Verzeichnisstruktur-Check

* `src/main/webapp/WEB-INF/web.xml`
* `src/main/java/com/lzw/config/{RootConfig,WebConfig}.java`
* `src/main/java/com/lzw/web/HelloController.java`

### 5) Führe es aus

Da du Jetty bereits in der POM hast:

```bash
mvn clean package
mvn jetty:run
```

Öffne: `http://localhost:8080/hello` → sollte `Hello, Spring MVC!` anzeigen.

---

#### Hinweise & Fallstricke

* Wenn du **unbedingt** `jakarta.servlet-api:5.x` behalten musst, bräuchtest du Spring 6 / Spring Boot 3+ (Jakarta-Namespace) und einen neueren Servlet-Container. Für deinen aktuellen Stack (Spring 5.2.2) **verwende `javax.servlet-api:4.0.1`**.
* Da du `maven-war-plugin` mit `failOnMissingWebXml=true` gesetzt hast, ist `web.xml` erforderlich, obwohl Spring 3.1+ auch ohne laufen kann.
* Für Views (JSP/Thymeleaf) später, füge einen View Resolver in `WebConfig` hinzu; für reinen JSON ist der `@RestController`-Ansatz oben ausreichend.