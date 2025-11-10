---
audio: false
generated: true
image: false
lang: es
layout: post
title: Compilar Ejemplo con Cargo
translated: true
type: note
---

Para que tu ejemplo compile, necesitas:

1. **Declarar las crates** que estás usando en `Cargo.toml`
2. **Proporcionar una función `main`** (y un runtime, si estás usando peticiones async)
3. **Eliminar** el `feature flag` `edition2024` que ya no es necesario

---

### 1. Actualiza `Cargo.toml`

```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"        # elige la edición actual; no necesitas un feature flag

[dependencies]
# Runtime async para `#[tokio::main]`
tokio = { version = "1.28", features = ["macros", "rt-multi-thread"] }

# Cliente HTTP con soporte JSON
reqwest = { version = "0.11", features = ["json"] }

# Serde para (de)serialización
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```

> **Nota:** Elimina cualquier sección `[features]` que liste `edition2024` — está integrada a partir de Cargo 1.85.

---

### 2. Proporciona una `main` async

Si quieres usar `reqwest::Client` (async), envuelve tu código en el runtime de Tokio:

```rust
// src/main.rs
use reqwest::{Client, StatusCode};
use serde_json::{json, Value};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Construye un cliente
    let client = Client::new();

    // Ejemplo GET
    let res = client
        .get("https://httpbin.org/status/200")
        .send()
        .await?;

    println!("Status: {}", res.status());

    // Ejemplo de cuerpo JSON
    let body: Value = res.json().await?;
    println!("JSON response: {}", body);

    Ok(())
}
```

---

### 3. (Alternativa) Usa reqwest blocking

Si no quieres async o Tokio, cambia a `reqwest::blocking` y elimina la dependencia de `tokio`:

```rust
// En Cargo.toml, elimina tokio y cambia reqwest a:
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

Con estos cambios, ejecutar `cargo build` (y luego `cargo run`) debería tener éxito.