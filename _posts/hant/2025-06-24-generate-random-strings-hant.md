---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Apache Commons Lang 生成隨機字串
translated: true
type: note
---

`RandomStringUtils` 是 Apache Commons Lang 函式庫中一個非常實用的類別，提供了多種用於生成隨機字串的靜態方法。這包括生成特定長度的字串、僅包含字母、僅包含數字、字母數字字符，甚至是自定義字符集。

以下是使用方法及必要的 Maven 依賴項：

## 如何使用 `org.apache.commons.lang3.RandomStringUtils;`

首先，您需要在 Java 檔案中導入此類別：

```java
import org.apache.commons.lang3.RandomStringUtils;
```

然後您可以使用其靜態方法。以下是一些常見範例：

1.  **生成指定長度的隨機字母數字字串：**

    ```java
    String randomAlphaNumeric = RandomStringUtils.randomAlphanumeric(10);
    System.out.println("隨機字母數字: " + randomAlphaNumeric); // 例如："aB5cY2x9Pq"
    ```

2.  **生成指定長度的隨機字母字串：**

    ```java
    String randomAlphabetic = RandomStringUtils.randomAlphabetic(8);
    System.out.println("隨機字母: " + randomAlphabetic); // 例如："GhJkLmNo"
    ```

3.  **生成指定長度的隨機數字字串：**

    ```java
    String randomNumeric = RandomStringUtils.randomNumeric(6);
    System.out.println("隨機數字: " + randomNumeric); // 例如："123456"
    ```

4.  **生成混合字母和數字的隨機字串，並指定標誌：**

    ```java
    String randomLettersAndNumbers = RandomStringUtils.random(12, true, true);
    System.out.println("隨機字母和數字: " + randomLettersAndNumbers); // 例如："abC123DeF456"
    ```

5.  **從自定義字符集生成隨機字串：**

    ```java
    String chars = "abcdefg";
    String randomFromCustomSet = RandomStringUtils.random(5, chars);
    System.out.println("自定義字符集隨機字串: " + randomFromCustomSet); // 例如："gcfae"
    ```

## 在 `pom.xml` 中使用哪個函式庫

要在 Maven 專案中使用 `RandomStringUtils`，您需要將 `commons-lang3` 依賴項添加到 `pom.xml` 檔案中。

以下是依賴項代碼片段：

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.14.0</version> </dependency>
```

**重要注意事項：**

  * **版本：** 請務必檢查 [Maven Central](https://mvnrepository.com/artifact/org.apache.commons/commons-lang3) 以獲取 `commons-lang3` 的最新穩定版本。根據我最後的更新，`3.14.0` 或更高版本是不錯的選擇，但最好還是使用當前可用的最新穩定版本。
  * **範圍：** 依賴項的預設範圍是 `compile`，這通常適用於像這樣的工具函式庫。這意味著 JAR 將在編譯、測試和運行時可用。如果您僅在測試中使用它，則可以使用 `<scope>test</scope>`。
  * **棄用說明：** 請注意，一些舊方法如 `RandomStringUtils.randomAlphabetic(int count)` 在較新版本的 Apache Commons Lang 3 中已被棄用。建議改用 `secure()`、`secureStrong()` 或 `insecure()` 方法，這些方法提供了對隨機源更好的控制。例如：`RandomStringUtils.secure().nextAlphanumeric(10)`。然而，對於許多使用場景，舊方法仍然有效。