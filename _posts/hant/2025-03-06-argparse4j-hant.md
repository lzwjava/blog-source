---
audio: false
generated: true
lang: hant
layout: post
title: 解析 Java 命令行參數
translated: true
---

要使用 `net.sourceforge.argparse4j`，一個受 Python 的 `argparse` 啟發的 Java 庫，用於解析命令行參數，請按照以下步驟進行：

---

### 1. **添加依賴**
要在項目中包含 `argparse4j`，請將其添加為依賴。如果使用 Maven，請更新 `pom.xml` 如下：

```xml
<dependency>
    <groupId>net.sourceforge.argparse4j</groupId>
    <artifactId>argparse4j</artifactId>
    <version>0.9.0</version>
</dependency>
```

對於其他構建工具如 Gradle，請參考 [Maven Central Repository](https://central.sonatype.com/artifact/net.sourceforge.argparse4j/argparse4j) 以獲取等效配置。

---

### 2. **創建 `ArgumentParser` 物件**
首先，使用 `ArgumentParsers.newFor("prog").build()` 創建一個 `ArgumentParser` 實例，其中 `"prog"` 是您的程序名稱。您還可以添加描述並啟用自動幫助生成。

**範例：**
```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;

ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
    .defaultHelp(true)  // 啟用 -h/--help 選項
    .description("計算給定文件的校驗和。");
```

---

### 3. **添加參數**
使用 `parser.addArgument()` 定義您的程序將接受的命令行參數。您可以指定：
- **可選參數** (例如 `-t`, `--type`) 具有標誌、選擇、默認值和幫助文本。
- **位置參數** (例如 `file`) 具有可選的變長支持，使用 `.nargs("*")`。

**範例：**
```java
parser.addArgument("-t", "--type")
    .choices("SHA-256", "SHA-512", "SHA1")  // 限制為這些選項
    .setDefault("SHA-256")                  // 如果未提供則使用默認值
    .help("指定要使用的哈希函數");  // 幫助消息的描述

parser.addArgument("file")
    .nargs("*")                             // 接受零個或多個參數
    .help("計算校驗和的文件");    // 幫助消息的描述
```

---

### 4. **解析命令行參數**
使用 `parser.parseArgs()` 解析命令行參數（通常從 `main` 方法中傳遞的 `String[] args`），並將其包裹在 try-catch 塊中以優雅地處理解析錯誤。

**範例：**
```java
import net.sourceforge.argparse4j.inf.Namespace;
import net.sourceforge.argparse4j.inf.ArgumentParserException;

public class Checksum {
    public static void main(String[] args) {
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("計算給定文件的校驗和。");

        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("指定要使用的哈希函數");
        parser.addArgument("file").nargs("*")
            .help("計算校驗和的文件");

        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);  // 解析參數
        } catch (ArgumentParserException e) {
            parser.handleError(e);        // 打印錯誤和幫助消息
            System.exit(1);               // 錯誤時退出
        }
    }
}
```

---

### 5. **訪問解析值**
`parseArgs()` 方法返回一個包含解析參數值的 `Namespace` 物件。使用方法如 `getString()` 或 `getList()` 來檢索它們。

**範例：**
```java
String hashType = ns.getString("type");  // 例如 "SHA-256"
List<String> files = ns.getList("file"); // 文件名列表

System.out.println("哈希類型: " + hashType);
System.out.println("文件: " + files);
```

---

### 將所有內容結合起來
這裡有一個完整的範例：

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
            .description("計算給定文件的校驗和。");

        // 步驟 3：添加參數
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("指定要使用的哈希函數");
        parser.addArgument("file").nargs("*")
            .help("計算校驗和的文件");

        // 步驟 4：解析參數
        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);
        } catch (ArgumentParserException e) {
            parser.handleError(e);
            System.exit(1);
        }

        // 步驟 5：訪問解析值
        String hashType = ns.getString("type");
        List<String> files = ns.getList("file");

        // 範例輸出
        System.out.println("哈希類型: " + hashType);
        System.out.println("文件: " + files);
    }
}
```

---

### 額外功能
- **自動幫助**：使用 `-h` 或 `--help` 運行您的程序以查看生成的幫助消息。
- **子命令**：使用 `parser.addSubparsers()` 進行複雜命令（例如 `git commit`，`git push`）。
- **註解**：使用註解將參數綁定到類字段（請參閱用戶手冊以獲取詳細信息）。

有關更高級的使用方法，請參閱 [Argparse4j 用戶手冊](https://argparse4j.github.io/userguide.html)。

---

這種工作流程讓您可以輕鬆地在 Java 應用程序中解析和處理命令行參數，使用 `net.sourceforge.argparse4j`。