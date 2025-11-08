---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 在 Ubuntu 上安裝 Rust
translated: true
type: note
---

### 在 Ubuntu 22.04 LTS 上安裝 Rust

建議使用官方工具鏈安裝程式 `rustup` 來安裝 Rust。這種方法簡單直接，支援輕鬆更新，並適用於您的 64 位元 Ubuntu 22.04 系統。除了基本的 Ubuntu 設定外，通常不需要額外的依賴項。

#### 逐步安裝說明

1. **更新套件清單**（可選但建議）：
   ```
   sudo apt update
   ```

2. **使用 rustup 安裝 Rust**：
   執行以下命令以下載並執行安裝腳本：
   ```
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   ```
   - 這將通過 HTTPS 安全下載腳本。
   - 當提示時，選擇預設安裝選項（按 `1` 並按 Enter）。
   - 安裝程式會將 Rust 二進位檔新增至 `~/.cargo/bin` 並更新您的 shell 設定檔（例如 `~/.bashrc` 或 `~/.profile`）。

3. **重新載入 shell 設定**：
   要立即讓變更生效而無需重新啟動終端機：
   ```
   source ~/.cargo/env
   ```
   或者，關閉並重新開啟終端機。

4. **驗證安裝**：
   檢查 Rust 是否正確安裝：
   ```
   rustc --version
   cargo --version
   ```
   您應該會看到類似 `rustc 1.82.0`（或最新的穩定版本）的輸出，Cargo 也會有類似的輸出。

#### 補充說明
- **解除安裝**：如有需要，請執行 `rustup self uninstall`。
- **更新 Rust**：使用 `rustup update` 來取得最新版本。
- **IDE/支援**：為了開發方便，考慮透過您的編輯器（例如 VS Code 擴充功能）安裝 `rust-analyzer` 以獲得更好的程式碼補全功能。
- 此安裝預設使用穩定版本通道。如需 nightly 或 beta 版本，請在設定後使用 `rustup install nightly`。

如果您遇到任何錯誤（例如找不到 curl），請使用 `sudo apt install curl` 安裝它。

[官方 Rust 安裝指南](https://www.rust-lang.org/tools/install)