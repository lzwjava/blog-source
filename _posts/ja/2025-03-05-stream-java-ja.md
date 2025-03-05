---
audio: false
generated: true
lang: ja
layout: post
title: JavaのStream API
translated: true
---

`java.util.stream` を Java で使用するには、Java 8 で導入された Stream API を活用して、データのコレクションを関数型および宣言的な方法で処理することができます。ストリームを使用すると、リストや配列などの要素のシーケンスに対してフィルタリング、マッピング、リデュースなどの操作を効率的にかつ簡潔に実行できます。以下に、整数のリストから 10 より大きい偶数の平均を求める具体的な例を通じて、`java.util.stream` の使用方法を説明します。これにより、主要なストリーム操作と概念が示されます。

---

### **`java.util.stream` の概要**
`java.util.stream` パッケージは、`Stream` インターフェースと関連クラス（`IntStream`、`DoubleStream` など）を提供してデータを処理します。ストリームは、パイプラインで実行される操作をサポートする要素のシーケンスです。これらの操作は以下の通りです：
- **中間操作**：ストリームを変換またはフィルタリングして新しいストリームを返します（例：`filter`、`map`）。これらは遅延され、終端操作が呼び出されたときにのみ実行されます。
- **終端操作**：結果または副作用を生成してデータを処理するパイプラインをトリガーします（例：`average`、`collect`）。

ストリームを使用するには、通常以下の手順を踏みます：
1. データソース（例：リスト）からストリームを作成します。
2. データを変換またはフィルタリングするために中間操作を適用します。
3. 結果を生成するために終端操作を使用します。

---

### **例の問題**
この問題を解決します：`List<Integer>` が与えられたとき、10 より大きいすべての偶数の平均を計算します。そのような数が存在しない場合は 0.0 を返します。これを `java.util.stream` を使用して行う方法は以下の通りです。

#### **ステップバイステップの解決方法**
1. **ストリームの作成**
   - `List<Integer>`（例：`List.of(1, 2, 12, 15, 20, 25, 30)`）から始めます。
   - `stream()` メソッドを使用して `Stream<Integer>` を作成します：
     ```java
     list.stream()
     ```

2. **ストリームのフィルタリング**
   - 10 より大きく偶数である数だけを保持するために `filter` メソッドを使用します。
   - `filter` メソッドは、ラムダ式としての `Predicate`（ブール値を返す関数）を取ります：
     ```java
     .filter(number -> number % 2 == 0 && number > 10)
     ```
     - `number % 2 == 0` は数が偶数かどうかを確認します。
     - `number > 10` は数が 10 より大きいかどうかを確認します。
     - 例のリスト `[1, 2, 12, 15, 20, 25, 30]` の場合、これは `[12, 20, 30]` を保持します。

3. **`IntStream` に変換**
   - `average()` は `IntStream` などのプリミティブストリームで利用可能であるため、`Stream<Integer>` を `IntStream` に変換します：
     ```java
     .mapToInt(i -> i)
     ```
     - `i -> i` は各 `Integer` を `int` にアンボックスします。代わりに `Integer::intValue` を使用することもできます。
     - これにより、`[12, 20, 30]` の `IntStream` が得られます。

4. **平均の計算**
   - `IntStream` 上で `average()` メソッドを使用し、ストリームが空の場合に `OptionalDouble` を返します：
     ```java
     .average()
     ```
     - `[12, 20, 30]` の場合、これは `(12 + 20 + 30) / 3 = 20.666...` を計算します。
     - ストリームが空の場合、空の `OptionalDouble` を返します。

5. **空の場合の処理**
   - フィルタに合致する数が存在しない場合に 0.0 を返すために、`OptionalDouble` に `orElse(0.0)` を使用します：
     ```java
     .orElse(0.0)
     ```
     - `[12, 20, 30]` の場合、これは `20.666...` を返します。
     - リスト `[1, 3, 5]`（偶数 > 10 が存在しない）の場合、これは `0.0` を返します。

#### **完了したコード**
以下は、メソッドとしての完全な解決策です：
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
        // テストケース
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

### **`java.util.stream` で示された主要な機能**
- **チェイニング**：操作はフルエントスタイルでチェーンされます（例：`.filter().mapToInt().average()`）。
- **遅延評価**：中間操作（`filter` や `mapToInt`）は終端操作（`average`）が呼び出されたときにのみ実行されます。
- **プリミティブストリーム**：`IntStream` は `average()` などの数値操作に特化したメソッドを提供し、ボクシングのオーバーヘッドを避けます。
- **オプショナルの処理**：`OptionalDouble` は結果が存在しない場合を処理し、`orElse` がデフォルト値を提供します。

---

### **代替アプローチ**
`Collectors` クラスを使用することもできます：
```java
import java.util.stream.Collectors;

double average = list.stream()
                     .filter(number -> number % 2 == 0 && number > 10)
                     .collect(Collectors.averagingInt(i -> i));
```
- これは空のストリームの場合に `0.0` を返す `Double` を直接返します。しかし、`mapToInt().average()` はこのシンプルなケースに対してより直接的であり、プリミティブストリームの使用に適しています。

---

### **ストリームの使用時機**
- コレクションを処理する際に、簡潔で読みやすいコードを作成するために `java.util.stream` を使用します。
- 大規模なデータセットの場合は、`parallelStream()` を `stream()` の代わりに使用して並列処理を活用することを検討してくださいが、小さなリストの場合はオーバーヘッドが大きいため過剰です。

---

この例は、`java.util.stream` を使用して実用的な問題を解決する方法を示しています。これらの手順—ストリームの作成、フィルタリング、マッピング、リデュース—を他のシナリオに適応させることができます！