---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Java基本プログラミングガイド
translated: true
type: note
---

以下は、**08553 プログラミング入門—Java**の**第II部: 基本プログラミング**に焦点を当てた、**全国高等教育自学試験（自考）** 向けの要点をまとめたガイドです。このセクションでは、小さく正しいJavaプログラムを作成し、Javaがデータと式をどのように扱うかを理解する訓練を行います。

---

## 1. コンソールからの入力読み取り

### 1.1 `Scanner`の使用

Javaは`java.util`パッケージの`Scanner`クラスを使用して入力を行います。

```java
import java.util.Scanner;

public class InputExample {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("名前を入力してください: ");
        String name = sc.nextLine();
        System.out.print("年齢を入力してください: ");
        int age = sc.nextInt();
        System.out.println("Hello " + name + ", you are " + age + " years old.");
        sc.close();
    }
}
```

**要点:**

* 常に`import java.util.Scanner;`を記述する。
* データ型に基づいて`nextInt()`, `nextDouble()`, `nextLine()`を使用する。
* リソースを解放するために`Scanner`を閉じる。
* 注意: `nextLine()`は行の残りを読み取るため、`nextInt()`などと混在させると入力がスキップされる可能性がある。

---

## 2. 識別子、変数、式、代入、定数

### 2.1 識別子

変数、メソッド、クラスに付ける名前。
**規則:**

* 文字、`_`、`$`のいずれかで始まる必要がある。
* 数字で始めることはできない。
* 大文字と小文字は区別される (`score` ≠ `Score`)。
* キーワード (`int`, `class`, `if`など) を使用することはできない。

**例:**
`studentName`, `_total`, `$price`

### 2.2 変数

変数は特定の**型**のデータを保持する。
宣言の例:

```java
int age = 20;
double price = 12.5;
char grade = 'A';
boolean passed = true;
```

### 2.3 代入文

`=`を使用して値を代入する (右辺 → 左辺):

```java
x = 5;
y = x + 2;
```

### 2.4 定数

`final`で宣言し、後で変更することはできない:

```java
final double PI = 3.14159;
```

定数には大文字の名前を使用する。

---

## 3. 数値データ型と演算

### 3.1 一般的な数値型

* `byte` (8ビット整数)
* `short` (16ビット整数)
* `int` (32ビット整数、最も一般的)
* `long` (64ビット整数)
* `float` (32ビット小数)
* `double` (64ビット小数、より高精度)

**例:**

```java
int count = 5;
double price = 19.99;
```

### 3.2 基本算術演算子

`+`, `-`, `*`, `/`, `%`

例:

```java
int a = 10, b = 3;
System.out.println(a / b);  // 3 (整数除算)
System.out.println(a % b);  // 1
System.out.println((double)a / b); // 3.3333 (型変換)
```

---

## 4. 型変換 (キャスト)

### 4.1 自動変換 (拡大変換)

小さい型 → 大きい型への変換は自動的に行われる:
`int` → `long` → `float` → `double`

例:

```java
int i = 10;
double d = i;  // 自動変換
```

### 4.2 手動変換 (キャスト)

大きい型 → 小さい型への変換を明示的に行う:

```java
double d = 9.7;
int i = (int) d; // i = 9 (小数部が失われる)
```

**精度の損失**に注意する。

---

## 5. 式の評価と演算子の優先順位

### 5.1 演算の順序

Javaは定義された順序に従う:

1. 括弧 `( )`
2. 単項演算子 `+`, `-`, `++`, `--`
3. 乗算、除算、剰余 `* / %`
4. 加算と減算 `+ -`
5. 代入 `=`

例:

```java
int x = 2 + 3 * 4;   // 14, 20ではない
int y = (2 + 3) * 4; // 20
```

### 5.2 混合式

一方のオペランドが`double`の場合、結果は`double`になる:

```java
double result = 5 / 2;     // 2.0 (最初に整数除算が行われる)
double result2 = 5.0 / 2;  // 2.5 (浮動小数点除算が行われる)
```

---

## 6. 複合代入とインクリメント/デクリメント

### 6.1 複合代入

短縮演算子:

```java
x += 3;  // x = x + 3 と同じ
y *= 2;  // y = y * 2 と同じ
```

### 6.2 インクリメントとデクリメント

`++`は1増加、`--`は1減少。
2つの形式:

```java
int a = 5;
System.out.println(a++); // 5を出力し、その後 a = 6 になる
System.out.println(++a); // a = 7 になり、その後 7を出力する
```

**覚えておくこと:**

* 後置 (`a++`) → 使用してからインクリメント
* 前置 (`++a`) → インクリメントしてから使用

---

## 7. 避けるべき一般的なミス

* 比較で`==`の代わりに`=`を使用する。
* 小数を期待しているのに整数除算を行う。
* 使用前に変数を初期化するのを忘れる。
* 型変換でデータが失われる (例: `(int) 3.9` → 3)。

---

## 8. 典型的な試験問題

**例1:**

> 以下のコードの出力は何ですか？
>
> ```java
> int x = 5, y = 2;
> double z = x / y;
> System.out.println(z);
> ```

**答え:** `2.0` (代入前に整数除算が行われる)

**例2:**

> どの演算子が最も優先順位が高いですか？
> A. `+`
> B. `*`
> C. `=`
> D. `++`
> **答え:** D

**例3:**

> このコードの出力は何ですか？
>
> ```java
> int a = 3;
> int b = ++a + a++;
> System.out.println(b);
> ```

**説明:**
`++a`で`a = 4`になり、`4`を加算し、その後`a++`で`4`を使用し、インクリメントされて`a = 5`になる。
したがって`b = 8`。

---

次に、**第III部: 制御構造 (選択文と反復文)** を続けましょうか？これは`if`, `switch`, `for`, `while`をカバーし、Java試験における手続き型ロジックの核心です。