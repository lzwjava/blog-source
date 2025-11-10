---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 啟用 Rust 2024 版本
translated: true
type: note
---

發生此錯誤是因為你的 Rust 專案試圖使用 `edition2024` 功能，但該功能在你目前的 Cargo 版本 (1.75.0) 中尚未穩定。要解決此問題，你需要明確啟用不穩定的 `edition2024` 功能。

### 解決步驟：

1. **啟用 `edition2024` 功能**：
   開啟你的 `Cargo.toml` 檔案，並在 `[package]` 區段之前的最頂端加入以下行：

   ```toml
   cargo-features = ["edition2024"]
   ```

   例如，你的 `Cargo.toml` 可能會看起來像這樣：

   ```toml
   cargo-features = ["edition2024"]

   [package]
   name = "your_project_name"
   version = "0.1.0"
   edition = "2024"
   ```

2. **使用 Nightly Rust 工具鏈**：
   由於 `edition2024` 是不穩定功能，你需要使用 nightly Rust 工具鏈，因為穩定版本 (如 1.75.0) 不支援它。執行以下命令：

   ```bash
   rustup update nightly
   rustup override set nightly
   ```

   第一個命令會更新 nightly 工具鏈，第二個命令則設定你的專案目錄使用 nightly 工具鏈。

3. **重新執行建置**：
   完成上述變更後，再次嘗試建置你的專案：

   ```bash
   cargo build
   ```

### 補充說明：
- `edition2024` 功能是實驗性的，可能會發生變更。請查閱 Rust 文件以了解其最新狀態：[Rust Edition 2024](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#edition-2024)
- 如果你不需要 `edition2024`，可以在 `Cargo.toml` 中切換回穩定版本 (例如 `edition = "2021"`) 以避免使用 nightly 工具鏈
- 請透過執行 `rustup update` 確保你的 `rustup` 是最新版本

如果你遇到其他問題，請提供你的 `Cargo.toml` 內容或任何新的錯誤訊息，以獲得更具體的指引。

[Rust Edition 2024](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#edition-2024)