---
audio: false
generated: true
lang: ar
layout: post
title: التعبيرات اللامدا وواجهة ستريم في جافا
translated: true
type: note
---

حسنًا، لنتعلم عن Lambda Expressions و Stream API في Java. هذه ميزات قوية تم تقديمها في Java 8 تتيح أسلوب برمجة أكثر وظيفية، مما يؤدي إلى كود أكثر إيجازًا وتعبيرية.

**1. Lambda Expressions**

**ما هي Lambda Expression؟**

تعبير لامدا هو في الأساس دالة مجهولة الاسم (بدون اسم). يسمح لك بتعريف دالة مضمنة دون الإعلان صراحة عن طريقة منفصلة. تعبيرات لامدا مفيدة بشكل خاص لتمرير السلوك كبيانات، مما يجعل الكود الخاص بك أكثر مرونة وقابلية للقراءة، خاصة عند العمل مع الواجهات الوظيفية.

**بناء جملة Lambda Expression:**

يحتوي تعبير لامدا على البنية الأساسية التالية:

```java
(parameter list) -> expression body
```

* **قائمة المعاملات:** تشبه معاملات الطريقة. يمكن أن تكون فارغة، أو تحتوي على معامل واحد، أو معاملات متعددة. يمكن غالبًا استنتاج أنواع المعاملات بواسطة المترجم، لذا لا تحتاج دائمًا إلى التصريح عنها صراحة.
* **رمز السهم (`->`):** يفصل قائمة المعاملات عن جسم التعبير.
* **جسم التعبير:** هذا هو الكود الذي ينفذه تعبير لامدا. يمكن أن يكون تعبيرًا واحدًا أو كتلة من العبارات محاطة بأقواس معقوفة `{}`.

**الواجهات الوظيفية:**

تُستخدم تعبيرات لامدا في Java لتنفيذ الطرق المعرفة بواسطة **الواجهات الوظيفية**. الواجهة الوظيفية هي واجهة تحتوي **على طريقة مجردة واحدة فقط**. يمكن أن تحتوي على طرق افتراضية وطرق ثابتة، ولكن طريقة مجردة واحدة فقط.

تشمل أمثلة الواجهات الوظيفية المضمنة في Java:

* `Runnable` (طريقة مجردة واحدة: `void run()`)
* `Callable<V>` (طريقة مجردة واحدة: `V call() throws Exception`)
* `Comparator<T>` (طريقة مجردة واحدة: `int compare(T o1, T o2)`)
* `Consumer<T>` (طريقة مجردة واحدة: `void accept(T t)`)
* `Function<T, R>` (طريقة مجردة واحدة: `R apply(T t)`)
* `Predicate<T>` (طريقة مجردة واحدة: `boolean test(T t)`)
* `Supplier<T>` (طريقة مجردة واحدة: `T get()`)

**أمثلة على تعبيرات لامدا:**

لنلقِ نظرة على بعض الأمثلة لفهم كيفية عمل تعبيرات لامدا:

* **لا توجد معاملات:**

    ```java
    Runnable myRunnable = () -> System.out.println("Hello from lambda!");
    myRunnable.run(); // Output: Hello from lambda!
    ```

* **معامل واحد (يمكن حذف الأقواس):**

    ```java
    Consumer<String> printMessage = message -> System.out.println("Message: " + message);
    printMessage.accept("Lambda is cool!"); // Output: Message: Lambda is cool!
    ```

* **معاملات متعددة:**

    ```java
    java.util.Comparator<Integer> compareTwoNumbers = (a, b) -> a.compareTo(b);
    int result = compareTwoNumbers.compare(5, 10); // result will be -1
    ```

* **تعبير لامدا مع كتلة من العبارات:**

    ```java
    java.util.function.Function<Integer, String> checkEvenOdd = number -> {
        if (number % 2 == 0) {
            return "Even";
        } else {
            return "Odd";
        }
    };
    String output = checkEvenOdd.apply(7); // output will be "Odd"
    ```

**مراجع الطرق:**

مراجع الطرق هي بناء جملة مختصر لتعبيرات لامدا التي تستدعي ببساطة طريقة موجودة. إنها تجعل الكود الخاص بك أكثر إيجازًا. هناك أربعة أنواع من مراجع الطرق:

1.  **المرجع إلى طريقة ثابتة:** `ClassName::staticMethodName`

    ```java
    java.util.function.Function<String, Integer> stringToInt = Integer::parseInt;
    int number = stringToInt.apply("123"); // number will be 123
    ```

2.  **المرجع إلى طريقة مثيل لكائن معين:** `instance::instanceMethodName`

    ```java
    String message = "Hello";
    java.util.function.Consumer<String> printContains = s -> message.contains(s);
    printContains.accept("ll"); // This will execute message.contains("ll")
    ```
    للمقارنة، مع `Supplier`:

    ```java
    String message = "Hello";
    java.util.function.Supplier<Integer> getLength = message::length;
    int len = getLength.get(); // len will be 5
    ```

3.  **المرجع إلى طريقة مثيل لكائن عشوائي من نوع معين:** `ClassName::instanceMethodName`

    ```java
    java.util.function.BiPredicate<String, String> checkStartsWith = String::startsWith;
    boolean starts = checkStartsWith.test("Java", "Ja"); // starts will be true
    ```

4.  **المرجع إلى مُنشئ:** `ClassName::new`

    ```java
    java.util.function.Supplier<String> createString = String::new;
    String emptyString = createString.get(); // emptyString will be ""

    java.util.function.Function<Integer, int[]> createIntArray = int[]::new;
    int[] myArray = createIntArray.apply(5); // myArray will be an int array of size 5
    ```

**2. Stream API**

**ما هو Stream API؟**

يوفر Stream API، الذي تم تقديمه في Java 8، طريقة قوية وأنيقة لمعالجة مجموعات البيانات. يمثل الدفق تسلسلاً من العناصر التي تدعم عمليات تجميعية متنوعة. تختلف التيارات عن المجموعات؛ المجموعات تتعلق بتخزين البيانات، بينما التيارات تتعلق بمعالجة البيانات.

**المفاهيم الأساسية لـ Stream API:**

* **Stream:** تسلسل من العناصر يدعم العمليات التجميعية التسلسلية والمتوازية.
* **المصدر:** أصل الدفق (مثل مجموعة، مصفوفة، قناة إدخال/إخراج).
* **عمليات وسيطة:** عمليات تحول أو ترشح الدفق وتُرجع دفقًا جديدًا. هذه العمليات كسولة، بمعنى أنها لا تُنفذ حتى يتم استدعاء عملية نهائية.
* **عمليات نهائية:** عمليات تنتج نتيجة أو تأثيرًا جانبيًا وتستهلك الدفق (لا يمكن استخدام الدفق بعد عملية نهائية).

**إنشاء التيارات:**

يمكنك إنشاء التيارات بطرق مختلفة:

* **من مجموعة:**

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob", "Charlie");
    java.util.stream.Stream<String> sequentialStream = names.stream();
    java.util.stream.Stream<String> parallelStream = names.parallelStream();
    ```

* **من مصفوفة:**

    ```java
    int[] numbers = {1, 2, 3, 4, 5};
    java.util.stream.IntStream intStream = java.util.Arrays.stream(numbers);
    ```

* **باستخدام `Stream.of()`:**

    ```java
    java.util.stream.Stream<String> stringStream = java.util.stream.Stream.of("apple", "banana", "cherry");
    ```

* **باستخدام `Stream.iterate()`:** (ينشئ دفقًا مرتبًا تسلسليًا لا نهائي)

    ```java
    java.util.stream.Stream<Integer> evenNumbers = java.util.stream.Stream.iterate(0, n -> n + 2).limit(5); // 0, 2, 4, 6, 8
    ```

* **باستخدام `Stream.generate()`:** (ينشئ دفقًا غير مرتب تسلسليًا لا نهائي)

    ```java
    java.util.stream.Stream<Double> randomNumbers = java.util.stream.Stream.generate(Math::random).limit(3);
    ```

**العمليات الوسيطة:**

تقوم هذه العمليات بتحويل أو ترشيح الدفق وتُرجع دفقًا جديدًا. تشمل العمليات الوسيطة الشائعة:

* **`filter(Predicate<T> predicate)`:** يُرجع دفقًا يتكون من العناصر التي تطابق المسند المحدد.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(1, 2, 3, 4, 5, 6);
    java.util.stream.Stream<Integer> evenNumbersStream = numbers.stream().filter(n -> n % 2 == 0); // 2, 4, 6
    ```

* **`map(Function<T, R> mapper)`:** يُرجع دفقًا يتكون من نتائج تطبيق الدالة المعطاة على عناصر هذا الدفق.

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob", "Charlie");
    java.util.stream.Stream<Integer> nameLengths = names.stream().map(String::length); // 5, 3, 7
    ```

* **`flatMap(Function<T, Stream<R>> mapper)`:** يُرجع دفقًا يتكون من نتائج استبدال كل عنصر من هذا الدفق بمحتويات دفق مُعيّن تم إنتاجه بتطبيق دالة التعيين المقدمة على كل عنصر. مفيد لتسطيح المجموعات المتداخلة.

    ```java
    java.util.List<java.util.List<Integer>> listOfLists = java.util.Arrays.asList(
            java.util.Arrays.asList(1, 2),
            java.util.Arrays.asList(3, 4, 5)
    );
    java.util.stream.Stream<Integer> singleStream = listOfLists.stream().flatMap(java.util.List::stream); // 1, 2, 3, 4, 5
    ```

* **`sorted()`:** يُرجع دفقًا يتكون من عناصر هذا الدفق، مرتبة وفقًا للترتيب الطبيعي.

    ```java
    java.util.List<String> fruits = java.util.Arrays.asList("banana", "apple", "cherry");
    java.util.stream.Stream<String> sortedFruits = fruits.stream().sorted(); // apple, banana, cherry
    ```

* **`distinct()`:** يُرجع دفقًا يتكون من العناصر المميزة (وفقًا لـ `equals()`) لهذا الدفق.

    ```java
    java.util.List<Integer> numbersWithDuplicates = java.util.Arrays.asList(1, 2, 2, 3, 3, 3);
    java.util.stream.Stream<Integer> distinctNumbers = numbersWithDuplicates.stream().distinct(); // 1, 2, 3
    ```

* **`peek(Consumer<T> action)`:** يُرجع دفقًا يتكون من عناصر هذا الدفق، مع أداء الإجراء المقدم على كل عنصر بشكل إضافي أثناء استهلاك العناصر من الدفق الناتج. بشكل أساسي لأغراض التصحيح أو التأثيرات الجانبية.

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob");
    java.util.stream.Stream<String> peekedNames = names.stream().peek(name -> System.out.println("Processing: " + name));
    peekedNames.forEach(System.out::println);
    // Output:
    // Processing: Alice
    // Alice
    // Processing: Bob
    // Bob
    ```

* **`limit(long maxSize)`:** يُرجع دفقًا يتكون من عناصر هذا الدفق، مقتصرًا على ألا يزيد طوله عن `maxSize`.

    ```java
    java.util.stream.Stream<Integer> firstThree = java.util.stream.Stream.iterate(1, n -> n + 1).limit(3); // 1, 2, 3
    ```

* **`skip(long n)`:** يُرجع دفقًا يتكون من العناصر المتبقية من هذا الدفق بعد التخلص من العناصر `n` الأولى.

    ```java
    java.util.stream.Stream<Integer> afterSkipping = java.util.stream.Stream.iterate(1, n -> n + 1).skip(2).limit(3); // 3, 4, 5
    ```

**العمليات النهائية:**

تنتج هذه العمليات نتيجة أو تأثيرًا جانبيًا وتستهلك الدفق. تشمل العمليات النهائية الشائعة:

* **`forEach(Consumer<T> action)`:** ينفذ إجراء لكل عنصر من عناصر هذا الدفق.

    ```java
    java.util.List<String> colors = java.util.Arrays.asList("red", "green", "blue");
    colors.stream().forEach(System.out::println);
    ```

* **`count()`:** يُرجع عدد العناصر في هذا الدفق.

    ```java
    long numberOfFruits = java.util.Arrays.asList("apple", "banana", "cherry").stream().count(); // 3
    ```

* **`collect(Collector<T, A, R> collector)`:** ينفذ عملية اختزال قابلة للتغيير على عناصر هذا الدفق باستخدام `Collector`. تشمل جامعي التجميع الشائعين `toList()`, `toSet()`, `toMap()`, `joining()`, `groupingBy()`, `summarizingInt()`, إلخ.

    ```java
    java.util.List<String> fruits = java.util.Arrays.asList("apple", "banana", "cherry");
    java.util.List<String> fruitList = fruits.stream().collect(java.util.stream.Collectors.toList());
    java.util.Set<String> fruitSet = fruits.stream().collect(java.util.stream.Collectors.toSet());
    String joinedFruits = fruits.stream().collect(java.util.stream.Collectors.joining(", ")); // "apple, banana, cherry"
    ```

* **`reduce(T identity, BinaryOperator<T> accumulator)`:** ينفذ عملية اختزال على عناصر هذا الدفق، باستخدام قيمة الهوية المقدمة ودالة تراكم ترابطية.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(1, 2, 3, 4);
    int sum = numbers.stream().reduce(0, (a, b) -> a + b); // sum will be 10
    ```

* **`min(Comparator<T> comparator)`:** يُرجع `Optional` يصف الحد الأدنى لعنصر هذا الدفق وفقًا للمقارن المقدم.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(3, 1, 4, 1, 5, 9);
    java.util.Optional<Integer> minNumber = numbers.stream().min(Integer::compareTo); // Optional[1]
    ```

* **`max(Comparator<T> comparator)`:** يُرجع `Optional` يصف الحد الأقصى لعنصر هذا الدفق وفقًا للمقارن المقدم.

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(3, 1, 4, 1, 5, 9);
    java.util.Optional<Integer> maxNumber = numbers.stream().max(Integer::compareTo); // Optional[9]
    ```

* **`findFirst()`:** يُرجع `Optional` يصف العنصر الأول من هذا الدفق.

    ```java
    java.util.Optional<String> firstFruit = java.util.Arrays.asList("apple", "banana", "cherry").stream().findFirst(); // Optional[apple]
    ```

* **`findAny()`:** يُرجع `Optional` يصف بعض عناصر الدفق. قد لا تُرجع هذه العملية دائمًا نفس النتيجة عندما يكون الدفق متوازيًا.

    ```java
    java.util.Optional<String> anyFruit = java.util.Arrays.asList("apple", "banana", "cherry").stream().findAny(); // Might return Optional[apple], Optional[banana], or Optional[cherry]
    ```

* **`anyMatch(Predicate<T> predicate)`:** يُرجع ما إذا كان أي عنصر من هذا الدفق يطابق المسند المقدم.

    ```java
    boolean hasEven = java.util.Arrays.asList(1, 3, 5, 2, 7).stream().anyMatch(n -> n % 2 == 0); // true
    ```

* **`allMatch(Predicate<T> predicate)`:** يُرجع ما إذا كانت جميع عناصر هذا الدفق تطابق المسند المقدم.

    ```java
    boolean allPositive = java.util.Arrays.asList(2, 4, 6, 8).stream().allMatch(n -> n > 0); // true
    ```

* **`noneMatch(Predicate<T> predicate)`:** يُرجع ما إذا لم يكن أي عنصر من عناصر هذا الدفق يطابق المسند المقدم.

    ```java
    boolean noNegatives = java.util.Arrays.asList(1, 2, 3, 4).stream().noneMatch(n -> n < 0); // true
    ```

**3. العلاقة بين Lambdas و Streams**

تُستخدم تعبيرات لامدا بشكل كبير مع Stream API. فهي توفر طريقة موجزة لتعريف السلوك للعديد من العمليات الوسيطة والنهائية. على سبيل المثال، غالبًا ما يتم تنفيذ `Predicate` في `filter()`، و `Function` في `map()`، و `Consumer` في `forEach()` باستخدام تعبيرات لامدا.

**أمثلة تجمع بين Lambdas و Streams:**

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class LambdaStreamExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Eve");

        // ترشيح الأسماء التي تبدأ بـ 'A' وتحويلها إلى أحرف كبيرة
        List<String> aNamesUppercase = names.stream()
                .filter(name -> name.startsWith("A")) // Lambda للترشيح
                .map(String::toUpperCase)             // Method reference للتحويل
                .collect(Collectors.toList());

        System.out.println("Names starting with 'A' in uppercase: " + aNamesUppercase);
        // Output: Names starting with 'A' in uppercase: [ALICE]

        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // إيجاد مجموع مربعات الأعداد الزوجية
        int sumOfSquaresOfEvens = numbers.stream()
                .filter(n -> n % 2 == 0)       // Lambda لترشيح الأعداد الزوجية
                .map(n -> n * n)              // Lambda للتربيع
                .reduce(0, Integer::sum);     // Method reference للجمع

        System.out.println("Sum of squares of even numbers: " + sumOfSquaresOfEvens);
        // Output: Sum of squares of even numbers: 220

        List<Person> people = Arrays.asList(
                new Person("Alice", 30),
                new Person("Bob", 25),
                new Person("Charlie", 35)
        );

        // الحصول على قائمة بأسماء الأشخاص الأكبر من 28 سنة
        List<String> olderPeopleNames = people.stream()
                .filter(person -> person.getAge() > 28) // Lambda للترشيح
                .map(Person::getName)                 // Method reference للحصول على الاسم
                .collect(Collectors.toList());

        System.out.println("Names of people older than 28: " + olderPeopleNames);
        // Output: Names of people older than 28: [Alice, Charlie]
    }
}

class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}
```

**4. التيارات المتوازية**

يدعم Stream API أيضًا المعالجة المتوازية. يمكنك بسهولة معالجة عناصر الدفق بشكل متوازٍ باستخدام طريقة `parallelStream()` على مجموعة أو عن طريق استدعاء طريقة `parallel()` على دفق تسلسلي. يمكن أن يحسن هذا الأداء بشكل كبير لعمليات معينة على مجموعات البيانات الكبيرة.

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// حساب مجموع المربعات بشكل متوازٍ
int sumOfSquaresParallel = numbers.parallelStream()
        .map(n -> n * n)
        .reduce(0, Integer::sum);

System.out.println("Sum of squares (parallel): " + sumOfSquaresParallel);
```

**الخلاصة**

تعبيرات لامدا و Stream API هما إضافتان قويتان إلى Java تتيحان طريقة أكثر وظيفية وإيجازًا لكتابة الكود، خاصة عند التعامل مع مجموعات البيانات. باستخدام تعبيرات لامدا مع التيارات، يمكنك تنفيذ عمليات معالجة بيانات معقدة بطريقة تصريحية وقابلة للقراءة. فهم هذه الميزات ضروري لتطوير Java الحديث. تذكر التدرب على استخدامها لتصبح أكثر راحة وإتقانًا.