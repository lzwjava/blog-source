---
audio: false
generated: true
lang: ar
layout: post
title: واجهة برمجة التطبيقات للتدفق في جافا
translated: true
type: note
---

لاستخدام `java.util.stream` في Java، يمكنك الاستفادة من Stream API التي تم تقديمها في Java 8 لمعالجة مجموعات البيانات بطريقة وظيفية وتقريرية. تتيح لك الـ Streams تنفيذ عمليات مثل التصفية، والتحويل، والاختزال على تسلسلات العناصر (مثل القوائم أو المصفوفات) بكفاءة وإيجاز. أدناه، سأشرح كيفية استخدام `java.util.stream` من خلال المشي في مثال محدد: إيجاد متوسط الأرقام الزوجية الأكبر من 10 من قائمة بالأعداد الصحيحة. سيوضح هذا عمليات ومفاهيم الـ Stream الأساسية.

---

### **نظرة عامة على `java.util.stream`**
توفر حزمة `java.util.stream` واجهة `Stream` والفئات ذات الصلة (مثل `IntStream`، `DoubleStream`، إلخ) لمعالجة البيانات. الـ Stream هو تسلسل من العناصر يدعم العمليات التي يتم تنفيذها في خط أنابيب. هذه العمليات هي:
- **العمليات الوسيطة**: تقوم بتحويل أو تصفية الـ Stream (مثل `filter`، `map`)، وتُرجع stream جديدًا. هذه العمليات كسولة ولا يتم تنفيذها إلا عند استدعاء عملية نهائية.
- **العمليات النهائية**: تنتج نتيجة أو تأثيرًا جانبيًا (مثل `average`، `collect`)، مما يؤدي إلى تشغيل خط الأنابيب لمعالجة البيانات.

لاستخدام الـ Streams، تقوم بشكل نموذجي بـ:
1. إنشاء stream من مصدر بيانات (مثل قائمة).
2. تطبيق عمليات وسيطة لتحويل البيانات أو تصفيتها.
3. استخدام عملية نهائية لإنتاج نتيجة.

---

### **مثال للمشكلة**
لنحل هذه المشكلة: بالنظر إلى `List<Integer>`، احسب متوسط جميع الأرقام الزوجية الأكبر من 10. إذا لم توجد مثل هذه الأرقام، فارجع 0.0. إليك كيفية القيام بذلك باستخدام `java.util.stream`.

#### **الحل خطوة بخطوة**
1. **إنشاء Stream**
   - ابدأ بـ `List<Integer>` (مثال: `List.of(1, 2, 12, 15, 20, 25, 30)`).
   - استخدم الطريقة `stream()` لإنشاء `Stream<Integer>`:
     ```java
     list.stream()
     ```

2. **تصفية الـ Stream**
   - استخدم الطريقة `filter` للاحتفاظ بالأرقام الزوجية فقط والأكبر من 10.
   - تأخذ الطريقة `filter` `Predicate` (دالة تُرجع قيمة منطقية) كتعبير لامدا:
     ```java
     .filter(number -> number % 2 == 0 && number > 10)
     ```
     - `number % 2 == 0` تتحقق مما إذا كان الرقم زوجيًا.
     - `number > 10` تضمن أن الرقم أكبر من 10.
     - بالنسبة للقائمة المثال `[1, 2, 12, 15, 20, 25, 30]`، هذا يحتفظ بـ `[12, 20, 30]`.

3. **التحويل إلى `IntStream`**
   - نظرًا لأن `average()` متاحة على الـ Streams البدائية مثل `IntStream` (وليس `Stream<Integer>`)، قم بتحويل `Stream<Integer>` إلى `IntStream` باستخدام `mapToInt`:
     ```java
     .mapToInt(i -> i)
     ```
     - `i -> i` تقوم بفك تغليف كل `Integer` إلى `int`. بدلاً من ذلك، يمكنك استخدام `Integer::intValue`.
     - هذا يعطي `IntStream` لـ `[12, 20, 30]`.

4. **حساب المتوسط**
   - استخدم الطريقة `average()` على `IntStream`، والتي تُرجع `OptionalDouble` (نظرًا لأن الـ Stream قد يكون فارغًا):
     ```java
     .average()
     ```
     - بالنسبة لـ `[12, 20, 30]`، هذا يحسب `(12 + 20 + 30) / 3 = 20.666...`.
     - إذا كان الـ Stream فارغًا، فإنه يُرجع `OptionalDouble` فارغًا.

5. **معالجة الحالة الفارغة**
   - استخدم `orElse(0.0)` على `OptionalDouble` لإرجاع 0.0 إذا لم توجد أرقام تُرضي عامل التصفية:
     ```java
     .orElse(0.0)
     ```
     - بالنسبة لـ `[12, 20, 30]`، هذا يُرجع `20.666...`.
     - بالنسبة لقائمة مثل `[1, 3, 5]` (لا توجد أرقام زوجية > 10)، فإنها تُرجع `0.0`.

#### **الكود الكامل**
إليك الحل الكامل كدالة:
```java
import java.util.List;

public class Main {
    public static double averageOfEvenGreaterThanTen(List<Integer> list) {
        return list.stream()
                   .filter(number -> number % 2 == 0 && number > 10)
                   .mapToInt(i -> i)
                   .average()
                   .orElse(0.0);
    }

    public static void main(String[] args) {
        // حالات اختبار
        System.out.println(averageOfEvenGreaterThanTen(List.of(1, 2, 12, 15, 20, 25, 30)));  // ~20.666
        System.out.println(averageOfEvenGreaterThanTen(List.of(1, 3, 5)));                    // 0.0
        System.out.println(averageOfEvenGreaterThanTen(List.of(12)));                         // 12.0
        System.out.println(averageOfEvenGreaterThanTen(List.of()));                           // 0.0
        System.out.println(averageOfEvenGreaterThanTen(List.of(10, 8, 6)));                   // 0.0
        System.out.println(averageOfEvenGreaterThanTen(List.of(11, 13, 14, 16)));             // 15.0
    }
}
```

---

### **الميزات الرئيسية لـ `java.util.stream` الموضحة**
- **التسلسل**: يتم ربط العمليات بأسلوب سلس (مثال: `.filter().mapToInt().average()`).
- **الكسل**: لا يتم تنفيذ العمليات الوسيطة (مثل `filter` و `mapToInt`) إلا عند استدعاء العملية النهائية (`average`).
- **الـ Streams البدائية**: توفر `IntStream` طرقًا مثل `average()` مصممة خصيصًا للعمليات العددية، مما يتجنب عبء فك وتغليف القيم.
- **معالجة الـ Optional**: يتعامل `OptionalDouble` مع الحالات التي لا توجد فيها نتيجة، مع توفير `orElse` لقيمة افتراضية.

---

### **طريقة بديلة**
يمكنك أيضًا استخدام فئة `Collectors`:
```java
import java.util.stream.Collectors;

double average = list.stream()
                     .filter(number -> number % 2 == 0 && number > 10)
                     .collect(Collectors.averagingInt(i -> i));
```
- هذا يُرجع `Double` مباشرة ويُرجع `0.0` لـ stream فارغ. ومع ذلك، فإن `mapToInt().average()` أكثر مباشرة في هذه الحالة البسيطة ويتوافق مع استخدام الـ Streams البدائية.

---

### **متى تستخدم الـ Streams**
- استخدم `java.util.stream` للحصول على كود موجز وسهل القراءة عند معالجة المجموعات.
- لمجموعات البيانات الكبيرة، فكر في استخدام `parallelStream()` بدلاً من `stream()` للاستفادة من التوازي، على الرغم من أن هذا مبالغة فيه للقوائم الصغيرة بسبب النفقات العامة.

---

يُظهر هذا المثال كيفية استخدام `java.util.stream` لحل مشكلة عملية. يمكنك تكييف هذه الخطوات—إنشاء stream، والتصفية، والتحويل، والاختزال—لتناسب سيناريوهات أخرى حسب الحاجة!