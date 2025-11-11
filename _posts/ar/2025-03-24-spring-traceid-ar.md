---
audio: false
generated: true
lang: ar
layout: post
title: تتبع طلبات Spring Boot Log4j
translated: true
type: note
---

في تطبيق Java Spring Boot الذي يستخدم Log4j بدون تصميم مُضمّن لمعرف التتبع (trace ID)، فإن تتبع إدخال سجل محدد إلى طلب بدأ من الواجهة الأمامية يمكن أن يكون بالفعل تحديًا. أنت محق في أن `%t` (اسم الموضوع) في Log4j يمكن أن يساعد في تحديد السجلات المرتبطة بموضوع معين، ولكن كما لاحظت، يصبح هذا أقل موثوقية عندما تمتد الطلبات عبر مواضيع متعددة (على سبيل المثال، due to async processing, thread pools, or downstream calls). استخدام نطاق زمني للبحث في السجلات هو حل بديل، ولكنه غير دقيق ومُتعِب، خاصة في الأنظمة ذات الحركة المرورية العالية. دعنا نستكشف بعض النصائح العملية لتحسين هذا الوضع دون الحاجة إلى إعادة هيكلة الإعداد بالكامل.

### اقتراحات سريعة وعملية
1. **الاستفادة من MDC (Mapped Diagnostic Context) مع Log4j**
   - يدعم Log4j خاصية MDC، والتي تسمح لك بإرفاق أزواج مفتاح-قيمة سياقية بالسجلات داخل موضوع معين (وحتى نشرها عبر حدود المواضيع بعناية).
   - قم بإنشاء معرف طلب فريد (مثل UUID) عندما يصل طلب الواجهة الأمامية إلى تطبيق Spring Boot الخاص بك، وقم بتخزينه في MDC. ثم قم بتضمين هذا ID في نمط السجل (log pattern) الخاص بك.
   - **كيفية التنفيذ:**
     - في عامل تصفية (filter) أو معترض (interceptor) في Spring Boot (مثل `OncePerRequestFilter`)، قم بإنشاء المعرف:
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
                   MDC.clear(); // Clean up after request
               }
           }
       }
       ```
     - سجل عامل التصفية في إعداد Spring Boot الخاص بك:
       ```java
       @Bean
       public FilterRegistrationBean<RequestTracingFilter> tracingFilter() {
           FilterRegistrationBean<RequestTracingFilter> registrationBean = new FilterRegistrationBean<>();
           registrationBean.setFilter(new RequestTracingFilter());
           registrationBean.addUrlPatterns("/*");
           return registrationBean;
       }
       ```
     - قم بتحديث نمط Log4j في `log4j.properties` أو `log4j.xml` لتضمين `traceId`:
       ```properties
       log4j.appender.console.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} [%t] %-5p %c{1} - %m [traceId=%X{traceId}]%n
       ```
     - الآن، كل سطر سجل مرتبط بهذا الطلب سيتضمن `traceId`، مما يجعل من السهل تتبعه مرة أخرى إلى النقر على الزر في الواجهة الأمامية.

2. **نشر معرف التتبع (Trace ID) عبر المواضيع (Threads)**
   - إذا كان تطبيقك يستخدم مجموعات مواضيع (thread pools) أو استدعاءات غير متزامنة (مثل `@Async`)، فقد لا ينتشر سياق MDC تلقائيًا. للتعامل مع هذا:
     - قم بتغليف المهام غير المتزامنة (async tasks) باستخدام منفذ مخصص (custom executor) يقوم بنسخ سياق MDC:
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
     - يضمن هذا أن `traceId` يبقى مرتبطًا بالطلب حتى عبر حدود المواضيع.

3. **إضافة ارتباط من الواجهة الأمامية (Frontend Correlation)**
   - إذا كان ذلك ممكنًا، اجعل الواجهة الأمامية ترسل رأسًا مخصصًا (مثل `X-Request-ID`) مع معرف فريد عند النقر على الزر. يمكن للواجهة الخلفية (backend) أن تلتقط هذا بدلاً من إنشاء UUID خاص بها. هذا يربط السجل مباشرة بإجراء الواجهة الأمامية دون الحاجة إلى تخمين إضافي.

4. **البديل: تعزيز التسجيل (Logging) ببيانات سياقية**
   - إذا شعرت أن استخدام MDC يفرض عبئًا كبيرًا في الوقت الحالي، قم بإثراء سجلاتك بمزيد من السياق في النقاط الرئيسية (مثل user ID, session ID, or endpoint name). على سبيل المثال:
     ```java
     logger.info("Button clicked, endpoint=/api/example, user={}", userId);
     ```
   - اجمع هذا مع `%t` (اسم الموضوع) ونطاق زمني ضيق لتضييق نطاق السجلات يدويًا. هذا ليس الحل الأمثل ولكنه يعمل في الظروف الصعبة.

### لماذا لا يعتمد فقط على النطاق الزمني؟
الاعتماد على الطوابع الزمنية فقط هو هش لأن:
- السجلات من الطلبات المتزامنة تتداخل، خاصة في النظام المزدحم.
- دقة الوقت (مثل المللي ثانية) قد لا تكون كافية لعزل طلب واحد.
- من الممل ربط السجلات عبر الخدمات أو عبر مكدس استدعاءات عميق.

### التوصية طويلة المدى
إذا نمت حاجة التتبع هذه، ففكر في اعتماد الدعم المدمج في Spring Boot للتتبع الموزع (مثل via Sleuth or Micrometer with Zipkin). يقوم Sleuth تلقائيًا بإنشاء معرفات التتبع والامتداد (trace and span IDs) ويتكامل بسلاسة مع Log4j، ولكنه يتطلب إعدادًا أكثر تعقيدًا. في الوقت الحالي، يعد MDC أرضية وسطى خفيفة الوزن وفعالة.

### النصيحة النهائية
ابدأ بأسلوب MDC — فهو بسيط، ويستفيد من إمكانيات Log4j الأصلية، ويوفر لك طريقة واضحة لربط السجلات بطلب بدأ من الواجهة الأمامية. سترى شيئًا مثل `[traceId=123e4567-e89b-12d3-a456-426614174000]` في كل سطر سجل لهذا الطلب، مما يجعل البحث والتتبع أمرًا سهلاً. دعني أعلم إذا كنت بحاجة إلى مساعدة في تعديل هذا further!