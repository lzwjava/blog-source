---
audio: false
generated: true
lang: hant
layout: post
title: 在 Java 中讀取控制台輸入
translated: true
type: note
---

要在 Java 中使用 `org.jline.reader` 套件（屬於 JLine 函式庫，用於處理具備進階功能的控制台輸入，例如行編輯、歷史記錄和自動完成），請遵循以下步驟。本指南提供完整且實用的方法助您入門。

### 前置準備
請確保已將 JLine 函式庫加入專案。若使用 Maven，請在 `pom.xml` 中加入以下依賴項：

```xml
<dependency>
    <groupId>org.jline</groupId>
    <artifactId>jline</artifactId>
    <version>3.21.0</version> <!-- 請使用最新版本 -->
</dependency>
```

### 使用 `org.jline.reader` 的基本步驟

1. **建立 Terminal 實例**
   - 使用 `org.jline.terminal` 中的 `TerminalBuilder` 類別來建立 `Terminal` 物件。這代表將讀取輸入的控制台環境。
   - 範例：
     ```java
     import org.jline.terminal.Terminal;
     import org.jline.terminal.TerminalBuilder;

     Terminal terminal = TerminalBuilder.builder().build();
     ```
   - `build()` 方法會建立一個適用於大多數環境的預設終端機。您可以進一步自訂（例如設定終端機類型），但預設值通常已足夠。

2. **建立 LineReader 實例**
   - 使用 `org.jline.reader` 中的 `LineReaderBuilder` 類別來建立 `LineReader` 物件，並將 `Terminal` 實例傳入。
   - `LineReader` 是使用 JLine 功能讀取使用者輸入的主要介面。
   - 範例：
     ```java
     import org.jline.reader.LineReader;
     import org.jline.reader.LineReaderBuilder;

     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .build();
     ```

3. **讀取使用者輸入**
   - 使用 `LineReader` 的 `readLine()` 方法讀取使用者輸入的一行文字。您可以選擇性指定要顯示的提示符號。
   - 範例：
     ```java
     String line = reader.readLine("> ");
     ```
   - 這會顯示 `> ` 作為提示符號，等待使用者輸入，並在使用者按下 Enter 時回傳輸入的字串。

### 簡單範例
以下是一個完整的最小範例，會循環讀取使用者輸入，直到使用者輸入 "exit"：

```java
import org.jline.reader.LineReader;
import org.jline.reader.LineReaderBuilder;
import org.jline.terminal.Terminal;
import org.jline.terminal.TerminalBuilder;

public class ConsoleExample {
    public static void main(String[] args) throws Exception {
        // 建立 Terminal
        Terminal terminal = TerminalBuilder.builder().build();
        
        // 建立 LineReader
        LineReader reader = LineReaderBuilder.builder()
            .terminal(terminal)
            .build();
        
        // 循環讀取輸入
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

- **輸出**：執行時會顯示 `> ` 提示符號。您可以輸入文字、使用退格鍵或方向鍵進行編輯（這是使用 `System.in` 不易實現的功能），然後按下 Enter。輸入 "exit" 會結束程式。

### 選用功能
您可以透過以下附加功能增強 `LineReader`：

#### 1. **啟用指令歷史記錄**
   - 加入 `History` 物件以儲存和重新呼叫先前的輸入（例如使用上/下方向鍵）。
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
   - 現在使用者可以瀏覽其輸入歷史記錄。

#### 2. **加入自動完成功能**
   - 實作 `Completer` 以在使用者按下 Tab 時建議完成選項。
   - 使用簡單字串完成器的範例：
     ```java
     import org.jline.reader.Completer;
     import org.jline.reader.impl.completer.StringsCompleter;

     Completer completer = new StringsCompleter("foo", "bar", "baz");
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .completer(completer)
         .build();
     ```
   - 輸入 "f" 並按下 Tab 會建議 "foo"。

#### 3. **讀取密碼（遮罩輸入）**
   - 使用帶有遮罩字元的 `readLine()` 來隱藏輸入（例如用於密碼）。
   - 範例：
     ```java
     String password = reader.readLine("輸入密碼: ", '*');
     ```
   - 顯示星號（`*`）而非輸入的字元。

### 資源管理
為確保應用程式的穩健性，請在完成後關閉 `Terminal` 以釋放資源。由於 `Terminal` 實作了 `Closeable`，請使用 try-with-resources 區塊：

```java
try (Terminal terminal = TerminalBuilder.builder().build()) {
    LineReader reader = LineReaderBuilder.builder()
        .terminal(terminal)
        .build();
    String line = reader.readLine("> ");
    System.out.println("您輸入了: " + line);
}
```

### 為何使用 `org.jline.reader`？
與使用 `System.in` 和 `BufferedReader` 的基本輸入不同，`org.jline.reader` 提供：
- **行編輯**：退格鍵、游標移動等。
- **歷史記錄**：重新呼叫先前的輸入。
- **自動完成**：自動建議選項。
- **跨平台終端機處理**：在不同環境中保持一致運作。

### 注意事項
- 若未在 `LineReaderBuilder` 中指定 `Terminal`，它會在內部建立預設值，因此 `LineReader reader = LineReaderBuilder.builder().build();` 在簡單情況下也能運作。
- 避免同時從多個執行緒呼叫 `readLine()`，因為 `LineReader` 不支援並行讀取的執行緒安全。
- 對於進階使用案例（例如多行輸入、自訂按鍵綁定），請探索 JLine 的附加功能，例如解析器或按鍵對應。

這涵蓋了使用 `org.jline.reader` 在 Java 中有效讀取控制台輸入的基本要點。請從基本設定開始，並根據應用程式需求加入歷史記錄或自動完成等功能！