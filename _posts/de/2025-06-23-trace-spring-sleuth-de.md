---
audio: false
generated: true
lang: de
layout: post
title: Meisterung von Spring Cloud Sleuth in Spring Boot
translated: true
type: note
---

Spring Cloud Sleuth ist ein leistungsstarkes Tool, um verteilte Tracing-Fähigkeiten zu Spring-Anwendungen hinzuzufügen. Während es besonders in Microservice-Architekturen nützlich ist, um Anfragen über mehrere Dienste hinweg zu verfolgen, bietet es auch erhebliche Vorteile für einzelne (Monolith-)Anwendungen, indem es die Log-Korrelation und Fehlerbehebung verbessert.

Diese Anleitung bietet einen umfassenden Überblick über die Verwendung von Spring Cloud Sleuth innerhalb einer einzelnen Spring Boot-Anwendung und greift auf den Ansatz von Baeldung zurück.

## 1. Was ist Spring Cloud Sleuth?

Im Kern instrumentiert Spring Cloud Sleuth Spring-Anwendungen, um automatisch Tracing-Informationen zu Logs hinzuzufügen und diese über verschiedene Komponenten und sogar Threads innerhalb einer einzelnen Anwendung hinweg zu verbreiten. Es nutzt dafür die Brave-Bibliothek von OpenZipkin.

**Wichtige Terminologie:**

*   **Trace:** Stellt eine einzelne Anfrage oder einen Job dar, der durch die Anwendung fließt. Jeder Trace hat eine eindeutige `traceId`. Man kann es sich als die komplette Reise einer Anfrage vorstellen.
*   **Span:** Stellt eine logische Arbeitseinheit innerhalb eines Traces dar. Ein Trace besteht aus mehreren Spans, die eine baumähnliche Struktur bilden. Jeder Span hat eine eindeutige `spanId`. Zum Beispiel könnte eine eingehende HTTP-Anfrage ein Span sein, und ein Methodenaufruf innerhalb dieser Anfrage könnte ein weiterer (untergeordneter) Span sein.
*   **MDC (Mapped Diagnostic Context):** Sleuth integriert sich in den MDC von Slf4J, um `traceId` und `spanId` in Ihre Log-Meldungen einzufügen, was das Filtern und Korrelieren von Logs für eine bestimmte Anfrage erleichtert.

## 2. Warum Sleuth in einer einzelnen Anwendung verwenden?

Selbst in einem Monolithen durchlaufen Anfragen oft mehrere Ebenen, asynchrone Operationen und verschiedene Threads. Das manuelle Korrelieren von Log-Meldungen für eine einzelne Anfrage kann mühsam und fehleranfällig sein. Sleuth automatisiert dies durch:

*   **Vereinfachte Fehlerbehebung:** Durch das Hinzufügen von `traceId` und `spanId` zu jedem Log-Eintrag können Sie Logs leicht filtern, um alles im Zusammenhang mit einer bestimmten Benutzeranfrage zu sehen, selbst wenn sie mehrere Methoden, Dienste oder Threads innerhalb Ihrer einzelnen Anwendung durchläuft.
*   **Verbesserte Observability:** Bietet ein klareres Bild davon, wie eine Anfrage fließt und wo potenzielle Engpässe oder Probleme auftreten könnten.
*   **Konsistenz:** Stellt einen konsistenten Ansatz für die Log-Korrelation sicher, ohne manuellen Aufwand in jedem Teil Ihrer Codebasis zu erfordern.

## 3. Erste Schritte: Einrichtung und Konfiguration

### 3.1. Projekteinrichtung (Maven)

Um zu beginnen, erstellen Sie ein neues Spring Boot-Projekt (Sie können Spring Initializr verwenden) und fügen Sie die `spring-cloud-starter-sleuth`-Abhängigkeit zu Ihrer `pom.xml` hinzu:

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-sleuth</artifactId>
</dependency>
```

**Wichtig:** Stellen Sie sicher, dass Sie eine kompatible Spring Boot- und Spring Cloud-Version verwenden. Spring Cloud-Abhängigkeiten werden typischerweise über ein Bill of Materials (BOM) verwaltet.

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

Ersetzen Sie `${spring-cloud.version}` durch die entsprechende Release Train-Version (z.B. `2021.0.1`, `2022.0.0`).

### 3.2. Anwendungsname

Es wird dringend empfohlen, einen Anwendungsnamen in Ihrer `application.properties`- oder `application.yml`-Datei zu setzen. Dieser Name erscheint in Ihren Logs, was hilfreich ist, um die Quelle von Logs zu identifizieren, besonders wenn Sie später zu einem verteilten System wechseln.

```properties
# application.properties
spring.application.name=my-single-app
```

### 3.3. Logging-Pattern

Spring Cloud Sleuth modifiziert automatisch das standardmäßige Logging-Pattern, um `traceId` und `spanId` einzuschließen. Eine typische Log-Ausgabe mit Sleuth könnte so aussehen:

```
2025-06-23 23:30:00.123 INFO [my-single-app,a1b2c3d4e5f6a7b8,a1b2c3d4e5f6a7b8,false] 12345 --- [nio-8080-exec-1] c.e.m.MyController : This is a log message.
```

Hier:

*   `my-single-app`: Ist der `spring.application.name`.
*   `a1b2c3d4e5f6a7b8`: Ist die `traceId`.
*   `a1b2c3d4e5f6a7b8` (die zweite): Ist die `spanId` (für den Root-Span sind traceId und spanId oft gleich).
*   `false`: Zeigt an, ob der Span exportierbar ist (true bedeutet, er wird an einen Tracing-Collector wie Zipkin gesendet).

Wenn Sie ein benutzerdefiniertes Logging-Pattern haben, müssen Sie `traceId` und `spanId` explizit mit `%X{traceId}` und `%X{spanId}` hinzufügen (für Logback).

Beispiel für ein benutzerdefiniertes Logback-Pattern in `logback-spring.xml`:

```xml
<appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
        <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level [${spring.application.name:-},%X{traceId:-},%X{spanId:-}] %thread %logger{36} - %msg%n</pattern>
    </encoder>
</appender>
```

## 4. Wie Sleuth in einer einzelnen Anwendung funktioniert

Sobald die `spring-cloud-starter-sleuth`-Abhängigkeit im Classpath ist, übernimmt die Auto-Konfiguration von Spring Boot.

### 4.1. Automatische Instrumentierung

Sleuth instrumentiert automatisch gängige Spring-Komponenten und Kommunikationskanäle:

*   **Servlet Filter:** Für eingehende HTTP-Anfragen an Ihre Controller.
*   **RestTemplate:** Für ausgehende HTTP-Aufrufe, die mit `RestTemplate` durchgeführt werden (stellen Sie sicher, dass Sie einen Bean-verwalteten `RestTemplate` verwenden, damit Sleuth ihn automatisch instrumentieren kann).
*   **Geplante Aktionen:** Für `@Scheduled`-Methoden.
*   **Nachrichtenkanäle:** Für Spring Integration und Spring Cloud Stream.
*   **Asynchrone Methoden:** Für `@Async`-Methoden (stellt sicher, dass der Trace/Span-Kontext über Thread-Grenzen hinweg propagiert wird).

### 4.2. Einfaches Web Request-Beispiel

Betrachten Sie eine einfache Spring Boot-Anwendung mit einem REST-Controller:

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

Wenn Sie auf `http://localhost:8080/` zugreifen, werden Sie Log-Meldungen wie diese sehen:

```
2025-06-23 23:35:00.123 INFO [my-single-app,c9d0e1f2a3b4c5d6,c9d0e1f2a3b4c5d6,false] 7890 --- [nio-8080-exec-1] c.e.m.MyController : Hello from MyController
```

Beachten Sie die automatisch hinzugefügte `traceId` und `spanId`.

### 4.3. Kontext über Methoden hinweg propagieren (Gleicher Span)

Wenn Ihre Anfrage mehrere Methoden innerhalb derselben Anwendung durchläuft und Sie möchten, dass diese Methoden Teil *desselben Spans* sind, erledigt Sleuth dies automatisch.

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
        Thread.sleep(100); // Simuliert etwas Arbeit
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

Logs für `/same-span-example` zeigen dieselbe `traceId` und `spanId` für sowohl die Controller- als auch die Service-Methoden:

```
2025-06-23 23:40:00.100 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyController : Entering same-span-example endpoint
2025-06-23 23:40:00.200 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyService : Doing some work in MyService
2025-06-23 23:40:00.205 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyController : Exiting same-span-example endpoint
```

### 4.4. Manuelles Erstellen neuer Spans

Möglicherweise möchten Sie einen neuen Span für eine bestimmte Arbeitseinheit innerhalb Ihrer Anwendung erstellen, selbst wenn sie Teil desselben übergeordneten Traces ist. Dies ermöglicht eine feingranularere Verfolgung und Zeitmessung. Spring Cloud Sleuth bietet die `Tracer`-API dafür.

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
    private Tracer tracer; // Injiziere den Brave Tracer

    public void doSomeWorkNewSpan() throws InterruptedException {
        logger.info("I'm in the original span before new span");

        // Erstelle einen neuen Span mit einem beschreibenden Namen
        Span newSpan = tracer.nextSpan().name("custom-internal-work").start();
        try (Tracer.SpanInScope ws = tracer.withSpanInScope(newSpan)) {
            Thread.sleep(200); // Simuliert etwas Arbeit im neuen Span
            logger.info("I'm in the new custom span doing some cool work");
        } finally {
            newSpan.finish(); // Beende den Span immer
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

Logs für `/new-span-example` zeigen, dass die Trace-ID gleich bleibt, aber eine neue `spanId` für die "custom-internal-work" erscheint:

```
2025-06-23 23:45:00.100 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyController : Entering new-span-example endpoint
2025-06-23 23:45:00.105 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm in the original span before new span
2025-06-23 23:45:00.300 INFO [my-single-app,f0e1d2c3b4a5f6e7,8a9b0c1d2e3f4a5b,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm in the new custom span doing some cool work
2025-06-23 23:45:00.305 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm back in the original span
2025-06-23 23:45:00.310 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyController : Exiting new-span-example endpoint
```

Beachten Sie, wie sich die `spanId` im `custom-internal-work`-Abschnitt in `8a9b0c1d2e3f4a5b` ändert und dann wieder zurückwechselt.

### 4.5. Asynchrone Verarbeitung

Sleuth integriert sich nahtlos mit Springs `@Async`-Annotation, um den Trace-Kontext über Thread-Grenzen hinweg zu propagieren.

Aktivieren Sie zunächst die asynchrone Verarbeitung in Ihrer Hauptanwendungsklasse:

```java
@SpringBootApplication
@EnableAsync // Aktiviere asynchrone Ausführung
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

Erstellen Sie dann einen asynchronen Service:

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
        Thread.sleep(500); // Simuliert eine langlaufende Aufgabe
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

Die Logs zeigen dieselbe `traceId`, aber eine andere `spanId` für die asynchrone Methode, da sie in einem neuen Thread läuft und eine neue Arbeitseinheit darstellt:

```
2025-06-23 23:50:00.100 INFO [my-single-app,1a2b3c4d5e6f7a8b,1a2b3c4d5e6f7a8b,false] 1234 --- [nio-8080-exec-4] c.e.m.MyController : Calling async task
2025-06-23 23:50:00.105 INFO [my-single-app,1a2b3c4d5e6f7a8b,9c0d1e2f3a4b5c6d,false] 1234 --- [           task-1] c.e.m.AsyncService : Starting async task
2025-06-23 23:50:00.110 INFO [my-single-app,1a2b3c4d5e6f7a8b,1a2b3c4d5e6f7a8b,false] 1234 --- [nio-8080-exec-4] c.e.m.MyController : Async task initiated, returning from controller
// ... einige Zeit später ...
2025-06-23 23:50:00.605 INFO [my-single-app,1a2b3c4d5e6f7a8b,9c0d1e2f3a4b5c6d,false] 1234 --- [           task-1] c.e.m.AsyncService : Finished async task
```

Beachten Sie, dass die `traceId` gleich bleibt, sich die `spanId` für die asynchrone Methode jedoch ändert und der Thread-Name auch den asynchronen Executor widerspiegelt.

### 4.6. Anpassen von Span-Namen mit `@SpanName`

Sie können die `@SpanName`-Annotation verwenden, um aussagekräftigere Namen für Ihre automatisch generierten Spans bereitzustellen.

```java
import org.springframework.cloud.sleuth.annotation.SpanName;
import org.springframework.stereotype.Service;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Service
public class AnnotatedService {
    private static final Logger logger = LoggerFactory.getLogger(AnnotatedService.class);

    @SpanName("Annotated_Service_Method") // Benutzerdefinierter Span-Name
    public void annotatedMethod() throws InterruptedException {
        logger.info("Inside annotated method");
        Thread.sleep(50);
    }
}

// ... in Ihrem Controller oder einem anderen Service ...
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

Die Logs spiegeln den benutzerdefinierten Span-Namen wider:

```
2025-06-23 23:55:00.100 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.MyController : Calling annotated method
2025-06-23 23:55:00.150 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.AnnotatedService : Inside annotated method (span name: Annotated_Service_Method)
2025-06-23 23:55:00.155 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.MyController : Finished calling annotated method
```

## 5. Integration mit Zipkin (Optional, aber empfohlen)

Während sich dieser Leitfaden auf einzelne Anwendungen konzentriert, entfaltet sich die wahre Stärke von Sleuth bei der Integration mit einem verteilten Tracing-System wie Zipkin. Zipkin sammelt die von Sleuth exportierten Trace- und Span-Daten und bietet eine UI, um den Fluss und die Zeitabläufe von Anfragen zu visualisieren.

Um die Integration mit Zipkin zu aktivieren, fügen Sie die `spring-cloud-starter-zipkin`-Abhängigkeit hinzu:

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-zipkin</artifactId>
</dependency>
```

Standardmäßig versucht Sleuth, Traces an einen Zipkin-Collector zu senden, der unter `http://localhost:9411` läuft. Sie können dies in `application.properties` konfigurieren:

```properties
spring.zipkin.base-url=http://localhost:9411
```

Sie können einen Zipkin-Server einfach mit Docker ausführen:

```bash
docker run -d -p 9411:9411 openzipkin/zipkin
```

Sobald Zipkin läuft, sendet Ihre einzelne Spring Boot-Anwendung automatisch ihre Trace-Daten, und Sie können die Traces unter `http://localhost:9411/` einsehen.

## 6. Sampling

Standardmäßig wendet Sleuth eine Sampling-Strategie an, um zu vermeiden, dass das Tracing-System mit Daten überflutet wird. Es sampled typischerweise einen Prozentsatz der Anfragen. Sie können die Sampling-Rate in `application.properties` konfigurieren:

```properties
# Sampled 100% der Anfragen
spring.sleuth.sampler.probability=1.0
```

Ein Wert von `1.0` bedeutet, dass alle Anfragen getraced werden, während `0.1` bedeutet, dass 10% getraced werden.

## 7. Fazit

Spring Cloud Sleuth verbessert selbst in einer einzelnen Anwendung die Protokollierung und Fehlerbehebung erheblich, indem es automatisch `traceId` und `spanId` in Ihre Log-Meldungen einfügt. Dies ermöglicht es Ihnen, den Ausführungsfluss einer einzelnen Anfrage leicht zu verfolgen, selbst wenn sie verschiedene Methoden und Threads durchläuft. Indem Sie die Kernkonzepte von Traces und Spans verstehen und die automatische Instrumentierung von Sleuth oder die manuelle Span-Erstellung nutzen, können Sie eine viel bessere Observability in Ihre monolithischen Anwendungen gewinnen. Die Integration mit Zipkin erschließt weiteres Potenzial für die Visualisierung und Analyse des Verhaltens Ihrer Anwendung.