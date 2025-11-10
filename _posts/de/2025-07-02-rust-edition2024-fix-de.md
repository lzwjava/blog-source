---
audio: false
generated: true
lang: de
layout: post
title: Behebung von Rust Edition 2024 Fehlern
translated: true
type: note
---

Die Fehlermeldung `feature edition2024 is required` zeigt an, dass Ihr Projekt für die Verwendung der `edition2024` von Rust konfiguriert ist, Ihre aktuelle Cargo-Version (1.84.1) diese in einer stabilen Version jedoch noch nicht unterstützt. Edition 2024 wird noch als instabile/Nightly-Funktion betrachtet.

Hier erfahren Sie, wie Sie das Problem beheben, und Informationen zur neuesten Cargo-Version:

### Problembehebung

Sie haben zwei Hauptoptionen:

**1. Eine Nightly Rust Toolchain verwenden (Empfohlen für `edition2024`)**

Da `edition2024` eine instabile Funktion ist, müssen Sie einen Nightly-Build von Rust und Cargo verwenden, um Ihr Projekt zu kompilieren.

  * **Nightly Toolchain installieren:** Falls Sie sie noch nicht haben, installieren Sie die Nightly-Toolchain mit `rustup`:
    ```bash
    rustup toolchain install nightly
    ```
  * **Nightly Toolchain für den Build verwenden:** Sie können Cargo anweisen, die Nightly-Toolchain speziell für diesen Befehl zu verwenden:
    ```bash
    OPENSSL_STATIC=yes cargo +nightly build --release
    ```
  * **(Optional) Nightly als Standard für das Projekt festlegen:** Wenn Sie möchten, dass dieses Projekt immer Nightly verwendet, können Sie eine `rust-toolchain.toml`-Datei im Stammverzeichnis Ihres Projekts mit folgendem Inhalt erstellen:
    ```toml
    [toolchain]
    channel = "nightly"
    ```
    Anschließend können Sie einfach `OPENSSL_STATIC=yes cargo build --release` wie gewohnt ausführen, und `rustup` wählt automatisch die Nightly-Toolchain für dieses Projekt aus.

**2. Die Edition Ihres Projekts herabstufen (Falls `edition2024`-Funktionen nicht kritisch sind)**

Wenn Ihr Projekt nicht strikt auf `edition2024`-Funktionen angewiesen ist, könnten Sie die Edition in Ihrer `Cargo.toml` auf `2021` (die aktuelle stabile Edition) zurücksetzen.

  * **`Cargo.toml` bearbeiten:** Öffnen Sie die `Cargo.toml`-Datei Ihres Projekts (laut Fehlermeldung `/Users/lzwjava/projects/seeker/seeker/Cargo.toml`) und ändern Sie das `edition`-Feld:
    ```toml
    [package]
    name = "your-package-name"
    version = "0.1.0"
    edition = "2021" # Ändern Sie dies von "2024" zu "2021"
    ```
  * **`cargo fix --edition` ausführen (Optional, aber empfohlen):** Nach dem Ändern der Edition sollten Sie möglicherweise `cargo fix --edition` ausführen, um Teile des Codes automatisch auf Kompatibilität mit der älteren Edition zu aktualisieren.

### Was ist die neueste Cargo-Version?

Stand Juli 2025 ist die neueste **stabile** Version von Cargo (und Rust) **1.88.0**.

Die `edition2024`-Funktion befindet sich noch im Nightly-Channel, was bedeutet, dass sie sich in aktiver Entwicklung befindet und noch nicht Teil einer stabilen Version ist. Es wird erwartet, dass sie in einer zukünftigen Version, voraussichtlich Rust 1.89.0 (derzeit in Beta), stabilisiert wird.