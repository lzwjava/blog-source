---
audio: false
generated: true
lang: ar
layout: post
title: الواجهات الوظيفية في جافا
translated: true
---

العبارة `java.util.function` في جافا تقدم مجموعة من الواجهات الوظيفية التي صممت لدعم البرمجة الوظيفية، والتي تم تقديمها في جافا 8. تحتوي هذه الواجهات على طريقة مجردة واحدة، مما يجعلها متوافقة مع تعبيرات اللامبدا ومقاطع الطرق. يشرح هذا الرد كيفية استخدام بعض أكثر الواجهات الوظيفية شيوعًا في هذه العبارة—`Function<T, R>`, `Predicate<T>`, `Consumer<T>`, و `Supplier<T>`—مع أمثلة عملية.

---

### ما هي الواجهات الوظيفية؟
الواجهة الوظيفية هي واجهة تحتوي على طريقة مجردة واحدة. تقدم العبارة `java.util.function` الواجهات الوظيفية المسبقة تعريفًا لمهام شائعة، فلا تحتاج إلى إنشاء الخاصة بك. تستخدم هذه الواجهات بشكل واسع مع تعبيرات اللامبدا ومقاطع الطرق وواجهة التدفق لتكتب كودًا مختصرًا ومفيدًا.

هنا كيفية استخدام الواجهات الرئيسية:

---

### 1. `Function<T, R>`: تحويل المدخل إلى المخرج
تمثل الواجهة `Function<T, R>` وظيفة تأخذ مدخلًا من نوع `T` وتنتج مخرجًا من نوع `R`. طريقةها المجردة هي `apply`.

#### مثال: الحصول على طول سلسلة
```java
import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        Function<String, Integer> stringLength = s -> s.length();
        System.out.println(stringLength.apply("Hello")); // يخرج: 5
    }
}
```
- **شرح**: يعرّف تعبير اللامبدا `s -> s.length()` وظيفة تأخذ سلسلة (`T`) وتعيد عددًا (`R`). تقوم طريقة `apply` بتنفيذ هذه المنطقية.

---

### 2. `Predicate<T>`: اختبار شرط
تمثل الواجهة `Predicate<T>` وظيفة ذات قيمة منطقية تأخذ مدخلًا من نوع `T`. طريقةها المجردة هي `test`.

#### مثال: التحقق من أن الرقم زوجي
```java
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        Predicate<Integer> isEven = n -> n % 2 == 0;
        System.out.println(isEven.test(4)); // يخرج: صحيح
        System.out.println(isEven.test(5)); // يخرج: خاطئ
    }
}
```
- **شرح**: يعرّف اللامبدا `n -> n % 2 == 0` شرطًا يعود `صحيح` إذا كان المدخل زوجيًا. تقوم طريقة `test` بتقييم هذا الشرط.

---

### 3. `Consumer<T>`: تنفيذ عمل
تمثل الواجهة `Consumer<T>` عملية تأخذ مدخلًا من نوع `T` ولا تعيد أي نتيجة. طريقةها المجردة هي `accept`.

#### مثال: طباعة سلسلة
```java
import java.util.function.Consumer;

public class Main {
    public static void main(String[] args) {
        Consumer<String> printer = s -> System.out.println(s);
        printer.accept("Hello, World!"); // يخرج: Hello, World!
    }
}
```
- **شرح**: يعرّف اللامبدا `s -> System.out.println(s)` مستهلكًا يطبع مدخله. تقوم طريقة `accept` بتنفيذ العمل.

---

### 4. `Supplier<T>`: توليد نتيجة
تمثل الواجهة `Supplier<T>` مورد نتائج، لا يأخذ مدخلًا ويعيد قيمة من نوع `T`. طريقةها المجردة هي `get`.

#### مثال: توليد عدد عشوائي
```java
import java.util.function.Supplier;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Supplier<Integer> randomInt = () -> new Random().nextInt(100);
        System.out.println(randomInt.get()); // يخرج عددًا عشوائيًا بين 0 و 99
    }
}
```
- **شرح**: يعرّف اللامبدا `() -> new Random().nextInt(100)` موردًا يولد عددًا عشوائيًا. تقوم طريقة `get` بجلب القيمة.

---

### استخدام الواجهات الوظيفية مع التدفقات
تلمع هذه الواجهات في واجهة التدفق في جافا، حيث تتيح معالجة البيانات بشكل مختصر. هنا مثال يصف، يصف، ويطبع قائمة من السلاسل:

#### مثال: معالجة قائمة من السلاسل
```java
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        List<String> strings = Arrays.asList("a", "bb", "ccc", "dddd");

        Predicate<String> longerThanTwo = s -> s.length() > 2;       // تصفية السلاسل أطول من 2
        Function<String, String> toUpperCase = s -> s.toUpperCase(); // تحويل إلى حروف كبيرة
        Consumer<String> printer = s -> System.out.println(s);       // طباعة كل نتيجة

        strings.stream()
               .filter(longerThanTwo)   // يحتفظ بـ "ccc" و "dddd"
               .map(toUpperCase)        // تحويل إلى "CCC" و "DDDD"
               .forEach(printer);       // يخرج: CCC, DDDD (في أسطر منفصلة)
    }
}
```
- **شرح**:
  - تستخدم `filter` شرطًا لتحتفظ بالسلاسل أطول من 2.
  - تستخدم `map` وظيفة لتحويل السلاسل إلى حروف كبيرة.
  - تستخدم `forEach` مستهلكًا لطباعة كل نتيجة.

#### استخدام مقاطع الطرق
يمكنك جعل هذا أقصر باستخدام مقاطع الطرق:
```java
strings.stream()
       .filter(s -> s.length() > 2)
       .map(String::toUpperCase)      // مقطع الطريق للمفوض
       .forEach(System.out::println); // مقطع الطريق للمستهلك
```

---

### تركيب الواجهات الوظيفية
تسمح بعض الواجهات بالتركيب لمهام أكثر تعقيدًا:
- **تركيب الوظيفة**: استخدم `andThen` أو `compose`.
  ```java
  Function<String, Integer> toLength = s -> s.length();
  Function<Integer, String> toString = i -> "Length is " + i;
  Function<String, String> combined = toLength.andThen(toString);
  System.out.println(combined.apply("Hello")); // يخرج: Length is 5
  ```
- **تركيب الشرط**: استخدم `and`, `or`, أو `negate`.
  ```java
  Predicate<String> isLong = s -> s.length() > 5;
  Predicate<String> startsWithA = s -> s.startsWith("A");
  Predicate<String> isLongAndStartsWithA = isLong.and(startsWithA);
  System.out.println(isLongAndStartsWithA.test("Avocado")); // يخرج: صحيح
  ```

---

### ملخص
هنا متى وكيف تستخدم هذه الواجهات:
- **`Function<T, R>`**: تحويل مدخل إلى مخرج (مثل `apply`).
- **`Predicate<T>`**: اختبار شرط (مثل `test`).
- **`Consumer<T>`**: تنفيذ عمل على مدخل (مثل `accept`).
- **`Supplier<T>`**: توليد قيمة بدون مدخل (مثل `get`).
- **مع التدفقات**: قم بدمجهم لمعالجة البيانات القوية.
- **التركيب**: قم بتسلسلهم أو دمجهم لمهام معقدة.

يمكنك تنفيذ هذه الواجهات باستخدام تعبيرات اللامبدا (مثل `s -> s.length()`) أو مقاطع الطرق (مثل `String::toUpperCase`). تتيح لك هذه الواجهات أسلوب البرمجة الوظيفية في جافا، مما يجعل كودك أكثر اختصارًا، قابلية للقراءة، وإعادة الاستخدام، خاصة مع واجهة التدفق.