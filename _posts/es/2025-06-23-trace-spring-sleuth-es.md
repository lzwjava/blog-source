---
audio: false
generated: true
lang: es
layout: post
title: Dominando Spring Cloud Sleuth en Spring Boot
translated: true
type: note
---

Spring Cloud Sleuth es una herramienta poderosa para agregar capacidades de trazado distribuido a las aplicaciones Spring. Si bien es particularmente útil en arquitecturas de microservicios para rastrear solicitudes a través de múltiples servicios, también proporciona beneficios significativos para aplicaciones únicas (monolíticas) al mejorar la correlación de registros y la depuración.

Esta guía proporcionará una descripción general completa del uso de Spring Cloud Sleuth dentro de una única aplicación Spring Boot, extrayendo ideas del enfoque de Baeldung.

## 1. ¿Qué es Spring Cloud Sleuth?

En esencia, Spring Cloud Sleuth instrumenta aplicaciones Spring para agregar automáticamente información de trazado a los registros y propagarla a través de diferentes componentes e incluso hilos dentro de una única aplicación. Aprovecha la biblioteca Brave de OpenZipkin para esta funcionalidad.

**Terminología Clave:**

  * **Trace (Trazado):** Representa una única solicitud o trabajo que fluye a través de la aplicación. Cada trazado tiene un `traceId` único. Piensa en ello como el viaje de extremo a extremo de una solicitud.
  * **Span (Intervalo):** Representa una unidad lógica de trabajo dentro de un trazado. Un trazado se compone de múltiples intervalos, formando una estructura similar a un árbol. Cada intervalo tiene un `spanId` único. Por ejemplo, una solicitud HTTP entrante podría ser un intervalo, y una llamada a un método dentro de esa solicitud podría ser otro intervalo (secundario).
  * **MDC (Mapped Diagnostic Context):** Sleuth se integra con el MDC de Slf4J para inyectar `traceId` y `spanId` en tus mensajes de registro, facilitando filtrar y correlacionar registros para una solicitud específica.

## 2. ¿Por qué usar Sleuth en una aplicación única?

Incluso en un monolito, las solicitudes a menudo involucran múltiples capas, operaciones asíncronas y diferentes hilos. Correlacionar manualmente los mensajes de registro para una única solicitud puede ser tedioso y propenso a errores. Sleuth automatiza esto mediante:

  * **Simplificar la Depuración:** Al agregar `traceId` y `spanId` a cada entrada de registro, puedes filtrar fácilmente los registros para ver todo lo relacionado con una solicitud de usuario específica, incluso si atraviesa múltiples métodos, servicios o hilos dentro de tu única aplicación.
  * **Observabilidad Mejorada:** Proporciona una imagen más clara de cómo fluye una solicitud y dónde podrían ocurrir posibles cuellos de botella o problemas.
  * **Consistencia:** Garantiza un enfoque consistente para la correlación de registros sin requerir esfuerzo manual en cada parte de tu base de código.

## 3. Comenzando: Configuración

### 3.1. Configuración del Proyecto (Maven)

Para comenzar, crea un nuevo proyecto Spring Boot (puedes usar Spring Initializr) y agrega la dependencia `spring-cloud-starter-sleuth` a tu `pom.xml`:

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-sleuth</artifactId>
</dependency>
```

**Importante:** Asegúrate de usar una versión compatible de Spring Boot y Spring Cloud. Las dependencias de Spring Cloud generalmente se gestionan usando un Bill of Materials (BOM).

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>${spring-cloud.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

Reemplaza `${spring-cloud.version}` con la versión adecuada del release train (por ejemplo, `2021.0.1`, `2022.0.0`).

### 3.2. Nombre de la Aplicación

Es muy recomendable establecer un nombre de aplicación en tu archivo `application.properties` o `application.yml`. Este nombre aparecerá en tus registros, lo cual es útil para identificar la fuente de los registros, especialmente si luego te mudas a un sistema distribuido.

```properties
# application.properties
spring.application.name=my-single-app
```

### 3.3. Patrón de Registro

Spring Cloud Sleuth modifica automáticamente el patrón de registro predeterminado para incluir `traceId` y `spanId`. Una salida de registro típica con Sleuth podría verse así:

```
2025-06-23 23:30:00.123 INFO [my-single-app,a1b2c3d4e5f6a7b8,a1b2c3d4e5f6a7b8,false] 12345 --- [nio-8080-exec-1] c.e.m.MyController : Este es un mensaje de registro.
```

Aquí:

  * `my-single-app`: Es el `spring.application.name`.
  * `a1b2c3d4e5f6a7b8`: Es el `traceId`.
  * `a1b2c3d4e5f6a7b8` (el segundo): Es el `spanId` (para el intervalo raíz, el traceId y el spanId a menudo son iguales).
  * `false`: Indica si el intervalo es exportable (true significa que se enviará a un colector de trazado como Zipkin).

Si tienes un patrón de registro personalizado, necesitarás agregar explícitamente el `traceId` y `spanId` usando `%X{traceId}` y `%X{spanId}` (para Logback).

Ejemplo de patrón Logback personalizado en `logback-spring.xml`:

```xml
<appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
        <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level [${spring.application.name:-},%X{traceId:-},%X{spanId:-}] %thread %logger{36} - %msg%n</pattern>
    </encoder>
</appender>
```

## 4. Cómo funciona Sleuth en una aplicación única

Una vez que la dependencia `spring-cloud-starter-sleuth` está en el classpath, la auto-configuración de Spring Boot se hace cargo.

### 4.1. Instrumentación Automática

Sleuth instrumenta automáticamente componentes comunes de Spring y canales de comunicación:

  * **Filtro Servlet:** Para solicitudes HTTP entrantes a tus controladores.
  * **RestTemplate:** Para llamadas HTTP salientes realizadas usando `RestTemplate` (asegúrate de usar un `RestTemplate` gestionado como bean para que Sleuth lo instrumente automáticamente).
  * **Acciones Programadas:** Para métodos con `@Scheduled`.
  * **Canales de Mensajería:** Para Spring Integration y Spring Cloud Stream.
  * **Métodos Asíncronos:** Para métodos con `@Async` (asegura que el contexto de trazado/intervalo se propague a través de los hilos).

### 4.2. Ejemplo de Solicitud Web Simple

Considera una aplicación Spring Boot simple con un controlador REST:

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MyController {

    private static final Logger logger = LoggerFactory.getLogger(MyController.class);

    @GetMapping("/")
    public String helloSleuth() {
        logger.info("Hello from MyController");
        return "success";
    }
}
```

Cuando accedes a `http://localhost:8080/`, verás mensajes de registro como:

```
2025-06-23 23:35:00.123 INFO [my-single-app,c9d0e1f2a3b4c5d6,c9d0e1f2a3b4c5d6,false] 7890 --- [nio-8080-exec-1] c.e.m.MyController : Hello from MyController
```

Observa el `traceId` y `spanId` agregados automáticamente.

### 4.3. Propagando el Contexto a Través de Métodos (Mismo Intervalo)

Si tu solicitud fluye a través de múltiples métodos dentro de la misma aplicación y deseas que estos métodos formen parte del *mismo intervalo*, Sleuth maneja esto automáticamente.

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.stereotype.Service;

@Service
class MyService {
    private static final Logger logger = LoggerFactory.getLogger(MyService.class);

    public void doSomeWork() throws InterruptedException {
        Thread.sleep(100); // Simular algo de trabajo
        logger.info("Doing some work in MyService");
    }
}

@RestController
public class MyController {
    private static final Logger logger = LoggerFactory.getLogger(MyController.class);

    @Autowired
    private MyService myService;

    @GetMapping("/same-span-example")
    public String sameSpanExample() throws InterruptedException {
        logger.info("Entering same-span-example endpoint");
        myService.doSomeWork();
        logger.info("Exiting same-span-example endpoint");
        return "success";
    }
}
```

Los registros para `/same-span-example` mostrarán el mismo `traceId` y `spanId` tanto para el controlador como para los métodos del servicio:

```
2025-06-23 23:40:00.100 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyController : Entering same-span-example endpoint
2025-06-23 23:40:00.200 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyService : Doing some work in MyService
2025-06-23 23:40:00.205 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyController : Exiting same-span-example endpoint
```

### 4.4. Creando Nuevos Intervalos Manualmente

Es posible que desees crear un nuevo intervalo para una unidad de trabajo distinta dentro de tu aplicación, incluso si es parte del mismo trazado general. Esto permite un seguimiento y una temporización más detallados. Spring Cloud Sleuth proporciona la API `Tracer` para esto.

```java
import brave.Tracer;
import brave.Span;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@Service
class MyService {
    private static final Logger logger = LoggerFactory.getLogger(MyService.class);

    @Autowired
    private Tracer tracer; // Inyectar el Brave Tracer

    public void doSomeWorkNewSpan() throws InterruptedException {
        logger.info("I'm in the original span before new span");

        // Crear un nuevo intervalo con un nombre descriptivo
        Span newSpan = tracer.nextSpan().name("custom-internal-work").start();
        try (Tracer.SpanInScope ws = tracer.withSpanInScope(newSpan)) {
            Thread.sleep(200); // Simular algo de trabajo en el nuevo intervalo
            logger.info("I'm in the new custom span doing some cool work");
        } finally {
            newSpan.finish(); // Siempre finalizar el intervalo
        }

        logger.info("I'm back in the original span");
    }
}

@RestController
public class MyController {
    private static final Logger logger = LoggerFactory.getLogger(MyController.class);

    @Autowired
    private MyService myService;

    @GetMapping("/new-span-example")
    public String newSpanExample() throws InterruptedException {
        logger.info("Entering new-span-example endpoint");
        myService.doSomeWorkNewSpan();
        logger.info("Exiting new-span-example endpoint");
        return "success";
    }
}
```

Los registros para `/new-span-example` mostrarán que el ID de trazado permanece igual, pero aparecerá un nuevo `spanId` para el "custom-internal-work":

```
2025-06-23 23:45:00.100 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyController : Entering new-span-example endpoint
2025-06-23 23:45:00.105 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm in the original span before new span
2025-06-23 23:45:00.300 INFO [my-single-app,f0e1d2c3b4a5f6e7,8a9b0c1d2e3f4a5b,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm in the new custom span doing some cool work
2025-06-23 23:45:00.305 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm back in the original span
2025-06-23 23:45:00.310 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyController : Exiting new-span-example endpoint
```

Observa cómo el `spanId` cambia a `8a9b0c1d2e3f4a5b` dentro de la sección `custom-internal-work` y luego vuelve al original.

### 4.5. Procesamiento Asíncrono

Sleuth se integra perfectamente con la anotación `@Async` de Spring para propagar el contexto de trazado a través de los límites de los hilos.

Primero, habilita el procesamiento asíncrono en tu clase de aplicación principal:

```java
@SpringBootApplication
@EnableAsync // Habilitar ejecución asíncrona
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

Luego, crea un servicio asíncrono:

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

@Service
public class AsyncService {
    private static final Logger logger = LoggerFactory.getLogger(AsyncService.class);

    @Async
    public void performAsyncTask() throws InterruptedException {
        logger.info("Starting async task");
        Thread.sleep(500); // Simular una tarea de larga duración
        logger.info("Finished async task");
    }
}

@RestController
public class MyController {
    private static final Logger logger = LoggerFactory.getLogger(MyController.class);

    @Autowired
    private AsyncService asyncService;

    @GetMapping("/async-example")
    public String asyncExample() throws InterruptedException {
        logger.info("Calling async task");
        asyncService.performAsyncTask();
        logger.info("Async task initiated, returning from controller");
        return "success";
    }
}
```

Los registros mostrarán el mismo `traceId` pero un `spanId` diferente para el método asíncrono, ya que se ejecuta en un nuevo hilo y representa una nueva unidad de trabajo:

```
2025-06-23 23:50:00.100 INFO [my-single-app,1a2b3c4d5e6f7a8b,1a2b3c4d5e6f7a8b,false] 1234 --- [nio-8080-exec-4] c.e.m.MyController : Calling async task
2025-06-23 23:50:00.105 INFO [my-single-app,1a2b3c4d5e6f7a8b,9c0d1e2f3a4b5c6d,false] 1234 --- [           task-1] c.e.m.AsyncService : Starting async task
2025-06-23 23:50:00.110 INFO [my-single-app,1a2b3c4d5e6f7a8b,1a2b3c4d5e6f7a8b,false] 1234 --- [nio-8080-exec-4] c.e.m.MyController : Async task initiated, returning from controller
// ... algún tiempo después ...
2025-06-23 23:50:00.605 INFO [my-single-app,1a2b3c4d5e6f7a8b,9c0d1e2f3a4b5c6d,false] 1234 --- [           task-1] c.e.m.AsyncService : Finished async task
```

Observa que el `traceId` permanece igual, pero el `spanId` cambia para el método asíncrono, y el nombre del hilo también refleja el ejecutor asíncrono.

### 4.6. Personalizando Nombres de Intervalos con `@SpanName`

Puedes usar la anotación `@SpanName` para proporcionar nombres más significativos para tus intervalos generados automáticamente.

```java
import org.springframework.cloud.sleuth.annotation.SpanName;
import org.springframework.stereotype.Service;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Service
public class AnnotatedService {
    private static final Logger logger = LoggerFactory.getLogger(AnnotatedService.class);

    @SpanName("Annotated_Service_Method") // Nombre personalizado del intervalo
    public void annotatedMethod() throws InterruptedException {
        logger.info("Inside annotated method");
        Thread.sleep(50);
    }
}

// ... en tu controlador u otro servicio ...
@Autowired
private AnnotatedService annotatedService;

@GetMapping("/annotated-span")
public String annotatedSpanExample() throws InterruptedException {
    logger.info("Calling annotated method");
    annotatedService.annotatedMethod();
    logger.info("Finished calling annotated method");
    return "success";
}
```

Los registros reflejarán el nombre personalizado del intervalo:

```
2025-06-23 23:55:00.100 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.MyController : Calling annotated method
2025-06-23 23:55:00.150 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.AnnotatedService : Inside annotated method (span name: Annotated_Service_Method)
2025-06-23 23:55:00.155 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.MyController : Finished calling annotated method
```

## 5. Integración con Zipkin (Opcional pero Recomendado)

Si bien esta guía se centra en aplicaciones únicas, el verdadero poder de Sleuth surge cuando se integra con un sistema de trazado distribuido como Zipkin. Zipkin recopila los datos de trazado e intervalo exportados por Sleuth y proporciona una interfaz de usuario para visualizar el flujo y el tiempo de las solicitudes.

Para integrar con Zipkin, agrega la dependencia `spring-cloud-starter-zipkin`:

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-zipkin</artifactId>
</dependency>
```

Por defecto, Sleuth intentará enviar los trazados a un colector de Zipkin ejecutándose en `http://localhost:9411`. Puedes configurar esto en `application.properties`:

```properties
spring.zipkin.base-url=http://localhost:9411
```

Puedes ejecutar un servidor Zipkin fácilmente con Docker:

```bash
docker run -d -p 9411:9411 openzipkin/zipkin
```

Una vez que Zipkin esté en ejecución, tu única aplicación Spring Boot enviará automáticamente sus datos de trazado, y podrás ver los trazados en `http://localhost:9411/`.

## 6. Muestreo

Por defecto, Sleuth aplica una estrategia de muestreo para evitar saturar el sistema de trazado con datos. Normalmente muestrea un porcentaje de las solicitudes. Puedes configurar la tasa de muestreo en `application.properties`:

```properties
# Muestrea el 100% de las solicitudes
spring.sleuth.sampler.probability=1.0
```

Un valor de `1.0` significa que todas las solicitudes serán trazadas, mientras que `0.1` significa que se trazará el 10%.

## 7. Conclusión

Spring Cloud Sleuth, incluso en una aplicación única, mejora significativamente el registro y la depuración al inyectar automáticamente `traceId` y `spanId` en tus mensajes de registro. Esto te permite seguir fácilmente el flujo de ejecución de una única solicitud, incluso cuando atraviesa diferentes métodos e hilos. Al comprender los conceptos centrales de trazados e intervalos y utilizar la instrumentación automática de Sleuth o la creación manual de intervalos, puedes obtener una observabilidad mucho mejor de tus aplicaciones monolíticas. La integración con Zipkin desbloquea aún más el potencial para la visualización y el análisis del comportamiento de tu aplicación.