---
audio: false
generated: true
lang: hant
layout: post
title: Java 正則表達式
translated: true
type: note
---

# 如何使用 Java 中的 `java.util.regex`

Java 中的 `java.util.regex` 套件提供了處理正則表達式（regex）的工具，這些模式用於匹配和操作文字。本指南將引導您了解此套件的基本用法，重點介紹兩個主要類別：`Pattern` 和 `Matcher`。我還會透過範例涵蓋常見使用情境，幫助您入門。

## `java.util.regex` 概述

`java.util.regex` 套件包括：

- **`Pattern`**：代表一個編譯過的正則表達式。您可以從 regex 字串創建它。
- **`Matcher`**：將模式應用於特定的輸入字串並執行匹配操作。

此外，Java 的 `String` 類別提供了基於 regex 的方法，用於較簡單的任務。

## 使用 `java.util.regex` 的基本步驟

要在 Java 中使用正則表達式，請遵循以下步驟：

1. **編譯模式**：將您的 regex 字串轉換為 `Pattern` 物件。
2. **創建匹配器**：使用該模式為您的輸入文字創建一個 `Matcher`。
3. **執行操作**：使用匹配器來檢查匹配、尋找模式或操作文字。

以下是實際運作方式。

## 範例 1：驗證電子郵件地址

讓我們使用基本的 regex 模式：`".+@.+\\..+"` 來創建一個簡單的電子郵件驗證器。此模式匹配在 `@` 符號前後至少有一個字元，後跟一個點和更多字元的字串（例如 `example@test.com`）。

```java
import java.util.regex.*;

public class EmailValidator {
    public static boolean isValidEmail(String email) {
        // 定義 regex 模式
        String regex = ".+@.+\\..+";
        // 編譯模式
        Pattern pattern = Pattern.compile(regex);
        // 為輸入字串創建匹配器
        Matcher matcher = pattern.matcher(email);
        // 檢查整個字串是否與模式匹配
        return matcher.matches();
    }

    public static void main(String[] args) {
        String email = "example@test.com";
        if (isValidEmail(email)) {
            System.out.println("有效的電子郵件");
        } else {
            System.out.println("無效的電子郵件");
        }
    }
}
```

### 解釋
- **`Pattern.compile(regex)`**：將 regex 字串編譯成 `Pattern` 物件。
- **`pattern.matcher(email)`**：為輸入字串 `email` 創建一個 `Matcher`。
- **`matcher.matches()`**：如果整個字串與模式匹配，則返回 `true`，否則返回 `false`。

**輸出**：`有效的電子郵件`

注意：這是一個簡化的電子郵件模式。真實的電子郵件驗證需要更複雜的 regex（例如，根據 RFC 5322），但這可以作為起點。

## 範例 2：在字串中尋找所有主題標籤

假設您想從一條推文中提取所有主題標籤（例如 `#java`）。使用 regex `"#\\w+"`，其中 `#` 匹配字面的主題標籤符號，而 `\\w+` 匹配一個或多個單詞字元（字母、數字或底線）。

```java
import java.util.regex.*;

public class HashtagExtractor {
    public static void main(String[] args) {
        String tweet = "這是一條帶有 #多個 主題標籤的 #示例 推文，例如 #java";
        String regex = "#\\w+";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(tweet);

        // 尋找所有匹配項
        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }
}
```

### 解釋
- **`matcher.find()`**：移動到輸入字串中的下一個匹配項，如果找到匹配項則返回 `true`。
- **`matcher.group()`**：返回目前匹配項的匹配文字。

**輸出**：
```
#示例
#多個
#java
```

## 範例 3：使用 Regex 替換文字

要替換單字的所有出現次數（例如，用星號審查 "badword"），您可以使用 `String.replaceAll()` 方法，該方法內部使用 regex。

```java
public class TextCensor {
    public static void main(String[] args) {
        String text = "這是一個 badword 範例，其中 badword 重複出現。";
        String censored = text.replaceAll("badword", "*******");
        System.out.println(censored);
    }
}
```

**輸出**：`這是一個 ******* 範例，其中 ******* 重複出現。`

對於更複雜的替換，請使用 `Matcher`：

```java
import java.util.regex.*;

public class ComplexReplacement {
    public static void main(String[] args) {
        String text = "聯絡方式：123-456-7890";
        String regex = "\\d{3}-\\d{3}-\\d{4}"; // 匹配電話號碼
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);
        String result = matcher.replaceAll("XXX-XXX-XXXX");
        System.out.println(result);
    }
}
```

**輸出**：`聯絡方式：XXX-XXX-XXXX`

## 範例 4：使用群組解析結構化數據

Regex 群組，用括號 `()` 定義，允許您捕獲匹配的部分。例如，要解析像 `123-45-6789` 這樣的社會安全號碼（SSN）：

```java
import java.util.regex.*;

public class SSNParser {
    public static void main(String[] args) {
        String ssn = "123-45-6789";
        String regex = "(\\d{3})-(\\d{2})-(\\d{4})"; // 區域、組別、序列號的群組
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(ssn);

        if (matcher.matches()) {
            System.out.println("區域號碼：" + matcher.group(1));
            System.out.println("組別號碼：" + matcher.group(2));
            System.out.println("序列號碼：" + matcher.group(3));
        }
    }
}
```

### 解釋
- **`"(\\d{3})-(\\d{2})-(\\d{4})"`**：定義三個群組：
  - 群組 1：`\\d{3}`（三位數字）
  - 群組 2：`\\d{2}`（兩位數字）
  - 群組 3：`\\d{4}`（四位數字）
- **`matcher.group(n)`**：檢索由群組 `n` 匹配的文字（基於 1 的索引）。

**輸出**：
```
區域號碼：123
組別號碼：45
序列號碼：6789
```

您也可以使用**命名群組**以增加清晰度：

```java
String regex = "(?<area>\\d{3})-(?<group>\\d{2})-(?<serial>\\d{4})";
Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher("123-45-6789");
if (matcher.matches()) {
    System.out.println("區域：" + matcher.group("area"));
    System.out.println("組別：" + matcher.group("group"));
    System.out.println("序列：" + matcher.group("serial"));
}
```

## 其他功能和提示

### 標誌
在 `Pattern.compile()` 中使用標誌來修改模式行為：
- **`Pattern.CASE_INSENSITIVE`**：匹配時忽略大小寫。
  ```java
  Pattern pattern = Pattern.compile("hello", Pattern.CASE_INSENSITIVE);
  Matcher matcher = pattern.matcher("HELLO");
  System.out.println(matcher.matches()); // true
  ```

### 字串方法
對於簡單任務，請使用 `String` 方法：
- **`matches()`**：檢查整個字串是否與 regex 匹配。
  ```java
  String text = "cat";
  System.out.println(text.matches("\\w{3}")); // true
  ```
- **`split()`**：根據 regex 模式分割字串。
  ```java
  String data = "apple, banana, cherry";
  String[] fruits = data.split("\\s*,\\s*");
  // 輸出：apple, banana, cherry
  ```

### 跳脫特殊字元
Regex 使用特殊字元，如 `.`、`*` 和 `?`。要按字面匹配它們，請使用 `\\` 跳脫：
- 匹配句點：`"\."`
- 在 Java 字串中，跳脫反斜線：`"\\d"` 用於數字，`"\\\\"` 用於字面反斜線。

### 效能
編譯模式成本高昂。盡可能重複使用 `Pattern` 物件：
```java
Pattern pattern = Pattern.compile("\\d+"); // 編譯一次
for (String input : new String[]{"123", "456"}) {
    Matcher matcher = pattern.matcher(input);
    if (matcher.matches()) {
        System.out.println("數字：" + input);
    }
}
```

### 錯誤處理
無效的 regex 模式會拋出 `PatternSyntaxException`。在生產程式碼中處理它：
```java
try {
    Pattern pattern = Pattern.compile("["); // 無效的 regex
} catch (PatternSyntaxException e) {
    System.err.println("無效的 regex：" + e.getMessage());
}
```

## 總結

- **編譯模式**：`Pattern.compile(regex)`
- **創建匹配器**：`pattern.matcher(input)`
- **關鍵操作**：
  - `matches()`：完整字串匹配
  - `find()`：尋找下一個匹配項
  - `group()`：提取匹配文字
  - `replaceAll()`：替換匹配項
- **便利性**：對於簡單任務，使用 `String` 方法。
- **最佳實踐**：跳脫特殊字元、重複使用模式，並處理例外。

這涵蓋了 `java.util.regex` 的基本知識。對於進階主題，如前瞻或字元類別，請查閱 [Java 文件](https://docs.oracle.com/en/java/javase/17/docs/api/java.util.regex/package-summary.html) 或針對特定使用情境進行實驗！