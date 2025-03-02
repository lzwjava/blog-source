---
audio: false
generated: false
lang: hant
layout: post
title: 使用 Visual Studio Code
translated: true
---

### 關鍵要點
- VS Code 是一個流行的免費程式碼編輯器，適用於 Windows、macOS 和 Linux，支持多種程式語言。
- 根據開發者的使用情況，其最有用的功能似乎包括語法高亮顯示、除錯和 Git 整合。
- 根據證據，超過 30 個內建功能可以提高生產力，例如多光標編輯和遠程開發。

---

### 開始使用 VS Code
Visual Studio Code (VS Code) 是一個輕量級的開源程式碼編輯器，由 Microsoft 開發，適合在 Windows、macOS 和 Linux 上進行編碼。要開始，請從官方網站 [這裡](https://code.visualstudio.com/download) 下載。安裝完成後，啟動 VS Code 開始編碼。

#### 基本使用
- **創建或打開文件**：使用 `File > New File` (或 Windows/Linux 上的 `Ctrl + N`，macOS 上的 `Cmd + N`) 來創建新文件，使用 `File > Open` (或 `Ctrl + O`，`Cmd + O`) 來打開現有文件。使用 `Ctrl + S` 或 `Cmd + S` 保存。
- **編輯程式碼**：享受語法高亮顯示、自動縮進和括號匹配等功能，以提高可讀性。使用程式碼片段進行快速插入，使用多光標編輯 (`Alt + Click`) 進行同時編輯。
- **導航**：使用 `Ctrl + Click` 跳轉到定義，右鍵點擊查找引用，使用 `Ctrl + P` 進行快速文件訪問。頂部的面包屑幫助導航文件路徑。
- **除錯和版本控制**：通過點擊行號設置斷點，使用 `F5` 進行除錯，並從源代碼控制面板管理 Git 操作，如提交和推送。
- **自定義**：通過 `File > Preferences > Color Theme` 更改主題，並在 `File > Preferences > Keyboard Shortcuts` 下調整快捷鍵。

#### 30 個最有用的功能
VS Code 提供豐富的內建功能，提高開發者的生產力。以下是 30 個最有用的功能，按類別分類：

| **類別**        | **功能**                          | **描述**                                                                 |
|---------------------|--------------------------------------|---------------------------------------------------------------------------------|
| **編輯**         | 語法高亮顯示                  | 根據語言為程式碼著色，以提高可讀性。                                  |
|                     | 自動縮進                     | 自動縮進程式碼以保持正確結構。                                |
|                     | 括號匹配                     | 高亮顯示匹配的括號，幫助錯誤檢測。                            |
|                     | 程式碼片段                        | 快速插入常用的程式碼模式。                                  |
|                     | 多光標編輯                 | 使用 `Alt + Click` 同時編輯多個程式碼部分。                    |
|                     | 程式碼折疊                         | 折疊/展開程式碼區域以獲得更好的概覽。                             |
|                     | 程式碼透鏡                            | 顯示額外信息，如提交歷史或測試狀態。                       |
|                     | 查看定義                      | 在懸停窗口中查看函數/變量定義，而不需要導航。       |
| **導航**      | 跳轉到定義                     | 使用 `Ctrl + Click` 跳轉到函數/變量定義。                     |
|                     | 查找所有引用                  | 定位程式碼庫中函數/變量的所有出現。                 |
|                     | 快速打開                           | 使用 `Ctrl + P` 快速打開文件。                                            |
|                     | 面包屑導航                | 顯示文件路徑以便輕鬆導航到不同部分。                      |
| **除錯**       | 内建除錯器                    | 設置斷點、逐步執行程式碼並檢查變量。                   |
|                     | 斷點                          | 在特定行暫停執行以進行除錯。                               |
|                     | 逐步執行程式碼                    | 在除錯期間逐行執行程式碼 (`F10`, `F11`)。                     |
|                     | 監視變量                      | 在除錯會話期間監視變量值。                             |
| **版本控制** | Git 整合                      | 支持提交、拉取、推送等 Git 操作。                 |
|                     | 提交、拉取、推送                   | 直接從 VS Code 執行 Git 操作。                                     |
|                     | 責任視圖                           | 顯示最後修改每行程式碼的開發者。                                      |
| **自定義**   | 顏色主題                         | 使用各種顏色方案自定義編輯器外觀。                        |
|                     | 鍵盤快捷鍵                   | 自定義或使用默認快捷鍵以提高效率。                            |
|                     | 設定同步                        | 同步多台機器的設定以保持一致。                        |
|                     | 設定檔                             | 保存和在不同項目之間切換不同的設定。                 |
| **遠程開發** | 遠程 SSH                     | 通過 SSH 進行遠程伺服器開發以獲得靈活訪問。                         |
|                     | 容器                           | 在隔離的容器環境中進行開發。                                    |
|                     | 代碼空間                           | 使用來自 GitHub 的基於雲的開發環境。                          |
| **生產力**    | 命令面板                      | 使用 `Ctrl + Shift + P` 訪問所有命令。                                   |
|                     | 任務運行器                          | 內部運行任務，如構建或測試程式碼。                            |
|                     | 內建終端                  | 直接在 VS Code 中訪問命令行。                                  |
|                     | 問題面板                       | 顯示錯誤、警告和問題以便快速解決。                     |

詳細探索，請訪問官方文檔 [這裡](https://code.visualstudio.com/docs)。

---

### 使用 VS Code 及其功能的全面指南
本節深入探討使用 Visual Studio Code (VS Code)，一個由 Microsoft 開發的多功能程式碼編輯器，並詳細介紹其 30 個最有用的內建功能，根據對開發者偏好和官方文檔的廣泛研究，截至 2025 年 2 月 27 日。VS Code 適用於 Windows、macOS 和 Linux，支持多種程式語言，並以其可擴展性和性能著稱，根據 2024 年 Stack Overflow 開發者調查，有 73.6% 的開發者使用它。

#### 安裝和初始設置
要開始，請從官方網站 [這裡](https://code.visualstudio.com/download) 下載 VS Code。安裝過程簡單，支持多個平台，確保所有用戶都能訪問。啟動後，用戶會看到一個歡迎頁面，提供打開文件夾或創建新文件等操作。對於工作區信任，特別是下載的程式碼，請根據文檔 [這裡](https://code.visualstudio.com/docs/getstarted/getting-started) 進行安全檢查。

#### 逐步使用指南
1. **創建和打開文件**：使用 `File > New File` 或 `Ctrl + N` (`Cmd + N` on macOS) 來創建新文件，使用 `File > Open` 或 `Ctrl + O` (`Cmd + O`) 來打開現有文件。使用 `Ctrl + S` 或 `Cmd + S` 保存。這對於開始任何項目都是基本的，如入門視頻 [這裡](https://code.visualstudio.com/docs/introvideos/basics) 所說明。
2. **基本編輯功能**：VS Code 提供語法高亮顯示、自動縮進和括號匹配等功能，提高可讀性並減少錯誤。例如，輸入 "console.log" 並按 Tab 鍵插入 JavaScript 片段，這在編輯教程 [這裡](https://code.visualstudio.com/docs/introvideos/codeediting) 中有詳細介紹。
3. **高級編輯**：多光標編輯，通過 `Alt + Click` 激活，允許在多行上同時進行編輯，這對於重複任務是一個生產力提升。程式碼片段和折疊進一步簡化工作流程，如技巧和技巧 [這裡](https://code.visualstudio.com/docs/getstarted/tips-and-tricks) 中所述。
4. **導航和搜索**：使用 `Ctrl + Click` 進行跳轉到定義，右鍵點擊查找所有引用，使用 `Ctrl + P` 進行快速打開。頂部的面包屑導航幫助導航複雜的文件結構，詳細信息請參閱用戶界面文檔 [這裡](https://code.visualstudio.com/docs/getstarted/userinterface)。
5. **除錯功能**：通過點擊行號設置斷點，使用 `F5` 開始除錯，並使用 `F10` (逐步執行)，`F11` (逐步進入) 和 `Shift + F11` (逐步退出) 進行詳細檢查。監視變量以監視值，這在 [這裡](https://code.visualstudio.com/docs/editor/debugging) 中有詳細介紹。
6. **Git 版本控制**：通過源代碼控制視圖初始化存儲庫，使用 `Ctrl + Enter` (macOS: `Cmd + Enter`) 提交，並管理拉取/推送操作。責任視圖顯示修改歷史，增強協作，如 [這裡](https://code.visualstudio.com/docs/sourcecontrol/overview) 所述。
7. **自定義選項**：通過 `File > Preferences > Color Theme` 更改顏色主題，在 `File > Preferences > Keyboard Shortcuts` 下自定義鍵盤快捷鍵，並使用設定同步在設備之間同步設定。設定檔允許保存不同的配置，詳細信息請參閱 [這裡](https://code.visualstudio.com/docs/getstarted/settings)。
8. **遠程和雲開發**：使用遠程 SSH 進行伺服器端開發，使用容器進行隔離環境，使用代碼空間進行基於雲的設置，擴展開發靈活性，如 [這裡](https://code.visualstudio.com/docs/remote/remote-overview) 所述。

#### 詳細功能分析
以下表格列出了 30 個最有用的內建功能，按類別分類，根據官方文檔和開發者使用模式的研究：

| **類別**        | **功能**                          | **描述**                                                                 |
|---------------------|--------------------------------------|---------------------------------------------------------------------------------|
| **編輯**         | 語法高亮顯示                  | 根據語言為程式碼著色，支持數百種語言。                                  |
|                     | 自動縮進                     | 自動縮進程式碼以保持正確結構，提高一致性。                                |
|                     | 括號匹配                     | 高亮顯示匹配的括號，幫助錯誤檢測和可讀性。                            |
|                     | 程式碼片段                        | 快速插入常用的程式碼模式，例如 JavaScript 的 "console.log"。 |
|                     | 多光標編輯                 | 使用 `Alt + Click` 同時編輯多個程式碼部分，提高生產力。                    |
|                     | 程式碼折疊                         | 折疊/展開程式碼區域以獲得更好的概覽，提高專注。                             |
|                     | 程式碼透鏡                            | 顯示額外信息，如提交歷史或測試狀態，幫助維護。    |
|                     | 查看定義                      | 在懸停窗口中查看函數/變量定義，而不需要導航，節省時間。       |
| **導航**      | 跳轉到定義                     | 使用 `Ctrl + Click` 跳轉到函數/變量定義，提高導航。                     |
|                     | 查找所有引用                  | 定位程式碼庫中函數/變量的所有出現，對重構有用。          |
|                     | 快速打開                           | 使用 `Ctrl + P` 快速打開文件，加快文件訪問。                    |
|                     | 面包屑導航                | 顯示文件路徑以便輕鬆導航到不同部分，提高定位。                      |
| **除錯**       | 内建除錯器                    | 設置斷點、逐步執行程式碼並檢查變量，對測試至關重要。                   |
|                     | 斷點                          | 在特定行暫停執行以進行詳細除錯，對錯誤查找至關重要。                               |
|                     | 逐步執行程式碼                    | 逐行執行程式碼 (`F10`, `F11`)，允許深入檢查。                     |
|                     | 監視變量                      | 在除錯會話期間監視變量值，幫助狀態跟蹤。                             |
| **版本控制** | Git 整合                      | 支持提交、拉取、推送等 Git 操作，增強協作。                 |
|                     | 提交、拉取、推送                   | 直接從 VS Code 執行 Git 操作，簡化版本控制。        |
|                     | 責任視圖                           | 顯示最後修改每行程式碼的開發者，對程式碼審查和問責有用。    |
| **自定義**   | 顏色主題                         | 自定義編輯器外觀，提高視覺舒適度，有多種選項。       |
|                     | 鍵盤快捷鍵                   | 自定義或使用默認快捷鍵，提高效率，完全可配置。                            |
|                     | 設定同步                        | 同步多台機器的設定以保持一致，詳細信息請參閱 [這裡](https://code.visualstudio.com/docs/getstarted/settings#_settings-sync)。 |
|                     | 設定檔                             | 保存和在不同項目之間切換設定，提高靈活性。                 |
| **遠程開發** | 遠程 SSH                     | 通過 SSH 進行遠程伺服器開發，擴展訪問，詳細信息請參閱 [這裡](https://code.visualstudio.com/docs/remote/ssh)。 |
|                     | 容器                           | 在隔離的容器環境中進行開發，確保一致性，詳細信息請參閱 [這裡](https://code.visualstudio.com/docs/remote/containers)。 |
|                     | 代碼空間                           | 使用來自 GitHub 的基於雲的開發環境，增強協作，詳細信息請參閱 [這裡](https://code.visualstudio.com/docs/remote/codespaces)。 |
| **生產力**    | 命令面板                      | 使用 `Ctrl + Shift + P` 訪問所有命令，集中功能。        |
|                     | 任務運行器                          | 內部運行任務，如構建或測試，提高工作流程，詳細信息請參閱 [這裡](https://code.visualstudio.com/docs/editor/tasks)。 |
|                     | 內建終端                  | 直接在 VS Code 中訪問命令行，提高整合，詳細信息請參閱 [這裡](https://code.visualstudio.com/docs/integrated-terminal)。 |
|                     | 問題面板                       | 顯示錯誤、警告和問題，幫助快速解決，對除錯至關重要。                     |

這些功能是根據廣泛的研究編製的，包括官方文檔和面向開發者的文章，確保它們與 2025 年的當前使用情況一致。例如，Git 和遠程開發功能的整合反映了 VS Code 為滿足現代開發需求而演變，如更新 [這裡](https://code.visualstudio.com/updates/v1_97) 所示。

#### 額外考慮
VS Code 的可擴展性，擁有超過 30,000 個擴展，補充了這些內建功能，但這裡的重點是原生功能。例如，雖然 GitHub Copilot 很受歡迎，但它是一個擴展，而不是內建功能，因此被排除在外。快速啟動時間和高效的內存使用，如性能討論 [這裡](https://code.visualstudio.com/docs/editor/whyvscode) 中所述，使其適合日常使用，這對於期望更重的 IDE 的用戶來說是一個意外的細節。

要進一步學習，請探索入門視頻 [這裡](https://code.visualstudio.com/docs/introvideos/basics) 和技巧和技巧 [這裡](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)，確保對 VS Code 功能的全面理解。

---

### 關鍵引用
- [官方 VS Code 文檔](https://code.visualstudio.com/docs/)
- [VS Code 功能技巧和技巧](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
- [VS Code 除錯指南](https://code.visualstudio.com/docs/editor/debugging)
- [VS Code Git 整合概述](https://code.visualstudio.com/docs/sourcecontrol/overview)
- [VS Code 設定同步文檔](https://code.visualstudio.com/docs/getstarted/settings#_settings-sync)
- [VS Code 遠程 SSH 開發](https://code.visualstudio.com/docs/remote/ssh)
- [VS Code 容器開發](https://code.visualstudio.com/docs/remote/containers)
- [VS Code 代碼空間開發](https://code.visualstudio.com/docs/remote/codespaces)
- [VS Code 任務運行器文檔](https://code.visualstudio.com/docs/editor/tasks)
- [VS Code 內建終端指南](https://code.visualstudio.com/docs/integrated-terminal)
- [為什麼我們建立 VS Code 編輯器](https://code.visualstudio.com/docs/editor/whyvscode)
- [VS Code 入門視頻](https://code.visualstudio.com/docs/introvideos/basics)
- [VS Code 2025 年 1 月更新](https://code.visualstudio.com/updates/v1_97)