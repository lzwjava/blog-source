---
audio: false
generated: true
lang: zh
layout: post
title: 读取Java控制台输入
translated: true
---

要在Java中使用 `org.jline.reader` 包，这是JLine库的一部分，用于处理带有高级功能（如行编辑、历史记录和自动补全）的控制台输入，请按照以下步骤进行操作。本指南提供了一个完整且实用的方法，帮助你快速上手。

### 前提条件
确保你的项目中添加了JLine库。如果你使用的是Maven，请在 `pom.xml` 中包含以下依赖项：

```xml
<dependency>
    <groupId>org.jline</groupId>
    <artifactId>jline</artifactId>
    <version>3.21.0</version> <!-- 使用最新版本 -->
</dependency>
```

### 使用 `org.jline.reader` 的基本步骤

1. **创建终端实例**
   - 使用 `org.jline.terminal` 中的 `TerminalBuilder` 类创建一个 `Terminal` 对象。这表示将读取输入的控制台环境。
   - 示例：
     ```java
     import org.jline.terminal.Terminal;
     import org.jline.terminal.TerminalBuilder;

     Terminal terminal = TerminalBuilder.builder().build();
     ```
   - `build()` 方法创建一个适用于大多数环境的默认终端。你可以进一步自定义它（例如设置终端类型），但默认设置通常足够。

2. **创建 LineReader 实例**
   - 使用 `org.jline.reader` 中的 `LineReaderBuilder` 类创建一个 `LineReader` 对象，并将 `Terminal` 实例传递给它。
   - `LineReader` 是使用JLine功能读取用户输入的主要接口。
   - 示例：
     ```java
     import org.jline.reader.LineReader;
     import org.jline.reader.LineReaderBuilder;

     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .build();
     ```

3. **从用户读取输入**
   - 使用 `LineReader` 的 `readLine()` 方法读取用户输入的文本行。你可以可选地指定一个提示符来显示。
   - 示例：
     ```java
     String line = reader.readLine("> ");
     ```
   - 这将显示 `> ` 作为提示符，等待用户输入，并在用户按下Enter键时返回输入的字符串。

### 简单示例
以下是一个完整的最小示例，它在用户输入 "exit" 之前循环读取用户输入：

```java
import org.jline.reader.LineReader;
import org.jline.reader.LineReaderBuilder;
import org.jline.terminal.Terminal;
import org.jline.terminal.TerminalBuilder;

public class ConsoleExample {
    public static void main(String[] args) throws Exception {
        // 创建终端
        Terminal terminal = TerminalBuilder.builder().build();

        // 创建 LineReader
        LineReader reader = LineReaderBuilder.builder()
            .terminal(terminal)
            .build();

        // 循环读取输入
        String line;
        while ((line = reader.readLine("> ")) != null) {
            System.out.println("你输入了: " + line);
            if (line.equals("exit")) {
                break;
            }
        }
    }
}
```

- **输出**：运行此程序时，它会显示 `> ` 提示符。你可以输入文本，使用退格键或箭头键进行编辑（这些功能在 `System.in` 中不容易实现），然后按Enter键。输入 "exit" 将结束程序。

### 可选功能
你可以通过以下方式增强 `LineReader` 的功能：

#### 1. **启用命令历史记录**
   - 添加一个 `History` 对象来存储和回调之前的输入（例如使用上下箭头键）。
   - 示例：
     ```java
     import org.jline.reader.impl.history.DefaultHistory;
     import org.jline.reader.History;

     History history = new DefaultHistory();
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .history(history)
         .build();
     ```
   - 现在，用户可以浏览他们的输入历史记录。

#### 2. **添加自动补全**
   - 实现一个 `Completer` 来建议在用户按下Tab键时的补全。
   - 使用简单字符串补全的示例：
     ```java
     import org.jline.reader.Completer;
     import org.jline.reader.impl.completer.StringsCompleter;

     Completer completer = new StringsCompleter("foo", "bar", "baz");
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .completer(completer)
         .build();
     ```
   - 输入 "f" 并按下Tab键建议 "foo"。

#### 3. **读取密码（掩码输入）**
   - 使用带有掩码字符的 `readLine()` 来隐藏输入（例如用于密码）。
   - 示例：
     ```java
     String password = reader.readLine("输入密码: ", '*');
     ```
   - 显示星号（`*`）而不是输入的字符。

### 资源管理
对于健壮的应用程序，完成后关闭 `Terminal` 以释放资源。由于 `Terminal` 实现了 `Closeable`，可以使用 try-with-resources 块：

```java
try (Terminal terminal = TerminalBuilder.builder().build()) {
    LineReader reader = LineReaderBuilder.builder()
        .terminal(terminal)
        .build();
    String line = reader.readLine("> ");
    System.out.println("你输入了: " + line);
}
```

### 为什么使用 `org.jline.reader`？
与基本的 `System.in` 和 `BufferedReader` 输入相比，`org.jline.reader` 提供了：
- **行编辑**：退格、光标移动等。
- **历史记录**：回调之前的输入。
- **补全**：自动建议选项。
- **跨平台终端处理**：在不同环境中一致工作。

### 注意事项
- 如果在 `LineReaderBuilder` 中没有指定 `Terminal`，它会在内部创建一个默认的，因此 `LineReader reader = LineReaderBuilder.builder().build();` 对于简单情况是有效的。
- 避免从多个线程同时调用 `readLine()`，因为 `LineReader` 对并发读取不安全。
- 对于高级用例（例如多行输入、自定义键绑定），探索JLine的其他功能，如解析器或键映射。

这涵盖了使用 `org.jline.reader` 读取Java控制台输入的基本要点。从基本设置开始，根据需要为你的应用程序添加功能，如历史记录或补全！