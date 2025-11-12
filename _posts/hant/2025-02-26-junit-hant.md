---
audio: false
generated: true
lang: hant
layout: post
title: Junit：Java 測試框架
translated: true
type: note
---

JUnit 是一個流行的 Java 測試框架。它允許開發者編寫和執行可重複的自動化測試，有助於確保程式碼行為符合預期。以下是如何使用 JUnit 進行測試的基本指南：

### 1. 在專案中設定 JUnit

- **Maven**：將 JUnit 依賴項加入您的 `pom.xml` 檔案。
  ```xml
  <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.13.2</version>
      <scope>test</scope>
  </dependency>
  ```

- **Gradle**：將 JUnit 依賴項加入您的 `build.gradle` 檔案。
  ```groovy
  testImplementation 'junit:junit:4.13.2'
  ```

### 2. 編寫測試類別

為您的測試建立新的 Java 類別。良好的做法是將測試類別命名為待測類別名稱後加上 "Test" 後綴。

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class MyClassTest {

    @Test
    public void testAddition() {
        MyClass myClass = new MyClass();
        int result = myClass.add(2, 3);
        assertEquals(5, result);
    }
}
```

### 3. 註解

- `@Test`：標示該方法為測試方法。
- `@Before`：在每個測試方法前執行。適用於設定工作。
- `@After`：在每個測試方法後執行。適用於清理工作。
- `@BeforeClass`：在類別中所有測試方法前執行一次。
- `@AfterClass`：在類別中所有測試方法後執行一次。

### 4. 斷言

斷言用於驗證程式碼行為是否符合預期。

- `assertEquals(expected, actual)`：檢查兩個值是否相等。
- `assertTrue(condition)`：檢查條件是否為真。
- `assertFalse(condition)`：檢查條件是否為假。
- `assertNull(object)`：檢查物件是否為空值。
- `assertNotNull(object)`：檢查物件是否非空值。

### 5. 執行測試

您可以使用 IDE 內建工具或透過命令列使用 Maven 或 Gradle 來執行測試。

- **Maven**：`mvn test`
- **Gradle**：`gradle test`

### 範例

以下是一個簡單類別及其對應測試類別的範例：

```java
// MyClass.java
public class MyClass {
    public int add(int a, int b) {
        return a + b;
    }
}

// MyClassTest.java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class MyClassTest {

    @Test
    public void testAddition() {
        MyClass myClass = new MyClass();
        int result = myClass.add(2, 3);
        assertEquals(5, result);
    }
}
```

### 額外提示

- **測試獨立性**：每個測試應獨立於其他測試。避免測試之間的依賴關係。
- **測試覆蓋率**：追求高測試覆蓋率，但應著重於有意義的測試而非僅提高覆蓋率百分比。
- **Mocking**：使用 Mockito 等 mocking 框架來隔離待測類別與其依賴項。

透過遵循這些步驟，您就能有效地使用 JUnit 為 Java 應用程式編寫和執行測試。