---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Shell 鏈接的 Rust 單行指令
translated: true
type: note
---

你提到的正是許多從 Python、Ruby 或 JavaScript 等語言轉來的資深開發者常有的需求——在那些語言中，通常只需一個指令就能直接執行腳本。Rust 作為編譯型語言，其預設工作流程略有不同。

不過，你絕對可以透過在 shell 中串聯指令的方式，實現類似「一行指令」的便捷操作，特別是在處理簡單腳本或練習時。

### 直接的「一行指令」方案（Shell 串聯）

你已經掌握了必要的組件：用 `rustc` 編譯，用 `./` 執行。你可以透過 shell 運算子將它們組合起來：

```bash
rustc scripts/rust/example.rs -o test/example && ./test/example
```

**說明：**

  * `rustc scripts/rust/example.rs -o test/example`：此指令編譯你的 Rust 檔案，並將可執行檔輸出至 `test/example`。
  * `&&`：這是 bash（及大多數類 Unix shell）中的**條件式指令分隔符號**。只有在 `&&` *之前*的指令成功完成（即返回退出碼 0）時，`&&` *之後*的指令才會執行。
      * 如果 `rustc` 編譯無誤，它將返回 0，接著 `./test/example` 便會執行。
      * 如果 `rustc` 遇到編譯錯誤，它將返回非零的退出碼，而 `./test/example` 就*不會*被執行。這是理想的行為\！

### 追求更「腳本化」的體驗（使用 Cargo）

雖然上述的 `&&` 方法適用於快速測試，但對於任何超越簡單單檔案的腳本任務，Rust 的 `cargo` 工具是推薦的方式，而且它*確實*提供了類似 Python 的一行指令來執行專案內的程式碼：

1.  **初始化 Cargo 專案（若尚未進行）：**
    如果你的 `scripts/rust/example.rs` 只是一個獨立的檔案，你通常應該在其父目錄（或一個新的專用目錄）中建立一個 Cargo 專案。

    ```bash
    # 切換到你希望建立專案的目錄（例如 scripts/rust）
    cd scripts/rust

    # 初始化一個新的 Cargo 二進位制專案
    cargo init --bin .
    ```

    這將建立 `Cargo.toml`，並將你的 `example.rs` 移動為 `main.rs`（或調整 `Cargo.toml` 指向它，如果你將 `example.rs` 重新命名為 `src/` 內的 `main.rs`）。

2.  **使用 Cargo 執行：**
    一旦你設定好 Cargo 專案，就可以用單一指令編譯並執行：

    ```bash
    # 從你的專案根目錄執行（例如，如果你在 scripts/rust 執行了 cargo init）
    cargo run
    ```

    `cargo run` 將會：

      * 編譯你的程式碼（如果尚未編譯或程式碼有變更）。
      * 接著，執行產生的二進位制檔案。
      * 預設情況下，二進位制檔案會放在專案內的 `target/debug/` 目錄中，但你無需擔心其具體路徑。

**為何推薦使用 Cargo：**

  * **依賴管理：** 如果你的程式碼需要外部函式庫（crate），Cargo 會自動處理下載、編譯和鏈結。你只需在 `Cargo.toml` 中指定它們。
  * **標準專案結構：** 它鼓勵一致的專案佈局（`src/main.rs`、`Cargo.toml`），這讓你的程式碼更容易被他人（以及未來的你）理解。
  * **測試：** `cargo test` 會執行你的單元測試和整合測試。
  * **發行版本建置：** `cargo run --release`（或 `cargo build --release`）會啟用優化編譯，適用於生產環境。
  * **無需手動清理：** 你無需手動刪除編譯出的二進位制檔案。`cargo clean` 會負責清理。

### 那有沒有像 Python 的 `python script.py` 那樣真正的「腳本」執行方式？

Rust 並非設計為直譯式腳本語言。它是一門編譯型系統語言。因此，你不會有一個直接的 `rust script.rs` 指令，能夠無需明確編譯步驟就直接編譯並執行。

然而，社群中有一些工具試圖彌合這一差距，用於快速執行單檔案的 Rust「腳本」（儘管它們底層仍然在進行編譯）：

  * **`cargo-script`**：一個 Cargo 子指令，允許你執行單一的 `.rs` 檔案，並透過註解處理依賴關係。你通常可以透過 `cargo install cargo-script` 安裝它。然後，你或許可以執行 `cargo script scripts/rust/example.rs`。
  * **`rust-script`**：另一個流行的工具，用於像腳本一樣直接執行 Rust 檔案。透過 `cargo install rust-script` 安裝。然後，你通常只需讓你的 `.rs` 檔案具有可執行權限（`chmod +x example.rs`）並執行它：`./example.rs`。它會在後台處理編譯和執行。

對於你快速測試 `example.rs` 的需求，使用 `rustc ... && ./...` 這種一行指令的方式完全可行，並直接解答了你關於如何串聯兩個指令的問題。對於任何非簡單的開發工作，擁抱 Cargo 將會是更高效且更符合 Rust 慣例的體驗。