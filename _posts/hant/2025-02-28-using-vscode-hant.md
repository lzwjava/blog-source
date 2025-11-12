---
audio: false
generated: true
lang: hant
layout: post
title: 使用 VS Code
translated: true
type: note
---

### 重點摘要
- VS Code 是一款適用於 Windows、macOS 和 Linux 的熱門免費程式碼編輯器，支援多種程式語言。
- 根據開發者的使用情況，其最實用的功能似乎包括語法突顯、偵錯和 Git 整合。
- 證據顯示其內建超過 30 項功能可提升生產力，例如多重游標編輯和遠端開發。

---

### VS Code 入門指南
Visual Studio Code（VS Code）是由 Microsoft 開發的輕量級開源程式碼編輯器，非常適合在 Windows、macOS 和 Linux 上進行編程。請先從官方網站[下載](https://code.visualstudio.com/download)。安裝完成後，啟動 VS Code 即可開始編寫程式碼。

#### 基本使用
- **建立或開啟檔案**：使用 `檔案 > 新增檔案`（Windows/Linux 上按 `Ctrl + N`，macOS 上按 `Cmd + N`）來建立新檔案；使用 `檔案 > 開啟`（或 `Ctrl + O`、`Cmd + O`）來開啟現有檔案。使用 `Ctrl + S` 或 `Cmd + S` 儲存。
- **編輯程式碼**：享受語法突顯、自動縮排和括號匹配等功能，以提高可讀性。使用程式碼片段快速插入程式碼，並使用多重游標編輯（`Alt + 點擊`）進行同步編輯。
- **導覽**：使用 `Ctrl + 點擊` 跳至定義，透過右鍵點擊尋找參考，並使用 `Ctrl + P` 快速存取檔案。頂部的麵包屑有助於瀏覽檔案路徑。
- **偵錯與版本控制**：在行號旁點擊設定中斷點，使用 `F5` 開始偵錯，並從原始檔控制面板管理 Git 操作（如提交和推送）。
- **自訂**：透過 `檔案 > 偏好設定 > 色彩主題` 變更主題，並在 `檔案 > 偏好設定 > 鍵盤快速鍵` 下調整快速鍵。

#### 30 個最實用的功能
VS Code 提供豐富的內建功能，可提升開發者的生產力。以下是 30 個最實用的功能，並按類別清晰列出：

| **類別**           | **功能**                           | **描述**                                                                 |
|--------------------|------------------------------------|--------------------------------------------------------------------------|
| **編輯**           | 語法突顯                           | 根據語言為程式碼上色，提高可讀性。                                       |
|                    | 自動縮排                           | 自動縮排程式碼以保持結構正確。                                           |
|                    | 括號匹配                           | 突顯匹配的括號，有助於偵錯。                                             |
|                    | 程式碼片段                         | 快速插入常用的程式碼模式。                                               |
|                    | 多重游標編輯                       | 使用 `Alt + 點擊` 同時編輯多個程式碼部分。                               |
|                    | 程式碼摺疊                         | 摺疊/展開程式碼區域，以便概覽。                                          |
|                    | Code Lens                          | 顯示額外資訊，如提交歷史或測試狀態。                                     |
|                    | 預覽定義                           | 在懸浮視窗中檢視函數/變數定義，無需跳轉。                                |
| **導覽**           | 移至定義                           | 使用 `Ctrl + 點擊` 跳至函數/變數定義。                                   |
|                    | 尋找所有參考                       | 在程式碼庫中定位函數/變數的所有出現位置。                                |
|                    | 快速開啟                           | 使用 `Ctrl + P` 快速開啟檔案。                                           |
|                    | 麵包屑導覽                         | 顯示檔案路徑，方便瀏覽不同部分。                                         |
| **偵錯**           | 內建偵錯器                         | 設定中斷點、逐步執行程式碼並檢查變數。                                   |
|                    | 中斷點                             | 在特定行暫停執行以進行偵錯。                                             |
|                    | 逐步執行程式碼                     | 在偵錯過程中逐行執行程式碼（`F10`、`F11`）。                             |
|                    | 監看變數                           | 在偵錯過程中監控變數值。                                                 |
| **版本控制**       | Git 整合                           | 原生支援 Git 操作，如提交、拉取和推送。                                  |
|                    | 提交、拉取、推送                   | 直接在 VS Code 中執行 Git 操作。                                         |
|                    | 追溯檢視                           | 顯示每行程式碼的最後修改者。                                             |
| **自訂**           | 色彩主題                           | 使用各種色彩方案自訂編輯器外觀。                                         |
|                    | 鍵盤快速鍵                         | 自訂或使用預設快速鍵以提高效率。                                         |
|                    | 設定同步                           | 在多台裝置間同步設定以保持一致。                                         |
|                    | 設定檔                             | 儲存並在不同專案的設定組之間切換。                                       |
| **遠端開發**       | Remote SSH                         | 透過 SSH 在遠端伺服器上進行開發，實現靈活存取。                          |
|                    | Containers                         | 在隔離的容器環境中進行開發。                                             |
|                    | Codespaces                         | 使用 GitHub 提供的雲端開發環境。                                         |
| **生產力**         | 命令選擇區                         | 透過 `Ctrl + Shift + P` 存取所有命令。                                   |
|                    | 工作執行器                         | 在內部執行建置或測試等工作。                                             |
|                    | 整合式終端機                       | 直接在 VS Code 內存取命令列。                                            |
|                    | 問題面板                           | 顯示錯誤、警告和問題，以便快速解決。                                     |

如需詳細探索，請造訪官方文件[這裡](https://code.visualstudio.com/docs)。

---

### VS Code 及其功能完整使用指南
本節深入探討如何使用 Visual Studio Code（VS Code）—— 一款由 Microsoft 開發的多功能程式碼編輯器，並詳細介紹其 30 個最實用的內建功能。這些資訊基於對開發者偏好和官方文件的廣泛研究（截至 2025 年 2 月 27 日）。VS Code 適用於 Windows、macOS 和 Linux，支援多種程式語言，並以其可擴充性和效能聞名。根據 2024 年 Stack Overflow 開發者調查，超過 73.6% 的開發者使用它。

#### 安裝與初始設定
首先，從官方網站[下載](https://code.visualstudio.com/download) VS Code。安裝過程簡單，支援多平台，確保所有使用者都能輕鬆使用。啟動後，使用者會看到歡迎頁面，提供如開啟資料夾或建立新檔案等操作。對於工作區信任，特別是下載的程式碼，請參閱文件[這裡](https://code.visualstudio.com/docs/getstarted/getting-started)以確保安全。

#### 逐步使用指南
1.  **建立與開啟檔案**：使用 `檔案 > 新增檔案` 或 `Ctrl + N`（macOS 上為 `Cmd + N`）建立新檔案，使用 `檔案 > 開啟` 或 `Ctrl + O`（`Cmd + O`）開啟現有檔案。使用 `Ctrl + S` 或 `Cmd + S` 儲存。這是啟動任何專案的基礎，如入門影片[這裡](https://code.visualstudio.com/docs/introvideos/basics)所述。
2.  **基本編輯功能**：VS Code 原生提供語法突顯、自動縮排和括號匹配，提高可讀性並減少錯誤。例如，輸入 "console.log" 並按 Tab 鍵會插入 JavaScript 片段，此功能在編輯教學[這裡](https://code.visualstudio.com/docs/introvideos/codeediting)中有強調。
3.  **進階編輯**：透過 `Alt + 點擊` 啟動的多重游標編輯，允許在多行進行同步編輯，對於重複性任務能提升生產力。程式碼片段和摺疊進一步簡化工作流程，如技巧與提示[這裡](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)所述。
4.  **導覽與搜尋**：使用 `Ctrl + 點擊` 進行「移至定義」，右鍵點擊進行「尋找所有參考」，並使用 `Ctrl + P` 進行「快速開啟」。頂部的麵包屑導覽有助於瀏覽複雜的檔案結構，詳細說明在使用者介面文件[這裡](https://code.visualstudio.com/docs/getstarted/userinterface)。
5.  **偵錯能力**：在行號旁點擊設定中斷點，使用 `F5` 開始偵錯，並使用 `F10`（跳過）、`F11`（步入）和 `Shift + F11`（步出）進行詳細檢查。監看變數以監控值，此功能在[這裡](https://code.visualstudio.com/docs/editor/debugging)有詳細說明。
6.  **使用 Git 進行版本控制**：透過原始檔控制檢視初始化儲存庫，使用 `Ctrl + Enter`（macOS：`Cmd + Enter`）提交，並管理拉取/推送操作。追溯檢視顯示修改歷史，增強協作，如[這裡](https://code.visualstudio.com/docs/sourcecontrol/overview)所述。
7.  **自訂選項**：透過 `檔案 > 偏好設定 > 色彩主題` 變更色彩主題，在 `檔案 > 偏好設定 > 鍵盤快速鍵` 下自訂鍵盤快速鍵，並使用設定同步在裝置間同步設定。設定檔允許儲存不同配置，詳細說明在[這裡](https://code.visualstudio.com/docs/getstarted/settings)。
8.  **遠端與雲端開發**：使用 Remote SSH 進行伺服器開發，使用 Containers 進行隔離環境開發，並使用 Codespaces 進行雲端設定，擴展開發靈活性，如[這裡](https://code.visualstudio.com/docs/remote/remote-overview)所述。

#### 詳細功能分析
下表列出 30 個最實用的內建功能，並按類別清晰劃分，基於官方文件和開發者使用模式的研究：

| **類別**           | **功能**                           | **描述**                                                                 |
|--------------------|------------------------------------|--------------------------------------------------------------------------|
| **編輯**           | 語法突顯                           | 根據語言為程式碼上色以提高可讀性，支援數百種語言。                       |
|                    | 自動縮排                           | 自動縮排程式碼以保持結構正確，提高一致性。                               |
|                    | 括號匹配                           | 突顯匹配的括號以協助偵錯和提高可讀性。                                   |
|                    | 程式碼片段                         | 快速插入常用程式碼模式，例如 JavaScript 的 "console.log"。              |
|                    | 多重游標編輯                       | 使用 `Alt + 點擊` 同時編輯多個程式碼部分，提升生產力。                   |
|                    | 程式碼摺疊                         | 摺疊/展開程式碼區域以便概覽，改善專注力。                                |
|                    | Code Lens                          | 顯示提交歷史或測試狀態等額外資訊，有助於維護。                           |
|                    | 預覽定義                           | 在懸浮視窗中檢視函數/變數定義而無需跳轉，節省時間。                      |
| **導覽**           | 移至定義                           | 使用 `Ctrl + 點擊` 跳至函數/變數定義，增強導覽。                         |
|                    | 尋找所有參考                       | 定位函數/變數的所有出現位置，對重構很有用。                              |
|                    | 快速開啟                           | 使用 `Ctrl + P` 快速開啟檔案，加快檔案存取速度。                         |
|                    | 麵包屑導覽                         | 顯示檔案路徑以便輕鬆瀏覽不同部分，改善導向。                             |
| **偵錯**           | 內建偵錯器                         | 設定中斷點、逐步執行程式碼並檢查變數，對測試至關重要。                   |
|                    | 中斷點                             | 在特定行暫停執行以進行詳細偵錯，對尋找錯誤很重要。                       |
|                    | 逐步執行程式碼                     | 逐行執行程式碼（`F10`、`F11`），允許深入檢查。                           |
|                    | 監看變數                           | 在偵錯過程中監控變數值，有助於狀態追蹤。                                 |
| **版本控制**       | Git 整合                           | 支援 Git 操作如提交、拉取、推送，增強協作。                              |
|                    | 提交、拉取、推送                   | 直接在 VS Code 中執行 Git 操作，簡化版本控制。                           |
|                    | 追溯檢視                           | 顯示每行程式碼的最後修改者，對程式碼審查和問責很有用。                   |
| **自訂**           | 色彩主題                           | 自訂編輯器外觀，改善視覺舒適度，提供多種選項。                           |
|                    | 鍵盤快速鍵                         | 自訂或使用預設快速鍵，提高效率，完全可配置。                             |
|                    | 設定同步                           | 在多台裝置間同步設定以確保一致性，詳細說明[這裡](https://code.visualstudio.com/docs/getstarted/settings#_settings-sync)。 |
|                    | 設定檔                             | 儲存並在不同專案的設定組之間切換，增強靈活性。                           |
| **遠端開發**       | Remote SSH                         | 透過 SSH 在遠端伺服器上進行開發，擴展存取範圍，詳細說明[這裡](https://code.visualstudio.com/docs/remote/ssh)。 |
|                    | Containers                         | 在隔離的容器環境中進行開發，確保一致性，如[這裡](https://code.visualstudio.com/docs/remote/containers)所述。 |
|                    | Codespaces                         | 使用 GitHub 提供的雲端開發環境，增強協作，詳細說明[這裡](https://code.visualstudio.com/docs/remote/codespaces)。 |
| **生產力**         | 命令選擇區                         | 透過 `Ctrl + Shift + P` 存取所有命令，集中功能。                         |
|                    | 工作執行器                         | 在內部執行建置或測試等工作，改善工作流程，詳細說明[這裡](https://code.visualstudio.com/docs/editor/tasks)。 |
|                    | 整合式終端機                       | 在 VS Code 內存取命令列，增強整合性，如[這裡](https://code.visualstudio.com/docs/integrated-terminal)所述。 |
|                    | 問題面板                           | 顯示錯誤、警告和問題，有助於快速解決，對偵錯至關重要。                   |

這些功能是根據廣泛研究編纂而成，包括官方文件和開發者導向的文章，確保它們符合 2025 年的當前使用情況。例如，Git 和遠端開發功能的整合反映了 VS Code 為滿足現代開發需求而進化的趨勢，如更新[這裡](https://code.visualstudio.com/updates/v1_97)所示。

#### 其他注意事項
VS Code 的可擴充性（擁有超過 30,000 個擴充功能）補充了這些內建功能，但本節重點在於原生功能。例如，雖然 GitHub Copilot 很受歡迎，但它是擴充功能而非內建，因此被排除在外。其快速的啟動時間和高效的記憶體使用（在效能討論[這裡](https://code.visualstudio.com/docs/editor/whyvscode)中提到）使其適合日常使用，這對於期望更重型的 IDE 的使用者來說是一個意想不到的細節。

如需進一步學習，請探索入門影片[這裡](https://code.visualstudio.com/docs/introvideos/basics)和技巧與提示[這裡](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)，以全面了解 VS Code 的功能。

---

### 主要參考文獻
- [Official VS Code Documentation](https://code.visualstudio.com/docs/)
- [VS Code Features Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
- [VS Code Debugging Guide](https://code.visualstudio.com/docs/editor/debugging)
- [VS Code Git Integration Overview](https://code.visualstudio.com/docs/sourcecontrol/overview)
- [VS Code Settings Sync Documentation](https://code.visualstudio.com/docs/getstarted/settings#_settings-sync)
- [VS Code Remote SSH Development](https://code.visualstudio.com/docs/remote/ssh)
- [VS Code Containers Development](https://code.visualstudio.com/docs/remote/containers)
- [VS Code Codespaces Development](https://code.visualstudio.com/docs/remote/codespaces)
- [VS Code Tasks Runner Documentation](https://code.visualstudio.com/docs/editor/tasks)
- [VS Code Integrated Terminal Guide](https://code.visualstudio.com/docs/integrated-terminal)
- [Why We Built VS Code Editor](https://code.visualstudio.com/docs/editor/whyvscode)
- [VS Code Introductory Videos](https://code.visualstudio.com/docs/introvideos/basics)
- [VS Code January 2025 Update](https://code.visualstudio.com/updates/v1_97)