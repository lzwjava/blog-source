---
audio: false
generated: true
lang: ar
layout: post
title: كيفية استخدام Spring Boot CLI
translated: true
---

Spring Boot CLI (واجهة السطر الأوامر) هو أداة قوية تسمح لك بتطوير، اختبار، وتجريب تطبيقات Spring Boot مباشرة من السطر الأوامر. وهي مفيدة بشكل خاص في تشغيل كودات Groovy بدون إعداد بنية مشروع كاملة، أو إنشاء مشاريع جديدة، أو التجريب مع ميزات Spring Boot. أدناه دليل شامل حول كيفية تثبيت واستخدام Spring Boot CLI بشكل فعال.

---

## التثبيت
قبل أن يمكنك استخدام Spring Boot CLI، عليك تثبيته. هناك طريقةان رئيسيتان اعتمادًا على نظام التشغيل الخاص بك:

### 1. باستخدام SDKMAN! (موصى به للنظم القائمة على يونكس مثل لينكس أو macOS)
SDKMAN! هو أداة لإدارة كتل البرمجة، مما يجعلها طريقة سهلة لتثبيت Spring Boot CLI.

- **الخطوة 1: تثبيت SDKMAN!**
  افتح مستودعك واكتب:
  ```bash
  curl -s "https://get.sdkman.io" | bash
  ```
  اتبع التوجيهات لتفعيل SDKMAN! من خلال تشغيل النص:
  ```bash
  source "$HOME/.sdkman/bin/sdkman-init.sh"
  ```

- **الخطوة 2: تثبيت Spring Boot CLI**
  اكتب الأمر التالي:
  ```bash
  sdk install springboot
  ```

### 2. التثبيت اليدوي (لويندوز أو التثبيت اليدوي)
إذا كنت على ويندوز أو تفضل التثبيت اليدوي:
- قم بتنزيل ملف Spring Boot CLI ZIP من [الموقع الرسمي لSpring](https://spring.io/projects/spring-boot).
- استخرج ملف ZIP إلى مجلد من اختيارك.
- أضف مجلد `bin` من المجلد المستخرج إلى متغير PATH للنظام.

### التحقق من التثبيت
للتأكد من أن Spring Boot CLI تم تثبيته بشكل صحيح، اكتب الأمر التالي في مستودعك:
```bash
spring --version
```
يجب أن ترى الإصدار المثبت لSpring Boot CLI (مثلًا `Spring CLI v3.3.0`). إذا عمل هذا، فأنت مستعد للبدء في استخدامه!

---

## طرق استخدام Spring Boot CLI الرئيسية
يوفر Spring Boot CLI عدة ميزات تجعلها مثالية للتطوير السريع والتجريب. هذه هي الطرق الرئيسية لاستخدامها:

### 1. تشغيل كودات Groovy
من الميزات البارزة لSpring Boot CLI قدرتها على تشغيل كودات Groovy مباشرة دون الحاجة إلى إعداد بنية مشروع كاملة. وهذا مثالي للتجريب السريع أو التجريب مع Spring Boot.

- **مثال: إنشاء تطبيق ويب بسيط**
  انشئ ملف باسم `hello.groovy` مع المحتوى التالي:
  ```groovy
  @RestController
  class HelloController {
      @RequestMapping("/")
      String home() {
          "Hello, World!"
      }
  }
  ```

- **تشغيل الكود**
  في مستودعك، انتقل إلى المجلد الذي يحتوي على `hello.groovy` واكتب:
  ```bash
  spring run hello.groovy
  ```
  هذا يبدأ خادم ويب على الميناء 8080. افتح متصفح ويب وزيارة `http://localhost:8080` لرؤية "Hello, World!".

- **إضافة الاعتماديات**
  يمكنك إضافة الاعتماديات مباشرة في الكود باستخدام تعليق `@Grab`. على سبيل المثال:
  ```groovy
  @Grab('org.springframework.boot:spring-boot-starter-data-jpa')
  @RestController
  class HelloController {
      @RequestMapping("/")
      String home() {
          "Hello, World!"
      }
  }
  ```
  هذا يضيف Spring Data JPA إلى الكود دون الحاجة إلى ملف بناء.

- **تشغيل كودات متعددة**
  لتشغيل جميع كودات Groovy في المجلد الحالي، اكتب:
  ```bash
  spring run *.groovy
  ```

### 2. إنشاء مشاريع Spring Boot جديدة
يمكن لSpring Boot CLI إنشاء بنية مشروع جديدة مع الاعتماديات التي تريدها، مما يوفر لك الوقت عند البدء في تطبيق كامل.

- **مثال: إنشاء مشروع**
  اكتب الأمر التالي لإنشاء مشروع جديد مع الاعتماديات web و data-jpa:
  ```bash
  spring init --dependencies=web,data-jpa my-project
  ```
  هذا يخلق مجلدًا باسم `my-project` يحتوي على تطبيق Spring Boot مهيأ مع Spring Web و Spring Data JPA.

- **خيارات التخصيص**
  يمكنك تحديد خيارات إضافية مثل:
  - أداة البناء: `--build=maven` أو `--build=gradle`
  - اللغة: `--language=java`, `--language=groovy`, أو `--language=kotlin`
  - التعبئة: `--packaging=jar` أو `--packaging=war`

  على سبيل المثال:
  ```bash
  spring init --dependencies=web --build=gradle --language=kotlin my-kotlin-project
  ```

### 3. تعبئة التطبيقات
يمكن لSpring Boot CLI تعبئة كوداتك إلى ملفات JAR أو WAR قابلة للتنفيذ للتبليغ.

- **إنشاء ملف JAR**
  ```bash
  spring jar my-app.jar *.groovy
  ```
  هذا يعبئ جميع كودات Groovy في المجلد الحالي إلى `my-app.jar`.

- **إنشاء ملف WAR**
  ```bash
  spring war my-app.war *.groovy
  ```
  هذا يخلق ملف `my-app.war` مناسب للتبليغ إلى خادم Servlet.

### 4. تشغيل الاختبارات
إذا كان لديك كودات اختبار Groovy، يمكنك تنفيذها باستخدام:
```bash
spring test *.groovy
```
هذا يجرى جميع كودات الاختبار في المجلد الحالي.

### 5. استخدام القشرة التفاعلية
لخبرة تفاعلية، اكتب القشرة Spring Boot CLI:
```bash
spring shell
```
داخل القشرة، يمكنك تشغيل الأوامر مثل `run`, `grab`, أو `jar` بشكل تفاعلي، وهو ممتاز للتجريب.

---

## ملخص
Spring Boot CLI هي أداة رائعة للمطورين الذين يريدون العمل مع Spring Boot بسرعة وفعالية من السطر الأوامر. إليك كيفية استخدامها في نكهة:

1. **تثبيته** باستخدام SDKMAN! (`sdk install springboot`) أو يدويًا من خلال تنزيل ZIP وتحديث PATH.
2. **تشغيل كودات Groovy** باستخدام `spring run <script.groovy>` للتجريب السريع.
3. **إنشاء مشاريع جديدة** باستخدام `spring init --dependencies=<deps> <project-name>`.
4. **عبئة التطبيقات** إلى ملفات JAR أو WAR باستخدام `spring jar` أو `spring war`.
5. **التجريب التفاعلي** باستخدام `spring shell`.

ما إذا كنت تبتكر فكرة، أو تعلم Spring Boot، أو تسيير مهام، فإن Spring Boot CLI يقدم طريقة خفيفة و مرنة للبدء دون عبء IDE كامل أو إعداد مشروع.