---
audio: false
generated: true
lang: ar
layout: post
title: إضافة مافن
translated: true
type: note
---

**إضافة Maven Dependency Plugin** هي أداة قوية في Maven، وهي أداة أتمتة بناء مستخدمة على نطاق واسع لمشاريع جافا، تساعدك في إدارة ومعالجة تبعيات المشروع. التبعيات في مشروع Maven هي مكتبات أو وحدات خارجية يتم التصريح عنها في ملف `pom.xml`، والتي يقوم Maven بتنزيلها من المستودعات وتوفيرها أثناء عملية الترجمة أو وقت التشغيل أو الاختبار. تقوم هذه الإضافة بتوسيع هذه الوظيفة من خلال توفير أهداف (مهام) متنوعة لتحليل أو نسخ أو سرد أو التعامل مع هذه التبعيات بطرق أخرى. إليك كيفية استخدامها بفعالية:

---

#### **1. نظرة عامة على الاستخدام**
يمكنك استخدام إضافة Maven Dependency Plugin بطريقتين رئيسيتين:
- **تكوينها في ملف `pom.xml`**: يسمح لك هذا بربط أهداف محددة للإضافة بمراحل دورة حياة بناء Maven (مثل `package`، `install`) لتنفيذها تلقائيًا أثناء عملية البناء.
- **تشغيل الأهداف مباشرة من سطر الأوامر**: هذا مثالي للمهام لمرة واحدة أو عندما لا ترغب في تعديل ملف `pom.xml`.

يتم التعرف على الإضافة من خلال إحداثياتها: `groupId: org.apache.maven.plugins`، `artifactId: maven-dependency-plugin`. ستحتاج إلى تحديد إصدار (مثل `3.2.0`) عند تكوينها، على الرغم من أن Maven يمكنه غالبًا حل أحدث إصدار إذا تم حذفه في استخدام سطر الأوامر.

---

#### **2. إضافة الإضافة إلى `pom.xml`**
لاستخدام الإضافة كجزء من عملية البناء الخاصة بك، أضفها إلى قسم `<build><plugins>` في ملف `pom.xml`. إليك مثال أساسي:

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

مع هذا الإعداد، يمكنك تكوين أهداف محددة لتنفيذها أثناء دورة حياة البناء عن طريق إضافة كتل `<executions>`.

---

#### **3. الأهداف الشائعة وكيفية استخدامها**
توفر الإضافة عدة أهداف لإدارة التبعيات. فيما يلي بعض أكثرها استخدامًا، مع أمثلة على كيفية استخدامها:

##### **أ. `copy-dependencies`**
- **الغرض**: نسخ تبعيات المشروع إلى دليل محدد (مثل، لتغليفها في مجلد `lib`).
- **التكوين في `pom.xml`**:
  اربط هذا الهدف بمرحلة `package` لنسخ التبعيات أثناء `mvn package`:

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

  - `${project.build.directory}/lib` يحل إلى `target/lib` في مشروعك.
  - `<includeScope>runtime</includeScope>` يحدد النسخ للتبعيات ذات النطاقات `compile` و `runtime`، باستثناء `test` و `provided`.

- **سطر الأوامر**:
  شغله مباشرة دون تعديل `pom.xml`:

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib
  ```

##### **ب. `tree`**
- **الغرض**: عرض شجرة التبعيات، مما يظهر جميع التبعيات المباشرة وغير المباشرة وإصداراتها. هذا مفيد لتحديد تعارضات الإصدارات.
- **سطر الأوامر**:
  ببساطة شغل:

  ```bash
  mvn dependency:tree
  ```

  هذا يخرج عرضًا هرميًا للتبعيات إلى وحدة التحكم.
- **التكوين في `pom.xml`** (اختياري):
  إذا أردت أن يعمل هذا أثناء مرحلة بناء (مثل `verify`)، قم بتكوينه بشكل مشابه لـ `copy-dependencies`.

##### **ج. `analyze`**
- **الغرض**: يحلل التبعيات لتحديد المشكلات، مثل:
  - التبعيات المستخدمة ولكن غير المصرح عنها.
  - التبعيات المصرح عنها ولكن غير المستخدمة.
- **سطر الأوامر**:
  شغل:

  ```bash
  mvn dependency:analyze
  ```

  هذا يولد تقريرًا في وحدة التحكم.
- **ملاحظة**: قد يتطلب هذا الهدف تكوينًا إضافيًا للمشاريع المعقدة لتحسين تحليله.

##### **د. `list`**
- **الغرض**: يسرد جميع التبعيات المحلولة للمشروع.
- **سطر الأوامر**:
  شغل:

  ```bash
  mvn dependency:list
  ```

  هذا يوفر قائمة مسطحة للتبعيات، مفيدة للمرجع السريع.

##### **هـ. `unpack`**
- **الغرض**: يستخرج محتويات تبعية محددة (مثل، ملف JAR) إلى دليل.
- **سطر الأوامر**:
  مثال لاستخراج قطعة أثرية محددة:

  ```bash
  mvn dependency:unpack -Dartifact=groupId:artifactId:version -DoutputDirectory=target/unpacked
  ```

  استبدل `groupId:artifactId:version` بإحداثيات التبعية (مثل `org.apache.commons:commons-lang3:3.12.0`).

##### **و. `purge-local-repository`**
- **الغرض**: يزيل تبعيات محددة من مستودع Maven المحلي الخاص بك (`~/.m2/repository`)، مما يجبر على تنزيل جديد من المستودعات البعيدة.
- **سطر الأوامر**:
  شغل:

  ```bash
  mvn dependency:purge-local-repository
  ```

  هذا مفيد لاستكشاف أخطاء ملفات التبعيات التالفة وإصلاحها.

---

#### **4. خيارات التخصيص**
تدعم العديد من الأهداف معلمات التكوين لتخصيص سلوكها:
- **`outputDirectory`**: يحدد مكان نسخ أو استخراج الملفات (مثل `target/lib`).
- **`includeScope` أو `excludeScope`**: يرشح التبعيات حسب النطاق (مثل `runtime`، `test`).
- **`artifact`**: يستهدف تبعية محددة لأهداف مثل `unpack`.

يمكن تعيين هذه في قسم `<configuration>` في `pom.xml` أو تمريرها كوسائط سطر أوامر باستخدام `-D` (مثل `-DincludeScope=runtime`).

---

#### **5. أمثلة عملية**
- **السيناريو 1: تغليف تطبيق قائم بذاته**
  استخدم `copy-dependencies` لجمع جميع تبعيات وقت التشغيل في مجلد `lib`:

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib -DincludeScope=runtime
  ```

- **السيناريو 2: تصحيح تعارضات التبعيات**
  شغل `dependency:tree` لفحص التبعيات غير المباشرة:

  ```bash
  mvn dependency:tree
  ```

  إذا لاحظت وجود إصدارات متعددة لمكتبة (مثل `commons-logging`)، قم بحل التعارض عن طريق إضافة قسم `<dependencyManagement>` في `pom.xml`.

- **السيناريو 3: استخراج الموارد**
  استخرج تبعية للوصول إلى محتوياتها:

  ```bash
  mvn dependency:unpack -Dartifact=org.example:my-lib:1.0.0 -DoutputDirectory=target/resources
  ```

---

#### **6. الملخص**
لاستخدام إضافة Maven Dependency Plugin:
- أضفها إلى `pom.xml` الخاص بك بأهداف وتكوينات محددة إذا أردت دمجها في عملية البناء الخاصة بك.
- شغل أهدافًا مثل `copy-dependencies`، `tree`، `analyze`، `list`، أو `unpack` مباشرة من سطر الأوامر للمهام المؤقتة.
- خصص السلوك باستخدام خيارات التكوين لتناسب احتياجات مشروعك.

هذه الإضافة هي أداة متعددة الاستخدامات لإدارة التبعيات تتجاوز التصريح البسيط، مما يجعلها لا تقدر بثمن لبناء وتصحيح أخطاء وتوزيع مشاريع Maven.