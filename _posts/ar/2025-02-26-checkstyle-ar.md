---
audio: false
lang: ar
layout: post
title: مُفَضَّلات Checkstyle
translated: true
---

## ما هو مافن تشيكستايل بلوجين؟

**مافن تشيكستايل بلوجين** هو أداة تدمج تشيكستايل - أداة تحليل كود ثابت - في عملية بناء مافن الخاصة بك. تشيكستايل يدرس كودك الجافا ضد مجموعة من القواعد المسبقة، مثل اتفاقية تسمية، وتحديد الصيغة، والتعقيد، لضمان معايير الترميز. من خلال دمج هذه الوظيفة في مافن، يتيح لك البلوجين أن تقوم بتشغيل هذه الفحوصات بشكل تلقائي أثناء بناءك، مما يضمن أن قاعدة كودك تتوافق مع معايير الجودة والنمط المتسقة.

## لماذا استخدام مافن تشيكستايل بلوجين؟

استخدام مافن تشيكستايل بلوجين يقدم عدة فوائد:

- **التساوي**: يضمن أن جميع المطورين يتبعون نفس معايير الترميز، مما يحسن قابلية القراءة والصيانة.
- **الجودة**: يكتشف المشاكل المحتملة مبكرًا، مثل الطرق المعقدة جدًا أو تعليقات جافادوك المفقودة.
- **التوظيف**: تجري الفحوصات تلقائيًا كجزء من عملية بناء مافن.
- **التخصيص**: يمكنك تعديل القواعد لتناسب احتياجات مشروعك.

## كيفية إعداد مافن تشيكستايل بلوجين

هنا كيفية البدء باستخدام البلوجين في مشروع مافن الخاص بك:

### 1. إضافة البلوجين إلى `pom.xml`

أضف البلوجين في قسم `<build><plugins>` من `pom.xml`. إذا كنت تستخدم POM أب مثل `spring-boot-starter-parent`، قد يتم إدارة الإصدار لك؛ وإلا، قم بتحديده بشكل صريح.

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.1.2</version> <!-- استبدل بالإصدار الأخير -->
        </plugin>
    </plugins>
</build>
```

### 2. تهيئة البلوجين

حدد ملف تشيكستايل (مثل `checkstyle.xml`) الذي يحدد القواعد التي يجب تطبيقها. يمكنك استخدام التهيئات المضمنة مثل Sun Checks أو Google Checks أو إنشاء ملف مخصص.

تهيئة مثال:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.1.2</version>
            <configuration>
                <configLocation>checkstyle.xml</configLocation>
            </configuration>
        </plugin>
    </plugins>
</build>
```

### 3. تقديم ملف تشيكستايل

ضع ملفك `checkstyle.xml` في الجذر المشروع أو في مجلد فرعي. أو قم بإشارة إلى تهيئة خارجية مثل Google:

```xml
<configLocation>google_checks.xml</configLocation>
```

لاستخدام تهيئة خارجية مثل Google Checks، قد تحتاج إلى إضافة اعتماد تشيكستايل:

```xml
<dependencies>
    <dependency>
        <groupId>com.puppycrawl.tools</groupId>
        <artifactId>checkstyle</artifactId>
        <version>8.44</version>
    </dependency>
</dependencies>
```

## تشغيل مافن تشيكستايل بلوجين

يدمج البلوجين مع دورة حياة مافن ويمكن تشغيله بطرق مختلفة:

- **تشغيل تشيكستايل بشكل صريح**:
  للتحقق من المخالفات وفعلا فشل البناء:
  ```
  mvn checkstyle:check
  ```

- **تشغيل أثناء البناء**:
  بافتراض، يربط البلوجين إلى المرحلة `verify`. استخدم:
  ```
  mvn verify
  ```
  لتوليد تقرير دون فشل البناء:
  ```
  mvn checkstyle:checkstyle
  ```

تولد التقارير عادةً في `target/site/checkstyle.html`.

## تخصيص البلوجين

يمكنك تعديل سلوك البلوجين في قسم `<configuration>` من `pom.xml`:

- **فشل عند المخالفة**:
  بافتراض، يفشل البناء إذا وجدت مخالفات. لتعطيل هذا:
  ```xml
  <configuration>
      <failOnViolation>false</failOnViolation>
  </configuration>
  ```

- **شمل أو استبعاد الملفات**:
  تحكم في الملفات التي سيتم فحصها:
  ```xml
  <configuration>
      <includes>**/*.java</includes>
      <excludes>**/generated/**/*.java</excludes>
  </configuration>
  ```

- **تعيين مستوى خطورة المخالفة**:
  حدد مستوى خطورة يسبب فشل البناء:
  ```xml
  <configuration>
      <violationSeverity>warning</violationSeverity>
  </configuration>
  ```

## مثال `checkstyle.xml`

هنا ملف `checkstyle.xml` أساسي يطبق اتفاقية تسمية وتطلبات جافادوك:

```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
    "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
    "https://checkstyle.org/dtds/configuration_1_3.dtd">

<module name="Checker">
    <module name="TreeWalker">
        <module name="JavadocMethod"/>
        <module name="MethodName"/>
        <module name="ConstantName"/>
    </module>
</module>
```

## حالات استخدام شائعة

يقدم البلوجين مجموعة متنوعة من الفحوصات، بما في ذلك:
- اتفاقية تسمية للصفوف، والأدوات، والمتغيرات.
- استخدام صحيح للفراغات والتحديد.
- وجود وصدق تعليقات جافادوك.
- اكتشاف الطرق المعقدة أو الطويلة.

## التكامل والتشخيص

- **تكامل IDE**: يمكن لأدوات مثل IntelliJ IDEA وEclipse استخدام نفس `checkstyle.xml` للحصول على ردود فعل في الوقت الفعلي.
- **التكامل المستمر**: أضف تشيكستايل إلى خطك CI لتطبيق المعايير على كل تعليق.
- **التشخيص**: إذا لم يتم العثور على ملف التهيئة، تأكد من مسار `<configLocation>`. تأكد من أن إصدارات الاعتماد تتوافق مع البلوجين.

## ملخص

**مافن تشيكستايل بلوجين** هو إضافة قيمة لأي مشروع جافا يستخدم مافن. لاستخدامه:
1. أضف وتهيئ البلوجين في `pom.xml`.
2. قدم ملف `checkstyle.xml` مع القواعد التي تريدها.
3. استخدم `mvn checkstyle:check` لتطبيق المعايير أو `mvn checkstyle:checkstyle` للحصول على التقارير.
4. قم بتخصيص حسب الحاجة لتناسب عملية العمل الخاصة بك.

يساعد هذا البلوجين على الحفاظ على كود ذو جودة عالية ومتسقة مع جهد قليل!