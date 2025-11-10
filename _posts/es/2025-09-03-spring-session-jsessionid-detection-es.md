---
audio: false
generated: true
image: false
lang: es
layout: post
title: Sesión de Primavera, JSESSIONID y Detección del Servidor
translated: true
type: note
---

Dividamos esto en dos partes: cómo funciona **Spring Session/JSESSIONID** y cómo saber si Spring se está ejecutando en **Tomcat o Netty**.

---

## 1. Cómo funcionan Spring Session y `JSESSIONID`

*   **JSESSIONID** es el identificador estándar de sesión HTTP utilizado por los contenedores de servlets (Tomcat, Jetty, Undertow, etc.).
*   Cuando un cliente realiza la primera solicitud que requiere una sesión, el contenedor (o Spring Session si lo usas) genera un ID de sesión aleatorio, almacena los datos de la sesión en el servidor y envía el ID al cliente en una cabecera `Set-Cookie`.
*   El cliente incluye esta cookie `JSESSIONID` en las solicitudes posteriores, permitiendo al servidor encontrar la sesión correcta.
*   Por defecto, los datos de la sesión se almacenan **en la memoria del contenedor de servlets**. Por ejemplo:

    *   Tomcat almacena las sesiones en la memoria (a menos que configures persistencia).
    *   Si usas **Spring Session**, el almacenamiento de sesiones se puede externalizar (Redis, JDBC, Hazelcast, etc.), mientras se sigue usando la cookie `JSESSIONID` para identificar a los usuarios.
*   Spring Security y otras características de Spring dependen de este mecanismo de sesión para la autenticación y la gestión del estado.

---

## 2. Cómo saber si Spring usa Tomcat o Netty

Spring Boot puede ejecutarse con diferentes servidores integrados:

*   **Tomcat** (por defecto para `spring-boot-starter-web`)
*   **Jetty** (si intercambias las dependencias)
*   **Undertow** (contenedor de servlets alternativo)
*   **Netty** (usado por Spring WebFlux, no está basado en servlets)

### Formas de comprobarlo:

1.  **Revisa tus dependencias**

    *   Si tu `pom.xml` o `build.gradle` incluye `spring-boot-starter-web`, usa **Tomcat** por defecto.
    *   Si incluye `spring-boot-starter-webflux`, usa **Netty** por defecto.

2.  **Revisa los registros de inicio**

    *   Cuando la aplicación arranca, Spring Boot registra el servidor integrado.
    *   Ejemplo (Tomcat):

        ```
        Tomcat started on port(s): 8080 (http)
        ```
    *   Ejemplo (Netty):

        ```
        Netty started on port(s): 8080
        ```

3.  **Revisa las clases en tiempo de ejecución**

    *   En el código o mediante actuator, comprueba qué clases de servidor están cargadas.
    *   Las clases de Tomcat empiezan con `org.apache.catalina.`
    *   Las clases de Netty empiezan con `io.netty.`

---

✅ **Resumen**:

*   `JSESSIONID` es simplemente la cookie que apunta a una sesión del lado del servidor, gestionada por Tomcat (por defecto) o por Spring Session (Redis/DB).
*   Puedes saber si Spring usa **Tomcat o Netty** revisando las dependencias, los registros de inicio o las clases en tiempo de ejecución.

---

¿Quieres que también explique **cómo difiere el manejo de sesiones entre Spring MVC (Tomcat) y Spring WebFlux (Netty)**? Ahí es donde la distinción es más importante.