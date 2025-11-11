---
audio: false
generated: true
lang: hant
layout: post
title: 解析 Java 命令行選項
translated: true
type: note
---

JOptSimple 是一個專為簡化命令列選項解析而設計的 Java 函式庫。它能讓您以靈活直觀的方式定義及處理選項，例如標記（如 `-v` 代表詳細模式）和帶參數的選項（如 `--file input.txt`）。以下是如何有效使用 JOptSimple 的逐步指南。

---

### **步驟 1：將 JOptSimple 加入專案**
要使用 JOptSimple，首先需要將其加入您的 Java 專案。若使用 Maven，請在 `pom.xml` 中加入以下依賴項：

```xml
<dependency>
    <groupId>net.sf.jopt-simple</groupId>
    <artifactId>jopt-simple</artifactId>
    <version>5.0.4</version>
</dependency>
```

請務必到 Maven Central 檢查最新版本，因為 `5.0.4` 可能不是最新版。若使用 Gradle 等其他建置工具，可相應調整依賴項（例如 `implementation 'net.sf.jopt-simple:jopt-simple:5.0.4'`）。

---

### **步驟 2：建立 OptionParser**
JOptSimple 的核心是 `OptionParser` 類別，用於定義和解析命令列選項。請在 `main` 方法中建立其執行個體：

```java
import joptsimple.OptionParser;
import joptsimple.OptionSet;

public class MyApp {
    public static void main(String[] args) {
        OptionParser parser = new OptionParser();
        // 在此定義選項（參見步驟 3）
    }
}
```

---

### **步驟 3：定義命令列選項**
您可以使用 `accepts` 或 `acceptsAll` 方法定義選項。選項可以是標記（不帶參數）或需要參數的選項（例如檔案名稱或數字）。設定方式如下：

- **標記**：使用 `accepts` 定義單一選項名稱，或使用 `acceptsAll` 指定別名（例如 `-v` 和 `--verbose`）：
  ```java
  parser.acceptsAll(Arrays.asList("v", "verbose"), "啟用詳細模式");
  ```

- **帶參數的選項**：使用 `withRequiredArg()` 表示選項需要值，並可選用 `ofType()` 指定其類型：
  ```java
  parser.acceptsAll(Arrays.asList("f", "file"), "指定輸入檔案").withRequiredArg();
  parser.acceptsAll(Arrays.asList("c", "count"), "指定計數值").withRequiredArg().ofType(Integer.class).defaultsTo(0);
  ```

  - `defaultsTo(0)` 設定預設值（例如 `0`），當選項未提供時使用。
  - `ofType(Integer.class)` 確保參數被解析為整數。

- **說明選項**：加入說明標記（例如 `-h` 或 `--help`）以顯示使用資訊：
  ```java
  parser.acceptsAll(Arrays.asList("h", "help"), "顯示此說明訊息");
  ```

---

### **步驟 4：解析命令列參數**
將 `main` 方法中的 `args` 陣列傳遞給解析器以處理命令列輸入。這會回傳包含已解析選項的 `OptionSet` 物件：

```java
OptionSet options = parser.parse(args);
```

將其包覆在 `try-catch` 區塊中以處理解析錯誤（例如無效選項或缺少參數）：

```java
try {
    OptionSet options = parser.parse(args);
    // 處理選項（參見步驟 5）
} catch (Exception e) {
    System.err.println("錯誤：" + e.getMessage());
    try {
        parser.printHelpOn(System.err);
    } catch (IOException ex) {
        ex.printStackTrace();
    }
    System.exit(1);
}
```

---

### **步驟 5：存取已解析的選項**
使用 `OptionSet` 檢查標記、擷取選項值，並取得非選項參數：

- **檢查標記**：使用 `has()` 檢查標記是否存在：
  ```java
  boolean verbose = options.has("v");
  if (verbose) {
      System.out.println("已啟用詳細模式");
  }
  ```

- **取得選項值**：使用 `valueOf()` 擷取選項的參數，並在需要時轉換為適當類型：
  ```java
  String fileName = (String) options.valueOf("f"); // 若未指定則回傳 null
  int count = (Integer) options.valueOf("c");     // 因 defaultsTo(0) 而回傳 0
  ```

  若您指定了 `ofType()` 和 `defaultsTo()`，`valueOf()` 將回傳類型化值或預設值。

- **非選項參數**：使用 `nonOptionArguments()` 取得未綁定選項的參數（例如檔案清單）：
  ```java
  List<String> files = options.nonOptionArguments();
  System.out.println("檔案：" + files);
  ```

- **處理說明**：若存在說明選項，則列印使用資訊：
  ```java
  if (options.has("h")) {
      parser.printHelpOn(System.out);
      System.exit(0);
  }
  ```

---

### **範例：完整整合**
以下是一個完整範例，接受詳細模式標記、計數選項和檔案清單：

```java
import joptsimple.OptionParser;
import joptsimple.OptionSet;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

public class MyApp {
    public static void main(String[] args) {
        OptionParser parser = new OptionParser();
        parser.acceptsAll(Arrays.asList("v", "verbose"), "啟用詳細模式");
        parser.acceptsAll(Arrays.asList("c", "count"), "指定計數值")
              .withRequiredArg()
              .ofType(Integer.class)
              .defaultsTo(0);
        parser.acceptsAll(Arrays.asList("h", "help"), "顯示此說明訊息");

        try {
            OptionSet options = parser.parse(args);

            if (options.has("h")) {
                parser.printHelpOn(System.out);
                System.exit(0);
            }

            boolean verbose = options.has("v");
            int count = (Integer) options.valueOf("c");
            List<String> files = options.nonOptionArguments();

            if (verbose) {
                System.out.println("已啟用詳細模式");
            }
            System.out.println("計數值：" + count);
            System.out.println("檔案：" + files);

        } catch (Exception e) {
            System.err.println("錯誤：" + e.getMessage());
            try {
                parser.printHelpOn(System.err);
            } catch (IOException ex) {
                ex.printStackTrace();
            }
            System.exit(1);
        }
    }
}
```

執行：`java MyApp -v -c 5 file1 file2`，輸出結果為：
```
已啟用詳細模式
計數值：5
檔案：[file1, file2]
```

執行 `-h` 時，將顯示包含所有已定義選項的使用說明訊息。

---

### **進階功能**
- **多重數值**：允許選項多次出現（例如 `-I dir1 -I dir2`）：
  ```java
  parser.accepts("I").withRequiredArg().ofType(String.class);
  List<String> includes = options.valuesOf("I"); // 回傳清單
  ```

- **可選參數**：若參數非必需，可使用 `withOptionalArg()` 替代 `withRequiredArg()`：
  ```java
  parser.accepts("o").withOptionalArg().ofType(String.class);
  ```

- **錯誤處理**：JOptSimple 在解析錯誤時會拋出 `OptionException`，您可捕捉此例外以提供使用者友善的錯誤訊息。

---

### **總結**
JOptSimple 讓 Java 命令列選項處理變得簡單。您需要：
1. 將函式庫加入專案。
2. 建立 `OptionParser` 並定義選項（標記、參數、預設值）。
3. 將 `args` 陣列解析為 `OptionSet`。
4. 使用 `OptionSet` 存取標記、數值和非選項參數。
5. 視需要處理錯誤並提供說明。

掌握這些基礎後，您就能為應用程式建置穩健的命令列介面！