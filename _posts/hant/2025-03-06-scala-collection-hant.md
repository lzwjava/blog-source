---
audio: false
generated: true
lang: hant
layout: post
title: 在 Java 中使用 Scala 集合庫
translated: true
type: note
---

若要在 Java 中使用 `scala.collection` 套件，您可以利用 Scala 與 Java 之間的互通性，因為這兩種語言都會編譯為 JVM 位元組碼。這使得 Java 程式碼能夠呼叫 Scala 類別，包括 `scala.collection` 套件中的類別，前提是您的 Java 專案能夠存取 Scala 函式庫。以下是如何實現此操作的逐步指南，包含詳細說明與範例。

---

### **步驟 1：在 Java 專案中包含 Scala 函式庫**
由於 `scala.collection` 套件是 Scala 標準函式庫的一部分，您需要將 Scala 函式庫加入 Java 專案的 classpath 中。這可以透過在建置工具中加入 Scala 函式庫相依性來實現：

- **Maven**：
  在 `pom.xml` 中加入以下內容：
  ```xml
  <dependency>
      <groupId>org.scala-lang</groupId>
      <artifactId>scala-library</artifactId>
      <version>2.13.12</version> <!-- 請使用符合您需求的版本 -->
  </dependency>
  ```

- **Gradle**：
  在 `build.gradle` 中加入：
  ```gradle
  implementation 'org.scala-lang:scala-library:2.13.12'
  ```

這確保了 Scala 類別（包括 `scala.collection` 中的類別）可供您的 Java 程式碼使用。

---

### **步驟 2：匯入 Scala 集合類別**
一旦 Scala 函式庫加入 classpath，您就可以在 Java 程式碼中從 `scala.collection` 套件匯入特定類別。例如，要使用 Scala 的不可變 `List`，您可以匯入：

```java
import scala.collection.immutable.List;
```

其他常用的集合包括：
- `scala.collection.immutable.Set`
- `scala.collection.immutable.Map`
- `scala.collection.mutable.Buffer`

請注意，Scala 集合分為可變與不可變兩種變體，這與 Java 的集合不同（Java 集合通常為可變，除非經過封裝，例如透過 `Collections.unmodifiableList`）。

---

### **步驟 3：在 Java 中建立 Scala 集合**
Scala 集合通常透過伴生物件（companion object）建立，這些物件提供了工廠方法，例如 `apply`。然而，由於 Java 不直接支援 Scala 的語法（例如 `List(1, 2, 3)`），您需要明確地使用這些方法。此外，當從 Java 呼叫時，Scala 集合（如 `List`）的 `apply` 方法需要一個 `Seq` 作為參數，這是因為 Scala 的可變參數編譯方式所致。

為了橋接 Java 與 Scala 集合，請使用 Scala 提供的轉換工具，例如 `scala.collection.JavaConverters`（適用於 Scala 2.12 及更早版本）或 `scala.jdk.CollectionConverters`（適用於 Scala 2.13 及更新版本）。以下是如何從 Java `List` 建立 Scala `List` 的範例：

#### **範例：建立 Scala List**
```java
import scala.collection.immutable.List;
import scala.collection.Seq;
import scala.jdk.CollectionConverters;
import java.util.Arrays;

public class ScalaCollectionExample {
    public static void main(String[] args) {
        // 建立 Java List
        java.util.List<Integer> javaList = Arrays.asList(1, 2, 3);

        // 將 Java List 轉換為 Scala Seq
        Seq<Integer> scalaSeq = CollectionConverters.asScala(javaList);

        // 使用伴生物件建立 Scala List
        List<Integer> scalaList = List$.MODULE$.apply(scalaSeq);

        // 輸出 Scala List
        System.out.println(scalaList); // 輸出：List(1, 2, 3)
    }
}
```

- **`CollectionConverters.asScala`**：將 Java `List` 轉換為 Scala `Seq`（在 Scala 2.13 中具體為 `mutable.Buffer`，它是 `Seq` 的子類型）。
- **`List$.MODULE$`**：存取 Scala 中 `List` 伴生物件的單例實例，讓您能夠呼叫其 `apply` 方法。
- **`apply(scalaSeq)`**：從 `Seq` 建立一個新的不可變 Scala `List`。

---

### **步驟 4：使用 Scala 集合**
一旦您在 Java 中擁有了 Scala 集合，就可以使用其方法。但請注意 Scala 與 Java 之間的差異：
- **不可變性**：許多 Scala 集合（例如 `scala.collection.immutable.List`）是不可變的，這意味著方法會回傳新的集合，而不是修改原始集合。
- **類型擦除**：Scala 與 Java 都使用類型擦除，因此在擷取元素時可能需要進行類型轉換。
- **函數式方法**：Scala 集合支援函數式操作，例如 `map`、`filter` 等，您可以搭配 Java 8+ 的 lambda 表達式使用。

#### **範例：存取元素**
```java
// 取得第一個元素
Integer head = (Integer) scalaList.head();
System.out.println("Head: " + head); // 輸出：Head: 1

// 取得尾部（除了首元素外的所有元素）
List<Integer> tail = scalaList.tail();
System.out.println("Tail: " + tail); // 輸出：Tail: List(2, 3)
```

#### **範例：對 Scala List 進行映射**
使用 lambda 將每個元素加倍：
```java
import scala.Function1;

Function1<Integer, Integer> doubler = x -> x * 2;
List<Integer> doubledList = scalaList.map(doubler);
System.out.println("Doubled: " + doubledList); // 輸出：Doubled: List(2, 4, 6)
```

此處的 `Function1` 是 Scala 的介面，代表具有一個參數的函數，這與 Java 的 lambda 語法相符。

---

### **關鍵注意事項**
- **類型安全**：Scala 集合是參數化的，但由於類型擦除，方法回傳類型在 Java 中可能顯示為 `Object`。請根據需要進行轉換（例如 `(Integer) scalaList.head()`）。
- **效能**：跨越 Java-Scala 邊界會帶來一些開銷，但通常較小。
- **典範轉移**：Scala 集合強調不可變性與函數式程式設計，這可能與 Java 的命令式風格不同。例如，您無法向不可變的 `List`「新增」元素——而是會建立一個新的 `List`（例如使用 `:+` 來附加元素，它會回傳一個新的 `List`）。
- **版本相容性**：請確保 Scala 函式庫版本符合您的需求。對於 Scala 2.13+，請使用 `scala.jdk.CollectionConverters`；對於 2.12 或更早版本，請使用 `scala.collection.JavaConverters`。

---

### **總結**
您可以透過以下方式在 Java 中使用 `scala.collection` 套件：
1. 將 Scala 函式庫加入專案的 classpath（例如透過 Maven 或 Gradle）。
2. 匯入所需的 Scala 集合類別（例如 `scala.collection.immutable.List`）。
3. 使用伴生物件（例如 `List$.MODULE$.apply`）建立 Scala 集合，並使用 `CollectionConverters` 將 Java 集合轉換為 Scala `Seq`。
4. 使用 Scala 方法操作集合，並根據需要使用類型轉換與 lambda 表達式。

這種方法讓您能夠在 Java 生態系統中，利用 Scala 強大的集合函式庫，例如其不可變資料結構或函數式操作。