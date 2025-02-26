---
audio: false
lang: ar
layout: post
title: تطبيق خادم Java على WebSphere Liberty Profile
translated: true
---

هنا دليل شامل لتشغيل تطبيق Servlet بسيط جدًا على WebSphere Liberty Profile (WLP). يخلق هذا المثال Servlet أساسيًا يعيد "Hello World!" ويقوم بتفريغه إلى WLP باستخدام مجلد `dropins`. سنفترض أنك قمت بالفعل بتكوين WLP مع ميزة `servlet-4.0` مفعلة، حيث توفر الدعم اللازم لServlet. يجنب هذا الدليل استخدام Maven ويقدم كل الكود والخطوات اللازمة للتفريغ.

---

### دليل خطوة بخطوة

#### 1. إنشاء هيكل تطبيق Servlet
إنشاء هيكل مجلدات لبرنامج Servlet يدويًا. يمكنك استخدام أي اسم مجلد، ولكن في هذا المثال سنسميه `SimpleServletApp`.

- **هيكل المجلدات:**
  ```
  SimpleServletApp/
  ├── src/
  │   └── com/
  │       └── example/
  │           └── HelloServlet.java
  └── webapp/
      └── WEB-INF/
          └── web.xml
  ```

#### 2. كتابة كود Servlet
إنشاء ملف باسم `HelloServlet.java` في `SimpleServletApp/src/com/example/` مع المحتوى التالي:

```java
package com.example;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        resp.setContentType("text/plain");
        resp.getWriter().write("Hello World!");
    }
}
```

- **شرح:** هذا Servlet يستجيب لطلبات HTTP GET بـ "Hello World!" كنص عادي. نحن نستخدم طريقة `doGet` بسيطة دون تعليقات للحصول على أقصى قدر من التوافق والتسهل.

#### 3. إنشاء ملف الوصف `web.xml`
إنشاء ملف باسم `web.xml` في `SimpleServletApp/webapp/WEB-INF/` مع المحتوى التالي:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
    <servlet>
        <servlet-name>HelloServlet</servlet-name>
        <servlet-class>com.example.HelloServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>HelloServlet</servlet-name>
        <url-pattern>/hello</url-pattern>
    </servlet-mapping>
</web-app>
```

- **شرح:** يربط ملف `web.xml` فئة `HelloServlet` بنمط URL `/hello`. هذا ضروري لأننا لا نستخدم تعليقات مثل `@WebServlet`.

#### 4. تجميع Servlet
تجميع ملف `HelloServlet.java` إلى ملف `.class` باستخدام `javac`. ستحتاج إلى مكتبة `javax.servlet-api` في مسار التصنيف الخاص بك، والتي يوفرها WLP ولكن يجب أن تكون متاحة أثناء التجميع.

- **الخطوات:**
  1. تحديد ملف Servlet API JAR في تثبيت WLP الخاص بك. على سبيل المثال، إذا كان WLP مثبتًا في `/opt/ibm/wlp`، يكون الملف JAR عادةً في:
     ```
     /opt/ibm/wlp/dev/api/spec/com.ibm.websphere.javaee.servlet.4.0_1.0.x.jar
     ```
     قد يختلف اسم الملف بناءً على إصدار WLP الخاص بك.
  2. تشغيل الأمر التالي من مجلد `SimpleServletApp`:
     ```bash
     javac -cp "/opt/ibm/wlp/dev/api/spec/com.ibm.websphere.javaee.servlet.4.0_1.0.x.jar" src/com/example/HelloServlet.java
     ```
  3. هذا يخلق `HelloServlet.class` في `SimpleServletApp/src/com/example/`.

#### 5. حزم التطبيق في ملف WAR
تنظيم الملفات المتجميعة وإعداد ملف WAR يدويًا.

- **نقل الملف المتجميع:**
  إنشاء مجلد `WEB-INF/classes` ونقل الملفات المتجميعة:
  ```bash
  mkdir -p webapp/WEB-INF/classes/com/example
  mv src/com/example/HelloServlet.class webapp/WEB-INF/classes/com/example/
  ```

- **إنشاء ملف WAR:**
  من مجلد `SimpleServletApp`، استخدم الأمر `jar` لتعبئة مجلد `webapp` في ملف WAR:
  ```bash
  cd webapp
  jar -cvf ../myapp.war .
  cd ..
  ```
  هذا يخلق `myapp.war` في مجلد `SimpleServletApp`.

#### 6. نشر ملف WAR على WLP
نشر ملف WAR إلى WLP باستخدام مجلد `dropins` للتفريغ التلقائي.

- **تحديد مجلد `dropins`:**
  العثور على مجلد `dropins` للمخدم الخاص بك. إذا كان WLP مثبتًا في `/opt/ibm/wlp` واسم المخدم هو `myServer`، يكون المسار:
  ```
  /opt/ibm/wlp/usr/servers/myServer/dropins
  ```

- **نسخ ملف WAR:**
  نقل ملف WAR إلى مجلد `dropins`:
  ```bash
  cp myapp.war /opt/ibm/wlp/usr/servers/myServer/dropins/
  ```

- **بدء المخدم (إذا لم يكن يعمل):**
  إذا لم يكن WLP يعمل، ابدأه:
  ```bash
  /opt/ibm/wlp/bin/server start myServer
  ```
  إذا كان يعمل بالفعل، فإنه سيكتشف وتفريغ ملف WAR تلقائيًا.

- **التحقق من التفريغ:**
  تحقق من سجلات المخدم أو الواجهة الأمامية للحصول على رسالة مثل:
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  سجلات في `/opt/ibm/wlp/usr/servers/myServer/logs/console.log`.

#### 7. الوصول إلى التطبيق
اختبار Servlet المتفريغ في المتصفح.

- **فتح متصفحك:**
  انتقل إلى:
  ```
  http://localhost:9080/myapp/hello
  ```
  - `9080` هو الميناء الافتراضي لـ WLP.
  - `/myapp` هو الجذر السياق من اسم ملف WAR.
  - `/hello` هو نمط URL المحدد في `web.xml`.

- **النتيجة المتوقعة:**
  يجب أن ترى:
  ```
  Hello World!
  ```
  كنص عادي.

---

### ملاحظات
- **لا يوجد JSP:** طلب الاستعلام عن ملفات JSP، ولكن للحفاظ على هذا *بسيط جدًا*، قمت بالتركيز على تطبيق Servlet فقط. يمكن إضافة JSPs إذا لزم الأمر.
- **جذر السياق:** يأتي جذر السياق (`/myapp`) من اسم ملف WAR. إعادة تسمية `myapp.war` لتغييره (على سبيل المثال، `app.war` لـ `/app`).
- **رقم الميناء:** يحدد WLP `9080` كميناء افتراضي لـ HTTP. تحقق من `server.xml` إذا كان مختلفًا.
- **إصدار Java:** استخدم إصدار Java متوافق مع WLP (على سبيل المثال، Java 8 أو 11).
- **إصلاح الأخطاء:** إذا لم يعمل، تحقق من `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` للحصول على الأخطاء، تأكد من أن ملف WAR في `dropins`، وتأكد من تشغيل المخدم.

---

### ملخص
يوضح هذا الدليل كيفية:
1. إنشاء Servlet بسيط (`HelloServlet.java`) و `web.xml`.
2. تجميع Servlet بدون Maven باستخدام `javac`.
3. حزمه في ملف WAR (`myapp.war`) يدويًا.
4. نشره إلى مجلد `dropins` لـ WLP.
5. الوصول إلى "Hello World!" في `http://localhost:9080/myapp/hello`.

يوفر هذا دليلًا بسيطًا ومباشرًا لServlet التطبيق يعمل على WebSphere Liberty Profile دون أدوات بناء مثل Maven.