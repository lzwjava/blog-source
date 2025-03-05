---
audio: false
generated: true
lang: hant
layout: post
title: 讀取 Java 中的控制台輸入
translated: true
---

要在 Java 中使用 `org.jline.reader` 套件，這是 JLine 圖書館的一部分，用於處理具有高級功能（如行編輯、歷史記錄和自動完成）的控制台輸入，請按照以下步驟進行。本指南提供了一個完整且實用的方法來幫助你開始。

### 前提條件
確保已將 JLine 圖書館添加到您的項目中。如果您使用 Maven，請在 `pom.xml` 中包含以下依賴項：

```xml
<dependency>
    <groupId>org.jline</groupId>
    <artifactId>jline</artifactId>
    <version>3.21.0</version> <!-- 使用最新版本 -->
</dependency>
```

### 使用 `org.jline.reader` 的基本步驟

1. **創建終端實例**
   - 使用 `org.jline.terminal` 中的 `TerminalBuilder` 類來創建一個 `Terminal` 對象。這代表了將讀取輸入的控制台環境。
   - 範例：
     ```java
     import org.jline.terminal.Terminal;
     import org.jline.terminal.TerminalBuilder;

     Terminal terminal = TerminalBuilder.builder().build();
     ```
   - `build()` 方法創建了一個適用於大多數環境的默認終端。您可以進一步自定義它（例如設置終端類型），但默認設置通常已經足夠。

2. **創建 LineReader 實例**
   - 使用 `org.jline.reader` 中的 `LineReaderBuilder` 類來創建一個 `LineReader` 對象，並將 `Terminal` 實例傳遞給它。
   - `LineReader` 是使用 JLine 功能讀取用戶輸入的主要介面。
   - 範例：
     ```java
     import org.jline.reader.LineReader;
     import org.jline.reader.LineReaderBuilder;

     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .build();
     ```

3. **從用戶讀取輸入**
   - 使用 `LineReader` 的 `readLine()` 方法讀取用戶輸入的文本行。您可以選擇指定要顯示的提示。
   - 範例：
     ```java
     String line = reader.readLine("> ");
     ```
   - 這將顯示 `> ` 作為提示，等待用戶輸入，並在用戶按下 Enter 鍵時返回輸入的字符串。

### 簡單範例
這是一個完整的最小範例，直到用戶輸入 "exit" 才讀取用戶輸入：

```java
import org.jline.reader.LineReader;
import org.jline.reader.LineReaderBuilder;
import org.jline.terminal.Terminal;
import org.jline.terminal.TerminalBuilder;

public class ConsoleExample {
    public static void main(String[] args) throws Exception {
        // 創建終端
        Terminal terminal = TerminalBuilder.builder().build();

        // 創建 LineReader
        LineReader reader = LineReaderBuilder.builder()
            .terminal(terminal)
            .build();

        // 在循環中讀取輸入
        String line;
        while ((line = reader.readLine("> ")) != null) {
            System.out.println("您輸入了: " + line);
            if (line.equals("exit")) {
                break;
            }
        }
    }
}
```

- **輸出**：當您運行此程序時，它會顯示 `> ` 提示。您可以輸入文本，使用退格或箭頭鍵進行編輯（這些功能與 `System.in` 不易實現），然後按 Enter。輸入 "exit" 結束程序。

### 可選功能
您可以通過以下方式增強 `LineReader` 的功能：

#### 1. **啟用命令歷史記錄**
   - 添加一個 `History` 對象來存儲和回顧先前的輸入（例如，使用上下箭頭鍵）。
   - 範例：
     ```java
     import org.jline.reader.impl.history.DefaultHistory;
     import org.jline.reader.History;

     History history = new DefaultHistory();
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .history(history)
         .build();
     ```
   - 現在，用戶可以瀏覽其輸入歷史記錄。

#### 2. **添加自動完成**
   - 實現一個 `Completer` 以在用戶按 Tab 鍵時建議完成。
   - 使用簡單字符串完成器的範例：
     ```java
     import org.jline.reader.Completer;
     import org.jline.reader.impl.completer.StringsCompleter;

     Completer completer = new StringsCompleter("foo", "bar", "baz");
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .completer(completer)
         .build();
     ```
   - 输入 "f" 並按 Tab 鍵建議 "foo"。

#### 3. **讀取密碼（掩碼輸入）**
   - 使用掩碼字符的 `readLine()` 來隱藏輸入（例如，用於密碼）。
   - 範例：
     ```java
     String password = reader.readLine("輸入密碼: ", '*');
     ```
   - 顯示星號 (`*`) 而不是輸入的字符。

### 資源管理
對於健壯的應用程序，完成後關閉 `Terminal` 以釋放資源。由於 `Terminal` 實現了 `Closeable`，請使用 try-with-resources 塊：

```java
try (Terminal terminal = TerminalBuilder.builder().build()) {
    LineReader reader = LineReaderBuilder.builder()
        .terminal(terminal)
        .build();
    String line = reader.readLine("> ");
    System.out.println("您輸入了: " + line);
}
```

### 為什麼使用 `org.jline.reader`？
與基本輸入 `System.in` 和 `BufferedReader` 不同，`org.jline.reader` 提供了：
- **行編輯**：退格、光標移動等。
- **歷史記錄**：回顧先前的輸入。
- **自動完成**：建議選項。
- **跨平台終端處理**：在不同環境中一致工作。

### 注意事項
- 如果在 `LineReaderBuilder` 中未指定 `Terminal`，它會在內部創建一個默認的，因此 `LineReader reader = LineReaderBuilder.builder().build();` 適用於簡單情況。
- 避免從多個線程同時調用 `readLine()`，因為 `LineReader` 不適合並發讀取。
- 針對高級用例（例如多行輸入、自定義鍵綁定），探索 JLine 的其他功能，如解析器或鍵映射。

這涵蓋了使用 `org.jline.reader` 有效讀取 Java 控制台輸入的基本知識。從基本設置開始，並根據應用程序的需求添加功能，如歷史記錄或自動完成！