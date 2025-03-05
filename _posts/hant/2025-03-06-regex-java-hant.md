---
audio: false
generated: true
lang: hant
layout: post
title: 正則表達式在Java
translated: true
---

# 如何在 Java 中使用 `java.util.regex`

`java.util.regex` 包在 Java 中提供了用於處理正則表達式（regex）的工具，這些正則表達式是用來匹配和操作文本的模式。本指南將帶您了解使用這個包的基本知識，重點介紹兩個主要的類別：`Pattern` 和 `Matcher`。我還將涵蓋一些常見的用例和範例，幫助您入門。

## `java.util.regex` 總覽

`java.util.regex` 包包括：

- **`Pattern`**：表示已編譯的正則表達式。您可以從正則表達式字串創建它。
- **`Matcher`**：將模式應用於特定的輸入字串並執行匹配操作。

此外，Java 的 `String` 類別提供了基於正則表達式的方法來處理簡單任務。

## 基本步驟使用 `java.util.regex`

要在 Java 中使用正則表達式，請按照以下步驟進行：

1. **編譯模式**：將您的正則表達式字串轉換為 `Pattern` 對象。
2. **創建匹配器**：使用模式為您的輸入文本創建一個 `Matcher`。
3. **執行操作**：使用匹配器檢查匹配項、查找模式或操作文本。

以下是實際操作的方式。

## 範例 1：驗證電子郵件地址

讓我們使用基本的正則表達式模式 `".+@.+\\..+"` 創建一個簡單的電子郵件驗證器。這個模式匹配在 `@` 符號前後至少有一個字符，後面跟著一個點和更多字符（例如 `example@test.com`）。

```java
import java.util.regex.*;

public class EmailValidator {
    public static boolean isValidEmail(String email) {
        // 定義正則表達式模式
        String regex = ".+@.+\\..+";
        // 編譯模式
        Pattern pattern = Pattern.compile(regex);
        // 為輸入字串創建匹配器
        Matcher matcher = pattern.matcher(email);
        // 檢查整個字串是否匹配模式
        return matcher.matches();
    }

    public static void main(String[] args) {
        String email = "example@test.com";
        if (isValidEmail(email)) {
            System.out.println("有效電子郵件");
        } else {
            System.out.println("無效電子郵件");
        }
    }
}
```

### 說明
- **`Pattern.compile(regex)`**：將正則表達式字串編譯為 `Pattern` 對象。
- **`pattern.matcher(email)`**：為輸入字串 `email` 創建一個 `Matcher`。
- **`matcher.matches()`**：如果整個字串匹配模式，則返回 `true`，否則返回 `false`。

**輸出**：`有效電子郵件`

注意：這是一個簡化的電子郵件模式。真正的電子郵件驗證需要更複雜的正則表達式（例如，根據 RFC 5322），但這可以作為起點。

## 範例 2：在字串中查找所有標籤

假設您想從推文中提取所有標籤（例如 `#java`）。使用正則表達式 `"#\\w+"`，其中 `#` 匹配標籤符號，`\\w+` 匹配一個或多個單詞字符（字母、數字或下劃線）。

```java
import java.util.regex.*;

public class HashtagExtractor {
    public static void main(String[] args) {
        String tweet = "這是一個 #sample 推文，有 #multiple 標籤，例如 #java";
        String regex = "#\\w+";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(tweet);

        // 查找所有匹配項
        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }
}
```

### 說明
- **`matcher.find()`**：將光標移到輸入字串中的下一個匹配項，如果找到匹配項則返回 `true`。
- **`matcher.group()`**：返回當前匹配的文本。

**輸出**：
```
#sample
#multiple
#java
```

## 範例 3：使用正則表達式替換文本

要替換字串中的所有出現（例如，將 "badword" 替換為星號），可以使用 `String.replaceAll()` 方法，該方法內部使用正則表達式。

```java
public class TextCensor {
    public static void main(String[] args) {
        String text = "這是一個 badword 範例，badword 重複。";
        String censored = text.replaceAll("badword", "*******");
        System.out.println(censored);
    }
}
```

**輸出**：`這是一個 ******* 範例，****** 重複。`

對於更複雜的替換，使用 `Matcher`：

```java
import java.util.regex.*;

public class ComplexReplacement {
    public static void main(String[] args) {
        String text = "聯繫方式：123-456-7890";
        String regex = "\\d{3}-\\d{3}-\\d{4}"; // 匹配電話號碼
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);
        String result = matcher.replaceAll("XXX-XXX-XXXX");
        System.out.println(result);
    }
}
```

**輸出**：`聯繫方式：XXX-XXX-XXXX`

## 範例 4：使用組來解析結構化數據

正則表達式組，用括號 `()` 定義，允許您捕獲匹配的一部分。例如，解析社會保障號碼（SSN）如 `123-45-6789`：

```java
import java.util.regex.*;

public class SSNParser {
    public static void main(String[] args) {
        String ssn = "123-45-6789";
        String regex = "(\\d{3})-(\\d{2})-(\\d{4})"; // 區域、組和序列號的組
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(ssn);

        if (matcher.matches()) {
            System.out.println("區域號碼：" + matcher.group(1));
            System.out.println("組號碼：" + matcher.group(2));
            System.out.println("序列號碼：" + matcher.group(3));
        }
    }
}
```

### 說明
- **`"(\\d{3})-(\\d{2})-(\\d{4})"`**：定義三個組：
  - 組 1：`\\d{3}`（三個數字）
  - 組 2：`\\d{2}`（兩個數字）
  - 組 3：`\\d{4}`（四個數字）
- **`matcher.group(n)`**：檢索由組 `n` 匹配的文本（基於 1 的索引）。

**輸出**：
```
區域號碼：123
組號碼：45
序列號碼：6789
```

您也可以使用 **命名組** 以提高可讀性：

```java
String regex = "(?<area>\\d{3})-(?<group>\\d{2})-(?<serial>\\d{4})";
Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher("123-45-6789");
if (matcher.matches()) {
    System.out.println("區域：" + matcher.group("area"));
    System.out.println("組：" + matcher.group("group"));
    System.out.println("序列：" + matcher.group("serial"));
}
```

## 額外功能和技巧

### 標誌

使用 `Pattern.compile()` 中的標誌來修改模式行為：
- **`Pattern.CASE_INSENSITIVE`**：在匹配時忽略大小寫。
  ```java
  Pattern pattern = Pattern.compile("hello", Pattern.CASE_INSENSITIVE);
  Matcher matcher = pattern.matcher("HELLO");
  System.out.println(matcher.matches()); // true
  ```

### 字串方法

對於簡單任務，使用 `String` 方法：
- **`matches()`**：檢查整個字串是否匹配正則表達式。
  ```java
  String text = "cat";
  System.out.println(text.matches("\\w{3}")); // true
  ```
- **`split()`**：根據正則表達式模式拆分字串。
  ```java
  String data = "蘋果, 香蕉, 櫻桃";
  String[] fruits = data.split("\\s*,\\s*");
  // 輸出：蘋果, 香蕉, 櫻桃
  ```

### 轉義特殊字符

正則表達式使用特殊字符，例如 `.`、`*` 和 `?`。要匹配它們，請使用 `\\` 轉義：
- 匹配句號：`"\\."`
- 在 Java 字串中，轉義反斜杠：`"\\d"` 表示數字，`"\\\\"` 表示字面反斜杠。

### 性能

編譯模式是昂貴的。在可能的情況下重用 `Pattern` 對象：
```java
Pattern pattern = Pattern.compile("\\d+"); // 只編譯一次
for (String input : new String[]{"123", "456"}) {
    Matcher matcher = pattern.matcher(input);
    if (matcher.matches()) {
        System.out.println("數字：" + input);
    }
}
```

### 錯誤處理

無效的正則表達式模式會拋出 `PatternSyntaxException`。在生產代碼中處理它：
```java
try {
    Pattern pattern = Pattern.compile("["); // 無效正則表達式
} catch (PatternSyntaxException e) {
    System.err.println("無效正則表達式：" + e.getMessage());
}
```

## 總結

- **編譯模式**：`Pattern.compile(regex)`
- **創建匹配器**：`pattern.matcher(input)`
- **關鍵操作**：
  - `matches()`：完全匹配字串
  - `find()`：查找下一個匹配項
  - `group()`：提取匹配的文本
  - `replaceAll()`：替換匹配項
- **便利性**：對於簡單任務，使用 `String` 方法。
- **最佳實踐**：轉義特殊字符，重用模式並處理例外。

這涵蓋了 `java.util.regex` 的基本知識。有關高級主題，例如前瞻或字符類，請參閱 [Java 文檔](https://docs.oracle.com/en/java/javase/17/docs/api/java.util.regex/package-summary.html) 或針對特定用例進行實驗！