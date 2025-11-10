---
audio: false
generated: true
lang: ar
layout: post
title: إتقان Spring Cloud Sleuth في Spring Boot
translated: true
type: note
---

Spring Cloud Sleuth هو أداة قوية لإضافة إمكانيات التتبع الموزع لتطبيقات Spring. بينما يكون مفيدًا بشكل خاص في بنيات الخدمات المصغرة (microservices) لتتبع الطلبات عبر خدمات متعددة، فإنه يوفر أيضًا فوائد كبيرة للتطبيقات المفردة (monolith) من خلال تعزيز ارتباط السجلات (log correlation) وتصحيح الأخطاء.

سيقدم هذا الدليل نظرة شاملة حول استخدام Spring Cloud Sleuth داخل تطبيق Spring Boot مفرد، مستندًا إلى رؤى من منهجية Baeldung.

## 1. ما هو Spring Cloud Sleuth؟

في جوهره، يقوم Spring Cloud Sleuth بتجهيز تطبيقات Spring لإضافة معلومات التتبع تلقائيًا إلى السجلات ونشرها عبر المكونات المختلفة وحتى الخيوط (threads) داخل التطبيق الواحد. يستخدم مكتبة Brave الخاصة بـ OpenZipkin لهذه الوظيفة.

**المصطلحات الأساسية:**

*   **Trace (التتبع):** يمثل طلبًا فرديًا أو وظيفة تتدفق عبر التطبيق. لكل تتبع `traceId` فريد. فكر فيه على أنه الرحلة من البداية إلى النهاية للطلب.
*   **Span (الامتداد):** يمثل وحدة عمل منطقية داخل التتبع. يتكون التتبع من عدة امتدادات، مشكلة بنية شبيهة بالشجرة. لكل امتداد `spanId` فريد. على سبيل المثال، قد يكون طلب HTTP الوارد امتدادًا واحدًا، واستدعاء طريقة داخل ذلك الطلب قد يكون امتدادًا آخر (فرعيًا).
*   **MDC (سياق التشخيص المعين):** يتكامل Sleuth مع MDC الخاص بـ Slf4J لحقن `traceId` و `spanId` في رسائل السجل الخاصة بك، مما يجعل من السهل تصفية وربط السجلات لطلب معين.

## 2. لماذا استخدام Sleuth في تطبيق مفرد؟

حتى في التطبيق المفرد، غالبًا ما تتضمن الطلبات طبقات متعددة، وعمليات غير متزامنة، وخيوطًا مختلفة. يمكن أن يكون ربط رسائل السجل يدويًا لطلب واحد مملًا وعرضة للخطأ. يقوم Sleuth بأتمتة هذا من خلال:

*   **تبسيط تصحيح الأخطاء:** من خلال إضافة `traceId` و `spanId` إلى كل مدخل في السجل، يمكنك بسهولة تصفية السجلات لرؤية كل ما يتعلق بطلب مستخدم معين، حتى إذا اجتاز طرقًا أو خدمات أو خيوطًا متعددة داخل تطبيقك المفرد.
*   **تحسين إمكانية المراقبة (Observability):** يوفر صورة أوضح لكيفية تدفق الطلب وأين قد تحدث الاختناقات أو المشكلات المحتملة.
*   **الاتساق:** يضمن نهجًا متسقًا لربط السجلات دون الحاجة إلى جهد يدوي في كل جزء من قاعدة التعليمات البرمجية الخاصة بك.

## 3. البدء: الإعداد والتكوين

### 3.1. إعداد المشروع (Maven)

للبدء، قم بإنشاء مشروع Spring Boot جديد (يمكنك استخدام Spring Initializr) وأضف الاعتماد `spring-cloud-starter-sleuth` إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-sleuth</artifactId>
</dependency>
```

**مهم:** تأكد من استخدام إصدار متوافق من Spring Boot و Spring Cloud. عادةً ما تتم إدارة تبعيات Spring Cloud باستخدام Bill of Materials (BOM).

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

استبدل `${spring-cloud.version}` بإصدار قطار الإصدار المناسب (على سبيل المثال، `2021.0.1`، `2022.0.0`).

### 3.2. اسم التطبيق

يوصى بشدة بتعيين اسم تطبيق في ملف `application.properties` أو `application.yml` الخاص بك. سيظهر هذا الاسم في سجلاتك، وهو مفيد لتحديد مصدر السجلات، خاصة إذا انتقلت لاحقًا إلى نظام موزع.

```properties
# application.properties
spring.application.name=my-single-app
```

### 3.3. نمط التسجيل (Logging Pattern)

يقوم Spring Cloud Sleuth تلقائيًا بتعديل نمط التسجيل الافتراضي لتضمين `traceId` و `spanId`. قد يبدو ناتج السجل النموذجي مع Sleuth كالتالي:

```
2025-06-23 23:30:00.123 INFO [my-single-app,a1b2c3d4e5f6a7b8,a1b2c3d4e5f6a7b8,false] 12345 --- [nio-8080-exec-1] c.e.m.MyController : This is a log message.
```

هنا:

*   `my-single-app`: هو `spring.application.name`.
*   `a1b2c3d4e5f6a7b8`: هو `traceId`.
*   `a1b2c3d4e5f6a7b8` (الثاني): هو `spanId` (للامتداد الجذري، غالبًا ما يكون `traceId` و `spanId` متماثلين).
*   `false`: يشير إلى ما إذا كان الامتداد قابلًا للتصدير (true تعني أنه سيتم إرساله إلى جامع التتبع مثل Zipkin).

إذا كان لديك نمط تسجيل مخصص، فستحتاج إلى إضافة `traceId` و `spanId` إليه صراحةً باستخدام `%X{traceId}` و `%X{spanId}` (لـ Logback).

مثال لنمط Logback مخصص في `logback-spring.xml`:

```xml
<appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
        <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level [${spring.application.name:-},%X{traceId:-},%X{spanId:-}] %thread %logger{36} - %msg%n</pattern>
    </encoder>
</appender>
```

## 4. كيف يعمل Sleuth في تطبيق مفرد

بمجرد وجود الاعتماد `spring-cloud-starter-sleuth` في classpath، يأخذ التكوين التلقائي لـ Spring Boot زمام المبادرة.

### 4.1. التجهيز التلقائي (Automatic Instrumentation)

يقوم Sleuth تلقائيًا بتجهيز مكونات Spring الشائعة وقنوات الاتصال:

*   **مرشح Servlet (Servlet Filter):** للطلبات HTTP الواردة إلى وحدات التحكم (controllers) الخاصة بك.
*   **RestTemplate:** للمكالمات HTTP الصادرة التي تتم باستخدام `RestTemplate` (تأكد من أنك تستخدم `RestTemplate` مُدارًا كـ bean حتى يتمكن Sleuth من تجهيزه تلقائيًا).
*   **الإجراءات المجدولة (Scheduled Actions):** للطرق ذات `@Scheduled`.
*   **قنوات الرسائل (Message Channels):** لـ Spring Integration و Spring Cloud Stream.
*   **الطرق غير المتزامنة (Asynchronous Methods):** للطرق ذات `@Async` (يضمن نشر سياق التتبع/الامتداد عبر الخيوط).

### 4.2. مثال على طلب ويب بسيط

فكر في تطبيق Spring Boot بسيط يحتوي على وحدة تحكم REST:

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

عند الوصول إلى `http://localhost:8080/`، سترى رسائل سجل مثل:

```
2025-06-23 23:35:00.123 INFO [my-single-app,c9d0e1f2a3b4c5d6,c9d0e1f2a3b4c5d6,false] 7890 --- [nio-8080-exec-1] c.e.m.MyController : Hello from MyController
```

لاحظ إضافة `traceId` و `spanId` تلقائيًا.

### 4.3. نشر السياق عبر الطرق (نفس الامتداد)

إذا كان طلبك يتدفق عبر عدة طرق داخل التطبيق نفسه وتريد أن تكون هذه الطرق جزءًا من *نفس الامتداد*، فإن Sleuth يتعامل مع هذا تلقائيًا.

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
        Thread.sleep(100); // محاكاة لبعض العمل
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

ستعرض السجلات لـ `/same-span-example` نفس `traceId` و `spanId` لكل من طرق وحدة التحكم والخدمة:

```
2025-06-23 23:40:00.100 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyController : Entering same-span-example endpoint
2025-06-23 23:40:00.200 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyService : Doing some work in MyService
2025-06-23 23:40:00.205 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyController : Exiting same-span-example endpoint
```

### 4.4. إنشاء امتدادات جديدة يدويًا

قد ترغب في إنشاء امتداد جديد لوحدة عمل متميزة داخل تطبيقك، حتى لو كانت جزءًا من نفس التتبع الشامل. يسمح هذا بالتتبع والتوقيت بدقة أعلى. يوفر Spring Cloud Sleuth واجهة برمجة التطبيقات `Tracer` لهذا الغرض.

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
    private Tracer tracer; // حقن Brave Tracer

    public void doSomeWorkNewSpan() throws InterruptedException {
        logger.info("I'm in the original span before new span");

        // إنشاء امتداد جديد باسم وصفي
        Span newSpan = tracer.nextSpan().name("custom-internal-work").start();
        try (Tracer.SpanInScope ws = tracer.withSpanInScope(newSpan)) {
            Thread.sleep(200); // محاكاة لبعض العمل في الامتداد الجديد
            logger.info("I'm in the new custom span doing some cool work");
        } finally {
            newSpan.finish(); // أنهِ الامتداد دائمًا
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

ستعرض السجلات لـ `/new-span-example` بقاء معرف التتبع كما هو، لكن سيظهر `spanId` جديد لـ "custom-internal-work":

```
2025-06-23 23:45:00.100 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyController : Entering new-span-example endpoint
2025-06-23 23:45:00.105 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm in the original span before new span
2025-06-23 23:45:00.300 INFO [my-single-app,f0e1d2c3b4a5f6e7,8a9b0c1d2e3f4a5b,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm in the new custom span doing some cool work
2025-06-23 23:45:00.305 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm back in the original span
2025-06-23 23:45:00.310 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyController : Exiting new-span-example endpoint
```

لاحظ كيف يتغير `spanId` إلى `8a9b0c1d2e3f4a5b` داخل قسم `custom-internal-work` ثم يعود.

### 4.5. المعالجة غير المتزامنة (Asynchronous Processing)

يتكامل Sleuth بسلاسة مع شرح `@Async` الخاص بـ Spring لنشر سياق التتبع عبر حدود الخيوط.

أولاً، قم بتمكين المعالجة غير المتزامنة في فئة التطبيق الرئيسية الخاصة بك:

```java
@SpringBootApplication
@EnableAsync // تمكين التنفيذ غير المتزامن
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

بعد ذلك، قم بإنشاء خدمة غير متزامنة:

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
        Thread.sleep(500); // محاكاة لمهمة طويلة المدى
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

ستظهر السجلات نفس `traceId` ولكن `spanId` مختلف للطريقة غير المتزامنة، حيث تعمل في خيط جديد وتمثل وحدة عمل جديدة:

```
2025-06-23 23:50:00.100 INFO [my-single-app,1a2b3c4d5e6f7a8b,1a2b3c4d5e6f7a8b,false] 1234 --- [nio-8080-exec-4] c.e.m.MyController : Calling async task
2025-06-23 23:50:00.105 INFO [my-single-app,1a2b3c4d5e6f7a8b,9c0d1e2f3a4b5c6d,false] 1234 --- [           task-1] c.e.m.AsyncService : Starting async task
2025-06-23 23:50:00.110 INFO [my-single-app,1a2b3c4d5e6f7a8b,1a2b3c4d5e6f7a8b,false] 1234 --- [nio-8080-exec-4] c.e.m.MyController : Async task initiated, returning from controller
// ... بعد بعض الوقت ...
2025-06-23 23:50:00.605 INFO [my-single-app,1a2b3c4d5e6f7a8b,9c0d1e2f3a4b5c6d,false] 1234 --- [           task-1] c.e.m.AsyncService : Finished async task
```

لاحظ أن `traceId` يظل كما هو، لكن `spanId` يتغير للطريقة غير المتزامنة، واسم الخيط يعكس أيضًا منفذ التنفيذ غير المتزامن (async executor).

### 4.6. تخصيص أسماء الامتدادات باستخدام `@SpanName`

يمكنك استخدام شرح `@SpanName` لتوفير أسماء أكثر معنى للامتدادات التي تم إنشاؤها تلقائيًا في تطبيقك.

```java
import org.springframework.cloud.sleuth.annotation.SpanName;
import org.springframework.stereotype.Service;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Service
public class AnnotatedService {
    private static final Logger logger = LoggerFactory.getLogger(AnnotatedService.class);

    @SpanName("Annotated_Service_Method") // اسم امتداد مخصص
    public void annotatedMethod() throws InterruptedException {
        logger.info("Inside annotated method");
        Thread.sleep(50);
    }
}

// ... في وحدة التحكم أو خدمة أخرى ...
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

ستعكس السجلات اسم الامتداد المخصص:

```
2025-06-23 23:55:00.100 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.MyController : Calling annotated method
2025-06-23 23:55:00.150 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.AnnotatedService : Inside annotated method (span name: Annotated_Service_Method)
2025-06-23 23:55:00.155 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.MyController : Finished calling annotated method
```

## 5. التكامل مع Zipkin (اختياري ولكنه موصى به)

بينما يركز هذا الدليل على التطبيقات المفردة، تظهر القوة الحقيقية لـ Sleuth عند التكامل مع نظام تتبع موزع مثل Zipkin. يقوم Zipkin بجمع بيانات التتبع والامتداد التي يصدرها Sleuth ويوفر واجهة مستخدم لتصور تدفق وتوقيت الطلبات.

للتكامل مع Zipkin، أضف الاعتماد `spring-cloud-starter-zipkin`:

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-zipkin</artifactId>
</dependency>
```

بشكل افتراضي، سيحاول Sleuth إرسال التتبعات إلى جامع Zipkin يعمل على `http://localhost:9411`. يمكنك تكوين هذا في `application.properties`:

```properties
spring.zipkin.base-url=http://localhost:9411
```

يمكنك تشغيل خادم Zipkin بسهولة باستخدام Docker:

```bash
docker run -d -p 9411:9411 openzipkin/zipkin
```

بمجرد تشغيل Zipkin، سيبدأ تطبيق Spring Boot المفرد الخاص بك في إرسال بيانات التتبع تلقائيًا، ويمكنك عرض التتبعات على `http://localhost:9411/`.

## 6. أخذ العينات (Sampling)

بشكل افتراضي، يطبق Sleuth استراتيجية أخذ عينات لتجنب إرباك نظام التتبع بالبيانات. عادةً يأخذ عينة من نسبة مئوية من الطلبات. يمكنك تكوين معدل أخذ العينات في `application.properties`:

```properties
# يأخذ عينات من 100% من الطلبات
spring.sleuth.sampler.probability=1.0
```

قيمة `1.0` تعني أنه سيتم تتبع جميع الطلبات، بينما `0.1` تعني أنه سيتم تتبع 10% منها.

## 7. الخاتمة

يعزز Spring Cloud Sleuth، حتى في التطبيق المفرد، التسجيل وتصحيح الأخطاء بشكل كبير من خلال حقن `traceId` و `spanId` تلقائيًا في رسائل السجل الخاصة بك. هذا يسمح لك بمتابعة تدفق تنفيذ طلب واحد بسهولة، حتى عندما يجتاز طرقًا وخيوطًا مختلفة. من خلال فهم المفاهيم الأساسية للتتبعات والامتدادات واستخدام التجهيز التلقائي لـ Sleuth أو إنشاء الامتدادات يدويًا، يمكنك الحصول على قدرة أفضل لمراقبة تطبيقاتك المفردة. يفتح التكامل مع Zipkin إمكانات إضافية لتصور وتحليل سلوك تطبيقك.