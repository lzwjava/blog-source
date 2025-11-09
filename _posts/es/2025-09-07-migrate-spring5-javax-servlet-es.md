---
audio: false
date: 2025-09-07
generated: true
image: false
lang: es
layout: post
title: Migración de WAR de Spring 5 a javax.servlet
translated: true
type: note
---

Ya casi estás ahí. Debido a que este proyecto es Spring 5 (era javax.\*) y un WAR, la forma más limpia es: **usa `javax.servlet-api` 4.x**, añade un `web.xml` mínimo, una configuración Java y un controlador pequeño.

### 0) Corrige la API de servlet (importante)

Spring 5.2.x usa `javax.servlet.*`, pero tu POM incluye **`jakarta.servlet-api:5.0.0`**. Cámbialo a `javax`:

```xml
<!-- reemplaza la dependencia jakarta con esta -->
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>
```

(Mantén Jetty 9.4 — es compatible con Servlet 3.1/4.0 usando javax.)

### 1) `web.xml` (ya que configuraste `failOnMissingWebXml=true`)

Crea `src/main/webapp/WEB-INF/web.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                             http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

  <!-- Contexto raíz de Spring (servicios/repositorios si los añades después) -->
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

  <!-- DispatcherServlet para MVC -->
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

### 2) Configuración Java

Crea dos clases de configuración.

`src/main/java/com/lzw/config/RootConfig.java`:

```java
package com.lzw.config;

import org.springframework.context.annotation.Configuration;

@Configuration
public class RootConfig {
    // Añade definiciones @Bean para servicios/repositorios si/los tienes.
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
    // Mantén vacío solo para REST. Añade resolutores de vistas/manejadores de recursos estáticos más tarde si es necesario.
}
```

### 3) Controlador Hello

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

### 4) Comprobación de la estructura de directorios

* `src/main/webapp/WEB-INF/web.xml`
* `src/main/java/com/lzw/config/{RootConfig,WebConfig}.java`
* `src/main/java/com/lzw/web/HelloController.java`

### 5) Ejecútalo

Ya que tienes Jetty en el POM:

```bash
mvn clean package
mvn jetty:run
```

Abre: `http://localhost:8080/hello` → debería mostrar `Hello, Spring MVC!`.

---

#### Notas y posibles problemas

* Si **debes** mantener `jakarta.servlet-api:5.x**, necesitarías Spring 6 / Spring Boot 3+ (espacio de nombres Jakarta) y un contenedor de servlets más nuevo. Para tu stack actual (Spring 5.2.2), **usa `javax.servlet-api:4.0.1`**.
* Debido a que configuraste `maven-war-plugin` con `failOnMissingWebXml=true`, `web.xml` es requerido aunque Spring 3.1+ pueda ejecutarse sin él.
* Para vistas (JSP/Thymeleaf) más adelante, añade un resolutor de vistas en `WebConfig`; para JSON puro, el enfoque con `@RestController` anterior es suficiente.