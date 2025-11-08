---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 Protobuf 編譯器建置錯誤
translated: true
type: note
---

### 理解錯誤原因

這個編譯失敗發生在編譯 `greptime-proto` crate 中的 Protocol Buffers (`.proto` 檔案) 時。建置腳本（使用 `prost-build`）需要 `protoc` 二進制檔案來從這些 proto 定義生成 Rust 程式碼，但在你的系統中找不到它。這是編譯依賴 gRPC 和 protobuf 進行內部通訊的專案（如 GreptimeDB）時常見的先決條件遺漏問題。

列出的 `.proto` 檔案（例如 `database.proto`、`health.proto`）是 GreptimeDB 用於 metadata、regions、WAL 等的核心定義，因此跳過此步驟會阻擋整個建置過程。

### 快速修復

1. **安裝 Protobuf 編譯器**（需要 ≥ 3.15 版本）：
   - 在 Debian/Ubuntu 上（符合你的錯誤提示）：
     ```
     sudo apt update
     sudo apt install protobuf-compiler
     ```
   - 在 Fedora/RHEL 上：
     ```
     sudo dnf install protobuf-compiler
     ```
   - 在 macOS 上（如適用）：
     ```
     brew install protobuf
     ```
   - 手動下載（跨平台）：從 [Protocol Buffers 發布頁面](https://github.com/protocolbuffers/protobuf/releases) 獲取最新版本，解壓縮後將 `bin/protoc` 加入你的 PATH 環境變數。

2. **驗證安裝**：
   ```
   protoc --version
   ```
   它應該輸出類似 `libprotoc 3.21.12` 的內容（或更高版本；任何 ≥ 3.15 的版本均可使用）。

3. **重新嘗試建置**：
   ```
   make clean  # 可選，用於清除任何部分產生的檔案
   make
   ```
   如果 `protoc` 已安裝但仍找不到（例如 PATH 問題），請設定環境變數：
   ```
   export PROTOC=/usr/bin/protoc  # 根據需要調整路徑
   make
   ```

### 其他提示
- 確保你已安裝其他先決條件：Nightly Rust（從先前的錯誤看來你似乎已擁有）、GCC/G++（透過 `sudo apt install build-essential` 安裝）以及 glibc 開發標頭檔（`sudo apt install libc6-dev`）。
- 如果你在容器或自訂環境中，請在該處加入安裝步驟。
- 建置後測試使用：`cargo run --bin greptime -- standalone start`。

這應該能讓你通過 proto 編譯階段。如果它在其他方面失敗（例如 C++ 依賴項），請檢查完整的先決條件。

### 參考資料
- [GreptimeDB GitHub：從原始碼建置](https://github.com/GreptimeTeam/greptimedb#build-from-source)
- [prost-build 文件：Sourcing Protoc](https://docs.rs/prost-build/#sourcing-protoc)