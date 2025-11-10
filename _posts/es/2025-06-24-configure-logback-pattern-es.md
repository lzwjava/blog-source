---
audio: false
generated: true
lang: es
layout: post
title: Configuración de Logback para Formato de Registro Personalizado
translated: true
type: note
---

Para lograr el formato de registro que proporcionaste, necesitas configurar tu archivo `logback.xml`. La clave es usar un `PatternLayout` dentro de tu appender y establecer correctamente la propiedad `pattern`.

Aquí tienes un desglose de los componentes en tu formato de registro deseado y cómo mapearlos a los convertidores de patrones de Logback:

*   **`2025-06-15T01:37:52.452+08:00`**: Esta es la marca de tiempo. Usarás `%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX}` para esto.
    *   `yyyy-MM-dd'T'HH:mm:ss.SSS`: Fecha y hora con milisegundos.
    *   `XXX`: Desplazamiento ISO 8601 desde UTC (ej., `+08:00`).
*   **`DEBUG`**: Este es el nivel de registro. Usarás `%-5p` (alineado a la izquierda, 5 caracteres de ancho).
*   **`302244`**: Este es el ID del proceso. Logback no expone directamente el ID del proceso en sus convertidores estándar. Sin embargo, *sí* expone el **ID del hilo** (`%t` o `%thread`). Si "302244" en tu ejemplo es en realidad un ID de hilo (lo cual es muy común en los registros de aplicaciones), entonces `%thread` es lo que necesitas. Si *debe* ser el ID del proceso del sistema operativo, podrías necesitar un convertidor personalizado de Logback o una propiedad del sistema si tu entorno lo permite. Para las aplicaciones típicas de Spring Boot, esto suele ser el ID del hilo. Asumiré que es el ID del hilo para este ejemplo.
*   **`---`**: Una cadena literal.
*   **`[nio-8090-exec-1]`**: Este es el nombre del hilo. Usarás `[%thread]` o `%-40.40thread` si lo quieres de ancho fijo.
*   **`o.s.w.s.m.m.a.HttpEntityMethodProcessor`**: Este es el nombre del logger (normalmente el nombre de la clase completamente calificado). Usarás `%-40.40logger{39}` para obtener un nombre de logger truncado, alineado a la derecha, de hasta 39 caracteres.
*   **`:`**: Dos puntos literales.
*   **`Writing ["{"vnstatversion":"2.9","jsonversion":"2","interfaces":[{"name":"enp4s0","alias":"","created":{"date" (truncated)..."]`**: Este es el mensaje de registro. Usarás `%msg%n`.

Aquí tienes una configuración de ejemplo de `logback.xml` que debería producir una salida muy similar:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>

    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX} %highlight(%-5p) %thread --- [%thread] %-40.40logger{39} : %msg%n</pattern>
        </encoder>
    </appender>

    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
    </root>

    <logger name="org.springframework.web.servlet.mvc.method.annotation.HttpEntityMethodProcessor" level="DEBUG"/>
    <logger name="org.springframework.web.servlet.DispatcherServlet" level="DEBUG"/>

</configuration>
```

**Explicación del `pattern`:**

*   `%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX}`: Fecha y hora en formato ISO 8601 con milisegundos y desplazamiento de zona horaria.
*   `%highlight(%-5p)`: Esto generará el nivel de registro (ej., DEBUG, INFO) alineado a la izquierda en 5 caracteres, y si la salida es a una consola, Logback intentará colorearlo.
*   `%thread`: El nombre del hilo que registró el evento. (Si necesitas el ID del proceso, es más complejo, pero para aplicaciones Spring, el ID del hilo es usualmente lo relevante aquí).
*   `---`: Un separador de cadena literal.
*   `[%thread]`: El nombre del hilo encerrado entre corchetes.
*   `%-40.40logger{39}`: El nombre del logger (normalmente el nombre de la clase).
    *   `%-40`: Alineado a la izquierda y rellenado a 40 caracteres.
    *   `.40logger`: Trunca el nombre del logger si es más largo de 40 caracteres.
    *   `{39}`: Esto le dice a Logback que muestre como máximo 39 caracteres del nombre del logger, comenzando desde el final del nombre del paquete (ej., `o.s.w.s.m.m.a.HttpEntityMethodProcessor` podría convertirse en `o.s.w.s.m.m.a.HttpEntityMethodProcessor` si cabe, o `...HttpEntityMethodProcessor` si se trunca desde el principio). Puedes ajustar este número.
*   ` :  `: Dos puntos literales y un espacio.
*   `%msg%n`: El mensaje de registro real seguido de una nueva línea.

**Notas Importantes:**

1.  **Ubicación:** Guarda este XML como `logback.xml` en tu directorio `src/main/resources` de tu proyecto Spring Boot.
2.  **ID de Proceso vs. ID de Hilo:** Como se mencionó, los convertidores de patrones estándar de Logback no exponen directamente el ID del proceso del sistema operativo. Si `302244` *debe* ser el ID del proceso, típicamente tendrías que implementar un `PatternLayoutConverter` personalizado o establecer una propiedad del sistema al inicio que luego referencies en tu patrón de Logback. Sin embargo, para la mayoría de los registros de aplicaciones, el ID del hilo (`%thread`) es suficiente y se usa comúnmente en esta posición.
3.  **Valores Predeterminados de Spring Boot:** Spring Boot a menudo proporciona su propia configuración predeterminada de Logback si no proporcionas una. Al colocar `logback.xml` en `src/main/resources`, anulas la predeterminada.
4.  **Niveles del Logger:** Asegúrate de que los loggers específicos (como `HttpEntityMethodProcessor` y `DispatcherServlet`) estén configurados en nivel `DEBUG` si quieres ver sus mensajes DEBUG. Si el nivel raíz es `INFO`, entonces, por defecto, los mensajes DEBUG no se mostrarán a menos que establezcas explícitamente el nivel para loggers específicos.

Esta configuración debería acercarte mucho a tu formato de registro deseado.