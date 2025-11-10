---
audio: false
generated: true
lang: de
layout: post
title: Rust Ausgabeort Optionen
translated: true
type: note
---

Das ist eine ausgezeichnete Frage, die berührt, wie Rust-Projekte typischerweise strukturiert und gebaut werden!

Wenn du `rustc` direkt verwendest, hast du zwei Hauptoptionen, um den Ausgabeort festzulegen:

1.  **`-o <output_filename>`**: Diese Option legt den *exakten Pfad und Dateinamen* für die kompilierte ausführbare Datei oder Bibliothek fest.

    ```bash
    rustc scripts/rust/example.rs -o test/example
    ```

    Dies kompiliert `example.rs` und platziert die ausführbare Datei namens `example` direkt in das `test/` Verzeichnis. Falls `test/` nicht existiert, wird `rustc` es erstellen.

2.  **`--out-dir <output_directory>`**: Diese Option legt ein *Verzeichnis* fest, in das `rustc` alle generierten Ausgabedateien platziert (die ausführbare Datei/Bibliothek, zusammen mit eventuellen Zwischendateien wie `.d`, `.rmeta`, etc.).

    ```bash
    rustc scripts/rust/example.rs --out-dir test/
    ```

    In diesem Fall kompiliert `rustc` `example.rs` und platziert die ausführbare Datei (die standardmäßig den Namen `example` hat, abgeleitet vom Quelltext-Dateinamen) in das `test/` Verzeichnis.

**Empfehlung: Verwende Cargo für Projekte**

Während `rustc` dir direkte, feingranulare Kontrolle gibt, wirst du für die meisten Rust-Projekte **Cargo** verwenden wollen. Cargo ist Rusts Build-System und Paketmanager und vereinfacht das Verwalten von Abhängigkeiten, das Bauen, Testen und Ausführen deines Codes.

Mit Cargo werden die kompilierten Binärdateien typischerweise in ein `target` Verzeichnis innerhalb deines Projektstammverzeichnisses platziert. Wenn du zum Beispiel ein Projekt mit Cargo hast:

```
my_project/
├── Cargo.toml
└── src/
    └── main.rs
```

Wenn du `cargo build` oder `cargo run` ausführst, wird die kompilierte ausführbare Datei unter `my_project/target/debug/my_project` (für Debug-Builds) oder `my_project/target/release/my_project` (für Release-Builds) platziert.

Wenn du das `target` Verzeichnis für Cargo steuern möchtest, kannst du:

  * **`CARGO_TARGET_DIR` Umgebungsvariable** verwenden:

    ```bash
    CARGO_TARGET_DIR=./test cargo build
    ```

    Dies platziert das gesamte `target` Verzeichnis (welches `debug`, `release`, etc. enthält) in dein `test/` Verzeichnis. Die ausführbare Datei wäre dann unter `test/debug/my_project`.

  * **Die `--target-dir` Kommandozeilenoption für Cargo** verwenden:

    ```bash
    cargo build --target-dir test/
    ```

    Dies bewirkt das Gleiche wie die Umgebungsvariable.

  * **`.cargo/config.toml`**: Du kannst ein standardmäßiges `target-dir` für alle Cargo-Projekte auf deinem Rechner oder für einen spezifischen Workspace festlegen, indem du es in einer `.cargo/config.toml` Datei hinzufügst.

**Warum Cargo verwenden?**

  * **Standardisiertes Projektlayout:** Cargo erzwingt eine gemeinsame Projektstruktur, was es für andere Rust-Entwickler einfach macht, deinen Code zu verstehen.
  * **Abhängigkeitsverwaltung:** Cargo übernimmt das automatische Herunterladen und Kompilieren der Abhängigkeiten deines Projekts.
  * **Testen und Benchmarking:** Cargo hat integrierte Befehle zum Ausführen von Tests (`cargo test`) und Benchmarks (`cargo bench`).
  * **Release-Management:** Cargo hilft beim Erstellen von Release-Builds (`cargo build --release`) und beim Veröffentlichen von Crates auf crates.io.

Es ist sehr empfohlen, deinen Rust-Code in einem Cargo-Projekt zu organisieren, es sei denn, du hast einen sehr spezifischen Grund, dies nicht zu tun.

**Basierend auf deiner `git status` Ausgabe:**

Dein `git status` zeigt `example` und `scripts/rust/` als unversioniert an. Dies deutet darauf hin, dass du `scripts/rust/example.rs` möglicherweise direkt mit `rustc` außerhalb eines Cargo-Projekts kompilierst.

Wenn `example` die kompilierte Binärdatei ist, dann hat der vorherige `rustc scripts/rust/example.rs` Befehl sie im aktuellen Verzeichnis (`lzwjava.github.io`) platziert.

Um dein Ziel, sie in `test/example` zu platzieren (angenommen `test` ist ein Verzeichnis im Stammverzeichnis von `lzwjava.github.io`), zu erreichen, würdest du verwenden:

```bash
rustc scripts/rust/example.rs -o test/example
```

Dies ist der direkteste Weg, um den von dir gewünschten spezifischen Ausgabepfad mit `rustc` zu erhalten.