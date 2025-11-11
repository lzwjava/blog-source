---
audio: false
generated: true
lang: ja
layout: post
title: Javaの関数型インターフェース
translated: true
type: note
---

Java 8で導入された`java.util.function`パッケージは、関数型プログラミングをサポートするための一連の関数型インターフェースを提供します。これらのインターフェースはそれぞれ単一の抽象メソッドを持ち、ラムダ式やメソッド参照との互換性があります。このレスポンスでは、このパッケージで最も一般的な関数型インターフェースである`Function<T, R>`、`Predicate<T>`、`Consumer<T>`、`Supplier<T>`の使用方法を実践的な例とともに説明します。

---

### 関数型インターフェースとは？
関数型インターフェースは、抽象メソッドを1つだけ持つインターフェースです。`java.util.function`パッケージは一般的なタスク向けに事前定義された関数型インターフェースを提供するため、独自に作成する必要はありません。これらのインターフェースは、ラムダ式、メソッド参照、Stream APIと組み合わせて使用され、簡潔で表現力のあるコードを記述するために広く利用されています。

主なインターフェースの使用方法は以下の通りです：

---

### 1. `Function<T, R>`: 入力から出力への変換
`Function<T, R>`インターフェースは、型`T`の入力を受け取り、型`R`の出力を生成する関数を表します。その抽象メソッドは`apply`です。

#### 例: 文字列の長さを取得する
```java
import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        Function<String, Integer> stringLength = s -> s.length();
        System.out.println(stringLength.apply("Hello")); // 出力: 5
    }
}
```
- **説明**: ラムダ式`s -> s.length()`は、`String`（`T`）を受け取り`Integer`（`R`）を返す`Function`を定義しています。`apply`メソッドがこのロジックを実行します。

---

### 2. `Predicate<T>`: 条件のテスト
`Predicate<T>`インターフェースは、型`T`の入力を受け取る真偽値関数を表します。その抽象メソッドは`test`です。

#### 例: 数値が偶数かどうかをチェックする
```java
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        Predicate<Integer> isEven = n -> n % 2 == 0;
        System.out.println(isEven.test(4)); // 出力: true
        System.out.println(isEven.test(5)); // 出力: false
    }
}
```
- **説明**: ラムダ式`n -> n % 2 == 0`は、入力が偶数の場合に`true`を返す`Predicate`を定義しています。`test`メソッドがこの条件を評価します。

---

### 3. `Consumer<T>`: アクションの実行
`Consumer<T>`インターフェースは、型`T`の入力を受け取り、結果を返さない操作を表します。その抽象メソッドは`accept`です。

#### 例: 文字列を出力する
```java
import java.util.function.Consumer;

public class Main {
    public static void main(String[] args) {
        Consumer<String> printer = s -> System.out.println(s);
        printer.accept("Hello, World!"); // 出力: Hello, World!
    }
}
```
- **説明**: ラムダ式`s -> System.out.println(s)`は、入力を受け取って出力する`Consumer`を定義しています。`accept`メソッドがアクションを実行します。

---

### 4. `Supplier<T>`: 結果の生成
`Supplier<T>`インターフェースは、結果の供給元を表し、入力を受け取らずに型`T`の値を返します。その抽象メソッドは`get`です。

#### 例: 乱数を生成する
```java
import java.util.function.Supplier;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Supplier<Integer> randomInt = () -> new Random().nextInt(100);
        System.out.println(randomInt.get()); // 0から99の範囲の乱数を出力
    }
}
```
- **説明**: ラムダ式`() -> new Random().nextInt(100)`は、乱数を生成する`Supplier`を定義しています。`get`メソッドが値を取得します。

---

### Stream APIでの関数型インターフェースの使用
これらのインターフェースはJava Stream APIで真価を発揮し、簡潔なデータ処理を可能にします。以下は文字列のリストをフィルタリング、変換、出力する例です：

#### 例: 文字列リストの処理
```java
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        List<String> strings = Arrays.asList("a", "bb", "ccc", "dddd");

        Predicate<String> longerThanTwo = s -> s.length() > 2;       // 長さが2より大きい文字列をフィルタリング
        Function<String, String> toUpperCase = s -> s.toUpperCase(); // 大文字に変換
        Consumer<String> printer = s -> System.out.println(s);       // 各結果を出力

        strings.stream()
               .filter(longerThanTwo)   // "ccc"と"dddd"を保持
               .map(toUpperCase)        // "CCC"と"DDDD"に変換
               .forEach(printer);       // 出力: CCC, DDDD（別々の行に）
    }
}
```
- **説明**: 
  - `filter`は`Predicate`を使用して長さ>2の文字列を保持します。
  - `map`は`Function`を使用して文字列を大文字に変換します。
  - `forEach`は`Consumer`を使用して各結果を出力します。

#### メソッド参照の使用
メソッド参照を使用するとさらに簡潔に記述できます：
```java
strings.stream()
       .filter(s -> s.length() > 2)
       .map(String::toUpperCase)      // Functionのメソッド参照
       .forEach(System.out::println); // Consumerのメソッド参照
```

---

### 関数型インターフェースの合成
一部のインターフェースは、より複雑な操作のために合成を可能にします：
- **Functionの合成**: `andThen`または`compose`を使用します。
  ```java
  Function<String, Integer> toLength = s -> s.length();
  Function<Integer, String> toString = i -> "Length is " + i;
  Function<String, String> combined = toLength.andThen(toString);
  System.out.println(combined.apply("Hello")); // 出力: Length is 5
  ```
- **Predicateの結合**: `and`、`or`、`negate`を使用します。
  ```java
  Predicate<String> isLong = s -> s.length() > 5;
  Predicate<String> startsWithA = s -> s.startsWith("A");
  Predicate<String> isLongAndStartsWithA = isLong.and(startsWithA);
  System.out.println(isLongAndStartsWithA.test("Avocado")); // 出力: true
  ```

---

### まとめ
これらのインターフェースの使用場面と方法：
- **`Function<T, R>`**: 入力を出力に変換する（例: `apply`）
- **`Predicate<T>`**: 条件をテストする（例: `test`）
- **`Consumer<T>`**: 入力に対してアクションを実行する（例: `accept`）
- **`Supplier<T>`**: 入力なしで値を生成する（例: `get`）
- **Stream APIでの使用**: 強力なデータ処理のために組み合わせる
- **合成**: 複雑なロジックのために連結または結合する

これらのインターフェースは、ラムダ式（例: `s -> s.length()`）またはメソッド参照（例: `String::toUpperCase`）を使用して実装できます。これらはJavaで関数型プログラミングスタイルを可能にし、特にStream APIと組み合わせることで、コードをより簡潔で読みやすく、再利用可能にします。