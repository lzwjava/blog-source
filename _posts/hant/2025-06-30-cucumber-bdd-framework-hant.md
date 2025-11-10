---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: 黃瓜框架用於行為驅動開發測試
translated: true
type: note
---

## 什麼是 Cucumber 框架？

Cucumber 框架是一個開源工具，旨在支援軟體開發中行為驅動開發（BDD）的自動化驗收測試。它允許團隊使用稱為 Gherkin 的結構化語法，以純英文編寫測試案例，這有助於彌合非技術利害關係人（如業務分析師或產品經理）與開發人員或測試人員之間的差距，促進更好的協作並確保測試符合業務需求。[1][2][3]

### 主要功能及其如何支援測試

Cucumber 能夠以日常語言編寫可執行的規格，使測試易於閱讀，並作為應用程式行為的活文件。它主要不是用於單元測試，而是在端到端（E2E）測試、整合測試和驗收測試方面表現出色。[2][4]

- **Gherkin 語言**：這是 Cucumber 用於編寫場景的語法。它使用關鍵字如 `Feature`、`Scenario`、`Given`、`When` 和 `Then` 來描述功能和行為。例如：

  ```
  Feature: 用戶登入

    Scenario: 無效登入
      Given 用戶位於登入頁面
      When 用戶輸入無效憑證
      Then 應顯示錯誤訊息
  ```

  Gherkin 將純文字結構化為 Cucumber 可以解析和執行的步驟，並支援多種口語語言。[2][5]

- **執行機制**：測試分為兩個主要檔案：
  - **功能檔案** (.feature)：包含 Gherkin 場景，描述軟體應做什麼。
  - **步驟定義檔案**：以程式語言（如 Ruby、Java、Python、JavaScript）編寫，這些檔案將每個 Gherkin 步驟映射到與應用程式互動的實際程式碼，例如通過 Selenium 自動化網頁互動或 API 呼叫。

  執行時，Cucumber 會將功能檔案中的步驟與相應的定義匹配，並驗證應用程式的行為。[3]

- **BDD 支援**：Cucumber 通過鼓勵探索、協作和基於範例的測試來推廣 BDD。它通常與 Selenium（用於網頁自動化）或 JUnit（用於 Java 基礎測試）等工具一起使用。[2][6][7]

### 在測試中使用 Cucumber 的好處

- **可讀性和可訪問性**：純語言使測試對任何人都易於理解，減少團隊之間的誤解。
- **協作**：增強開發人員、測試人員和業務利害關係人之間的溝通。
- **可重用性**：步驟定義可以在多個場景中重複使用，提高效率。
- **活文件**：測試自動記錄系統行為，並隨著功能變化而更新。
- **可擴展性**：支援與持續整合（CI）工具（如 Jenkins 或 GitHub Actions）整合，用於自動化管道。[3][8]

然而，它可能存在一些限制，例如由於 Gherkin 解析導致執行速度較慢，以及對於簡單的單元測試設置複雜，因此更適合廣泛的驗收測試，而不是細粒度的程式碼級驗證。

### 如何開始使用 Cucumber 進行測試

1. **安裝 Cucumber**：根據程式語言，安裝相關的 Cucumber 庫（例如通過 RubyGems 用於 Ruby，通過 Maven 用於 Java）。
2. **編寫功能檔案**：使用 Gherkin 創建一個包含場景的 `.feature` 檔案，如上所示。
3. **定義步驟**：在步驟定義檔案中實現每個步驟，使用斷言（例如通過 JUnit 或 RSpec）來檢查應用程式響應。
4. **執行測試**：通過命令行（例如 Ruby 的 `cucumber`）或整合到 IDE/建置工具中執行。結果以 JSON 或 HTML 等格式輸出，用於報告。
5. **與其他工具整合**：與 Selenium 配對用於瀏覽器測試，或與 REST 庫配對用於 API 驗證。

有關詳細指南，請參考官方資源或像 BrowserStack 這樣的平台，它提供基於雲端的測試環境，可以在多個瀏覽器和設備上執行 Cucumber 腳本。[3][7]

該框架在行業中廣泛使用，通過協作式自動化測試確保軟體符合用戶期望。[4]

引用文獻：
[1] https://cucumber.io/
[2] https://cucumber.io/docs/
[3] https://www.browserstack.com/guide/learn-about-cucumber-testing-tool
[4] https://en.wikipedia.org/wiki/Cucumber_(software)
[5] https://testgrid.io/blog/cucumber-testing/
[6] https://www.headspin.io/blog/cucumber-testing-a-complete-guide
[7] https://www.accelq.com/blog/cucumber-testing-framework/
[8] https://www.geeksforgeeks.org/software-testing/what-is-cucumber-framework/