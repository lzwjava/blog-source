---
audio: false
generated: true
lang: ar
layout: post
title: أداة الاعتماد Maven
translated: true
---

**إضافة Maven Dependency Plugin** هو أداة قوية في Maven، أداة بناء تلقائي شائعة الاستخدام لمشاريع Java، تساعدك على إدارة وتعديل الاعتماديات للمشروع. الاعتماديات في مشروع Maven هي مكتبات خارجية أو وحدات تم إعلانها في ملف `pom.xml`، والتي تنزيلها Maven من المستودعات وتجعلها متاحة أثناء التجميع، أو التشغيل، أو الاختبار. يوسع Plugin هذه الوظيفة من خلال تقديم أهداف مختلفة (مهام) لتحليل، نسخ، قائمة، أو معالجة هذه الاعتماديات. إليك كيفية استخدامه بشكل فعال:

---

#### **1. نظرة عامة على الاستخدام**
يمكنك استخدام Plugin Maven Dependency Plugin بطريقتين رئيسيتين:
- **تكوينه في ملف `pom.xml`**: هذا يسمح لك بربط أهداف Plugin محددة بمراحل دورة حياة بناء Maven (مثل `package`, `install`) لتنفذ تلقائيًا أثناء عملية البناء.
- **تنفيد الأهداف مباشرة من سطر الأوامر**: هذا مفيد لمهام فردية أو عندما لا تريد تعديل ملف `pom.xml`.

يحدد Plugin بواسطة إحداثياته: `groupId: org.apache.maven.plugins`, `artifactId: maven-dependency-plugin`. عليك تحديد إصدار (مثل `3.2.0`) عند تكوينه، على الرغم من أن Maven يمكن أن يحل الإصدار الأخير إذا تم إغفاله في استخدام سطر الأوامر.

---

#### **2. إضافة Plugin إلى `pom.xml`**
لاستخدام Plugin كجزء من عملية البناء، أضفه إلى قسم `<build><plugins>` من ملف `pom.xml`. إليك مثال أساسي:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-dependency-plugin</artifactId>
            <version>3.2.0</version>
        </plugin>
    </plugins>
</build>
```

مع هذه الإعدادات، يمكنك تكوين أهداف محددة لتنفيذها أثناء دورة حياة البناء من خلال إضافة أقسام `<executions>`.

---

#### **3. الأهداف الشائعة وكيفية استخدامها**
يوفر Plugin عدة أهداف لإدارة الاعتماديات. إليك بعض الأهداف الأكثر استخدامًا، مع أمثلة على كيفية استخدامها:

##### **a. `copy-dependencies`**
- **الغرض**: نسخ الاعتماديات للمشروع إلى دليل محدد (مثل حزمة في مجلد `lib`).
- **مُكوّن في `pom.xml`**:
  ربط هذه الهدف بمرحلة `package` لنقل الاعتماديات أثناء `mvn package`:

  ```xml
  <build>
      <plugins>
          <plugin>
              <groupId>org.apache.maven.plugins</groupId>
              <artifactId>maven-dependency-plugin</artifactId>
              <version>3.2.0</version>
              <executions>
                  <execution>
                      <id>copy-dependencies</id>
                      <phase>package</phase>
                      <goals>
                          <goal>copy-dependencies</goal>
                      </goals>
                      <configuration>
                          <outputDirectory>${project.build.directory}/lib</outputDirectory>
                          <includeScope>runtime</includeScope>
                      </configuration>
                  </execution>
              </executions>
          </plugin>
      </plugins>
  </build>
  ```

  - `${project.build.directory}/lib` يتحول إلى `target/lib` في مشروعك.
  - `<includeScope>runtime</includeScope>` يقصر النسخ على الاعتماديات التي لها نطاق `compile` و `runtime`، ويغفل `test` و `provided`.

- **سطر الأوامر**:
  تنفذه مباشرة دون تعديل `pom.xml`:

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib
  ```

##### **b. `tree`**
- **الغرض**: عرض شجرة الاعتماديات، تظهر جميع الاعتماديات المباشرة والعكسية وأصنافها. هذا مفيد لتحديد تنازعات الأصدارات.
- **سطر الأوامر**:
  تنفذه ببساطة:

  ```bash
  mvn dependency:tree
  ```

  هذا يوفر عرض هرمي للاعتماديات في الشاشة.
- **مُكوّن في `pom.xml`** (اختياري):
  إذا كنت تريد تنفيذه أثناء مرحلة بناء (مثل `verify`), فاكتبه بنفس طريقة `copy-dependencies`.

##### **c. `analyze`**
- **الغرض**: تحليل الاعتماديات لتحديد المشاكل مثل:
  - الاعتماديات المستخدمة ولكن غير معلنة.
  - الاعتماديات المعلنة ولكن غير مستخدمة.
- **سطر الأوامر**:
  تنفذه:

  ```bash
  mvn dependency:analyze
  ```

  هذا يولد تقرير في الشاشة.
- **ملاحظة**: قد يتطلب هذا الهدف تكوينًا إضافيًا لمشاريع معقدة لتحسين تحليله.

##### **d. `list`**
- **الغرض**: قائمة جميع الاعتماديات المحلولة للمشروع.
- **سطر الأوامر**:
  تنفذه:

  ```bash
  mvn dependency:list
  ```

  هذا يوفر قائمة مسطحة للاعتماديات، مفيدة للمراجع السريعة.

##### **e. `unpack`**
- **الغرض**: استخراج محتويات اعتمادية محددة (مثل ملف JAR) إلى دليل.
- **سطر الأوامر**:
  مثال لاستخراج اعتمادية محددة:

  ```bash
  mvn dependency:unpack -Dartifact=groupId:artifactId:version -DoutputDirectory=target/unpacked
  ```

  استبدل `groupId:artifactId:version` بإحداثيات الاعتمادية (مثل `org.apache.commons:commons-lang3:3.12.0`).

##### **f. `purge-local-repository`**
- **الغرض**: إزالة الاعتماديات المحددة من مستودع Maven المحلي (`~/.m2/repository`), مما يضمن تنزيلها من المستودعات البعيدة.
- **سطر الأوامر**:
  تنفذه:

  ```bash
  mvn dependency:purge-local-repository
  ```

  هذا مفيد لحل ملفات الاعتماديات الفاسدة.

---

#### **4. خيارات التخصيص**
تسمح العديد من الأهداف بتكوين متغيرات لتخصيص سلوكها:
- **`outputDirectory`**: يحدد مكان نسخ أو استخراج الملفات (مثل `target/lib`).
- **`includeScope` أو `excludeScope`**: تصفية الاعتماديات حسب النطاق (مثل `runtime`, `test`).
- **`artifact`**: يحدد اعتمادية محددة لأهداف مثل `unpack`.

يمكن تعيين هذه المتغيرات في قسم `<configuration>` من `pom.xml` أو تمريرها كمتغيرات سطر الأوامر مع `-D` (مثل `-DincludeScope=runtime`).

---

#### **5. أمثلة عملية**
- **سيناريو 1: حزم تطبيق مستقل**
  استخدم `copy-dependencies` لجمع جميع الاعتماديات التشغيلية في مجلد `lib`:

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib -DincludeScope=runtime
  ```

- **سيناريو 2: تصحيح تنازعات الاعتماديات**
  تنفذ `dependency:tree` لفحص الاعتماديات العكسية:

  ```bash
  mvn dependency:tree
  ```

  إذا لاحظت عدة اصدارات لمكتبة (مثل `commons-logging`), حل التنازع من خلال إضافة قسم `<dependencyManagement>` في `pom.xml`.

- **سيناريو 3: استخراج الموارد**
  استخرج اعتمادية للوصول إلى محتواها:

  ```bash
  mvn dependency:unpack -Dartifact=org.example:my-lib:1.0.0 -DoutputDirectory=target/resources
  ```

---

#### **6. ملخص**
لاستخدام Plugin Maven Dependency:
- أضفه إلى `pom.xml` مع أهداف ومكوّنات محددة إذا كنت تريد دمجه في عملية البناء.
- تنفذ أهداف مثل `copy-dependencies`, `tree`, `analyze`, `list`, أو `unpack` مباشرة من سطر الأوامر لمهام فردية.
- تخصيص السلوك باستخدام خيارات التكوين لتناسب احتياجات مشروعك.

هذا Plugin أداة متعددة الاستخدامات لإدارة الاعتماديات أكثر من مجرد إعلان، مما يجعلها قيمة في بناء، تصحيح الأخطاء، وتوزيع مشاريع Maven.