---
audio: false
generated: true
lang: ar
layout: post
title: التعبيرات النمطية في جافا
translated: true
type: note
---

# كيفية استخدام `java.util.regex` في جافا

توفّر حزمة `java.util.regex` في جافا أدوات للعمل مع التعبيرات النمطية (Regex)، وهي أنماط تُستخدم لمطابقة النص ومعالجته. سيرشدك هذا الدليل خلال أساسيات استخدام هذه الحزمة، مع التركيز على الصنفين الرئيسيين: `Pattern` و `Matcher`. سأغطي أيضًا حالات الاستخدام الشائعة مع أمثلة لمساعدتك على البدء.

## نظرة عامة على `java.util.regex`

تتضمن حزمة `java.util.regex`:

- **`Pattern`**: يمثّل تعبيرًا نمطيًا مُصرّفًا. تقوم بإنشائه من سلسلة تعبير نمطي.
- **`Matcher`**: يطبّق النمط على سلسلة إدخال محددة وينفذ عمليات المطابقة.

بالإضافة إلى ذلك، توفّر صنف `String` في جافا طرقًا تعتمد على التعبيرات النمطية للمهام البسيطة.

## الخطوات الأساسية لاستخدام `java.util.regex`

لاستخدام التعبيرات النمطية في جافا، اتّبع هذه الخطوات:

1.  **اصرف نمطًا (Compile a Pattern)**: حوّل سلسلة التعبير النمطي الخاصة بك إلى كائن `Pattern`.
2.  **أنشئ مُطابِقًا (Create a Matcher)**: استخدم النمط لإنشاء `Matcher` لنص الإدخال الخاص بك.
3.  **نفّذ العمليات (Perform Operations)**: استخدم المُطابِق للتحقق من وجود مطابقات، أو العثور على أنماط، أو معالجة النص.

إليك كيفية عمل ذلك عمليًا.

## المثال 1: التحقق من صحة عنوان بريد إلكتروني

لننشئ مدقق بريد إلكتروني بسيط باستخدام نمط تعبير نمطي أساسي: `".+@.+\\..+"`. يطابق هذا النمط السلاسل التي تحتوي على حرف واحد على الأقل قبل وبعد رمز `@`، يليه نقطة والمزيد من الأحرف (مثل `example@test.com`).

```java
import java.util.regex.*;

public class EmailValidator {
    public static boolean isValidEmail(String email) {
        // تعريف نمط التعبير النمطي
        String regex = ".+@.+\\..+";
        // تصريف النمط
        Pattern pattern = Pattern.compile(regex);
        // إنشاء مُطابِق لسلسلة الإدخال
        Matcher matcher = pattern.matcher(email);
        // التحقق مما إذا كانت السلسلة بأكملها تطابق النمط
        return matcher.matches();
    }

    public static void main(String[] args) {
        String email = "example@test.com";
        if (isValidEmail(email)) {
            System.out.println("Valid email");
        } else {
            System.out.println("Invalid email");
        }
    }
}
```

### الشرح
- **`Pattern.compile(regex)`**: يصرف سلسلة التعبير النمطي إلى كائن `Pattern`.
- **`pattern.matcher(email)`**: ينشئ `Matcher` لسلسلة الإدخال `email`.
- **`matcher.matches()`**: يُرجع `true` إذا كانت السلسلة بأكملها تطابق النمط، و `false` بخلاف ذلك.

**الناتج**: `Valid email`

ملاحظة: هذا نمط بريد إلكتروني مبسط. يتطلب التحقق من صحة البريد الإلكتروني الحقيقي تعبيرًا نمطيًا أكثر تعقيدًا (مثلًا، وفقًا لـ RFC 5322)، لكن هذا يخدم كنقطة بداية.

## المثال 2: العثور على جميع وسمات الهاشتاغ في سلسلة

لنفترض أنك تريد استخراج جميع وسمات الهاشتاغ (مثل `#java`) من تغريدة. استخدم التعبير النمطي `"#\\w+"`، حيث `#` تطابق رمز الهاشتاغ الحرفي و `\\w+` تطابق حرفًا كلميًا واحدًا أو أكثر (أحرف، أرقام، أو شرطات سفلية).

```java
import java.util.regex.*;

public class HashtagExtractor {
    public static void main(String[] args) {
        String tweet = "This is a #sample tweet with #multiple hashtags like #java";
        String regex = "#\\w+";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(tweet);

        // العثور على جميع المطابقات
        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }
}
```

### الشرح
- **`matcher.find()`**: ينتقل إلى المطابقة التالية في سلسلة الإدخال ويُرجع `true` إذا تم العثور على مطابقة.
- **`matcher.group()`**: يُرجع النص المطابق للمطابقة الحالية.

**الناتج**:
```
#sample
#multiple
#java
```

## المثال 3: استبدال النص باستخدام التعبير النمطي

لاستبدال جميع تكرارات كلمة ما (مثل تحويل كلمة "badword" إلى نجوم)، يمكنك استخدام الطريقة `String.replaceAll()`، التي تستخدم التعبير النمطي داخليًا.

```java
public class TextCensor {
    public static void main(String[] args) {
        String text = "This is a badword example with badword repeated.";
        String censored = text.replaceAll("badword", "*******");
        System.out.println(censored);
    }
}
```

**الناتج**: `This is a ******* example with ******* repeated.`

لعمليات الاستبدال الأكثر تعقيدًا، استخدم `Matcher`:

```java
import java.util.regex.*;

public class ComplexReplacement {
    public static void main(String[] args) {
        String text = "Contact: 123-456-7890";
        String regex = "\\d{3}-\\d{3}-\\d{4}"; // يطابق أرقام الهواتف
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);
        String result = matcher.replaceAll("XXX-XXX-XXXX");
        System.out.println(result);
    }
}
```

**الناتج**: `Contact: XXX-XXX-XXXX`

## المثال 4: استخدام المجموعات لتحليل البيانات المهيكلة

تسمح لك مجموعات التعبير النمطي، المُعرّفة بالأقواس `()`، بالتقاط أجزاء من مطابقة. على سبيل المثال، لتحليل رقم الضمان الاجتماعي (SSN) مثل `123-45-6789`:

```java
import java.util.regex.*;

public class SSNParser {
    public static void main(String[] args) {
        String ssn = "123-45-6789";
        String regex = "(\\d{3})-(\\d{2})-(\\d{4})"; // مجموعات للمنطقة، المجموعة، والتسلسلي
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(ssn);

        if (matcher.matches()) {
            System.out.println("Area number: " + matcher.group(1));
            System.out.println("Group number: " + matcher.group(2));
            System.out.println("Serial number: " + matcher.group(3));
        }
    }
}
```

### الشرح
- **`"(\\d{3})-(\\d{2})-(\\d{4})"`**: يحدد ثلاث مجموعات:
  - المجموعة 1: `\\d{3}` (ثلاثة أرقام)
  - المجموعة 2: `\\d{2}` (رقمان)
  - المجموعة 3: `\\d{4}` (أربعة أرقام)
- **`matcher.group(n)`**: يسترجع النص المطابق بواسطة المجموعة `n` (فهرس قائم على 1).

**الناتج**:
```
Area number: 123
Group number: 45
Serial number: 6789
```

يمكنك أيضًا استخدام **المجموعات المسماة** للوضوح:

```java
String regex = "(?<area>\\d{3})-(?<group>\\d{2})-(?<serial>\\d{4})";
Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher("123-45-6789");
if (matcher.matches()) {
    System.out.println("Area: " + matcher.group("area"));
    System.out.println("Group: " + matcher.group("group"));
    System.out.println("Serial: " + matcher.group("serial"));
}
```

## ميزات ونصائح إضافية

### الأعلام (Flags)
عدّل سلوك النمط باستخدام الأعلام في `Pattern.compile()`:
- **`Pattern.CASE_INSENSITIVE`**: يتجاهل حالة الأحرف عند المطابقة.
  ```java
  Pattern pattern = Pattern.compile("hello", Pattern.CASE_INSENSITIVE);
  Matcher matcher = pattern.matcher("HELLO");
  System.out.println(matcher.matches()); // true
  ```

### طرق الصنف `String`
للمهام البسيطة، استخدم طرق `String`:
- **`matches()`**: يتحقق مما إذا كانت السلسلة بأكملها تطابق تعبيرًا نمطيًا.
  ```java
  String text = "cat";
  System.out.println(text.matches("\\w{3}")); // true
  ```
- **`split()`**: يقسم سلسلة بناءً على نمط تعبير نمطي.
  ```java
  String data = "apple, banana, cherry";
  String[] fruits = data.split("\\s*,\\s*");
  // الناتج: apple, banana, cherry
  ```

### تهريب الأحرف الخاصة (Escaping)
يستخدم التعبير النمطي أحرفًا خاصة مثل `.`، `*`، و `?`. لمطابقتها حرفيًا، قم بتهريبها باستخدام `\\`:
- لمطابقة نقطة: `"\."`
- في سلاسل جافا، قم بتهريب الشرطات المائلة للخلف: `"\\d"` للأرقام، `"\\\\"` لشرطة مائلة للخلف حرفية.

### الأداء
تصريف النمط مكلف. أعد استخدام كائنات `Pattern` عندما يكون ذلك ممكنًا:
```java
Pattern pattern = Pattern.compile("\\d+"); // اصرفه مرة واحدة
for (String input : new String[]{"123", "456"}) {
    Matcher matcher = pattern.matcher(input);
    if (matcher.matches()) {
        System.out.println("Number: " + input);
    }
}
```

### معالجة الأخطاء
تطرح أنماط التعبير النمطي غير الصالحة استثناء `PatternSyntaxException`. تعامل معه في كود الإنتاج:
```java
try {
    Pattern pattern = Pattern.compile("["); // تعبير نمطي غير صالح
} catch (PatternSyntaxException e) {
    System.err.println("Invalid regex: " + e.getMessage());
}
```

## الملخص

- **اصرف نمطًا**: `Pattern.compile(regex)`
- **أنشئ مُطابِقًا**: `pattern.matcher(input)`
- **العمليات الرئيسية**:
  - `matches()`: مطابقة السلسلة الكاملة
  - `find()`: العثور على المطابقة التالية
  - `group()`: استخراج النص المطابق
  - `replaceAll()`: استبدال المطابقات
- **الراحة**: استخدم طرق `String` للمهام البسيطة.
- **أفضل الممارسات**: اهرب الأحرف الخاصة، أعد استخدام الأنماط، وتعامل مع الاستثناءات.

يغطي هذا أساسيات `java.util.regex`. للمواضيع المتقدمة مثل lookaheads أو فئات الأحرف، استشر [توثيق جافا](https://docs.oracle.com/en/java/javase/17/docs/api/java.util.regex/package-summary.html) أو جرّب حالات استخدام محددة!