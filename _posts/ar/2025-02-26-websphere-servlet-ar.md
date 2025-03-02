---
audio: true
generated: false
lang: ar
layout: post
title: 'Servlet Version in WebSphere Liberty Profile


  النسخة Servlet في WebSphere Liberty Profile'
translated: true
---

### فهم الخطأ

يرد أن رسالة الخطأ من `console.log` تشير إلى `DDParser ParseException` المتعلقة بملف `web-fragment.xml` في `spring-web-6.2.3.jar`. وتوضح أن الوصف الوصفي للإنشاء يشير إلى الإصدار "50" (الذي يتوافق مع Servlet 5.0)، ولكن خادم WebSphere Liberty Profile (WLP) حاليًا مزوّد بالنسخة "40" (Servlet 4.0). يحدث هذا التناقض لأن:

- **Servlet 5.0** جزء من Jakarta EE 9 ويحتاج إليه إصدارات أحدث من Spring Boot (مثل Spring Boot 3.x، والتي تتضمن `spring-web-6.2.3.jar`).
- **Servlet 4.0** جزء من Java EE 8، وWLP محتمل أن يكون مكوّنًا مع الميزة `javaee-8.0`، والتي لا تدعم Servlet 5.0.

لإصلاح ذلك، عليك توحيد الإصدار الذي يدعمه WLP مع الإصدار المطلوب من تطبيقك. الحل الموصى به هو تحديث WLP لدعم Servlet 5.0 من خلال تمكين الميزة `jakartaee-9.1`.

---

### الحل: تحديث WLP لدعم Servlet 5.0

هنا كيفية إصلاح المشكلة من خلال تحديث WLP لاستخدام الميزة `jakartaee-9.1`، والتي تشمل دعم Servlet 5.0:

#### 1. **إيجاد ملف `server.xml`**
- يحدد ملف `server.xml` الميزات المفعلة في WLP.
- عادة ما يكون موجودًا في دليل الخادم، مثل `/opt/ibm/wlp/usr/servers/myServer/server.xml`، حيث `myServer` هو اسم خادمك.

#### 2. **تحرير ملف `server.xml`**
- افتح ملف `server.xml` في محرر النصوص.
- ايجاد قسم `<featureManager>`، الذي يحدد الميزات المفعلة للخادم. قد يبدو حاليًا كالتالي:
  ```xml
  <featureManager>
      <feature>javaee-8.0</feature>
  </featureManager>
  ```
- استبدل الميزة `javaee-8.0` بالميزة `jakartaee-9.1` لتمكين دعم Servlet 5.0:
  ```xml
  <featureManager>
      <feature>jakartaee-9.1</feature>
  </featureManager>
  ```
- احفظ الملف.

#### 3. **تطبيق التغييرات في WLP في وضع التطوير (إذا كان ذلك مناسبًا)**
- إذا كنت تعمل WLP في **وضع التطوير** (مثل استخدام الأمر `wlp/bin/server run` أو التكامل مع IDE)، يمكنك تطبيق التغييرات كما يلي:
  - **إيقاف وإعادة تشغيل يدويًا:**
    - إيقاف الخادم:
      ```bash
      /opt/ibm/wlp/bin/server stop myServer
      ```
    - إعادة تشغيل الخادم:
      ```bash
      /opt/ibm/wlp/bin/server start myServer
      ```
  - **إعادة تحميل الساخن في وضع التطوير:**
    - إذا كان WLP يعمل في وضع التطوير (مثلًا عبر `server run` أو IDE)، قد يلاحظ التغييرات في `server.xml` تلقائيًا. ومع ذلك، من أجل التأكد من تحميل الميزة الجديدة، يُنصح بإعادة التشغيل.

#### 4. **التحقق من الحل**
- بعد إعادة تشغيل الخادم، أعيد نشر تطبيقك (مثلًا من خلال نسخ ملف WAR إلى دليل `dropins` أو استخدام طريقة نشرك).
- تحقق من سجلات الخادم للحصول على تأكيد نجاح النشر. ابحث عن رسائل مثل:
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  ```
  CWWKZ0001I: Application myapp started in X.XXX seconds.
  ```
- قم بزيارة تطبيقك (مثلًا `http://localhost:9080/myapp/`) للتأكد من أنه يعمل بدون أخطاء.

---

### الحل البديل: تخفيض Spring Boot

إذا لم يكن تحديث WLP إلى `jakartaee-9.1` خيارًا (مثلًا بسبب قيود التوافق مع تطبيقات أخرى)، يمكنك تخفيض تطبيق Spring Boot إلى إصدار يتوافق مع Servlet 4.0:

#### 1. **الانتقال إلى Spring Boot 2.7.x**
- يدعم Spring Boot 2.7.x Servlet 4.0 (وإصدارات سابقة مثل Servlet 3.1).
- تحديث ملف `pom.xml` لاستخدام Spring Boot 2.7.x:
  ```xml
  <parent>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-parent</artifactId>
      <version>2.7.18</version> <!-- استخدم أحدث إصدار 2.7.x -->
      <relativePath/>
  </parent>
  ```

#### 2. **إعادة بناء وإعادة نشر**
- إعادة بناء تطبيقك:
  ```bash
  mvn clean package
  ```
- أعيد نشر ملف WAR المولد إلى WLP وتحقق من أنه يبدأ بدون أخطاء.

---

### ملخص
- **سبب الخطأ:** يتطلب تطبيقك (`spring-web-6.2.3.jar`) Servlet 5.0، ولكن WLP مكوّنًا لـ Servlet 4.0.
- **الحل المفضل:** تحديث WLP لاستخدام الميزة `jakartaee-9.1` من خلال تعديل `server.xml` وإعادة تشغيل الخادم.
- **الحل البديل:** تخفيض إلى Spring Boot 2.7.x لتوافق مع دعم Servlet 4.0 لـ WLP.

يضمن الحل المفضل (تحديث WLP) أن يمكن تطبيقك استخدام أحدث ميزات Spring Boot 3.x وJakarta EE 9. اتبع الخطوات أعلاه لحل المشكلة ونشر تطبيقك بنجاح.