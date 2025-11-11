---
audio: false
generated: true
lang: ar
layout: post
title: إضافة مافن سورفاير
translated: true
type: note
---

فيما يلي شرح لـ **Maven Surefire Plugin**، وهو مكون أساسي في المشاريع القائمة على Maven لتشغيل اختبارات الوحدة أثناء عملية البناء. يغطي هذا الشرح الغرض منه، وطريقة التهيئة، والاستخدام، وخيارات التخصيص.

---

## ما هو Maven Surefire Plugin؟

**Maven Surefire Plugin** هو إضافة (plugin) في Apache Maven مصممة لتنفيذ اختبارات الوحدة أثناء دورة حياة البناء (build lifecycle). وهو يندمج بسلاسة مع مرحلة `test` في Maven ويتم تشغيله تلقائيًا عند تشغيل أوامر مثل `mvn test` أو `mvn package` أو `mvn install`. تدعم هذه الإضافة أطر عمل الاختبار الشائعة مثل JUnit (الإصدارات 3 و4 و5) و TestNG، وتقوم بتوليد تقارير الاختبار لمساعدة المطورين على تقييم نتائج الاختبار.

### الميزات الرئيسية
- يشغل الاختبارات في عملية JVM منفصلة لعزلها.
- يدعم أطر عمل اختبار متعددة (JUnit, TestNG، إلخ).
- يولد تقارير الاختبار بصيغ مثل XML والنص العادي.
- يقدم مرونة لتخطي الاختبارات، أو تشغيل اختبارات محددة، أو تخصيص التنفيذ.

---

## الإعداد الأساسي في `pom.xml`

يتم تضمين Surefire Plugin افتراضيًا في دورة حياة البناء في Maven، لذا لا تحتاج إلى تهيئته للاستخدام الأساسي. ومع ذلك، يمكنك التصريح عنه صراحة في ملف `pom.xml` الخاص بك لتحديد إصدار معين أو تخصيص سلوكه.

### التهيئة الدنيا
إذا لم تقم بإضافة أي تهيئة، يستخدم Maven الإضافة بالإعدادات الافتراضية:
- توجد الاختبارات في `src/test/java`.
- تتبع ملفات الاختبار أنماط تسمية مثل `**/*Test.java` أو `**/Test*.java` أو `**/*Tests.java`.

### التصريح الصريح
لتخصيص الإضافة أو التأكد من استخدام إصدار محدد، أضفها إلى قسم `<build><plugins>` في ملف `pom.xml`. إليك مثال:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M5</version> <!-- استخدم أحدث إصدار -->
        </plugin>
    </plugins>
</build>
```

---

## تشغيل الاختبارات باستخدام Surefire

ترتبط هذه الإضافة بمرحلة `test` في دورة حياة Maven. إليك كيفية استخدامها:

### تشغيل جميع الاختبارات
لتنفيذ جميع اختبارات الوحدة، شغِّل:

```
mvn test
```

### تشغيل الاختبارات في عملية بناء أكبر
يتم تنفيذ الاختبارات تلقائيًا عند تشغيل أوامر تتضمن مرحلة `test`، مثل:

```
mvn package
mvn install
```

### تخطي الاختبارات
يمكنك تخطي تنفيذ الاختبارات باستخدام علامات سطر الأوامر:
- **تخطي تشغيل الاختبارات**: `-DskipTests`
  ```
  mvn package -DskipTests
  ```
- **تخطي ترجمة وتنفيذ الاختبارات**: `-Dmaven.test.skip=true`
  ```
  mvn package -Dmaven.test.skip=true
  ```

---

## تخصيص Maven Surefire Plugin

يمكنك تخصيص سلوك الإضافة عن طريق إضافة قسم `<configuration>` في `pom.xml`. فيما يلي بعض عمليات التخصيص الشائعة:

### تضمين أو استبعاد اختبارات محددة
حدد الاختبارات التي تريد تشغيلها أو تخطيها باستخدام الأنماط:
```xml
<configuration>
    <includes>
        <include>**/My*Test.java</include>
    </includes>
    <excludes>
        <exclude>**/SlowTest.java</exclude>
    </excludes>
</configuration>
```

### تشغيل الاختبارات بالتوازي
اسرع وقت التنفيذ عن طريق تشغيل الاختبارات في وقت واحد:
```xml
<configuration>
    <parallel>methods</parallel>
    <threadCount>2</threadCount>
</configuration>
```
*ملاحظة*: تأكد من أن اختباراتك آمنة للخيوط (thread-safe) قبل تمكين هذا الخيار.

### تمرير خصائص النظام
عيّن الخصائص لبيئة JVM الخاصة بالاختبار:
```xml
<configuration>
    <systemPropertyVariables>
        <propertyName>propertyValue</propertyName>
    </systemPropertyVariables>
</configuration>
```

### توليد التقارير
افتراضيًا، يتم حفظ التقارير في `target/surefire-reports`. للحصول على تقرير HTML، استخدم `maven-surefire-report-plugin`:
```xml
<reporting>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-report-plugin</artifactId>
            <version>3.0.0-M5</version>
        </plugin>
    </plugins>
</reporting>
```
شغِّل `mvn surefire-report:report` لتوليد تقرير HTML.

---

## التعامل مع فشل الاختبارات

### فشل عملية البناء عند فشل الاختبار
افتراضيًا، يتسبب اختبار فاشل في فشل عملية البناء. لتجاهل حالات الفشل والمتابعة:
```
mvn test -Dmaven.test.failure.ignore=true
```

### إعادة تشغيل الاختبارات الفاشلة
تعامل مع الاختبارات غير المستقرة (flaky tests) عن طريق إعادة محاولة تشغيل الفاشلة منها:
```xml
<configuration>
    <rerunFailingTestsCount>2</rerunFailingTestsCount>
</configuration>
```
هذا يعيد تشغيل الاختبارات الفاشلة حتى مرتين.

---

## استخدام Surefire مع أطر عمل الاختبار

تدعم الإضافة أطر عمل اختبار متنوعة مع حد أدنى من الإعداد:

### JUnit 4
لا حاجة لتهيئة إضافية؛ فـ Surefire يكتشف اختبارات JUnit 4 تلقائيًا.

### JUnit 5
أضف تبعية JUnit 5:
```xml
<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <version>5.8.1</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```
استخدم الإصدار 2.22.0 أو أحدث من Surefire للحصول على دعم كامل.

### TestNG
أضف تبعية TestNG:
```xml
<dependencies>
    <dependency>
        <groupId>org.testng</groupId>
        <artifactId>testng</artifactId>
        <version>7.4.0</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```
سوف يقوم Surefire تلقائيًا بتشغيل اختبارات TestNG.

---

## ملاحظات رئيسية

- **موقع الاختبارات**: يجب أن تكون الاختبارات في `src/test/java`، والموارد في `src/test/resources`.
- **اتفاقيات التسمية**: تشمل الأنماط الافتراضية `**/*Test.java`، `**/Test*.java`، إلخ، ولكن يمكن تخصيصها.
- **إصدار الإضافة**: استخدم إصدارًا حديثًا (مثل 3.0.0-M5) للحصول على أحدث الميزات ودعم أطر العمل.

---

## الملخص

**Maven Surefire Plugin** ضروري لتشغيل اختبارات الوحدة في مشاريع Maven. لاستخدامه:
1. اعتمد على سلوكه الافتراضي أو صرّح عنه صراحة في `pom.xml` للتخصيص.
2. شغِّل الاختبارات باستخدام `mvn test` أو كجزء من عمليات بناء أكبر مثل `mvn package`.
3. خصصه بخيارات مثل أنماط التضمين/الاستبعاد، أو التنفيذ المتوازي، أو خصائص النظام.
4. تعامل مع حالات الفشل عن طريق تخطي الاختبارات، أو تجاهلها، أو إعادة تشغيل غير المستقرة منها.
5. تأكد من التوافق مع إطار الاختبار الخاص بك (JUnit, TestNG) عن طريق إضافة التبعيات الصحيحة.

توفر هذه الإضافة طريقة قوية ومرنة لإدارة اختبارات الوحدة في مشاريع Maven الخاصة بك!