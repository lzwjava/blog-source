---
audio: false
generated: true
image: false
lang: ar
layout: post
title: جاكوكو لتغطية ليبرتي جيه في إم
translated: true
type: note
---

يمكنك فعل ذلك—اربط JaCoCo بـ **Liberty JVM** الذي يشغّل EAR الخاص بك. النقطة الأساسية هي: يجب أن يكون JaCoCo داخل نفس JVM مثل Liberty، وليس داخل مشغّل Python الخاص بك.

إليك الإعدادات الموثوقة (اختر واحدة).

---

## 1) بسيط وقوي: الكتابة إلى ملف عند إنهاء JVM

**متى تستخدم:** عندما يمكنك إيقاف خادم Liberty بعد الاختبارات.

1. **اجعل ملف الـ agent jar متاحًا** (مرة واحدة في عملية البناء الخاصة بك)

```xml
<!-- copy jacoco agent into target/jacoco/jacocoagent.jar -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-dependency-plugin</artifactId>
  <version>3.6.1</version>
  <executions>
    <execution>
      <id>copy-jacoco-agent</id>
      <phase>prepare-package</phase>
      <goals><goal>copy</goal></goals>
      <configuration>
        <artifactItems>
          <artifactItem>
            <groupId>org.jacoco</groupId>
            <artifactId>org.jacoco.agent</artifactId>
            <version>0.8.12</version>
            <classifier>runtime</classifier>
            <destFileName>jacocoagent.jar</destFileName>
          </artifactItem>
        </artifactItems>
        <outputDirectory>${project.build.directory}/jacoco</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
```

2. **أضف خيار JVM لـ Liberty** (في الملف: `wlp/usr/servers/<serverName>/jvm.options`)

```text
-javaagent:${server.config.dir}/jacoco/jacocoagent.jar=output=file,append=false,includes=com.myco.*,excludes=org.slf4j.*,destfile=${server.output.dir}/jacoco/jacoco-it.exec
```

* ضع `jacocoagent.jar` في `wlp/usr/servers/<serverName>/jacoco/` (أو أي مسار قابل للقراءة).
* عدّل `includes`/`excludes` ليناسب الحزم الخاصة بك.

3. **تدفق التشغيل**

* شغّل Liberty (`server start <serverName>`)، ونزّل EAR.
* شغّل اختبارات Python `unittest` الخاصة بك (ستصل إلى النقاط الطرفية).
* أوقف Liberty (`server stop <serverName>`).
  ← سيكتب الـ agent الملف `${server.output.dir}/jacoco/jacoco-it.exec`.

4. **إنشاء التقرير**

* إذا كان مشروعك متعدد الوحدات (EAR + EJB + WAR)، استخدم pom aggregate و `report-aggregate`:

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <executions>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report-aggregate</goal></goals>
      <configuration>
        <dataFile>${env.SERVER_OUTPUT_DIR}/jacoco/jacoco-it.exec</dataFile>
        <includes>
          <include>com/myco/**</include>
        </includes>
      </configuration>
    </execution>
  </executions>
</plugin>
```

(أو استخدم `jacococli`:)

```bash
java -jar jacococli.jar report /path/to/jacoco-it.exec \
  --classfiles module1/target/classes --classfiles module2/target/classes \
  --sourcefiles module1/src/main/java --sourcefiles module2/src/main/java \
  --html target/jacoco-it-report
```

---

## 2) تفريغ حي دون إيقاف Liberty (وضع خادم TCP)

**متى تستخدم:** عندما تريد إبقاء Liberty قيد التشغيل وسحب التغطية عند الطلب.

1. `jvm.options`:

```text
-javaagent:${server.config.dir}/jacoco/jacocoagent.jar=output=tcpserver,address=*,port=6300,append=false,includes=com.myco.*
```

2. شغّل Liberty، نفّذ اختبارات Python، ثم **قم بالتفريغ**:

```bash
# pulls coverage over TCP and writes a .exec locally
java -jar jacococli.jar dump --address 127.0.0.1 --port 6300 --destfile jacoco-it.exec --reset
```

الآن أنشئ التقرير كما هو مذكور أعلاه.
ملاحظة: `--reset` يمسح العدادات حتى تتمكن من أخذ لقطات متعددة أثناء جلسة تشغيل طويلة.

---

## 3) الحاويات / CI (نمط البيئة)

* إذا كنت تشغّل Liberty في Docker/K8s، ثبّت الـ agent وعيّن:

  * `jvm.options` كما هو مذكور أعلاه، **أو**
  * متغيرات البيئة `WLP_JAVA_OPTIONS` / `JAVA_TOOL_OPTIONS` تحتوي على نفس `-javaagent=...`.
* بالنسبة للعناقيد التي تحتوي على عدة JVMs من Liberty، أعط كل واحدة منفذ TCP أو مسار ملف مختلف، ثم **ادمج**:

```bash
java -jar jacococli.jar merge node1.exec node2.exec --destfile merged.exec
```

---

## ملاحظات ومطبات شائعة

* **تخطيط EAR لا يهم** JaCoCo؛ فهو يقوم بتجهيز bytecode في الذاكرة. إنشاء التقارير يحتاج فقط إلى **ملفات الـ class الأصلية** من وحداتك (`target/classes`) ومصادرها لإنشاء HTML منسق.
* استخدم **إصدار JaCoCo حديث (0.8.12+)** لتكون متوافقًا مع Java 17/21 (غالبًا ما يعمل Liberty على OpenJ9/HotSpot—كلاهما جيد).
* راقب `includes/excludes` لتجنب حساب مكتبات الطرف الثالث.
* إذا كان ملف `.exec` فارغًا، فمن المحتمل أنك:

  * نسيت إرفاق الـ agent،
  * أو استبعدت الحزم الخاصة بك،
  * أو قمت بسحب التفريغ قبل أن يصل الزحف إلى الكود.

---

إذا شاركت تخطيط الوحدات الخاص بـ EAR (وحدات EJB/WAR وجذور الحزم)، يمكنني إضافة إعداد `report-aggregate` دقيق ونص برمجي صغير لـ: تشغيل Liberty → تشغيل اختبارات Python → جلب التفريغ → بناء تقرير HTML في خطوة واحدة.