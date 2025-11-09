---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: Spring Boot HTTP-Anforderungsprotokollierungsfilter
translated: true
type: note
---

Hier ist ein Beispiel zur Implementierung eines benutzerdefinierten Servlet-Filters in Spring (z.B. Spring Boot oder Spring MVC), um strukturierte Daten von eingehenden HTTP-Anfragen zu protokollieren. Dieser Filter erfasst und protokolliert:

- **HTTP-Methode**: z.B. GET, POST.
- **Query-Parameter**: Extrahiert als Map.
- **Request Body**: Für Methoden wie POST/PUT (Hinweis: Der Body ist ein Stream, daher wrappen wir die Anfrage, um ihn zu lesen, ohne ihn für die Weiterverarbeitung zu konsumieren).

Die Protokollausgabe erfolgt im strukturierten JSON-Format. Wir verwenden:
- **SLF4J** für die Protokollierung (üblich in Spring).
- **Jackson** zur Serialisierung der Daten in JSON (in Spring Boot standardmäßig enthalten).
- Einen benutzerdefinierten `HttpServletRequestWrapper`, um den Body sicher zu lesen.

Dieser Filter kann global registriert werden, um alle Anfragen abzufangen.

### Schritt 1: Abhängigkeiten
Bei Verwendung von Spring Boot stellen Sie sicher, dass diese in Ihrer `pom.xml` (Maven) oder `build.gradle` (Gradle) vorhanden sind:
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <!-- Jackson ist enthalten, aber explizit für Klarheit -->
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
    </dependency>
</dependencies>
```

### Schritt 2: Benutzerdefinierte Request-Wrapper-Klasse
Dieser Wrapper ermöglicht das mehrfache Lesen des Request-Bodys (durch Zwischenspeicherung als String).

```java
package com.example.filter;

import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.servlet.ReadListener;
import jakarta.servlet.ServletInputStream;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletRequestWrapper;
import org.springframework.util.StreamUtils;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.LinkedHashMap;
import java.util.Map;

public class ContentCachingRequestWrapper extends HttpServletRequestWrapper {
    private final byte[] cachedBody;
    private final ObjectMapper objectMapper = new ObjectMapper();

    public ContentCachingRequestWrapper(HttpServletRequest request) throws IOException {
        super(request);
        InputStream requestInputStream = request.getInputStream();
        this.cachedBody = StreamUtils.copyToByteArray(requestInputStream);
    }

    @Override
    public ServletInputStream getInputStream() throws IOException {
        return new CachedServletInputStream(this.cachedBody);
    }

    @Override
    public BufferedReader getReader() throws IOException {
        byte[] requestBodyBytes = getRequestBody();
        return new BufferedReader(new InputStreamReader(new ByteArrayInputStream(requestBodyBytes),
                StandardCharsets.UTF_8));
    }

    public String getRequestBodyAsString() {
        if (cachedBody.length > 0) {
            return new String(cachedBody, StandardCharsets.UTF_8);
        }
        return "";
    }

    public byte[] getRequestBody() {
        return cachedBody;
    }

    // Hilfsmethode zum Extrahieren der Query-Parameter als Map
    public Map<String, String[]> getQueryParams() {
        Map<String, String[]> params = new LinkedHashMap<>();
        // Query-String-Parameter hinzufügen
        String queryString = getQueryString();
        if (queryString != null) {
            // Einfaches Parsing; für komplexe Fälle Bibliotheken wie Apache Commons verwenden
            String[] pairs = queryString.split("&");
            for (String pair : pairs) {
                String[] keyValue = pair.split("=", 2);
                if (keyValue.length == 2) {
                    params.put(keyValue[0], new String[]{keyValue[1]});
                } else {
                    params.put(keyValue[0], new String[]{});
                }
            }
        }
        // Mit Parameter-Map zusammenführen
        params.putAll(getParameterMap());
        return params;
    }

    private static class CachedServletInputStream extends ServletInputStream {
        private final ByteArrayInputStream cachedBodyInputStream;

        public CachedServletInputStream(byte[] cachedBody) {
            this.cachedBodyInputStream = new ByteArrayInputStream(cachedBody);
        }

        @Override
        public boolean isFinished() {
            return cachedBodyInputStream.available() == 0;
        }

        @Override
        public boolean isReady() {
            return true;
        }

        @Override
        public void setReadListener(ReadListener readListener) {
            throw new UnsupportedOperationException();
        }

        @Override
        public int read() throws IOException {
            return cachedBodyInputStream.read();
        }
    }
}
```

### Schritt 3: Der Benutzerdefinierte Filter
Dieser Filter protokolliert die strukturierten Daten als JSON unter Verwendung von SLF4J. Er wird auf alle Anfragen angewendet.

```java
package com.example.filter;

import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import org.springframework.util.StreamUtils;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

@Component
public class LoggingFilter extends OncePerRequestFilter {

    private static final Logger logger = LoggerFactory.getLogger(LoggingFilter.class);
    private final ObjectMapper objectMapper = new ObjectMapper();

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {

        // Request nur für Methoden mit Body wrappen (z.B. POST, PUT)
        ContentCachingRequestWrapper wrappedRequest = null;
        String body = "";
        if ("GET".equalsIgnoreCase(request.getMethod()) == false) {
            wrappedRequest = new ContentCachingRequestWrapper(request);
            body = wrappedRequest.getRequestBodyAsString();
        } else {
            wrappedRequest = new ContentCachingRequestWrapper(request);
        }

        // Strukturierte Daten-Map aufbauen
        Map<String, Object> logData = new HashMap<>();
        logData.put("httpMethod", request.getMethod());
        logData.put("requestUri", request.getRequestURI());
        logData.put("queryParams", wrappedRequest.getQueryParams());
        logData.put("requestBody", body); // Nur bei POST-ähnlichen Methoden nicht leer

        // Als JSON protokollieren
        String jsonLog = objectMapper.writeValueAsString(logData);
        logger.info("Eingehende Anfrage: {}", jsonLog);

        // Mit dem gewrappten Request fortfahren
        filterChain.doFilter(wrappedRequest != null ? wrappedRequest : request, response);
    }
}
```

### Schritt 4: Filter Registrieren (Automatisch in Spring Boot)
In Spring Boot registriert die `@Component`-Annotation auf dem Filter diesen automatisch. Bei Verwendung von plain Spring MVC (ohne Boot) können Sie ihn manuell registrieren:

```java
// In einer @Configuration-Klasse
@Bean
public FilterRegistrationBean<LoggingFilter> loggingFilter() {
    FilterRegistrationBean<LoggingFilter> registrationBean = new FilterRegistrationBean<>();
    registrationBean.setFilter(new LoggingFilter());
    registrationBean.addUrlPatterns("/*"); // Auf alle URLs anwenden
    registrationBean.setOrder(1);
    return registrationBean;
}
```

### Beispielhafte Protokollausgabe
Wenn eine Anfrage wie `POST /api/users` mit Body `{"name": "John"}` und Query `?id=123` eingeht, sieht die Protokollierung etwa so aus (vorausgesetzt, Ihr Logger ist für JSON-Ausgabe konfiguriert, z.B. über Logback mit JSON-Appender):

```json
{
  "httpMethod": "POST",
  "requestUri": "/api/users",
  "queryParams": {
    "id": ["123"]
  },
  "requestBody": "{\"name\": \"John\"}"
}
```

- **Logger-Konfiguration**: Für vollständige JSON-Logs konfigurieren Sie Logback (in `logback-spring.xml` oder `application.properties`) mit einem JSON-Encoder wie `net.logstash.logback.encoder.LogstashEncoder`. Beispiel in `application.yml`:
  ```yaml
  logging:
    pattern:
      console: "%msg%n"  # Oder verwenden Sie einen JSON-Appender für strukturierte Ausgabe
  ```

### Hinweise
- **Body-Lesebeschränkung**: Wir lesen den Body nur für Nicht-GET-Methoden. Bei GET ist er leer. Dies vermeidet Probleme mit großen Bodys oder mehrfachem Lesen.
- **Sicherheit**: Seien Sie vorsichtig beim Protokollieren sensibler Daten (z.B. Passwörter im Body/Query). Möglicherweise möchten Sie Felder maskieren.
- **Performance**: Das Zwischenspeichern des Bodys verwendet Speicher; für sehr große Bodys sollten Sie Limits in Betracht ziehen (z.B. nur die ersten N Bytes lesen).
- **Testing**: Fügen Sie dies einer Spring-Boot-App hinzu und senden Sie eine POST-Anfrage via curl: `curl -X POST http://localhost:8080/api/users?id=123 -d '{"name":"John"}' -H "Content-Type: application/json"`.
- **Alternativen**: Für erweiterte Protokollierung ziehen Sie Spring Boot Actuator oder Bibliotheken wie `spring-boot-starter-logging` mit strukturierter Protokollierung in Betracht.

Dies ist ein produktionsreifer Ausgangspunkt. Passen Sie ihn nach Bedarf an! Bei weiteren Fragen lassen Sie es mich wissen.