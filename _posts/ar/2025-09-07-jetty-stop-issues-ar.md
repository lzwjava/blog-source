---
audio: false
date: 2025-09-07
generated: true
image: false
lang: ar
layout: post
title: إصلاح مشاكل إيقاف جتي المتفرعة
translated: true
type: note
---

لقد قمت في الواقع بمعظم الأمور بشكل صحيح — المشكلة تكون دائمًا تقريبًا بسبب **عدم تمكن هدف الإيقاف من الوصول إلى Jetty المتشعب** (stopHost/port/key scope خاطئ) أو بسبب **استمرار `run-forked` في إبقاء Maven متصلاً** بشكل غير متوقع. إليك حلان فعّالان أدناه؛ اختر أحدهما.

### الخيار أ — النمط الموثوق: `jetty:start` (خفي daemon) + `jetty:stop`

هذا يتجنب `run-forked` تمامًا وهو الأكثر استقرارًا لدورات حياة اختبار التكامل.

**ما الذي يجب تغييره**

1. ثبّت إصدار الإضافة plugin واستخدم `start` مع `daemon=true` في `pre-integration-test`.
2. احتفظ باختبارات التكامل الخاصة بـ Python في `integration-test`.
3. استخدم `stop` في `post-integration-test`.
4. وفر *نفس* `stopHost/stopPort/stopKey` في **كلا** عمليتي التنفيذ executions.

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <version>9.4.54.v20240208</version>

  <configuration>
    <httpConnector>
      <port>8080</port>
      <host>127.0.0.1</host>
    </httpConnector>
  </configuration>

  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals>
        <goal>start</goal>
      </goals>
      <configuration>
        <daemon>true</daemon>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec},append=true
        </jvmArgs>
        <webApp>
          <contextPath>/</contextPath>
        </webApp>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals>
        <goal>stop</goal>
      </goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>
      </configuration>
    </execution>
  </executions>
</plugin>
```

**لماذا يُصلح هذا المشكلة "التوقف"**

* `daemon=true` تجعل `start` تُعيد التحكم إلى Maven فورًا، حتى يمكن لاختبارات التكامل أن تعمل.
* تطابق `stopHost/stopPort/stopKey` يضمن أن هدف `stop` يصل إلى نفس نسخة Jetty.
* لا يوجد اعتماد على سلوك خيط المراقبة monitor thread الخاص بـ `run-forked`.

---

### الخيار ب — احتفظ بـ `run-forked`، ولكن اجعل الإيقاف يعمل فعلًا

إذا كنت تفضل `run-forked`، فإن المزالق الشائعة هي:

* إعدادات `stopHost` الافتراضية قد تختلف عن كيفية ربط العملية الفرعية (IPv6 مقابل IPv4).
* `stopPort/stopKey` يتم تعيينها فقط في عملية التنفيذ البدء **وليس** منعكسة على عملية تنفيذ الإيقاف.
* العملية الفرعية لا تعرض معالج الإيقاف stop handler إذا كان التكوين في غير مكانه.

**شدد التكوين هكذا:**

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <version>9.4.54.v20240208</version>

  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals>
        <goal>run-forked</goal>
      </goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>

        <httpConnector>
          <host>127.0.0.1</host>
          <port>8080</port>
        </httpConnector>

        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec},append=true
        </jvmArgs>
        <webApp>
          <contextPath>/</contextPath>
        </webApp>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals>
        <goal>stop</goal>
      </goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>
      </configuration>
    </execution>
  </executions>
</plugin>
```

**إجراءات وقائية إضافية**

* أضف `-Djava.net.preferIPv4Stack=true` إلى `jvmArgs` الخاصة بالعملية الفرعية إذا كان نظام macOS/Java الخاص بك يختار IPv6 بينما يستخدم هدف الإيقاف IPv4:

  ```
  <jvmArgs>
    -Djava.net.preferIPv4Stack=true
    -javaagent:...
  </jvmArgs>
  ```
* تأكد من عدم وجود أي شيء آخر على المنفذ `8081`. إذا كان هناك شيء، غيّر كلاً من البدء والإيقاف إلى منفذ حر آخر.
* إذا تعطلت اختبارات التكامل أو توقفت عن الاستجابة، فقد لا يتم تشغيل `post-integration-test` مطلقًا؛ في هذه الحالة، أضف شبكة أمان احتياطية للقتل في مرحلة `verify` (انظر أدناه).

---

### شبكة أمان اختيارية — اقتل العملية الفرعية إذا فشل `stop`

أضف أداة مساعدة صغيرة لقتل نسخة Jetty المتشعبة قسريًا باستخدام معرف العملية PID المكتوب في ملف:

1. في تكوين `run-forked`/`start`:

```
<pidFile>${project.build.directory}/jetty.pid</pidFile>
```

2. بعد `post-integration-test`، أضف `exec-maven-plugin` في `verify` يتحقق من ملف pid ويدمر العملية إذا كانت لا تزال نشطة.

---

### ملاحظتان بسيطتان من سجلك

* `No Spring WebApplicationInitializer types detected` أمر طبيعي إذا كنت تستخدم `web.xml` + DispatcherServlet؛ لا علاقة له بتوقف الاستجابة.
* فكر في نقل اختبارات التكامل إلى **maven-failsafe-plugin** (يرتبط بـ `integration-test`/`verify`) واحتفظ باختبارات الوحدة على surefire. نهج `exec-maven-plugin` الحالي يعمل، لكن failsafe يتكامل بشكل أفضل مع دورة حياة اختبار التكامل.

---

إذا أردت، الصق **كامل** كتلة إضافة Jetty الخاصة بك + أي مرايا mirrors في `settings.xml` (لمسار المستودع المحلي) وسأعدل الفرق الأدنى الدقيق لمستودعك.