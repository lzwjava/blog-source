---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 從目錄執行 Rust 程式
translated: true
type: note
---

要從你提供的目錄結構中執行一個簡單的 Rust 程式，看起來你正在處理一個 Rust 專案（`lzwjava.github.io/rust`），其中包含 `src` 資料夾，內有 `main.rs` 和 `simple.rs`。以下是執行簡單 Rust 程式的方法，假設你想執行 `main.rs` 或 `simple.rs` 中的程式碼。

### 執行 Rust 程式的步驟

1. **檢查專案結構**：
   - 你的專案有一個 `Cargo.toml` 檔案，表示這是一個由 Cargo（Rust 的建置工具）管理的 Rust 專案。
   - `src/main.rs` 檔案是 Rust 二進位應用程式的預設進入點。
   - `simple.rs` 檔案可能是一個模組或另一個原始碼檔案，但除非它在 `main.rs` 中被引用或在 `Cargo.toml` 中配置為二進位檔案，否則無法直接執行。

2. **使用 Cargo 執行程式**：
   - 如果你想執行 `src/main.rs` 中的程式碼，請在專案根目錄（`~/projects/lzwjava.github.io/rust`）中使用以下指令：
     ```bash
     cargo run
     ```
     這個指令：
     - 編譯專案（解析依賴項並建置程式碼）。
     - 執行從 `src/main.rs` 生成的二進位檔案。
     - 輸出將顯示在終端機中。

3. **如果你想執行 `simple.rs`**：
   - 預設情況下，Cargo 期望主要進入點是 `src/main.rs`。如果 `simple.rs` 是一個模組，你需要在 `main.rs` 中引用它。例如，在 `src/main.rs` 中：
     ```rust
     mod simple; // 宣告 simple 模組

     fn main() {
         simple::some_function(); // 從 simple.rs 呼叫函式
     }
     ```
     然後如上所述執行 `cargo run`。
   - 如果 `simple.rs` 是一個獨立的二進位檔案，你需要在 `Cargo.toml` 中配置它。在 `Cargo.toml` 中加入以下內容：
     ```toml
     [[bin]]
     name = "simple"
     path = "src/simple.rs"
     ```
     然後執行：
     ```bash
     cargo run --bin simple
     ```

4. **替代方案：不使用 Cargo 執行**：
   - 如果你想編譯並執行單一檔案（例如 `simple.rs`）而不使用 Cargo，請確保它有一個 `main` 函式，並使用 `rustc` 編譯器：
     ```bash
     rustc src/simple.rs
     ./simple
     ```
     這會在當前目錄中生成一個名為 `simple` 的可執行檔案並執行它。注意：這種方法不處理依賴項，因此僅適用於簡單、獨立的程式。

5. **檢查錯誤**：
   - 如果遇到錯誤，請確保：
     - 已安裝 Rust 和 Cargo（使用 `rustc --version` 和 `cargo --version` 驗證）。
     - `Cargo.toml` 已正確配置必要的依賴項。
     - `main.rs` 或 `simple.rs` 中的程式碼具有有效的 `fn main()` 函式。
   - 執行 `cargo check` 以在不建置二進位檔案的情況下驗證程式碼：
     ```bash
     cargo check
     ```

6. **`simple.rs` 範例**：
   如果 `simple.rs` 包含類似以下的內容：
   ```rust
   fn main() {
       println!("Hello from simple!");
   }
   ```
   並且你已將其作為二進位檔案添加到 `Cargo.toml` 中，執行 `cargo run --bin simple` 將列印 `Hello from simple!`。

### 注意事項
- `target/debug` 目錄包含編譯後的成品。你可以直接使用 `./target/debug/<project_name>` 執行二進位檔案（將 `<project_name>` 替換為 `Cargo.toml` 中的名稱），但建議使用 `cargo run`，因為它會處理編譯和執行。
- 如果 `simple.rs` 是一個模組，請確保它已通過 `mod simple;` 正確整合到 `main.rs` 中。
- 對於更複雜的設定或 `simple.rs` 中的特定程式碼，請分享 `simple.rs` 或 `Cargo.toml` 的內容以獲得針對性的指導。

如果你所說的「在這裡執行 simple」有特定含義（例如特定的函式或配置），請提供更多詳細資訊，我將進一步完善答案！