---
audio: false
generated: true
image: false
lang: ar
layout: post
title: حلول لمشاكل إضافة مافن لتوم كات
translated: true
type: note
---

لقد حصلت على الدليل الرئيسي مباشرة في سجلك:

> `[INFO] Skipping non-war project`

لم يبدأ أي شيء لأن **إضافة tomcat7-maven-plugin تعمل فقط على تطبيقات الويب المُعبأة كـ WAR** بتخطيط `src/main/webapp` الكلاسيكي. مشروعك على الأرجح مُعبأ حاليًا كـ JAR، لذا فإن الإضافة تخرج ببساطة بعد البناء.

هناك عقبة ثانية: أنت تستخدم **Tomcat 11** (واجهات برمجة تطبيقات Jakarta `jakarta.*`)، لكن تبعياتك هي **Spring 5.2.x** (تستخدم `javax.*`). هذا التباين يعني أنه حتى لو بدأ Tomcat، فإن النشر العادي على Tomcat 11 سيفشل دون ترحيل. استخدم Tomcat 9 (javax) مع Spring 5، أو قم بترقية التطبيق إلى Spring 6/Jakarta ليعمل مع Tomcat 10/11.

إليك المسارات الواضحة التي يمكنك اختيارها — اختر واحدة وستعمل:

### المسار 1 — ابق على Spring 5، وشغّله محليًا باستخدام إضافة Jetty (الأسرع)

لا حاجة لـ WAR؛ جيد للتجريب والتطوير.

1. أضف الإضافة:

   ```xml
   <plugin>
     <groupId>org.eclipse.jetty</groupId>
     <artifactId>jetty-maven-plugin</artifactId>
     <version>9.4.54.v20240208</version>
   </plugin>
   ```
2. شغّل:

   ```bash
   mvn jetty:run -Djetty.port=8080
   ```

هذا يستخدم `javax.*`، متوافق مع Spring 5.

### المسار 2 — ابق على Spring 5، أنشئ WAR، واستخدم إضافة Tomcat7

1. في `pom.xml` عيّن التعبئة كـ WAR:

   ```xml
   <packaging>war</packaging>
   ```
2. تأكد من وجود تخطيط تطبيق الويب:

   ```
   src/main/webapp/
   src/main/webapp/WEB-INF/web.xml   # اختياري إذا كان لديك مُهيئ Servlet 3
   ```
3. (اختياري) أضف تهيئة الإضافة:

   ```xml
   <plugin>
     <groupId>org.apache.tomcat.maven</groupId>
     <artifactId>tomcat7-maven-plugin</artifactId>
     <version>2.2</version>
     <configuration>
       <path>/</path>
       <port>8080</port>
     </configuration>
   </plugin>
   ```
4. شغّل:

   ```bash
   mvn tomcat7:run            # لتطبيق ويب مُنفجر (exploded)
   # أو
   mvn package && mvn tomcat7:run-war
   ```

### المسار 3 — ابق على Spring 5، ونشّر على Tomcat 9 منفصل

هذا يتوافق مع `javax.*` دون تغيير الكود.

```bash
brew install tomcat@9
/opt/homebrew/opt/tomcat@9/bin/catalina start
```

ابنِ مشروعك وأسقط ملف WAR في `.../tomcat@9/libexec/webapps/`.

### المسار 4 — قم بترقية التطبيق إلى Spring 6/Jakarta، والتزم باستخدام Tomcat 11

إذا كنت تريد إصدار Tomcat حديث:

* ارتقِ إلى Spring Framework 6.x / Spring Boot 3.x.
* غيّر الاستيرادات من `javax.*` إلى `jakarta.*`.
* عندها سيعمل Tomcat 10/11 بشكل جيد.

---

#### لماذا أظهر `mvn tomcat7:run` نجاحًا ولكن "لم يحدث شيء"

* اكتملت مراحل Maven بنجاح، لكن الإضافة رأت أن **نوع التعبئة ليس WAR**، لذا **لم تبدأ** Tomcat مضمّن. هذا بالضبط ما يعنيه "Skipping non-war project".

---

إذا أخبرتني بأي مسار تفضل، سأعطيك ملف `pom.xml` الدقيق والملفات الدنيا لذلك الإعداد (بما في ذلك وحدة تحكم صغيرة وكيفية الوصول إليها عبر `http://localhost:8080/hello`).