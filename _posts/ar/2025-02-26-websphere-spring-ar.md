---
audio: true
generated: true
lang: ar
layout: post
title: توزيع Spring Boot إلى WebSphere Liberty Profile
translated: true
---

هنا دليل شامل لتشغيل تطبيق Spring Boot بسيط على WebSphere Liberty Profile (WLP). يوضح هذا المثال كيفية إنشاء تطبيق Spring Boot مع نقطة نهاية REST أساسية ترجع "Hello World!" وتنفذه على WLP باستخدام مجلد `dropins`. سنفترض أنك قد قمت بالفعل بتكوين WLP مع الميزة `javaee-8.0` المفعلة، حيث توفر الدعم اللازم لServlet.

---

### دليل خطوة بخطوة

#### 1. إنشاء تطبيق Spring Boot
ابدأ بإنشاء مشروع Spring Boot جديد باستخدام Spring Initializr (أو أي طريقة تفضلها). سنستخدم Maven، Java، وDependency Spring Web لبناء تطبيق ويب بسيط.

- **إنشاء المشروع:**
  - اذهب إلى [Spring Initializr](https://start.spring.io/).
  - قم بتكوين التالي:
    - **المشروع:** Maven
    - **اللغة:** Java
    - **إصدار Spring Boot:** 2.7.x (أو أحدث إصدار مستقر)
    - **المجموعة:** `com.example`
    - **المنتج:** `demo`
    - **الاعتماديات:** Spring Web
  - انقر على "Generate" لتنزيل ملف ZIP للمشروع، ثم فكه وافتحه في IDE الخاص بك.

- **إضافة Controller REST بسيط:**
  داخل `src/main/java/com/example/demo`، قم بإنشاء ملف باسم `HelloController.java` مع المحتوى التالي:
  ```java
  package com.example.demo;

  import org.springframework.web.bind.annotation.GetMapping;
  import org.springframework.web.bind.annotation.RestController;

  @RestController
  public class HelloController {
      @GetMapping("/")
      public String hello() {
          return "Hello World!";
      }
  }
  ```
  هذا يخلق نقطة نهاية REST في المسار الجذر (`/`) ترجع "Hello World!" كنص عادي.

#### 2. تكوين التطبيق لتغليف WAR
بالتعريف، يغلف Spring Boot التطبيقات كملفات JAR مع خادم مدمج (مثل Tomcat). لتنفذه على WLP، علينا تغليفها كملف WAR وتكوينها للعمل مع خادم Servlet الخاص بـ WLP.

- **تعديل الفئة الرئيسية للتطبيق:**
  قم بتحرير `src/main/java/com/example/demo/DemoApplication.java` لتوسيع `SpringBootServletInitializer`، مما يسمح للتطبيق بالعمل في خادم Servlet خارجي مثل WLP:
  ```java
  package com.example.demo;

  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;
  import org.springframework.boot.builder.SpringApplicationBuilder;
  import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;

  @SpringBootApplication
  public class DemoApplication extends SpringBootServletInitializer {

      @Override
      protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
          return application.sources(DemoApplication.class);
      }

      public static void main(String[] args) {
          SpringApplication.run(DemoApplication.class, args);
      }
  }
  ```

- **تحديث `pom.xml` لتغليف WAR:**
  افتح `pom.xml` واجعل هذه التغييرات:
  - قم بتحديد التغليف WAR بإضافة هذه السطر بالقرب من الأعلى (تحت `<modelVersion>`):
    ```xml
    <packaging>war</packaging>
    ```
  - قم بتحديد Dependency Tomcat المدمجة ك `provided` بحيث لا يتم تضمينها في WAR (يوفر WLP خادم Servlet الخاص به). قم بتعديل Dependency `spring-boot-starter-web` (الذي يتضمن Tomcat) كما يلي:
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    ```
    أضف هذا تحتها:
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-tomcat</artifactId>
        <scope>provided</scope>
    </dependency>
    ```
  يجب أن تبدو قسم الاعتماديات في `pom.xml` الآن مثل هذا:
  ```xml
  <dependencies>
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-web</artifactId>
      </dependency>
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-tomcat</artifactId>
          <scope>provided</scope>
      </dependency>
      <!-- قد تبقى الاعتماديات الأخرى مثل spring-boot-starter-test -->
  </dependencies>
  ```

#### 3. بناء ملف WAR
قم بتجميع وتغليف التطبيق إلى ملف WAR باستخدام Maven.

- **تنفذ الأمر التجميع:**
  من مجلد الجذر للمشروع (حيث يوجد `pom.xml`)، قم بتنفيد:
  ```bash
  mvn clean package
  ```
  هذا يخلق ملف WAR في مجلد `target`، مثل `target/demo-0.0.1-SNAPSHOT.war`.

- **إعادة تسمية ملف WAR (اختياري):**
  لURL أكثر نظافة، قم بإعادة تسمية ملف WAR إلى `myapp.war`:
  ```bash
  mv target/demo-0.0.1-SNAPSHOT.war target/myapp.war
  ```
  هذا يبسط الجذر السياق إلى `/myapp` بدلاً من `/demo-0.0.1-SNAPSHOT`.

#### 4. نشر ملف WAR على WLP
قم بنشر ملف WAR على WLP باستخدام مجلد `dropins`، مما يتيح نشرًا تلقائيًا.

- **تحديد مجلد `dropins`:**
  ايجد مجلد `dropins` لخدمتك WLP. إذا كان WLP مثبتًا في `/opt/ibm/wlp` واسم خدمتك هو `myServer`، فإن المسار هو:
  ```
  /opt/ibm/wlp/usr/servers/myServer/dropins
  ```

- **نسخ ملف WAR:**
  قم بنقل ملف WAR إلى مجلد `dropins`:
  ```bash
  cp target/myapp.war /opt/ibm/wlp/usr/servers/myServer/dropins/
  ```

- **إطلاق الخادم (إذا لم يكن يعمل):**
  إذا لم يكن WLP يعمل، قم بإطلاقه:
  ```bash
  /opt/ibm/wlp/bin/server start myServer
  ```
  إذا كان يعمل بالفعل، فإنه سيكتشف ونشر ملف WAR تلقائيًا.

- **التحقق من النشر:**
  قم بالبحث في سجلات الخادم أو الواجهة الأمامية لمessage مثل:
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  - سجلات في `/opt/ibm/wlp/usr/servers/myServer/logs/console.log` (الوضع الخلفي) أو عرضها في الواجهة الأمامية (الوضع الأمامي مع `./server run myServer`).

#### 5. الوصول إلى التطبيق
اختبر تطبيق Spring Boot المنشور في المتصفح.

- **افتح متصفحك:**
  اذهب إلى:
  ```
  http://localhost:9080/myapp/
  ```
  - `9080` هو الميناء الافتراضي لـ WLP لـ HTTP.
  - `/myapp` هو الجذر السياق من اسم ملف WAR.
  - `/` يتطابق مع `@GetMapping("/")` في Controller.

- **النتيجة المتوقعة:**
  يجب أن ترى:
  ```
  Hello World!
  ```
  كنص عادي.

---

### ملاحظات
- **الجذر السياق:** الجذر السياق (`/myapp`) مستمد من اسم ملف WAR. قم بتعديله بإعادة تسمية ملف WAR حسب الحاجة.
- **رقم الميناء:** يستخدم WLP `9080` افتراضيًا لـ HTTP. إذا كان خادمك يستخدم ميناء مختلفًا، قم بتحديث URL وفقًا لذلك.
- **إصدار Java:** تأكد من أن WLP وبيئة التجميع الخاصة بك تستخدم إصدار Java متوافقًا (مثل Java 8 أو 11 لـ Spring Boot 2.7.x).
- **ميزات WLP:** الميزة `javaee-8.0` تتضمن دعم Servlet 4.0، والتي تتوافق مع متطلبات Spring Boot 2.7.x (Servlet 3.1+).
- **إصلاح الأخطاء:**
  - إذا لم يتم تحميل الصفحة، قم بالبحث في `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` عن الأخطاء.
  - تأكد من أن ملف WAR في `dropins` وخدمتك تعمل.

---

### ملخص
يوضح هذا الدليل كيفية:
1. إنشاء تطبيق Spring Boot مع نقطة نهاية REST.
2. تكوينه لتغليف WAR عن طريق توسيع `SpringBootServletInitializer` وتحديد Tomcat ك `provided`.
3. بناء ونشر ملف WAR إلى مجلد `dropins` لـ WLP.
4. الوصول إلى "Hello World!" في `http://localhost:9080/myapp/`.

يستفيد هذا النهج من قدرات نشر WLP التلقائي و مرونة Spring Boot، مما يوفر تطبيق ويب بسيطًا ولكن وظيفيًا على WebSphere Liberty Profile.