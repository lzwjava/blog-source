---
audio: false
generated: true
lang: de
layout: post
title: Spring Boot Log4j Anforderungsverfolgung
translated: true
type: note
---

In einer Java Spring Boot Anwendung, die Log4j ohne ein integriertes Trace-ID-Design verwendet, kann es tatsächlich schwierig sein, einen bestimmten Logeintrag auf eine vom Frontend initiierte Anfrage zurückzuführen. Sie haben recht, dass `%t` (Thread-Name) in Log4j dabei hilft, Logs zu identifizieren, die an einen bestimmten Thread gebunden sind. Wie Sie jedoch festgestellt haben, wird dies unzuverlässiger, wenn Anfragen mehrere Threads umspannen (z.B. aufgrund asynchroner Verarbeitung, Thread-Pools oder Downstream-Aufrufe). Die Verwendung eines Zeitbereichs zur Suche in Logs ist ein Workaround, aber ungenau und umständlich, besonders in Systemen mit hohem Verkehrsaufkommen. Lassen Sie uns einige praktische Ratschläge erkunden, um diese Situation zu verbessern, ohne Ihr gesamtes Setup zu überarbeiten.

### Schnelle und praktische Vorschläge
1.  **Nutzen Sie MDC (Mapped Diagnostic Context) mit Log4j**
    - Log4j unterstützt MDC, was es Ihnen erlaubt, kontextuelle Schlüssel-Wert-Paare an Logs innerhalb eines Threads anzuhängen (und sie mit etwas Aufwand sogar über Thread-Grenzen hinweg zu propagieren).
    - Generieren Sie eine eindeutige Anfrage-ID, wenn die Frontend-Anfrage Ihre Spring Boot Anwendung erreicht (z.B. eine UUID), und speichern Sie sie im MDC. Nehmen Sie dann diese ID in Ihr Log-Muster auf.
    - **Umsetzung:**
        - In einem Spring Boot Filter oder Interceptor (z.B. `OncePerRequestFilter`), generieren Sie die ID:
          ```java
          import org.slf4j.MDC;
          import javax.servlet.FilterChain;
          import javax.servlet.http.HttpServletRequest;
          import javax.servlet.http.HttpServletResponse;
          import java.util.UUID;

          public class RequestTracingFilter extends OncePerRequestFilter {
              @Override
              protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) {
                  try {
                      String traceId = UUID.randomUUID().toString();
                      MDC.put("traceId", traceId);
                      filterChain.doFilter(request, response);
                  } finally {
                      MDC.clear(); // Bereinigung nach der Anfrage
                  }
              }
          }
          ```
        - Registrieren Sie den Filter in Ihrer Spring Boot Konfiguration:
          ```java
          @Bean
          public FilterRegistrationBean<RequestTracingFilter> tracingFilter() {
              FilterRegistrationBean<RequestTracingFilter> registrationBean = new FilterRegistrationBean<>();
              registrationBean.setFilter(new RequestTracingFilter());
              registrationBean.addUrlPatterns("/*");
              return registrationBean;
          }
          ```
        - Aktualisieren Sie Ihr Log4j-Muster in `log4j.properties` oder `log4j.xml`, um die `traceId` einzuschließen:
          ```properties
          log4j.appender.console.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} [%t] %-5p %c{1} - %m [traceId=%X{traceId}]%n
          ```
        - Jede Logzeile, die zu dieser Anfrage gehört, enthält nun die `traceId`, was die Rückverfolgung zum Frontend-Button-Klick einfach macht.

2.  **Propagieren Sie die Trace-ID über Thread-Grenzen hinweg**
    - Wenn Ihre App Thread-Pools oder asynchrone Aufrufe verwendet (z.B. `@Async`), wird der MDC-Kontext möglicherweise nicht automatisch propagiert. Um dies zu handhaben:
        - Wrappen Sie asynchrone Tasks mit einem benutzerdefinierten Executor, der den MDC-Kontext kopiert:
          ```java
          import java.util.concurrent.Executor;
          import org.springframework.context.annotation.Bean;
          import org.springframework.context.annotation.Configuration;
          import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

          @Configuration
          public class AsyncConfig {
              @Bean(name = "taskExecutor")
              public Executor taskExecutor() {
                  ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
                  executor.setCorePoolSize(10);
                  executor.setMaxPoolSize(20);
                  executor.setQueueCapacity(100);
                  executor.setTaskDecorator(task -> {
                      Map<String, String> context = MDC.getCopyOfContextMap();
                      return () -> {
                          try {
                              if (context != null) MDC.setContextMap(context);
                              task.run();
                          } finally {
                              MDC.clear();
                          }
                      };
                  });
                  executor.initialize();
                  return executor;
              }
          }
          ```
        - Dies stellt sicher, dass die `traceId` auch über Thread-Grenzen hinweg bei der Anfrage bleibt.

3.  **Fügen Sie Frontend-Korrelation hinzu**
    - Wenn möglich, lassen Sie das Frontend einen benutzerdefinierten Header (z.B. `X-Request-ID`) mit einer eindeutigen ID mitsenden, wenn der Button geklickt wird. Ihr Backend kann diese dann übernehmen, anstatt eine eigene UUID zu generieren. Dies verknüpft den Log direkt mit der Frontend-Aktion ohne zusätzliche Rätselarbeit.

4.  **Fallback: Verbessern Sie das Logging mit kontextuellen Daten**
    - Falls MDC im Moment zu viel Overhead bedeutet, reichern Sie Ihre Logs an Schlüsselstellen mit mehr Kontext an (z.B. User-ID, Session-ID oder Endpunkt-Name). Beispiel:
      ```java
      logger.info("Button clicked, endpoint=/api/example, user={}", userId);
      ```
    - Kombinieren Sie dies mit `%t` (Thread-Name) und einem engen Zeitbereich, um Logs manuell einzugrenzen. Es ist nicht ideal, funktioniert aber notfalls.

### Warum nicht nur Zeitbereich?
Das Verlassen auf reine Zeitstempel ist fragil, weil:
- Logs von gleichzeitigen Anfragen sich überlappen, besonders in einem ausgelasteten System.
- Die Zeitgenauigkeit (z.B. Millisekunden) möglicherweise nicht ausreicht, um eine einzelne Anfrage zu isolieren.
- Es mühsam ist, Logs über Services oder tiefe Aufrufstapel hinweg zu korrelieren.

### Langfristige Empfehlung
Wenn der Bedarf an Tracing wächst, ziehen Sie in Betracht, die eingebaute Unterstützung von Spring Boot für verteiltes Tracing zu übernehmen (z.B. via Sleuth oder Micrometer mit Zipkin). Sleuth generiert automatisch Trace- und Span-IDs und integriert sich nahtlos mit Log4j, ist aber aufwändiger einzurichten. Im Moment ist MDC ein leichtgewichtiger, effektiver Mittelweg.

### Abschließender Ratschlag
Beginnen Sie mit dem MDC-Ansatz – er ist einfach, nutzt die nativen Fähigkeiten von Log4j und bietet Ihnen eine klare Möglichkeit, Logs an eine vom Frontend initiierte Anfrage zu binden. Sie werden dann etwas wie `[traceId=123e4567-e89b-12d3-a456-426614174000]` in jeder Logzeile für diese Anfrage sehen, was die Suche und Rückverfolgung trivial macht. Lassen Sie mich wissen, wenn Sie Hilfe bei weiteren Anpassungen benötigen!