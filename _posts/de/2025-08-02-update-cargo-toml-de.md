---
audio: false
generated: true
image: false
lang: de
layout: post
title: Beispiel mit Cargo kompilieren
translated: true
type: note
---

Um dein Beispiel zum Kompilieren zu bringen, musst du:

1. **Die verwendeten Crates** in `Cargo.toml` deklarieren
2. **Eine `main`-Funktion** bereitstellen (und eine Runtime, falls du async Requests verwendest)
3. **Das nun unnötige** `edition2024`-Feature-Flag entfernen

---

### 1. Aktualisiere `Cargo.toml`

```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"        # wähle die aktuelle Edition; kein Feature-Flag nötig

[dependencies]
# Async-Runtime für `#[tokio::main]`
tokio = { version = "1.28", features = ["macros", "rt-multi-thread"] }

# HTTP-Client mit JSON-Unterstützung
reqwest = { version = "0.11", features = ["json"] }

# Serde für (De)Serialisierung
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```

> **Hinweis:** Entferne jeden `[features]`-Abschnitt, der `edition2024` auflistet – es ist ab Cargo 1.85 integriert.

---

### 2. Stelle eine async `main` bereit

Wenn du `reqwest::Client` (async) verwenden möchtest, wickle deinen Code in Tokios Runtime ein:

```rust
// src/main.rs
use reqwest::{Client, StatusCode};
use serde_json::{json, Value};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Erstelle einen Client
    let client = Client::new();

    // Beispiel GET
    let res = client
        .get("https://httpbin.org/status/200")
        .send()
        .await?;

    println!("Status: {}", res.status());

    // Beispiel JSON-Body
    let body: Value = res.json().await?;
    println!("JSON-Antwort: {}", body);

    Ok(())
}
```

---

### 3. (Alternative) Verwende blockierendes reqwest

Wenn du kein Async oder Tokio verwenden möchtest, wechsle zu `reqwest::blocking` und entferne die `tokio`-Abhängigkeit:

```rust
// In Cargo.toml, entferne tokio und ändere reqwest zu:
reqwest = { version = "0.11", features = ["blocking", "json"] }

// src/main.rs:
use reqwest::blocking::Client;
use serde_json::Value;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new();
    let res = client.get("https://httpbin.org/status/200").send()?;
    println!("Status: {}", res.status());
    let body: Value = res.json()?;
    println!("JSON-Antwort: {}", body);
    Ok(())
}
```

Mit diesen Änderungen sollte `cargo build` (und anschließend `cargo run`) erfolgreich ausgeführt werden.