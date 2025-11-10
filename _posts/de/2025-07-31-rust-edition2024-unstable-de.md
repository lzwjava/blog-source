---
audio: false
generated: true
image: false
lang: de
layout: post
title: Edition 2024 in Rust aktivieren
translated: true
type: note
---

Der Fehler tritt auf, weil Ihr Rust-Projekt versucht, das `edition2024`-Feature zu verwenden, das in Ihrer aktuellen Cargo-Version (1.75.0) noch nicht stabilisiert ist. Um dies zu beheben, müssen Sie das instabile `edition2024`-Feature explizit aktivieren.

### Schritte zur Behebung:

1. **Aktivieren Sie das `edition2024`-Feature**:
   Öffnen Sie Ihre `Cargo.toml`-Datei und fügen Sie die folgende Zeile ganz oben hinzu, vor dem `[package]`-Abschnitt:

   ```toml
   cargo-features = ["edition2024"]
   ```

   Beispielsweise könnte Ihre `Cargo.toml`-Datei dann so aussehen:

   ```toml
   cargo-features = ["edition2024"]

   [package]
   name = "your_project_name"
   version = "0.1.0"
   edition = "2024"
   ```

2. **Verwenden Sie eine Nightly Rust Toolchain**:
   Da `edition2024` ein instabiles Feature ist, müssen Sie die nightly Rust-Toolchain verwenden, da stabile Versionen (wie 1.75.0) dies nicht unterstützen. Führen Sie die folgenden Befehle aus:

   ```bash
   rustup update nightly
   rustup override set nightly
   ```

   Der erste Befehl aktualisiert die nightly-Toolchain, und der zweite Befehl stellt Ihr Projektverzeichnis so ein, dass es die nightly-Toolchain verwendet.

3. **Führen Sie den Build erneut aus**:
   Nachdem Sie diese Änderungen vorgenommen haben, versuchen Sie, Ihr Projekt erneut zu builden:

   ```bash
   cargo build
   ```

### Zusätzliche Hinweise:
- Das `edition2024`-Feature ist experimentell und kann sich ändern. Überprüfen Sie die Rust-Dokumentation auf Updates zum Status: [Rust Edition 2024](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#edition-2024).
- Wenn Sie `edition2024` nicht benötigen, können Sie in `Cargo.toml` auf eine stabile Edition (z.B. `edition = "2021"`) zurückwechseln, um die Verwendung der nightly-Toolchain zu vermeiden.
- Stellen Sie sicher, dass Ihr `rustup` auf dem neuesten Stand ist, indem Sie `rustup update` ausführen.

Wenn Sie weiterhin Probleme haben, teilen Sie den Inhalt Ihrer `Cargo.toml`-Datei oder etwaige neue Fehlermeldungen für spezifischere Anleitung mit.

[Rust Edition 2024](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#edition-2024)