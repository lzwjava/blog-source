---
audio: false
generated: true
lang: hant
layout: post
title: Java 中的功能性介面
translated: true
---

`java.util.function` 套件在 Java 中提供了一組功能性介面，旨在支持功能式編程，自 Java 8 引入。這些介面各自有一個抽象方法，使其與 lambda 表達式和方法引用相容。本回應解釋如何使用這個套件中最常見的功能性介面——`Function<T, R>`、`Predicate<T>`、`Consumer<T>` 和 `Supplier<T>`——並附上實際範例。

---

### 什麼是功能性介面？
功能性介面是一個僅有一個抽象方法的介面。`java.util.function` 套件提供了預定義的功能性介面，用於常見任務，因此你不需要自己創建。這些介面廣泛用於 lambda 表達式、方法引用和 Stream API，以編寫簡潔且表達力強的代碼。

以下是如何使用這些關鍵介面：

---

### 1. `Function<T, R>`：轉換輸入為輸出
`Function<T, R>` 介面表示一個函數，接受類型為 `T` 的輸入並產生類型為 `R` 的輸出。其抽象方法是 `apply`。

#### 範例：獲取字串的長度
```java
import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        Function<String, Integer> stringLength = s -> s.length();
        System.out.println(stringLength.apply("Hello")); // 輸出: 5
    }
}
```
- **說明**：lambda 表達式 `s -> s.length()` 定義了一個 `Function`，接受一個 `String` (`T`) 並返回一個 `Integer` (`R`)。`apply` 方法執行這個邏輯。

---

### 2. `Predicate<T>`：測試條件
`Predicate<T>` 介面表示一個布爾值函數，接受類型為 `T` 的輸入。其抽象方法是 `test`。

#### 範例：檢查數字是否為偶數
```java
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        Predicate<Integer> isEven = n -> n % 2 == 0;
        System.out.println(isEven.test(4)); // 輸出: true
        System.out.println(isEven.test(5)); // 輸出: false
    }
}
```
- **說明**：lambda `n -> n % 2 == 0` 定義了一個 `Predicate`，當輸入為偶數時返回 `true`。`test` 方法評估這個條件。

---

### 3. `Consumer<T>`：執行動作
`Consumer<T>` 介面表示一個操作，接受類型為 `T` 的輸入並不返回結果。其抽象方法是 `accept`。

#### 範例：打印字串
```java
import java.util.function.Consumer;

public class Main {
    public static void main(String[] args) {
        Consumer<String> printer = s -> System.out.println(s);
        printer.accept("Hello, World!"); // 輸出: Hello, World!
    }
}
```
- **說明**：lambda `s -> System.out.println(s)` 定義了一個 `Consumer`，打印其輸入。`accept` 方法執行這個動作。

---

### 4. `Supplier<T>`：生成結果
`Supplier<T>` 介面表示一個結果供應者，不接受輸入並返回類型為 `T` 的值。其抽象方法是 `get`。

#### 範例：生成隨機數
```java
import java.util.function.Supplier;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Supplier<Integer> randomInt = () -> new Random().nextInt(100);
        System.out.println(randomInt.get()); // 輸出一個 0 到 99 之間的隨機整數
    }
}
```
- **說明**：lambda `() -> new Random().nextInt(100)` 定義了一個 `Supplier`，生成一個隨機整數。`get` 方法獲取這個值。

---

### 使用功能性介面與流
這些介面在 Java Stream API 中表現出色，使數據處理更加簡潔。以下是範例，篩選、轉換並打印一組字串：

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

        Predicate<String> longerThanTwo = s -> s.length() > 2;       // 篩選長度大於 2 的字串
        Function<String, String> toUpperCase = s -> s.toUpperCase(); // 轉換為大寫
        Consumer<String> printer = s -> System.out.println(s);       // 打印每個結果

        strings.stream()
               .filter(longerThanTwo)   // 保留 "ccc" 和 "dddd"
               .map(toUpperCase)        // 轉換為 "CCC" 和 "DDDD"
               .forEach(printer);       // 輸出: CCC, DDDD (各自一行)
    }
}
```
- **說明**：
  - `filter` 使用一個 `Predicate` 保留長度大於 2 的字串。
  - `map` 使用一個 `Function` 將字串轉換為大寫。
  - `forEach` 使用一個 `Consumer` 打印每個結果。

#### 使用方法引用
你可以使用方法引用使其更加簡潔：
```java
strings.stream()
       .filter(s -> s.length() > 2)
       .map(String::toUpperCase)      // 方法引用用於 Function
       .forEach(System.out::println); // 方法引用用於 Consumer
```

---

### 組合功能性介面
某些介面允許組合以進行更複雜的操作：
- **函數組合**：使用 `andThen` 或 `compose`。
  ```java
  Function<String, Integer> toLength = s -> s.length();
  Function<Integer, String> toString = i -> "Length is " + i;
  Function<String, String> combined = toLength.andThen(toString);
  System.out.println(combined.apply("Hello")); // 輸出: Length is 5
  ```
- **條件組合**：使用 `and`、`or` 或 `negate`。
  ```java
  Predicate<String> isLong = s -> s.length() > 5;
  Predicate<String> startsWithA = s -> s.startsWith("A");
  Predicate<String> isLongAndStartsWithA = isLong.and(startsWithA);
  System.out.println(isLongAndStartsWithA.test("Avocado")); // 輸出: true
  ```

---

### 總結
以下是何時及如何使用這些介面：
- **`Function<T, R>`**：將輸入轉換為輸出（例如 `apply`）。
- **`Predicate<T>`**：測試條件（例如 `test`）。
- **`Consumer<T>`**：對輸入執行動作（例如 `accept`）。
- **`Supplier<T>`**：不接受輸入生成值（例如 `get`）。
- **與流**：結合以進行強大的數據處理。
- **組合**：鏈接或組合以進行複雜邏輯。

你可以使用 lambda 表達式（例如 `s -> s.length()`）或方法引用（例如 `String::toUpperCase`）來實現這些介面。它們使 Java 代碼更加簡潔、可讀和可重用，特別是與 Stream API 一起使用。