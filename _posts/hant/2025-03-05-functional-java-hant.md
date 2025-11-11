---
audio: false
generated: true
lang: hant
layout: post
title: Java 中的函數式介面
translated: true
type: note
---

Java 中的 `java.util.function` 套件提供了一系列函數式介面，旨在支援 Java 8 引入的函數式程式設計。這些介面各自只有一個抽象方法，因此能與 lambda 表達式和方法參考相容。本文將透過實際範例，說明如何使用此套件中最常見的幾個函數式介面——`Function<T, R>`、`Predicate<T>`、`Consumer<T>` 和 `Supplier<T>`。

---

### 什麼是函數式介面？
函數式介面是指僅有一個抽象方法的介面。`java.util.function` 套件提供了預先定義的函數式介面，用於處理常見任務，因此您無需自行創建。這些介面常與 lambda 表達式、方法參考及 Stream API 搭配使用，讓程式碼更簡潔且具表達力。

以下將介紹幾個關鍵介面的使用方法：

---

### 1. `Function<T, R>`：將輸入轉換為輸出
`Function<T, R>` 介面代表一個函數，它接受類型 `T` 的輸入並產生類型 `R` 的輸出。其抽象方法為 `apply`。

#### 範例：取得字串長度
```java
import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        Function<String, Integer> stringLength = s -> s.length();
        System.out.println(stringLength.apply("Hello")); // 輸出：5
    }
}
```
- **說明**：lambda 表達式 `s -> s.length()` 定義了一個 `Function`，它接受一個 `String`（`T`）並回傳一個 `Integer`（`R`）。`apply` 方法會執行此邏輯。

---

### 2. `Predicate<T>`：測試條件
`Predicate<T>` 介面代表一個布林值函數，它接受類型 `T` 的輸入。其抽象方法為 `test`。

#### 範例：檢查數字是否為偶數
```java
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        Predicate<Integer> isEven = n -> n % 2 == 0;
        System.out.println(isEven.test(4)); // 輸出：true
        System.out.println(isEven.test(5)); // 輸出：false
    }
}
```
- **說明**：lambda 表達式 `n -> n % 2 == 0` 定義了一個 `Predicate`，當輸入為偶數時回傳 `true`。`test` 方法會評估此條件。

---

### 3. `Consumer<T>`：執行操作
`Consumer<T>` 介面代表一個操作，它接受類型 `T` 的輸入且不回傳結果。其抽象方法為 `accept`。

#### 範例：印出字串
```java
import java.util.function.Consumer;

public class Main {
    public static void main(String[] args) {
        Consumer<String> printer = s -> System.out.println(s);
        printer.accept("Hello, World!"); // 輸出：Hello, World!
    }
}
```
- **說明**：lambda 表達式 `s -> System.out.println(s)` 定義了一個 `Consumer`，它會印出其輸入。`accept` 方法會執行此操作。

---

### 4. `Supplier<T>`：產生結果
`Supplier<T>` 介面代表一個結果的供應者，它不接受輸入，但會回傳類型 `T` 的值。其抽象方法為 `get`。

#### 範例：產生隨機數字
```java
import java.util.function.Supplier;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Supplier<Integer> randomInt = () -> new Random().nextInt(100);
        System.out.println(randomInt.get()); // 輸出一個介於 0 到 99 的隨機整數
    }
}
```
- **說明**：lambda 表達式 `() -> new Random().nextInt(100)` 定義了一個 `Supplier`，它會產生一個隨機整數。`get` 方法會取得該值。

---

### 在 Stream 中使用函數式介面
這些介面在 Java Stream API 中尤其強大，能讓資料處理更簡潔。以下是一個範例，展示如何過濾、轉換並印出字串列表：

#### 範例：處理字串列表
```java
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        List<String> strings = Arrays.asList("a", "bb", "ccc", "dddd");

        Predicate<String> longerThanTwo = s -> s.length() > 2;       // 過濾長度大於 2 的字串
        Function<String, String> toUpperCase = s -> s.toUpperCase(); // 轉換為大寫
        Consumer<String> printer = s -> System.out.println(s);       // 印出每個結果

        strings.stream()
               .filter(longerThanTwo)   // 保留 "ccc" 和 "dddd"
               .map(toUpperCase)        // 轉換為 "CCC" 和 "DDDD"
               .forEach(printer);       // 輸出：CCC, DDDD（各佔一行）
    }
}
```
- **說明**：
  - `filter` 使用 `Predicate` 來保留長度大於 2 的字串。
  - `map` 使用 `Function` 將字串轉換為大寫。
  - `forEach` 使用 `Consumer` 來印出每個結果。

#### 使用方法參考
您還可以使用方法參考讓程式碼更簡潔：
```java
strings.stream()
       .filter(s -> s.length() > 2)
       .map(String::toUpperCase)      // Function 的方法參考
       .forEach(System.out::println); // Consumer 的方法參考
```

---

### 組合函數式介面
某些介面允許組合，以實現更複雜的操作：
- **Function 組合**：使用 `andThen` 或 `compose`。
  ```java
  Function<String, Integer> toLength = s -> s.length();
  Function<Integer, String> toString = i -> "Length is " + i;
  Function<String, String> combined = toLength.andThen(toString);
  System.out.println(combined.apply("Hello")); // 輸出：Length is 5
  ```
- **Predicate 組合**：使用 `and`、`or` 或 `negate`。
  ```java
  Predicate<String> isLong = s -> s.length() > 5;
  Predicate<String> startsWithA = s -> s.startsWith("A");
  Predicate<String> isLongAndStartsWithA = isLong.and(startsWithA);
  System.out.println(isLongAndStartsWithA.test("Avocado")); // 輸出：true
  ```

---

### 總結
以下是這些介面的使用時機與方法：
- **`Function<T, R>`**：將輸入轉換為輸出（例如 `apply`）。
- **`Predicate<T>`**：測試條件（例如 `test`）。
- **`Consumer<T>`**：對輸入執行操作（例如 `accept`）。
- **`Supplier<T>`**：在不接受輸入的情況下產生值（例如 `get`）。
- **與 Stream 搭配**：結合它們以實現強大的資料處理。
- **組合功能**：透過鏈結或組合來實現複雜邏輯。

您可以使用 lambda 表達式（例如 `s -> s.length()`）或方法參考（例如 `String::toUpperCase`）來實現這些介面。它們讓 Java 能夠以函數式風格編程，使程式碼更簡潔、易讀且可重複使用，尤其是在與 Stream API 搭配時。