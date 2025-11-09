---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Maven 多模組依賴解析
translated: true
type: note
---

是的，正確無誤——在 Maven 多模組專案中，當一個模組（例如 EAR 模組）依賴另一個模組（例如 WAR 模組）時，Maven 預設會從本地的 `.m2/repository` 解析依賴項，而非直接從其他模組的 `target/` 目錄讀取。這是因為 Maven 將模組間的依賴視為標準的工件引用（如同外部函式庫），因此被依賴的工件必須先經過安裝（或至少完成打包並能透過建置反應器被發現）。

### 發生原因解析
- **本地儲存庫解析機制**：Maven 的依賴解析機制會優先從本地儲存庫尋找工件。`target/` 目錄僅在單一模組建置期間臨時使用，對於跨模組引用，Maven 要求工件必須先被「發布」（安裝）。
- **反應器建置雖有幫助，但並非萬能**：若從**父 POM 根目錄**執行 `mvn package`（或 `mvn install`），Maven 的反應器會自動依拓撲順序建置模組，在建置階段即時解析模組間依賴，無需顯式安裝即可從其他模組的新鮮 `target/` 輸出取得內容。但若**獨立建置**依賴模組（例如切至 ear-module 執行 `mvn package`），則無法偵測到 WAR 模組的 `target/` 內容——除非 WAR 工件已存在於 `.m2` 中，否則建置將失敗。

### 針對 WAR 至 EAR 打包的特殊說明
在 EAR 專案中：
- EAR 外掛（`maven-ear-plugin`）要求將 WAR（及其他模組）作為已解析的工件納入 EAR 封存（例如透過 EAR POM 中的 `<modules>` 設定）。
- 若 WAR 未被安裝，將出現「無法解析依賴項」或 EAR 中缺少模組的錯誤。

**解決方案**：若需獨立建置模組，通常需要先對「原始」（被依賴）模組執行 `mvn install`（或至少在完整反應器建置中執行 `mvn package`）。最佳實踐如下：
1. **建議方式：從父層級建置**：在專案根目錄執行 `mvn clean install`。此操作會將所有內容安裝至 `.m2` 並自動處理建置順序。
2. **若需分模組建置**：
   - 先執行 `cd war-module && mvn clean install`（將 WAR JAR 安裝至 `.m2`）。
   - 接著執行 `cd ear-module && mvn clean package`（或 `install`——EAR 通常僅需 `package`）。
3. **避免直接引用 Target 目錄**：切勿使用 `<systemPath>` 或檔案路徑直接指向 `target/` 目錄來規避此機制——此作法脆弱且會跳過 Maven 的校驗碼檢查與傳遞性處理。

此行為在近期 Maven 版本（截至 2025 年的 3.9.x）中均未改變。詳情可查閱官方多模組指南。

[建置生命週期簡介 - 多模組專案](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#multi-module)  
[Maven EAR 外掛文件](https://maven.apache.org/plugins/maven-ear-plugin/ear-mojo.html)