---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Configuration d'une application Web Spring sans Boot
translated: true
type: note
---

Compris. Puisque vous utilisez **Java 8** avec **Spring 5.2.2** (pas de Spring Boot ici, juste Spring core + web), vous devrez configurer une application minimale manuellement. Voici un exemple simple montrant comment construire une applications web avec un seul contrôleur.

---

### 1. Ajouter les Dépendances Requises

Vous avez déjà `spring-context`, `spring-web`, et `spring-core`. Pour traiter les requêtes, vous avez aussi besoin de `spring-webmvc` :

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>5.2.2.RELEASE</version>
</dependency>
```

---

### 2. Créer un Contrôleur

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

* `@Controller` indique à Spring qu'il s'agit d'un contrôleur web.
* `@RequestMapping("/hello")` mappe vers `http://localhost:8080/hello`.
* `@ResponseBody` fait qu'il retourne du texte brut (pas une JSP).

---

### 3. Définir la Configuration Spring

Puisque nous n'utilisons pas Spring Boot, nous devons tout configurer manuellement.

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

Ceci active Spring MVC et scanne votre package pour trouver les contrôleurs.

---

### 4. Configurer `web.xml` (pour conteneur de servlets Tomcat)

Si vous empaquetez en WAR :

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

Ceci configure le `DispatcherServlet` et charge votre `AppConfig`.

---

### 5. Exécuter l'Application

* Empaquetez en WAR et déployez sur Tomcat (ou Jetty).
* Démarrez Tomcat et visitez :

  ```
  http://localhost:8080/votre-app/hello
  ```
* Vous devriez voir :

  ```
  Hello, Spring Web!
  ```

---

👉 Question pour vous : souhaitez-vous que cette application s'exécute dans **Tomcat (déploiement WAR)**, ou préférez-vous un **lanceur `main()` autonome** (serveur embarqué, comme Spring Boot mais minimal) ? Je peux montrer les deux méthodes selon votre configuration.