---
audio: false
generated: true
lang: hant
layout: post
title: 在 Java 中解析命令行參數
translated: true
type: note
---

要使用 `net.sourceforge.argparse4j`（一個受 Python `argparse` 啟發的 Java 命令列參數解析程式庫），請遵循以下步驟：

---

### 1. **添加依賴項**
要將 `argparse4j` 加入你的專案，請將其添加為依賴項。如果你使用 Maven，請在 `pom.xml` 中加入以下內容：

```xml
<dependency>
    <groupId>net.sourceforge.argparse4j</groupId>
    <artifactId>argparse4j</artifactId>
    <version>0.9.0</version>
</dependency>
```

對於其他建置工具如 Gradle，請查閱 [Maven Central Repository](https://central.sonatype.com/artifact/net.sourceforge.argparse4j/argparse4j) 以獲取等效配置。

---

### 2. **創建 `ArgumentParser` 物件**
首先使用 `ArgumentParsers.newFor("prog").build()` 創建一個 `ArgumentParser` 實例，其中 `"prog"` 是你的程式名稱。你還可以添加描述並啟用自動幫助生成。

**範例：**
```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;

ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
    .defaultHelp(true)  // 啟用 -h/--help 選項
    .description("Calculate checksum of given files.");
```

---

### 3. **添加參數**
使用 `parser.addArgument()` 定義你的程式將接受的命令列參數。你可以指定：
- **可選參數**（例如 `-t`、`--type`），包含標誌、選項、預設值和幫助文字。
- **位置參數**（例如 `file`），可選支援可變長度，使用 `.nargs("*")`。

**範例：**
```java
parser.addArgument("-t", "--type")
    .choices("SHA-256", "SHA-512", "SHA1")  // 限制為這些選項
    .setDefault("SHA-256")                  // 如果未提供時的預設值
    .help("Specify hash function to use");  // 幫助訊息的描述

parser.addArgument("file")
    .nargs("*")                             // 接受零個或多個參數
    .help("File to calculate checksum");    // 幫助訊息的描述
```

---

### 4. **解析命令列參數**
使用 `parser.parseArgs()` 解析命令列參數（通常從你的 `main` 方法作為 `String[] args` 傳入）。將其包裝在 try-catch 區塊中，以優雅地處理解析錯誤。

**範例：**
```java
import net.sourceforge.argparse4j.inf.Namespace;
import net.sourceforge.argparse4j.inf.ArgumentParserException;

public class Checksum {
    public static void main(String[] args) {
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("Calculate checksum of given files.");
        
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("Specify hash function to use");
        parser.addArgument("file").nargs("*")
            .help("File to calculate checksum");

        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);  // 解析參數
        } catch (ArgumentParserException e) {
            parser.handleError(e);        // 打印錯誤和幫助訊息
            System.exit(1);               // 發生錯誤時退出
        }
    }
}
```

---

### 5. **存取解析後的值**
`parseArgs()` 方法返回一個包含解析後參數值的 `Namespace` 物件。使用 `getString()` 或 `getList()` 等方法來獲取它們。

**範例：**
```java
String hashType = ns.getString("type");  // 例如 "SHA-256"
List<String> files = ns.getList("file"); // 檔案名稱列表

System.out.println("Hash Type: " + hashType);
System.out.println("Files: " + files);
```

---

### 完整範例
以下是一個完整範例：

```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;
import net.sourceforge.argparse4j.inf.ArgumentParserException;
import net.sourceforge.argparse4j.inf.Namespace;
import java.util.List;

public class Checksum {
    public static void main(String[] args) {
        // 步驟 2：創建解析器
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("Calculate checksum of given files.");

        // 步驟 3：添加參數
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("Specify hash function to use");
        parser.addArgument("file").nargs("*")
            .help("File to calculate checksum");

        // 步驟 4：解析參數
        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);
        } catch (ArgumentParserException e) {
            parser.handleError(e);
            System.exit(1);
        }

        // 步驟 5：存取解析後的值
        String hashType = ns.getString("type");
        List<String> files = ns.getList("file");

        // 範例輸出
        System.out.println("Hash Type: " + hashType);
        System.out.println("Files: " + files);
    }
}
```

---

### 額外功能
- **自動幫助**：使用 `-h` 或 `--help` 運行你的程式以查看生成的幫助訊息。
- **子命令**：對於複雜命令（例如 `git commit`、`git push`），使用 `parser.addSubparsers()`。
- **註解**：使用註解將參數綁定到類別欄位（詳見使用者手冊）。

有關更高級的用法，請參閱 [Argparse4j User Manual](https://argparse4j.github.io/userguide.html)。

---

這個工作流程讓你可以使用 `net.sourceforge.argparse4j` 輕鬆解析和處理 Java 應用程式中的命令列參數。