---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Scala 的集合庫在 Java 中
translated: true
---

要在 Java 中使用 `scala.collection` 包，可以利用 Scala 和 Java 之間的互操作性，因為兩種語言都編譯成 JVM 字節碼。這使得 Java 代碼可以調用 Scala 類，包括 `scala.collection` 包中的類，只要 Scala 圖書館對您的 Java 專案可見即可。以下是實現這一點的分步指南，並附有說明和示例。

---

### **步驟 1：在 Java 專案中包含 Scala 圖書館**
由於 `scala.collection` 包是 Scala 標準圖書館的一部分，您需要在 Java 專案的類路徑中包含 Scala 圖書館。這可以通過將 Scala 圖書館依賴項添加到您的構建工具來完成：

- **Maven**：
  將以下內容添加到您的 `pom.xml`：
  ```xml
  <dependency>
      <groupId>org.scala-lang</groupId>
      <artifactId>scala-library</artifactId>
      <version>2.13.12</version> <!-- 使用符合您需求的版本 -->
  </dependency>
  ```

- **Gradle**：
  將以下內容添加到您的 `build.gradle`：
  ```gradle
  implementation 'org.scala-lang:scala-library:2.13.12'
  ```

這樣可以確保 Scala 類，包括 `scala.collection` 中的類，對您的 Java 代碼可見。

---

### **步驟 2：導入 Scala 集合類**
一旦 Scala 圖書館在類路徑中，您可以在 Java 代碼中導入 `scala.collection` 包中的特定類。例如，要使用 Scala 的不可變 `List`，您可以導入：

```java
import scala.collection.immutable.List;
```

其他常用的集合包括：
- `scala.collection.immutable.Set`
- `scala.collection.immutable.Map`
- `scala.collection.mutable.Buffer`

請注意，Scala 集合有可變和不可變兩種變體，而 Java 的集合通常是可變的，除非包裝（例如，通過 `Collections.unmodifiableList`）。

---

### **步驟 3：在 Java 中創建 Scala 集合**
Scala 集合通常使用伴隨對象來創建，這些對象提供工廠方法，例如 `apply`。然而，由於 Java 不支持 Scala 的語法（例如 `List(1, 2, 3)`），您需要明確使用這些方法。此外，Scala 的 `apply` 方法對於像 `List` 這樣的集合來說，當從 Java 被調用時，期望一個 `Seq` 作為參數，因為 Scala 的可變參數是如何編譯的。

要橋接 Java 和 Scala 集合，請使用 Scala 提供的轉換工具，例如 `scala.collection.JavaConverters`（適用於 Scala 2.12 及更早版本）或 `scala.jdk.CollectionConverters`（適用於 Scala 2.13 及更晚版本）。以下是如何從 Java `List` 創建 Scala `List` 的方法：

#### **示例：創建 Scala List**
```java
import scala.collection.immutable.List;
import scala.collection.Seq;
import scala.jdk.CollectionConverters;
import java.util.Arrays;

public class ScalaCollectionExample {
    public static void main(String[] args) {
        // 創建 Java List
        java.util.List<Integer> javaList = Arrays.asList(1, 2, 3);

        // 將 Java List 轉換為 Scala Seq
        Seq<Integer> scalaSeq = CollectionConverters.asScala(javaList);

        // 使用伴隨對象創建 Scala List
        List<Integer> scalaList = List$.MODULE$.apply(scalaSeq);

        // 打印 Scala List
        System.out.println(scalaList); // 輸出: List(1, 2, 3)
    }
}
```

- **`CollectionConverters.asScala`**：將 Java `List` 轉換為 Scala `Seq`（在 Scala 2.13 中，這是 `mutable.Buffer`，是 `Seq` 的子類型）。
- **`List$.MODULE$`**：訪問 Scala 中 `List` 伴隨對象的單例實例，從而可以調用其 `apply` 方法。
- **`apply(scalaSeq)`**：從 `Seq` 創建一個新的不可變 Scala `List`。

---

### **步驟 4：使用 Scala 集合**
一旦在 Java 中擁有 Scala 集合，您可以使用其方法。然而，請注意 Scala 和 Java 之間的差異：
- **不可變性**：許多 Scala 集合（例如 `scala.collection.immutable.List`）是不可變的，這意味著方法返回新的集合，而不是修改原始集合。
- **類型擦除**：Scala 和 Java 都使用類型擦除，因此在檢索元素時可能需要對結果進行強制轉型。
- **函數式方法**：Scala 集合支持函數式操作，例如 `map`、`filter` 等，您可以使用 Java 8+ lambda 來使用。

#### **示例：訪問元素**
```java
// 获取第一个元素
Integer head = (Integer) scalaList.head();
System.out.println("Head: " + head); // 輸出: Head: 1

// 获取尾部（除了頭部之外的所有内容）
List<Integer> tail = scalaList.tail();
System.out.println("Tail: " + tail); // 輸出: Tail: List(2, 3)
```

#### **示例：對 Scala List 進行映射**
使用 lambda 將每個元素加倍：
```java
import scala.Function1;

Function1<Integer, Integer> doubler = x -> x * 2;
List<Integer> doubledList = scalaList.map(doubler);
System.out.println("Doubled: " + doubledList); // 輸出: Doubled: List(2, 4, 6)
```

這裡，`Function1` 是一個表示具有一個參數的函數的 Scala 接口，與 Java 的 lambda 語法相對應。

---

### **關鍵考量**
- **類型安全**：Scala 集合是參數化的，但由於類型擦除，方法返回類型可能會顯示為 `Object`。根據需要進行轉型（例如，`(Integer) scalaList.head()`）。
- **性能**：跨越 Java-Scala 邊界會引入一些開銷，但通常是微不足道的。
- **範式轉變**：Scala 集合強調不可變性和函數式編程，這可能與 Java 的命令式風格不同。例如，您不能“添加”到不可變的 `List`——您創建一個新的（例如，使用 `:+` 附加，這將返回一個新的 `List`）。
- **版本兼容性**：確保 Scala 圖書館版本符合您的需求。對於 Scala 2.13+，使用 `scala.jdk.CollectionConverters`；對於 2.12 或更早版本，使用 `scala.collection.JavaConverters`。

---

### **總結**
您可以通過以下方式在 Java 中使用 `scala.collection` 包：
1. 將 Scala 圖書館添加到專案的類路徑（例如，通過 Maven 或 Gradle）。
2. 導入所需的 Scala 集合類（例如 `scala.collection.immutable.List`）。
3. 使用伴隨對象（例如 `List$.MODULE$.apply`）創建 Scala 集合，並使用 `CollectionConverters` 將 Java 集合轉換為 Scala `Seq`。
4. 使用 Scala 方法操作集合，根據需要使用轉型和 lambda。

這種方法允許您在 Java 生態系統中利用 Scala 的強大集合圖書館，例如其不可變數據結構或函數式操作。