---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast:free
title: स्प्रिंग बूट एचटीटीपी अनुरोध लॉगिंग फ़िल्टर
translated: true
type: note
---

नीचे एक उदाहरण दिया गया है कि कैसे Spring (जैसे, Spring Boot या Spring MVC) में आने वाले HTTP अनुरोधों से संरचित डेटा लॉग करने के लिए एक कस्टम Servlet Filter लागू किया जाए। यह फ़िल्टर कैप्चर और लॉग करेगा:

- **HTTP Method**: जैसे, GET, POST.
- **Query Parameters**: एक मैप के रूप में निकाले गए।
- **Request Body**: POST/PUT जैसी विधियों के लिए (ध्यान दें: बॉडी एक स्ट्रीम है, इसलिए हम अनुरोध को रैप करते हैं ताकि इसे डाउनस्ट्रीम प्रोसेसिंग के लिए उपभोग किए बिना पढ़ा जा सके)।

लॉग आउटपुट संरचित JSON प्रारूप में होगा। हम उपयोग करेंगे:
- **SLF4J** लॉगिंग के लिए (Spring में आम)।
- **Jackson** डेटा को JSON में क्रमबद्ध करने के लिए (Spring Boot इसे डिफ़ॉल्ट रूप से शामिल करता है)।
- बॉडी को सुरक्षित रूप से पढ़ने के लिए एक कस्टम `HttpServletRequestWrapper`।

इस फ़िल्टर को सभी अनुरोधों को इंटरसेप्ट करने के लिए वैश्विक रूप से पंजीकृत किया जा सकता है।

### चरण 1: निर्भरताएँ
यदि Spring Boot का उपयोग कर रहे हैं, तो सुनिश्चित करें कि ये आपके `pom.xml` (Maven) या `build.gradle` (Gradle) में हैं:
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <!-- Jackson शामिल है, लेकिन स्पष्टता के लिए स्पष्ट रूप से -->
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
    </dependency>
</dependencies>
```

### चरण 2: कस्टम अनुरोध रैपर
यह रैपर अनुरोध बॉडी को कई बार पढ़ने की अनुमति देता है (इसे एक स्ट्रिंग के रूप में कैश करके)।

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

    // Helper to extract query params as a map
    public Map<String, String[]> getQueryParams() {
        Map<String, String[]> params = new LinkedHashMap<>();
        // Add query string params
        String queryString = getQueryString();
        if (queryString != null) {
            // Simple parsing; for complex cases, use libraries like Apache Commons
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
        // Merge with parameter map
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

### चरण 3: कस्टम फ़िल्टर
यह फ़िल्टर SLF4J का उपयोग करके संरचित डेटा को JSON के रूप में लॉग करता है। यह सभी अनुरोधों पर लागू होता है।

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

        // Wrap the request only for methods that have a body (e.g., POST, PUT)
        ContentCachingRequestWrapper wrappedRequest = null;
        String body = "";
        if ("GET".equalsIgnoreCase(request.getMethod()) == false) {
            wrappedRequest = new ContentCachingRequestWrapper(request);
            body = wrappedRequest.getRequestBodyAsString();
        } else {
            wrappedRequest = new ContentCachingRequestWrapper(request);
        }

        // Build structured data map
        Map<String, Object> logData = new HashMap<>();
        logData.put("httpMethod", request.getMethod());
        logData.put("requestUri", request.getRequestURI());
        logData.put("queryParams", wrappedRequest.getQueryParams());
        logData.put("requestBody", body); // Only non-empty for POST-like methods

        // Log as JSON
        String jsonLog = objectMapper.writeValueAsString(logData);
        logger.info("Incoming Request: {}", jsonLog);

        // Proceed with the wrapped request
        filterChain.doFilter(wrappedRequest != null ? wrappedRequest : request, response);
    }
}
```

### चरण 4: फ़िल्टर पंजीकृत करें (Spring Boot में स्वचालित)
Spring Boot में, फ़िल्टर पर `@Component` एनोटेशन इसे स्वचालित रूप से पंजीकृत कर देता है। यदि आप सादे Spring MVC (Boot नहीं) का उपयोग कर रहे हैं, तो आप इसे मैन्युअल रूप से पंजीकृत कर सकते हैं:

```java
// In a @Configuration class
@Bean
public FilterRegistrationBean<LoggingFilter> loggingFilter() {
    FilterRegistrationBean<LoggingFilter> registrationBean = new FilterRegistrationBean<>();
    registrationBean.setFilter(new LoggingFilter());
    registrationBean.addUrlPatterns("/*"); // Apply to all URLs
    registrationBean.setOrder(1);
    return registrationBean;
}
```

### उदाहरण लॉग आउटपुट
जब `POST /api/users` जैसा अनुरोध बॉडी `{"name": "John"}` और क्वेरी `?id=123` के साथ आता है, तो लॉग कुछ इस तरह दिखेगा (यह मानते हुए कि आपका लॉगर JSON आउटपुट के लिए कॉन्फ़िगर किया गया है, जैसे कि Logback with JSON appender के साथ):

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

- **Logger Configuration**: पूर्ण JSON लॉग प्राप्त करने के लिए, Logback ( `logback-spring.xml` या `application.properties` में) को `net.logstash.logback.encoder.LogstashEncoder` जैसे JSON एनकोडर के साथ कॉन्फ़िगर करें। उदाहरण के लिए, `application.yml` में:
  ```yaml
  logging:
    pattern:
      console: "%msg%n"  # या संरचित आउटपुट के लिए JSON appender का उपयोग करें
  ```

### नोट्स
- **Body Reading Limitation**: हम बॉडी को केवल गैर-GET विधियों के लिए पढ़ते हैं। GET के लिए, यह खाली है। यह बड़ी बॉडी या एकाधिक रीड के मुद्दों से बचाता है।
- **Security**: संवेदनशील डेटा (जैसे बॉडी/क्वेरी में पासवर्ड) लॉग करते समय सावधान रहें। आप फ़ील्ड्स को मास्क करना चाह सकते हैं।
- **Performance**: बॉडी को कैश करने से मेमोरी का उपयोग होता है; बहुत बड़ी बॉडी के लिए, सीमा पर विचार करें (जैसे, केवल पहले N बाइट्स पढ़ें)।
- **Testing**: इसे एक Spring Boot ऐप में जोड़ें और curl के माध्यम से एक POST अनुरोध भेजें: `curl -X POST http://localhost:8080/api/users?id=123 -d '{"name":"John"}' -H "Content-Type: application/json"`।
- **Alternatives**: अधिक उन्नत लॉगिंग के लिए, Spring Boot Actuator या `spring-boot-starter-logging` जैसी लाइब्रेरीज को संरचित लॉगिंग के साथ विचार करें।

यह एक प्रोडक्शन-रेडी शुरुआती बिंदु है। आवश्यकतानुसार अनुकूलित करें! यदि आपको अधिक विवरण की आवश्यकता है, तो मुझे बताएं।