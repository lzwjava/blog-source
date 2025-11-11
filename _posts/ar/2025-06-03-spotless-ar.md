---
audio: false
generated: true
lang: ar
layout: post
title: استخدام سبوتلس لتهيئة الكود
translated: true
type: note
---

لا يوجد أمر `mvn checkstyle:format` في إضافة Maven Checkstyle Plugin. صممت هذه الإضافة أساسًا للتحقق من الكود مقابل تكوين Checkstyle والإبلاغ عن المخالفات، وليس لتنسيق الكود تلقائيًا. ومع ذلك، يمكنك تحقيق تنسيق الكود بناءً على تكوين Checkstyle باستخدام أدوات أخرى مثل Spotless أو Maven Formatter Plugin، والتي يمكن تكوينها لتتوافق مع قواعد Checkstyle الخاصة بك.

أدناه، سأشرح كيفية تنسيق الكود بناءً على تكوين Checkstyle الخاص بك باستخدام **إضافة Spotless Maven Plugin**، حيث أنها خيار شائع لهذا الغرض ويمكنها التكامل مع قواعد Checkstyle.

### الحل: استخدام Spotless مع تكوين Checkstyle

يمكن لإضافة Spotless Maven Plugin تنسيق كود Java وفقًا لملف تكوين Checkstyle (مثل `checkstyle.xml`). إليك كيفية إعداده:

#### 1. أضف Spotless إلى ملف `pom.xml` الخاص بك
أضف إضافة Spotless إلى ملف `pom.xml` وقم بتكوينها لاستخدام ملف تكوين Checkstyle الخاص بك.

```xml
<build>
  <plugins>
    <plugin>
      <groupId>com.diffplug.spotless</groupId>
      <artifactId>spotless-maven-plugin</artifactId>
      <version>2.43.0</version> <!-- استخدم أحدث إصدار -->
      <configuration>
        <java>
          <!-- أشر إلى ملف تكوين Checkstyle الخاص بك -->
          <googleJavaFormat>
            <version>1.22.0</version> <!-- اختياري: استخدم إصدارًا محددًا -->
            <style>GOOGLE</style> <!-- أو AOSP، أو احذف للاستخدام الافتراضي -->
          </googleJavaFormat>
          <formatAnnotations>
            <!-- استخدم تكوين Checkstyle للتنسيق -->
            <checkstyle>
              <file>${project.basedir}/checkstyle.xml</file> <!-- المسار إلى تكوين Checkstyle -->
              <version>10.17.0</version> <!-- طابق إصدار Checkstyle الخاص بك -->
            </checkstyle>
          </formatAnnotations>
        </java>
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>apply</goal> <!-- ينسق الكود تلقائيًا -->
          </goals>
          <phase>process-sources</phase> <!-- اختياري: اربط بمرحلة -->
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

#### 2. تأكد من وجود تكوين Checkstyle الخاص بك
تأكد من وجود ملف `checkstyle.xml` في مشروعك (على سبيل المثال، في الدليل الجذر أو دليل فرعي). يحدد هذا الملف معايير البرمجة (مثل المسافات البادئة، والمسافات البيضاء، إلخ) التي ستستخدمها Spotless لتنسيق كودك. إذا كنت تستخدم معيارًا مثل Google Java Format، فيمكنك الرجوع إليه، أو استخدام تكوين Checkstyle مخصص مصمم خصيصًا لمشروعك.

مقتطف مثال لملف `checkstyle.xml` للقواعد الأساسية للتنسيق:
```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN" "https://checkstyle.sourceforge.io/dtds/configuration_1_3.dtd">
<module name="Checker">
  <module name="TreeWalker">
    <module name="Indentation">
      <property name="basicOffset" value="2"/>
      <property name="braceAdjustment" value="0"/>
    </module>
  </module>
</module>
```

#### 3. شغّل Spotless لتنسيق الكود
لتنسيق كودك بناءً على تكوين Checkstyle، شغّل:
```bash
mvn spotless:apply
```

سيقوم هذا الأمر بتنسيق جميع ملفات Java في مشروعك وفقًا للقواعد المحددة في تكوين Checkstyle الخاص بك وأي إعدادات تنسيق إضافية (مثل Google Java Format).

#### 4. تحقق من التنسيق باستخدام Checkstyle
بعد التنسيق، يمكنك تشغيل `mvn checkstyle:check` للتحقق من امتثال الكود المنسق لقواعد Checkstyle الخاصة بك. إذا اتبعت النصيحة السابقة لتعيين `<failOnViolation>false</failOnViolation>`، فسيتم الإبلاغ عن أي مخالفات متبقية دون إيقاف عملية البناء.

### بديل: Maven Formatter Plugin
إذا كنت تفضل عدم استخدام Spotless، يمكنك استخدام **Maven Formatter Plugin**، والذي يدعم أيضًا التنسيق بناءً على القواعد ولكنه أقل شيوعًا في الاستخدام مع تكوينات Checkstyle مباشرة. إليك الإعداد الأساسي:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>net.revelc.code.formatter</groupId>
      <artifactId>formatter-maven-plugin</artifactId>
      <version>2.23.0</version> <!-- استخدم أحدث إصدار -->
      <configuration>
        <configFile>${project.basedir}/checkstyle.xml</configFile> <!-- المسار إلى تكوين Checkstyle -->
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>format</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

شغّل التنسيق باستخدام:
```bash
mvn formatter:format
```

### ملاحظات
- **لا يوجد أمر تنسيق مباشر لـ Checkstyle**: إضافة Checkstyle Maven Plugin لا توفر هدف `format`. هناك حاجة إلى أدوات مثل Spotless أو Formatter Plugin لتطبيق التنسيق بناءً على قواعد Checkstyle.
- **توافق إصدار Checkstyle**: تأكد من أن إصدار Checkstyle المحدد في Spotless (أو Formatter) يطابق الإصدار المستخدم في إضافة Checkstyle الخاصة بك لتجنب عدم تطابق القواعد.
- **قواعد Checkstyle المخصصة**: يجب أن يتضمن ملف `checkstyle.xml` الخاص بك قواعد متعلقة بالتنسيق (مثل `Indentation`، `WhitespaceAround`، إلخ) حتى تتمكن Spotless من تطبيقها بشكل صحيح.
- **مشاريع متعددة النماط**: في مشروع Maven متعدد النماط، يمكنك وضع تكوين Spotless/Formatter في ملف `pom.xml` الرئيسي لتطبيقه عبر جميع النماط، أو تكوينه لكل نمط حسب الحاجة.
- **تحقق بعد التنسيق**: دائمًا شغّل `mvn checkstyle:check` بعد التنسيق للتأكد من الامتثال، خاصة إذا كان لديك قواعد غير متعلقة بالتنسيق (مثل طول الطريقة، التعقيد) في تكوين Checkstyle الخاص بك.

إذا لم يكن لديك ملف `checkstyle.xml` أو تحتاج إلى مساعدة في إنشاء واحد، فأخبرني، ويمكنني تقديم نموذج أو إرشادك further! أيضًا، إذا كنت تفضل أداة مختلفة أو لديك متطلبات تنسيق محددة، فيرجى مشاركتها، وسأقوم بتعديل الحل.