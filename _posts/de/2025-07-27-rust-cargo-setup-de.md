---
audio: false
generated: true
image: false
lang: de
layout: post
title: Behebung der Rust-Projekteinrichtung
translated: true
type: note
---

Es sieht so aus, als würdest du versuchen, ein einfaches Rust-Projekt basierend auf dem bereitgestellten `Cargo.toml`-Auszug und der Dateistruktur (ein `rust`-Unterverzeichnis, das `example.rs` enthält) einzurichten und auszuführen. Es gibt jedoch einige Probleme, die eine sofortige Verwendung verhindern:

- Das Verzeichnis `/Users/lzwjava/projects/lzwjava.github.io` (dein GitHub Pages-Root) scheint noch nicht als gültiger Rust-Workspace konfiguriert zu sein, weshalb rust-analyzer zuvor fehlgeschlagen ist.
- Die Angabe `edition = "2025"` in `Cargo.toml` ist ungültig – die aktuellen Rust-Editionen sind 2015, 2018, 2021 und 2024 (veröffentlicht Anfang 2025). Es gibt keine Edition 2025.
- Von Cargo verwaltete Rust-Projekte erwarten eine Standardstruktur: `Cargo.toml` im Root-Verzeichnis, mit Quelldateien in einem `src/`-Unterverzeichnis (z.B. `src/main.rs` für eine ausführbare Binärdatei). Deine `example.rs` befindet sich in einem `rust/`-Unterverzeichnis, was standardmäßig nicht erkannt wird.
- Angenommen, `example.rs` enthält ein einfaches ausführbares Programm (z.B. ein "Hello, World!" mit `fn main()`), hast du zwei Hauptoptionen: Führe es als Einzeldatei-Skript aus (ohne Cargo) oder richte es als richtiges Cargo-Projekt ein.

Ich werde dir beide Ansätze Schritt für Schritt erklären. Verwende ein Terminal im Root-Verzeichnis deines Projekts (`lzwjava.github.io`).

### Option 1: Als Einzeldatei-Skript ausführen (Schnellste Methode, ohne Cargo)
Dies kompiliert und führt `example.rs` direkt mit dem Rust-Compiler (`rustc`) aus. Ideal, wenn du keine Abhängigkeiten oder ein vollständiges Projekt-Setup benötigst.

1. Wechsle in das Verzeichnis mit der Datei:
   ```
   cd rust
   ```

2. Kompiliere die Datei:
   ```
   rustc example.rs
   ```
   - Dies erzeugt eine ausführbare Datei namens `example` (unter macOS/Linux) oder `example.exe` (unter Windows).
   - Schlägt die Kompilierung fehl (z.B. aufgrund von Syntaxfehlern in `example.rs`), korrigiere den Code und versuche es erneut.

3. Führe die ausführbare Datei aus:
   ```
   ./example
   ```
   - Die Ausgabe hängt vom Inhalt von `example.rs` ab (z.B. "Hello, World!").

Wenn `example.rs` eine Bibliothek ist (keine `fn main()`), funktioniert dies nicht – verwende stattdessen `cargo test` in einem Projekt-Setup.

### Option 2: Als Cargo-Projekt einrichten und ausführen (Empfohlen für rust-analyzer und Skalierbarkeit)
Dies behebt den rust-analyzer-Fehler, indem ein gültiger Workspace erstellt wird. Es ermöglicht auch die Verwendung von `cargo run` für einfacheres Bauen und Ausführen.

1. Erstelle ein dediziertes Projektverzeichnis oder wechsle dorthin (um die Unordnung im GitHub Pages-Root zu vermeiden):
   ```
   mkdir rust_project
   cd rust_project
   ```
   - Wenn du darauf bestehst, das vorhandene `rust`-Verzeichnis zu verwenden, führe stattdessen `cd rust` aus und fahre fort.

2. Erstelle `Cargo.toml` mit deinem bereitgestellten Inhalt, korrigiere aber die Edition:
   ```
   [package]
   name = "example"
   version = "0.1.0"
   edition = "2024"  # Geändert von ungültig "2025"
   authors = ["lzwjava@gmail.com"]
   description = "A simple Rust example project"

   [dependencies]
   ```
   - Speichere dies als `Cargo.toml` im aktuellen Verzeichnis.

3. Richte das Quellverzeichnis ein und verschiebe deine Datei:
   ```
   mkdir src
   mv ../rust/example.rs src/main.rs  # Passe den Pfad bei Bedarf an; benennt es in main.rs für die Binärausführung um
   ```
   - Wenn `example.rs` nicht der Haupteinstiegspunkt sein soll, benenne es stattdessen in `lib.rs` um und füge `[lib]` zu `Cargo.toml` für eine Library-Crate hinzu.

4. Baue das Projekt:
   ```
   cargo build
   ```
   - Dies lädt alle benötigten Crates (hier keine) herunter und kompiliert. Schlägt es fehl, überprüfe `src/main.rs` auf Fehler.

5. Führe das Projekt aus:
   ```
   cargo run
   ```
   - Dies baut bei Bedarf und führt `src/main.rs` aus.

6. Um den rust-analyzer-Fehler in VS Code (oder einem ähnlichen Editor) zu beheben:
   - Öffne den `rust_project`-Ordner als deinen Workspace-Root (**Datei > Ordner öffnen**).
   - Lade das Fenster neu (**Cmd+Shift+P** > **Developer: Reload Window**).
   - rust-analyzer sollte das Projekt jetzt über `Cargo.toml` erkennen.

### Tipps zur Problembehebung
- **Wenn `cargo` nicht installiert ist**: Führe `rustup update` aus (angenommen, du hast Rust über rustup installiert). Falls nicht, installiere Rust von https://rustup.rs/.
- **Editionsfehler**: Wenn du "2025" beibehältst, wird Cargo sich beschweren: "error: invalid edition: '2025'". Bleibe bei "2024".
- **Keine `fn main()` in `example.rs`**: Füge eine hinzu, z.B.:
  ```
  fn main() {
      println!("Hello, World!");
  }
  ```
- **Abhängigkeiten benötigt?**: Füge sie unter `[dependencies]` in `Cargo.toml` hinzu, z.B. `rand = "0.8"`, dann `cargo build`.
- **rust-analyzer schlägt immer noch fehl?**: Stelle sicher, dass die Rust-Erweiterung deines Editors aktualisiert ist, und füge `"rust-analyzer.linkedProjects": ["./Cargo.toml"]` zur `settings.json` deines Workspaces hinzu, wenn sich das Projekt in einem Unterverzeichnis befindet.
- Für komplexere Setups (z.B. mehrere Crates) verwende `cargo new --bin example`, um eine Vorlage zu generieren.

Wenn dies nicht deinem Setup entspricht (z.B. teile den Inhalt von `example.rs` oder weitere Details mit), lass es mich für verfeinerte Schritte wissen.

[Announcing Rust 1.88.0](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/)  
[Rust | endoflife.date](https://endoflife.date/rust)