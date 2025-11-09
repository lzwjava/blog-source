---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hant
layout: post
title: 混合式 Java 開發策略
translated: true
type: note
---

簡短看法：對於大型 Java 程式碼庫，**混合使用**效果最佳。將 **VS Code** 作為你的 AI 優先操作平台（Claude Code + Copilot = 更快的迭代和樣板程式碼處理），並保留 **IntelliJ IDEA** 用於「精細手術」（深度重構、程式碼檢查、進階 Spring/Gradle/Maven 精靈）。你無需固守單一信仰。🙂

以下是我的思考方式——不用表格，只談要點：

### VS Code 的優勢所在

* **AI 工作流程**：Copilot 的行內程式碼補全在 VS Code 中依然最出色，而且 Claude Code 的儲存庫層級推理在該環境中反應更靈敏。非常適合用於起草服務、測試、映射器、SQL 以及快速重新設計。
* **輕量級與模組化**：你只需按需添加功能。在大型單體儲存庫中，冷啟動和記憶體使用更為友善。
* **「跳轉」+ LSP**：搭配 Java 擴充功能，「移至定義/實作」、型別階層、呼叫階層和符號搜尋等功能足以應付日常開發。

推薦擴充功能（依 ID 搜尋）：

* `vscjava.vscode-java-pack`（包含以下大部分功能）
* `redhat.java` (Java 語言支援)
* `vscjava.vscode-java-debug` / `vscjava.vscode-java-test`
* `vscjava.vscode-maven` / `vscjava.vscode-gradle`
* `vscjava.vscode-spring-boot-dashboard` + `vscjava.vscode-spring-initializr`
* `sonarsource.sonarlint-vscode`（靜態檢查）
* `streetsidesoftware.code-spell-checker`（在 JavaDocs 中意外地好用）
* Claude Code + GitHub Copilot

大型專案效能調校（放入 `.vscode/settings.json`）：

```json
{
  "java.maxConcurrentBuilds": 4,
  "java.jdt.ls.vmargs": "-Xms512m -Xmx4g -XX:+UseG1GC -XX:+UseStringDeduplication",
  "java.errors.incompleteClasspath.severity": "ignore",
  "java.referencesCodeLens.enabled": false,
  "java.implementationsCodeLens.enabled": false,
  "files.watcherExclude": {
    "**/target/**": true,
    "**/.gradle/**": true,
    "**/node_modules/**": true
  }
}
```

提示：

* 以 **Gradle** 或 **Maven** 專案形式匯入（盡可能避免混合建置）。
* 啟用 **Spring Boot Dashboard** 以執行/偵錯多個服務。
* 讓 Claude/Copilot 起草類別和測試，但使用 **SonarLint** 和單元測試作為安全防護。

### IntelliJ IDEA 依然領先的領域

* **重構深度與準確性**：跨大型階層重新命名/移動/提取、泛型繁重的 API、Lombok、XML 配置，甚至 Spring bean 裝配——IDEA 的語意模型難以超越。
* **程式碼檢查與快速修復**：內建的程式碼檢查（以及結構化搜尋/取代）能比大多數 VS Code 設定捕捉到更細微的程式碼異味。
* **UML 與導航便利性**：資料流追蹤、相依性圖表和進階搜尋範圍在複雜領域中能節省大量時間。

實用模式：

* 在 **VS Code** 中使用 Claude/Copilot 進行**探索 + 腳手架搭建 + 重複性編輯**。
* 當需要進行**非平凡重構**時（例如，拆分核心模組、跨 40 個模組變更 API 合約、遷移 Spring 配置），在 IDEA 中開啟同一儲存庫，讓它索引一次，安全地執行重構，推送後再返回 VS Code。

### 關於「Codex」

OpenAI 舊版的 **Codex** 模型已於一段時間前停止服務。現今你主要會使用 **GitHub Copilot**（底層由 OpenAI 技術驅動）和 **Claude Code**。可將「Codex」視為歷史產物——你當前的技術堆疊應為 **Copilot + Claude Code**。

### VS Code 中的靜態分析與程式碼品質

* **SonarLint** 在 VS Code 中提供近乎 IDEA 的體驗；可與 CI 中的 SonarQube/SonarCloud 門禁搭配使用。
* 透過 Gradle/Maven 外掛加入 **SpotBugs** 和 **Checkstyle**，以便在 CI 中執行品質檢查（不僅僅在本地）。
* 使用 **JUnit** 測試總管和 **Coverage Gutters** 擴充功能來維持緊湊的紅綠重構循環。

### Spring/企業級特定事項

* VS Code 的 **Spring 工具** 對於執行/偵錯、執行器端點和屬性提示很有幫助。對於複雜的自動配置或元註解，IDEA 在解析方面仍然更可靠——當註解顯得「神秘」時，請使用它。
* 對於 **Gradle** 多模組龐大專案：保持 daemon + 並行建置開啟，並考慮使用複合建置來限制工作區大小。

### 可擴展的 AI 工作流程

* 使用 **Copilot 行內補全**進行輸入時的微小編輯。
* 使用 **Claude Code** 聊天進行儲存庫層級的推理（「如果我變更 `LedgerPosting` 的建構函式，會有哪些副作用？」/「起草一個 PR 來將我們的自訂重試邏輯替換為 resilience4j」）。
* 要求模型產生**重構計劃 + 檢查清單**；然後以小型、可審查的提交來套用變更。
* 保持**模型輸出受測試覆蓋**：要求 AI 產生的 PR 中包含單元/整合測試的差異。

### 那麼…你應該以哪個為主？

* 如果你日常工作是**編碼 + 迭代 + 大量 AI 輔助** → 目前以 **VS Code** 作為主要編輯器感覺更佳。
* 如果你日常工作是**架構設計 + 大型重構 + 偵錯框架邊緣案例** → 在這些時候保持 **IntelliJ** 開啟。
* 許多資深工程師會兩者交替使用。這並非效率低下，而是根據風險等級使用合適的工具。

如果你需要，我可以為你的單體儲存庫生成一次性的 **VS Code Java 啟動設定**（extensions.json、settings.json、推薦的 tasks/launch 配置）——以及一份簡短的 IDEA 檢查清單，用於「呼叫重型機械」的時刻。