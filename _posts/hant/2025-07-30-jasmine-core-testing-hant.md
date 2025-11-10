---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 茉莉核心測試框架概覽
translated: true
type: note
---

### Jasmine-Core
Jasmine-core 是 Jasmine 的核心函式庫，這是一個廣受歡迎的 JavaScript 測試框架。它提供了編寫行為驅動開發（BDD）測試的工具，包括測試套件（describe 區塊）、獨立測試（it 區塊）以及用於斷言的匹配器（例如 expect().toBe()）。它是獨立運行的，可在瀏覽器或 Node.js 環境中執行。

- **用途**：讓開發者能夠以可讀性高的規格化格式編寫和執行 JavaScript 應用程式的單元測試。
- **安裝方式**：通常透過 npm 安裝（`npm install jasmine-core`）。
- **使用範例**：您可以手動設定測試，或與 Karma 等工具整合。它是開源專案，在 GitHub（https://github.com/jasmine/jasmine）上維護，截至我最後更新時的最新版本約為 5.x。
- **相關性證明**：它是許多 JavaScript 測試設定的基礎依賴項，被 Angular 和 React 等專案用於 TDD/BDD 實踐。

### Karma-Jasmine-HTML-Reporter
karma-jasmine-html-reporter 是一個 NPM 套件，為 JavaScript 測試執行器 Karma 提供基於 HTML 的報告器外掛。它透過在用戶友好的網頁介面中顯示測試結果來與 Jasmine 測試整合，展示通過/失敗的測試、堆疊追蹤和計時資訊，所有內容都在測試執行期間實時更新並呈現在 HTML 頁面上。

- **用途**：透過提供基於瀏覽器的 HTML 使用者介面來增強測試反饋，而非僅依賴控制台輸出，使開發者更容易進行除錯。它依賴 jasmine-core 處理測試邏輯，並依賴 karma 在多個瀏覽器中執行測試。
- **安裝方式**：透過 npm 安裝（`npm install karma-jasmine-html-reporter --save-dev`）。
- **設定方式**：作為外掛和報告器添加到 Karma 的設定檔（例如 `karma.conf.js`）中。需要同時設定 karma 和 karma-jasmine。
- **相關性證明**：它是 Karma 使用者的熱門選擇，在官方 Karma 網站（https://karma-runner.github.io）上有相關文件，並經常更新。它不會改變測試執行，但能改善結果可視化，這在許多開發工作流程中都能看到。

這兩種工具經常一起使用：jasmine-core 處理測試邏輯，而 karma-jasmine-html-reporter 則在 Karma 執行的測試套件中可視化結果。如果您正在設定 JS 測試，建議從 Karma 的文件開始了解整合方式。