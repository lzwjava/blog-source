---
audio: false
lang: ar
layout: post
title: أداة Maven Surefire
translated: true
---

أدناه شرح **مُفَضَل Maven Surefire Plugin**، وهو مكون أساسي في مشاريع Maven لتشغيل اختبارات الوحدة أثناء عملية البناء. يغطي هذا الشرح غرضه، وتكوينه، واستخدامه، واختيارات تخصيصه.

---

## ما هو مُفَضَل Maven Surefire Plugin؟

**مُفَضَل Maven Surefire Plugin** هو مُفَضَل في Apache Maven مصمم لتنفيذ اختبارات الوحدة أثناء دورة حياة البناء. يتكامل بشكل سلس مع مرحلة `test` في Maven ويُشغَّل تلقائيًا عند تنفيذ الأوامر مثل `mvn test`، `mvn package`، أو `mvn install`. يدعم المُفَضَل إطارات الاختبار الشائعة مثل JUnit (الإصدارات 3، 4، و5) وTestNG، ويُنتج تقارير الاختبار لمساعدة المطورين على تقييم نتائج الاختبارات.

### الميزات الرئيسية
- يشغل الاختبارات في عملية JVM منفصلة للعزل.
- يدعم إطارات الاختبار المتعددة (JUnit، TestNG، إلخ).
- يُنتج تقارير الاختبار في صيغ مثل XML و نص عادي.
- يوفر مرونة لتخطي الاختبارات، أو تشغيل اختبارات محددة، أو تخصيص التنفيذ.

---

## الإعداد الأساسي في `pom.xml`

يضم مُفَضَل Surefire بشكل افتراضي في دورة حياة بناء Maven، فلا تحتاج إلى تكوينه للاستخدام الأساسي. ومع ذلك، يمكنك إعلانه بشكل صريح في ملف `pom.xml` الخاص بك لتحديد الإصدار أو تخصيص سلوكه.

### الإعداد الأدنى
إذا لم تضف أي تكوين، يستخدم Maven المُفَضَل مع الإعدادات الافتراضية:
- تقع الاختبارات في `src/test/java`.
- تتبع ملفات الاختبار نماذج الأسماء مثل `**/*Test.java`، `**/Test*.java`، أو `**/*Tests.java`.

### الإعلان الصريح
للتخصيص المُفَضَل أو التأكد من إصدار معين، أضفه إلى قسم `<build><plugins>` من ملف `pom.xml`. voici مثال:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M5</version> <!-- استخدم أحدث الإصدار -->
        </plugin>
    </plugins>
</build>
```

---

## تشغيل الاختبارات مع Surefire

يربط المُفَضَل بالمرحلة `test` من دورة حياة Maven. voici كيفية استخدامه:

### تشغيل جميع الاختبارات
لتنفيذ جميع اختبارات الوحدة، قم بإطلاق:

```
mvn test
```

### تشغيل الاختبارات في بناء أكبر
تُشغَّل الاختبارات تلقائيًا عند تنفيذ الأوامر التي تتضمن مرحلة `test`، مثل:

```
mvn package
mvn install
```

### تخطي الاختبارات
يمكنك تخطي تنفيذ الاختبارات باستخدام علامات السطر الأوامر:
- **تخطي تشغيل الاختبارات**: `-DskipTests`
  ```
  mvn package -DskipTests
  ```
- **تخطي تجميع واختبار الاختبارات**: `-Dmaven.test.skip=true`
  ```
  mvn package -Dmaven.test.skip=true
  ```

---

## تخصيص مُفَضَل Surefire

يمكنك تخصيص سلوك المُفَضَل بإضافة قسم `<configuration>` في ملف `pom.xml`. voici بعض التخصيصات الشائعة:

### تضمين أو استبعاد اختبارات محددة
حدد الاختبارات التي يجب تشغيلها أو تخطيها باستخدام النماذج:
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

### تشغيل الاختبارات بشكل متزامن
سريع من تنفيذ الاختبارات من خلال تشغيلها بشكل متزامن:
```xml
<configuration>
    <parallel>methods</parallel>
    <threadCount>2</threadCount>
</configuration>
```
**ملاحظة**: تأكد من أن اختباراتك آمنة للخطوات قبل تمكين هذا.

### تمرير خواص النظام
قم بتعيين خواص JVM الاختبار:
```xml
<configuration>
    <systemPropertyVariables>
        <propertyName>propertyValue</propertyName>
    </systemPropertyVariables>
</configuration>
```

### إنشاء التقارير
بالتفault، يتم حفظ التقارير في `target/surefire-reports`. لتلقي تقرير HTML، استخدم `maven-surefire-report-plugin`:
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
قم بإطلاق `mvn surefire-report:report` لإنشاء التقرير HTML.

---

## معالجة فشل الاختبارات

### فشل البناء عند فشل الاختبار
بالتفault، يسبب اختبار فاشل فشل البناء. لتجاهل الفشل و الاستمرار:
```
mvn test -Dmaven.test.failure.ignore=true
```

### إعادة تشغيل الاختبارات الفاشلة
قم بمعالجة الاختبارات المتقلبة من خلال إعادة تشغيل الفشل:
```xml
<configuration>
    <rerunFailingTestsCount>2</rerunFailingTestsCount>
</configuration>
```
هذا يعيد تشغيل الاختبارات الفاشلة حتى 2 مرات.

---

## استخدام Surefire مع إطارات الاختبار

يدعم المُفَضَل إطارات الاختبار المختلفة مع إعدادات قليلة:

### JUnit 4
لا تحتاج إلى أي إعداد إضافي؛ يكتشف Surefire اختبارات JUnit 4 تلقائيًا.

### JUnit 5
أضف التبعية JUnit 5:
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
استخدم Surefire الإصدار 2.22.0 أو أحدث للحصول على دعم كامل.

### TestNG
أضف التبعية TestNG:
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
سيعمل Surefire تلقائيًا على تشغيل اختبارات TestNG.

---

## ملاحظات رئيسية

- **موقع الاختبار**: يجب أن تكون الاختبارات في `src/test/java`، مع الموارد في `src/test/resources`.
- **أسماء التسمية**: تشمل النماذج الافتراضية `**/*Test.java`، `**/Test*.java`، إلخ، ولكن يمكن تخصيصها.
- **إصدار المُفَضَل**: استخدم إصدارًا حديثًا (مثل 3.0.0-M5) للحصول على أحدث الميزات ودعم الإطارات.

---

## ملخص

**مُفَضَل Maven Surefire Plugin** هو أساسي لتشغيل اختبارات الوحدة في مشاريع Maven. لاستخدامه:
1. اعتمد على سلوكه الافتراضي أو اعلانه بشكل صريح في `pom.xml` للتخصيص.
2. قم بإطلاق الاختبارات باستخدام `mvn test` أو كجزء من بناء أكبر مثل `mvn package`.
3. قم بتخصيصه باستخدام خيارات مثل نماذج تضمين/استبعاد، تنفيذ متزامن، أو خواص النظام.
4. قم بمعالجة الفشل من خلال تخطي الاختبارات، تجاهلها، أو إعادة تشغيل الاختبارات المتقلبة.
5. تأكد من التوافق مع إطار اختبارك (JUnit، TestNG) من خلال إضافة التبعيات الصحيحة.

يوفر هذا المُفَضَل طريقة قوية ومتعددة الاستخدامات لإدارة اختبارات الوحدة في مشاريع Maven!