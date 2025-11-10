---
audio: false
generated: true
image: false
lang: hi
layout: post
title: कार्गो के साथ उदाहरण संकलित करें
translated: true
type: note
---

अपना उदाहरण कंपाइल करने के लिए, आपको यह करना होगा:

1. **`Cargo.toml` में उपयोग किए जा रहे क्रेट्स घोषित करें**
2. **एक `main` फ़ंक्शन प्रदान करें** (और एक रनटाइम, यदि आप async अनुरोधों का उपयोग कर रहे हैं)
3. **अब अनावश्यक `edition2024` फीचर फ्लैग को हटा दें**

---

### 1. `Cargo.toml` अपडेट करें

```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"        # वर्तमान एडिशन चुनें; फीचर फ्लैग की आवश्यकता नहीं है

[dependencies]
# `#[tokio::main]` के लिए Async runtime
tokio = { version = "1.28", features = ["macros", "rt-multi-thread"] }

# JSON सपोर्ट के साथ HTTP client
reqwest = { version = "0.11", features = ["json"] }

# (डी)सीरियलाइज़ेशन के लिए Serde
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```

> **नोट:** `edition2024` वाले किसी भी `[features]` सेक्शन को हटा दें — यह Cargo 1.85 से बिल्ट-इन है।

---

### 2. एक async `main` प्रदान करें

यदि आप `reqwest::Client` (async) का उपयोग करना चाहते हैं, तो अपने कोड को Tokio के रनटाइम में लपेटें:

```rust
// src/main.rs
use reqwest::{Client, StatusCode};
use serde_json::{json, Value};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // एक क्लाइंट बनाएं
    let client = Client::new();

    // उदाहरण GET
    let res = client
        .get("https://httpbin.org/status/200")
        .send()
        .await?;

    println!("Status: {}", res.status());

    // उदाहरण JSON बॉडी
    let body: Value = res.json().await?;
    println!("JSON response: {}", body);

    Ok(())
}
```

---

### 3. (विकल्प) ब्लॉकिंग reqwest का उपयोग करें

यदि आप async या Tokio नहीं चाहते हैं, तो `reqwest::blocking` पर स्विच करें और `tokio` डिपेंडेंसी हटा दें:

```rust
// Cargo.toml में, tokio को हटाएं और reqwest को इस प्रकार बदलें:
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

इन परिवर्तनों के साथ, `cargo build` (और फिर `cargo run`) चलाना सफल होना चाहिए।