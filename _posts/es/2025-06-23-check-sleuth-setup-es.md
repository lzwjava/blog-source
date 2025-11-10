---
audio: false
generated: true
lang: es
layout: post
title: Solución de problemas de `traceId` y `spanId` vacíos en registros
translated: true
type: note
---

El `traceId` y `spanId` están vacíos en tus líneas de log `[blog-server,,]` probablemente debido a una de las siguientes razones:

  * **Dependencia de Sleuth Faltante o Incorrecta:** Asegúrate de que la dependencia `spring-cloud-starter-sleuth` esté correctamente agregada en el `pom.xml` (para Maven) o `build.gradle` (para Gradle) de tu proyecto, y que estés usando versiones compatibles de Spring Boot y Spring Cloud. Sin esta dependencia, la auto-configuración de Spring Cloud Sleuth no se activará.

    ```xml
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-sleuth</artifactId>
    </dependency>
    ```

  * **Patrón de Logging Personalizado:** Si has definido un patrón de logging personalizado (por ejemplo, en `logback-spring.xml` o `application.properties`), debes incluir explícitamente los marcadores de posición para el `traceId` y `spanId`. Si estos marcadores de posición faltan, los IDs no aparecerán en tus logs incluso si Sleuth está activo.

    Para Logback, asegúrate de que tu patrón incluya `%X{traceId}` y `%X{spanId}`:

    ```xml
    <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level [${spring.application.name:-},%X{traceId:-},%X{spanId:-}] %thread %logger{36} - %msg%n</pattern>
    ```

  * **Sin Contexto de Trace/Span Activo:** Aunque Sleuth instrumenta automáticamente muchos componentes de Spring (como `DispatcherServlet` para peticiones HTTP), es posible que estos mensajes de log específicos se generen en un contexto donde ningún trace o span ha sido iniciado o propagado todavía. Por ejemplo, algunos logs muy tempranos durante el inicio de la aplicación o logs de hilos no gestionados por la propagación de contexto de Sleuth podrían no tener estos IDs. Sin embargo, para logs durante el procesamiento activo de peticiones HTTP como `HttpEntityMethodProcessor` y `DispatcherServlet` completando una petición, esto es menos común si Sleuth está configurado correctamente.

Para solucionar el problema, primero verifica tus dependencias y la configuración de logging. Si esos aspectos son correctos, asegúrate de que las peticiones realmente estén llegando a tu aplicación y siendo procesadas por el `DispatcherServlet` de Spring MVC, lo cual debería activar la instrumentación de Sleuth.