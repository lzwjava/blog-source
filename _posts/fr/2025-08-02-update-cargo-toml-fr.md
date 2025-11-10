---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Compiler un exemple avec Cargo
translated: true
type: note
---

Pour que votre exemple compile, vous devez :

1. **Déclarer les crates** que vous utilisez dans `Cargo.tml`
2. **Fournir une fonction `main`** (et un runtime, si vous utilisez des requêtes asynchrones)
3. **Supprimer** le flag de fonctionnalité `edition2024` désormais inutile

---

### 1. Mettre à jour `Cargo.toml`

```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"        # choisissez l'édition actuelle ; pas besoin d'un flag de fonctionnalité

[dependencies]
# Runtime asynchrone pour `#[tokio::main]`
tokio = { version = "1.28", features = ["macros", "rt-multi-thread"] }

# Client HTTP avec support JSON
reqwest = { version = "0.11", features = ["json"] }

# Serde pour la (dé)sérialisation
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```

> **Remarque :** Supprimez toute section `[features]` listant `edition2024` — elle est intégrée depuis Cargo 1.85.

---

### 2. Fournir une fonction `main` asynchrone

Si vous souhaitez utiliser `reqwest::Client` (asynchrone), encapsulez votre code dans le runtime de Tokio :

```rust
// src/main.rs
use reqwest::{Client, StatusCode};
use serde_json::{json, Value};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Construire un client
    let client = Client::new();

    // Exemple GET
    let res = client
        .get("https://httpbin.org/status/200")
        .send()
        .await?;

    println!("Status: {}", res.status());

    // Exemple de corps JSON
    let body: Value = res.json().await?;
    println!("JSON response: {}", body);

    Ok(())
}
```

---

### 3. (Alternative) Utiliser reqwest en mode bloquant

Si vous ne voulez pas de code asynchrone ou de Tokio, passez à `reqwest::blocking` et supprimez la dépendance `tokio` :

```rust
// Dans Cargo.toml, supprimez tokio et modifiez reqwest comme suit :
reqwest = { version = "0.11", features = ["blocking", "json"] }

// src/main.rs :
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

Avec ces modifications, l'exécution de `cargo build` (puis `cargo run`) devrait réussir.