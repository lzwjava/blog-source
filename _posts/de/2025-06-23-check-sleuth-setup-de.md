---
audio: false
generated: true
lang: de
layout: post
title: Fehlerbehebung bei leeren `traceId` und `spanId` in Protokollen
translated: true
type: note
---

Die `traceId` und `spanId` sind in Ihren Log-Zeilen `[blog-server,,]` wahrscheinlich aus einem der folgenden Gründe leer:

* **Fehlende oder falsche Sleuth-Abhängigkeit:** Stellen Sie sicher, dass die `spring-cloud-starter-sleuth`-Abhängigkeit korrekt in Ihrer `pom.xml` (für Maven) oder `build.gradle` (für Gradle) hinzugefügt wurde und dass Sie kompatible Spring Boot und Spring Cloud Versionen verwenden. Ohne diese Abhängigkeit wird die Auto-Konfiguration von Spring Cloud Sleuth nicht aktiviert.

    ```xml
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-sleuth</artifactId>
    </dependency>
    ```

* **Benutzerdefiniertes Logging-Pattern:** Wenn Sie ein benutzerdefiniertes Logging-Pattern definiert haben (z.B. in `logback-spring.xml` oder `application.properties`), müssen Sie explizit Platzhalter für die `traceId` und `spanId` einfügen. Wenn diese Platzhalter fehlen, erscheinen die IDs nicht in Ihren Logs, selbst wenn Sleuth aktiv ist.

    Für Logback stellen Sie sicher, dass Ihr Pattern `%X{traceId}` und `%X{spanId}` enthält:

    ```xml
    <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level [${spring.application.name:-},%X{traceId:-},%X{spanId:-}] %thread %logger{36} - %msg%n</pattern>
    ```

* **Kein aktiver Trace/Span-Kontext:** Während Sleuth automatisch viele Spring-Komponenten instrumentiert (wie z.B. `DispatcherServlet` für HTTP-Anfragen), ist es möglich, dass diese spezifischen Log-Nachrichten in einem Kontext generiert werden, in dem noch keine Trace oder Span initiiert oder propagiert wurde. Zum Beispiel könnten einige sehr frühe Anwendungs-Startup-Logs oder Logs von Threads, die nicht von Sleuths Kontext-Propagierung verwaltet werden, diese IDs nicht haben. Für Logs während der aktiven HTTP-Anfrageverarbeitung, wie `HttpEntityMethodProcessor` und `DispatcherServlet`, die eine Anfrage abschließen, ist dies jedoch weniger wahrscheinlich, wenn Sleuth korrekt eingerichtet ist.

Um das Problem zu beheben, überprüfen Sie zunächst Ihre Abhängigkeiten und die Logging-Konfiguration. Wenn diese korrekt sind, stellen Sie sicher, dass Anfragen tatsächlich Ihre Anwendung erreichen und vom Spring MVC `DispatcherServlet` verarbeitet werden, was die Instrumentierung von Sleuth auslösen sollte.