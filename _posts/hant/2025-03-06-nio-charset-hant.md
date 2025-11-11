---
audio: false
generated: true
lang: hant
layout: post
title: Java 中的字符編碼與解碼
translated: true
type: note
---

Java 中的 `java.nio.charset` 套件提供了處理字符編碼與解碼的工具，在處理不同格式或跨系統的文字資料時至關重要。以下是如何有效使用此套件的完整指南。

---

#### **什麼是 `java.nio.charset`？**
`java.nio.charset` 套件包含管理字符集（charsets）的類別，這些字符集定義了字符如何編碼為位元組及解碼回字符。這對於讀寫檔案、網路通訊或處理不同語言文字等任務極為關鍵，其中可能使用 UTF-8、ISO-8859-1 或其他編碼方式。

此套件中的主要類別是 `Charset`，並由其他類別如 `CharsetEncoder` 和 `CharsetDecoder` 支援更進階的使用情境。

---

#### **`java.nio.charset` 中的關鍵類別**
1. **`Charset`**  
   代表一種字符編碼（例如 UTF-8、ISO-8859-1）。您可以使用此類別來指定位元組與字符之間轉換的編碼方式。

2. **`StandardCharsets`**  
   一個工具類別，提供常用字符集的常數，例如 `StandardCharsets.UTF_8` 或 `StandardCharsets.ISO_8859_1`。它避免了手動查找字符集名稱的需求。

3. **`CharsetEncoder` 與 `CharsetDecoder`**  
   這些類別提供對編碼（字符到位元組）和解碼（位元組到字符）的細粒度控制，通常與 NIO 緩衝區（如 `ByteBuffer` 和 `CharBuffer`）一起使用。

---

#### **如何使用 `java.nio.charset`**

##### **1. 取得 `Charset` 實例**
要開始使用 `java.nio.charset`，您需要一個 `Charset` 物件。主要有兩種取得方式：

- **使用 `StandardCharsets`**（推薦用於常用字符集）：
  ```java
  import java.nio.charset.StandardCharsets;

  Charset charset = StandardCharsets.UTF_8; // 預定義的 UTF-8 字符集
  ```

- **使用 `Charset.forName()`**（適用於任何支援的字符集）：
  ```java
  import java.nio.charset.Charset;

  Charset charset = Charset.forName("UTF-8"); // UTF-8 字符集
  ```
  注意：如果字符集名稱無效，此方法會拋出 `UnsupportedCharsetException`，因此請適當處理：
  ```java
  try {
      Charset charset = Charset.forName("UTF-8");
  } catch (UnsupportedCharsetException e) {
      System.err.println("不支援的字符集：" + e.getMessage());
  }
  ```

---

##### **2. 基本用法：字串與位元組之間的轉換**
對於大多數應用程式，您可以將 `Charset` 與 `String` 類別一起使用來編碼或解碼文字。

- **將位元組解碼為字串**：
  使用特定字符集將位元組陣列轉換為 `String`：
  ```java
  byte[] bytes = {72, 101, 108, 108, 111}; // UTF-8 中的 "Hello"
  Charset charset = StandardCharsets.UTF_8;
  String text = new String(bytes, charset);
  System.out.println(text); // 輸出：Hello
  ```

- **將字串編碼為位元組**：
  使用特定字符集將 `String` 轉換為位元組陣列：
  ```java
  String text = "Hello, world!";
  Charset charset = StandardCharsets.UTF_8;
  byte[] bytes = text.getBytes(charset);
  ```

這些方法簡單且足以應對大多數使用情境，例如檔案 I/O 或基本文字處理。

---

##### **3. 使用讀取器與寫入器**
當處理串流（例如 `InputStream` 或 `OutputStream`）時，您可以將 `InputStreamReader` 和 `OutputStreamWriter` 與 `Charset` 一起使用來處理文字資料。

- **從 InputStream 讀取**：
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

- **寫入 OutputStream**：
  ```java
  import java.io.*;
  import java.nio.charset.StandardCharsets;

  OutputStream outputStream = new FileOutputStream("file.txt");
  OutputStreamWriter writer = new OutputStreamWriter(outputStream, StandardCharsets.UTF_8);
  writer.write("Hello, world!");
  writer.close();
  ```

注意：這些類別接受字符集名稱（例如 `"UTF-8"`）或 `Charset` 物件。

---

##### **4. 使用 `java.nio.file.Files` 簡化檔案操作**
自 Java 7 起，`java.nio.file` 套件提供了方便的方法來使用 `Charset` 讀寫檔案：

- **將檔案讀取為字串**：
  ```java
  import java.nio.file.*;
  import java.nio.charset.StandardCharsets;

  Path path = Paths.get("file.txt");
  String content = Files.readString(path, StandardCharsets.UTF_8);
  System.out.println(content);
  ```

- **將字串寫入檔案**：
  ```java
  import java.nio.file.*;
  import java.nio.charset.StandardCharsets;

  Path path = Paths.get("file.txt");
  String content = "Hello, world!";
  Files.writeString(path, content, StandardCharsets.UTF_8);
  ```

這些方法在內部處理編碼與解碼，使其成為簡單檔案操作的理想選擇。

---

##### **5. 進階用法：`CharsetEncoder` 與 `CharsetDecoder`**
對於需要更多控制的情境（例如使用 NIO 通道或處理部分資料），請使用 `CharsetEncoder` 和 `CharsetDecoder`。

- **使用 `CharsetEncoder` 編碼**：
  使用 NIO 緩衝區將字符轉換為位元組：
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
  將位元組轉換為字符：
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

這些類別在處理 `SocketChannel`、`FileChannel` 或其他 NIO 元件時非常有用，因為資料可能以區塊形式到達。

---

#### **最佳實踐**
- **始終指定字符集**：避免依賴 `Charset.defaultCharset()`，因為預設值因平台而異（例如 Linux 上為 UTF-8，Windows 上為 windows-1252）。明確指定字符集可確保行為一致：
  ```java
  // 避免這樣做：
  byte[] bytes = "Hello".getBytes(); // 使用平台預設字符集

  // 應該這樣做：
  byte[] bytes = "Hello".getBytes(StandardCharsets.UTF_8);
  ```

- **使用 `StandardCharsets`**：這樣更簡潔，且能避免因無效字符集名稱而導致的執行時例外。

- **處理例外**：使用 `Charset.forName()` 時，請捕捉 `UnsupportedCharsetException` 以處理不支援的字符集。

---

#### **總結**
要使用 `java.nio.charset`：
1. **取得 `Charset`**：使用 `StandardCharsets` 或 `Charset.forName()`。
2. **執行轉換**：
   - 使用 `String` 方法（`getBytes()`、建構函式）進行簡單的位元組-字符轉換。
   - 使用 `InputStreamReader`/`OutputStreamWriter` 處理串流。
   - 使用 `Files.readString()`/`writeString()` 進行檔案操作。
   - 使用 `CharsetEncoder`/`CharsetDecoder` 處理進階 NIO 情境。
3. **確保可移植性**：透過明確指定字符集。

此套件提供了靈活且強大的工具來管理字符編碼，使您的 Java 應用程式能夠穩健地處理多樣化的文字資料。