---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Java関数型プログラミングガイド
translated: true
type: note
---

JavaはJava 8以降、関数型プログラミングの原則を取り入れ、ラムダ式、ストリームなどの機能を導入し、コードをより簡潔で読みやすく、宣言的にしました。このガイドでは、コアJavaの知識を前提に、基礎から高度な概念までをカバーします。これらの機能が登場したJava 8以降の構文を使用します。例は簡単にコピーできるようJavaコードブロックで示します。

## 1. Javaにおける関数型プログラミングの紹介

関数型プログラミング（FP）は以下を重視します：
- **純粋関数**: 副作用のない関数（例：可変状態の変更なし）。
- **不変性**: データは一度作成されたら変更されない。
- **高階関数**: 他の関数を引数に取る、または返す関数。
- **宣言型スタイル**: *どのように*ではなく、*何を*行うかに焦点（例：ループの代わりにストリームを使用）。

JavaはHaskellのように純粋に関数型ではありませんが、FPとオブジェクト指向のルーツを融合しています。主要な実現手段：
- ラムダ式（匿名関数）。
- 関数型インターフェース（単一の抽象メソッドを持つインターフェース）。
- コレクションを関数型的に処理するためのStreams API。

利点： ボイラープレートの削減、並列処理の容易化、優れた合成性。

## 2. ラムダ式

ラムダは、短い使い捨ての実装に使用される匿名関数です。JavaにおけるFPへの入り口です。

### 基本構文
ラムダは： `(パラメータ) -> { 本体 }`
- 単一パラメータの場合、括弧は省略可能。
- 単一式の場合、中括弧は省略可能（暗黙的なreturn）。
- 型推論がしばしば機能するが、型を指定することも可能。

```java
// 従来の匿名インナークラス
Runnable r = new Runnable() {
    @Override
    public void run() {
        System.out.println("Hello, World!");
    }
};

// ラムダによる同等の記述
Runnable lambda = () -> System.out.println("Hello, World!");
lambda.run();
```

### パラメータ付き
```java
// 二項演算子の例
BinaryOperator<Integer> add = (a, b) -> a + b;
System.out.println(add.apply(2, 3)); // 5

// 複数行の本体
Comparator<String> comparator = (s1, s2) -> {
    int lenDiff = s1.length() - s2.length();
    return lenDiff != 0 ? lenDiff : s1.compareTo(s2);
};
```

### 変数のキャプチャ（実質的final）
ラムダは外部変数にアクセスできるが、それらは**実質的final**（再代入されない）である必要があります。
```java
int threshold = 10;
Predicate<Integer> isHigh = x -> x > threshold; // OK
// threshold = 20; // エラー: 実質的finalではない
```

## 3. 関数型インターフェース

関数型インターフェースは、正確に1つの抽象メソッド（SAM - Single Abstract Method）を持ちます。Javaは`java.util.function`に組み込みのものを提供します。

### 組み込みの例
- `Predicate<T>`: `boolean test(T t)`
- `Function<T, R>`: `R apply(T t)`
- `Consumer<T>`: `void accept(T t)`
- `Supplier<T>`: `T get()`
- `BiFunction<T, U, R>`など、2つの入力用。

カスタム関数型インターフェース：
```java
@FunctionalInterface  // 任意だが、良い習慣
interface Transformer {
    String transform(String input);
}

Transformer upper = s -> s.toUpperCase();
System.out.println(upper.transform("java")); // JAVA
```

SAMを強制するには`@FunctionalInterface`を使用します。

### デフォルトメソッドと静的メソッド
関数型インターフェースは（Java 8以降）デフォルトメソッドを持つことができます。`Optional.orElse()`など。
```java
default int compare(String a, String b) { ... } // 許可される
static void utility() { ... } // 許可される
```

## 4. メソッド参照

既存のメソッドを呼び出すラムダ式の省略記法。構文： `クラス::メソッド` または `インスタンス::メソッド`。

種類：
- 静的: `クラス::静的メソッド`
- 特定の型のインスタンス: `クラス::インスタンスメソッド`
- 任意のオブジェクトのインスタンス: `オブジェクト::インスタンスメソッド`
- コンストラクタ: `クラス::new`

例：
```java
// ラムダ: x -> System.out.println(x)
Consumer<String> printer = System.out::println;

// 静的メソッド
Function<String, Integer> length = String::length;

// インスタンスメソッド
List<String> list = Arrays.asList("a", "b");
list.forEach(System.out::println); // 各要素を出力

// コンストラクタ
Supplier<List<String>> listSupplier = ArrayList::new;
```

## 5. Streams API

ストリームはコレクションを宣言的に処理します：作成 → 変換 → 収集。遅延評価（中間操作は終端操作が実行されるまで実行されない）。

### ストリームの作成
```java
import java.util.*;
import java.util.stream.*;

List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

// コレクションから
Stream<String> stream = names.stream();

// 配列から
String[] arr = {"x", "y"};
Stream<String> arrStream = Arrays.stream(arr);

// 無限ストリーム
Stream<Integer> infinite = Stream.iterate(0, n -> n + 1);
```

### 中間操作（遅延）
これらをチェーンする。終端操作まで計算は実行されない。
- `filter(Predicate)`: 一致する要素を保持。
- `map(Function)`: 各要素を変換。
- `flatMap(Function<? super T, ? extends Stream<? extends R>>)`: ネストしたストリームを平坦化。
- `distinct()`, `sorted()`, `limit(n)`, `skip(n)`.

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
List<Integer> evensSquared = numbers.stream()
    .filter(n -> n % 2 == 0)
    .map(n -> n * n)
    .collect(Collectors.toList()); // [4, 16]
```

### 終端操作（熱心）
計算をトリガーし、結果を返す。
- `collect(Collector)`: リスト、セット、マップへ。
- `forEach(Consumer)`: 副作用（可能であれば避ける）。
- `reduce()`: 集約（例：合計）。
- `anyMatch()`, `allMatch()`, `findFirst()`.

```java
// Reduce: 合計
int sum = numbers.stream().reduce(0, Integer::sum); // 15

// マップへ収集
Map<String, Integer> nameLengths = Stream.of("Alice", "Bob")
    .collect(Collectors.toMap(s -> s, String::length)); // {Alice=5, Bob=3}

// グループ化
Map<Integer, List<String>> byLength = names.stream()
    .collect(Collectors.groupingBy(String::length)); // {5=[Alice, Charlie], 3=[Bob]}
```

### 並列ストリーム
並列処理のために： `parallelStream()` または `.parallel()`。注意して使用（デバッグが困難）。
```java
long count = names.parallelStream().count(); // 3
```

## 6. コレクタ

`java.util.stream.Collectors`から。複雑なリダクションを構築。

一般的なもの：
- `toList()`, `toSet()`, `toMap()`
- `joining()`: 文字列を連結。
- `summingInt()`, `averagingDouble()`
- `groupingBy()`, `partitioningBy()`
- `collectingAndThen()`: 後処理。

```java
// 長さによる最大値のカスタムコレクタ
String longest = names.stream()
    .collect(Collectors.maxBy(Comparator.comparingInt(String::length)))
    .orElse(""); // "Charlie"

// 偶数/奇数で分割
Map<Boolean, List<Integer>> partitions = numbers.stream()
    .collect(Collectors.partitioningBy(n -> n % 2 == 0));
```

## 7. Optional

潜在的にnullである値をラップすることで`NullPointerException`を回避します。明示的なnull処理を促進します。

作成：
- `Optional.of(値)`: 非null。
- `Optional.ofNullable(値)`: Null → empty。
- `Optional.empty()`.

操作：
- `isPresent()`, `ifPresent(Consumer)`
- `orElse(デフォルト値)`, `orElseThrow()`
- `map()`, `flatMap()` でチェーン。

```java
Optional<String> opt = Optional.ofNullable(getName()); // nullを返す可能性があると仮定

String name = opt.orElse("Unknown");
opt.ifPresent(System.out::println);

String upper = opt.map(String::toUpperCase).orElse("DEFAULT");
```

ストリームはしばしば`Optional`を返します（例：`findFirst()`）。

## 8. 高度なトピック

### 合成可能な関数
`Function.andThen()`, `Function.compose()` でチェーン。
```java
Function<String, Integer> len = String::length;
Function<Integer, String> toStr = i -> "Len: " + i;

Function<String, String> chain = len.andThen(toStr);
System.out.println(chain.apply("Java")); // Len: 4
```

### 再帰と末尾呼び出し
Javaは最適化を欠くが、反復的な再帰には`Stream.iterate()`を使用。

### 不変性ヘルパー
`Collections.unmodifiableList()` または Guava/Immutable Collections のようなライブラリを使用（ただしJava 10+以降では`List.of()`が組み込み）。

`List.of("a", "b")` は不変リストを作成（Java 9+）。

### パターンマッチング（Java 21+ プレビュー/安定版）
スイッチでの分解によるFPを強化。
```java
// プレビュー機能; --enable-previewで有効化
String desc = switch (obj) {
    case Integer i -> "int: " + i;
    case String s -> "str: " + s.length();
    default -> "unknown";
};
```

### 仮想スレッド（Java 21+）
FPは、並行ストリームのための軽量スレッドで輝きます。

## 9. ベストプラクティス

- **不変性を優先**: finalフィールドを使用、コレクションの変更を避ける。
- **副作用を避ける**: ラムダを純粋に保つ。副作用は`forEach`または明示的なコンシューマ内でのみ。
- **ストリーム vs ループ**: 可読性にはストリームを。パフォーマンスがクリティカルなコードにはループを。
- **Null**: nullチェックより`Optional`を好む。
- **テスト**: ラムダで関数型インターフェースを簡単にモック。
- **パフォーマンス**: ストリームにはオーバーヘッドあり。並列使用前にプロファイル。
- **可読性**: 短いラムダは問題ない。複雑なロジックにはメソッドを抽出。

一般的な落とし穴：
- ラムダ内で外部状態を変更。
- 終端操作を忘れる（ストリームは何もしない！）。
- 並列ストリームの過剰使用（常に高速とは限らない）。

## 10. 例: 関数型パイプライン

従業員のリストを関数型的に処理。

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

        // 高給なエンジニアの名前をソートして取得
        List<String> result = employees.stream()
            .filter(e -> e.dept == Department.ENG)
            .filter(e -> e.salary > 52000)
            .map(Employee::getName)  // ゲッターがあると仮定
            .sorted()
            .collect(Collectors.toList());

        System.out.println(result); // [Charlie]
    }
}
```

## 結論

ラムダとFPはJavaを命令型から表現豊かなものへと変えます。単純な置換（例：ループの代わりに`forEach`）から始め、パイプラインを構築していきましょう。習得には実際のプロジェクトで実践を。より深く学ぶには、IDEで実験してください。

### 参考文献
- [Oracle Java Tutorials: Lambda Expressions](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html)
- [Baeldung: Java 8 Functional Interfaces](https://www.baeldung.com/java-functional-interfaces)
- [Java Streams Guide](https://www.baeldung.com/java-8-streams)
- [Effective Java (3rd Ed.) - Item 42-45 on Lambdas](https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/)