---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast:free
title: Filtro de Registro de Solicitudes HTTP de Spring Boot
translated: true
type: note
---

A continuación se muestra un ejemplo de cómo implementar un Filtro Servlet personalizado en Spring (por ejemplo, Spring Boot o Spring MVC) para registrar datos estructurados de las solicitudes HTTP entrantes. Este filtro capturará y registrará:

- **Método HTTP**: por ejemplo, GET, POST.
- **Parámetros de Consulta**: Extraídos como un mapa.
- **Cuerpo de la Solicitud**: Para métodos como POST/PUT (nota: el cuerpo es un flujo, por lo que envolvemos la solicitud para leerlo sin consumirlo para el procesamiento posterior).

La salida del registro estará en formato JSON estructurado. Usaremos:
- **SLF4J** para el registro (común en Spring).
- **Jackson** para serializar los datos a JSON (Spring Boot lo incluye por defecto).
- Un `HttpServletRequestWrapper` personalizado para leer el cuerpo de forma segura.

Este filtro se puede registrar globalmente para interceptar todas las solicitudes.

### Paso 1: Dependencias
Si usas Spring Boot, asegúrate de tener esto en tu `pom.xml` (Maven) o `build.gradle` (Gradle):
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <!-- Jackson está incluido, pero explícitamente para mayor claridad -->
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
    </dependency>
</dependencies>
```

### Paso 2: Wrapper de Solicitud Personalizado
Este wrapper permite leer el cuerpo de la solicitud múltiples veces (almacenándolo en caché como una cadena).

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

    // Helper para extraer parámetros de consulta como un mapa
    public Map<String, String[]> getQueryParams() {
        Map<String, String[]> params = new LinkedHashMap<>();
        // Añadir parámetros de la cadena de consulta
        String queryString = getQueryString();
        if (queryString != null) {
            // Análisis simple; para casos complejos, usa bibliotecas como Apache Commons
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
        // Combinar con el mapa de parámetros
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

### Paso 3: El Filtro Personalizado
Este filtro registra los datos estructurados como JSON usando SLF4J. Se aplica a todas las solicitudes.

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

        // Envolver la solicitud solo para métodos que tienen un cuerpo (por ejemplo, POST, PUT)
        ContentCachingRequestWrapper wrappedRequest = null;
        String body = "";
        if ("GET".equalsIgnoreCase(request.getMethod()) == false) {
            wrappedRequest = new ContentCachingRequestWrapper(request);
            body = wrappedRequest.getRequestBodyAsString();
        } else {
            wrappedRequest = new ContentCachingRequestWrapper(request);
        }

        // Construir el mapa de datos estructurados
        Map<String, Object> logData = new HashMap<>();
        logData.put("httpMethod", request.getMethod());
        logData.put("requestUri", request.getRequestURI());
        logData.put("queryParams", wrappedRequest.getQueryParams());
        logData.put("requestBody", body); // Solo no vacío para métodos tipo POST

        // Registrar como JSON
        String jsonLog = objectMapper.writeValueAsString(logData);
        logger.info("Solicitud Entrante: {}", jsonLog);

        // Proceder con la solicitud envuelta
        filterChain.doFilter(wrappedRequest != null ? wrappedRequest : request, response);
    }
}
```

### Paso 4: Registrar el Filtro (Automático en Spring Boot)
En Spring Boot, la anotación `@Component` en el filtro lo registra automáticamente. Si usas Spring MVC plano (sin Boot), puedes registrarlo manualmente:

```java
// En una clase @Configuration
@Bean
public FilterRegistrationBean<LoggingFilter> loggingFilter() {
    FilterRegistrationBean<LoggingFilter> registrationBean = new FilterRegistrationBean<>();
    registrationBean.setFilter(new LoggingFilter());
    registrationBean.addUrlPatterns("/*"); // Aplicar a todas las URLs
    registrationBean.setOrder(1);
    return registrationBean;
}
```

### Ejemplo de Salida del Registro
Cuando llega una solicitud como `POST /api/users` con cuerpo `{"name": "John"}` y consulta `?id=123`, el registro se verá así (asumiendo que tu logger está configurado para salida JSON, por ejemplo, mediante Logback con un appender JSON):

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

- **Configuración del Logger**: Para obtener registros JSON completos, configura Logback (en `logback-spring.xml` o `application.properties`) con un codificador JSON como `net.logstash.logback.encoder.LogstashEncoder`. Por ejemplo, en `application.yml`:
  ```yaml
  logging:
    pattern:
      console: "%msg%n"  # O usa un appender JSON para salida estructurada
  ```

### Notas
- **Limitación de Lectura del Cuerpo**: Solo leemos el cuerpo para métodos no GET. Para GET, está vacío. Esto evita problemas con cuerpos grandes o lecturas múltiples.
- **Seguridad**: Ten cuidado al registrar datos sensibles (por ejemplo, contraseñas en el cuerpo/consulta). Es posible que desees enmascarar campos.
- **Rendimiento**: El almacenamiento en caché del cuerpo usa memoria; para cuerpos muy grandes, considera límites (por ejemplo, leer solo los primeros N bytes).
- **Pruebas**: Añade esto a una aplicación Spring Boot y envía una solicitud POST mediante curl: `curl -X POST http://localhost:8080/api/users?id=123 -d '{"name":"John"}' -H "Content-Type: application/json"`.
- **Alternativas**: Para un registro más avanzado, considera Spring Boot Actuator o bibliotecas como `spring-boot-starter-logging` con registro estructurado.

Este es un punto de partida listo para producción. ¡Personalízalo según sea necesario! Si necesitas más detalles, házmelo saber.