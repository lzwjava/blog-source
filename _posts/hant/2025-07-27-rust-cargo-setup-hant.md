---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 修復 Rust 專案設定
translated: true
type: note
---

看來你正嘗試根據提供的 `Cargo.toml` 片段和檔案結構（包含 `example.rs` 的 `rust` 子目錄）來設置並執行一個簡單的 Rust 專案。不過，目前有幾個問題導致無法直接運行：

- 目錄 `/Users/lzwjava/projects/lzwjava.github.io`（你的 GitHub Pages 根目錄）似乎尚未配置為有效的 Rust workspace，這就是為什麼 rust-analyzer 之前會失敗。
- `Cargo.toml` 中的 `edition = "2025"` 是無效的——Rust 目前的版本為 2015、2018、2021 和 2024（於 2025 年初發布）。目前並沒有 2025 版本。
- 由 Cargo 管理的 Rust 專案預期採用標準結構：根目錄下的 `Cargo.toml`，原始碼檔案位於 `src/` 子目錄中（例如，`src/main.rs` 用於二進制執行檔）。你的 `example.rs` 位於 `rust/` 子目錄中，這在預設情況下不會被識別。
- 假設 `example.rs` 包含一個簡單的可執行程式（例如，帶有 `fn main()` 的 "Hello, World!"），你有兩個主要選擇：將其作為單一檔案腳本運行（無需 Cargo）或將其設置為適當的 Cargo 專案。

我將逐步引導你完成這兩種方法。請在你的專案根目錄（`lzwjava.github.io`）中使用終端機。

### 選項 1：作為單一檔案腳本運行（最快速，無需 Cargo）
這使用 Rust 編譯器（`rustc`）直接編譯並運行 `example.rs`。如果你不需要依賴項或完整的專案設置，這是最理想的方法。

1. 導航到包含該檔案的目錄：
   ```
   cd rust
   ```

2. 編譯檔案：
   ```
   rustc example.rs
   ```
   - 這將生成一個名為 `example` 的可執行檔（在 macOS/Linux 上）或 `example.exe`（在 Windows 上）。
   - 如果編譯失敗（例如，由於 `example.rs` 中的語法錯誤），請修正程式碼並重試。

3. 執行可執行檔：
   ```
   ./example
   ```
   - 輸出將取決於 `example.rs` 中的內容（例如，"Hello, World!"）。

如果 `example.rs` 是一個函式庫（沒有 `fn main()`），此方法將無法運作——請在專案設置中使用 `cargo test`。

### 選項 2：設置並作為 Cargo 專案運行（推薦用於 rust-analyzer 和可擴展性）
這通過創建一個有效的 workspace 來解決 rust-analyzer 錯誤。同時允許使用 `cargo run` 來更輕鬆地建置/運行。

1. 創建或移動到專用的專案目錄（以避免混亂你的 GitHub Pages 根目錄）：
   ```
   mkdir rust_project
   cd rust_project
   ```
   - 如果你堅持使用現有的 `rust` 目錄，請改為 `cd rust` 並繼續。

2. 使用你提供的內容創建 `Cargo.toml`，但修正版本：
   ```
   [package]
   name = "example"
   version = "0.1.0"
   edition = "2024"  # 從無效的 "2025" 更改而來
   authors = ["lzwjava@gmail.com"]
   description = "A simple Rust example project"

   [dependencies]
   ```
   - 將其保存為目前目錄中的 `Cargo.toml`。

3. 設置原始碼目錄並移動你的檔案：
   ```
   mkdir src
   mv ../rust/example.rs src/main.rs  # 如果需要，調整路徑；將其重新命名為 main.rs 以用於二進制執行
   ```
   - 如果 `example.rs` 並非預設的主要進入點，請將其重新命名為 `lib.rs`，並在 `Cargo.toml` 中添加 `[lib]` 以用於函式庫 crate。

4. 建置專案：
   ```
   cargo build
   ```
   - 這將下載任何需要的 crates（此處沒有）並進行編譯。如果失敗，請檢查 `src/main.rs` 中的錯誤。

5. 運行專案：
   ```
   cargo run
   ```
   - 這將在需要時建置並執行 `src/main.rs`。

6. 為了解決 VS Code（或類似編輯器）中的 rust-analyzer 錯誤：
   - 將 `rust_project` 資料夾作為你的 workspace 根目錄打開（**檔案 > 打開資料夾**）。
   - 重新加載視窗（**Cmd+Shift+P** > **Developer: Reload Window**）。
   - rust-analyzer 現在應該通過 `Cargo.toml` 檢測到專案。

### 故障排除提示
- **如果未安裝 `cargo`**：運行 `rustup update`（假設你已通過 rustup 安裝 Rust）。如果沒有，請從 https://rustup.rs/ 安裝 Rust。
- **版本錯誤**：如果你保留 "2025"，Cargo 會報錯："error: invalid edition: '2025'"。請堅持使用 "2024"。
- **`example.rs` 中沒有 `fn main()`**：添加一個，例如：
  ```
  fn main() {
      println!("Hello, World!");
  }
  ```
- **需要依賴項？**：在 `Cargo.toml` 的 `[dependencies]` 下添加它們，例如 `rand = "0.8"`，然後執行 `cargo build`。
- **rust-analyzer 仍然失敗？**：確保你的編輯器 Rust 擴展已更新，如果專案位於子目錄中，請將 `"rust-analyzer.linkedProjects": ["./Cargo.toml"]` 添加到你的 workspace `settings.json` 中。
- 對於更複雜的設置（例如，多個 crates），使用 `cargo new --bin example` 來生成模板。

如果這與你的設置不符（例如，提供 `example.rs` 的內容或更多細節），請告訴我以獲取更精確的步驟。

[Announcing Rust 1.88.0](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/)  
[Rust | endoflife.date](https://endoflife.date/rust)