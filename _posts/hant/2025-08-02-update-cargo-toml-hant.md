---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 使用 Cargo 編譯範例
translated: true
type: note
---

要讓你的範例成功編譯，你需要：

1. **在 `Cargo.tml` 中宣告**所使用的 crates
2. **提供 `main` 函式**（若使用非同步請求，還需提供執行環境）
3. **移除**現已不必要的 `edition2024` 功能標記

---

### 1. 更新 `Cargo.toml`

```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"        # 選擇當前版本；無需功能標記

[dependencies]
# 用於 `#[tokio::main]` 的非同步執行環境
tokio = { version = "1.28", features = ["macros", "rt-multi-thread"] }

# 支援 JSON 的 HTTP 客戶端
reqwest = { version = "0.11", features = ["json"] }

# 用於（反）序列化的 Serde
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```

> **注意：** 移除任何列出 `edition2024` 的 `[features]` 區段 — 自 Cargo 1.85 起已內建此功能。

---

### 2. 提供非同步 `main` 函式

若想使用 `reqwest::Client`（非同步），請將程式碼包裝在 Tokio 的執行環境中：

```rust
// src/main.rs
use reqwest::{Client, StatusCode};
use serde_json::{json, Value};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // 建立客戶端
    let client = Client::new();

    // GET 請求範例
    let res = client
        .get("https://httpbin.org/status/200")
        .send()
        .await?;

    println!("狀態: {}", res.status());

    // JSON 主體範例
    let body: Value = res.json().await?;
    println!("JSON 回應: {}", body);

    Ok(())
}
```

---

### 3. （替代方案）使用阻塞式 reqwest

若不想使用非同步或 Tokio，可改用 `reqwest::blocking` 並移除 `tokio` 依賴：

```rust
// 在 Cargo.toml 中移除 tokio，並將 reqwest 改為：
reqwest = { version = "0.11", features = ["blocking", "json"] }

// src/main.rs：
use reqwest::blocking::Client;
use serde_json::Value;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new();
    let res = client.get("https://httpbin.org/status/200").send()?;
    println!("狀態: {}", res.status());
    let body: Value = res.json()?;
    println!("JSON 回應: {}", body);
    Ok(())
}
```

完成這些修改後，執行 `cargo build`（接著執行 `cargo run`）應該就能成功。