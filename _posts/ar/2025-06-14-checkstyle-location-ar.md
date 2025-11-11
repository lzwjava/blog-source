---
audio: false
generated: true
lang: ar
layout: post
title: موقع إعدادات Checkstyle
translated: true
type: note
---

لإصلاح المشكلات التي تواجهها مع `maven-checkstyle-plugin` عند تشغيل `mvn clean checkstyle:check`، حيث لا يمكنه العثور على ملف `checks.xml` وفشل في تهيئة وحدة `SuppressWithNearbyTextFilter`، اتبع هذه الخطوات. تنبع المشكلات من موقع الملف وإصدار Checkstyle غير المتوافق. إليك الحل الكامل:

---

### الخطوة 1: إصلاح موقع ملف `checks.xml`
يشير الخطأ إلى أن البرنامج المساعد لا يمكنه العثور على `checks.xml`. نظرًا لأنه موجود في الجذر الرئيسي لمشروعك (وليس في `src/main/resources`، حيث يبحث البرنامج المساعد عادةً)، تحتاج إلى إخبار البرنامج المساعد صراحةً بمكان العثور عليه.

- **الإجراء**: قم بتحديث `<configLocation>` في ملف `pom.xml` للإشارة إلى الجذر الرئيسي للمشروع.

---

### الخطوة 2: حل خطأ `SuppressWithNearbyTextFilter`
تفشل وحدة `SuppressWithNearbyTextFilter` في التهيئة لأن إصدار Checkstyle الذي يستخدمه البرنامج المساعد قديم ولا يدعم هذا المرشح. تحتاج إلى ترقية البرنامج المساعد وتحديد إصدار متوافق من Checkstyle.

- **الإجراء**: قم بترقية `maven-checkstyle-plugin` إلى الإصدار `3.3.1` وأضف تبعية لإصدار Checkstyle `10.17.0`، الذي يدعم `SuppressWithNearbyTextFilter`.

---

### تكوين `pom.xml` المحدث
قم بتعديل قسم `maven-checkstyle-plugin` في ملف `pom.xml` على النحو التالي:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-checkstyle-plugin</artifactId>
    <version>3.3.1</version> <!-- الترقية إلى أحدث إصدار -->
    <configuration>
        <configLocation>${project.basedir}/checks.xml</configLocation> <!-- الإشارة إلى checks.xml في الجذر الرئيسي للمشروع -->
    </configuration>
    <dependencies>
        <dependency>
            <groupId>com.puppycrawl.tools</groupId>
            <artifactId>checkstyle</artifactId>
            <version>10.17.0</version> <!-- يدعم SuppressWithNearbyTextFilter -->
        </dependency>
    </dependencies>
    <executions>
        <execution>
            <id>checkstyle-check</id>
            <phase>compile</phase>
            <goals>
                <goal>check</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

#### الشرح:
- **`<configLocation>${project.basedir}/checks.xml</configLocation>`**: يحدد أن `checks.xml` موجود في الجذر الرئيسي للمشروع (`${project.basedir}` هو خاصية Maven للدليل الرئيسي).
- **`الإصدار 3.3.1`**: يستخدم إصدارًا أحدث من البرنامج المساعد للحصول على توافق أفضل.
- **تبعية Checkstyle `10.17.0`**: يضمن أن البرنامج المساعد يستخدم إصدار Checkstyle الذي يتضمن `SuppressWithNearbyTextFilter`.

---

### الخطوة 3: التحقق من تكوين `checks.xml`
تأكد من أن وحدة `SuppressWithNearbyTextFilter` في ملف `checks.xml` محددة بشكل صحيح. قد يبدو مثال التكوين كما يلي:

```xml
<module name="SuppressWithNearbyTextFilter">
    <property name="nearbyTextPattern" value="@SuppressWarnings"/>
</module>
```

- **الإجراء**: تحقق من وجود أخطاء إملائية أو خصائص غير صحيحة في `checks.xml`. راجع [توثيق Checkstyle](https://checkstyle.org/filters/suppresswithnearbytextfilter.html) للحصول على التفاصيل.
- **نصيحة استكشاف الأخطاء وإصلاحها**: إذا استمر الخطأ، قم بإزالة وحدة `SuppressWithNearbyTextFilter` مؤقتًا من `checks.xml` وشغل `mvn checkstyle:check` لمعرفة ما إذا كانت المشكلة خاصة بهذا المرشح.

---

### الخطوة 4: اختبار الإصلاح
- شغل الأمر التالي للاختبار:
  ```bash
  mvn clean checkstyle:check
  ```
- إذا عمل بشكل صحيح، يجب أن يجد البرنامج المساعد `checks.xml` ويعالج جميع الوحدات دون أخطاء.
- للتأكد من تشغيل Checkstyle أثناء الترجمة، استخدم:
  ```bash
  mvn compile
  ```

---

### اختياري: موقع بديل للملف
إذا كنت تفضل إعداد Maven أكثر تقليدية:
- انقل `checks.xml` إلى `src/main/resources/checks.xml`.
- قم بتحديث `<configLocation>` إلى:
  ```xml
  <configLocation>classpath:checks.xml</configLocation>
  ```
- يتماشى هذا مع اصطلاح Maven لوضع الموارد في `src/main/resources`.

---

### ملاحظات إضافية
- **تحذير غير مرتبط**: إذا رأيت تحذيرًا حول علامة `<blocked>` في `/usr/share/maven/conf/settings.xml`، فهذا غير مرتبط بهذه المشكلة ولكنه يشير إلى مشكلة في ملف إعدادات Maven الخاص بك. راجعه بشكل منفصل إذا لزم الأمر.
- **لا تزال تواجه مشاكل؟** شارك ما يلي لمزيد من المساعدة:
  - محتوى (أو مقتطف) من `checks.xml`.
  - الناتج الكامل لـ `mvn clean checkstyle:check -X` (وضع التصحيح).

---

من خلال تطبيق هذه التغييرات، يجب أن يحدد `maven-checkstyle-plugin` موقع `checks.xml` بشكل صحيح ويدعم `SuppressWithNearbyTextFilter`، مما يحل الأخطاء الخاصة بك.

---

أشار الخطأ الذي واجهته سابقًا إلى أن `maven-checkstyle-plugin` لم يتمكن من العثور على `checks.xml` في مسار الفئة ثم فشل بسبب مشكلة في وحدة `SuppressWithNearbyTextFilter`. من هيكل مشروعك المحدث، يبدو أن `checks.xml` موجود في الجذر الرئيسي للمشروع (`~/Projects/blog-server/checks.xml`)، وليس في `src/main/resources` كما افترضنا سابقًا. هذا يفسر سبب عدم تمكن البرنامج المساعد من العثور عليه عند التكوين باستخدام `<configLocation>classpath:checks.xml</configLocation>` أو `<configLocation>checks.xml</configLocation>`، حيث تتوقع هذه الإعدادات وجود الملف في مسار الفئة (عادةً `src/main/resources`).

لإصلاح هذا وضمان تشغيل `maven-checkstyle-plugin` مع `mvn compile` باستخدام `checks.xml` المخصص الخاص بك في الجذر الرئيسي للمشروع، تحتاج إلى تحديث `<configLocation>` للإشارة إلى المسار المطلق أو النسبي للمشروع للملف. بالإضافة إلى ذلك، تحتاج إلى معالجة مشكلة `SuppressWithNearbyTextFilter` من خلال ضمان التوافق مع إصدار Checkstyle. فيما يلي الحل خطوة بخطوة.

### تكوين `pom.xml` المحدث
قم بتعديل `maven-checkstyle-plugin` في ملف `pom.xml` للإشارة إلى `checks.xml` في الجذر الرئيسي للمشروع واستخدام إصدار متوافق من Checkstyle لدعم `SuppressWithNearbyTextFilter`.

```xml
<build>
    <resources>
        <resource>
            <directory>src/main/resources</directory>
            <includes>
                <include>**/*.xml</include>
                <include>**/*.yaml</include>
            </includes>
        </resource>
    </resources>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <version>3.4.2</version>
            <executions>
                <execution>
                    <goals>
                        <goal>repackage</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M8</version>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.3.1</version> <!-- أحدث إصدار لتوافق أفضل -->
            <configuration>
                <configLocation>${project.basedir}/checks.xml</configLocation> <!-- الإشارة إلى checks.xml في الجذر الرئيسي للمشروع -->
            </configuration>
            <dependencies>
                <dependency>
                    <groupId>com.puppycrawl.tools</groupId>
                    <artifactId>checkstyle</artifactId>
                    <version>10.17.0</version> <!-- يدعم SuppressWithNearbyTextFilter -->
                </dependency>
            </dependencies>
            <executions>
                <execution>
                    <id>checkstyle-check</id>
                    <phase>compile</phase>
                    <goals>
                        <goal>check</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

### شرح التغييرات
1. **تم تحديث `<configLocation>`**:
   - تم التغيير إلى `${project.basedir}/checks.xml` للإشارة إلى `checks.xml` في الجذر الرئيسي للمشروع (`~/Projects/blog-server/checks.xml`).
   - `${project.basedir}` يحل إلى الدليل الذي يحتوي على `pom.xml`، مما يضمن أن البرنامج المساعد يجد الملف بغض النظر عن مسار الفئة.

2. **تمت ترقية إصدار البرنامج المساعد**:
   - تم تحديث `maven-checkstyle-plugin` إلى `3.3.1` (الأحدث اعتبارًا من يونيو 2025) للحصول على توافق وإصلاحات أخطاء أفضل.

3. **تمت إضافة تبعية Checkstyle**:
   - تمت إضافة `<dependency>` لـ Checkstyle `10.17.0`، الذي يتضمن دعمًا لـ `SuppressWithNearbyTextFilter`. إصدار Checkstyle الافتراضي في `maven-checkstyle-plugin:3.1.1` (`8.29`) لا يدعم هذا المرشح، مما تسبب في الخطأ السابق.

4. **تم الاحتفاظ بـ `<phase>compile</phase>`**:
   - يضمن تشغيل `checkstyle:check` أثناء `mvn compile`، كما هو مطلوب.

5. **قسم الموارد**:
   - تم الاحتفاظ بقسم `<resources>` لضمان معالجة ملفات `src/main/resources` (مثل `application.yaml`)، على الرغم من أنه غير مرتبط مباشرة بـ `checks.xml` نظرًا لأنه موجود الآن في الجذر الرئيسي للمشروع.

### التحقق من محتوى `checks.xml`
يشير الخطأ حول `SuppressWithNearbyTextFilter` إلى أن `checks.xml` الخاص بك يشير إلى هذا المرشح. تأكد من تكوينه بشكل صحيح. مثال صالح:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE module PUBLIC
    "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
    "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
    <module name="SuppressWithNearbyTextFilter">
        <!-- خصائص مثال، قم بالتعديل حسب الحاجة -->
        <property name="nearbyTextPattern" value="@SuppressWarnings"/>
    </module>
    <module name="TreeWalker">
        <!-- فحوصات أخرى -->
        <module name="ConstantName"/>
    </module>
</module>
```

- **التحقق**: افتح `checks.xml` في `~/Projects/blog-server/checks.xml` وتأكد من أن `SuppressWithNearbyTextFilter` مكتوب بشكل صحيح ويتضمن أي خصائص مطلوبة (راجع [توثيق Checkstyle](https://checkstyle.org/filters/suppresswithnearbytextfilter.html)).
- **الإجراء**: إذا كنت غير متأكد، قم بإزالة قسم `<module name="SuppressWithNearbyTextFilter"/>` مؤقتًا واختبر لعزل المشكلة.

### اختبار التكوين
1. **تنظيف المشروع**:
   ```bash
   mvn clean
   ```
   يزيل هذا دليل `target`، بما في ذلك `checkstyle-checker.xml` و `checkstyle-result.xml`، مما يضمن عدم تداخل القطع الأثرية القديمة.

2. **تشغيل Checkstyle**:
   ```bash
   mvn checkstyle:check
   ```
   يختبر هذا تكوين Checkstyle بشكل مستقل.

3. **تشغيل الترجمة**:
   ```bash
   mvn compile
   ```
   يجب أن يشغل هذا Checkstyle (بسبب ربط مرحلة `compile`) ثم يقوم بالترجمة إذا لم توجد انتهاكات تفشل في بناء المشروع.

### التصحيح إذا استمرت المشكلات
إذا واجهت أخطاء:
1. **تحقق من مسار الملف**:
   - تأكد من وجود `checks.xml` في `~/Projects/blog-server/checks.xml`.
   - تحقق من أن اسم الملف هو بالضبط `checks.xml` (حساس لحالة الأحرف، بدون امتدادات مخفية).

2. **التشغيل بتسجيل التصحيح**:
   ```bash
   mvn clean checkstyle:check -X
   ```
   ابحث عن رسائل حول تحميل `checks.xml` أو تهيئة `SuppressWithNearbyTextFilter`. شارك الناتج ذي الصلة إذا استمر الخطأ.

3. **الاختبار باستخدام `checks.xml` بسيط**:
   استبدل `checks.xml` مؤقتًا بتكوين بسيط لاستبعاد المشكلات المتعلقة بمحتوى الملف:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE module PUBLIC
       "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
       "https://checkstyle.org/dtds/configuration_1_3.dtd">
   <module name="Checker">
       <module name="TreeWalker">
           <module name="ConstantName"/>
       </module>
   </module>
   ```
   ثم شغل `mvn checkstyle:check`. إذا عمل هذا، فإن المشكلة تكمن في `SuppressWithNearbyTextFilter` أو وحدات أخرى في `checks.xml` الأصلي.

### ملاحظات إضافية
- **تحذير Settings.xml**: يُظهر ناتجك تحذيرًا حول علامة `<blocked>` غير المعترف بها في `/usr/share/maven/conf/settings.xml`. هذا غير مرتبط بمشكلة Checkstyle ولكنه يشير إلى مشكلة محتملة في تكوين Maven الخاص بك. تحقق من السطر 164 في `/usr/share/maven/conf/settings.xml` وقم بإزالة أو تصحيح علامة `<blocked>`، لأنها ليست عنصرًا قياسيًا في إعدادات Maven.
- **موقع بديل للملف**: إذا كنت تفضل، يمكنك نقل `checks.xml` إلى `src/main/resources/checks.xml` وإعادة `<configLocation>` إلى `classpath:checks.xml`. هذا أكثر تقليدية لمشاريع Maven، حيث يتم تضمين الموارد تلقائيًا في مسار الفئة.
- **الفشل عند الانتهاك**: إذا كانت انتهاكات Checkstyle تفشل في بناء المشروع وتريد السماح للمترجم بالمتابعة، أضف `<failOnViolation>false</failOnViolation>` إلى `<configuration>` في البرنامج المساعد:
  ```xml
  <configuration>
      <configLocation>${project.basedir}/checks.xml</configLocation>
      <failOnViolation>false</failOnViolation>
  </configuration>
  ```

### التحقق
بعد تطبيق التغييرات:
1. شغل `mvn clean compile` وتأكد من أن:
   - يعمل Checkstyle باستخدام `checks.xml` من الجذر الرئيسي للمشروع.
   - لا تحدث أخطاء تتعلق بـ `checks.xml` أو `SuppressWithNearbyTextFilter`.
   - تستمر الترجمة إذا نجح Checkstyle أو تم تكوينه لعدم فشل بناء المشروع.
2. تحقق من `target/checkstyle-result.xml` للحصول على نتائج Checkstyle.

إذا استمر الخطأ، يرجى مشاركة:
- محتوى (أو مقتطف ذي صلة) من `checks.xml`.
- ناتج التصحيح من `mvn clean checkstyle:check -X`.
- أي قواعد Checkstyle محددة تحاول فرضها باستخدام `SuppressWithNearbyTextFilter`.