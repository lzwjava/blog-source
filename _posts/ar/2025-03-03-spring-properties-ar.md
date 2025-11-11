---
audio: false
generated: true
lang: ar
layout: post
title: اختيار ملف الخصائص في سبرينغ بوت
translated: true
type: note
---

في مشروع Spring Boot باستخدام Maven، لديك ملفي خصائص، `appProperties.properties` و `appProperties-hk.properties`، موجودان في المسار `src/main/resources`. للتحكم في ملف الخصائص المستخدم، خاصة لتحديد استخدام خصائص `-hk`، يمكنك الاستفادة من آليات التهيئة في Spring Boot. إليك كيف يمكنك القيام بذلك:

### الحل

1. **إنشاء ملف `application.properties`**
   - بشكل افتراضي، يبحث Spring Boot عن ملف `application.properties` أو `application.yml` في `src/main/resources` لتحميل إعدادات التهيئة.
   - لاستخدام ملفات الخصائص المخصصة الخاصة بك (`appProperties.properties` و `appProperties-hk.properties`)، تحتاج إلى إخبار Spring Boot بالبحث عن ملفات تحمل الاسم الأساسي `appProperties` بدلاً من الاسم الافتراضي `application`.
   - أضف السطر التالي إلى ملف `application.properties` جديد في `src/main/resources`:

     ```properties
     spring.config.name=appProperties
     ```

   - يخبر هذا الإعداد Spring Boot بتحميل `appProperties.properties` كملف التهيئة الأساسي، وسيبحث تلقائيًا عن المتغيرات الخاصة بالملفات الشخصية مثل `appProperties-{profile}.properties` عندما يكون الملف الشخصي نشطًا.

2. **استخدام الملفات الشخصية (Profiles) في Spring لتحديد خصائص `-hk`**
   - يدعم Spring Boot الملفات الشخصية، والتي تسمح لك بتحميل ملفات خصائص إضافية أو متجاورة بناءً على الملف الشخصي النشط.
   - نظرًا لأن ملفك يحمل اسم `appProperties-hk.properties`، فإنه يتبع النمط `appProperties-{profile}.properties`. هنا، يمكن اعتبار "hk" اسم ملف شخصي.
   - لاستخدام `appProperties-hk.properties`، قم بتفعيل الملف الشخصي "hk" عند تشغيل تطبيقك. بعد ذلك، سيقوم Spring Boot بتحميل كل من `appProperties.properties` و `appProperties-hk.properties`، مع إعطاء الأولوية للخصائص المحددة في `appProperties-hk.properties` لتجاوز أي خصائص متطابقة في `appProperties.properties`.

3. **كيفية تفعيل الملف الشخصي "hk"**
   - **عبر سطر الأوامر**: عند تشغيل تطبيق Spring Boot الخاص بك، حدد الملف الشخصي النشط باستخدام الوسيطة `--spring.profiles.active`. على سبيل المثال:
     ```bash
     java -jar target/myapp.jar --spring.profiles.active=hk
     ```
     استبدل `myapp.jar` باسم ملف JAR الخاص بتطبيقك الذي تم إنشاؤه بواسطة Maven.

   - **عبر Maven**: إذا كنت تقوم بتشغيل التطبيق باستخدام هدف `spring-boot:run`، قم بتكوين الملف الشخصي في ملف `pom.xml` الخاص بك:
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
     ثم قم بالتشغيل:
     ```bash
     mvn spring-boot:run
     ```

   - **عبر خاصية النظام (System Property)**: عيّن الملف الشخصي كوسيطة JVM:
     ```bash
     java -Dspring.profiles.active=hk -jar target/myapp.jar
     ```

   - **عبر متغير البيئة (Environment Variable)**: قم بتصدير الملف الشخصي في بيئتك (على سبيل المثال، في نظام يشبه Unix):
     ```bash
     export SPRING_PROFILES_ACTIVE=hk
     java -jar target/myapp.jar
     ```

### آلية العمل
- مع تعيين `spring.config.name=appProperties` في `application.properties`، يستخدم Spring Boot `appProperties` كاسم أساسي لملفات التهيئة.
- عندما لا يكون هناك ملف شخصي نشط، يتم تحميل `appProperties.properties` فقط.
- عند تفعيل الملف الشخصي "hk" (على سبيل المثال، عبر `--spring.profiles.active=hk`)، يقوم Spring Boot بتحميل كل من `appProperties.properties` و `appProperties-hk.properties`. تأخذ الخصائص المعرفة في `appProperties-hk.properties` الأسبقية على تلك الموجودة في `appProperties.properties` في حالة وجود أي تكرار.

### الخطوات النهائية
- تأكد من أن كلا الملفين `appProperties.properties` و `appProperties-hk.properties` موجودان في `src/main/resources`.
- أضف `application.properties` الذي يحتوي على `spring.config.name=appProperties` إلى `src/main/resources`.
- شغّل تطبيقك مع تفعيل الملف الشخصي "hk" لاستخدام خصائص `-hk`.

هذا النهج يتوافق مع أعراف Spring Boot، مما يجعله طريقة نموذجية ومباشرة للتحكم في ملف الخصائص المستخدم في مشروعك. لاستخدام خصائص `-hk` تحديدًا، ما عليك سوى تفعيل الملف الشخصي "hk" كما هو موضح أعلاه.