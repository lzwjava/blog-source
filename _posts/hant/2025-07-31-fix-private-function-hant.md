---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 修正私有函數錯誤
translated: true
type: note
---

錯誤 `E0603: function run_simple is private` 表示 `simple.rs` 中的 `run_simple` 函數是私有的（缺少 `pub` 關鍵字），因此無法從 `main.rs` 存取。在 Rust 中，函數預設為私有，需要使用 `pub` 明確設為公開才能在其模組外部存取。

### 解決錯誤的步驟

1. **將 `run_simple` 設為公開**：
   - 開啟 `src/simple.rs`。
   - 在 `run_simple` 函數前加上 `pub` 關鍵字使其可公開存取。
   - 範例：
     ```rust
     pub fn run_simple() {
         // 現有函數主體
         println!("Hello from run_simple!");
     }
     ```

2. **確保正確的模組宣告**：
   - 在 `src/main.rs` 中，確保已正確宣告 `simple` 模組：
     ```rust
     mod simple; // 宣告 simple 模組

     fn main() {
         simple::run_simple(); // 呼叫公開函數
     }
     ```

3. **重新編譯並執行**：
   - 將函數設為公開後，重新編譯專案：
     ```bash
     cargo build
     ```
   - 若編譯成功，執行程式：
     ```bash
     cargo run
     ```

4. **檢查其他問題**：
   - 錯誤訊息提到 `src/simple.rs:47:1`，請確認該行的 `run_simple` 函數正確定義且沒有其他問題（例如語法錯誤或缺少依賴項）。
   - 若 `simple.rs` 使用外部 crate，請確保它們已列在 `Cargo.toml` 的 `[dependencies]` 下方。

5. **Cargo 警告處理**：
   - 關於 `edition2024` 的警告提示你在 `Cargo.toml` 中使用了不再需要的功能旗標，因為 Rust 1.85 已穩定支援 2024 版本。請開啟 `Cargo.toml` 並移除 `edition2024` 功能（若存在於 `[features]` 或 `cargo-features` 中）。改為直接設定版本：
     ```toml
     [package]
     name = "example"
     version = "0.1.0"
     edition = "2024"
     ```
   - 這能確保專案使用 2024 版本而無需棄用的功能旗標。

### 檔案範例

以下是檔案應有的內容範例：

**`src/simple.rs`**：
```rust
pub fn run_simple() {
    println!("Hello from run_simple!");
}
```

**`src/main.rs`**：
```rust
mod simple;

fn main() {
    simple::run_simple();
}
```

**`Cargo.toml`**（精簡範例）：
```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"
```

### 補充說明
- 若 `run_simple` 依賴其他程式碼或模組，請確保從 `main.rs` 存取時這些項目也設為公開。
- 若錯誤持續發生，請提供 `src/simple.rs`（特別是第 47 行附近）和 `src/main.rs` 的內容以獲得更具體的指引。
- 執行 `rustc --explain E0603` 指令可查看此錯誤的詳細說明文件。
- 成功編譯後，編譯產生的二進位檔案（`example`）將位於 `target/debug` 目錄中。

請嘗試以上步驟，若有其他問題歡迎告知！