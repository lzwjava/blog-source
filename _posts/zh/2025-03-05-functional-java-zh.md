---
audio: false
generated: true
lang: zh
layout: post
title: 函数式接口
translated: true
---

`java.util.function` 包在 Java 中提供了一组功能接口，旨在支持功能编程，自 Java 8 引入。这些接口各自有一个抽象方法，使其与 lambda 表达式和方法引用兼容。本文将解释如何使用该包中最常见的功能接口——`Function<T, R>`、`Predicate<T>`、`Consumer<T>` 和 `Supplier<T>`——并附有实用示例。

---

### 什么是功能接口？
功能接口是一个具有单个抽象方法的接口。`java.util.function` 包为常见任务提供了预定义的功能接口，因此您不需要创建自己的。这些接口广泛用于与 lambda 表达式、方法引用和 Stream API 一起编写简洁和表达性强的代码。

以下是如何使用关键接口：

---

### 1. `Function<T, R>`：将输入转换为输出
`Function<T, R>` 接口表示一个接受类型 `T` 输入并生成类型 `R` 输出的函数。其抽象方法是 `apply`。

#### 示例：获取字符串的长度
```java
import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        Function<String, Integer> stringLength = s -> s.length();
        System.out.println(stringLength.apply("Hello")); // 输出: 5
    }
}
```
- **解释**：lambda 表达式 `s -> s.length()` 定义了一个 `Function`，它接受一个 `String` (`T`) 并返回一个 `Integer` (`R`)。`apply` 方法执行此逻辑。

---

### 2. `Predicate<T>`：测试条件
`Predicate<T>` 接口表示一个接受类型 `T` 输入并返回布尔值的函数。其抽象方法是 `test`。

#### 示例：检查一个数是否为偶数
```java
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        Predicate<Integer> isEven = n -> n % 2 == 0;
        System.out.println(isEven.test(4)); // 输出: true
        System.out.println(isEven.test(5)); // 输出: false
    }
}
```
- **解释**：lambda `n -> n % 2 == 0` 定义了一个 `Predicate`，如果输入为偶数则返回 `true`。`test` 方法评估此条件。

---

### 3. `Consumer<T>`：执行操作
`Consumer<T>` 接口表示一个接受类型 `T` 输入并不返回结果的操作。其抽象方法是 `accept`。

#### 示例：打印字符串
```java
import java.util.function.Consumer;

public class Main {
    public static void main(String[] args) {
        Consumer<String> printer = s -> System.out.println(s);
        printer.accept("Hello, World!"); // 输出: Hello, World!
    }
}
```
- **解释**：lambda `s -> System.out.println(s)` 定义了一个 `Consumer`，它打印其输入。`accept` 方法执行操作。

---

### 4. `Supplier<T>`：生成结果
`Supplier<T>` 接口表示一个结果供应商，不接受输入并返回类型 `T` 的值。其抽象方法是 `get`。

#### 示例：生成随机数
```java
import java.util.function.Supplier;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Supplier<Integer> randomInt = () -> new Random().nextInt(100);
        System.out.println(randomInt.get()); // 输出一个 0 到 99 之间的随机整数
    }
}
```
- **解释**：lambda `() -> new Random().nextInt(100)` 定义了一个 `Supplier`，它生成一个随机整数。`get` 方法检索值。

---

### 使用功能接口与流
这些接口在 Java Stream API 中表现出色，使数据处理更加简洁。以下是一个过滤、转换和打印字符串列表的示例：

#### 示例：处理字符串列表
```java
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        List<String> strings = Arrays.asList("a", "bb", "ccc", "dddd");

        Predicate<String> longerThanTwo = s -> s.length() > 2;       // 过滤长度大于 2 的字符串
        Function<String, String> toUpperCase = s -> s.toUpperCase(); // 转换为大写
        Consumer<String> printer = s -> System.out.println(s);       // 打印每个结果

        strings.stream()
               .filter(longerThanTwo)   // 保留 "ccc" 和 "dddd"
               .map(toUpperCase)        // 转换为 "CCC" 和 "DDDD"
               .forEach(printer);       // 输出: CCC, DDDD (每行一个)
    }
}
```
- **解释**：
  - `filter` 使用 `Predicate` 保留长度大于 2 的字符串。
  - `map` 使用 `Function` 将字符串转换为大写。
  - `forEach` 使用 `Consumer` 打印每个结果。

#### 使用方法引用
您可以使用方法引用使其更短：
```java
strings.stream()
       .filter(s -> s.length() > 2)
       .map(String::toUpperCase)      // Function 的方法引用
       .forEach(System.out::println); // Consumer 的方法引用
```

---

### 组合功能接口
某些接口允许组合以进行更复杂的操作：
- **函数组合**：使用 `andThen` 或 `compose`。
  ```java
  Function<String, Integer> toLength = s -> s.length();
  Function<Integer, String> toString = i -> "Length is " + i;
  Function<String, String> combined = toLength.andThen(toString);
  System.out.println(combined.apply("Hello")); // 输出: Length is 5
  ```
- **谓词组合**：使用 `and`、`or` 或 `negate`。
  ```java
  Predicate<String> isLong = s -> s.length() > 5;
  Predicate<String> startsWithA = s -> s.startsWith("A");
  Predicate<String> isLongAndStartsWithA = isLong.and(startsWithA);
  System.out.println(isLongAndStartsWithA.test("Avocado")); // 输出: true
  ```

---

### 总结
以下是何时以及如何使用这些接口：
- **`Function<T, R>`**：将输入转换为输出（例如，`apply`）。
- **`Predicate<T>`**：测试条件（例如，`test`）。
- **`Consumer<T>`**：对输入执行操作（例如，`accept`）。
- **`Supplier<T>`**：不接受输入生成值（例如，`get`）。
- **与流**：将它们结合以进行强大的数据处理。
- **组合**：链接或组合以进行复杂逻辑。

您可以使用 lambda 表达式（例如，`s -> s.length()`）或方法引用（例如，`String::toUpperCase`）实现这些接口。它们使 Java 中的函数式编程风格更加简洁、可读和可重用，特别是与 Stream API 一起使用。