---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग बूट में स्प्रिंग क्लाउड स्लूथ में महारत हासिल करना
translated: true
type: note
---

Spring Cloud Sleuth Spring एप्लिकेशन में distributed tracing क्षमताएँ जोड़ने के लिए एक शक्तिशाली टूल है। हालांकि यह माइक्रोसर्विस आर्किटेक्चर में कई सेवाओं में requests को ट्रैक करने के लिए विशेष रूप से उपयोगी है, यह लॉग correlation और डीबगिंग को बेहतर बनाकर single (monolith) एप्लिकेशन के लिए भी महत्वपूर्ण लाभ प्रदान करता है।

यह गाइड Baeldung के approach से insights लेते हुए, एक single Spring Boot एप्लिकेशन के भीतर Spring Cloud Sleuth का उपयोग करने का एक व्यापक अवलोकन प्रदान करेगी।

## 1. Spring Cloud Sleuth क्या है?

इसके मूल में, Spring Cloud Sleuth, Spring एप्लिकेशन को automatically tracing information को लॉग में जोड़ने और इसे एक ही एप्लिकेशन के भीतर विभिन्न components और यहां तक कि threads में propagate करने के लिए instrument करता है। यह इस functionality के लिए OpenZipkin की Brave लाइब्रेरी का लाभ उठाता है।

**मुख्य शब्दावली:**

*   **Trace:** एप्लिकेशन के माध्यम से प्रवाहित होने वाली एक single request या job को दर्शाता है। प्रत्येक trace का एक अद्वितीय `traceId` होता है। इसे किसी request की end-to-end journey के रूप में सोचें।
*   **Span:** एक trace के भीतर कार्य की एक logical unit को दर्शाता है। एक trace कई spans से बना होता है, जो एक tree जैसी संरचना बनाता है। प्रत्येक span का एक अद्वितीय `spanId` होता है। उदाहरण के लिए, एक incoming HTTP request एक span हो सकती है, और उस request के भीतर एक method call दूसरा (child) span हो सकता है।
*   **MDC (Mapped Diagnostic Context):** Sleuth, किसी specific request के लिए लॉग को filter और correlate करना आसान बनाने के लिए, आपके log messages में `traceId` और `spanId` inject करने के लिए Slf4J के MDC के साथ integrate करता है।

## 2. Single एप्लिकेशन में Sleuth का उपयोग क्यों करें?

एक monolith में भी, requests में अक्सर multiple layers, asynchronous operations और different threads शामिल होते हैं। किसी single request के लिए log messages को manually correlate करना थकाऊ और error-prone हो सकता है। Sleuth इसे निम्नलिखित तरीके से automate करता है:

*   **डीबगिंग को सरल बनाना:** प्रत्येक log entry में `traceId` और `spanId` जोड़कर, आप आसानी से लॉग को filter कर सकते हैं ताकि किसी specific user request से संबंधित सब कुछ देख सकें, भले ही वह आपके single एप्लिकेशन के भीतर multiple methods, services, या threads से होकर गुजरता हो।
*   **बेहतर Observability:** यह request के प्रवाह और संभावित bottlenecks या issues के होने की जगह की स्पष्ट तस्वीर प्रदान करता है।
*   **Consistency:** आपके codebase के हर हिस्से में manual effort की आवश्यकता के बिना logging correlation के लिए एक consistent approach सुनिश्चित करता है।

## 3. प्रारंभ करना: सेटअप और कॉन्फ़िगरेशन

### 3.1. प्रोजेक्ट सेटअप (Maven)

शुरुआत करने के लिए, एक नया Spring Boot प्रोजेक्ट बनाएं (आप Spring Initializr का उपयोग कर सकते हैं) और अपनी `pom.xml` में `spring-cloud-starter-sleuth` dependency जोड़ें:

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-sleuth</artifactId>
</dependency>
```

**महत्वपूर्ण:** सुनिश्चित करें कि आप एक compatible Spring Boot और Spring Cloud version का उपयोग कर रहे हैं। Spring Cloud dependencies को आमतौर पर एक Bill of Materials (BOM) का उपयोग करके manage किया जाता है।

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

`${spring-cloud.version}` को appropriate release train version (जैसे, `2021.0.1`, `2022.0.0`) से बदलें।

### 3.2. एप्लिकेशन नाम

अपनी `application.properties` या `application.yml` फ़ाइल में एक एप्लिकेशन नाम सेट करने की अत्यधिक अनुशंसा की जाती है। यह नाम आपके लॉग में दिखाई देगा, जो logs के स्रोत की पहचान करने में मददगार है, खासकर यदि आप बाद में distributed system पर चले जाते हैं।

```properties
# application.properties
spring.application.name=my-single-app
```

### 3.3. लॉगिंग पैटर्न

Spring Cloud Sleuth स्वचालित रूप से `traceId` और `spanId` को शामिल करने के लिए डिफ़ॉल्ट लॉगिंग पैटर्न को संशोधित करता है। Sleuth के साथ एक typical लॉग आउटपुट इस तरह दिख सकता है:

```
2025-06-23 23:30:00.123 INFO [my-single-app,a1b2c3d4e5f6a7b8,a1b2c3d4e5f6a7b8,false] 12345 --- [nio-8080-exec-1] c.e.m.MyController : This is a log message.
```

यहाँ:

*   `my-single-app`: `spring.application.name` है।
*   `a1b2c3d4e5f6a7b8`: `traceId` है।
*   `a1b2c3d4e5f6a7b8` (दूसरा वाला): `spanId` है (root span के लिए, traceId और spanId अक्सर एक ही होते हैं)।
*   `false`: इंगित करता है कि क्या span exportable है (true का मतलब है कि इसे Zipkin जैसे tracing collector पर भेजा जाएगा)।

यदि आपके पास एक custom logging pattern है, तो आपको `%X{traceId}` और `%X{spanId}` (Logback के लिए) का उपयोग करके इसे explicitly अपने pattern में जोड़ना होगा।

`logback-spring.xml` में custom Logback pattern का उदाहरण:

```xml
<appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
        <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level [${spring.application.name:-},%X{traceId:-},%X{spanId:-}] %thread %logger{36} - %msg%n</pattern>
    </encoder>
</appender>
```

## 4. एक Single एप्लिकेशन में Sleuth कैसे काम करता है

एक बार `spring-cloud-starter-sleuth` dependency classpath पर हो जाने के बाद, Spring Boot की auto-configuration काम संभाल लेती है।

### 4.1. स्वचालित इंस्ट्रुमेंटेशन

Sleuth सामान्य Spring components और communication channels को स्वचालित रूप से instrument करता है:

*   **Servlet Filter:** आपके controllers के लिए incoming HTTP requests के लिए।
*   **RestTemplate:** `RestTemplate` का उपयोग करके किए गए outgoing HTTP calls के लिए (सुनिश्चित करें कि Sleuth द्वारा इसे auto-instrument करने के लिए आप एक bean-managed `RestTemplate` का उपयोग कर रहे हैं)।
*   **Scheduled Actions:** `@Scheduled` methods के लिए।
*   **Message Channels:** Spring Integration और Spring Cloud Stream के लिए।
*   **Asynchronous Methods:** `@Async` methods के लिए (यह सुनिश्चित करता है कि trace/span context threads में propagate हो)।

### 4.2. सरल वेब रिक्वेस्ट उदाहरण

एक साधारण REST controller वाले सरल Spring Boot एप्लिकेशन पर विचार करें:

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

जब आप `http://localhost:8080/` एक्सेस करेंगे, तो आपको इस तरह के लॉग संदेश दिखाई देंगे:

```
2025-06-23 23:35:00.123 INFO [my-single-app,c9d0e1f2a3b4c5d6,c9d0e1f2a3b4c5d6,false] 7890 --- [nio-8080-exec-1] c.e.m.MyController : Hello from MyController
```

स्वचालित रूप से जोड़े गए `traceId` और `spanId` पर ध्यान दें।

### 4.3. Methods में Context को Propagate करना (Same Span)

यदि आपकी request एक ही एप्लिकेशन के भीतर multiple methods से होकर गुजरती है और आप चाहते हैं कि ये methods *same span* का हिस्सा हों, तो Sleuth इसे automatically handle करता है।

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
        Thread.sleep(100); // कुछ कार्य का अनुकरण करें
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

`/same-span-example` के लिए लॉग controller और service methods दोनों के लिए समान `traceId` और `spanId` दिखाएंगे:

```
2025-06-23 23:40:00.100 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyController : Entering same-span-example endpoint
2025-06-23 23:40:00.200 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyService : Doing some work in MyService
2025-06-23 23:40:00.205 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyController : Exiting same-span-example endpoint
```

### 4.4. मैन्युअल रूप से नए Spans बनाना

आप अपने एप्लिकेशन के भीतर कार्य की एक distinct unit के लिए एक नया span बनाना चाह सकते हैं, भले ही वह समग्र trace का हिस्सा हो। यह finer-grained tracking और timing की अनुमति देता है। Spring Cloud Sleuth इसके लिए `Tracer` API प्रदान करता है।

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
    private Tracer tracer; // Brave Tracer को Inject करें

    public void doSomeWorkNewSpan() throws InterruptedException {
        logger.info("I'm in the original span before new span");

        // एक descriptive name के साथ एक नया span बनाएं
        Span newSpan = tracer.nextSpan().name("custom-internal-work").start();
        try (Tracer.SpanInScope ws = tracer.withSpanInScope(newSpan)) {
            Thread.sleep(200); // नए span में कुछ कार्य का अनुकरण करें
            logger.info("I'm in the new custom span doing some cool work");
        } finally {
            newSpan.finish(); // Span को हमेशा finish करें
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

`/new-span-example` के लिए लॉग trace ID को समान रखते हुए दिखाएंगे, लेकिन "custom-internal-work" के लिए एक नया `spanId` दिखाई देगा:

```
2025-06-23 23:45:00.100 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyController : Entering new-span-example endpoint
2025-06-23 23:45:00.105 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm in the original span before new span
2025-06-23 23:45:00.300 INFO [my-single-app,f0e1d2c3b4a5f6e7,8a9b0c1d2e3f4a5b,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm in the new custom span doing some cool work
2025-06-23 23:45:00.305 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm back in the original span
2025-06-23 23:45:00.310 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyController : Exiting new-span-example endpoint
```

ध्यान दें कि `spanId` `custom-internal-work` सेक्शन के भीतर `8a9b0c1d2e3f4a5b` में कैसे बदल जाता है और फिर वापस आ जाता है।

### 4.5. अतुल्यकालिक प्रसंस्करण (Asynchronous Processing)

Sleuth, trace context को thread boundaries में propagate करने के लिए Spring के `@Async` annotation के साथ seamlessly integrate करता है।

सबसे पहले, अपनी main एप्लिकेशन क्लास में asynchronous processing को enable करें:

```java
@SpringBootApplication
@EnableAsync // Async execution को enable करें
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

फिर, एक async service बनाएं:

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
        Thread.sleep(500); // कुछ long-running task का अनुकरण करें
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

लॉग asynchronous method के लिए समान `traceId` लेकिन एक अलग `spanId` दिखाएंगे, क्योंकि यह एक नए thread में चलता है और कार्य की एक नई unit का प्रतिनिधित्व करता है:

```
2025-06-23 23:50:00.100 INFO [my-single-app,1a2b3c4d5e6f7a8b,1a2b3c4d5e6f7a8b,false] 1234 --- [nio-8080-exec-4] c.e.m.MyController : Calling async task
2025-06-23 23:50:00.105 INFO [my-single-app,1a2b3c4d5e6f7a8b,9c0d1e2f3a4b5c6d,false] 1234 --- [           task-1] c.e.m.AsyncService : Starting async task
2025-06-23 23:50:00.110 INFO [my-single-app,1a2b3c4d5e6f7a8b,1a2b3c4d5e6f7a8b,false] 1234 --- [nio-8080-exec-4] c.e.m.MyController : Async task initiated, returning from controller
// ... कुछ समय बाद ...
2025-06-23 23:50:00.605 INFO [my-single-app,1a2b3c4d5e6f7a8b,9c0d1e2f3a4b5c6d,false] 1234 --- [           task-1] c.e.m.AsyncService : Finished async task
```

ध्यान दें कि `traceId` वही रहता है, लेकिन async method के लिए `spanId` बदल जाता है, और thread name भी async executor को reflect करता है।

### 4.6. `@SpanName` के साथ Span Names को Customize करना

आप अपने automatically generated spans के लिए अधिक meaningful names प्रदान करने के लिए `@SpanName` annotation का उपयोग कर सकते हैं।

```java
import org.springframework.cloud.sleuth.annotation.SpanName;
import org.springframework.stereotype.Service;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Service
public class AnnotatedService {
    private static final Logger logger = LoggerFactory.getLogger(AnnotatedService.class);

    @SpanName("Annotated_Service_Method") // Custom span name
    public void annotatedMethod() throws InterruptedException {
        logger.info("Inside annotated method");
        Thread.sleep(50);
    }
}

// ... आपके controller या किसी अन्य service में ...
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

लॉग custom span name को reflect करेंगे:

```
2025-06-23 23:55:00.100 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.MyController : Calling annotated method
2025-06-23 23:55:00.150 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.AnnotatedService : Inside annotated method (span name: Annotated_Service_Method)
2025-06-23 23:55:00.155 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.MyController : Finished calling annotated method
```

## 5. Zipkin के साथ एकीकरण (वैकल्पिक लेकिन अनुशंसित)

हालांकि यह गाइड single एप्लिकेशन पर केंद्रित है, Sleuth की वास्तविक शक्ति तब सामने आती है जब यह Zipkin जैसी distributed tracing system के साथ integrated होती है। Zipkin, Sleuth द्वारा export किए गए trace और span डेटा को collect करती है और requests के प्रवाह और timing को visualize करने के लिए एक UI प्रदान करती है।

Zipkin के साथ integrate करने के लिए, `spring-cloud-starter-zipkin` dependency जोड़ें:

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-zipkin</artifactId>
</dependency>
```

डिफ़ॉल्ट रूप से, Sleuth `http://localhost:9411` पर चल रहे Zipkin collector को traces भेजने का प्रयास करेगा। आप इसे `application.properties` में configure कर सकते हैं:

```properties
spring.zipkin.base-url=http://localhost:9411
```

आप Docker के साथ आसानी से एक Zipkin सर्वर चला सकते हैं:

```bash
docker run -d -p 9411:9411 openzipkin/zipkin
```

एक बार Zipkin चलने के बाद, आपका single Spring Boot एप्लिकेशन automatically अपना trace डेटा भेज देगा, और आप traces को `http://localhost:9411/` पर देख सकते हैं।

## 6. सैंपलिंग

डिफ़ॉल्ट रूप से, Sleuth डेटा से tracing system को overwhelm होने से बचाने के लिए एक sampling strategy लागू करता है। यह आमतौर पर requests का एक percentage sample करता है। आप `application.properties` में sampling rate configure कर सकते हैं:

```properties
# 100% requests को sample करता है
spring.sleuth.sampler.probability=1.0
```

`1.0` का मान means सभी requests का trace किया जाएगा, जबकि `0.1` का मतलब है कि 10% का trace किया जाएगा।

## 7. निष्कर्ष

Spring Cloud Sleuth, एक single एप्लिकेशन में भी, आपके log messages में automatically `traceId` और `spanId` inject करके logging और debugging को काफी बढ़ाता है। यह आपको किसी single request के execution flow को आसानी से follow करने की अनुमति देता है, भले ही वह different methods और threads से होकर गुजरता हो। Traces और spans की core concepts को समझकर और Sleuth के automatic instrumentation या manual span creation का उपयोग करके, आप अपने monolithic एप्लिकेशन में बहुत बेहतर observability प्राप्त कर सकते हैं। Zipkin के साथ integrating आपके एप्लिकेशन के behavior की visualization और analysis की क्षमता को और अधिक unlock करती है।