---
audio: false
date: 2025-09-08
generated: true
image: false
lang: ar
layout: post
title: استراتيجية تغطية التكامل لآلة جافا الافتراضية الواحدة
translated: true
type: note
---

لا تحتاج إلى تشغيل Jetty مرتين أو إنشاء ملف `.exec` منفصل لـ JaCoCo لكل وحدة. يمكن لعامل واحد على JVM المنفرد الذي يخدم ملف WAR الخاص بك تسجيل التغطية **لجميع الفئات التي يحملها JVM** — بما في ذلك `PlaygroundUtils` — في **ملف exec مشترك واحد**. ثم يمكن لكل وحدة إنشاء تقريرها الخاص بالإشارة إلى نفس ملف exec. لمشروع كبير (10+ وحدات)، هذا الحل قابل للتطوير بشكل أنيق.

فيما يلي خطة ملموسة وحد الأدنى والتعديلات الجاهزة لمستودعك.

---

## الاستراتيجية

1.  **استخدم ملف exec موحدًا ومشتركًا لاختبارات التكامل على مستوى المشروع الرئيسي.**
    شغّل Jetty **مرة واحدة**، مع تكوين JaCoCo، ليكتب في المسار `../target/it-coverage/jacoco-it.exec` (مسار على مستوى المشروع الرئيسي).
2.  **شغّل اختبارات Python الخارجية مرة واحدة.**
    ستصل هذه الاختبارات إلى التطبيق المُنشَر؛ وسيسجل العامل الزيارات لجميع الفئات المحملة (الويب والمكتبات).
3.  **أنشئ تقارير لكل وحدة**، حيث تشير كل وحدة إلى ملف `jacoco-it.exec` المشترك.
    سيحصل `PlaygroundUtils` على تقرير حتى لو لم يكن لديه اختبارات — فهو يربط ملف exec المشترك بملفات `target/classes` الخاصة به.
4.  (اختياري) **أنشئ أيضًا تقرير HTML مجمع** على مستوى المشروع الرئيسي باستخدام `report-aggregate`، أو اكتفِ بتقارير كل وحدة على حدة.

فقط عندما يكون لديك حقًا **عدة JVMs** (على سبيل المثال، عدة خدمات صغيرة) ستحتاج إلى عدة ملفات exec وخطوة `jacoco:merge`. لبناء JVM المنفرد الحالي (Jetty)، حافظ على استخدام ملف exec واحد.

---

## التعديلات المحددة

### 1) الملف الرئيسي `pom.xml` (PlaygroundLib)

أضف خصائص مشتركة حتى تتمكن كل وحدة من الإشارة إلى نفس ملف exec:

```xml
<properties>
  <!-- ... إصداراتك الحالية ... -->
  <it.coverage.dir>${project.basedir}/target/it-coverage</it.coverage.dir>
  <jacoco.it.exec>${it.coverage.dir}/jacoco-it.exec</jacoco.it.exec>
  <!-- تبديل إنشاء تقرير اختبار التكامل لكل وحدة -->
  <it.report.skip>false</it.report.skip>
</properties>
```

(اختياري) إذا كنت تريد **تقرير HTML مجمع** واحد على مستوى المشروع الرئيسي، أضف هذا التنفيذ:

```xml
<build>
  <pluginManagement>
    <!-- احتفظ بكتلاتك الحالية -->
  </pluginManagement>

  <plugins>
    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>it-aggregate-report</id>
          <phase>verify</phase>
          <goals>
            <goal>report-aggregate</goal>
          </goals>
          <configuration>
            <!-- استخدم ملف exec لاختبارات التكامل المشترك الناتج عن تشغيل Jetty -->
            <dataFile>${jacoco.it.exec}</dataFile>
            <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

> إذا رفض إصدار JaCoCo الخاص بك `<dataFile>` في `report-aggregate`، فتخطَّ هذه الكتلة الاختيارية واعتمد على التقارير لكل وحدة أدناه. يمكنك دائمًا إضافة وحدة تجميع تغطية صغيرة لاحقًا لتشغيل `merge` + `report`.

---

### 2) `PlaygroundWeb/pom.xml`

وجّه عامل Jetty إلى مسار ملف exec **على مستوى المشروع الرئيسي** ومكّن الإلحاق:

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals><goal>start</goal></goals>
      <configuration>
        <daemon>true</daemon>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${project.parent.basedir}/target/it-coverage/jacoco-it.exec,append=true,includes=org.lzw.*
        </jvmArgs>
        <httpConnector>
          <port>8080</port>
          <host>127.0.0.1</host>
        </httpConnector>
        <webApp><contextPath>/</contextPath></webApp>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals><goal>stop</goal></goals>
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

حدّث `jacoco:report` في `PlaygroundWeb` لقراءة **نفس** ملف exec المشترك:

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <executions>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report</goal></goals>
      <configuration>
        <dataFile>${project.parent.basedir}/target/it-coverage/jacoco-it.exec</dataFile>
        <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
```

إن البرنامج المساعد Maven Plugin الحالي الذي يشغل `python -m unittest discover tests -v` مثالي — اتركه كما هو.

---

### 3) `PlaygroundUtils/pom.xml`

أضف تنفيذًا **للإبلاغ فقط** حتى يتمكن من ربط ملف exec المشترك بفئاته الخاصة:

```xml
<build>
  <plugins>
    <!-- احتفظ بالبرامج المساعدة الحالية -->

    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>report-it</id>
          <phase>verify</phase>
          <goals><goal>report</goal></goals>
          <configuration>
            <dataFile>${project.parent.basedir}/target/it-coverage/jacoco-it.exec</dataFile>
            <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
            <skip>${it.report.skip}</skip>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

هذه الوحدة لا تشغّل Jetty أو تشغّل Python أبدًا؛ إنها تستهلك فقط ملف exec المشترك وملفات `target/classes` الخاصة بها. إذا تم استخدام أي فئات من `PlaygroundUtils` بواسطة تطبيق الويب أثناء الاختبارات، فستظهر مع بيانات التغطية. إذا لم يتم استدعاؤها، فستكون النسبة 0% — وهي الإشارة الصحيحة.

---

## كيفية التشغيل

من جذر المستودع:

```bash
mvn -pl PlaygroundWeb -am clean verify
```

ترتيب البناء يترجم كلا الوحدتين، يشغّل Jetty مرة واحدة مع العامل، يشغّل اختبارات Python الخاصة بك، يوقف Jetty، ثم يولد:

* `PlaygroundWeb/target/site/jacoco-it/index.html`
* `PlaygroundUtils/target/site/jacoco-it/index.html`
* تقريرًا مجمعًا اختياريًا تحت المشروع الرئيسي إذا كنت قد مكّنت `report-aggregate`.

---

## عندما يكون لديك 10 وحدات

* إذا انتهى الأمر بجميع الـ 10 داخل **نفس WAR/JVM**، حافظ على نمط **ملف exec المشترك المنفرد**. تضيف كل وحدة تنفيذ `report` يشير إلى ملف exec المشترك. لا تزال تشغّل Jetty مرة واحدة وتشغّل Python مرة واحدة.

* إذا كان لديك **عدة JVMs** (على سبيل المثال، خدمات منفصلة)، امنح كل JVM ملف `destfile` الخاص به (مثل `it-coverage/serviceA.exec`، `serviceB.exec`)، ثم في المشروع الرئيسي شغّل:

  ```xml
  <plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
      <execution>
        <id>merge-it</id>
        <phase>post-integration-test</phase>
        <goals><goal>merge</goal></goals>
        <configuration>
          <destFile>${project.basedir}/target/it-coverage/jacoco-merged.exec</destFile>
          <files>
            <file>${project.basedir}/target/it-coverage/serviceA.exec</file>
            <file>${project.basedir}/target/it-coverage/serviceB.exec</file>
            <!-- أضف المزيد حسب الحاجة -->
          </files>
        </configuration>
      </execution>

      <execution>
        <id>aggregate-report</id>
        <phase>verify</phase>
        <goals><goal>report-aggregate</goal></goals>
        <configuration>
          <dataFile>${project.basedir}/target/it-coverage/jacoco-merged.exec</dataFile>
          <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
        </configuration>
      </execution>
    </executions>
  </plugin>
  ```

* إذا أردت تقليل الضوضاء، اضبط `includes=org.lzw.*` (موضح سابقًا) أو أضف `excludes` إلى سطر العامل لتصفية مكتبات الطرف الثالث.

---

## سبب المشكلة الحالية

* كنت تنشئ **ملفات exec لكل وحدة**، مما جعلك مضطرًا لإعادة تشغيل Jetty بعوامل مختلفة لملء كل منها. هذا غير ضروري. لا يهم العامل الوحدة التي "تنتمي" إليها الفئة — فهو يسجل أي فئة محملة. ركّز ملف exec في مكان واحد ووجّه `report` لكل وحدة إليه.

---

## قائمة مراجعة سريعة

* ملف **مشترك** واحد `${jacoco.it.exec}` تحت المشروع الرئيسي.
* تشغيل Jetty **مرة واحدة** مع `append=true` و `includes=org.lzw.*`.
* تشغيل اختبارات Python **مرة واحدة**.
* لكل وحدة `jacoco:report` يقرأ ملف exec المشترك.
* (اختياري) `report-aggregate` على مستوى المشروع الرئيسي للحصول على HTML واحد شامل.

هذا يجب أن يجعل إعدادك أبسط وأكثر قابلية للتطوير. إذا أردت، يمكنني إنتاج فروقات محددة لملفات POM الحالية الخاصة بك مع تطبيق هذه التغييرات.