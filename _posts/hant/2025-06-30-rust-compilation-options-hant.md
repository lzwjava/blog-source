---
audio: false
generated: true
lang: hant
layout: post
title: Rust 輸出位置選項
translated: true
type: note
---

你問了一個很好的問題，這涉及到 Rust 專案的典型結構和建置方式！

當你直接使用 `rustc` 時，有兩個主要選項可以指定輸出位置：

1.  **`-o <output_filename>`**：此選項指定編譯後的可執行檔或函式庫的*確切路徑和檔案名稱*。

    ```bash
    rustc scripts/rust/example.rs -o test/example
    ```

    這會編譯 `example.rs` 並將名為 `example` 的可執行檔直接放入 `test/` 目錄中。如果 `test/` 不存在，`rustc` 會建立它。

2.  **`--out-dir <output_directory>`**：此選項指定一個*目錄*，`rustc` 應將所有生成的輸出檔案（可執行檔/函式庫，以及任何中間檔案，如 `.d`、`.rmeta` 等）放入該目錄。

    ```bash
    rustc scripts/rust/example.rs --out-dir test/
    ```

    在這種情況下，`rustc` 會編譯 `example.rs` 並將可執行檔（預設名稱為 `example`，源自原始檔名）放入 `test/` 目錄內。

**建議：對於專案請使用 Cargo**

雖然直接使用 `rustc` 能提供細粒度的控制，但對於大多數 Rust 專案，你會希望使用 **Cargo**。Cargo 是 Rust 的建置系統和套件管理員，它簡化了依賴項管理、建置、測試和執行程式碼的過程。

使用 Cargo 時，輸出二進位檔通常會放在專案根目錄下的 `target` 目錄中。例如，如果你有一個使用 Cargo 設定的專案：

```
my_project/
├── Cargo.toml
└── src/
    └── main.rs
```

當你執行 `cargo build` 或 `cargo run` 時，編譯後的可執行檔將被放置在 `my_project/target/debug/my_project`（用於除錯建置）或 `my_project/target/release/my_project`（用於發行建置）。

如果你想控制 Cargo 的 `target` 目錄，你可以：

  * **使用 `CARGO_TARGET_DIR` 環境變數**：

    ```bash
    CARGO_TARGET_DIR=./test cargo build
    ```

    這會將整個 `target` 目錄（包含 `debug`、`release` 等）放入你的 `test/` 目錄中。可執行檔隨後會位於 `test/debug/my_project`。

  * **使用 Cargo 的 `--target-dir` 命令列選項**：

    ```bash
    cargo build --target-dir test/
    ```

    這與使用環境變數的效果相同。

  * **使用 `.cargo/config.toml`**：你可以透過將其加入到 `.cargo/config.toml` 檔案中，為你機器上的所有 Cargo 專案或特定工作區設定預設的 `target-dir`。

**為什麼要使用 Cargo？**

  * **標準化的專案佈局：** Cargo 強制執行通用的專案結構，使其他 Rust 開發者容易理解你的程式碼。
  * **依賴項管理：** Cargo 自動處理專案依賴項的下載和編譯。
  * **測試和效能評測：** Cargo 內建了執行測試（`cargo test`）和效能評測（`cargo bench`）的命令。
  * **發行管理：** Cargo 有助於建立發行建置（`cargo build --release`）並將 crate 發佈到 crates.io。

除非你有非常特定的理由不這樣做，否則強烈建議將你的 Rust 程式碼組織成 Cargo 專案。

**根據你的 `git status` 輸出：**

你的 `git status` 顯示 `example` 和 `scripts/rust/` 未被追蹤。這表明你可能是在 Cargo 專案之外直接使用 `rustc` 編譯 `scripts/rust/example.rs`。

如果 `example` 是編譯後的二進位檔，那麼之前的 `rustc scripts/rust/example.rs` 命令將其放置在了當前目錄（`lzwjava.github.io`）中。

要實現你將它放入 `test/example` 的目標（假設 `test` 是 `lzwjava.github.io` 根目錄下的一個目錄），你可以使用：

```bash
rustc scripts/rust/example.rs -o test/example
```

這是使用 `rustc` 獲得你所要求特定輸出路徑最直接的方法。