---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Installieren von Rust auf Ubuntu
translated: true
type: note
---

### Rust auf Ubuntu 22.04 LTS installieren

Rust wird am besten mit `rustup`, dem offiziellen Toolchain-Installer, installiert. Diese Methode ist unkompliziert, unterstützt einfache Updates und funktioniert auf Ihrem 64-Bit-Ubuntu-22.04-System. In der Regel sind keine zusätzlichen Abhängigkeiten über eine grundlegende Ubuntu-Einrichtung hinaus erforderlich.

#### Schritt-für-Schritt-Anleitung

1.  **Aktualisieren Sie Ihre Paketliste** (optional, aber empfohlen):
    ```
    sudo apt update
    ```

2.  **Installieren Sie Rust mit rustup**:
    Führen Sie den folgenden Befehl aus, um das Installationsskript herunterzuladen und auszuführen:
    ```
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```
    - Dies lädt das Skript sicher über HTTPS herunter.
    - Wenn Sie dazu aufgefordert werden, wählen Sie die Standardinstallationsoption (drücken Sie `1` und Enter).
    - Der Installer fügt die Rust-Binärdateien zu `~/.cargo/bin` hinzu und aktualisiert Ihr Shell-Profil (z.B. `~/.bashrc` oder `~/.profile`).

3.  **Laden Sie Ihre Shell-Konfiguration neu**:
    Um die Änderungen sofort zu übernehmen, ohne Ihr Terminal neu zu starten:
    ```
    source ~/.cargo/env
    ```
    Alternativ können Sie Ihr Terminal schließen und wieder öffnen.

4.  **Überprüfen Sie die Installation**:
    Prüfen Sie, ob Rust korrekt installiert wurde:
    ```
    rustc --version
    cargo --version
    ```
    Sie sollten eine Ausgabe wie `rustc 1.82.0` (oder die neueste stabile Version) und Ähnliches für Cargo sehen.

#### Zusätzliche Hinweise
-   **Deinstallation**: Führen Sie bei Bedarf `rustup self uninstall` aus.
-   **Rust aktualisieren**: Verwenden Sie `rustup update`, um die neueste Version zu erhalten.
-   **IDE/Support**: Für die Entwicklung können Sie `rust-analyzer` über Ihren Editor installieren (z.B. VS Code Extension) für eine bessere Code-Vervollständigung.
-   Standardmäßig wird der Stable-Kanal installiert. Für Nightly oder Beta verwenden Sie nach der Einrichtung `rustup install nightly`.

Falls Sie Fehler erhalten (z.B. curl nicht gefunden), installieren Sie es mit `sudo apt install curl`.

[Offizieller Rust-Installationsleitfaden](https://www.rust-lang.org/tools/install)