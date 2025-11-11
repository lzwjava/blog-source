---
audio: false
generated: true
lang: hi
layout: post
title: जावा में लैम्ब्डा एक्सप्रेशन और स्ट्रीम एपीआई
translated: true
type: note
---

ठीक है, आइए Java में Lambda Expressions और Stream API के बारे में सीखते हैं। ये Java 8 में पेश किए गए शक्तिशाली फीचर्स हैं जो एक अधिक functional programming शैली को सक्षम करते हैं, जिससे कोड अधिक संक्षिप्त और अभिव्यंजक बनता है।

**1. Lambda Expressions**

**Lambda Expression क्या है?**

एक lambda expression अनिवार्य रूप से एक अनाम (unnamed) फंक्शन है। यह आपको बिना अलग से method घोषित किए, इनलाइन एक फंक्शन को परिभाषित करने की अनुमति देता है। Lambda expressions विशेष रूप से behavior को data के रूप में पास करने के लिए उपयोगी हैं, जो आपके कोड को अधिक लचीला और पठनीय बनाता है, खासकर functional interfaces के साथ काम करते समय।

**Lambda Expression का सिंटैक्स:**

एक lambda expression का मूल सिंटैक्स निम्नलिखित है:

```java
(parameter list) -> expression body
```

* **Parameter List:** यह एक method के parameters के समान है। यह खाली हो सकता है, एक parameter रख सकता है, या multiple parameters रख सकता है। Parameters के प्रकार अक्सर compiler द्वारा अनुमानित किए जा सकते हैं, इसलिए आपको हमेशा उन्हें स्पष्ट रूप से घोषित करने की आवश्यकता नहीं होती है।
* **Arrow Token (`->`):** यह parameter list को expression body से अलग करता है।
* **Expression Body:** यह वह कोड है जिसे lambda expression execute करता है। यह एक single expression या curly braces `{}` में संलग्न statements का एक ब्लॉक हो सकता है।

**Functional Interfaces:**

Java में lambda expressions का उपयोग **functional interfaces** द्वारा परिभाषित methods को implement करने के लिए किया जाता है। एक functional interface एक ऐसा interface है जिसमें **केवल एक abstract method** होता है। इसमें default methods और static methods हो सकते हैं, लेकिन केवल एक abstract method।

Java में built-in functional interfaces के उदाहरणों में शामिल हैं:

* `Runnable` (single abstract method: `void run()`)
* `Callable<V>` (single abstract method: `V call() throws Exception`)
* `Comparator<T>` (single abstract method: `int compare(T o1, T o2)`)
* `Consumer<T>` (single abstract method: `void accept(T t)`)
* `Function<T, R>` (single abstract method: `R apply(T t)`)
* `Predicate<T>` (single abstract method: `boolean test(T t)`)
* `Supplier<T>` (single abstract method: `T get()`)

**Lambda Expressions के उदाहरण:**

आइए कुछ उदाहरण देखें ताकि समझ सकें कि lambda expressions कैसे काम करते हैं:

* **कोई parameter नहीं:**

    ```java
    Runnable myRunnable = () -> System.out.println("Hello from lambda!");
    myRunnable.run(); // Output: Hello from lambda!
    ```

* **एक parameter (parentheses छोड़े जा सकते हैं):**

    ```java
    Consumer<String> printMessage = message -> System.out.println("Message: " + message);
    printMessage.accept("Lambda is cool!"); // Output: Message: Lambda is cool!
    ```

* **Multiple parameters:**

    ```java
    java.util.Comparator<Integer> compareTwoNumbers = (a, b) -> a.compareTo(b);
    int result = compareTwoNumbers.compare(5, 10); // result will be -1
    ```

* **Statements के एक ब्लॉक के साथ Lambda expression:**

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

**Method References:**

Method references, lambda expressions के लिए एक शॉर्टहैंड सिंटैक्स हैं जो केवल एक मौजूदा method को call करते हैं। ये आपके कोड को और भी अधिक संक्षिप्त बनाते हैं। Method references चार प्रकार के होते हैं:

1.  **Reference to a static method:** `ClassName::staticMethodName`

    ```java
    java.util.function.Function<String, Integer> stringToInt = Integer::parseInt;
    int number = stringToInt.apply("123"); // number will be 123
    ```

2.  **Reference to an instance method of a particular object:** `instance::instanceMethodName`

    ```java
    String message = "Hello";
    java.util.function.Consumer<String> printLength = message::length; // Incorrect - Consumer takes one arg
    java.util.function.Supplier<Integer> getLength = message::length;
    int len = getLength.get(); // len will be 5
    ```
    **Correction:** `Consumer` उदाहरण को एक argument लेना चाहिए। यहाँ एक बेहतर उदाहरण है:

    ```java
    String message = "Hello";
    java.util.function.Consumer<String> printContains = s -> message.contains(s);
    printContains.accept("ll"); // This will execute message.contains("ll")
    ```
    एक `Supplier` के लिए, यह अधिक इस तरह है:

    ```java
    String message = "Hello";
    java.util.function.Supplier<Integer> getLength = message::length;
    int len = getLength.get(); // len will be 5
    ```

3.  **Reference to an instance method of an arbitrary object of a particular type:** `ClassName::instanceMethodName`

    ```java
    java.util.function.BiPredicate<String, String> checkStartsWith = String::startsWith;
    boolean starts = checkStartsWith.test("Java", "Ja"); // starts will be true
    ```

4.  **Reference to a constructor:** `ClassName::new`

    ```java
    java.util.function.Supplier<String> createString = String::new;
    String emptyString = createString.get(); // emptyString will be ""

    java.util.function.Function<Integer, int[]> createIntArray = int[]::new;
    int[] myArray = createIntArray.apply(5); // myArray will be an int array of size 5
    ```

**2. Stream API**

**Stream API क्या है?**

Stream API, Java 8 में पेश की गई, डेटा के collections को प्रोसेस करने का एक शक्तिशाली और सुरुचिपूर्ण तरीका प्रदान करती है। एक stream तत्वों के एक sequence का प्रतिनिधित्व करता है जो विभिन्न aggregate operations का समर्थन करता है। Streams, collections से अलग हैं; collections डेटा को स्टोर करने के बारे में हैं, जबकि streams डेटा को प्रोसेस करने के बारे में हैं।

**Stream API की मुख्य अवधारणाएँ:**

* **Stream:** तत्वों का एक sequence जो sequential और parallel aggregate operations का समर्थन करता है।
* **Source:** Stream का स्रोत (जैसे, एक collection, एक array, एक I/O channel)।
* **Intermediate Operations:** ऐसे operations जो stream को transform या filter करते हैं और एक नया stream return करते हैं। ये operations lazy होते हैं, मतलब कि इन्हें तब तक execute नहीं किया जाता जब तक कि एक terminal operation invoke नहीं किया जाता।
* **Terminal Operations:** ऐसे operations जो एक result या side effect उत्पन्न करते हैं और stream को consume करते हैं (terminal operation के बाद stream अब usable नहीं होता)।

**Streams बनाना:**

आप विभिन्न तरीकों से streams बना सकते हैं:

* **एक Collection से:**

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob", "Charlie");
    java.util.stream.Stream<String> sequentialStream = names.stream();
    java.util.stream.Stream<String> parallelStream = names.parallelStream();
    ```

* **एक Array से:**

    ```java
    int[] numbers = {1, 2, 3, 4, 5};
    java.util.stream.IntStream intStream = java.util.Arrays.stream(numbers);
    ```

* **`Stream.of()` का उपयोग करके:**

    ```java
    java.util.stream.Stream<String> stringStream = java.util.stream.Stream.of("apple", "banana", "cherry");
    ```

* **`Stream.iterate()` का उपयोग करके:** (एक infinite sequential ordered stream बनाता है)

    ```java
    java.util.stream.Stream<Integer> evenNumbers = java.util.stream.Stream.iterate(0, n -> n + 2).limit(5); // 0, 2, 4, 6, 8
    ```

* **`Stream.generate()` का उपयोग करके:** (एक infinite sequential unordered stream बनाता है)

    ```java
    java.util.stream.Stream<Double> randomNumbers = java.util.stream.Stream.generate(Math::random).limit(3);
    ```

**Intermediate Operations:**

ये operations stream को transform या filter करते हैं और एक नया stream return करते हैं। सामान्य intermediate operations में शामिल हैं:

* **`filter(Predicate<T> predicate)`:** दिए गए predicate से मेल खाने वाले तत्वों से युक्त एक stream return करता है।

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(1, 2, 3, 4, 5, 6);
    java.util.stream.Stream<Integer> evenNumbersStream = numbers.stream().filter(n -> n % 2 == 0); // 2, 4, 6
    ```

* **`map(Function<T, R> mapper)`:** इस stream के तत्वों पर दिए गए function को apply करने के results से युक्त एक stream return करता है।

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob", "Charlie");
    java.util.stream.Stream<Integer> nameLengths = names.stream().map(String::length); // 5, 3, 7
    ```

* **`flatMap(Function<T, Stream<R>> mapper)`:** इस stream के प्रत्येक तत्व को प्रदान mapping function को apply करके उत्पादित mapped stream की सामग्री से replace करने के results से युक्त एक stream return करता है। Nested collections को flatten करने के लिए उपयोगी।

    ```java
    java.util.List<java.util.List<Integer>> listOfLists = java.util.Arrays.asList(
            java.util.Arrays.asList(1, 2),
            java.util.Arrays.asList(3, 4, 5)
    );
    java.util.stream.Stream<Integer> singleStream = listOfLists.stream().flatMap(java.util.List::stream); // 1, 2, 3, 4, 5
    ```

* **`sorted()`:** इस stream के तत्वों से युक्त एक stream return करता है, जो natural order के अनुसार sorted होते हैं।

    ```java
    java.util.List<String> fruits = java.util.Arrays.asList("banana", "apple", "cherry");
    java.util.stream.Stream<String> sortedFruits = fruits.stream().sorted(); // apple, banana, cherry
    ```

* **`distinct()`:** इस stream के distinct तत्वों (`equals()` के अनुसार) से युक्त एक stream return करता है।

    ```java
    java.util.List<Integer> numbersWithDuplicates = java.util.Arrays.asList(1, 2, 2, 3, 3, 3);
    java.util.stream.Stream<Integer> distinctNumbers = numbersWithDuplicates.stream().distinct(); // 1, 2, 3
    ```

* **`peek(Consumer<T> action)`:** इस stream के तत्वों से युक्त एक stream return करता है, जो resulting stream से elements के consumed होने पर प्रत्येक element पर प्रदान action को अतिरिक्त रूप से perform करता है। मुख्य रूप से debugging या side effects के लिए।

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

* **`limit(long maxSize)`:** इस stream के तत्वों से युक्त एक stream return करता है, जिसकी लंबाई `maxSize` से अधिक नहीं होती।

    ```java
    java.util.stream.Stream<Integer> firstThree = java.util.stream.Stream.iterate(1, n -> n + 1).limit(3); // 1, 2, 3
    ```

* **`skip(long n)`:** पहले `n` तत्वों को discard करने के बाद इस stream के शेष तत्वों से युक्त एक stream return करता है।

    ```java
    java.util.stream.Stream<Integer> afterSkipping = java.util.stream.Stream.iterate(1, n -> n + 1).skip(2).limit(3); // 3, 4, 5
    ```

**Terminal Operations:**

ये operations एक result या side effect उत्पन्न करते हैं और stream को consume करते हैं। सामान्य terminal operations में शामिल हैं:

* **`forEach(Consumer<T> action)`:** इस stream के प्रत्येक element के लिए एक action perform करता है।

    ```java
    java.util.List<String> colors = java.util.Arrays.asList("red", "green", "blue");
    colors.stream().forEach(System.out::println);
    ```

* **`count()`:** इस stream में तत्वों की count return करता है।

    ```java
    long numberOfFruits = java.util.Arrays.asList("apple", "banana", "cherry").stream().count(); // 3
    ```

* **`collect(Collector<T, A, R> collector)`:** एक `Collector` का उपयोग करके इस stream के तत्वों पर एक mutable reduction operation perform करता है। सामान्य collectors में `toList()`, `toSet()`, `toMap()`, `joining()`, `groupingBy()`, `summarizingInt()`, आदि शामिल हैं।

    ```java
    java.util.List<String> fruits = java.util.Arrays.asList("apple", "banana", "cherry");
    java.util.List<String> fruitList = fruits.stream().collect(java.util.stream.Collectors.toList());
    java.util.Set<String> fruitSet = fruits.stream().collect(java.util.stream.Collectors.toSet());
    String joinedFruits = fruits.stream().collect(java.util.stream.Collectors.joining(", ")); // "apple, banana, cherry"
    ```

* **`reduce(T identity, BinaryOperator<T> accumulator)`:** प्रदान identity value और एक associative accumulation function का उपयोग करके, इस stream के तत्वों पर एक reduction perform करता है।

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(1, 2, 3, 4);
    int sum = numbers.stream().reduce(0, (a, b) -> a + b); // sum will be 10
    ```

* **`min(Comparator<T> comparator)`:** प्रदान comparator के अनुसार इस stream के न्यूनतम तत्व का वर्णन करते हुए एक `Optional` return करता है।

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(3, 1, 4, 1, 5, 9);
    java.util.Optional<Integer> minNumber = numbers.stream().min(Integer::compareTo); // Optional[1]
    ```

* **`max(Comparator<T> comparator)`:** प्रदान comparator के अनुसार इस stream के अधिकतम तत्व का वर्णन करते हुए एक `Optional` return करता है।

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(3, 1, 4, 1, 5, 9);
    java.util.Optional<Integer> maxNumber = numbers.stream().max(Integer::compareTo); // Optional[9]
    ```

* **`findFirst()`:** इस stream के पहले तत्व का वर्णन करते हुए एक `Optional` return करता है।

    ```java
    java.util.Optional<String> firstFruit = java.util.Arrays.asList("apple", "banana", "cherry").stream().findFirst(); // Optional[apple]
    ```

* **`findAny()`:** इस stream के किसी तत्व का वर्णन करते हुए एक `Optional` return करता है। यह operation हमेशा एक ही result return नहीं कर सकता है जब stream parallel हो।

    ```java
    java.util.Optional<String> anyFruit = java.util.Arrays.asList("apple", "banana", "cherry").stream().findAny(); // Might return Optional[apple], Optional[banana], or Optional[cherry]
    ```

* **`anyMatch(Predicate<T> predicate)`:** return करता है कि क्या इस stream का कोई तत्व प्रदान predicate से मेल खाता है।

    ```java
    boolean hasEven = java.util.Arrays.asList(1, 3, 5, 2, 7).stream().anyMatch(n -> n % 2 == 0); // true
    ```

* **`allMatch(Predicate<T> predicate)`:** return करता है कि क्या इस stream के सभी तत्व प्रदान predicate से मेल खाते हैं।

    ```java
    boolean allPositive = java.util.Arrays.asList(2, 4, 6, 8).stream().allMatch(n -> n > 0); // true
    ```

* **`noneMatch(Predicate<T> predicate)`:** return करता है कि क्या इस stream का कोई भी तत्व प्रदान predicate से मेल नहीं खाता है।

    ```java
    boolean noNegatives = java.util.Arrays.asList(1, 2, 3, 4).stream().noneMatch(n -> n < 0); // true
    ```

**3. Lambdas और Streams के बीच संबंध**

Lambda expressions का भारी उपयोग Stream API के साथ किया जाता है। वे कई intermediate और terminal operations के लिए behavior को परिभाषित करने का एक संक्षिप्त तरीका प्रदान करते हैं। उदाहरण के लिए, `filter()` में `Predicate`, `map()` में `Function`, और `forEach()` में `Consumer` अक्सर lambda expressions का उपयोग करके implement किए जाते हैं।

**Lambdas और Streams को जोड़ने वाले उदाहरण:**

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class LambdaStreamExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Eve");

        // Filter names starting with 'A' and convert them to uppercase
        List<String> aNamesUppercase = names.stream()
                .filter(name -> name.startsWith("A")) // Filtering के लिए Lambda
                .map(String::toUpperCase)             // Mapping के लिए Method reference
                .collect(Collectors.toList());

        System.out.println("Names starting with 'A' in uppercase: " + aNamesUppercase);
        // Output: Names starting with 'A' in uppercase: [ALICE]

        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // Find the sum of squares of even numbers
        int sumOfSquaresOfEvens = numbers.stream()
                .filter(n -> n % 2 == 0)       // Even numbers को filter करने के लिए Lambda
                .map(n -> n * n)              // Squaring के लिए Lambda
                .reduce(0, Integer::sum);     // Summing के लिए Method reference

        System.out.println("Sum of squares of even numbers: " + sumOfSquaresOfEvens);
        // Output: Sum of squares of even numbers: 220

        List<Person> people = Arrays.asList(
                new Person("Alice", 30),
                new Person("Bob", 25),
                new Person("Charlie", 35)
        );

        // Get a list of names of people older than 28
        List<String> olderPeopleNames = people.stream()
                .filter(person -> person.getAge() > 28) // Filtering के लिए Lambda
                .map(Person::getName)                 // Name प्राप्त करने के लिए Method reference
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

**4. Parallel Streams**

Stream API parallel processing का भी समर्थन करती है। आप किसी collection पर `parallelStream()` method का उपयोग करके या किसी sequential stream पर `parallel()` method को call करके आसानी से किसी stream के तत्वों को parallel में process कर सकते हैं। यह बड़े datasets पर certain operations के लिए performance में काफी सुधार कर सकता है।

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// Calculate the sum of squares in parallel
int sumOfSquaresParallel = numbers.parallelStream()
        .map(n -> n * n)
        .reduce(0, Integer::sum);

System.out.println("Sum of squares (parallel): " + sumOfSquaresParallel);
```

**निष्कर्ष**

Lambda expressions और Stream API Java में शक्तिशाली जोड़ हैं जो कोड लिखने के एक अधिक functional और संक्षिप्त तरीके को सक्षम करते हैं, खासकर जब डेटा के collections से निपटना हो। Streams के साथ lambdas का उपयोग करके, आप जटिल डेटा प्रोसेसिंग operations को एक declarative और पठनीय तरीके से perform कर सकते हैं। इन features को समझना आधुनिक Java development के लिए आवश्यक है। इनका अभ्यास करना याद रखें ताकि आप अधिक सहज और कुशल बन सकें।