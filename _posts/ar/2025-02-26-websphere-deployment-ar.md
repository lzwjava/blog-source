---
audio: false
lang: ar
layout: post
title: إصلاح مشاكل نشر في WebSphere Liberty Profile
translated: true
---

عندما تحاول الوصول إلى تطبيق Spring Boot الخاص بك في `http://localhost:9080/myapp/` وتواجه خطأ "context root not found" في WebSphere Liberty Profile (WLP)، فهذا يعني أن WLP لم ينجح في نشر التطبيق تحت الجذر المتوقع (`/myapp`). عادة ما يحدث هذا بسبب مشاكل في تكوين النشر، إعدادات الخادم، أو ملف WAR نفسه. أدناه دليل شامل لتشخيص وإصلاح هذه المشكلة.

---

### فهم المشكلة
يعني خطأ "context root not found" أن WLP لا يمكن العثور على تطبيق نشر في `/myapp`. عادةً، عندما تضع ملف WAR باسم `myapp.war` في مجلد `dropins` لـ WLP، يجب أن ينشر تلقائيًا مع الجذر `/myapp`، مما يجعله متاحًا في `http://localhost:9080/myapp/`. نظرًا لأن هذا لا يحدث، علينا التحقيق في سبب فشل النشر.

---

### خطوات تشخيص المشكلة

#### 1. **تحقق من سجلات الخادم للرسائل النشر**
الخطوة الأولى هي تأكيد ما إذا كان WLP قد نشر تطبيقك.

- **تحديد السجلات:**
  - إذا كان اسم خادمك هو `myServer`، ففحص السجلات في:
    ```
    /opt/ibm/wlp/usr/servers/myServer/logs/messages.log
    ```
    أو
    ```
    /opt/ibm/wlp/usr/servers/myServer/logs/console.log
    ```
  - إذا كنت تستخدم الخادم الافتراضي، استبدل `myServer` بـ `defaultServer`.

- **بحث عن تأكيد النشر:**
  - يجب أن ترى رسالة مثل:
    ```
    [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
    ```
    وهذا يشير إلى أن التطبيق نشر ونشر.
  - بالإضافة إلى ذلك، ابحث عن:
    ```
    CWWKZ0001I: Application myapp started in X.XXX seconds.
    ```
    وهذا يثبت أن التطبيق بدأ بنجاح.

- **ما يجب فعله:**
  - إذا كانت هذه الرسائل غائبة، فلا يزال التطبيق غير منشور. ابحث عن أي رسائل `ERROR` أو `WARNING` في السجلات التي قد تشير إلى السبب (مثل الميزات المفقودة، أو أذن الملفات، أو فشل البدء).
  - إذا رأيت سجلات بدء Spring Boot (مثل شعار Spring Boot)، فإن التطبيق يتم تحميله، ويمكن أن يكون المشكلة في الجذر أو خريطة URL.

#### 2. **تحقق من موقع ملف WAR واذوناته**
تأكد من أن ملف WAR يتم وضعه بشكل صحيح في مجلد `dropins` و هو متاح لـ WLP.

- **تحقق من المسار:**
  - بالنسبة لخادم باسم `myServer`، يجب أن يكون ملف WAR في:
    ```
    /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```
  - إذا كنت تستخدم `defaultServer`، فعدل حسب الحاجة:
    ```
    /opt/ibm/wlp/usr/servers/defaultServer/dropins/myapp.war
    ```

- **تحقق من الأذونات:**
  - تأكد من أن عملية WLP لديها أذونات القراءة للملف. في نظام Unix مثل، قم بتشغيل:
    ```bash
    ls -l /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```
    يجب أن يكون الملف قابل للقراءة من قبل المستخدم الذي يعمل WLP (مثل `rw-r--r--`).

- **ما يجب فعله:**
  - إذا كان الملف مفقودًا أو غير موجود، قم بنسخه إلى مجلد `dropins` الصحيح:
    ```bash
    cp target/myapp.war /opt/ibm/wlp/usr/servers/myServer/dropins/
    ```
  - إذا كان هناك حاجة إلى إصلاح الأذونات:
    ```bash
    chmod 644 /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war
    ```

#### 3. **تأكيد مراقبة `dropins` في `server.xml`**
مجلد `dropins` لـ WLP مفعّل بشكل افتراضي، ولكن قد يكون هناك تهيئة مخصصة تعطيله.

- **تحقق من `server.xml`:**
  - افتح ملف تهيئة الخادم:
    ```
    /opt/ibm/wlp/usr/servers/myServer/server.xml
    ```
  - ابحث عن عنصر `applicationMonitor`:
    ```xml
    <applicationMonitor updateTrigger="polled" pollingRate="5s" dropins="dropins" />
    ```
    وهذا يثبت أن WLP يراقب مجلد `dropins` كل 5 ثوانٍ للبحث عن تطبيقات جديدة.

- **ما يجب فعله:**
  - إذا كان غائبًا، أضف السطر أعلاه داخل علامات `<server>` أو تأكد من عدم وجود تهيئة مفرطة تعطيل `dropins`.
  - أعيد تشغيل الخادم بعد التغييرات:
    ```bash
    /opt/ibm/wlp/bin/server stop myServer
    /opt/ibm/wlp/bin/server start myServer
    ```

#### 4. **تأكد من تمكين الميزات المطلوبة**
يحتاج WLP إلى ميزات محددة لنشر ملف WAR لـ Spring Boot، مثل دعم Servlet.

- **تحقق من `server.xml`:**
  - تأكد من أن القسم `featureManager` يحتوي على:
    ```xml
    <featureManager>
        <feature>javaee-8.0</feature>
    </featureManager>
    ```
    الميزة `javaee-8.0` تحتوي على Servlet 4.0، والتي متوافقة مع Spring Boot. أو على الأقل يجب أن يكون `servlet-4.0` موجودًا.

- **ما يجب فعله:**
  - إذا كان غائبًا، أضف الميزة وأعيد تشغيل الخادم.

#### 5. **تحقق من بنية ملف WAR**
قد يمنع ملف WAR الفاسد أو غير المهيأ بشكل صحيح من النشر.

- **تحقق من WAR:**
  - فك ضغط ملف WAR للتحقق من محتوياته:
    ```bash
    unzip -l myapp.war
    ```
  - ابحث عن:
    - `WEB-INF/classes/com/example/demo/HelloController.class` (فئة التحكم الخاصة بك).
    - `WEB-INF/lib/` يحتوي على اعتمادات Spring Boot (مثل `spring-web-x.x.x.jar`).

- **ما يجب فعله:**
  - إذا كانت البنية غير صحيحة، أعيد بناء WAR:
    ```bash
    mvn clean package
    ```
    تأكد من أن `pom.xml` يحدد `<packaging>war</packaging>` ويحدد `spring-boot-starter-tomcat` كـ `<scope>provided</scope>`.

#### 6. **نشر بديل عبر مجلد `apps`**
إذا فشل `dropins`، حاول نشر التطبيق بشكل صريح عبر مجلد `apps`.

- **الخطوات:**
  - نقل ملف WAR:
    ```bash
    mv /opt/ibm/wlp/usr/servers/myServer/dropins/myapp.war /opt/ibm/wlp/usr/servers/myServer/apps/
    ```
  - تعديل `server.xml` لإضافة:
    ```xml
    <application id="myapp" name="myapp" type="war" location="${server.config.dir}/apps/myapp.war">
        <context-root>/myapp</context-root>
    </application>
    ```
  - أعيد تشغيل الخادم:
    ```bash
    /opt/ibm/wlp/bin/server restart myServer
    ```

- **اختبار مرة أخرى:**
  - زور `http://localhost:9080/myapp/`. إذا كان يعمل، كانت المشكلة في `dropins`.

#### 7. **تحقق من حالة الخادم**
تأكد من أن الخادم يعمل بشكل صحيح.

- **تحقق من الحالة:**
  ```bash
  /opt/ibm/wlp/bin/server status myServer
  ```
  - إذا كان متوقفًا، ابدأه:
    ```bash
    /opt/ibm/wlp/bin/server start myServer
    ```

- **اختبار WLP نفسه:**
  - زور `http://localhost:9080/`. إذا كان WLP يعمل، فسترى صفحة مرحبا (إلا إذا تم استبدالها). إذا فشل هذا، هناك مشكلة أوسع في الخادم.

---

### الحل
لإصلاح خطأ "context root not found":

1. **ابدأ من هنا:**
   - تحقق من سجلات الخادم (`messages.log` أو `console.log`) للرسائل النشر أو الأخطاء.
   - تأكد من أن `myapp.war` في مجلد `dropins` مع أذونات صحيحة.

2. **الخطوات التالية:**
   - تأكد من أن `server.xml` يفعّل الميزة `javaee-8.0` ويراقب `dropins`.
   - إذا لم يتم حل المشكلة، نشر عبر مجلد `apps` مع تهيئة `<application>` صريحة في `server.xml`.

3. **التحقق النهائي:**
   - بعد إجراء التغييرات، أعيد تشغيل WLP و زور `http://localhost:9080/myapp/`. يجب أن ترى "Hello World!" إذا نجح النشر.

بمتابعة هذه الخطوات، ستعرف ما إذا كانت المشكلة تتعلق بتهيئة الخادم، أو موقع WAR، أو ملف WAR نفسه، وتحلها بشكل مناسب.