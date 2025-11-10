---
audio: false
generated: true
lang: hant
layout: post
title: 在 Ubuntu 22.04 上尋找您的 OpenJDK 21.0.7 安裝位置
translated: true
type: note
---

您執行的 `java --version` 指令顯示系統中已安裝 OpenJDK 21.0.7，這是專為 Ubuntu 22.04 打包的版本。此輸出確認 Java Development Kit (JDK) 已安裝並可從命令列存取。

Java 安裝位置通常可透過檢查 `java` 二進位檔所在路徑來確認。由於您使用的是 Ubuntu 系統，OpenJDK 很可能安裝在標準系統目錄中，例如 `/usr/lib/jvm/`。

若要定位 Java 安裝的具體路徑：

1. **尋找 `java` 二進位檔路徑**：
   在終端機中執行以下指令：
   ```bash
   which java
   ```
   這可能會輸出類似 `/usr/bin/java` 的路徑。這是指向實際 Java 二進位檔的符號連結。

2. **追蹤符號連結至實際位置**：
   由於 `/usr/bin/java` 通常是符號連結，您可透過以下指令查找實際安裝目錄：
   ```bash
   readlink -f $(which java)
   ```
   這可能會輸出類似 `/usr/lib/jvm/java-21-openjdk-amd64/bin/java` 的路徑，表示 JDK 安裝在 `/usr/lib/jvm/java-21-openjdk-amd64/` 目錄中。

3. **驗證安裝目錄**：
   您可以列出 JVM 目錄的內容來確認：
   ```bash
   ls /usr/lib/jvm/
   ```
   您應該會看到類似 `java-21-openjdk-amd64` 的目錄，其中包含 OpenJDK 安裝檔案。

### 總結
您的 Java 安裝位置很可能位於 `/usr/lib/jvm/java-21-openjdk-amd64/`（或 `/usr/lib/jvm/` 下的類似目錄）。您執行的 `java` 指令是指向該目錄內 `java` 二進位檔的符號連結。若需確認確切路徑，請使用 `readlink -f $(which java)` 指令。