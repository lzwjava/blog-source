---
audio: false
generated: true
lang: ja
layout: post
title: JavaのストリームAPI
translated: true
type: note
---

Javaで`java.util.stream`を使用するには、Java 8で導入されたStream APIを活用して、データのコレクションを機能的かつ宣言的に処理できます。ストリームを使用すると、要素のシーケンス（リストや配列など）に対してフィルタリング、マッピング、リデュースなどの操作を効率的かつ簡潔に実行できます。以下では、整数のリストから10より大きい偶数の平均値を求める具体的な例を通して、`java.util.stream`の使用方法を説明します。これにより、主要なストリーム操作と概念を実演します。

---

### **`java.util.stream`の概要**
`java.util.stream`パッケージは、データを処理するための`Stream`インターフェースおよび関連クラス（`IntStream`、`DoubleStream`など）を提供します。ストリームは、パイプラインで実行される操作をサポートする要素のシーケンスです。これらの操作は以下の通りです：
- **中間操作**: ストリームを変換またはフィルタリングします（例: `filter`、`map`）。新しいストリームを返し、遅延実行され、終端操作が呼び出されたときにのみ実行されます。
- **終端操作**: 結果や副作用を生成します（例: `average`、`collect`）。データ処理のパイプラインをトリガーします。

ストリームを使用するには、一般的に以下の手順を踏みます：
1. データソース（例: リスト）からストリームを作成します。
2. データを変換またはフィルタリングするために中間操作を適用します。
3. 結果を生成するために終端操作を使用します。

---

### **例題**
この問題を解決します：`List<Integer>`が与えられたとき、10より大きいすべての偶数の平均値を計算します。該当する数値が存在しない場合は0.0を返します。以下に、`java.util.stream`を使用した方法を示します。

#### **ステップバイステップの解決策**
1. **ストリームの作成**
   - `List<Integer>`（例: `List.of(1, 2, 12, 15, 20, 25, 30)`）から開始します。
   - `stream()`メソッドを使用して`Stream<Integer>`を作成します：
     ```java
     list.stream()
     ```

2. **ストリームのフィルタリング**
   - `filter`メソッドを使用して、偶数かつ10より大きい数値のみを保持します。
   - `filter`メソッドはラムダ式として`Predicate`（ブール値を返す関数）を取ります：
     ```java
     .filter(number -> number % 2 == 0 && number > 10)
     ```
     - `number % 2 == 0`は数値が偶数かどうかをチェックします。
     - `number > 10`は数値が10より大きいことを保証します。
     - 例のリスト`[1, 2, 12, 15, 20, 25, 30]`の場合、`[12, 20, 30]`が保持されます。

3. **`IntStream`への変換**
   - `average()`は`IntStream`のようなプリミティブストリームで利用可能です（`Stream<Integer>`ではありません）。`mapToInt`を使用して`Stream<Integer>`を`IntStream`に変換します：
     ```java
     .mapToInt(i -> i)
     ```
     - `i -> i`は各`Integer`を`int`にアンボックスします。代わりに`Integer::intValue`を使用することもできます。
     - これにより`[12, 20, 30]`の`IntStream`が得られます。

4. **平均値の計算**
   - `IntStream`の`average()`メソッドを使用します。これは`OptionalDouble`を返します（ストリームが空の場合があるため）：
     ```java
     .average()
     ```
     - `[12, 20, 30]`の場合、`(12 + 20 + 30) / 3 = 20.666...`を計算します。
     - ストリームが空の場合、空の`OptionalDouble`を返します。

5. **空の場合の処理**
   - `OptionalDouble`で`orElse(0.0)`を使用し、フィルターを満たす数値がない場合は0.0を返します：
     ```java
     .orElse(0.0)
     ```
     - `[12, 20, 30]`の場合、`20.666...`を返します。
     - `[1, 3, 5]`（10より大きい偶数がない）のようなリストの場合、`0.0`を返します。

#### **完全なコード**
メソッドとしての完全な解決策は以下の通りです：
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

### **`java.util.stream`の主な機能の実演**
- **チェーニング**: 操作は流暢なスタイルでチェーンされます（例: `.filter().mapToInt().average()`）。
- **遅延実行**: 中間操作（`filter`や`mapToInt`など）は、終端操作（`average`）が呼び出されたときにのみ実行されます。
- **プリミティブストリーム**: `IntStream`は数値操作に特化した`average()`などのメソッドを提供し、ボクシングのオーバーヘッドを回避します。
- **Optionalの処理**: `OptionalDouble`は結果が存在しない場合を処理し、`orElse`はデフォルト値を提供します。

---

### **代替アプローチ**
`Collectors`クラスを使用することもできます：
```java
import java.util.stream.Collectors;

double average = list.stream()
                     .filter(number -> number % 2 == 0 && number > 10)
                     .collect(Collectors.averagingInt(i -> i));
```
- これは直接`Double`を返し、空のストリームの場合には`0.0`を返します。ただし、この単純なケースでは`mapToInt().average()`の方が直接的であり、プリミティブストリームの使用に適しています。

---

### **ストリームを使用する場合**
- コレクションを処理する際に、簡潔で読みやすいコードのために`java.util.stream`を使用します。
- 大規模なデータセットの場合、オーバーヘッドがあるため小さいリストでは過剰ですが、並列性を活用するために`stream()`の代わりに`parallelStream()`を検討してください。

---

この例は、実用的な問題を解決するために`java.util.stream`を使用する方法を示しています。これらのステップ—ストリームの作成、フィルタリング、マッピング、リデュース—を必要に応じて他のシナリオに適応させることができます！