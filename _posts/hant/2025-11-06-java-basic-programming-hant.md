---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: Java 基礎程式設計指南
translated: true
type: note
---

以下是針對 *08553 程式設計導論—Java* **第二部分：基礎程式設計**的精要指南，專為**全國高等教育自學考試（自考）**量身打造。本節將訓練你撰寫小型、正確的 Java 程式，並理解 Java 如何處理資料與運算式。

---

## 1. 從控制台讀取輸入

### 1.1 使用 `Scanner`

Java 使用 `java.util` 中的 `Scanner` 類別來讀取輸入。

```java
import java.util.Scanner;

public class InputExample {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("請輸入您的姓名：");
        String name = sc.nextLine();
        System.out.print("請輸入您的年齡：");
        int age = sc.nextInt();
        System.out.println("你好 " + name + "，您今年 " + age + " 歲。");
        sc.close();
    }
}
```

**重點提示：**

* 務必 `import java.util.Scanner;`
* 根據資料類型使用 `nextInt()`、`nextDouble()`、`nextLine()`。
* 關閉 `Scanner` 以釋放資源。
* 注意：`nextLine()` 會讀取該行的剩餘部分，因此與 `nextInt()` 混用可能導致輸入被跳過。

---

## 2. 識別符、變數、運算式、指派與常數

### 2.1 識別符

你為變數、方法或類別所命的名稱。
**規則：**

* 必須以字母、`_` 或 `$` 開頭。
* 不能以數字開頭。
* 區分大小寫（`score` ≠ `Score`）。
* 不能是關鍵字（`int`、`class`、`if` 等）。

**範例：**
`studentName`、`_total`、`$price`

### 2.2 變數

變數持有特定**類型**的資料。
宣告範例：

```java
int age = 20;
double price = 12.5;
char grade = 'A';
boolean passed = true;
```

### 2.3 指派陳述式

使用 `=` 指派值（由右至左）：

```java
x = 5;
y = x + 2;
```

### 2.4 常數

使用 `final` 宣告，之後無法更改：

```java
final double PI = 3.14159;
```

常數名稱請使用大寫。

---

## 3. 數值資料類型與運算

### 3.1 常見數值類型

* `byte` (8 位元整數)
* `short` (16 位元)
* `int` (32 位元，最常見)
* `long` (64 位元)
* `float` (32 位元小數)
* `double` (64 位元小數，更精確)

**範例：**

```java
int count = 5;
double price = 19.99;
```

### 3.2 基本算術運算子

`+`、`-`、`*`、`/`、`%`

範例：

```java
int a = 10, b = 3;
System.out.println(a / b);  // 3 (整數除法)
System.out.println(a % b);  // 1
System.out.println((double)a / b); // 3.3333 (型別轉換)
```

---

## 4. 型別轉換（轉型）

### 4.1 自動轉換（擴展）

小類型 → 大類型自動轉換：
`int` → `long` → `float` → `double`

範例：

```java
int i = 10;
double d = i;  // 自動轉換
```

### 4.2 手動轉換（轉型）

明確地將大類型 → 小類型：

```java
double d = 9.7;
int i = (int) d; // i = 9 (小數部分遺失)
```

注意**精度遺失**。

---

## 5. 運算式求值與運算子優先順序

### 5.1 運算順序

Java 遵循既定順序：

1. 括號 `( )`
2. 一元運算子 `+`、`-`、`++`、`--`
3. 乘法、除法、取餘數 `* / %`
4. 加法與減法 `+ -`
5. 指派 `=`

範例：

```java
int x = 2 + 3 * 4;   // 14，不是 20
int y = (2 + 3) * 4; // 20
```

### 5.2 混合運算式

若其中一個運算元是 `double`，結果將轉為 `double`：

```java
double result = 5 / 2;     // 2.0 (先進行整數除法)
double result2 = 5.0 / 2;  // 2.5 (浮點數除法)
```

---

## 6. 複合指派與遞增/遞減

### 6.1 複合指派

快捷運算子：

```java
x += 3;  // 等同於 x = x + 3
y *= 2;  // 等同於 y = y * 2
```

### 6.2 遞增與遞減

`++` 增加 1，`--` 減少 1。
兩種形式：

```java
int a = 5;
System.out.println(a++); // 輸出 5，然後 a = 6
System.out.println(++a); // a = 7，然後輸出 7
```

**記住：**

* 後置（`a++`）→ 先使用再遞增
* 前置（`++a`）→ 先遞增再使用

---

## 7. 常見錯誤避免

* 在比較中使用 `=` 而非 `==`。
* 預期得到小數結果時卻使用了整數除法。
* 使用變數前忘記初始化。
* 型別轉換中遺失資料（例如 `(int) 3.9` → 3）。

---

## 8. 典型考題範例

**範例 1：**

> 以下程式碼的輸出是什麼？
>
> ```java
> int x = 5, y = 2;
> double z = x / y;
> System.out.println(z);
> ```

**答案：** `2.0` (指派前先進行整數除法)

**範例 2：**

> 哪個運算子的優先順序最高？
> A. `+`
> B. `*`
> C. `=`
> D. `++`
> **答案：** D

**範例 3：**

> 這段程式碼的輸出是什麼？
>
> ```java
> int a = 3;
> int b = ++a + a++;
> System.out.println(b);
> ```

**解釋：**
`++a` 使 `a = 4`，加上 `4`，然後 `a++` 使用 `4` 並遞增至 `5`。
所以 `b = 8`。

---

您是否希望我繼續講解**第三部分：控制結構（選擇與迴圈陳述式）**？該部分涵蓋 `if`、`switch`、`for`、`while`，是 Java 考試中程序邏輯的核心。