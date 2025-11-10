---
audio: false
generated: true
lang: ar
layout: post
title: استكشاف مشكلة `traceId` و `spanId` الفارغة في السجلات
translated: true
type: note
---

`traceId` و `spanId` فارغتان في سطور السجل `[blog-server,,]` على الأرجح بسبب أحد الأسباب التالية:

  * **اعتماد Sleuth مفقود أو غير صحيح:** تأكد من إضافة الاعتماد `spring-cloud-starter-sleuth` بشكل صحيح إلى ملف `pom.xml` الخاص بمشروعك (لـ Maven) أو `build.gradle` (لـ Gradle)، وأنك تستخدم إصدارات متوافقة من Spring Boot و Spring Cloud. بدون هذا الاعتماد، لن يتم تفعيل التهيئة التلقائية لـ Spring Cloud Sleuth.

    ```xml
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-sleuth</artifactId>
    </dependency>
    ```

  * **نمط تسجيل مخصص:** إذا قمت بتعريف نمط تسجيل مخصص (مثلًا في `logback-spring.xml` أو `application.properties`)، فيجب أن تتضمن بشكل صريح عناصر نائبة لـ `traceId` و `spanId`. إذا كانت هذه العناصر النائبة مفقودة، فلن تظهر المعرفات في سجلاتك حتى إذا كان Sleuth نشطًا.

    لـ Logback، تأكد من أن نمطك يتضمن `%X{traceId}` و `%X{spanId}`:

    ```xml
    <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level [${spring.application.name:-},%X{traceId:-},%X{spanId:-}] %thread %logger{36} - %msg%n</pattern>
    ```

  * **لا يوجد سياق تتبع Trace/Span نشط:** بينما يقوم Sleuth تلقائيًا بتجهيز العديد من مكونات Spring (مثل `DispatcherServlet` لطلبات HTTP)، فمن الممكن أن تكون رسائل السجل هذه مُنشأة في سياق لم يتم فيه بدء أو نشر تتبع Trace أو مدى Span بعد. على سبيل المثال، بعض سجلات بدء التطبيق المبكرة جدًا أو السجلات من الخيوط threads التي لا تديرها عملية نشر سياق Sleuth قد لا تحتوي على هذه المعرفات. ومع ذلك، بالنسبة للسجلات أثناء معالجة طلب HTTP نشط مثل `HttpEntityMethodProcessor` و `DispatcherServlet` التي تكمل طلبًا، فإن هذا أقل شيوعًا إذا تم إعداد Sleuth بشكل صحيح.

لحل المشكلة، تحقق أولاً من الاعتماديات وتكوين التسجيل. إذا كانت هذه صحيحة، تأكد من أن الطلبات تصل بالفعل إلى تطبيقك ويتم معالجتها بواسطة `DispatcherServlet` الخاص بـ Spring MVC، والذي من المفترض أن يُطلق تجهيزات Sleuth.