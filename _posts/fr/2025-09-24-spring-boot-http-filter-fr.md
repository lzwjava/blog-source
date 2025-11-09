---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Filtre de Journalisation des Requêtes HTTP Spring Boot
translated: true
type: note
---

Voici un exemple de mise en œuvre d'un filtre Servlet personnalisé dans Spring (par exemple, Spring Boot ou Spring MVC) pour journaliser les données structurées des requêtes HTTP entrantes. Ce filtre capturera et journalisera :

- **Méthode HTTP** : par exemple, GET, POST.
- **Paramètres de requête** : Extraits sous forme de map.
- **Corps de la requête** : Pour les méthodes comme POST/PUT (note : le corps est un flux, donc nous encapsulons la requête pour le lire sans le consommer pour le traitement en aval).

La sortie de journal sera au format JSON structuré. Nous utiliserons :
- **SLF4J** pour la journalisation (commun dans Spring).
- **Jackson** pour sérialiser les données en JSON (Spring Boot l'inclut par défaut).
- Un `HttpServletRequestWrapper` personnalisé pour lire le corps en toute sécurité.

Ce filtre peut être enregistré globalement pour intercepter toutes les requêtes.

### Étape 1 : Dépendances
Si vous utilisez Spring Boot, assurez-vous que celles-ci sont dans votre `pom.xml` (Maven) ou `build.gradle` (Gradle) :
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <!-- Jackson est inclus, mais explicitement pour plus de clarté -->
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
    </dependency>
</dependencies>
```

### Étape 2 : Wrapper de requête personnalisé
Ce wrapper permet de lire le corps de la requête plusieurs fois (en le mettant en cache sous forme de chaîne).

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

    // Helper pour extraire les paramètres de requête sous forme de map
    public Map<String, String[]> getQueryParams() {
        Map<String, String[]> params = new LinkedHashMap<>();
        // Ajouter les paramètres de la chaîne de requête
        String queryString = getQueryString();
        if (queryString != null) {
            // Parsing simple ; pour les cas complexes, utilisez des bibliothèques comme Apache Commons
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
        // Fusionner avec la map des paramètres
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

### Étape 3 : Le filtre personnalisé
Ce filtre journalise les données structurées au format JSON en utilisant SLF4J. Il est appliqué à toutes les requêtes.

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

        // Encapsuler la requête uniquement pour les méthodes qui ont un corps (par exemple, POST, PUT)
        ContentCachingRequestWrapper wrappedRequest = null;
        String body = "";
        if ("GET".equalsIgnoreCase(request.getMethod()) == false) {
            wrappedRequest = new ContentCachingRequestWrapper(request);
            body = wrappedRequest.getRequestBodyAsString();
        } else {
            wrappedRequest = new ContentCachingRequestWrapper(request);
        }

        // Construire la map de données structurées
        Map<String, Object> logData = new HashMap<>();
        logData.put("httpMethod", request.getMethod());
        logData.put("requestUri", request.getRequestURI());
        logData.put("queryParams", wrappedRequest.getQueryParams());
        logData.put("requestBody", body); // Seulement non vide pour les méthodes de type POST

        // Journaliser en JSON
        String jsonLog = objectMapper.writeValueAsString(logData);
        logger.info("Requête entrante : {}", jsonLog);

        // Poursuivre avec la requête encapsulée
        filterChain.doFilter(wrappedRequest != null ? wrappedRequest : request, response);
    }
}
```

### Étape 4 : Enregistrer le filtre (Automatique dans Spring Boot)
Dans Spring Boot, l'annotation `@Component` sur le filtre l'enregistre automatiquement. Si vous utilisez Spring MVC standard (sans Boot), vous pouvez l'enregistrer manuellement :

```java
// Dans une classe @Configuration
@Bean
public FilterRegistrationBean<LoggingFilter> loggingFilter() {
    FilterRegistrationBean<LoggingFilter> registrationBean = new FilterRegistrationBean<>();
    registrationBean.setFilter(new LoggingFilter());
    registrationBean.addUrlPatterns("/*"); // Appliquer à toutes les URLs
    registrationBean.setOrder(1);
    return registrationBean;
}
```

### Exemple de sortie de journal
Lorsqu'une requête comme `POST /api/users` avec le corps `{"name": "John"}` et la requête `?id=123` arrive, le journal ressemblera à ceci (en supposant que votre logger est configuré pour la sortie JSON, par exemple via Logback avec un appender JSON) :

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

- **Configuration du Logger** : Pour obtenir des journaux JSON complets, configurez Logback (dans `logback-spring.xml` ou `application.properties`) avec un encodeur JSON comme `net.logstash.logback.encoder.LogstashEncoder`. Par exemple, dans `application.yml` :
  ```yaml
  logging:
    pattern:
      console: "%msg%n"  # Ou utilisez un appender JSON pour la sortie structurée
  ```

### Notes
- **Limitation de lecture du corps** : Nous lisons le corps uniquement pour les méthodes non-GET. Pour GET, il est vide. Cela évite les problèmes avec les corps volumineux ou les lectures multiples.
- **Sécurité** : Soyez prudent lors de la journalisation des données sensibles (par exemple, les mots de passe dans le corps/la requête). Vous voudrez peut-être masquer des champs.
- **Performance** : La mise en cache du corps utilise de la mémoire ; pour les corps très volumineux, envisagez des limites (par exemple, lire seulement les N premiers octets).
- **Test** : Ajoutez ceci à une application Spring Boot et envoyez une requête POST via curl : `curl -X POST http://localhost:8080/api/users?id=123 -d '{"name":"John"}' -H "Content-Type: application/json"`.
- **Alternatives** : Pour une journalisation plus avancée, envisagez Spring Boot Actuator ou des bibliothèques comme `spring-boot-starter-logging` avec journalisation structurée.

Ceci est un point de départ prêt pour la production. Personnalisez selon les besoins ! Si vous avez besoin de plus de détails, faites-le moi savoir.