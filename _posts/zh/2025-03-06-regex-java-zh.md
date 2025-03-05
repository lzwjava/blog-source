---
audio: false
generated: true
lang: zh
layout: post
title: 正则表达式在Java中
translated: true
---

# 如何在 Java 中使用 `java.util.regex`

`java.util.regex` 包在 Java 中提供了用于处理正则表达式（regex）的工具，这些正则表达式是用于匹配和操作文本的模式。本指南将带您了解使用该包的基础知识，重点介绍两个主要类：`Pattern` 和 `Matcher`。我还将涵盖一些常见的用例和示例，以帮助您入门。

## `java.util.regex` 概述

`java.util.regex` 包包括：

- **`Pattern`**：表示编译后的正则表达式。您可以从正则表达式字符串创建它。
- **`Matcher`**：将模式应用于特定的输入字符串并执行匹配操作。

此外，Java 的 `String` 类还提供了基于正则表达式的方法，用于更简单的任务。

## 使用 `java.util.regex` 的基本步骤

要在 Java 中使用正则表达式，请按照以下步骤进行：

1. **编译一个模式**：将正则表达式字符串转换为 `Pattern` 对象。
2. **创建一个匹配器**：使用模式为输入文本创建一个 `Matcher`。
3. **执行操作**：使用匹配器检查匹配项、查找模式或操作文本。

以下是实际操作的示例。

## 示例 1：验证电子邮件地址

让我们使用基本的正则表达式模式 `".+@.+\\..+"` 创建一个简单的电子邮件验证器。该模式匹配在 `@` 符号前后至少有一个字符的字符串，后跟一个点和更多字符（例如，`example@test.com`）。

```java
import java.util.regex.*;

public class EmailValidator {
    public static boolean isValidEmail(String email) {
        // 定义正则表达式模式
        String regex = ".+@.+\\..+";
        // 编译模式
        Pattern pattern = Pattern.compile(regex);
        // 为输入字符串创建匹配器
        Matcher matcher = pattern.matcher(email);
        // 检查整个字符串是否与模式匹配
        return matcher.matches();
    }

    public static void main(String[] args) {
        String email = "example@test.com";
        if (isValidEmail(email)) {
            System.out.println("有效的电子邮件");
        } else {
            System.out.println("无效的电子邮件");
        }
    }
}
```

### 解释
- **`Pattern.compile(regex)`**：将正则表达式字符串编译为 `Pattern` 对象。
- **`pattern.matcher(email)`**：为输入字符串 `email` 创建一个 `Matcher`。
- **`matcher.matches()`**：如果整个字符串与模式匹配，则返回 `true`，否则返回 `false`。

**输出**：`有效的电子邮件`

注意：这是一个简化的电子邮件模式。实际的电子邮件验证需要更复杂的正则表达式（例如，按照 RFC 5322），但这可以作为起点。

## 示例 2：在字符串中查找所有标签

假设您想从推文中提取所有标签（例如，`#java`）。使用正则表达式 `"#\\w+"`，其中 `#` 匹配字面标签符号，`\\w+` 匹配一个或多个单词字符（字母、数字或下划线）。

```java
import java.util.regex.*;

public class HashtagExtractor {
    public static void main(String[] args) {
        String tweet = "这是一个 #sample 推文，带有 #multiple 标签，例如 #java";
        String regex = "#\\w+";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(tweet);

        // 查找所有匹配项
        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }
}
```

### 解释
- **`matcher.find()`**：将光标移到输入字符串中的下一个匹配项，如果找到匹配项，则返回 `true`。
- **`matcher.group()`**：返回当前匹配项的匹配文本。

**输出**：
```
#sample
#multiple
#java
```

## 示例 3：使用正则表达式替换文本

要替换文本中的所有出现（例如，将 `badword` 替换为星号），可以使用 `String.replaceAll()` 方法，该方法在内部使用正则表达式。

```java
public class TextCensor {
    public static void main(String[] args) {
        String text = "这是一个 badword 示例，带有 badword 重复。";
        String censored = text.replaceAll("badword", "*******");
        System.out.println(censored);
    }
}
```

**输出**：`这是一个 ******* 示例，带有 ******* 重复。`

对于更复杂的替换，请使用 `Matcher`：

```java
import java.util.regex.*;

public class ComplexReplacement {
    public static void main(String[] args) {
        String text = "联系方式：123-456-7890";
        String regex = "\\d{3}-\\d{3}-\\d{4}"; // 匹配电话号码
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);
        String result = matcher.replaceAll("XXX-XXX-XXXX");
        System.out.println(result);
    }
}
```

**输出**：`联系方式：XXX-XXX-XXXX`

## 示例 4：使用组解析结构化数据

正则表达式组，用括号 `()` 定义，允许您捕获匹配的一部分。例如，解析社保号（SSN）如 `123-45-6789`：

```java
import java.util.regex.*;

public class SSNParser {
    public static void main(String[] args) {
        String ssn = "123-45-6789";
        String regex = "(\\d{3})-(\\d{2})-(\\d{4})"; // 区域、组和序列号的组
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(ssn);

        if (matcher.matches()) {
            System.out.println("区域号码：" + matcher.group(1));
            System.out.println("组号码：" + matcher.group(2));
            System.out.println("序列号：" + matcher.group(3));
        }
    }
}
```

### 解释
- **`"(\\d{3})-(\\d{2})-(\\d{4})"`**：定义三个组：
  - 组 1：`\\d{3}`（三个数字）
  - 组 2：`\\d{2}`（两个数字）
  - 组 3：`\\d{4}`（四个数字）
- **`matcher.group(n)`**：检索组 `n`（基于 1 的索引）匹配的文本。

**输出**：
```
区域号码：123
组号码：45
序列号：6789
```

您还可以使用 **命名组** 以便于理解：

```java
String regex = "(?<area>\\d{3})-(?<group>\\d{2})-(?<serial>\\d{4})";
Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher("123-45-6789");
if (matcher.matches()) {
    System.out.println("区域：" + matcher.group("area"));
    System.out.println("组：" + matcher.group("group"));
    System.out.println("序列：" + matcher.group("serial"));
}
```

## 附加功能和技巧

### 标志

使用 `Pattern.compile()` 中的标志修改模式行为：
- **`Pattern.CASE_INSENSITIVE`**：在匹配时忽略大小写。
  ```java
  Pattern pattern = Pattern.compile("hello", Pattern.CASE_INSENSITIVE);
  Matcher matcher = pattern.matcher("HELLO");
  System.out.println(matcher.matches()); // true
  ```

### 字符串方法

对于简单任务，使用 `String` 方法：
- **`matches()`**：检查整个字符串是否与正则表达式匹配。
  ```java
  String text = "cat";
  System.out.println(text.matches("\\w{3}")); // true
  ```
- **`split()`**：按正则表达式模式拆分字符串。
  ```java
  String data = "apple, banana, cherry";
  String[] fruits = data.split("\\s*,\\s*");
  // 输出：apple, banana, cherry
  ```

### 转义特殊字符

正则表达式使用特殊字符，例如 `.`、`*` 和 `?`。要匹配它们，请使用 `\\` 转义：
- 匹配句号：`"\\."`
- 在 Java 字符串中，转义反斜杠：`"\\d"` 表示数字，`"\\\\"` 表示字面反斜杠。

### 性能

编译模式是昂贵的。尽可能重用 `Pattern` 对象：
```java
Pattern pattern = Pattern.compile("\\d+"); // 编译一次
for (String input : new String[]{"123", "456"}) {
    Matcher matcher = pattern.matcher(input);
    if (matcher.matches()) {
        System.out.println("数字：" + input);
    }
}
```

### 错误处理

无效的正则表达式模式会抛出 `PatternSyntaxException`。在生产代码中处理它：
```java
try {
    Pattern pattern = Pattern.compile("["); // 无效的正则表达式
} catch (PatternSyntaxException e) {
    System.err.println("无效的正则表达式：" + e.getMessage());
}
```

## 总结

- **编译一个模式**：`Pattern.compile(regex)`
- **创建一个匹配器**：`pattern.matcher(input)`
- **关键操作**：
  - `matches()`：完全匹配字符串
  - `find()`：查找下一个匹配项
  - `group()`：提取匹配的文本
  - `replaceAll()`：替换匹配项
- **便利性**：对于简单任务，使用 `String` 方法。
- **最佳实践**：转义特殊字符，重用模式，并处理异常。

这涵盖了 `java.util.regex` 的基本知识。有关高级主题（例如前瞻或字符类），请参阅 [Java 文档](https://docs.oracle.com/en/java/javase/17/docs/api/java.util.regex/package-summary.html) 或针对特定用例进行实验！