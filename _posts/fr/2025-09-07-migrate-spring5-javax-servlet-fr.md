---
audio: false
date: 2025-09-07
generated: true
image: false
lang: fr
layout: post
title: Migration de Spring 5 WAR vers javax.servlet
translated: true
type: note
---

Vous y êtes presque. Comme ce projet utilise Spring 5 (ère javax.\*) et est un WAR, la méthode la plus propre est : **utiliser `javax.servlet-api` 4.x**, ajouter un `web.xml` minimal, une configuration Java et un petit contrôleur.

### 0) Corriger l'API servlet (important)

Spring 5.2.x utilise `javax.servlet.*`, mais votre POM récupère **`jakarta.servlet-api:5.0.0`**. Remplacez-la par `javax` :

```xml
<!-- remplacer la dépendance jakarta par celle-ci -->
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>
```

(Gardez Jetty 9.4 — il est compatible Servlet 3.1/4.0 avec javax.)

### 1) `web.xml` (puisque vous avez défini `failOnMissingWebXml=true`)

Créez `src/main/webapp/WEB-INF/web.xml` :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                             http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

  <!-- Contexte Spring racine (services/repos si vous en ajoutez plus tard) -->
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

  <!-- DispatcherServlet pour MVC -->
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

### 2) Configuration Java

Créez deux classes de configuration.

`src/main/java/com/lzw/config/RootConfig.java` :

```java
package com.lzw.config;

import org.springframework.context.annotation.Configuration;

@Configuration
public class RootConfig {
    // Ajoutez des définitions @Bean pour les services/repositories si/vous en avez.
}
```

`src/main/java/com/lzw/config/WebConfig.java` :

```java
package com.lzw.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

@Configuration
@EnableWebMvc
@ComponentScan(basePackages = "com.lzw.web")
public class WebConfig {
    // Gardez vide pour REST uniquement. Ajoutez des résolveurs de vue/gestionnaires de ressources statiques plus tard si nécessaire.
}
```

### 3) Contrôleur Hello

`src/main/java/com/lzw/web/HelloController.java` :

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

### 4) Vérification de la structure des répertoires

* `src/main/webapp/WEB-INF/web.xml`
* `src/main/java/com/lzw/config/{RootConfig,WebConfig}.java`
* `src/main/java/com/lzw/web/HelloController.java`

### 5) Exécutez-le

Puisque vous avez déjà Jetty dans le POM :

```bash
mvn clean package
mvn jetty:run
```

Ouvrez : `http://localhost:8080/hello` → devrait afficher `Hello, Spring MVC!`.

---

#### Notes & écueils

* Si vous **devez** garder `jakarta.servlet-api:5.x`, vous auriez besoin de Spring 6 / Spring Boot 3+ (espace de noms Jakarta) et d'un conteneur servlet plus récent. Pour votre stack actuelle (Spring 5.2.2), **utilisez `javax.servlet-api:4.0.1`**.
* Parce que vous avez défini `maven-war-plugin` avec `failOnMissingWebXml=true`, `web.xml` est requis même si Spring 3.1+ peut fonctionner sans lui.
* Pour les vues (JSP/Thymeleaf) plus tard, ajoutez un résolveur de vue dans `WebConfig` ; pour du JSON pur, l'approche `@RestController` ci-dessus est suffisante.