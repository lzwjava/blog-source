---
audio: false
generated: true
lang: ar
layout: post
title: العبارات العادية في جاڤا
translated: true
---

# كيفية استخدام `java.util.regex` في جاڤا

يوفر حزمة `java.util.regex` في جاڤا أدواتًا للعمل مع التعبيرات العادية (regex)، والتي هي نماذج تستخدم لمطابقة وتعديل النص. سيقوم هذا الدليل بتمريرك عبر أساسيات استخدام هذه الحزمة، مع التركيز على الفئتين الرئيسيتين: `Pattern` و `Matcher`. سأغطي أيضًا حالات الاستخدام الشائعة مع أمثلة لمساعدتك على البدء.

## نظرة عامة على `java.util.regex`

تضم حزمة `java.util.regex`:

- **`Pattern`**: يمثل تعبيرًا عاديًا مدمجًا. تخلقها من سلسلة regex.
- **`Matcher`**: يطبق النمط على سلسلة إدخال محددة ويؤدي عمليات المطابقة.

بالإضافة إلى ذلك، تقدم فئة `String` في جاڤا طرقًا تعتمد على regex لأغراض أبسط.

## الخطوات الأساسية لاستخدام `java.util.regex`

لتستخدم التعبيرات العادية في جاڤا، اتبع هذه الخطوات:

1. **تجميع نمط**: تحويل سلسلة regex إلى كائن `Pattern`.
2. **إنشاء Matcher**: استخدام النمط لإنشاء `Matcher` للنص المدخل.
3. **إجراء العمليات**: استخدام Matcher للتحقق من المطابقة، العثور على الأنماط، أو تعديل النص.

هكذا يعمل في الممارسة.

## مثال 1: التحقق من صحة عنوان بريد إلكتروني

نخلق مصفوفة بسيطة للتحقق من صحة البريد الإلكتروني باستخدام نمط regex الأساسي: `".+@.+\\..+"`. يطابق هذا النمط السلاسل التي تحتوي على حرف واحد على الأقل قبل و بعد رمز `@`، متبوعًا بنقطة و أحرف أخرى (مثل `example@test.com`).

```java
import java.util.regex.*;

public class EmailValidator {
    public static boolean isValidEmail(String email) {
        // تحديد نمط regex
        String regex = ".+@.+\\..+";
        // تجميع النمط
        Pattern pattern = Pattern.compile(regex);
        // إنشاء Matcher للنص المدخل
        Matcher matcher = pattern.matcher(email);
        // التحقق من أن السلسلة بأكملها تطابق النمط
        return matcher.matches();
    }

    public static void main(String[] args) {
        String email = "example@test.com";
        if (isValidEmail(email)) {
            System.out.println("عنوان بريد إلكتروني صحيح");
        } else {
            System.out.println("عنوان بريد إلكتروني غير صحيح");
        }
    }
}
```

### شرح
- **`Pattern.compile(regex)`**: يجمع السلسلة regex إلى كائن `Pattern`.
- **`pattern.matcher(email)`**: يخلق Matcher للنص المدخل `email`.
- **`matcher.matches()`**: يعيد `true` إذا تطابقت السلسلة بأكملها مع النمط، `false` في حال أخرى.

**الخرج**: `عنوان بريد إلكتروني صحيح`

ملاحظة: هذا نمط بريد إلكتروني بسيط. يتطلب التحقق من صحة البريد الإلكتروني الحقيقي نمط regex أكثر تعقيدًا (مثل RFC 5322)، ولكن هذا يخدم كبداية.

## مثال 2: العثور على جميع الهاشتاجات في سلسلة

فرضًا أنك تريد استخراج جميع الهاشتاجات (مثل `#java`) من تويت. استخدم النمط regex `"#\\w+"`، حيث `#` يطابق رمز الهاشتاج الحرفية و `\\w+` يطابق حرف واحد أو أكثر (أحرف، أرقام، أو خطوط تحتية).

```java
import java.util.regex.*;

public class HashtagExtractor {
    public static void main(String[] args) {
        String tweet = "هذا هو تويت #مثال مع #هاشتاجات متعددة مثل #java";
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

### شرح
- **`matcher.find()`**: يتحرك إلى المطابقة التالية في السلسلة المدخلية ويعيد `true` إذا وجد مطابقة.
- **`matcher.group()`**: يعيد النص المطابق للمطابقة الحالية.

**الخرج**:
```
#مثال
#هاشتاجات
#java
```

## مثال 3: استبدال النص باستخدام regex

لاستبدال جميع ظهور كلمة (مثل إخفاء "badword" بأستار)، يمكنك استخدام طريقة `String.replaceAll()`، التي تستخدم regex داخليًا.

```java
public class TextCensor {
    public static void main(String[] args) {
        String text = "هذا هو مثال badword مع badword مكرر.";
        String censored = text.replaceAll("badword", "*******");
        System.out.println(censored);
    }
}
```

**الخرج**: `هذا هو مثال ******* مع ******* مكرر.`

لاستبدالات أكثر تعقيدًا، استخدم `Matcher`:

```java
import java.util.regex.*;

public class ComplexReplacement {
    public static void main(String[] args) {
        String text = "اتصل: 123-456-7890";
        String regex = "\\d{3}-\\d{3}-\\d{4}"; // يطابق أرقام الهاتف
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);
        String result = matcher.replaceAll("XXX-XXX-XXXX");
        System.out.println(result);
    }
}
```

**الخرج**: `اتصل: XXX-XXX-XXXX`

## مثال 4: استخدام المجموعات لفك تشفير البيانات المهيئة

تسمح مجموعات regex، التي يتم تعريفها مع الأقواس `()`, بكتابة أجزاء من المطابقة. على سبيل المثال، لفك تشفير رقم التأمين الاجتماعي (SSN) مثل `123-45-6789`:

```java
import java.util.regex.*;

public class SSNParser {
    public static void main(String[] args) {
        String ssn = "123-45-6789";
        String regex = "(\\d{3})-(\\d{2})-(\\d{4})"; // مجموعات للمنطقة، المجموعة، الرقم التسلسلي
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(ssn);

        if (matcher.matches()) {
            System.out.println("رقم المنطقة: " + matcher.group(1));
            System.out.println("رقم المجموعة: " + matcher.group(2));
            System.out.println("رقم التسلسلي: " + matcher.group(3));
        }
    }
}
```

### شرح
- **`"(\\d{3})-(\\d{2})-(\\d{4})"`**: يحدد ثلاثة مجموعات:
  - مجموعة 1: `\\d{3}` (ثلاثة أرقام)
  - مجموعة 2: `\\d{2}` (أرقامتين)
  - مجموعة 3: `\\d{4}` (أربعة أرقام)
- **`matcher.group(n)`**: يسترجع النص المطابق للمجموعة `n` (مؤشر 1-based).

**الخرج**:
```
رقم المنطقة: 123
رقم المجموعة: 45
رقم التسلسلي: 6789
```

يمكنك أيضًا استخدام **المجموعات المسماة** للوضوح:

```java
String regex = "(?<area>\\d{3})-(?<group>\\d{2})-(?<serial>\\d{4})";
Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher("123-45-6789");
if (matcher.matches()) {
    System.out.println("منطقة: " + matcher.group("area"));
    System.out.println("مجموعة: " + matcher.group("group"));
    System.out.println("تسلسلي: " + matcher.group("serial"));
}
```

## ميزات إضافية ونصائح

### أعلام
تعديل سلوك النمط باستخدام أعلام في `Pattern.compile()`:
- **`Pattern.CASE_INSENSITIVE`**: تجاهل الحروف الكبيرة والصغيرة عند المطابقة.
  ```java
  Pattern pattern = Pattern.compile("hello", Pattern.CASE_INSENSITIVE);
  Matcher matcher = pattern.matcher("HELLO");
  System.out.println(matcher.matches()); // true
  ```

### طرق السلسلة
لأغراض بسيطة، استخدم طرق `String`:
- **`matches()`**: التحقق من أن السلسلة بأكملها تطابق regex.
  ```java
  String text = "cat";
  System.out.println(text.matches("\\w{3}")); // true
  ```
- **`split()`**: تقسيم السلسلة بواسطة نمط regex.
  ```java
  String data = "tuffah, banan, kersh";
  String[] fruits = data.split("\\s*,\\s*");
  // الخرج: tuffah, banan, kersh
  ```

### الهروب من الأحرف الخاصة
تستخدم regex أحرفًا خاصة مثل `.` و `*` و `?`. لتطابقهم حرفيًا، هرب من `\\`:
- تطابق نقطة: `"\\."`
- في سلاسل جاڤا، هرب من السطر الخلفي: `"\\d"` للأرقام، `"\\\\"` لسطر الخلفي حرفية.

### الأداء
تجميع نمط هو مكلف. إعادة استخدام كائنات `Pattern` كلما أمكن:
```java
Pattern pattern = Pattern.compile("\\d+"); // تجميع مرة واحدة
for (String input : new String[]{"123", "456"}) {
    Matcher matcher = pattern.matcher(input);
    if (matcher.matches()) {
        System.out.println("رقم: " + input);
    }
}
```

### معالجة الأخطاء
تسبب الأنماط regex غير الصالحة في `PatternSyntaxException`. قم بمعالجتها في الكود الإنتاجي:
```java
try {
    Pattern pattern = Pattern.compile("["); // نمط regex غير صحيح
} catch (PatternSyntaxException e) {
    System.err.println("نمط regex غير صحيح: " + e.getMessage());
}
```

## ملخص

- **تجميع نمط**: `Pattern.compile(regex)`
- **إنشاء Matcher**: `pattern.matcher(input)`
- **عمليات رئيسية**:
  - `matches()`: تطابق السلسلة بأكملها
  - `find()`: العثور على المطابقة التالية
  - `group()`: استخراج النص المطابق
  - `replaceAll()`: استبدال المطابقات
- **راحة**: استخدم طرق `String` لأغراض بسيطة.
- **أفضل الممارسات**: هرب من الأحرف الخاصة، إعادة استخدام الأنماط، ومعالجة الاستثناءات.

هذا يغطي أساسيات `java.util.regex`. لموضوعات متقدمة مثل النظرات إلى الأمام أو فئات الأحرف، استشارك [التوثيق الرسمي لجاڤا](https://docs.oracle.com/en/java/javase/17/docs/api/java.util.regex/package-summary.html) أو تجريب مع حالات استخدام محددة!