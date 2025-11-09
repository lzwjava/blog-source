---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دليل البرمجة الوظيفية في جافا
translated: true
type: note
---

تبنى Java مبادئ البرمجة الوظيفية منذ الإصدار Java 8، حيث قدمت تعبيرات Lambda، والتدفقات (Streams)، وميزات أخرى تجعل الشفرة أكثر إيجازاً وقابلية للقراءة وتصريحية (declarative). يغطي هذا الدليل الأساسيات وصولاً إلى المفاهيم المتقدمة، بافتراض الإلمام بـ Java الأساسية. سنستخدم صيغة Java 8+، فهي الفترة التي ظهرت فيها هذه الميزات. الأمثلة مكتوبة داخل كتل كود Java لسهولة النسخ.

## 1. مقدمة في البرمجة الوظيفية في Java

تركز البرمجة الوظيفية (FP) على:
- **الدوال الخالصة (Pure functions)**: دوال بدون تأثيرات جانبية (مثل عدم تغيير حالة متغيرة).
- **الثبات (Immutability)**: البيانات لا تتغير بمجرد إنشائها.
- **الدوال ذات الرتبة الأعلى (Higher-order functions)**: دوال تأخذ دوالاً أخرى كمدخلات أو تُرجعها كمخرجات.
- **النمط التصريحي (Declarative style)**: التركيز على *ماذا* نريد فعله، وليس *كيف* (على سبيل المثال، باستخدام الـ Streams بدلاً من الحلقات).

ليست Java لغة وظيفية بحتة مثل Haskell، لكنها تدمج البرمجة الوظيفية مع جذورها كائنية التوجه. المُمكنات الرئيسية:
- تعبيرات Lambda (دوال مجهولة الاسم).
- الواجهات الوظيفية (Functional interfaces) (واجهات تحتوي على دالة مجردة واحدة).
- Streams API لمعالجة المجموعات (Collections) بشكل وظيفي.

الفوائد: تقليل الشفرة المتكررة، تسهيل التوازي (parallelism)، قابلية أفضل للتركيب (composability).

## 2. تعبيرات Lambda

تعبيرات Lambda هي دوال مجهولة الاسم تُستخدم للتطبيقات القصيرة والمرحلية. إنها المدخل إلى البرمجة الوظيفية في Java.

### الصيغة الأساسية
تعبير Lambda هو: `(معاملات الإدخال) -> { جسم الدالة }`
- الأقواس اختيارية لمعامل إدخال واحد.
- الأقواس المعقوفة اختيارية لعبارة واحدة (يُفترض وجود return).
- الاستدلال على النوع (Type inference) يعمل غالباً، ولكن يمكنك تحديد الأنواع.

```java
// الفئة الداخلية المجهولة التقليدية
Runnable r = new Runnable() {
    @Override
    public void run() {
        System.out.println("Hello, World!");
    }
};

// المكافئ باستخدام Lambda
Runnable lambda = () -> System.out.println("Hello, World!");
lambda.run();
```

### مع معاملات الإدخال
```java
// مثال على عامل ثنائي (Binary operator)
BinaryOperator<Integer> add = (a, b) -> a + b;
System.out.println(add.apply(2, 3)); // 5

// جسم متعدد الأسطر
Comparator<String> comparator = (s1, s2) -> {
    int lenDiff = s1.length() - s2.length();
    return lenDiff != 0 ? lenDiff : s1.compareTo(s2);
};
```

### التقاط المتغيرات (Effectively Final)
يمكن لـ Lambda الوصول إلى المتغيرات الخارجية، ولكن يجب أن تكون **فعلياً نهائية (effectively final)** (لا يتم إعادة تعيينها).
```java
int threshold = 10;
Predicate<Integer> isHigh = x -> x > threshold; // مسموح
// threshold = 20; // خطأ: ليست فعلياً نهائية
```

## 3. الواجهات الوظيفية

الواجهة الوظيفية (Functional Interface) تحتوي بالضبط على دالة مجردة واحدة (SAM - Single Abstract Method). توفر Java واجهات مدمجة في `java.util.function`.

### أمثلة مدمجة
- `Predicate<T>`: `boolean test(T t)`
- `Function<T, R>`: `R apply(T t)`
- `Consumer<T>`: `void accept(T t)`
- `Supplier<T>`: `T get()`
- `BiFunction<T, U, R>`، إلخ، لمدخلين.

واجهات مخصصة:
```java
@FunctionalInterface  // اختياري، لكنه ممارسة جيدة
interface Transformer {
    String transform(String input);
}

Transformer upper = s -> s.toUpperCase();
System.out.println(upper.transform("java")); // JAVA
```

استخدم `@FunctionalInterface` لفرض قاعدة SAM.

### الدوال الافتراضية والثابتة
يمكن للواجهات الوظيفية أن تحتوي على دوال افتراضية (Java 8+)، مثل `Optional.orElse()`.
```java
default int compare(String a, String b) { ... } // مسموح
static void utility() { ... } // مسموح
```

## 4. مراجع الدوال (Method References)

اختصار لتعبيرات Lambda التي تستدعي دوالاً موجودة. الصيغة: `Class::method` أو `instance::method`.

الأنواع:
- ثابتة (Static): `Class::staticMethod`
- مثيل لنوع محدد: `Class::instanceMethod`
- مثيل لكائن تعسفي: `object::instanceMethod`
- المُنشئ (Constructor): `Class::new`

أمثلة:
```java
// Lambda: x -> System.out.println(x)
Consumer<String> printer = System.out::println;

// دالة ثابتة
Function<String, Integer> length = String::length;

// دالة مثيل
List<String> list = Arrays.asList("a", "b");
list.forEach(System.out::println); // يطبع كل عنصر

// المُنشئ
Supplier<List<String>> listSupplier = ArrayList::new;
```

## 5. Streams API

تقوم الـ Streams بمعالجة المجموعات (Collections) بشكل تصريحي: الإنشاء → التحويل → الجمع. التقييم الكسول (Lazy evaluation) (العمليات المتوسطة لا تعمل حتى العملية النهائية).

### إنشاء الـ Streams
```java
import java.util.*;
import java.util.stream.*;

List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

// من مجموعة (Collection)
Stream<String> stream = names.stream();

// من مصفوفة (Array)
String[] arr = {"x", "y"};
Stream<String> arrStream = Arrays.stream(arr);

// لا نهائي
Stream<Integer> infinite = Stream.iterate(0, n -> n + 1);
```

### العمليات المتوسطة (كسولة)
يمكن ربطها؛ لا يتم الحساب حتى العملية النهائية.
- `filter(Predicate)`: الاحتفاظ بالعناصر المطابقة.
- `map(Function)`: تحويل كل عنصر.
- `flatMap(Function<? super T, ? extends Stream<? extends R>>)`: تسطيح الـ Streams المتداخلة.
- `distinct()`, `sorted()`, `limit(n)`, `skip(n)`.

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
List<Integer> evensSquared = numbers.stream()
    .filter(n -> n % 2 == 0)
    .map(n -> n * n)
    .collect(Collectors.toList()); // [4, 16]
```

### العمليات النهائية (متعجلة)
تُطلق الحساب وتُرجع نتيجة.
- `collect(Collector)`: إلى قائمة، مجموعة، خريطة.
- `forEach(Consumer)`: تأثير جانبي (تجنبه إذا أمكن).
- `reduce()`: تجميع (مثل المجموع).
- `anyMatch()`, `allMatch()`, `findFirst()`.

```java
// Reduce: المجموع
int sum = numbers.stream().reduce(0, Integer::sum); // 15

// Collect إلى خريطة
Map<String, Integer> nameLengths = Stream.of("Alice", "Bob")
    .collect(Collectors.toMap(s -> s, String::length)); // {Alice=5, Bob=3}

// التجميع (Grouping)
Map<Integer, List<String>> byLength = names.stream()
    .collect(Collectors.groupingBy(String::length)); // {5=[Alice, Charlie], 3=[Bob]}
```

### الـ Streams المتوازية (Parallel Streams)
لتحقيق التوازي: `parallelStream()` أو `.parallel()`. استخدم بحذر (التصحيح أصعب).
```java
long count = names.parallelStream().count(); // 3
```

## 6. المجمعات (Collectors)

من `java.util.stream.Collectors`. تبني عمليات اختزال معقدة.

شائعة:
- `toList()`, `toSet()`, `toMap()`
- `joining()`: ربط السلاسل النصية.
- `summingInt()`, `averagingDouble()`
- `groupingBy()`, `partitioningBy()`
- `collectingAndThen()`: معالجة لاحقة.

```java
// مجمع مخصص للحد الأقصى حسب الطول
String longest = names.stream()
    .collect(Collectors.maxBy(Comparator.comparingInt(String::length)))
    .orElse(""); // "Charlie"

تقسيم الأعداد الزوجية والفردية
Map<Boolean, List<Integer>> partitions = numbers.stream()
    .collect(Collectors.partitioningBy(n -> n % 2 == 0));
```

## 7. Optional

يتجنب `NullPointerException` عن طريق تغليف القيم التي قد تكون null. يشجع على التعامل الصريح مع القيم الفارغة.

الإنشاء:
- `Optional.of(value)`: قيمة غير null.
- `Optional.ofNullable(value)`: null → فارغ.
- `Optional.empty()`.

العمليات:
- `isPresent()`, `ifPresent(Consumer)`
- `orElse(default)`, `orElseThrow()`
- `map()`, `flatMap()` للتسلسل.

```java
Optional<String> opt = Optional.ofNullable(getName()); // افترض أنها قد تُرجع null

String name = opt.orElse("Unknown");
opt.ifPresent(System.out::println);

String upper = opt.map(String::toUpperCase).orElse("DEFAULT");
```

غالباً ما تُرجع الـ Streams `Optional` (مثلاً، `findFirst()`).

## 8. مواضيع متقدمة

### الدوال القابلة للتركيب (Composable Functions)
`Function.andThen()`, `Function.compose()` للتسلسل.
```java
Function<String, Integer> len = String::length;
Function<Integer, String> toStr = i -> "Len: " + i;

Function<String, String> chain = len.andThen(toStr);
System.out.println(chain.apply("Java")); // Len: 4
```

### العودية (Recursion) ونداءات الذيل (Tail Calls)
تفتقر Java إلى التحسين، ولكن استخدم `Stream.iterate()` للعودية التكرارية.

### مساعدو الثبات (Immutability Helpers)
استخدم `Collections.unmodifiableList()` أو مكتبات مثل Guava/Immutable Collections (على الرغم من وجودها مدمجة منذ Java 10+ مع `List.of()`).

`List.of("a", "b")` تنشئ قوائم غير قابلة للتعديل (Java 9+).

### مطابقة الأنماط (Pattern Matching) (Java 21+ معاينة/مستقرة)
تعزز البرمجة الوظيفية مع تفكيك الهيكل (destructuring) في جمل switch.
```java
// ميزة معاينة؛ فعّلها باستخدام --enable-preview
String desc = switch (obj) {
    case Integer i -> "int: " + i;
    case String s -> "str: " + s.length();
    default -> "unknown";
};
```

### الخيوط الافتراضية (Virtual Threads) (Java 21+)
تتفوق البرمجة الوظيفية مع الخيوط خفيفة الوزن لـ Streams متزامنة.

## 9. أفضل الممارسات

- **افضل الثبات (Immutability)**: استخدم الحقول النهائية (final fields)، تجنب تعديل المجموعات.
- **تجنب التأثيرات الجانبية**: حافظ على نقاء تعبيرات Lambda؛ استخدم التأثيرات الجانبية فقط في `forEach` أو مستهلكين (consumers) صريحين.
- **الـ Streams مقابل الحلقات**: استخدم الـ Streams لقابلية القراءة؛ استخدم الحلقات للشفرة الحرجة أدائياً.
- **القيم الفارغة (Nulls)**: فضّل `Optional` على فحوصات null.
- **الاختبار (Testing)**: يمكن محاكاة الواجهات الوظيفية بسهولة باستخدام تعبيرات Lambda.
- **الأداء**: للـ Streams عبء إضافي؛ قم بتحليل الأداء قبل استخدام المتوازي.
- **قابلية القراءة**: تعبيرات Lambda القصيرة جيدة؛ استخرج دوالاً للغ المعقد.

المزالق الشائعة:
- تعديل الحالة الخارجية في تعبيرات Lambda.
- نسيان العملية النهائية (الـ Streams لا تفعل شيئاً!).
- الإفراط في استخدام الـ Streams المتوازية (ليست أسرع دائماً).

## 10. مثال: خط أنابيب وظيفي (Functional Pipeline)

معالجة قائمة من الموظفين بشكل وظيفي.

```java
import java.util.*;
import java.util.stream.Collectors;

class Employee {
    String name;
    int salary;
    Department dept;

    Employee(String name, int salary, Department dept) {
        this.name = name;
        this.salary = salary;
        this.dept = dept;
    }
}

enum Department { ENG, HR }

public class FunctionalExample {
    public static void main(String[] args) {
        List<Employee> employees = Arrays.asList(
            new Employee("Alice", 50000, Department.ENG),
            new Employee("Bob", 60000, Department.HR),
            new Employee("Charlie", 55000, Department.ENG)
        );

        // أسماء المهندسين ذوي الرواتب العالية، مرتبة
        List<String> result = employees.stream()
            .filter(e -> e.dept == Department.ENG)
            .filter(e -> e.salary > 52000)
            .map(Employee::getName)  // افترض وجود دالة getter
            .sorted()
            .collect(Collectors.toList());

        System.out.println(result); // [Charlie]
    }
}
```

## خاتمة

تقوم تعبيرات Lambda والبرمجة الوظيفية بتحويل Java من إجرائية (imperative) إلى تعبيرية (expressive). ابدأ بالبدائل البسيطة (مثل `forEach` بدلاً من الحلقات)، ثم ابني خطوط الأنابيب. تدرب على مشاريع حقيقية للإتقان. للغوص أعمق، جرب في بيئة التطوير المتكاملة (IDE).

### المراجع
- [Oracle Java Tutorials: Lambda Expressions](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html)
- [Baeldung: Java 8 Functional Interfaces](https://www.baeldung.com/java-functional-interfaces)
- [Java Streams Guide](https://www.baeldung.com/java-8-streams)
- [Effective Java (3rd Ed.) - Item 42-45 on Lambdas](https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/)