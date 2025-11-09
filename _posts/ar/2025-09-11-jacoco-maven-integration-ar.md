---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: فهم تكامل جاكوكو ومافن
translated: true
type: note
---

حسنًا — إليك كيف تعمل أجزاء JaCoCo في **ملف POM الخاص بك بالضبط** معًا، خطوة بخطوة، والسبب.

---

# تدفقَي التغطية اللذين ينشئهما ملف POM هذا

1. **تغطية اختبارات الوحدة (مسار Surefire)**

* تربط **`prepare-agent`** الخاص بـ JaCoCo بدون أي إعدادات خاصة:

  ```xml
  <execution>
    <id>prepare-agent</id>
    <goals><goal>prepare-agent</goal></goals>
  </execution>
  ```

  هذا يحقن `-javaagent:...org.jacoco.agent-<ver>-runtime.jar` في JVM اختبار **Surefire** عبر خاصية `argLine`.
  • **الملف الهدف** الافتراضي هو `${project.build.directory}/jacoco.exec`.
  • **الإلحاق** الافتراضي هو `true` (عميل JaCoCo يلحق البيانات عندما يكون الملف موجودًا بالفعل).
  • التأثير: عند تشغيل اختبارات الوحدة (إن وجدت) أثناء `test`، تذهب التغطية إلى `target/jacoco.exec`.

2. **تغطية اختبارات التكامل (مسار Jetty)**

* تحدد **ملفًا منفصلًا** لتغطية اختبارات التكامل:

  ```xml
  <properties>
    <jacoco.it.exec>${project.build.directory}/jacoco-it.exec</jacoco.it.exec>
  </properties>
  ```
* تبدأ تشغيل Jetty **مع عميل JaCoCo الخاص به** مشيرًا إلى ذلك الملف:

  ```xml
  <plugin>
    <artifactId>jetty-maven-plugin</artifactId>
    ...
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals><goal>start</goal></goals>
      <configuration>
        <daemon>true</daemon>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec}
        </jvmArgs>
        ...
      </configuration>
    </execution>
  </plugin>
  ```

  • يعمل Jetty في **JVM منفصل**؛ يقوم العميل الخاص به بالكتابة إلى `target/jacoco-it.exec`.
  • لأن `append` غير محددة، ينطبق الافتراضي لـ JaCoCo وهو `append=true` — لذا فإن عمليات تشغيل Jetty المتعددة ستلحق البيانات بنفس الملف ما لم تقم بالتنظيف أو تعيين `append=false`.

---

# تدفق دورة الحياة (ما يحدث عند `mvn verify`)

1. **compile**

   * يتم تنسيق الكود بـ Spotless (`spotless-maven-plugin`) وتشغيل Checkstyle (`maven-checkstyle-plugin`).
   * يتم تحضير ملف WAR الخاص بك (`maven-war-plugin`).

2. **test (Surefire)**

   * إذا كان لديك اختبارات وحدة، فإنها تعمل تحت سطر الأوامر المحقون **`prepare-agent`** → تذهب التغطية إلى `target/jacoco.exec`.

3. **pre-integration-test**

   * يبدأ تشغيل Jetty **في وضع الخدمة الخلفية**:

     ```xml
     <daemon>true</daemon>
     ```

     يستعيد Maven السيطرة فورًا؛ يستمر Jetty في العمل مع عميل JaCoCo مرفق، ويكتب في `jacoco-it.exec`.

4. **integration-test**

   * تصل اختبارات Python الخاصة بك إلى التطبيق قيد التشغيل:

     ```xml
     <plugin>
       <artifactId>exec-maven-plugin</artifactId>
       <execution>
         <id>python-integration-tests</id>
         <phase>integration-test</phase>
         <goals><goal>exec</goal></goals>
         <configuration>
           <executable>python3</executable>
           <workingDirectory>${project.parent.basedir}</workingDirectory>
           <arguments>
             <argument>-m</argument><argument>unittest</argument>
             <argument>discover</argument><argument>tests/</argument>
             <argument>-v</argument>
           </arguments>
         </configuration>
       </execution>
     </plugin>
     ```

     تختبر هذه الاختبارات تطبيق Jetty، لذا تتراكم التغطية في **`target/jacoco-it.exec`** عبر عميل JVM الخاص بـ Jetty.

5. **post-integration-test**

   * يتم إيقاف Jetty بطريقة نظيفة:

     ```xml
     <execution>
       <id>stop-jetty</id>
       <phase>post-integration-test</phase>
       <goals><goal>stop</goal></goals>
       ...
     </execution>
     ```

6. **verify**

   * تقوم بإنشاء **تقرير منفصل لاختبارات التكامل** باستخدام ملف بيانات اختبارات التكامل ومجلد إخراج مخصص:

     ```xml
     <execution>
       <id>report-it</id>
       <phase>verify</phase>
       <goals><goal>report</goal></goals>
       <configuration>
         <dataFile>${jacoco.it.exec}</dataFile>
         <outputDirectory>${project.reporting.outputDirectory}/jacoco-it
         </outputDirectory>
       </configuration>
     </execution>
     ```
   * النتيجة: يذهب HTML إلى `target/site/jacoco-it/index.html` يلخص **فقط** تغطية **التكامل** (من Jetty).

> ملاحظة: إذا كنت تريد أيضًا تقريرًا لـ **اختبارات الوحدة**، يمكنك إضافة تنفيذ آخر لـ `jacoco:report` يشير إلى `target/jacoco.exec` الافتراضي ويخرج إلى `target/site/jacoco` — مما يحافظ على فصل تقارير الوحدة واختبارات التكامل.

---

# حول "إنشاء جديد أم استبدال؟" لملفات `.exec`

* **الافتراضي لعميل JaCoCo هو `append=true`**.

  * بالنسبة **لاختبارات الوحدة**، الملف هو `target/jacoco.exec`. عند تشغيل `mvn verify` بشكل متكرر **بدون `clean`**، قد تلحق البيانات عبر عمليات التشغيل.
  * بالنسبة **لـ Jetty IT**، `jvmArgs` الخاصة بك لا تتجاوز `append`، لذا فإن `target/jacoco-it.exec` أيضًا **يلحق** بشكل افتراضي.

**أفضل ممارسة** (لتجنب خلط البيانات القديمة):

* قم بتشغيل `mvn clean verify`، **أو** أضف `append=false` في سطر عميل Jetty:

  ```xml
  -javaagent:...org.jacoco.agent-...-runtime.jar=destfile=${jacoco.it.exec},append=false
  ```
* إذا أردت دمج ملفات `.exec` متعددة عن قصد، استخدم `jacoco:merge` قبل `jacoco:report`.

---

# ما يفعله كل كتلة ذات صلة في XML الأصلي الخاص بك (حسب المرجع)

* **موقع ملف IT**

  ```xml
  <properties>
    <jacoco.it.exec>${project.build.directory}/jacoco-it.exec</jacoco.it.exec>
    <it.report.skip>false</it.report.skip>
  </properties>
  ```

  يحدد مكان تخزين تغطية التكامل. `it.report.skip` مُعلن عنه ولكنه غير موصول بعد بتنفيذ التقرير (انظر النصيحة أدناه).

* **عميل اختبار الوحدة (مسار Surefire)**

  ```xml
  <plugin>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
      <execution>
        <id>prepare-agent</id>
        <goals><goal>prepare-agent</goal></goals>
      </execution>
      ...
    </executions>
  </plugin>
  ```

* **Jetty مع JaCoCo لـ IT**

  ```xml
  <plugin>
    <artifactId>jetty-maven-plugin</artifactId>
    ...
    <jvmArgs>
      -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec}
    </jvmArgs>
    ...
  </plugin>
  ```

* **اختبارات تكامل Python أثناء تشغيل Jetty**

  ```xml
  <plugin>
    <artifactId>exec-maven-plugin</artifactId>
    <execution>
      <id>python-integration-tests</id>
      <phase>integration-test</phase>
      <goals><goal>exec</goal></goals>
      ...
    </execution>
  </plugin>
  ```

* **إنشاء تقرير تغطية IT عند verify**

  ```xml
  <execution>
    <id>report-it</id>
    <phase>verify</phase>
    <goals><goal>report</goal></goals>
    <configuration>
      <dataFile>${jacoco.it.exec}</dataFile>
      <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
    </configuration>
  </execution>
  ```

---

# نصائح عملية / تحسينات صغيرة

* **تجنب بيانات IT قديمة**
  أضف `append=false` إلى عميل Jetty (كما هو موضح أعلاه)، أو قم دائمًا بتشغيل `mvn clean verify`.

* **وصل مفتاح `it.report.skip` الخاص بك**
  إذا كنت تريد تخطي إنشاء تقرير IT عبر خاصية:

  ```xml
  <execution>
    <id>report-it</id>
    <phase>verify</phase>
    <goals><goal>report</goal></goals>
    <configuration>
      <skip>${it.report.skip}</skip>
      <dataFile>${jacoco.it.exec}</dataFile>
      <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
    </configuration>
  </execution>
  ```

* **احتفظ بتقارير الوحدة و IT منفصلة**
  لقد فصلت بالفعل تقرير IT إلى `site/jacoco-it`. إذا كنت تحتاج أيضًا إلى تقرير الوحدة، أضف `jacoco:report` آخر (بدون تجاوز `dataFile`) يكتب إلى `site/jacoco`.

* **ملاحظة حول الوحدات المتعددة**
  هذا الإعداد المحلي للوحدة يقدم تقارير التغطية لـ **PlaygroundWeb** فقط. إذا أردت لاحقًا عرضًا **مدمجًا**، استخدم `jacoco:merge` (لدمج ملفات `.exec`) و/أو `report-aggregate` من `pom` أبوي بـ `packaging=pom` (JaCoCo 0.8.8+).

---

# ملخص سريع

* **اختبارات الوحدة** → `prepare-agent` يحقن JaCoCo في JVM الخاص بـ Surefire → `target/jacoco.exec`.
* **اختبارات التكامل** → يبدأ Jetty مع عميل JaCoCo الخاص به → `target/jacoco-it.exec`.
* **التقرير** → عند `verify`، يقوم `jacoco:report` بعرض **فقط تغطية IT** إلى `target/site/jacoco-it`.
* **سلوك الملف** → JaCoCo **يلحق بشكل افتراضي**؛ يُفضل استخدام `mvn clean verify` أو `append=false` لتجنب خلط عمليات التشغيل.