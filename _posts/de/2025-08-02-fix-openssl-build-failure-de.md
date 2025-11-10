---
audio: false
generated: true
image: false
lang: de
layout: post
title: Behebung von OpenSSL-Build-Fehlern
translated: true
type: note
---

Du stößt auf den klassischen `openssl-sys`-Build-Fehler, weil du entweder das `pkg-config`-Tool oder die OpenSSL-Entwicklungsheader des Systems nicht installiert hast. Unter Ubuntu/Debian ist die einfachste Lösung:

1. **Installiere pkg-config und die OpenSSL-Dev-Header**

   ```bash
   sudo apt update
   sudo apt install pkg-config libssl-dev
   ```

   * `pkg-config` ermöglicht dem Rust-Build-Skript, OpenSSL zu finden.
   * `libssl-dev` stellt die Header und Bibliotheken bereit (das „–dev“-Paket).

2. **Starte deinen Build erneut**

   ```bash
   cargo clean
   cargo run
   ```

---

### Alternative: Verwende das "vendored"-Feature

Wenn du nicht von System-OpenSSL abhängen möchtest (oder keinen Root-Zugriff hast), kannst du das Crate anweisen, eine gebündelte Kopie von OpenSSL aus dem Quellcode zu erstellen:

1. Ändere in deiner **Cargo.toml** die Abhängigkeit zu:

   ```toml
   [dependencies]
   openssl = { version = "0.10", features = ["vendored"] }
   ```
2. Baue dann erneut:

   ```bash
   cargo clean
   cargo run
   ```

Dies kompiliert OpenSSL selbst und verlinkt dagegen, wodurch eine Systeminstallation überflüssig wird.

---

### (Optional) Benutzerdefinierte OpenSSL-Installation

Wenn du OpenSSL an einem nicht standardmäßigen Ort installiert hast, kannst du den Build darauf verweisen:

```bash
export OPENSSL_DIR=/pfad/zu/deinem/openssl
export OPENSSL_LIB_DIR=$OPENSSL_DIR/lib
export OPENSSL_INCLUDE_DIR=$OPENSSL_DIR/include
```

Starte dann `cargo run` erneut. Dies teilt openssl-sys genau mit, wo es Header und Bibliotheken finden kann.

---

> **Hinweis:** Die Warnung, dass `edition2024` stabilisiert wurde, ist harmlos – du kannst dieses Feature aus deiner `Cargo.toml` entfernen, aber es blockiert deinen Build nicht.