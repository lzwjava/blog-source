---
audio: false
generated: true
image: false
lang: ar
layout: post
title: تجميع مثال باستخدام كارجو
translated: true
type: note
---

لجعل مثالك يُترجم، تحتاج إلى:

1. **تحديد الصنفات (crates)** التي تستخدمها في ملف `Cargo.toml`
2. **توفير دالة `main`** (وقت تشغيل (runtime)، إذا كنت تستخدم طلبات غير متزامنة (async))
3. **إزالة** سمة `edition2024` التي لم تعد ضرورية

---

### 1. تحديث `Cargo.toml`

```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"        # اختر الإصدار الحالي؛ لا حاجة لسمة feature flag

[dependencies]
# Async runtime for `#[tokio::main]`
tokio = { version = "1.28", features = ["macros", "rt-multi-thread"] }

# HTTP client with JSON support
reqwest = { version = "0.11", features = ["json"] }

# Serde for (de)serialization
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```

> **ملاحظة:** أزل أي قسم `[features]` يحتوي على `edition2024` — فقد أصبحت مدمجة بدءًا من Cargo 1.85.

---

### 2. توفير دالة `main` غير متزامنة

إذا كنت تريد استخدام `reqwest::Client` (غير المتزامن)، فغلف الكود الخاص بك في وقت تشغيل (runtime) توكيو (Tokio):

```rust
// src/main.rs
use reqwest::{Client, StatusCode};
use serde_json::{json, Value};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Build a client
    let client = Client::new();

    // Example GET
    let res = client
        .get("https://httpbin.org/status/200")
        .send()
        .await?;

    println!("Status: {}", res.status());

    // Example JSON body
    let body: Value = res.json().await?;
    println!("JSON response: {}", body);

    Ok(())
}
```

---

### 3. (بديل) استخدام reqwest المتزامن (blocking)

إذا كنت لا تريد استخدام البرمجة غير المتزامنة أو توكيو، فانتقل إلى `reqwest::blocking` وأزل الاعتماد على `tokio`:

```rust
// In Cargo.toml, remove tokio and change reqwest to:
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

مع هذه التغييرات، يجب أن ينجح تشغيل `cargo build` (ثم `cargo run`).