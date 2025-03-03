---
audio: false
generated: true
lang: ar
layout: post
title: اختيار ملفات الخصائص في Spring Boot
translated: true
---

في مشروع Spring Boot Maven، لديك ملفين من ملفات الخصائص، `appProperties.properties` و `appProperties-hk.properties`، ويقعان تحت `src/main/resources`. للتحكم في ملف الخصائص المستخدم، وخاصة تحديد استخدام الخصائص `-hk`، يمكنك الاستفادة من آليات تكوين Spring Boot. إليك كيفية القيام بذلك:

### الحل

1. **إنشاء ملف `application.properties`**
   - من خلال الافتراض، يبحث Spring Boot عن `application.properties` أو `application.yml` في `src/main/resources` لتحميل إعدادات التكوين.
   - لاستخدام ملفات الخصائص الخاصة بك (`appProperties.properties` و `appProperties-hk.properties`), يجب أن تخبر Spring Boot البحث عن ملفات ذات الاسم الأساسي `appProperties` بدلاً من الافتراض `application`.
   - أضف السطر التالي إلى ملف `application.properties` الجديد في `src/main/resources`:

     ```properties
     spring.config.name=appProperties
     ```

   - هذا الإعداد يخبر Spring Boot بتحميل `appProperties.properties` كملف التكوين الأساسي، وسيبحث أيضًا تلقائيًا عن متغيرات محددة للملفات مثل `appProperties-{profile}.properties` عندما يكون ملف محدد نشطًا.

2. **استخدام ملفات Spring Profiles لتحديد الخصائص `-hk`**
   - يدعم Spring Boot ملفات الملفات، والتي تسمح لك بتحميل ملفات خصائص إضافية أو استبدالها بناءً على الملف النشط.
   - نظرًا لأن ملفك يُسمى `appProperties-hk.properties`، فإنه يتبع النمط `appProperties-{profile}.properties`. هنا يمكن معالجة "hk" كاسم ملف.
   - لاستخدام `appProperties-hk.properties`، قم بتفعيل ملف "hk" عند تشغيل تطبيقك. Spring Boot سيقوم بتحميل كل من `appProperties.properties` و `appProperties-hk.properties`، مع أن الخصائص في `appProperties-hk.properties` ستستبدل أي خصائص متطابقة في `appProperties.properties`.

3. **كيفية تفعيل ملف "hk"**
   - **من خلال السطر الأوامر**: عند تشغيل تطبيق Spring Boot الخاص بك، حدد الملف النشط باستخدام الحجة `--spring.profiles.active`. على سبيل المثال:
     ```bash
     java -jar target/myapp.jar --spring.profiles.active=hk
     ```
     استبدل `myapp.jar` باسم ملف JAR الخاص بتبنيك الذي تم إنشاؤه بواسطة Maven.

   - **من خلال Maven**: إذا كنت تجرى التطبيق باستخدام الهدف `spring-boot:run`، قم بتكوين الملف في `pom.xml`:
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <configuration>
             <profiles>
                 <profile>hk</profile>
             </profiles>
         </configuration>
     </plugin>
     ```
     ثم قم بتشغيل:
     ```bash
     mvn spring-boot:run
     ```

   - **من خلال خاصية النظام**: قم بتعيين الملف كحجة JVM:
     ```bash
     java -Dspring.profiles.active=hk -jar target/myapp.jar
     ```

   - **من خلال متغير البيئة**: قم بتصدير الملف في البيئة (على سبيل المثال، في نظام مشابه لـ Unix):
     ```bash
     export SPRING_PROFILES_ACTIVE=hk
     java -jar target/myapp.jar
     ```

### كيفية العمل
- مع `spring.config.name=appProperties` محدد في `application.properties`، يستخدم Spring Boot `appProperties` كاسم أساسي للملفات التكوينية.
- عندما لا يكون ملف نشطًا، يتم تحميل `appProperties.properties` فقط.
- عندما يتم تفعيل ملف "hk" (على سبيل المثال، من خلال `--spring.profiles.active=hk`), Spring Boot يقوم بتحميل كل من `appProperties.properties` و `appProperties-hk.properties`. الخصائص المحددة في `appProperties-hk.properties` تأخذ الأولوية على تلك في `appProperties.properties` إذا كان هناك أي تكرار.

### الخطوات النهائية
- تأكد من أن كل من `appProperties.properties` و `appProperties-hk.properties` في `src/main/resources`.
- أضف `application.properties` مع `spring.config.name=appProperties` إلى `src/main/resources`.
- قم بتشغيل تطبيقك مع ملف "hk" النشط لاستخدام الخصائص `-hk`.

يتبع هذا النهج معايير Spring Boot، مما يجعله طريقة عادية ومباشرة للتحكم في ملف الخصائص المستخدم في مشروعك. لاستخدام الخصائص `-hk` بشكل محدد، قم بتفعيل ملف "hk" كما هو موضح أعلاه.