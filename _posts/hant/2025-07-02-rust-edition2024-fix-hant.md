---
audio: false
generated: true
lang: hant
layout: post
title: 修復 Rust 2024 版本錯誤
translated: true
type: note
---

錯誤訊息 `feature edition2024 is required` 表示你的專案設定為使用 Rust 的 `edition2024`，但你目前的 Cargo 版本 (1.84.1) 在穩定版中尚未支援此功能。Edition 2024 目前仍被視為不穩定/夜間版功能。

以下是解決方法及 Cargo 最新版本的相關資訊：

### 如何修復

你有兩個主要選擇：

**1. 使用夜間版 Rust 工具鏈（推薦用於 `edition2024`）**

由於 `edition2024` 是不穩定功能，你需要使用 Rust 和 Cargo 的夜間建置版來編譯專案。

  * **安裝夜間版工具鏈：** 如果尚未安裝，請使用 `rustup` 安裝夜間版工具鏈：
    ```bash
    rustup toolchain install nightly
    ```
  * **使用夜間版工具鏈進行建置：** 你可以指示 Cargo 在此指令中特別使用夜間版工具鏈：
    ```bash
    OPENSSL_STATIC=yes cargo +nightly build --release
    ```
  * **（可選）將夜間版設為專案預設：** 若希望此專案始終使用夜間版，可在專案根目錄建立 `rust-toolchain.toml` 檔案，內容如下：
    ```toml
    [toolchain]
    channel = "nightly"
    ```
    之後，你只需照常執行 `OPENSSL_STATIC=yes cargo build --release`，`rustup` 會自動為此專案選用夜間版工具鏈。

**2. 降級專案的 Edition（若 `edition2024` 功能非必需）**

若專案未嚴格依賴 `edition2024` 功能，可將 edition 改回 `2021`（當前穩定版）。

  * **編輯 `Cargo.toml`：** 開啟專案的 `Cargo.toml` 檔案（根據錯誤訊息中的路徑 `/Users/lzwjava/projects/seeker/seeker/Cargo.toml`），修改 `edition` 欄位：
    ```toml
    [package]
    name = "your-package-name"
    version = "0.1.0"
    edition = "2021" # 將此處從 "2024" 改為 "2021"
    ```
  * **執行 `cargo fix --edition`（可選但建議）：** 變更 edition 後，建議執行 `cargo fix --edition` 以自動更新部分程式碼，確保與舊版 edition 相容。

### Cargo 最新版本為何？

截至 2025 年 7 月，Cargo（及 Rust）的最新**穩定**版本為 **1.88.0**。

`edition2024` 功能目前仍處於夜間版通道，意味著它正在積極開發中，尚未納入穩定版。預計將在未來版本中穩定化，很可能是 Rust 1.89.0（目前處於測試階段）。