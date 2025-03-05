---
audio: false
generated: true
lang: zh
layout: post
title: Java 中的 Stream API
translated: true
---

要在 Java 中使用 `java.util.stream`，可以利用 Java 8 引入的 Stream API 以函数式和声明式的方式处理数据集合。流允许你高效且简洁地对元素序列（如列表或数组）执行操作，如过滤、映射和减少。下面，我将通过一个具体的例子来解释如何使用 `java.util.stream`：从整数列表中找到大于 10 的偶数的平均值。这将演示关键的流操作和概念。

---

### **`java.util.stream` 概述**
`java.util.stream` 包提供了 `Stream` 接口及相关类（如 `IntStream`、`DoubleStream` 等）来处理数据。流是支持在管道中执行操作的元素序列。这些操作包括：
- **中间操作**：转换或过滤流（例如 `filter`、`map`），返回一个新的流。这些操作是懒惰的，只有在调用终端操作时才会执行。
- **终端操作**：生成结果或副作用（例如 `average`、`collect`），触发管道处理数据。

要使用流，通常：
1. 从数据源（例如列表）创建一个流。
2. 应用中间操作来转换或过滤数据。
3. 使用终端操作生成结果。

---

### **示例问题**
解决这个问题：给定一个 `List<Integer>`，计算所有大于 10 的偶数的平均值。如果没有这样的数字，返回 0.0。以下是使用 `java.util.stream` 实现的方法。

#### **逐步解决方案**
1. **创建流**
   - 从一个 `List<Integer>` 开始（例如 `List.of(1, 2, 12, 15, 20, 25, 30)`）。
   - 使用 `stream()` 方法创建一个 `Stream<Integer>`：
     ```java
     list.stream()
     ```

2. **过滤流**
   - 使用 `filter` 方法保留仅大于 10 的偶数。
   - `filter` 方法接受一个 `Predicate`（返回布尔值的函数）作为 lambda 表达式：
     ```java
     .filter(number -> number % 2 == 0 && number > 10)
     ```
     - `number % 2 == 0` 检查一个数是否为偶数。
     - `number > 10` 确保数字大于 10。
     - 对于示例列表 `[1, 2, 12, 15, 20, 25, 30]`，这将保留 `[12, 20, 30]`。

3. **转换为 `IntStream`**
   - 由于 `average()` 可用于原始流（如 `IntStream`），而不是 `Stream<Integer>`，使用 `mapToInt` 将 `Stream<Integer>` 转换为 `IntStream`：
     ```java
     .mapToInt(i -> i)
     ```
     - `i -> i` 将每个 `Integer` 解包为 `int`。或者，可以使用 `Integer::intValue`。
     - 这将得到一个 `IntStream` 的 `[12, 20, 30]`。

4. **计算平均值**
   - 在 `IntStream` 上使用 `average()` 方法，它返回一个 `OptionalDouble`（因为流可能为空）：
     ```java
     .average()
     ```
     - 对于 `[12, 20, 30]`，这将计算 `(12 + 20 + 30) / 3 = 20.666...`。
     - 如果流为空，它将返回一个空的 `OptionalDouble`。

5. **处理空情况**
   - 在 `OptionalDouble` 上使用 `orElse(0.0)` 返回 0.0，如果没有数字满足过滤条件：
     ```java
     .orElse(0.0)
     ```
     - 对于 `[12, 20, 30]`，这将返回 `20.666...`。
     - 对于列表 `[1, 3, 5]`（没有大于 10 的偶数），它将返回 `0.0`。

#### **完整代码**
以下是完整的解决方案作为一个方法：
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
        // 测试用例
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

### **`java.util.stream` 演示的关键特性**
- **链式操作**：操作以流畅的方式链接（例如 `.filter().mapToInt().average()`）。
- **懒惰性**：中间操作（如 `filter` 和 `mapToInt`）只有在调用终端操作（如 `average`）时才会执行。
- **原始流**：`IntStream` 提供了针对数值操作的方法（如 `average()`），避免了装箱开销。
- **可选处理**：`OptionalDouble` 处理没有结果的情况，`orElse` 提供默认值。

---

### **替代方法**
也可以使用 `Collectors` 类：
```java
import java.util.stream.Collectors;

double average = list.stream()
                     .filter(number -> number % 2 == 0 && number > 10)
                     .collect(Collectors.averagingInt(i -> i));
```
- 这直接返回一个 `Double`，并且对于空流返回 `0.0`。然而，`mapToInt().average()` 对于这个简单的情况更直接，并且与原始流使用一致。

---

### **何时使用流**
- 使用 `java.util.stream` 编写简洁、可读的代码来处理集合。
- 对于大数据集，考虑使用 `parallelStream()` 而不是 `stream()` 以利用并行性，尽管对于小列表来说这会带来开销。

---

这个例子展示了如何使用 `java.util.stream` 解决实际问题。你可以将这些步骤（创建流、过滤、映射和减少）应用到其他场景中！