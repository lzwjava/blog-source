---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 修復 OpenSSL 編譯失敗問題
translated: true
type: note
---

你遇到的是典型的「openssl-sys」編譯失敗問題，這是因為系統未安裝 pkg-config 工具或 OpenSSL 開發標頭檔。在 Ubuntu/Debian 系統上，最簡單的解決方法是：

1. **安裝 pkg-config 與 OpenSSL 開發標頭檔**

   ```bash
   sudo apt update
   sudo apt install pkg-config libssl-dev
   ```

   * `pkg-config` 可讓 Rust 建置腳本偵測 OpenSSL 的位置
   * `libssl-dev` 提供標頭檔與函式庫（屬於「–dev」開發套件）

2. **重新執行建置**

   ```bash
   cargo clean
   cargo run
   ```

---

### 替代方案：使用「vendored」功能

若不想依賴系統的 OpenSSL（或沒有 root 權限），可要求 crate 從原始碼編譯內嵌的 OpenSSL：

1. 在 **Cargo.toml** 中將依賴項改為：

   ```toml
   [dependencies]
   openssl = { version = "0.10", features = ["vendored"] }
   ```
2. 重新執行建置：

   ```bash
   cargo clean
   cargo run
   ```

這會直接編譯 OpenSSL 並進行連結，無需安裝系統套件。

---

### （選用）自訂 OpenSSL 安裝路徑

若 OpenSSL 安裝在非標準路徑，可透過環境變數指定位置：

```bash
export OPENSSL_DIR=/path/to/your/openssl
export OPENSSL_LIB_DIR=$OPENSSL_DIR/lib
export OPENSSL_INCLUDE_DIR=$OPENSSL_DIR/include
```

接著重新執行 `cargo run`，這會明確告知 openssl-sys 標頭檔與函式庫的所在位置。

---

> **注意：** 關於 `edition2024` 已穩定的警告不影響執行——你可以從 `Cargo.toml` 移除該功能，但不會阻礙建置流程。