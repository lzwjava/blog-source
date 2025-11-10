---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دليل تعبئة WAR مقابل EAR
translated: true
type: note
---

إليك مقارنة عملية بدون جداول بين تعبئة Maven **WAR** مقابل **EAR** وكيفية استخدام كل منهما في المشاريع الحقيقية.

# الغرض من كل نوع تعبئة

*   **WAR (`packaging: war`)** – تطبيق ويب منفرد: Servlets/Jakarta REST، JSP/JSF، Spring MVC/Boot (كـ WAR)، إلخ. يتم نشره على حاوية سيرفلات (Tomcat/Jetty) أو طبقة الويب في خادم تطبيقات كامل.
*   **EAR (`packaging: ear`)** – حزمة من وحدات متعددة يتم نشرها معًا إلى خادم تطبيقات Java EE/Jakarta EE كامل (WildFly/JBoss EAP, WebLogic, WebSphere). تحتوي عادةً على واحد أو أكثر من ملفات WAR، وملفات EJB JAR، والمكتبات المشتركة مع وحدة نشر واحدة.

# متى تختار كلًا منهما بشكل نموذجي

*   اختر **WAR** إذا كان لديك تطبيق ويب منفرد أو تطبيق Spring Boot ولا تحتاج إلى EJBs أو ميزات الخادم متعددة الوحدات.
*   اختر **EAR** إذا كان يجب عليك نشر عدة وحدات معًا (مثل EJBs + عدة ملفات WAR + مكتبات مشتركة)، أو كنت تحتاج إلى خدمات خادم التطبيقات (XA، مجالات الأمان المركزية، JMS، المعاملات الموزعة) عبر الوحدات، أو إذا كانت مؤسستك تفرض استخدام EARs.

# محتويات الـ Artifact

*   محتويات **WAR**: `/WEB-INF/classes`، `/WEB-INF/lib`، `web.xml` اختياري (أو annotations)، والأصول الثابتة. يوجد مُحَمِّل فئات (classloader) واحد لكل WAR في معظم الخوادم.
*   محتويات **EAR**: `*.war`، `*.jar` (EJBs/utility)، `META-INF/application.xml` (أو annotations/skinny config)، و `lib/` اختياري للمكتبات المشتركة بين جميع الوحدات. يوفر مُحَمِّل فئات (classloader) على مستوى EAR يكون مرئيًا لجميع الوحدات.

# اعتبارات الاعتماديات وتحميل الفئات

*   **WAR**: عرّف واجهات برمجة تطبيقات السيرفلات/Jakarta EE كـ `provided`؛ كل شيء آخر يوضع في `/WEB-INF/lib`. العزل أبسط؛ تقل فيه تصادمات الإصدارات.
*   **EAR**: ضع المكتبات المشتركة في `lib/` الخاصة بالـ EAR (عبر `maven-ear-plugin`)، بحيث تشارك جميع الوحدات إصدارًا واحدًا. انتبه للتعارضات بين مكتبات الوحدات وواجهات برمجة التطبيقات التي يوفرها الخادم؛ وائِم بين الإصدارات واستخدم `provided` حيثما كان ذلك مناسبًا.

# إضافات Maven التي ستستخدمها

*   **مشاريع WAR**: `maven-war-plugin`
*   **مجمّع EAR**: `maven-ear-plugin`
*   **وحدات EJB (إن وجدت)**: `maven-ejb-plugin`
*   غالبًا ما يستخدم المشروع الأصلي/المجمّع `packaging: pom` لربط الوحدات معًا.

# أمثلة بسيطة

تطبيق ويب منفرد (WAR):

```xml
<!-- pom.xml -->
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId><artifactId>my-web</artifactId><version>1.0.0</version>
  <packaging>war</packaging>

  <dependencies>
    <!-- Use provided for server APIs -->
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-web-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
    <!-- Your app deps -->
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.4.0</version>
        <!-- Optional: configure webResources, warName, filtering -->
      </plugin>
    </plugins>
  </build>
</project>
```

EAR متعدد الوحدات مع WAR و EJB:

```xml
<!-- parent/pom.xml -->
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId><artifactId>my-app</artifactId><version>1.0.0</version>
  <packaging>pom</packaging>
  <modules>
    <module>ejb-module</module>
    <module>web-module</module>
    <module>ear-assembly</module>
  </modules>
</project>
```

```xml
<!-- ejb-module/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>ejb-module</artifactId>
  <packaging>ejb</packaging>
  <dependencies>
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
  </dependencies>
</project>
```

```xml
<!-- web-module/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>web-module</artifactId>
  <packaging>war</packaging>
  <dependencies>
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-web-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
    <dependency>
      <groupId>com.example</groupId><artifactId>ejb-module</artifactId><version>1.0.0</version>
      <type>ejb</type> <!-- allows @EJB injection -->
    </dependency>
  </dependencies>
</project>
```

```xml
<!-- ear-assembly/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>ear-assembly</artifactId>
  <packaging>ear</packaging>

  <dependencies>
    <dependency>
      <groupId>com.example</groupId><artifactId>web-module</artifactId><version>1.0.0</version>
      <type>war</type>
    </dependency>
    <dependency>
      <groupId>com.example</groupId><artifactId>ejb-module</artifactId><version>1.0.0</version>
      <type>ejb</type>
    </dependency>
    <!-- Libraries to put in EAR/lib shared by all modules -->
    <dependency>
      <groupId>com.fasterxml.jackson.core</groupId><artifactId>jackson-databind</artifactId>
      <version>2.17.2</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-ear-plugin</artifactId>
        <version>3.4.0</version>
        <configuration>
          <defaultLibBundleDir>lib</defaultLibBundleDir>
          <modules>
            <webModule>
              <groupId>com.example</groupId>
              <artifactId>web-module</artifactId>
              <contextRoot>/myapp</contextRoot>
            </webModule>
            <ejbModule>
              <groupId>com.example</groupId>
              <artifactId>ejb-module</artifactId>
            </ejbModule>
          </modules>
          <!-- Optional: generate application.xml, or provide a custom one -->
          <generateApplicationXml>true</generateApplicationXml>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

نتيجة البناء:

*   `mvn -pl web-module -am clean package` → `web-module-1.0.0.war`
*   `mvn -pl ear-assembly -am clean package` → `ear-assembly-1.0.0.ear` يحتوي على WAR، EJB، و `lib/`.

# الاختلافات التشغيلية المهمة

*   **هدف النشر**

    *   WAR: حاوية سيرفلات أو طبقة الويب في خادم التطبيقات.
    *   EAR: خادم تطبيقات كامل؛ ينشر جميع الوحدات بشكل ذري.
*   **المعاملات والمراسلة**

    *   يستخدم WAR بمفرده ما يعرضه الخادم؛ غالبًا ما توجد إعدادات XA/JMS المعقدة داخل EJBs ضمن ملفات EAR.
*   **إدارة الإصدارات والنشر**

    *   WAR: إعادة بناء ونشر تطبيق منفرد أمر بسيط.
    *   EAR: يتطلب تنسيق إصدارات العديد من الوحدات؛ وحدة نشر واحدة لضمان الاتساق.
*   **وقت البدء والتطوير المحلي**

    *   WAR: ملاحظات سريعة، وقت تشغيل أخف.
    *   EAR: أثقل؛ يساعد التكامل مع IDE/الخادم ولكن دورات التطوير أبطأ.
*   **ملاحظة حول Spring Boot الحديث**

    *   يفضل Boot **JAR** القابل للتنفيذ؛ يتم دعم WAR إذا كنت تنشر على حاوية خارجية.
    *   لا يستهدف Boot **EAR**؛ إذا كان يجب عليك استخدام خادم تطبيقات، انشر Boot كـ WAR، وتجنب EAR إلا إذا تطلبه منصتك.

# الأخطاء الشائعة والنصائح

*   استخدم `provided` لواجهات برمجة تطبيقات الخادم لتجنب تضمينها.
*   بالنسبة لـ EARs، ضع المكتبات المشتركة في `defaultLibBundleDir` لمنع وجود نسخ مكررة داخل كل WAR/EJB.
*   وائِم إصدارات Jakarta EE عبر جميع الوحدات؛ يؤدي عدم التطابق إلى أخطاء في تحميل الفئات.
*   على WebLogic/WebSphere، انتبه لسياسات تحميل الفئات (parent-first vs parent-last)؛ أحيانًا تحتاج إلى أوصاف (descriptors) خاصة بالبائع.
*   إذا كنت لا تحتاج إلى EJBs/XA، فإن WAR عادي (أو Boot JAR) يكون أبسط وعادةً ما يكون أكثر قابلية للنقل.

إذا أخبرتني بخادم التطبيقات الذي تستخدمه (Tomcat مقابل WildFly/WebLogic/etc.) وما إذا كان لديك EJBs أو تطبيقات ويب متعددة، يمكنني رسم ملفات POM وأوصاف النشر التي ستحتاجها بالضبط.