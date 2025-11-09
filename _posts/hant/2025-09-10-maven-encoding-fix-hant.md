---
audio: false
date: 2025-09-10
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 修復 Maven 平台編碼警告
translated: true
type: note
---

那個 Maven 警告表示您的專案建置過程依賴於**預設平台編碼**（例如在中文 Windows 系統上的 GBK）。如果其他開發人員或 CI 伺服器使用不同的編碼（如 Linux 上的 UTF-8），文字資源（Java 原始碼、properties、XML 等）可能會被錯誤讀取或編譯。

以下是解決方法：

---

### 1. 在 `pom.xml` 中設定原始碼編碼

在您專案的 `<properties>` 區段中明確宣告編碼：

```xml
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    <maven.compiler.encoding>UTF-8</maven.compiler.encoding>
</properties>
```

這能確保 Maven 無論在何種作業系統預設編碼下，都能以 UTF-8 一致地編譯原始碼並生成報告。

---

### 2. 設定編譯器外掛（如尚未設定）

某些舊版 Maven 設定需要在編譯器外掛下指定編碼：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.11.0</version>
            <configuration>
                <source>1.8</source>
                <target>1.8</target>
                <encoding>UTF-8</encoding>
            </configuration>
        </plugin>
    </plugins>
</build>
```

---

### 3. 檢查檔案編碼

* 確保您的 `.java`、`.properties`、`.yml` 等檔案以 UTF-8 格式儲存，而非 GBK
* 在 IntelliJ IDEA 或 VS Code 中，於專案設定中將**檔案編碼設為 UTF-8**
* 對於 Git，如有需要可透過 `.gitattributes` 強制實施一致編碼

---

### 4. 以明確編碼執行 Maven（可選）

您也可以在執行 Maven 時覆寫編碼設定：

```bash
mvn clean install -Dfile.encoding=UTF-8
```

但最佳實踐是在 `pom.xml` 中修復此問題，以確保所有使用者的一致性。

---

✅ 完成這些變更後，「platform dependent encoding GBK」警告應該會消失，您的 Spring + Maven 專案將能在不同機器間保持編碼安全。

您是否需要我進一步示範如何**安全地將現有 GBK 原始碼檔案轉換為 UTF-8**（讓您的程式庫保持整潔一致）？