---
audio: false
generated: true
lang: ar
layout: post
title: الواجهات الوظيفية في جافا
translated: true
type: note
---

توفّر حزمة `java.util.function` في جافا مجموعة من الواجهات الوظيفية المصممة لدعم البرمجة الوظيفية، والتي أُدخلت في جافا 8. تمتلك كل من هذه الواجهات طريقة مجردة واحدة، مما يجعلها متوافقة مع تعبيرات لامدا والإشارات إلى الأساليب. يشرح هذا الرد كيفية استخدام بعض الواجهات الوظيفية الأكثر شيوعًا في هذه الحزمة—`Function<T, R>`, `Predicate<T>`, `Consumer<T>`, و `Supplier<T>`—مع أمثلة عملية.

---

### ما هي الواجهات الوظيفية؟
الواجهة الوظيفية هي واجهة تحتوي على طريقة مجردة واحدة بالضبط. توفّر حزمة `java.util.function` واجهات وظيفية مُحددة مسبقًا للمهام الشائعة، لذا لا تحتاج إلى إنشاء واجهاتك الخاصة. تُستخدم هذه الواجهات على نطاق واسع مع تعبيرات لامدا، والإشارات إلى الأساليب، وواجهة برمجة Stream لكتابة كود موجز ومعبّر.

إليك كيفية استخدام الواجهات الرئيسية:

---

### 1. `Function<T, R>`: تحويل المدخلات إلى مخرجات
تمثل واجهة `Function<T, R>` دالة تأخذ مدخلًا من النوع `T` وتنتج مخرجًا من النوع `R`. طريقتها المجردة هي `apply`.

#### مثال: الحصول على طول السلسلة النصية
```java
import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        Function<String, Integer> stringLength = s -> s.length();
        System.out.println(stringLength.apply("Hello")); // المخرجات: 5
    }
}
```
- **الشرح**: يحدد تعبير لامدا `s -> s.length()` `Function` تأخذ `String` (`T`) وترجع `Integer` (`R`). تنفذ طريقة `apply` هذا المنطق.

---

### 2. `Predicate<T>`: اختبار شرط
تمثل واجهة `Predicate<T>` دالة ذات قيمة منطقية تأخذ مدخلًا من النوع `T`. طريقتها المجردة هي `test`.

#### مثال: التحقق مما إذا كان الرقم زوجيًا
```java
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        Predicate<Integer> isEven = n -> n % 2 == 0;
        System.out.println(isEven.test(4)); // المخرجات: true
        System.out.println(isEven.test(5)); // المخرجات: false
    }
}
```
- **الشرح**: يحدد تعبير لامدا `n -> n % 2 == 0` `Predicate` ترجع `true` إذا كان المدخل زوجيًا. تقيّم طريقة `test` هذا الشرط.

---

### 3. `Consumer<T>`: تنفيذ إجراء
تمثل واجهة `Consumer<T>` عملية تأخذ مدخلًا من النوع `T` ولا ترجع أي نتيجة. طريقتها المجردة هي `accept`.

#### مثال: طباعة سلسلة نصية
```java
import java.util.function.Consumer;

public class Main {
    public static void main(String[] args) {
        Consumer<String> printer = s -> System.out.println(s);
        printer.accept("Hello, World!"); // المخرجات: Hello, World!
    }
}
```
- **الشرح**: يحدد تعبير لامدا `s -> System.out.println(s)` `Consumer` تطبع مدخلاتها. تنفذ طريقة `accept` هذا الإجراء.

---

### 4. `Supplier<T>`: توليد نتيجة
تمثل واجهة `Supplier<T>` موردًا للنتائج، لا تأخذ أي مدخل وتُرجع قيمة من النوع `T`. طريقتها المجردة هي `get`.

#### مثال: توليد رقم عشوائي
```java
import java.util.function.Supplier;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Supplier<Integer> randomInt = () -> new Random().nextInt(100);
        System.out.println(randomInt.get()); // يُخرج عددًا صحيحًا عشوائيًا بين 0 و 99
    }
}
```
- **الشرح**: يحدد تعبير لامدا `() -> new Random().nextInt(100)` `Supplier` يولد عددًا صحيحًا عشوائيًا. تسترجع طريقة `get` القيمة.

---

### استخدام الواجهات الوظيفية مع Streams
تظهر هذه الواجهات بشكل رائع في واجهة برمجة Java Stream، حيث تتيح معالجة البيانات بشكل موجز. إليك مثال يقوم بتصفية وتحويل وطباعة قائمة من السلاسل النصية:

#### مثال: معالجة قائمة من السلاسل النصية
```java
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        List<String> strings = Arrays.asList("a", "bb", "ccc", "dddd");

        Predicate<String> longerThanTwo = s -> s.length() > 2;       // تصفية السلاسل الأطول من 2
        Function<String, String> toUpperCase = s -> s.toUpperCase(); // التحويل إلى أحرف كبيرة
        Consumer<String> printer = s -> System.out.println(s);       // طباعة كل نتيجة

        strings.stream()
               .filter(longerThanTwo)   // تحتفظ بـ "ccc" و "dddd"
               .map(toUpperCase)        // تحول إلى "CCC" و "DDDD"
               .forEach(printer);       // المخرجات: CCC, DDDD (على أسطر منفصلة)
    }
}
```
- **الشرح**: 
  - يستخدم `filter` `Predicate` للاحتفاظ بالسلاسل التي يزيد طولها عن 2.
  - يستخدم `map` `Function` لتحويل السلاسل إلى أحرف كبيرة.
  - يستخدم `forEach` `Consumer` لطباعة كل نتيجة.

#### استخدام الإشارات إلى الأساليب
يمكنك جعل هذا أقصر باستخدام الإشارات إلى الأساليب:
```java
strings.stream()
       .filter(s -> s.length() > 2)
       .map(String::toUpperCase)      // إشارة إلى أسلوب لـ Function
       .forEach(System.out::println); // إشارة إلى أسلوب لـ Consumer
```

---

### تأليف الواجهات الوظيفية
تسمح بعض الواجهات بالتأليف لعمليات أكثر تعقيدًا:
- **تأليف الدوال**: استخدم `andThen` أو `compose`.
  ```java
  Function<String, Integer> toLength = s -> s.length();
  Function<Integer, String> toString = i -> "Length is " + i;
  Function<String, String> combined = toLength.andThen(toString);
  System.out.println(combined.apply("Hello")); // المخرجات: Length is 5
  ```
- **دمج الشروط**: استخدم `and`, `or`, أو `negate`.
  ```java
  Predicate<String> isLong = s -> s.length() > 5;
  Predicate<String> startsWithA = s -> s.startsWith("A");
  Predicate<String> isLongAndStartsWithA = isLong.and(startsWithA);
  System.out.println(isLongAndStartsWithA.test("Avocado")); // المخرجات: true
  ```

---

### الملخص
إليك متى وكيف تستخدم هذه الواجهات:
- **`Function<T, R>`**: تحويل مدخل إلى مخرج (مثل `apply`).
- **`Predicate<T>`**: اختبار شرط (مثل `test`).
- **`Consumer<T>`**: تنفيذ إجراء على مدخل (مثل `accept`).
- **`Supplier<T>`**: توليد قيمة بدون مدخل (مثل `get`).
- **مع Streams**: اجمعها لمعالجة بيانات قوية.
- **التأليف**: اربطها أو اجمعها لمنطق معقد.

يمكنك تنفيذ هذه الواجهات باستخدام تعبيرات لامدا (مثل `s -> s.length()`) أو الإشارات إلى الأساليب (مثل `String::toUpperCase`). تتيح هذه الواجهات أسلوب برمجة وظيفي في جافا، مما يجعل كودك أكثر إيجازًا وقابلية للقراءة وإعادة الاستخدام، خاصة مع واجهة برمجة Stream.