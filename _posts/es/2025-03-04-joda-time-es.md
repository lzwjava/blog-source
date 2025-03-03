---
audio: false
generated: true
lang: es
layout: post
title: Operaciones de Fecha y Hora en Java
translated: true
---

### Puntos Clave
- Parece probable que para usar `org.joda.time`, debas agregarlo a tu proyecto de Java e importar sus clases para operaciones de fecha y hora.
- La investigación sugiere incluir la biblioteca a través de Maven con la versión 2.13.1 o descargar el archivo JAR, luego usar clases como `DateTime` y `LocalDate`.
- La evidencia indica que Joda-Time es útil para manejar zonas horarias, sistemas de calendario y intervalos de tiempo, con ejemplos como crear objetos de fecha y modificarlos.

### ¿Qué es Joda-Time y Cómo Configurarlo?
Joda-Time es una biblioteca para manejar fechas y horas en Java, especialmente útil antes de Java 8, ofreciendo una API intuitiva para reemplazar las clases más antiguas, menos seguras para subprocesos `Date` y `Calendar`. Para usarla, primero incluye la biblioteca en tu proyecto. Si usas Maven, agrega esta dependencia a tu `pom.xml`:
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
Alternativamente, descarga el archivo JAR desde [este sitio web](https://www.joda.org/joda-time/download.html) y agrégalo a la ruta de clase de tu proyecto, como en Eclipse creando una carpeta "libs" y vinculando el JAR a través de las propiedades del proyecto.

### Ejemplos Básicos de Uso
Una vez configurado, importa clases como `org.joda.time.DateTime` o `org.joda.time.LocalDate`. Aquí hay algunos ejemplos:
- Crear una fecha y hora actuales: `DateTime now = new DateTime();`
- Acceder a campos: `int year = now.getYear(); String monthName = now.monthOfYear().getAsText();`
- Modificar: `DateTime future = now.plusDays(5);`

### Características Avanzadas
Joda-Time soporta zonas horarias (por ejemplo, `DateTimeZone.forID("America/New_York")`) y diferentes sistemas de calendario (por ejemplo, Coptic a través de `CopticChronology.getInstance()`). También maneja intervalos y duraciones, como `Interval interval = new Interval(startDt, endDt);`.

Un detalle inesperado es que Joda-Time se considera un proyecto "finalizado", con el paquete `java.time` de Java 8 recomendado para nuevos proyectos, pero sigue siendo relevante para sistemas legados o necesidades específicas.

---

### Nota de Encuesta: Guía Completa para Usar `org.joda.time`

Esta sección proporciona una exploración detallada del uso de la biblioteca `org.joda.time`, ampliando la respuesta directa con contexto adicional y profundidad técnica, adecuada para desarrolladores que buscan una comprensión exhaustiva. Incluye configuración, ejemplos de uso, características clave y recursos adicionales, asegurando una referencia completa para la implementación.

#### Introducción a Joda-Time
Joda-Time, desarrollado por joda.org, es una biblioteca ampliamente utilizada para el procesamiento de fechas y horas, especialmente antes del lanzamiento de Java 8. Aborda problemas de diseño en las clases `Date` y `Calendar` de Java, como preocupaciones de seguridad de subprocesos, utilizando clases inmutables. Antes de Java 8, la clase `Date` y `SimpleDateFormatter` no eran seguras para subprocesos, y operaciones como desfasajes de día/mes/año eran contraintuitivas (por ejemplo, días comenzando en 0, meses en 1, requiriendo `Calendar`). Joda-Time ofrece una API limpia y fluida y soporta ocho sistemas de calendario, en comparación con los dos de Java (Gregoriano y Japonés Imperial). Después de Java 8, los autores consideran Joda-Time en gran medida finalizado, recomendando la migración a `java.time` (JSR-310) para nuevos proyectos, pero sigue siendo relevante para sistemas legados o casos de uso específicos.

#### Configuración de Joda-Time
Para usar Joda-Time, primero debes incluirlo en tu proyecto de Java. La última versión hasta el 3 de marzo de 2025 es 2.13.1, asegurando estabilidad y compatibilidad con JDK 1.5 o posterior. Para usuarios de Maven, agrega la siguiente dependencia a tu `pom.xml`:
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
Esto se puede encontrar en [Maven Repository](https://mvnrepository.com/artifact/joda-time/joda-time). Para proyectos no Maven, descarga el archivo `.tar.gz` desde [este sitio web](https://www.joda.org/joda-time/download.html), extráelo y agrega el `joda-time-2.13.1.jar` a la ruta de clase de tu proyecto. Por ejemplo, en Eclipse, crea una carpeta "libs", copia el JAR y vincúlalo a través de Propiedades -> Ruta de compilación de Java -> Bibliotecas -> Agregar Jars. Prueba la configuración con `DateTime test = new DateTime();` para asegurar la funcionalidad.

#### Uso Básico y Ejemplos
Una vez incluido, importa clases de `org.joda.time`, como `DateTime`, `LocalDate`, `LocalTime` y `LocalDateTime`, todas inmutables para seguridad de subprocesos. Aquí hay ejemplos detallados:

- **Creación de Objetos de Fecha-Hora:**
  - Desde la hora actual: `DateTime now = new DateTime();` usa la zona horaria predeterminada y el calendario ISO.
  - Desde una `Date` de Java: `java.util.Date juDate = new Date(); DateTime dt = new DateTime(juDate);` para interoperabilidad.
  - Desde valores específicos: Los constructores aceptan `Long` (milisegundos), `String` (ISO8601) u otros objetos Joda-Time, por ejemplo, `DateTime dt = new DateTime(2025, 3, 3, 8, 39);`.

- **Acceso a Campos:**
  - Usa métodos getter: `int year = now.getYear(); int month = now.getMonthOfYear();` donde enero es 1 y diciembre es 12.
  - Para representación textual: `String dayName = now.dayOfWeek().getAsText();` devuelve, por ejemplo, "Lunes" para el 3 de marzo de 2025.
  - Verifica propiedades: `boolean isLeap = now.year().isLeap();` devuelve `false` para 2025.

- **Modificación de Fecha-Hora:**
  - Crea nuevas instancias con modificaciones: `DateTime newDt = now.withYear(2025);` o `DateTime future = now.plusDays(5);`.
  - Añade duraciones: `DateTime later = now.plusHours(2);` para añadir dos horas, devolviendo una nueva instancia.

Un ejemplo práctico de GeeksforGeeks ilustra el uso:
```java
import org.joda.time.DateTime;
import org.joda.time.LocalDateTime;
public class JodaTime {
    public static void main(String[] args) {
        DateTime now = new DateTime();
        System.out.println("Día Actual: " + now.dayOfWeek().getAsText());
        System.out.println("Mes Actual: " + now.monthOfYear().getAsText());
        System.out.println("Año Actual: " + now.year().getAsText());
        System.out.println("El Año Actual es Bisiesto: " + now.year().isLeap());
        LocalDateTime dt = LocalDateTime.now();
        System.out.println(dt);
    }
}
```
Para el 3 de marzo de 2025, la salida podría incluir "Día Actual: Lunes", "Mes Actual: Marzo", "Año Actual: 2025", "El Año Actual es Bisiesto: false", y una marca de tiempo como "2025-03-03T08:39:00.000".

#### Características Clave y Uso Avanzado
Joda-Time ofrece características robustas para operaciones complejas de fecha-hora, detalladas a continuación:

- **Zonas Horarias:**
  - Administradas a través de `DateTimeZone`, soportando zonas nombradas (por ejemplo, "Asia/Tokyo") y desfasajes fijos. Ejemplo:
    ```java
    DateTimeZone zone = DateTimeZone.forID("America/New_York");
    DateTime nyTime = new DateTime(zone);
    ```
  - La zona predeterminada coincide con la de JDK, pero puede ser anulada con `DateTimeZone.setDefault(zone);`. Los datos de zona horaria se actualizan manualmente varias veces al año, basados en [global-tz](https://github.com/JodaOrg/global-tz).

- **Sistemas de Calendario:**
  - Soporta siete sistemas: Budista, Cópico, Etiopio, Gregoriano, GregorianoJuliano, Islámico, Juliano, con provisión para sistemas personalizados. Ejemplo:
    ```java
    Chronology coptic = CopticChronology.getInstance();
    LocalDate copticDate = new LocalDate(coptic);
    ```
  - Predeterminado al calendario ISO, históricamente inexacto antes de 1583, pero adecuado para el uso civil moderno.

- **Intervalos, Duraciones y Períodos:**
  - `Interval`: Representa un rango de tiempo, semiabierto (inicio inclusivo, fin exclusivo), por ejemplo, `Interval interval = new Interval(startDt, endDt);`.
  - `Duration`: Tiempo exacto en milisegundos, por ejemplo, `Duration duration = new Duration(interval);`, útil para añadir a instantes.
  - `Period`: Definido en campos (años, meses, días, etc.), inexacto en milisegundos, por ejemplo, `Period period = new Period(startDt, endDt);`. Ejemplo de diferencia: Añadir 1 día en el horario de verano (por ejemplo, 2005-03-26 12:00:00) con `plus(Period.days(1))` añade 23 horas, mientras que `plus(new Duration(24L*60L*60L*1000L))` añade 24 horas, destacando el comportamiento de período frente a duración.

La guía de inicio rápido proporciona una tabla que resume las clases principales y casos de uso:
| **Aspecto**                  | **Detalles**                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| **Clases Principales de Fecha-Hora**   | Instant, DateTime, LocalDate, LocalTime, LocalDateTime (5 clases, todas inmutables)               |
| **Caso de Uso de Instant**         | Marca de tiempo de un evento, sin sistema de calendario o zona horaria                                          |
| **Caso de Uso de LocalDate**       | Fecha de nacimiento, sin hora del día necesarios                                                           |
| **Caso de Uso de LocalTime**       | Hora del día, por ejemplo, apertura/cierre de tienda, sin fecha                                               |
| **Caso de Uso de DateTime**        | Propósito general, reemplaza el Calendario de JDK, incluye información de zona horaria                          |
| **Tipos de Constructores**        | El constructor de objeto acepta: Date, Calendar, String (ISO8601), Long (milisegundos), clases Joda-Time |
| **Ejemplo de Conversión**       | `java.util.Date` a `DateTime`: `DateTime dt = new DateTime(new Date());`                      |
| **Métodos de Acceso a Campos**     | `getMonthOfYear()` (1=Enero, 12=Diciembre), `getYear()`                                        |
| **Métodos de Modificación**     | `withYear(2000)`, `plusHours(2)`                                                               |
| **Ejemplos de Métodos de Propiedades**| `monthOfYear().getAsText()`, `monthOfYear().getAsShortText(Locale.FRENCH)`, `year().isLeap()`, `dayOfMonth().roundFloorCopy()` |
| **Sistema de Calendario Predeterminado**  | Sistema de calendario ISO (calendario civil de facto, históricamente inexacto antes de 1583)              |
| **Zona Horaria Predeterminada**        | Mismo que la predeterminada de JDK, puede ser anulada                                                         |
| **Clase Chronology**         | Soporta múltiples sistemas de calendario, por ejemplo, `CopticChronology.getInstance()`                     |
| **Ejemplo de Zona Horaria**        | `DateTimeZone zone = DateTimeZone.forID("Asia/Tokyo");`, `GJChronology.getInstance(zone)`      |
| **Clase Interval**           | `Interval` - mantiene fecha-hora de inicio y fin, operaciones basadas en rango                          |
| **Clase Period**             | `Period` - mantiene período como 6 meses, 3 días, 7 horas, puede derivarse de intervalo               |
| **Clase Duration**           | `Duration` - duración exacta en milisegundos, puede derivarse de intervalo                          |
| **Ejemplo de Period vs Duration**| Añadir 1 día en horario de verano (2005-03-26 12:00:00): `plus(Period.days(1))` añade 23 horas, `plus(new Duration(24L*60L*60L*1000L))` añade 24 horas |

Un detalle interesante es la extensibilidad de los constructores de objetos, permitiendo la conversión desde `Date` o `Calendar` de JDK pasando directamente, simplificando la migración desde código legado.

#### Aprendizaje Adicional y Recursos
Para una exploración más profunda, consulta la documentación oficial en [Joda-Time User Guide](https://www.joda.org/joda-time/userguide.html), que cubre temas avanzados como formateo y análisis. La guía de inicio rápido en [Joda-Time Quick Start](https://www.joda.org/joda-time/quickstart.html) ofrece una introducción concisa. Tutoriales adicionales están disponibles en [Baeldung Joda-Time](https://www.baeldung.com/joda-time) y [GeeksforGeeks Joda-Time](https://www.geeksforgeeks.org/joda-time/), con ejemplos de código e instrucciones de configuración. La documentación de la API en [Joda-Time API Docs](https://www.joda.org/joda-time/apidocs/index.html) es útil para referencia, aunque más técnica.

#### Conclusión
Joda-Time proporciona una alternativa robusta y segura para subprocesos para operaciones de fecha y hora, con un soporte extenso para zonas horarias, sistemas de calendario y cálculos de tiempo. Aunque considerado finalizado después de Java 8, sigue siendo valioso para sistemas legados, con configuración a través de Maven o inclusión manual de JAR, y uso a través de clases inmutables como `DateTime` y `LocalDate`. Esta guía asegura que los desarrolladores tengan toda la información necesaria para la implementación, desde ejemplos básicos hasta características avanzadas, respaldadas por recursos completos.

### Citaciones Clave
- [Página Principal de Joda-Time con Información General](https://www.joda.org/joda-time/)
- [Guía de Inicio Rápido de Joda-Time para Principiantes](https://www.joda.org/joda-time/quickstart.html)
- [Tutorial de Baeldung sobre el Uso de Joda-Time](https://www.baeldung.com/joda-time)
- [Artículo de GeeksforGeeks sobre Joda-Time con Ejemplos](https://www.geeksforgeeks.org/joda-time/)
- [Guía del Usuario de Joda-Time para Referencia Detallada](https://www.joda.org/joda-time/userguide.html)
- [Página de Descarga e Instalación de Joda-Time](https://www.joda.org/joda-time/download.html)
- [Repositorio Maven para Dependencia de Joda-Time](https://mvnrepository.com/artifact/joda-time/joda-time)
- [Documentación de la API de Joda-Time para Referencia Técnica](https://www.joda.org/joda-time/apidocs/index.html)