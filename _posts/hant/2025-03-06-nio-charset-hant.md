---
audio: false
generated: true
lang: hant
layout: post
title: 字符編碼與解碼於Java
translated: true
---

`java.nio.charset` 套件在 Java 中提供了處理字符編碼和解碼的工具，這在處理不同格式的文本數據或跨不同系統時是必不可少的。以下是如何有效使用此套件的全面指南。

---

#### **什麼是 `java.nio.charset`？**
`java.nio.charset` 套件包含管理字符集（charsets）的類，這些字符集定義了如何將字符編碼為字節並將其解碼回字符。這對於讀取和寫入文件、網絡通信或處理不同語言的文本等任務至關重要，這些任務可能會使用 UTF-8、ISO-8859-1 或其他編碼。

此套件的主要類是 `Charset`，由 `CharsetEncoder` 和 `CharsetDecoder` 等附加類支持，用於更高級的用例。

---

#### **`java.nio.charset` 中的關鍵類**
1. **`Charset`**
   表示字符編碼（例如 UTF-8、ISO-8859-1）。使用此類指定字節和字符之間的轉換編碼。

2. **`StandardCharsets`**
   提供常用字符集的常量的實用程序類，例如 `StandardCharsets.UTF_8` 或 `StandardCharsets.ISO_8859_1`。它消除了手動查找字符集名稱的需求。

3. **`CharsetEncoder` 和 `CharsetDecoder`**
   這些類提供對編碼（字符到字節）和解碼（字節到字符）的精細控制，通常與 NIO 緩衝區（例如 `ByteBuffer` 和 `CharBuffer`）一起使用。

---

#### **如何使用 `java.nio.charset`**

##### **1. 获取一個 `Charset` 實例**
要開始使用 `java.nio.charset`，您需要一個 `Charset` 對象。有兩種主要方法可以獲取一個：

- **使用 `StandardCharsets`** （建議用於常用字符集）：
  ```java
  import java.nio.charset.StandardCharsets;

  Charset charset = StandardCharsets.UTF_8; // 預定義的 UTF-8 字符集
  ```

- **使用 `Charset.forName()`** （用於任何支持的字符集）：
  ```java
  import java.nio.charset.Charset;

  Charset charset = Charset.forName("UTF-8"); // UTF-8 字符集
  ```
  注意：如果字符集名稱無效，這將引發 `UnsupportedCharsetException`，因此請適當處理：
  ```java
  try {
      Charset charset = Charset.forName("UTF-8");
  } catch (UnsupportedCharsetException e) {
      System.err.println("字符集不受支持：" + e.getMessage());
  }
  ```

---

##### **2. 基本用法：在字符串和字節之間轉換**
對於大多數應用程序，您可以使用 `Charset` 及 `String` 類來編碼或解碼文本。

- **將字節解碼為字符串**：
  使用特定字符集將字節數組轉換為 `String`：
  ```java
  byte[] bytes = {72, 101, 108, 108, 111}; // "Hello" 以 UTF-8 編碼
  Charset charset = StandardCharsets.UTF_8;
  String text = new String(bytes, charset);
  System.out.println(text); // 輸出：Hello
  ```

- **將字符串編碼為字節**：
  使用特定字符集將 `String` 轉換為字節數組：
  ```java
  String text = "Hello, world!";
  Charset charset = StandardCharsets.UTF_8;
  byte[] bytes = text.getBytes(charset);
  ```

這些方法簡單且對於大多數用例（例如文件 I/O 或基本文本處理）已經足夠。

---

##### **3. 使用讀取器和寫入器**
在處理流（例如 `InputStream` 或 `OutputStream`）時，您可以使用 `InputStreamReader` 和 `OutputStreamWriter` 及 `Charset` 來處理文本數據。

- **從 `InputStream` 讀取**：
  ```java
  import java.io.*;
  import java.nio.charset.StandardCharsets;

  InputStream inputStream = new FileInputStream("file.txt");
  InputStreamReader reader = new InputStreamReader(inputStream, StandardCharsets.UTF_8);
  int data;
  while ((data = reader.read()) != -1) {
      System.out.print((char) data);
  }
  reader.close();
  ```

- **寫入 `OutputStream`**：
  ```java
  import java.io.*;
  import java.nio.charset.StandardCharsets;

  OutputStream outputStream = new FileOutputStream("file.txt");
  OutputStreamWriter writer = new OutputStreamWriter(outputStream, StandardCharsets.UTF_8);
  writer.write("Hello, world!");
  writer.close();
  ```

注意：這些類接受字符集名稱（例如 `"UTF-8"`）或 `Charset` 對象。

---

##### **4. 使用 `java.nio.file.Files` 簡化文件操作**
自 Java 7 起，`java.nio.file` 套件提供了使用 `Charset` 讀取和寫入文件的便捷方法：

- **將文件讀取為字符串**：
  ```java
  import java.nio.file.*;
  import java.nio.charset.StandardCharsets;

  Path path = Paths.get("file.txt");
  String content = Files.readString(path, StandardCharsets.UTF_8);
  System.out.println(content);
  ```

- **將字符串寫入文件**：
  ```java
  import java.nio.file.*;
  import java.nio.charset.StandardCharsets;

  Path path = Paths.get("file.txt");
  String content = "Hello, world!";
  Files.writeString(path, content, StandardCharsets.UTF_8);
  ```

這些方法在內部處理編碼和解碼，使其非常適合簡單的文件操作。

---

##### **5. 高級用法：`CharsetEncoder` 和 `CharsetDecoder`**
對於需要更多控制的情況（例如與 NIO 通道一起工作或處理部分數據），請使用 `CharsetEncoder` 和 `CharsetDecoder`。

- **使用 `CharsetEncoder` 編碼**：
  使用 NIO 緩衝區將字符轉換為字節：
  ```java
  import java.nio.*;
  import java.nio.charset.*;

  Charset charset = StandardCharsets.UTF_8;
  CharsetEncoder encoder = charset.newEncoder();
  CharBuffer charBuffer = CharBuffer.wrap("Hello");
  ByteBuffer byteBuffer = encoder.encode(charBuffer);
  byte[] bytes = byteBuffer.array();
  ```

- **使用 `CharsetDecoder` 解碼**：
  將字節轉換為字符：
  ```java
  import java.nio.*;
  import java.nio.charset.*;

  Charset charset = StandardCharsets.UTF_8;
  CharsetDecoder decoder = charset.newDecoder();
  ByteBuffer byteBuffer = ByteBuffer.wrap(new byte[]{72, 101, 108, 108, 111});
  CharBuffer charBuffer = decoder.decode(byteBuffer);
  String text = charBuffer.toString();
  System.out.println(text); // 輸出：Hello
  ```

這些類在與 `SocketChannel`、`FileChannel` 或其他 NIO 組件一起工作時非常有用，這些組件的數據以塊的形式到達。

---

#### **最佳實踐**
- **始終指定字符集**：避免依賴 `Charset.defaultCharset()`，因為默認值會因平台而異（例如，Linux 上的 UTF-8，Windows 上的 windows-1252）。明確指定字符集可以確保一致的行為：
  ```java
  // 避免這樣：
  byte[] bytes = "Hello".getBytes(); // 使用平台默認字符集

  // 這樣做：
  byte[] bytes = "Hello".getBytes(StandardCharsets.UTF_8);
  ```

- **使用 `StandardCharsets`**：它更乾淨，並避免了無效字符集名稱的運行時異常。

- **處理異常**：在使用 `Charset.forName()` 時，捕獲 `UnsupportedCharsetException` 以處理不受支持的字符集。

---

#### **總結**
要使用 `java.nio.charset`：
1. **獲取一個 `Charset`** 使用 `StandardCharsets` 或 `Charset.forName()`。
2. **執行轉換**：
   - 使用 `String` 方法（`getBytes()`、構造函數）進行簡單的字節-字符轉換。
   - 使用 `InputStreamReader`/`OutputStreamWriter` 進行流操作。
   - 使用 `Files.readString()`/`writeString()` 進行文件操作。
   - 使用 `CharsetEncoder`/`CharsetDecoder` 進行高級 NIO 情況。
3. **確保可攜性** 通過明確指定字符集。

此套件提供了靈活且強大的工具來管理字符編碼，使您的 Java 應用程序強大且與多樣化的文本數據兼容。