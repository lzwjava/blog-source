---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hant
layout: post
title: 解決缺失的 JaCoCo 執行數據文件
translated: true
type: note
---

要生成 JaCoCo 執行資料檔案（通常稱為 **'.exec' 檔案**），您需要在執行測試時附加 JaCoCo 代理程式。日誌訊息「Skipping JaCoCo execution due to missing execution data file」表示 `report` 目標在 `prepare-agent` 目標未成功執行的情況下被執行。

-----

### 步驟 1：配置 JaCoCo Maven 插件

首先，請確保您的 `pom.xml` 檔案已正確配置 JaCoCo Maven 插件。配置應類似以下內容：

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.12</version>
    <executions>
        <execution>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
        </execution>
        <execution>
            <id>report</id>
            <phase>test</phase>
            <goals>
                <goal>report</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

**`prepare-agent`** 目標至關重要，它負責設置 JaCoCo 運行時代理程式。該代理程式在測試運行期間對您的程式碼進行檢測，以收集覆蓋率資料。

-----

### 步驟 2：執行測試

配置插件後，運行您的 Maven 構建。執行測試並生成報告的典型指令是：

`mvn clean install`

當您運行此指令時，Maven 會首先執行 `prepare-agent` 目標，將 JaCoCo 代理程式附加到 JVM。接著，在 `test` 階段運行時，代理程式會記錄程式碼覆蓋率資料並將其保存到檔案中，通常位於 **`target/jacoco.exec`**。隨後執行的 `report` 目標會讀取此 `.exec` 檔案並生成最終的 HTML 或 XML 報告。

如果您仍然遇到問題，請檢查以下事項：

  * **專案結構**：確保您的測試位於標準的 Maven 目錄 `src/test/java` 中。
  * **測試失敗**：如果測試失敗，構建可能會在生成 `.exec` 檔案之前停止。請先解決所有測試失敗問題。
  * **版本不匹配**：請確保 JaCoCo 插件版本與您的 Maven 和 Java 版本相容。