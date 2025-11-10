---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Cargoでのコンパイル例
translated: true
type: note
---

あなたの例をコンパイルするには、以下の手順が必要です：

1. **クレートの宣言**を `Cargo.toml` に記述する
2. **`main` 関数を提供する**（非同期リクエストを使用する場合はランタイムも）
3. **不要になった `edition2024` 機能フラグを削除する**

---

### 1. `Cargo.toml` の更新

```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"        # 現在のエディションを選択。機能フラグは不要

[dependencies]
# `#[tokio::main]` のための非同期ランタイム
tokio = { version = "1.28", features = ["macros", "rt-multi-thread"] }

# JSON サポート付き HTTP クライアント
reqwest = { version = "0.11", features = ["json"] }

# (デ)シリアライゼーションのための Serde
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```

> **注意:** `edition2024` をリストしている `[features]` セクションは削除してください — Cargo 1.85 以降では組み込まれています。

---

### 2. 非同期 `main` 関数の提供

`reqwest::Client`（非同期）を使用したい場合は、コードを Tokio のランタイムでラップしてください：

```rust
// src/main.rs
use reqwest::{Client, StatusCode};
use serde_json::{json, Value};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // クライアントの構築
    let client = Client::new();

    // GET リクエストの例
    let res = client
        .get("https://httpbin.org/status/200")
        .send()
        .await?;

    println!("Status: {}", res.status());

    // JSON ボディの例
    let body: Value = res.json().await?;
    println!("JSON response: {}", body);

    Ok(())
}
```

---

### 3. (代替案) ブロッキング reqwest の使用

非同期や Tokio を使用したくない場合は、`reqwest::blocking` に切り替えて `tokio` 依存関係を削除してください：

```rust
// Cargo.toml で、tokio を削除し、reqwest を以下に変更：
reqwest = { version = "0.11", features = ["blocking", "json"] }

// src/main.rs:
use reqwest::blocking::Client;
use serde_json::Value;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new();
    let res = client.get("https://httpbin.org/status/200").send()?;
    println!("Status: {}", res.status());
    let body: Value = res.json()?;
    println!("JSON response: {}", body);
    Ok(())
}
```

これらの変更を加えると、`cargo build`（そして `cargo run`）の実行が成功するはずです。