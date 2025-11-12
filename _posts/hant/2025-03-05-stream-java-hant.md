---
audio: false
generated: true
lang: hant
layout: post
title: Java 串流 API
translated: true
type: note
---

要使用 Java 中的 `java.util.stream`，您可以利用 Java 8 引入的 Stream API，以函數式和宣告式的方式處理資料集合。Stream 能讓您高效簡潔地對元素序列（例如列表或陣列）執行過濾、映射和歸約等操作。下面我將透過具體範例說明如何使用 `java.util.stream`：從整數列表中找出大於 10 的偶數的平均值。這將展示串流操作的關鍵概念與步驟。

---

### **`java.util.stream` 概覽**
`java.util.stream` 套件提供 `Stream` 介面及相關類別（如 `IntStream`、`DoubleStream` 等）來處理資料。串流是一個支援管道操作的元素序列，這些操作分為兩類：
- **中介操作**：轉換或過濾串流（例如 `filter`、`map`），傳回新串流。這類操作採用惰性求值，僅在終端操作觸發時執行。
- **終端操作**：產生結果或副作用（例如 `average`、`collect`），觸發資料管道的處理。

使用串流的典型步驟如下：
1. 從資料來源（例如列表）建立串流。
2. 套用中介操作來轉換或過濾資料。
3. 使用終端操作產生結果。

---

### **問題範例**
我們來解決這個問題：給定一個 `List<Integer>`，計算所有大於 10 的偶數的平均值。若無符合條件的數字，則傳回 0.0。以下是使用 `java.util.stream` 的實現方法。

#### **逐步解決方案**
1. **建立串流**
   - 從 `List<Integer>` 開始（例如 `List.of(1, 2, 12, 15, 20, 25, 30)`）。
   - 使用 `stream()` 方法建立 `Stream<Integer>`：
     ```java
     list.stream()
     ```

2. **過濾串流**
   - 使用 `filter` 方法僅保留偶數且大於 10 的數字。
   - `filter` 方法接受一個 `Predicate`（傳回布林值的函式）作為 lambda 表達式：
     ```java
     .filter(number -> number % 2 == 0 && number > 10)
     ```
     - `number % 2 == 0` 檢查數字是否為偶數。
     - `number > 10` 確保數字大於 10。
     - 對於範例列表 `[1, 2, 12, 15, 20, 25, 30]`，此操作將保留 `[12, 20, 30]`。

3. **轉換為 `IntStream`**
   - 由於 `average()` 方法僅在基本型別串流（如 `IntStream`）上提供，而非 `Stream<Integer>`，因此需使用 `mapToInt` 將 `Stream<Integer>` 轉換為 `IntStream`：
     ```java
     .mapToInt(i -> i)
     ```
     - `i -> i` 將每個 `Integer` 拆箱為 `int`。亦可使用 `Integer::intValue`。
     - 此操作產生 `[12, 20, 30]` 的 `IntStream`。

4. **計算平均值**
   - 在 `IntStream` 上使用 `average()` 方法，該方法傳回 `OptionalDouble`（因為串流可能為空）：
     ```java
     .average()
     ```
     - 對於 `[12, 20, 30]`，計算結果為 `(12 + 20 + 30) / 3 = 20.666...`。
     - 若串流為空，則傳回空的 `OptionalDouble`。

5. **處理空值情況**
   - 在 `OptionalDouble` 上使用 `orElse(0.0)`，若無數字符合過濾條件則傳回 0.0：
     ```java
     .orElse(0.0)
     ```
     - 對於 `[12, 20, 30]`，傳回 `20.666...`。
     - 對於像 `[1, 3, 5]` 這樣的列表（無大於 10 的偶數），則傳回 `0.0`。

#### **完整程式碼**
以下是作為方法的完整解決方案：
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
        // 測試案例
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

### **展示的 `java.util.stream` 關鍵特性**
- **鏈式操作**：以流暢風格鏈接操作（例如 `.filter().mapToInt().average()`）。
- **惰性求值**：中介操作（如 `filter` 和 `mapToInt`）僅在終端操作（`average`）呼叫時執行。
- **基本型別串流**：`IntStream` 提供如 `average()` 等專為數值操作設計的方法，避免裝箱開銷。
- **Optional 處理**：`OptionalDouble` 處理無結果的情況，並透過 `orElse` 提供預設值。

---

### **替代方案**
您也可以使用 `Collectors` 類別：
```java
import java.util.stream.Collectors;

double average = list.stream()
                     .filter(number -> number % 2 == 0 && number > 10)
                     .collect(Collectors.averagingInt(i -> i));
```
- 此方法直接傳回 `Double`，並在串流為空時傳回 `0.0`。但在這種簡單情況下，使用 `mapToInt().average()` 更為直接，且符合基本型別串流的使用方式。

---

### **何時使用串流**
- 在處理集合時，使用 `java.util.stream` 可撰寫簡潔易讀的程式碼。
- 對於大型資料集，可考慮使用 `parallelStream()` 而非 `stream()` 以利用平行處理，但對於小型列表而言，由於額外開銷，此舉可能過度複雜。

---

此範例展示了如何使用 `java.util.stream` 解決實際問題。您可以根據需求調整這些步驟——建立串流、過濾、映射和歸約——以應用於其他情境！