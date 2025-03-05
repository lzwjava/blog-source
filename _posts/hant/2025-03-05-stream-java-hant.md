---
audio: false
generated: true
lang: hant
layout: post
title: Java 中的 Stream API
translated: true
---

要在 Java 中使用 `java.util.stream`，可以利用 Java 8 引入的 Stream API 以功能性和聲明性的方式處理數據集合。流允許您高效且簡潔地對元素序列（如列表或數組）執行過濾、映射和減少等操作。以下，我將通過一個具體的例子來解釋如何使用 `java.util.stream`：從整數列表中找出大於 10 的偶數的平均值。這將展示關鍵的流操作和概念。

---

### **`java.util.stream` 概述**
`java.util.stream` 包提供了 `Stream` 接口及相關類（如 `IntStream`、`DoubleStream` 等）來處理數據。流是一個支持管道執行操作的元素序列。這些操作包括：
- **中間操作**：轉換或過濾流（例如 `filter`、`map`），返回一個新的流。這些操作是懶惰的，只有在調用終端操作時才會執行。
- **終端操作**：產生結果或副作用（例如 `average`、`collect`），觸發管道處理數據。

要使用流，通常：
1. 從數據源（例如列表）創建一個流。
2. 使用中間操作轉換或過濾數據。
3. 使用終端操作產生結果。

---

### **示例問題**
讓我們解決這個問題：給定一個 `List<Integer>`，計算所有大於 10 的偶數的平均值。如果沒有這樣的數字，返回 0.0。以下是使用 `java.util.stream` 來完成的方法。

#### **逐步解決方案**
1. **創建一個流**
   - 從一個 `List<Integer>`（例如 `List.of(1, 2, 12, 15, 20, 25, 30)`）開始。
   - 使用 `stream()` 方法創建一個 `Stream<Integer>`：
     ```java
     list.stream()
     ```

2. **過濾流**
   - 使用 `filter` 方法保留僅大於 10 的偶數。
   - `filter` 方法接受一個 `Predicate`（返回布爾值的函數）作為 Lambda 表達式：
     ```java
     .filter(number -> number % 2 == 0 && number > 10)
     ```
     - `number % 2 == 0` 檢查一個數是否為偶數。
     - `number > 10` 確保數字大於 10。
     - 對於列表 `[1, 2, 12, 15, 20, 25, 30]`，這將保留 `[12, 20, 30]`。

3. **轉換為 `IntStream`**
   - 由於 `average()` 可用於原始流（如 `IntStream`），而不是 `Stream<Integer>`，使用 `mapToInt` 將 `Stream<Integer>` 轉換為 `IntStream`：
     ```java
     .mapToInt(i -> i)
     ```
     - `i -> i` 將每個 `Integer` 解包為 `int`。或者，您可以使用 `Integer::intValue`。
     - 這將給出一個 `IntStream` 的 `[12, 20, 30]`。

4. **計算平均值**
   - 在 `IntStream` 上使用 `average()` 方法，它返回一個 `OptionalDouble`（因為流可能為空）：
     ```java
     .average()
     ```
     - 對於 `[12, 20, 30]`，這將計算 `(12 + 20 + 30) / 3 = 20.666...`。
     - 如果流為空，它將返回一個空的 `OptionalDouble`。

5. **處理空情況**
   - 在 `OptionalDouble` 上使用 `orElse(0.0)` 返回 0.0，如果沒有數字滿足過濾條件：
     ```java
     .orElse(0.0)
     ```
     - 對於 `[12, 20, 30]`，這將返回 `20.666...`。
     - 對於列表 `[1, 3, 5]`（沒有大於 10 的偶數），它將返回 `0.0`。

#### **完整代碼**
以下是完整的解決方案作為一個方法：
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
        // 測試用例
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

### **`java.util.stream` 示範的關鍵特性**
- **鏈接**：操作以流暢的風格鏈接（例如 `.filter().mapToInt().average()`）。
- **懶惰性**：中間操作（如 `filter` 和 `mapToInt`）僅在調用終端操作（`average`）時執行。
- **原始流**：`IntStream` 提供了針對數值操作的方法（如 `average()`），避免了裝箱開銷。
- **可選處理**：`OptionalDouble` 處理沒有結果的情況，`orElse` 提供一個默認值。

---

### **替代方法**
您也可以使用 `Collectors` 類：
```java
import java.util.stream.Collectors;

double average = list.stream()
                     .filter(number -> number % 2 == 0 && number > 10)
                     .collect(Collectors.averagingInt(i -> i));
```
- 這將直接返回一個 `Double`，並對空流返回 `0.0`。然而，`mapToInt().average()` 更直接，適合這個簡單的情況，並與原始流使用一致。

---

### **何時使用流**
- 使用 `java.util.stream` 來處理集合時，編寫簡潔、可讀的代碼。
- 對於大數據集，考慮使用 `parallelStream()` 而不是 `stream()` 來利用並行性，儘管對於小列表來說這是過度的，因為有開銷。

---

這個例子展示了如何使用 `java.util.stream` 來解決一個實際問題。您可以將這些步驟（創建流、過濾、映射和減少）應用到其他情況中！