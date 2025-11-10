---
audio: false
generated: true
image: false
lang: es
layout: post
title: Configuración de Aplicación Web Spring Sin Boot
translated: true
type: note
---

Entendido. Como estás usando **Java 8** con **Spring 5.2.2** (sin Spring Boot aquí, solo Spring core + web), necesitarás configurar una aplicación mínima manualmente. A continuación, un ejemplo simple que muestra cómo construir una aplicación web con un controlador.

---

### 1. Agregar las Dependencias Necesarias

Ya tienes `spring-context`, `spring-web` y `spring-core`. Para atender peticiones, también necesitas `spring-webmvc`:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>5.2.2.RELEASE</version>
</dependency>
```

---

### 2. Crear un Controlador

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

* `@Controller` le indica a Spring que esta es un controlador web.
* `@RequestMapping("/hello")` se asigna a `http://localhost:8080/hello`.
* `@ResponseBody` hace que devuelva texto plano (no un JSP).

---

### 3. Definir la Configuración de Spring

Como no estamos usando Spring Boot, debemos configurar las cosas manualmente.

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

Esto habilita Spring MVC y escanea tu paquete en busca de controladores.

---

### 4. Configurar `web.xml` (para contenedor Servlet/Tomcat)

Si estás empaquetando como un WAR:

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

Esto configura el `DispatcherServlet` y carga tu `AppConfig`.

---

### 5. Ejecutar la Aplicación

* Empaqueta como un WAR y despliégalo en Tomcat (o Jetty).
* Inicia Tomcat y visita:

  ```
  http://localhost:8080/tu-app/hello
  ```
* Deberías ver:

  ```
  Hello, Spring Web!
  ```

---

👉 Pregunta para ti: ¿quieres que esta aplicación se ejecute dentro de **Tomcat (despliegue WAR)**, o preferirías un **`main()` lanzador independiente** (servidor embebido, como Spring Boot pero mínimo)? Puedo mostrar ambas formas dependiendo de tu configuración.