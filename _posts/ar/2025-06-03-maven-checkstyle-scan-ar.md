---
audio: false
generated: true
lang: ar
layout: post
title: 'مافن تشيك ستايل: متابعة المسح'
translated: true
type: note
---

لجعل الأمر `mvn checkstyle:check` يستمر في فحص جميع الوحدات دون أن يتوقف مبكرًا بسبب المخالفات، تحتاج إلى تكوين إضافة Checkstyle لـ Maven لتعطيل خيار `failOnViolation`. بشكل افتراضي، يكون `failOnViolation` معينًا إلى `true`، مما يتسبب في توقف عملية البناء بمجرد العثور على مخالفات. تعيينه إلى `false` يسمح للمسح الضوئي بالإكمال عبر جميع الوحدات، والإبلاغ عن جميع المخالفات دون إيقاف عملية البناء.

### الحل
قم بتحديث ملف `pom.xml` الخاص بك لتكوين إضافة Checkstyle كما يلي:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-checkstyle-plugin</artifactId>
      <version>3.3.1</version> <!-- استخدم أحدث إصدار -->
      <configuration>
        <failOnViolation>false</failOnViolation>
        <logViolationsToConsole>true</logViolationsToConsole> <!-- اختياري: يسجل المخالفات في وحدة التحكم -->
      </configuration>
      <executions>
        <execution>
          <id>checkstyle</id>
          <phase>validate</phase> <!-- أو المرحلة التي تفضلها -->
          <goals>
            <goal>check</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

### الشرح
- **`<failOnViolation>false</failOnViolation>`**: هذا الإعداد يمنع عملية البناء من الفشل عند اكتشاف مخالفات Checkstyle، مما يسمح للمسح الضوئي بالمتابعة عبر جميع الوحدات.
- **`<logViolationsToConsole>true</logViolationsToConsole>`**: (اختياري) يضمن طباعة المخالفات في وحدة التحكم لزيادة الوضوح، حتى لو لم تفشل عملية البناء.
- **مرحلة التنفيذ**: الربط `<phase>validate</phase>` يربط فحص Checkstyle بمرحلة `validate` من دورة حياة Maven. يمكنك ضبط المرحلة (مثل `compile` أو `verify`) إذا أردت أن يعمل في مرحلة مختلفة.

### تشغيل الأمر
قم بتشغيل الأمر مرة أخرى:
```bash
mvn checkstyle:check
```
مع تعيين `failOnViolation` إلى `false`، سيقوم Maven بفحص جميع الوحدات، والإبلاغ عن جميع المخالفات، وإكمال عملية البناء دون توقف مبكر.

### ملاحظات
- تأكد من استخدامك إصدارًا حديثًا من `maven-checkstyle-plugin` (مثل 3.3.1 كما هو موضح). تحقق من أحدث إصدار على Maven Central إذا لزم الأمر.
- إذا كنت تعمل في مشروع متعدد الوحدات، فإن هذا التكوين ينطبق على جميع الوحدات ما لم يتم تجاوزه في ملف `pom.xml` تابع.
- لإنشاء تقرير عن المخالفات، فكر في تشغيل `mvn checkstyle:checkstyle` بدلاً من ذلك، والذي ينتج تقرير HTML دون أن يفشل البناء بشكل افتراضي.

إذا كانت لديك متطلبات محددة (مثل قواعد Checkstyle مخصصة أو إعداد مختلف)، فأخبرني، وسأقوم بتخصيص الحل بشكل أكبر!