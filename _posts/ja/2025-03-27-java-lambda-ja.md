---
audio: false
generated: true
lang: ja
layout: post
title: Javaにおけるラムダ式とストリームAPI
translated: true
type: note
---

では、Javaのラムダ式とStream APIについて学びましょう。これらはJava 8で導入された強力な機能で、より関数型プログラミングのスタイルを可能にし、簡潔で表現力のあるコードにつながります。

**1. ラムダ式**

**ラムダ式とは？**

ラムダ式は本質的には無名（名前のない）関数です。これにより、別途メソッドを宣言することなく、インラインで関数を定義できます。ラムダ式は、特に機能インターフェースを扱う際に、振る舞いをデータとして渡すことを可能にし、コードをより柔軟で読みやすくするのに特に有用です。

**ラムダ式の構文:**

ラムダ式は以下の基本的な構文を持ちます：

```java
(パラメータリスト) -> 式本体
```

*   **パラメータリスト:** これはメソッドのパラメータと似ています。空でも、1つのパラメータを含んでも、複数のパラメータを含んでもかまいません。パラメータの型はコンパイラによって推論されることが多いため、常に明示的に宣言する必要はありません。
*   **アロー演算子 (`->`):** これはパラメータリストと式本体を分離します。
*   **式本体:** これはラムダ式が実行するコードです。単一の式でも、中括弧 `{}` で囲まれた文のブロックでもかまいません。

**関数型インターフェース:**

Javaにおけるラムダ式は、**関数型インターフェース** によって定義されたメソッドを実装するために使用されます。関数型インターフェースとは、**抽象メソッドを1つだけ** 含むインターフェースです。デフォルトメソッドやstaticメソッドを持つことはできますが、抽象メソッドは1つだけです。

Javaに組み込まれている関数型インターフェースの例：

*   `Runnable` (単一の抽象メソッド: `void run()`)
*   `Callable<V>` (単一の抽象メソッド: `V call() throws Exception`)
*   `Comparator<T>` (単一の抽象メソッド: `int compare(T o1, T o2)`)
*   `Consumer<T>` (単一の抽象メソッド: `void accept(T t)`)
*   `Function<T, R>` (単一の抽象メソッド: `R apply(T t)`)
*   `Predicate<T>` (単一の抽象メソッド: `boolean test(T t)`)
*   `Supplier<T>` (単一の抽象メソッド: `T get()`)

**ラムダ式の例:**

ラムダ式がどのように機能するかを理解するために、いくつかの例を見てみましょう：

*   **パラメータなし:**

    ```java
    Runnable myRunnable = () -> System.out.println("Hello from lambda!");
    myRunnable.run(); // 出力: Hello from lambda!
    ```

*   **1つのパラメータ (括弧は省略可能):**

    ```java
    Consumer<String> printMessage = message -> System.out.println("Message: " + message);
    printMessage.accept("Lambda is cool!"); // 出力: Message: Lambda is cool!
    ```

*   **複数のパラメータ:**

    ```java
    java.util.Comparator<Integer> compareTwoNumbers = (a, b) -> a.compareTo(b);
    int result = compareTwoNumbers.compare(5, 10); // result は -1
    ```

*   **文のブロックを持つラムダ式:**

    ```java
    java.util.function.Function<Integer, String> checkEvenOdd = number -> {
        if (number % 2 == 0) {
            return "Even";
        } else {
            return "Odd";
        }
    };
    String output = checkEvenOdd.apply(7); // output は "Odd"
    ```

**メソッド参照:**

メソッド参照は、既存のメソッドを単に呼び出すだけのラムダ式の短縮形の構文です。これによりコードはさらに簡潔になります。メソッド参照には4種類あります：

1.  **staticメソッドへの参照:** `クラス名::staticメソッド名`

    ```java
    java.util.function.Function<String, Integer> stringToInt = Integer::parseInt;
    int number = stringToInt.apply("123"); // number は 123
    ```

2.  **特定のオブジェクトのインスタンスメソッドへの参照:** `インスタンス::インスタンスメソッド名`

    ```java
    String message = "Hello";
    java.util.function.Supplier<Integer> getLength = message::length;
    int len = getLength.get(); // len は 5
    ```

3.  **特定の型の任意のオブジェクトのインスタンスメソッドへの参照:** `クラス名::インスタンスメソッド名`

    ```java
    java.util.function.BiPredicate<String, String> checkStartsWith = String::startsWith;
    boolean starts = checkStartsWith.test("Java", "Ja"); // starts は true
    ```

4.  **コンストラクタへの参照:** `クラス名::new`

    ```java
    java.util.function.Supplier<String> createString = String::new;
    String emptyString = createString.get(); // emptyString は ""

    java.util.function.Function<Integer, int[]> createIntArray = int[]::new;
    int[] myArray = createIntArray.apply(5); // myArray はサイズ5のint配列
    ```

**2. Stream API**

**Stream APIとは？**

Stream APIはJava 8で導入され、データのコレクションを処理するための強力でエレガントな方法を提供します。ストリームは、様々な集約操作をサポートする一連の要素を表します。ストリームはコレクションとは異なります。コレクションはデータの格納に関するものですが、ストリームはデータの処理に関するものです。

**Stream APIの主要な概念:**

*   **Stream:** 逐次および並列の集約操作をサポートする一連の要素。
*   **ソース:** ストリームの起源（例：コレクション、配列、I/Oチャネル）。
*   **中間操作:** ストリームを変換またはフィルタリングし、新しいストリームを返す操作。これらの操作は遅延して実行され、終端操作が呼び出されるまで実行されません。
*   **終端操作:** 結果や副作用を生成し、ストリームを消費する操作（終端操作の後、ストリームは使用できなくなります）。

**ストリームの作成:**

様々な方法でストリームを作成できます：

*   **コレクションから:**

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob", "Charlie");
    java.util.stream.Stream<String> sequentialStream = names.stream();
    java.util.stream.Stream<String> parallelStream = names.parallelStream();
    ```

*   **配列から:**

    ```java
    int[] numbers = {1, 2, 3, 4, 5};
    java.util.stream.IntStream intStream = java.util.Arrays.stream(numbers);
    ```

*   **`Stream.of()` を使用:**

    ```java
    java.util.stream.Stream<String> stringStream = java.util.stream.Stream.of("apple", "banana", "cherry");
    ```

*   **`Stream.iterate()` を使用:** (無限の順次順序付けされたストリームを作成)

    ```java
    java.util.stream.Stream<Integer> evenNumbers = java.util.stream.Stream.iterate(0, n -> n + 2).limit(5); // 0, 2, 4, 6, 8
    ```

*   **`Stream.generate()` を使用:** (無限の順次非順序付けされたストリームを作成)

    ```java
    java.util.stream.Stream<Double> randomNumbers = java.util.stream.Stream.generate(Math::random).limit(3);
    ```

**中間操作:**

これらの操作はストリームを変換またはフィルタリングし、新しいストリームを返します。一般的な中間操作には以下があります：

*   **`filter(Predicate<T> predicate)`:** 指定された述語に一致する要素からなるストリームを返します。

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(1, 2, 3, 4, 5, 6);
    java.util.stream.Stream<Integer> evenNumbersStream = numbers.stream().filter(n -> n % 2 == 0); // 2, 4, 6
    ```

*   **`map(Function<T, R> mapper)`:** このストリームの各要素に関数を適用した結果からなるストリームを返します。

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob", "Charlie");
    java.util.stream.Stream<Integer> nameLengths = names.stream().map(String::length); // 5, 3, 7
    ```

*   **`flatMap(Function<T, Stream<R>> mapper)`:** このストリームの各要素を、提供されたマッピング関数を各要素に適用して生成されたマップされたストリームの内容で置き換えた結果からなるストリームを返します。ネストされたコレクションを平坦化するのに便利です。

    ```java
    java.util.List<java.util.List<Integer>> listOfLists = java.util.Arrays.asList(
            java.util.Arrays.asList(1, 2),
            java.util.Arrays.asList(3, 4, 5)
    );
    java.util.stream.Stream<Integer> singleStream = listOfLists.stream().flatMap(java.util.List::stream); // 1, 2, 3, 4, 5
    ```

*   **`sorted()`:** このストリームの要素を自然順序でソートしたストリームを返します。

    ```java
    java.util.List<String> fruits = java.util.Arrays.asList("banana", "apple", "cherry");
    java.util.stream.Stream<String> sortedFruits = fruits.stream().sorted(); // apple, banana, cherry
    ```

*   **`distinct()`:** このストリームの重複のない要素 (`equals()` に従って) からなるストリームを返します。

    ```java
    java.util.List<Integer> numbersWithDuplicates = java.util.Arrays.asList(1, 2, 2, 3, 3, 3);
    java.util.stream.Stream<Integer> distinctNumbers = numbersWithDuplicates.stream().distinct(); // 1, 2, 3
    ```

*   **`peek(Consumer<T> action)`:** このストリームの要素からなるストリームを返しますが、その際、結果のストリームから要素が消費されるときに、提供されたアクションを各要素に対して追加的に実行します。主にデバッグや副作用のために使用されます。

    ```java
    java.util.List<String> names = java.util.Arrays.asList("Alice", "Bob");
    java.util.stream.Stream<String> peekedNames = names.stream().peek(name -> System.out.println("Processing: " + name));
    peekedNames.forEach(System.out::println);
    // 出力:
    // Processing: Alice
    // Alice
    // Processing: Bob
    // Bob
    ```

*   **`limit(long maxSize)`:** このストリームの要素からなる、長さが `maxSize` 以下に切り詰められたストリームを返します。

    ```java
    java.util.stream.Stream<Integer> firstThree = java.util.stream.Stream.iterate(1, n -> n + 1).limit(3); // 1, 2, 3
    ```

*   **`skip(long n)`:** 最初の `n` 個の要素を破棄した後、このストリームの残りの要素からなるストリームを返します。

    ```java
    java.util.stream.Stream<Integer> afterSkipping = java.util.stream.Stream.iterate(1, n -> n + 1).skip(2).limit(3); // 3, 4, 5
    ```

**終端操作:**

これらの操作は結果や副作用を生成し、ストリームを消費します。一般的な終端操作には以下があります：

*   **`forEach(Consumer<T> action)`:** このストリームの各要素に対してアクションを実行します。

    ```java
    java.util.List<String> colors = java.util.Arrays.asList("red", "green", "blue");
    colors.stream().forEach(System.out::println);
    ```

*   **`count()`:** このストリームの要素の数を返します。

    ```java
    long numberOfFruits = java.util.Arrays.asList("apple", "banana", "cherry").stream().count(); // 3
    ```

*   **`collect(Collector<T, A, R> collector)`:** `Collector` を使用して、このストリームの要素に対して可変的リダクション操作を実行します。一般的なコレクタには `toList()`, `toSet()`, `toMap()`, `joining()`, `groupingBy()`, `summarizingInt()` などがあります。

    ```java
    java.util.List<String> fruits = java.util.Arrays.asList("apple", "banana", "cherry");
    java.util.List<String> fruitList = fruits.stream().collect(java.util.stream.Collectors.toList());
    java.util.Set<String> fruitSet = fruits.stream().collect(java.util.stream.Collectors.toSet());
    String joinedFruits = fruits.stream().collect(java.util.stream.Collectors.joining(", ")); // "apple, banana, cherry"
    ```

*   **`reduce(T identity, BinaryOperator<T> accumulator)`:** 提供された単位元値と結合的な累積関数を使用して、このストリームの要素に対してリダクションを実行します。

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(1, 2, 3, 4);
    int sum = numbers.stream().reduce(0, (a, b) -> a + b); // sum は 10
    ```

*   **`min(Comparator<T> comparator)`:** 提供されたコンパレータに従って、このストリームの最小要素を記述する `Optional` を返します。

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(3, 1, 4, 1, 5, 9);
    java.util.Optional<Integer> minNumber = numbers.stream().min(Integer::compareTo); // Optional[1]
    ```

*   **`max(Comparator<T> comparator)`:** 提供されたコンパレータに従って、このストリームの最大要素を記述する `Optional` を返します。

    ```java
    java.util.List<Integer> numbers = java.util.Arrays.asList(3, 1, 4, 1, 5, 9);
    java.util.Optional<Integer> maxNumber = numbers.stream().max(Integer::compareTo); // Optional[9]
    ```

*   **`findFirst()`:** このストリームの最初の要素を記述する `Optional` を返します。

    ```java
    java.util.Optional<String> firstFruit = java.util.Arrays.asList("apple", "banana", "cherry").stream().findFirst(); // Optional[apple]
    ```

*   **`findAny()`:** このストリームのある要素を記述する `Optional` を返します。この操作は、ストリームが並列の場合、常に同じ結果を返すとは限りません。

    ```java
    java.util.Optional<String> anyFruit = java.util.Arrays.asList("apple", "banana", "cherry").stream().findAny(); // Optional[apple], Optional[banana], Optional[cherry] のいずれかを返す可能性あり
    ```

*   **`anyMatch(Predicate<T> predicate)`:** このストリームのいずれかの要素が指定された述語に一致するかどうかを返します。

    ```java
    boolean hasEven = java.util.Arrays.asList(1, 3, 5, 2, 7).stream().anyMatch(n -> n % 2 == 0); // true
    ```

*   **`allMatch(Predicate<T> predicate)`:** このストリームのすべての要素が指定された述語に一致するかどうかを返します。

    ```java
    boolean allPositive = java.util.Arrays.asList(2, 4, 6, 8).stream().allMatch(n -> n > 0); // true
    ```

*   **`noneMatch(Predicate<T> predicate)`:** このストリームのどの要素も指定された述語に一致しないかどうかを返します。

    ```java
    boolean noNegatives = java.util.Arrays.asList(1, 2, 3, 4).stream().noneMatch(n -> n < 0); // true
    ```

**3. ラムダとストリームの関係**

ラムダ式はStream APIと強力に連携して使用されます。これらは、多くの中間操作および終端操作のための振る舞いを定義する簡潔な方法を提供します。例えば、`filter()` 内の `Predicate`、`map()` 内の `Function`、`forEach()` 内の `Consumer` は、多くの場合ラムダ式を使用して実装されます。

**ラムダとストリームを組み合わせた例:**

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class LambdaStreamExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Eve");

        // 'A'で始まる名前をフィルタリングし、大文字に変換する
        List<String> aNamesUppercase = names.stream()
                .filter(name -> name.startsWith("A")) // フィルタリング用のラムダ
                .map(String::toUpperCase)             // マッピング用のメソッド参照
                .collect(Collectors.toList());

        System.out.println("Names starting with 'A' in uppercase: " + aNamesUppercase);
        // 出力: Names starting with 'A' in uppercase: [ALICE]

        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // 偶数の二乗の和を求める
        int sumOfSquaresOfEvens = numbers.stream()
                .filter(n -> n % 2 == 0)       // 偶数をフィルタリングするラムダ
                .map(n -> n * n)              // 二乗するラムダ
                .reduce(0, Integer::sum);     // 合計するメソッド参照

        System.out.println("Sum of squares of even numbers: " + sumOfSquaresOfEvens);
        // 出力: Sum of squares of even numbers: 220

        List<Person> people = Arrays.asList(
                new Person("Alice", 30),
                new Person("Bob", 25),
                new Person("Charlie", 35)
        );

        // 28歳より上の人の名前のリストを取得する
        List<String> olderPeopleNames = people.stream()
                .filter(person -> person.getAge() > 28) // フィルタリング用のラムダ
                .map(Person::getName)                 // 名前を取得するメソッド参照
                .collect(Collectors.toList());

        System.out.println("Names of people older than 28: " + olderPeopleNames);
        // 出力: Names of people older than 28: [Alice, Charlie]
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

**4. 並列ストリーム**

Stream APIは並列処理もサポートしています。コレクションに対して `parallelStream()` メソッドを使用するか、順次ストリームに対して `parallel()` メソッドを呼び出すことで、ストリームの要素を簡単に並列処理できます。これは、大規模なデータセットに対する特定の操作のパフォーマンスを大幅に向上させることができます。

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// 二乗和を並列で計算する
int sumOfSquaresParallel = numbers.parallelStream()
        .map(n -> n * n)
        .reduce(0, Integer::sum);

System.out.println("Sum of squares (parallel): " + sumOfSquaresParallel);
```

**結論**

ラムダ式とStream APIは、Javaへの強力な追加機能であり、特にデータのコレクションを扱う際に、より関数型的で簡潔なコードを書くことを可能にします。ラムダをストリームと共に使用することで、複雑なデータ処理操作を宣言的で読みやすい方法で実行できます。これらの機能を理解することは、現代のJava開発において不可欠です。これらを使いこなせるよう、練習を重ねて慣れ親しんでください。