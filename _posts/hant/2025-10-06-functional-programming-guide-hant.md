---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Java 函數式編程指南
translated: true
type: note
---

Java 自 Java 8 起引入了函數式程式設計原則，新增了 lambda 表達式、串流等特性，使程式碼更簡潔、可讀性更高且更具宣告性。本指南涵蓋從基礎到進階的概念，假設讀者已熟悉核心 Java。我們將使用 Java 8+ 語法，因為這些特性是從該版本開始引入的。範例將置於 Java 程式碼區塊中，方便複製使用。

## 1. Java 函數式程式設計簡介

函數式程式設計（FP）強調：
- **純函數**：無副作用（例如，無可變狀態變更）的函數。
- **不可變性**：資料一旦建立即不改變。
- **高階函數**：可接收或回傳其他函數的函數。
- **宣告式風格**：專注於「做什麼」而非「如何做」（例如，使用串流替代迴圈）。

Java 並非如 Haskell 般純函數式語言，而是將 FP 與其物件導向根源相融合。關鍵實現工具：
- Lambda 表達式（匿名函數）。
- 函數式介面（僅有一個抽象方法的介面）。
- 用於以函數式處理集合的 Streams API。

優點：減少樣板程式碼、更易實現平行處理、更好的可組合性。

## 2. Lambda 表達式

Lambda 是用於簡短、一次性實現的匿名函數。它們是 Java 中進入 FP 的入口。

### 基礎語法
Lambda 格式為：`(參數) -> { 主體 }`
- 單一參數時可省略括號。
- 單一表達式時可省略大括號（隱含回傳）。
- 通常可進行型別推斷，但也可明確指定型別。

```java
// 傳統匿名內部類
Runnable r = new Runnable() {
    @Override
    public void run() {
        System.out.println("Hello, World!");
    }
};

// Lambda 等效寫法
Runnable lambda = () -> System.out.println("Hello, World!");
lambda.run();
```

### 帶參數範例
```java
// 二元運算子範例
BinaryOperator<Integer> add = (a, b) -> a + b;
System.out.println(add.apply(2, 3)); // 5

// 多行主體
Comparator<String> comparator = (s1, s2) -> {
    int lenDiff = s1.length() - s2.length();
    return lenDiff != 0 ? lenDiff : s1.compareTo(s2);
};
```

### 捕獲變數（實質上最終）
Lambda 可存取外部變數，但變數必須是 **實質上最終**（未被重新賦值）。
```java
int threshold = 10;
Predicate<Integer> isHigh = x -> x > threshold; // 正確
// threshold = 20; // 錯誤：非實質上最終
```

## 3. 函數式介面

函數式介面僅有一個抽象方法（SAM - Single Abstract Method）。Java 在 `java.util.function` 中提供了內建介面。

### 內建範例
- `Predicate<T>`：`boolean test(T t)`
- `Function<T, R>`：`R apply(T t)`
- `Consumer<T>`：`void accept(T t)`
- `Supplier<T>`：`T get()`
- `BiFunction<T, U, R>` 等，用於兩個輸入。

自訂介面：
```java
@FunctionalInterface  // 可選，但建議使用
interface Transformer {
    String transform(String input);
}

Transformer upper = s -> s.toUpperCase();
System.out.println(upper.transform("java")); // JAVA
```

使用 `@FunctionalInterface` 來強制 SAM 規範。

### 預設與靜態方法
函數式介面可包含預設方法（Java 8+），例如 `Optional.orElse()`。
```java
default int compare(String a, String b) { ... } // 允許
static void utility() { ... } // 允許
```

## 4. 方法參考

為呼叫現有方法的 Lambda 提供簡寫語法。格式：`Class::method` 或 `instance::method`。

類型：
- 靜態方法：`Class::staticMethod`
- 特定類型的實例方法：`Class::instanceMethod`
- 任意物件的實例方法：`object::instanceMethod`
- 建構子：`Class::new`

範例：
```java
// Lambda：x -> System.out.println(x)
Consumer<String> printer = System.out::println;

// 靜態方法
Function<String, Integer> length = String::length;

// 實例方法
List<String> list = Arrays.asList("a", "b");
list.forEach(System.out::println); // 列印每個元素

// 建構子
Supplier<List<String>> listSupplier = ArrayList::new;
```

## 5. Streams API

串流以宣告式處理集合：建立 → 轉換 → 收集。採用惰性求值（中介操作直到終端操作才執行）。

### 建立串流
```java
import java.util.*;
import java.util.stream.*;

List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

// 從集合建立
Stream<String> stream = names.stream();

// 從陣列建立
String[] arr = {"x", "y"};
Stream<String> arrStream = Arrays.stream(arr);

// 無限串流
Stream<Integer> infinite = Stream.iterate(0, n -> n + 1);
```

### 中介操作（惰性）
可鏈式呼叫；直到終端操作才進行計算。
- `filter(Predicate)`：保留符合條件的元素。
- `map(Function)`：轉換每個元素。
- `flatMap(Function<? super T, ? extends Stream<? extends R>>)`：扁平化嵌套串流。
- `distinct()`、`sorted()`、`limit(n)`、`skip(n)`。

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
List<Integer> evensSquared = numbers.stream()
    .filter(n -> n % 2 == 0)
    .map(n -> n * n)
    .collect(Collectors.toList()); // [4, 16]
```

### 終端操作（急切）
觸發計算並回傳結果。
- `collect(Collector)`：收集為 list、set、map。
- `forEach(Consumer)`：副作用操作（盡可能避免）。
- `reduce()`：聚合（例如求和）。
- `anyMatch()`、`allMatch()`、`findFirst()`。

```java
// Reduce：求和
int sum = numbers.stream().reduce(0, Integer::sum); // 15

// 收集為 map
Map<String, Integer> nameLengths = Stream.of("Alice", "Bob")
    .collect(Collectors.toMap(s -> s, String::length)); // {Alice=5, Bob=3}

// 分組
Map<Integer, List<String>> byLength = names.stream()
    .collect(Collectors.groupingBy(String::length)); // {5=[Alice, Charlie], 3=[Bob]}
```

### 平行串流
用於平行處理：`parallelStream()` 或 `.parallel()`。請謹慎使用（除錯較困難）。
```java
long count = names.parallelStream().count(); // 3
```

## 6. Collectors

來自 `java.util.stream.Collectors`。用於建構複雜的歸約操作。

常見：
- `toList()`、`toSet()`、`toMap()`
- `joining()`：連接字串。
- `summingInt()`、`averagingDouble()`
- `groupingBy()`、`partitioningBy()`
- `collectingAndThen()`：後處理。

```java
// 自訂收集器：按長度取最大值
String longest = names.stream()
    .collect(Collectors.maxBy(Comparator.comparingInt(String::length)))
    .orElse(""); // "Charlie"

// 分割奇偶數
Map<Boolean, List<Integer>> partitions = numbers.stream()
    .collect(Collectors.partitioningBy(n -> n % 2 == 0));
```

## 7. Optional

透過封裝可能為 null 的值來避免 `NullPointerException`。鼓勵明確的 null 處理。

建立方式：
- `Optional.of(value)`：非 null 值。
- `Optional.ofNullable(value)`：null 值轉為 empty。
- `Optional.empty()`。

操作：
- `isPresent()`、`ifPresent(Consumer)`
- `orElse(default)`、`orElseThrow()`
- `map()`、`flatMap()` 用於鏈式呼叫。

```java
Optional<String> opt = Optional.ofNullable(getName()); // 假設可能回傳 null

String name = opt.orElse("Unknown");
opt.ifPresent(System.out::println);

String upper = opt.map(String::toUpperCase).orElse("DEFAULT");
```

串流常回傳 `Optional`（例如 `findFirst()`）。

## 8. 進階主題

### 可組合函數
使用 `Function.andThen()`、`Function.compose()` 進行鏈式呼叫。
```java
Function<String, Integer> len = String::length;
Function<Integer, String> toStr = i -> "Len: " + i;

Function<String, String> chain = len.andThen(toStr);
System.out.println(chain.apply("Java")); // Len: 4
```

### 遞迴與尾呼叫
Java 缺乏優化，但可使用 `Stream.iterate()` 進行迭代遞迴。

### 不可變性輔助工具
使用 `Collections.unmodifiableList()` 或 Guava/Immutable Collections 等函式庫（但 Java 10+ 已內建 `List.of()`）。

`List.of("a", "b")` 可建立不可變列表（Java 9+）。

### 模式匹配（Java 21+ 預覽/穩定版）
透過 switch 中的解構增強 FP。
```java
// 預覽功能；需使用 --enable-preview 啟用
String desc = switch (obj) {
    case Integer i -> "int: " + i;
    case String s -> "str: " + s.length();
    default -> "unknown";
};
```

### 虛擬執行緒（Java 21+）
FP 在輕量級執行緒的並行串流中表現出色。

## 9. 最佳實踐

- **偏好不可變性**：使用 final 欄位，避免變更集合。
- **避免副作用**：保持 lambda 純粹；僅在 `forEach` 或明確的 consumer 中產生副作用。
- **串流 vs. 迴圈**：為可讀性使用串流；為效能關鍵程式碼使用迴圈。
- **Null 處理**：優先使用 `Optional` 而非 null 檢查。
- **測試**：使用 lambda 輕鬆模擬函數式介面。
- **效能**：串流有開銷；使用平行處理前請先分析。
- **可讀性**：簡短 lambda 沒問題；複雜邏輯請提取為方法。

常見陷阱：
- 在 lambda 中修改外部狀態。
- 忘記終端操作（串流不會執行任何操作！）。
- 過度使用平行串流（並非總是更快）。

## 10. 範例：函數式管道

以函數式方式處理員工列表。

```java
import java.util.*;
import java.util.stream.Collectors;

class Employee {
    String name;
    int salary;
    Department dept;

    Employee(String name, int salary, Department dept) {
        this.name = name;
        this.salary = salary;
        this.dept = dept;
    }
}

enum Department { ENG, HR }

public class FunctionalExample {
    public static void main(String[] args) {
        List<Employee> employees = Arrays.asList(
            new Employee("Alice", 50000, Department.ENG),
            new Employee("Bob", 60000, Department.HR),
            new Employee("Charlie", 55000, Department.ENG)
        );

        // 高薪工程師的姓名，已排序
        List<String> result = employees.stream()
            .filter(e -> e.dept == Department.ENG)
            .filter(e -> e.salary > 52000)
            .map(Employee::getName)  // 假設有 getter
            .sorted()
            .collect(Collectors.toList());

        System.out.println(result); // [Charlie]
    }
}
```

## 結論

Lambda 與 FP 將 Java 從指令式轉變為表達式。從簡單替換開始（例如使用 `forEach` 替代迴圈），再逐步建構管道。在實際專案中練習以達精通。欲深入探索，可在 IDE 中進行實驗。

### 參考資料
- [Oracle Java 教程：Lambda 表達式](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html)
- [Baeldung：Java 8 函數式介面](https://www.baeldung.com/java-functional-interfaces)
- [Java Streams 指南](https://www.baeldung.com/java-8-streams)
- [Effective Java（第三版）- 關於 Lambda 的項目 42-45](https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/)