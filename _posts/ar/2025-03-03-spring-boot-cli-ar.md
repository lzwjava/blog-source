---
audio: false
generated: true
lang: ar
layout: post
title: كيفية استخدام Spring Boot CLI
translated: true
type: note
---

Spring Boot CLI (واجهة سطر الأوامر) هي أداة قوية تتيح لك تطوير واختبار وإنشاء نماذج أولية لتطبيقات Spring Boot مباشرة من سطر الأوامر. إنها مفيدة بشكل خاص لتشغيل نصوص Groovy دون إعداد بنية مشروع كاملة، أو إنشاء مشاريع جديدة، أو تجربة ميزات Spring Boot. فيما يلي دليل كامل حول كيفية تثبيت واستخدام Spring Boot CLI بفعالية.

---

## التثبيت
قبل أن تتمكن من استخدام Spring Boot CLI، تحتاج إلى تثبيتها. هناك طريقتان رئيسيتان حسب نظام التشغيل الخاص بك:

### 1. استخدام SDKMAN! (موصى به لأنظمة Unix مثل Linux أو macOS)
SDKMAN! هي أداة لإدارة أدوات تطوير البرمجيات، مما يجعلها طريقة سهلة لتثبيت Spring Boot CLI.

- **الخطوة 1: تثبيت SDKMAN!**
  افتح طرفيتك وقم بتشغيل:
  ```bash
  curl -s "https://get.sdkman.io" | bash
  ```
  اتبع التعليمات لتهيئة SDKMAN! من خلال تحميل البرنامج النصي:
  ```bash
  source "$HOME/.sdkman/bin/sdkman-init.sh"
  ```

- **الخطوة 2: تثبيت Spring Boot CLI**
  قم بتشغيل الأمر التالي:
  ```bash
  sdk install springboot
  ```

### 2. التثبيت اليدوي (لـ Windows أو الإعداد اليدوي)
إذا كنت تستخدم Windows أو تفضل التثبيت اليدوي:
- قم بتنزيل ملف ZIP الخاص بـ Spring Boot CLI من [موقع Spring الرسمي](https://spring.io/projects/spring-boot).
- استخرج ملف ZIP إلى الدليل الذي تختاره.
- أضف الدليل `bin` من المجلد المستخرج إلى متغير بيئة PATH في نظامك.

### التحقق من التثبيت
لتأكيد تثبيت Spring Boot CLI بشكل صحيح، قم بتشغيل هذا الأمر في طرفيتك:
```bash
spring --version
```
يجب أن ترى الإصدار المثبت من Spring Boot CLI (مثال: `Spring CLI v3.3.0`). إذا عمل هذا، فأنت جاهز لبدء استخدامه!

---

## الطرق الرئيسية لاستخدام Spring Boot CLI
توفر Spring Boot CLI عدة ميزات تجعلها مثالية للتطوير السريع وإنشاء النماذج الأولية. فيما يلي الطرق الرئيسية لاستخدامها:

### 1. تشغيل نصوص Groovy
إحدى الميزات البارزة في Spring Boot CLI هي قدرتها على تشغيل نصوص Groovy مباشرة دون الحاجة إلى إعداد مشروع كامل. هذا مثالي لإنشاء النماذج الأولية السريعة أو تجربة Spring Boot.

- **مثال: إنشاء تطبيق ويب بسيط**
  قم بإنشاء ملف باسم `hello.groovy` بالمحتوى التالي:
  ```groovy
  @RestController
  class HelloController {
      @RequestMapping("/")
      String home() {
          "Hello, World!"
      }
  }
  ```

- **تشغيل النص**
  في طرفيتك، انتقل إلى الدليل الذي يحتوي على `hello.groovy` وقم بتشغيل:
  ```bash
  spring run hello.groovy
  ```
  هذا يبدأ خادم ويب على المنفذ 8080. افتح متصفحًا وقم بزيارة `http://localhost:8080` لرؤية "Hello, World!" معروض.

- **إضافة التبعيات**
  يمكنك تضمين التبعيات مباشرة في النص باستخدام شرح `@Grab`. على سبيل المثال:
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
  هذا يضيف Spring Data JPA إلى نصك دون الحاجة إلى ملف بناء.

- **تشغيل نصوص متعددة**
  لتشغيل جميع نصوص Groovy في الدليل الحالي، استخدم:
  ```bash
  spring run *.groovy
  ```

### 2. إنشاء مشاريع Spring Boot جديدة
يمكن لـ Spring Boot CLI إنشاء بنية مشروع جديدة مع التبعيات التي تريدها، مما يوفر لك الوقت عند بدء تطبيق كامل.

- **مثال: إنشاء مشروع**
  قم بتشغيل هذا الأمر لإنشاء مشروع جديد مع تبعيات web و data-jpa:
  ```bash
  spring init --dependencies=web,data-jpa my-project
  ```
  هذا ينشئ دليلًا يسمى `my-project` يحتوي على تطبيق Spring Boot مكون مع Spring Web و Spring Data JPA.

- **خيارات التخصيص**
  يمكنك تحديد خيارات إضافية مثل:
  - أداة البناء: `--build=maven` أو `--build=gradle`
  - اللغة: `--language=java`، `--language=groovy`، أو `--language=kotlin`
  - التغليف: `--packaging=jar` أو `--packaging=war`

  على سبيل المثال:
  ```bash
  spring init --dependencies=web --build=gradle --language=kotlin my-kotlin-project
  ```

### 3. تغليف التطبيقات
تسمح لك Spring Boot CLI بتغليف نصوصك في ملفات JAR أو WAR قابلة للتنفيذ للنشر.

- **إنشاء ملف JAR**
  ```bash
  spring jar my-app.jar *.groovy
  ```
  هذا يغلف جميع نصوص Groovy في الدليل الحالي في `my-app.jar`.

- **إنشاء ملف WAR**
  ```bash
  spring war my-app.war *.groovy
  ```
  هذا يولد ملف `my-app.war` مناسب للنشر إلى حاوية servlet.

### 4. تشغيل الاختبارات
إذا كان لديك نصوص اختبار Groovy، يمكنك تنفيذها باستخدام:
```bash
spring test *.groovy
```
هذا يشغل جميع نصوص الاختبار في الدليل الحالي.

### 5. استخدام الوضع التفاعلي Shell
لتجربة تفاعلية، قم بتشغيل Spring Boot CLI shell:
```bash
spring shell
```
داخل الـ shell، يمكنك تشغيل أوامر مثل `run`، أو `grab`، أو `jar` بشكل تفاعلي، وهو رائع للتجربة.

---

## الملخص
Spring Boot CLI هي أداة ممتازة للمطورين الذين يريدون العمل مع Spring Boot بسرعة وكفاءة من سطر الأوامر. فيما يلي كيفية استخدامها باختصار:

1. **قم بتثبيتها** باستخدام SDKMAN! (`sdk install springboot`) أو يدويًا عن طريق تنزيل ZIP وتحديد PATH الخاص بك.
2. **شغّل نصوص Groovy** باستخدام `spring run <script.groovy>` لإنشاء النماذج الأولية السريعة.
3. **أنشئ مشاريع جديدة** باستخدام `spring init --dependencies=<deps> <project-name>`.
4. **غلف التطبيقات** في ملفات JAR أو WAR باستخدام `spring jar` أو `spring war`.
5. **جرب بشكل تفاعلي** مع `spring shell`.

سواء كنت تنشئ نموذجًا أوليًا لفكرة، أو تتعلم Spring Boot، أو تؤتمت المهام، تقدم Spring Boot CLI طريقة خفيفة الوزن ومرنة للبدء دون الحاجة إلى بيئة تطوير متكاملة كاملة أو إعداد مشروع.