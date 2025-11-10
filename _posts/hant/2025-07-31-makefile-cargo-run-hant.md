---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 貨運運行冗餘
translated: true
type: note
---

你完全正確！在你的 `Makefile` 範例中：

```makefile
run:
	cargo build
	cargo run
```

在 `cargo run` 之前加入 `cargo build` 是多餘的，因為 `cargo run` 已經包含了建置步驟。當你執行 `cargo run` 時，Cargo 會自動檢查專案是否需要重新建置（例如原始碼檔案有變更），並在必要時先編譯專案再執行產生的二進位檔。這使得明確的 `cargo build` 步驟在此情境下變得沒有必要。

### 說明
- **`cargo run`**：
  - 結合了 `cargo build`（將專案編譯成 `target/debug/<專案名稱>`）然後執行二進位檔。
  - 只有在原始碼或依賴項有變更時才會重新建置。
- **`cargo build`**：
  - 僅編譯專案而不執行二進位檔。
  - 適用於你想驗證編譯而不執行程式的情況。

### 修正 `Makefile`
為了精簡你的 `Makefile`，可以移除多餘的 `cargo build`：

```makefile
run:
	cargo run
```

這樣能達到相同的效果：專案會被建置（如果需要）然後執行。

### 何時分開使用 `cargo build`
你可能會想將 `cargo build` 保留為 `Makefile` 中的獨立目標，用於以下情況：
- 檢查編譯錯誤。
- 準備用於部署或測試的二進位檔而不執行。

例如：

```makefile
build:
	cargo build

run:
	cargo run

clean:
	cargo clean
```

- 執行 `make build` 僅進行編譯。
- 執行 `make run` 來建置（如果需要）並執行。
- 執行 `make clean` 來清除建置產物。

### 處理你先前的情境
由於你正在處理一個 Rust 專案，其中 `main.rs` 呼叫了 `simple.rs` 中的 `run_simple`，請確保透過在 `src/simple.rs` 中將 `run_simple` 設為公開來解決隱私錯誤（`E0603`）：

```rust
pub fn run_simple() {
    println!("Hello from run_simple!");
}
```

並在 `src/main.rs` 中：

```rust
mod simple;

fn main() {
    simple::run_simple();
}
```

同時，更新 `Cargo.toml` 以移除 `edition2024` 警告，如先前討論：

```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"
```

### 測試設定
1. 如上所示更新 `Makefile`。
2. 執行：
   ```bash
   make run
   ```
   這將執行 `cargo run`，它會建置（如果需要）並執行程式，印出 `Hello from run_simple!`（或 `run_simple` 產生的任何輸出）。
3. 如果你想單獨驗證編譯：
   ```bash
   make build
   ```

### 補充說明
- 如果你使用 `cargo run --bin simple`（用於 `simple.rs` 中的獨立二進位檔），請確保 `Cargo.toml` 包含：

  ```toml
  [[bin]]
  name = "simple"
  path = "src/simple.rs"
  ```

  且 `simple.rs` 有 `main` 函式：

  ```rust
  pub fn run_simple() {
      println!("Hello from run_simple!");
  }

  fn main() {
      run_simple();
  }
  ```

- 如果遇到問題，請分享 `make run` 或 `cargo run` 的輸出以進一步除錯。

### 最終 `Makefile` 建議

```makefile
build:
	cargo build

run:
	cargo run

clean:
	cargo clean
```

這個設定避免了冗餘，同時支援建置和執行，並保持工作流程簡潔。如果你有更多問題或需要特定錯誤的協助，請告訴我！