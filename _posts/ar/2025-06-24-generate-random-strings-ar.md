---
audio: false
generated: true
lang: ar
layout: post
title: إنشاء سلاسل عشوائية باستخدام أباتشي كومنز لانج
translated: true
type: note
---

`RandomStringUtils` هو صنف مفيد جدًا من مكتبة Apache Commons Lang يوفر طرقًا ثابتة متنوعة لتوليد سلاسل نصية عشوائية. يتضمن ذلك توليد سلاسل نصية بأطوال محددة، تحتوي على أحرف فقط، أرقام فقط، أحرف أبجدية رقمية، أو حتى من مجموعة أحرف مخصصة.

إليك كيفية استخدامه والاعتماد Maven اللازم:

## كيفية استخدام `org.apache.commons.lang3.RandomStringUtils;`

أولاً، تحتاج إلى استيراد الصنف في ملف Java الخاص بك:

```java
import org.apache.commons.lang3.RandomStringUtils;
```

ثم يمكنك استخدام طرقه الثابتة. فيما يلي بعض الأمثلة الشائعة:

1.  **توليد سلسلة أبجدية رقمية عشوائية بطول محدد:**

    ```java
    String randomAlphaNumeric = RandomStringUtils.randomAlphanumeric(10);
    System.out.println("Random alphanumeric: " + randomAlphaNumeric); // e.g., "aB5cY2x9Pq"
    ```

2.  **توليد سلسلة أبجدية عشوائية بطول محدد:**

    ```java
    String randomAlphabetic = RandomStringUtils.randomAlphabetic(8);
    System.out.println("Random alphabetic: " + randomAlphabetic); // e.g., "GhJkLmNo"
    ```

3.  **توليد سلسلة رقمية عشوائية بطول محدد:**

    ```java
    String randomNumeric = RandomStringUtils.randomNumeric(6);
    System.out.println("Random numeric: " + randomNumeric); // e.g., "123456"
    ```

4.  **توليد سلسلة عشوائية بمزيج من الأحرف والأرقام، مع تحديد الإشارات:**

    ```java
    String randomLettersAndNumbers = RandomStringUtils.random(12, true, true);
    System.out.println("Random letters and numbers: " + randomLettersAndNumbers); // e.g., "abC123DeF456"
    ```

5.  **توليد سلسلة عشوائية من مجموعة أحرف مخصصة:**

    ```java
    String chars = "abcdefg";
    String randomFromCustomSet = RandomStringUtils.random(5, chars);
    System.out.println("Random from custom set: " + randomFromCustomSet); // e.g., "gcfae"
    ```

## أي مكتبة تستخدم في `pom.xml`

لاستخدام `RandomStringUtils` في مشروع Maven، تحتاج إلى إضافة الاعتماد `commons-lang3` إلى ملف `pom.xml` الخاص بك.

إليك snippet الاعتماد:

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.14.0</version> </dependency>
```

**ملاحظات مهمة:**

  * **الإصدار:** تحقق دائمًا من [Maven Central](https://mvnrepository.com/artifact/org.apache.commons/commons-lang3) للحصول على أحدث إصدار مستقر من `commons-lang3`. اعتبارًا من آخر تحديث لي، `3.14.0` أو أعلى هو خيار جيد، ولكن من الأفضل دائمًا استخدام أحدث إصدار مستقر متاح.
  * **النطاق:** النطاق الافتراضي للتبعيات هو `compile`، وهو عادة ما تريده لمكتبات الأدوات المساعدة مثل هذه. هذا يعني أن JAR سيكون متاحًا أثناء الترجمة والاختبار ووقت التشغيل. إذا كنت تستخدمه للاختبار فقط، فقد تستخدم `<scope>test</scope>`.
  * **إهمال الاستخدام:** لاحظ أن بعض الطرق القديمة مثل `RandomStringUtils.randomAlphabetic(int count)` أصبحت مهملة في الإصدارات الأحدث من Apache Commons Lang 3. بدلاً من ذلك، يوصى باستخدام الطرق `secure()` أو `secureStrong()` أو `insecure()`، والتي توفر تحكمًا أكبر في مصدر العشوائية. على سبيل المثال، `RandomStringUtils.secure().nextAlphanumeric(10)`. ومع ذلك، لا تزال الطرق القديمة تعمل في العديد من حالات الاستخدام.