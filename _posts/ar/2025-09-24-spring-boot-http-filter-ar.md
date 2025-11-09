---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast:free
title: مرشح تسجيل طلبات HTTP في Spring Boot
translated: true
type: note
---

فيما يلي مثال حول كيفية تنفيذ مُرشح Servlet مخصص في Spring (مثل Spring Boot أو Spring MVC) لتسجيل البيانات المهيكلة من طلبات HTTP الواردة. سيقوم هذا المُرشح بالتقاط وتسجيل:

-   **طريقة HTTP**: مثل GET أو POST.
-   **معلمات Query**: يتم استخراجها كخريطة.
-   **نص الطلب (Body)**: للطرق مثل POST/PUT (ملاحظة: ال body هو تيار، لذا نقوم بتغليف الطلب لقراءته دون استهلاكه للمعالجة اللاحقة).

سيكون ناتج السجل بتنسيق JSON مهيكل. سنستخدم:
-   **SLF4J** للتسجيل (شائع الاستخدام في Spring).
-   **Jackson** لتحويل البيانات إلى JSON (يدمجه Spring Boot افتراضيًا).
-   `HttpServletRequestWrapper` مخصص لقراءة body الطلب بأمان.

يمكن تسجيل هذا المُرشح globally لاعتراض جميع الطلبات.

### الخطوة 1: التبعيات
إذا كنت تستخدم Spring Boot، تأكد من وجود هذه في ملف `pom.xml` (Maven) أو `build.gradle` (Gradle):

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <!-- Jackson مضمن، ولكن نذكره صراحة للتوضيح -->
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
    </dependency>
</dependencies>
```

### الخطوة 2: غلاف الطلب المخصص (Custom Request Wrapper)
يسمح هذا الغلاف بقراءة body الطلب عدة مرات (عن طريق تخزينه مؤقتًا كسلسلة نصية string).

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

    // مساعد لاستخراج معلمات query كخريطة
    public Map<String, String[]> getQueryParams() {
        Map<String, String[]> params = new LinkedHashMap<>();
        // إضافة معلمات query string
        String queryString = getQueryString();
        if (queryString != null) {
            // تحليل بسيط؛ للحالات المعقدة، استخدم مكتبات مثل Apache Commons
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
        // الدمج مع خريطة المعلمات
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

### الخطوة 3: المُرشح المخصص
يقوم هذا المُرشح بتسجيل البيانات المهيكلة كـ JSON باستخدام SLF4J. يتم تطبيقه على جميع الطلبات.

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

        // لف الطلب فقط للطرق التي تحتوي على body (مثل POST, PUT)
        ContentCachingRequestWrapper wrappedRequest = null;
        String body = "";
        if ("GET".equalsIgnoreCase(request.getMethod()) == false) {
            wrappedRequest = new ContentCachingRequestWrapper(request);
            body = wrappedRequest.getRequestBodyAsString();
        } else {
            wrappedRequest = new ContentCachingRequestWrapper(request);
        }

        // بناء خريطة البيانات المهيكلة
        Map<String, Object> logData = new HashMap<>();
        logData.put("httpMethod", request.getMethod());
        logData.put("requestUri", request.getRequestURI());
        logData.put("queryParams", wrappedRequest.getQueryParams());
        logData.put("requestBody", body); // تكون غير فارغة فقط لطرق مثل POST

        // التسجيل كـ JSON
        String jsonLog = objectMapper.writeValueAsString(logData);
        logger.info("Incoming Request: {}", jsonLog);

        // المتابعة مع الطلب المغلف
        filterChain.doFilter(wrappedRequest != null ? wrappedRequest : request, response);
    }
}
```

### الخطوة 4: تسجيل المُرشح (تلقائي في Spring Boot)
في Spring Boot، تسجل annotation `@Component` على المُرشح تلقائيًا. إذا كنت تستخدم Spring MVC عادي (وليس Boot)، يمكنك تسجيله يدويًا:

```java
// في فصل مُعطى بـ @Configuration
@Bean
public FilterRegistrationBean<LoggingFilter> loggingFilter() {
    FilterRegistrationBean<LoggingFilter> registrationBean = new FilterRegistrationBean<>();
    registrationBean.setFilter(new LoggingFilter());
    registrationBean.addUrlPatterns("/*"); // تطبيق على جميع الـ URLs
    registrationBean.setOrder(1);
    return registrationBean;
}
```

### مثال على ناتج السجل
عند وصول طلب مثل `POST /api/users` مع body `{"name": "John"}` و query `?id=123`، سيبدو السجل كما يلي (بافتراض أن إعدادات المسجل logger مُهيأة لناتج JSON، على سبيل المثال عبر Logback مع JSON appender):

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

-   **إعدادات المسجل (Logger Configuration)**: للحصول على سجلات JSON كاملة، قم بتهيئة Logback (في `logback-spring.xml` أو `application.properties`) مع مشفر JSON مثل `net.logstash.logback.encoder.LogstashEncoder`. على سبيل المثال، في `application.yml`:

    ```yaml
    logging:
      pattern:
        console: "%msg%n"  # أو استخدم JSON appender للناتج المهيكل
    ```

### ملاحظات
-   **قيود قراءة Body**: نقرأ body فقط لطرق غير GET. بالنسبة لـ GET، يكون فارغًا. هذا يتجنب مشاكل الـ bodies الكبيرة أو القراءات المتعددة.
-   **الأمان**: كن حذرًا عند تسجيل البيانات الحساسة (مثل كلمات المرور في body أو query). قد ترغب في إخفاء بعض الحقول.
-   **الأداء**: يؤدي تخزين body مؤقتًا إلى استخدام الذاكرة؛ بالنسبة لـ bodies كبيرة جدًا، ضع في اعتبارك وضع حدود (مثل قراءة أول N بايت فقط).
-   **الاختبار**: أضف هذا إلى تطبيق Spring Boot وأرسل طلب POST عبر curl: `curl -X POST http://localhost:8080/api/users?id=123 -d '{"name":"John"}' -H "Content-Type: application/json"`.
-   **بدائل**: للتسجيل المتقدم، فكر في استخدام Spring Boot Actuator أو مكتبات مثل `spring-boot-starter-logging` مع التسجيل المهيكل.

هذه نقطة بداية جاهزة للإنتاج. قم بالتخصيص حسب الحاجة! إذا كنت بحاجة إلى مزيد من التفاصيل، دعني أعلم.