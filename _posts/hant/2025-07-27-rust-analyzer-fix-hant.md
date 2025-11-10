---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Rust Analyzer 工作區問題
translated: true
type: note
---

您看到的錯誤訊息表明 rust-analyzer（Rust 語言伺服器）無法在指定目錄 `/Users/lzwjava/projects/lzwjava.github.io` 中檢測到有效的 Rust 工作區。這通常是因為該資料夾根目錄缺少 `Cargo.toml` 檔案（或其他 Rust 專案標記），或者 rust-analyzer 未配置為在正確位置查找。rust-analyzer 期望在開啟的工作區中至少找到一個 Rust 專案；如果找不到，則無法載入。

此目錄名稱（`lzwjava.github.io`）表明它可能是一個 GitHub Pages 網站（例如，用於靜態部落格或網站），這通常不是 Rust 專案，除非您使用基於 Rust 的工具（如自訂靜態網站生成器）。如果這不應是 Rust 工作區，則 rust-analyzer 可能不必要地處於活動狀態（例如，由於編輯器中的全域擴充功能設定）。

假設您使用的是 VS Code（此問題最常見的編輯器；如果不是，請參閱下方的說明），以下是修復步驟：

### 1. **驗證並開啟正確的工作區資料夾**
   - 確保您將包含 Rust 專案 `Cargo.toml` 檔案的資料夾作為 VS Code 工作區根目錄開啟。
   - 如果您的專案位於子目錄中（例如 `/Users/lzwjava/projects/lzwjava.github.io/my-rust-app`），請透過 **檔案 > 開啟資料夾** 開啟該子資料夾。
   - 變更工作區後重新啟動 VS Code。

### 2. **在 rust-analyzer 設定中配置連結專案**
   - 如果 `Cargo.toml` 存在但不在工作區根目錄中（例如，在子資料夾中），請告訴 rust-analyzer 在哪裡找到它：
     - 開啟 VS Code 設定（**Code > Preferences > Settings** 或在 Mac 上使用 Cmd+,）。
     - 搜尋 "rust-analyzer"。
     - 在 **Rust-analyzer > Server: Extra Env** 或直接在擴充功能設定中找到 **Linked Projects**。
     - 將其設定為指向您的 `Cargo.toml` 路徑的陣列。例如，將以下內容新增到您工作區的 `settings.json` 中（透過 **Preferences: Open Workspace Settings (JSON)**）：
       ```
       {
         "rust-analyzer.linkedProjects": [
           "./path/to/your/Cargo.toml"
         ]
       }
       ```
       將 `./path/to/your/Cargo.toml` 替換為相對於您工作區根目錄的相對路徑。
     - 儲存並重新載入視窗（透過 Command Palette 使用 **Developer: Reload Window**，Cmd+Shift+P）。

### 3. **如果這不是 Rust 專案**
   - 為此工作區停用 rust-analyzer：
     - 前往擴充功能檢視（Cmd+Shift+X）。
     - 找到 "rust-analyzer" > 點擊齒輪圖示 > **Disable (Workspace)**。
   - 或者，如果您完全不需要此擴充功能，請解除安裝它。

### 4. **其他疑難排解**
   - **重新安裝 rust-analyzer 和 Rustup**：有時損壞的安裝會導致問題。在終端機中執行 `rustup self uninstall`，然後執行 `rustup self update`，並重新安裝 VS Code 擴充功能。
   - **檢查多個工作區**：如果您有多根工作區，請確保每個根目錄都有自己的有效配置。
   - **更新所有內容**：確保 VS Code、rust-analyzer 擴充功能和 Rust 工具鏈（`rustup update`）都是最新版本。
   - **檢視日誌以獲取更多詳細資訊**：在 VS Code 中檢查 rust-analyzer 的輸出（**View > Output**，從下拉選單中選擇 "rust-analyzer"）以獲取其他線索。

如果您使用不同的編輯器：
- **Neovim 或 Vim**：確保您的 LSP 配置（例如，透過 lsp-zero 或 nvim-lspconfig）使用 `root_dir` 模式（如 `util.find_git_ancestor`）指向正確的根目錄，或明確設定為查找 `Cargo.toml`。
- **Kate 或 Emacs**：問題可能是編輯器未正確傳遞專案路徑——嘗試在 LSP 配置中手動設定專案根目錄，或檢查編輯器特定的錯誤（例如，確保存在 `.git` 資料夾，如果需要）。
- **其他 IDE**：尋找等效的 "linked projects" 或 "workspace root" 設定。

如果以上方法均無效，請提供更多詳細資訊，例如您的編輯器、這是否是 Rust 專案，以及該目錄中是否有任何 Rust 檔案。

[rust-analyzer failed to discover workspace in vscode - Stack Overflow](https://stackoverflow.com/questions/72062935/rust-analyzer-failed-to-discover-workspace-in-vscode)  
[Question about failed to find any projects in [AbsPathBuf...] - GitHub](https://github.com/rust-analyzer/rust-analyzer/issues/11666)  
[Problem with Rust-Analyzer - Rust Users Forum](https://users.rust-lang.org/t/problem-with-rust-analyzer/91453)  
[Configuration - rust-analyzer Manual](https://rust-analyzer.github.io/manual.html#configuration)