---
audio: false
generated: true
image: false
lang: de
layout: post
title: Konfiguration einer Spring-Webanwendung ohne Boot
translated: true
type: note
---

Verstanden. Da du **Java 8** mit **Spring 5.2.2** verwendest (hier kein Spring Boot, nur Core Spring + Web), musst du eine minimale Anwendung manuell einrichten. Unten findest du ein einfaches Beispiel, das zeigt, wie man eine Web-App mit einem Controller erstellt.

---

### 1. Erforderliche Abhängigkeiten hinzufügen

Du hast bereits `spring-context`, `spring-web` und `spring-core`. Zum Bearbeiten von Anfragen benötigst du auch `spring-webmvc`:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>5.2.2.RELEASE</version>
</dependency>
```

---

### 2. Einen Controller erstellen

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

* `@Controller` teilt Spring mit, dass dies ein Web-Controller ist.
* `@RequestMapping("/hello")` weist die URL `http://localhost:8080/hello` zu.
* `@ResponseBody` bewirkt, dass Klartext zurückgegeben wird (keine JSP).

---

### 3. Spring-Konfiguration definieren

Da wir Spring Boot nicht verwenden, müssen wir die Komponenten manuell konfigurieren.

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

Dies aktiviert Spring MVC und scannt dein Paket nach Controllern.

---

### 4. `web.xml` einrichten (für Tomcat/Servlet-Container)

Falls du das Projekt als WAR packst:

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

Dies richtet den `DispatcherServlet` ein und lädt deine `AppConfig`.

---

### 5. Die App ausführen

* Packe die Anwendung als WAR und deploye sie auf Tomcat (oder Jetty).
* Starte Tomcat und rufe auf:

  ```
  http://localhost:8080/your-app/hello
  ```
* Du solltest sehen:

  ```
  Hello, Spring Web!
  ```

---

👉 Frage an dich: Soll diese App innerhalb von **Tomcat (WAR Deployment)** laufen, oder bevorzugst du einen **standalone `main()` Launcher** (eingebetteter Server, ähnlich wie Spring Boot, aber minimal)? Ich kann beide Wege zeigen, je nach deinem Setup.