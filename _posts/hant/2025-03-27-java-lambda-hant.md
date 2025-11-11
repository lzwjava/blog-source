---
audio: false
generated: true
lang: hant
layout: post
title: Java 中的 Lambda 表達式與串流 API
translated: true
type: note
---

好的，讓我們來學習 Java 中的 Lambda 表達式與 Stream API。這些是 Java 8 引入的強大功能，支援更函數式的程式設計風格，讓程式碼更簡潔且具表達力。

**1. Lambda 表達式**

**什麼是 Lambda 表達式？**

Lambda 表達式本質上是一個匿名（未命名）函數。它允許你直接定義一個函數，而無需明確宣告一個獨立的方法。Lambda 表達式在將行為作為資料傳遞時特別有用，尤其是在使用函數式介面時，能讓你的程式碼更靈活且易讀。

**Lambda 表達式的語法：**

Lambda 表達式的基本語法如下：

```java
(參數列表) -> 表達式主體
```

*   **參數列表：** 類似於方法的參數。可以是空的、包含一個參數或多個參數。參數的型別通常可由編譯器推斷，因此你不需要總是明確宣告它們。
*   **箭頭符號 (`->`):** 用於分隔參數列表和表達式主體。
*   **表達式主體：** 這是 Lambda 表達式執行的程式碼。它可以是一個單一表達式，或是用大括號 `{}` 包圍的陳述式區塊。

**函數式介面：**

Java 中的 Lambda 表達式用於實作 **函數式介面** 所定義的方法。一個函數式介面是只包含 **一個抽象方法** 的介面。它可以有預設方法和靜態方法，但只能有一個抽象方法。

Java 內建的函數式介面範例包括：

*   `Runnable` (單一抽象方法：`void run()`)
*   `Callable<V>` (單一抽象方法：`V call() throws Exception`)
*   `Comparator<T>` (單一抽象方法：`int compare(T o1, T o2)`)
*   `Consumer<T>` (單一抽象方法：`void accept(T t)`)
*   `Function<T, R>` (單一抽象方法：`R apply(T t)`)
*   `Predicate<T>` (單一抽象方法：`boolean test(T t)`)
*   `Supplier<T>` (單一抽象方法：`T get()`)

**Lambda 表達式範例：**

讓我們看一些範例來理解 Lambda 表達式如何運作：

*   **沒有參數：**

    ```java
    Runnable myRunnable = () -> System.out.println("Hello from lambda!");
    myRunnable.run(); // 輸出： Hello from lambda!
    ```

*   **一個參數（括號可以省略）：**

    ```java
    Consumer<String> printMessage = message -> System.out.println("Message: " + message);
    printMessage.accept("Lambda is cool!"); // 輸出： Message: Lambda is cool!
    ```

*   **多個參數：**

    ```java
    java.util.Comparator<Integer> compareTwoNumbers = (a, b) -> a.compareTo(b);
    int result = compareTwoNumbers.compare(5, 10); // result 將會是 -1
    ```

*   **包含陳述式區塊的 Lambda 表達式：**

    ```java
    java.util.function.Function<Integer, String> checkEvenOdd = number -> {
        if (number % 2 == 0) {
            return "Even";
        } else {
            return "Odd";
        }
    };
    String output = checkEvenOdd.apply(7); // output 將會是 "Odd"
    ```

**方法參考：**

方法參考是 Lambda 表達式的一種簡寫語法，僅用於呼叫現有的方法。它們讓你的程式碼更加簡潔。方法參考有四種：

1.  **參考至靜態方法：** `ClassName::staticMethodName`

    ```java
    java.util.function.Function<String, Integer> stringToInt = Integer::parseInt;
    int number = stringToInt.apply("123"); // number 將會是 123
    ```

2.  **參考至特定物件的實例方法：** `instance::instanceMethodName`

    ```java
    String message = "Hello";
    java.util.function.Consumer<String> printLength = message::length; // 不正確 - Consumer 接受一個參數
    java.util.function.Supplier<Integer> getLength = message::length;
    int len = getLength.get(); // len 將會是 5
    ```
    **修正：** `Consumer` 的範例應該接受一個參數。這裡提供一個更好的範例：

    ```java
    String message = "Hello";
    java.util.function.Consumer<String> printContains = s -> message.contains(s);
    printContains.accept("ll"); // 這將執行 message.contains("ll")
    ```
    對於 `Supplier`，它更像是：

    ```java
    String message = "Hello";
    java.util.function.Supplier<Integer> getLength = message::length;
    int len = getLength.get(); // len 將會是 5
    ```

3.  **參考至特定型別的任意物件的實例方法：** `ClassName::instanceMethodName`

    ```java
    java.util.function.BiPredicate<String, String> checkStartsWith = String::startsWith;
    boolean starts = checkStartsWith.test("Java", "Ja"); // starts 將會是 true
    ```

4.  **參考至建構子：** `ClassName::new`

    ```java
    java.util.function.Supplier<String> createString = String::new;
    String emptyString = createString.get(); // emptyString 將會是 ""

    java.util.function.Function<Integer, int[]> createIntArray = int[]::new;
    int[] myArray = createIntArray.apply(5); // myArray 將會是一個大小為 5 的 int 陣列
    ```

**2. Stream API**

**什麼是 Stream API？**

Stream API 在 Java 8 中引入，提供了一個強大且優雅的方式來處理資料集合。一個 stream 代表一個支援各種聚合操作的元素序列。Stream 與集合不同；集合是關於儲存資料，而 stream 是關於處理資料。

**Stream API 的關鍵概念：**

*   **Stream：** 一個支援順序和並行聚合操作的元素序列。
*   **來源：** Stream 的來源（例如：一個集合、一個陣列、一個 I/O 通道）。
*   **中介操作：** 轉換或過濾 stream 並回傳一個新 stream 的操作。這些操作是惰性的，意味著它們直到呼叫了終端操作才會被執行。
*   **終端操作：** 產生結果或副作用並消耗 stream 的操作（在終端操作之後，stream 就無法再使用）。

**建立 Stream：**

你可以透過多種方式建立 stream：

*   **從集合：**

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob", "Charlie");
    java.util.stream.Stream<String> sequentialStream = names.stream();
    java.util.stream.Stream<String> parallelStream = names.parallelStream();
    ```

*   **從陣列：**

    ```java
    int[] numbers = {1, 2, 3, 4, 5};
    java.util.stream.IntStream intStream = java.util.Arrays.stream(numbers);
    ```

*   **使用 `Stream.of()`：**

    ```java
    java.util.stream.Stream<String> stringStream = java.util.stream.Stream.of("apple", "banana", "cherry");
    ```

*   **使用 `Stream.iterate()`：** (建立一個無限的順序有序 stream)

    ```java
    java.util.stream.Stream<Integer> evenNumbers = java.util.stream.Stream.iterate(0, n -> n + 2).limit(5); // 0, 2, 4, 6, 8
    ```

*   **使用 `Stream.generate()`：** (建立一個無限的順序無序 stream)

    ```java
    java.util.stream.Stream<Double> randomNumbers = java.util.stream.Stream.generate(Math::random).limit(3);
    ```

**中介操作：**

這些操作轉換或過濾 stream 並回傳一個新的 stream。常見的中介操作包括：

*   **`filter(Predicate<T> predicate)`：** 回傳一個由符合給定 predicate 的元素組成的 stream。

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(1, 2, 3, 4, 5, 6);
    java.util.stream.Stream<Integer> evenNumbersStream = numbers.stream().filter(n -> n % 2 == 0); // 2, 4, 6
    ```

*   **`map(Function<T, R> mapper)`：** 回傳一個由對該 stream 的元素應用給定函數的結果組成的 stream。

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob", "Charlie");
    java.util.stream.Stream<Integer> nameLengths = names.stream().map(String::length); // 5, 3, 7
    ```

*   **`flatMap(Function<T, Stream<R>> mapper)`：** 回傳一個由將該 stream 的每個元素替換為透過對每個元素應用提供的映射函數所產生的映射 stream 的內容組成的 stream。對於扁平化巢狀集合很有用。

    ```java
    java.util.List<java.util.List<Integer>> listOfLists = java.util.Arrays.asList(
            java.util.Arrays.asList(1, 2),
            java.util.Arrays.asList(3, 4, 5)
    );
    java.util.stream.Stream<Integer> singleStream = listOfLists.stream().flatMap(java.util.List::stream); // 1, 2, 3, 4, 5
    ```

*   **`sorted()`：** 回傳一個由該 stream 的元素組成的 stream，根據自然順序排序。

    ```java
    java.util.List<String> fruits = java.util.Arrays.asList("banana", "apple", "cherry");
    java.util.stream.Stream<String> sortedFruits = fruits.stream().sorted(); // apple, banana, cherry
    ```

*   **`distinct()`：** 回傳一個由該 stream 中的不同元素（根據 `equals()`）組成的 stream。

    ```java
    java.util.List<Integer> numbersWithDuplicates = java.util.Arrays.asList(1, 2, 2, 3, 3, 3);
    java.util.stream.Stream<Integer> distinctNumbers = numbersWithDuplicates.stream().distinct(); // 1, 2, 3
    ```

*   **`peek(Consumer<T> action)`：** 回傳一個由該 stream 的元素組成的 stream，並在從結果 stream 中消耗元素時，對每個元素執行提供的 action。主要用於除錯或副作用。

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob");
    java.util.stream.Stream<String> peekedNames = names.stream().peek(name -> System.out.println("Processing: " + name));
    peekedNames.forEach(System.out::println);
    // 輸出：
    // Processing: Alice
    // Alice
    // Processing: Bob
    // Bob
    ```

*   **`limit(long maxSize)`：** 回傳一個由該 stream 的元素組成的 stream，其長度被截斷為不超過 `maxSize`。

    ```java
    java.util.stream.Stream<Integer> firstThree = java.util.stream.Stream.iterate(1, n -> n + 1).limit(3); // 1, 2, 3
    ```

*   **`skip(long n)`：** 回傳一個在丟棄該 stream 的前 `n` 個元素後，由其餘元素組成的 stream。

    ```java
    java.util.stream.Stream<Integer> afterSkipping = java.util.stream.Stream.iterate(1, n -> n + 1).skip(2).limit(3); // 3, 4, 5
    ```

**終端操作：**

這些操作產生結果或副作用並消耗 stream。常見的終端操作包括：

*   **`forEach(Consumer<T> action)`：** 對該 stream 的每個元素執行一個操作。

    ```java
    java.util.List<String> colors = java.util.Arrays.asList("red", "green", "blue");
    colors.stream().forEach(System.out::println);
    ```

*   **`count()`：** 回傳該 stream 中的元素數量。

    ```java
    long numberOfFruits = java.util.Arrays.asList("apple", "banana", "cherry").stream().count(); // 3
    ```

*   **`collect(Collector<T, A, R> collector)`：** 使用 `Collector` 對該 stream 的元素執行可變的歸約操作。常見的收集器包括 `toList()`, `toSet()`, `toMap()`, `joining()`, `groupingBy()`, `summarizingInt()` 等。

    ```java
    java.util.List<String> fruits = java.util.Arrays.asList("apple", "banana", "cherry");
    java.util.List<String> fruitList = fruits.stream().collect(java.util.stream.Collectors.toList());
    java.util.Set<String> fruitSet = fruits.stream().collect(java.util.stream.Collectors.toSet());
    String joinedFruits = fruits.stream().collect(java.util.stream.Collectors.joining(", ")); // "apple, banana, cherry"
    ```

*   **`reduce(T identity, BinaryOperator<T> accumulator)`：** 使用提供的 identity 值和一個關聯的累積函數，對該 stream 的元素執行歸約。

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(1, 2, 3, 4);
    int sum = numbers.stream().reduce(0, (a, b) -> a + b); // sum 將會是 10
    ```

*   **`min(Comparator<T> comparator)`：** 根據提供的 comparator，回傳一個描述該 stream 中最小元素的 `Optional`。

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(3, 1, 4, 1, 5, 9);
    java.util.Optional<Integer> minNumber = numbers.stream().min(Integer::compareTo); // Optional[1]
    ```

*   **`max(Comparator<T> comparator)`：** 根據提供的 comparator，回傳一個描述該 stream 中最大元素的 `Optional`。

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(3, 1, 4, 1, 5, 9);
    java.util.Optional<Integer> maxNumber = numbers.stream().max(Integer::compareTo); // Optional[9]
    ```

*   **`findFirst()`：** 回傳一個描述該 stream 的第一個元素的 `Optional`。

    ```java
    java.util.Optional<String> firstFruit = java.util.Arrays.asList("apple", "banana", "cherry").stream().findFirst(); // Optional[apple]
    ```

*   **`findAny()`：** 回傳一個描述該 stream 中某個元素的 `Optional`。當 stream 是並行時，此操作可能不會總是回傳相同的結果。

    ```java
    java.util.Optional<String> anyFruit = java.util.Arrays.asList("apple", "banana", "cherry").stream().findAny(); // 可能回傳 Optional[apple], Optional[banana], 或 Optional[cherry]
    ```

*   **`anyMatch(Predicate<T> predicate)`：** 回傳該 stream 中是否有任何元素符合提供的 predicate。

    ```java
    boolean hasEven = java.util.Arrays.asList(1, 3, 5, 2, 7).stream().anyMatch(n -> n % 2 == 0); // true
    ```

*   **`allMatch(Predicate<T> predicate)`：** 回傳該 stream 中所有元素是否都符合提供的 predicate。

    ```java
    boolean allPositive = java.util.Arrays.asList(2, 4, 6, 8).stream().allMatch(n -> n > 0); // true
    ```

*   **`noneMatch(Predicate<T> predicate)`：** 回傳該 stream 中是否沒有元素符合提供的 predicate。

    ```java
    boolean noNegatives = java.util.Arrays.asList(1, 2, 3, 4).stream().noneMatch(n -> n < 0); // true
    ```

**3. Lambda 與 Stream 的關係**

Lambda 表達式在 Stream API 中被大量使用。它們提供了一種簡潔的方式來定義許多中介和終端操作的行為。例如，`filter()` 中的 `Predicate`、`map()` 中的 `Function` 以及 `forEach()` 中的 `Consumer`，通常都是使用 Lambda 表達式來實作的。

**結合 Lambda 與 Stream 的範例：**

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class LambdaStreamExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Eve");

        // 過濾以 'A' 開頭的名字並將其轉換為大寫
        List<String> aNamesUppercase = names.stream()
                .filter(name -> name.startsWith("A")) // 用於過濾的 Lambda
                .map(String::toUpperCase)             // 用於映射的方法參考
                .collect(Collectors.toList());

        System.out.println("Names starting with 'A' in uppercase: " + aNamesUppercase);
        // 輸出： Names starting with 'A' in uppercase: [ALICE]

        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // 找出偶數的平方和
        int sumOfSquaresOfEvens = numbers.stream()
                .filter(n -> n % 2 == 0)       // 用於過濾偶數的 Lambda
                .map(n -> n * n)              // 用於平方的 Lambda
                .reduce(0, Integer::sum);     // 用於求和的方法參考

        System.out.println("Sum of squares of even numbers: " + sumOfSquaresOfEvens);
        // 輸出： Sum of squares of even numbers: 220

        List<Person> people = Arrays.asList(
                new Person("Alice", 30),
                new Person("Bob", 25),
                new Person("Charlie", 35)
        );

        // 取得年齡大於 28 歲的人的名字列表
        List<String> olderPeopleNames = people.stream()
                .filter(person -> person.getAge() > 28) // 用於過濾的 Lambda
                .map(Person::getName)                 // 用於取得名字的方法參考
                .collect(Collectors.toList());

        System.out.println("Names of people older than 28: " + olderPeopleNames);
        // 輸出： Names of people older than 28: [Alice, Charlie]
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

**4. 並行 Stream**

Stream API 也支援並行處理。你可以使用集合上的 `parallelStream()` 方法，或是在順序 stream 上呼叫 `parallel()` 方法，輕鬆地並行處理 stream 中的元素。對於大型資料集上的某些操作，這可以顯著提升效能。

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// 並行計算平方和
int sumOfSquaresParallel = numbers.parallelStream()
        .map(n -> n * n)
        .reduce(0, Integer::sum);

System.out.println("Sum of squares (parallel): " + sumOfSquaresParallel);
```

**結論**

Lambda 表達式和 Stream API 是 Java 強大的新增功能，它們支援更函數式、更簡潔的程式碼撰寫風格，特別是在處理資料集合時。透過將 Lambda 與 Stream 結合使用，你可以以宣告式且易讀的方式執行複雜的資料處理操作。理解這些功能對於現代 Java 開發至關重要。記得要多加練習使用它們，以變得更熟練。