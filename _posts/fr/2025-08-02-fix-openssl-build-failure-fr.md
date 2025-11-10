---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Correction de l'Échec de Compilation d'OpenSSL
translated: true
type: note
---

Vous rencontrez l'erreur classique de compilation "openssl-sys" car vous n'avez pas installé l'outil pkg-config du système ou les en-têtes de développement d'OpenSSL. Sur Ubuntu/Debian, la solution la plus simple est :

1. **Installer pkg-config et les en-têtes de développement OpenSSL**

   ```bash
   sudo apt update
   sudo apt install pkg-config libssl-dev
   ```

   * `pkg-config` permet au script de compilation Rust de détecter où se trouve OpenSSL.
   * `libssl-dev` fournit les en-têtes et bibliothèques (le paquet « –dev »).

2. **Relancer votre compilation**

   ```bash
   cargo clean
   cargo run
   ```

---

### Alternative : utiliser la fonctionnalité "vendored"

Si vous ne voulez pas dépendre d'OpenSSL système (ou si vous n'avez pas les droits administrateur), vous pouvez demander à la crate de compiler une copie groupée d'OpenSSL à partir des sources :

1. Dans votre **Cargo.toml**, modifiez votre dépendance comme suit :

   ```toml
   [dependencies]
   openssl = { version = "0.10", features = ["vendored"] }
   ```
2. Puis recompilez :

   ```bash
   cargo clean
   cargo run
   ```

Cela compilera OpenSSL lui-même et effectuera l'édition des liens avec cette version, évitant ainsi d'avoir besoin d'une installation système.

---

### (Optionnel) Installation personnalisée d'OpenSSL

Si vous avez installé OpenSSL dans un emplacement non standard, vous pouvez indiquer à la compilation où le trouver :

```bash
export OPENSSL_DIR=/chemin/vers/votre/openssl
export OPENSSL_LIB_DIR=$OPENSSL_DIR/lib
export OPENSSL_INCLUDE_DIR=$OPENSSL_DIR/include
```

Puis relancez `cargo run`. Cela indique à openssl-sys exactement où trouver les en-têtes et les bibliothèques.

---

> **Remarque :** L'avertissement concernant la stabilisation d'`edition2024` est inoffensif — vous pouvez supprimer cette fonctionnalité de votre `Cargo.toml`, mais elle ne bloquera pas votre compilation.