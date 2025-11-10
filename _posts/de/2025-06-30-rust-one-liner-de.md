---
audio: false
generated: true
lang: de
layout: post
title: Einzeiler in Rust mit Shell-Chaining
translated: true
type: note
---

Du sprichst einen häufigen Wunsch von erfahrenen Entwicklern an, die von Sprachen wie Python, Ruby oder JavaScript kommen, wo man oft einen einzelnen Befehl hat, um ein Skript direkt auszuführen. Rust, als kompilierte Sprache, hat standardmäßig einen etwas anderen Workflow.

Du kannst jedoch definitiv ein "One-Liner"-Gefühl erreichen, besonders für einfache Skripte oder Übungen, indem du Befehle in deiner Shell verkettest.

### Der direkte "One-Liner" (Shell-Verkettung)

Du hast bereits die Komponenten: `rustc` zur Kompilierung und `./` zur Ausführung. Du kannst sie mit Shell-Operatoren kombinieren:

```bash
rustc scripts/rust/example.rs -o test/example && ./test/example
```

**Erklärung:**

  * `rustc scripts/rust/example.rs -o test/example`: Dies kompiliert deine Rust-Datei und platziert die ausführbare Datei unter `test/example`.
  * `&&`: Dies ist ein **bedingter Befehlsseparator** in bash (und den meisten Unix-ähnlichen Shells). Der Befehl *nach* `&&` wird nur ausgeführt, wenn der Befehl *vor* `&&` erfolgreich abgeschlossen wird (d.h. einen Exit-Code von 0 zurückgibt).
      * Wenn `rustc` ohne Fehler kompiliert, gibt es 0 zurück, und dann wird `./test/example` ausgeführt.
      * Wenn `rustc` einen Kompilierungsfehler findet, gibt es einen Exit-Code ungleich Null zurück, und `./test/example` wird *nicht* ausgeführt. Das ist ein gutes Verhalten\!

### Für eine mehr "skript-ähnliche" Erfahrung (Cargo)

Während der oben genannte `&&`-Ansatz für schnelle Tests gut funktioniert, ist für alles, was über triviale Einzeldatei-Skripte hinausgeht, Rusts `cargo`-Tool der empfohlene Weg, und es bietet *tatsächlich* einen Python-ähnlichen One-Liner für die Ausführung von Code innerhalb eines Projekts:

1.  **Initialisiere ein Cargo-Projekt (falls noch nicht geschehen):**
    Wenn deine `scripts/rust/example.rs` nur eine eigenständige Datei ist, würdest du typischerweise damit beginnen, ein Cargo-Projekt in ihrem übergeordneten Verzeichnis (oder einem neuen, dedizierten Verzeichnis) zu erstellen.

    ```bash
    # Wechsle in das Verzeichnis, in dem dein Projekt sein soll (z.B. scripts/rust)
    cd scripts/rust

    # Initialisiere ein neues Cargo-Binärprojekt
    cargo init --bin .
    ```

    Dies erstellt `Cargo.toml` und verschiebt deine `example.rs` (wenn sie `main.rs` war) oder passt die `Cargo.toml` an, um auf sie zu verweisen (wenn du `example.rs` in `src/` in `main.rs` umbenennst).

2.  **Ausführung mit Cargo:**
    Sobald du ein Cargo-Projekt eingerichtet hast, kannst du mit einem einzigen Befehl kompilieren und ausführen:

    ```bash
    # Von deinem Projektstammverzeichnis aus (z.B. scripts/rust, wenn du dort cargo init ausgeführt hast)
    cargo run
    ```

    `cargo run` wird:

      * Deinen Code kompilieren (falls er noch nicht kompiliert wurde oder Änderungen vorgenommen wurden).
      * Dann die resultierende Binärdatei ausführen.
      * Standardmäßig wird die Binärdatei in `target/debug/` innerhalb deines Projekts platziert, aber du musst dich nicht um ihren spezifischen Pfad kümmern.

**Warum Cargo bevorzugt wird:**

  * **Abhängigkeitsverwaltung:** Falls dein Code jemals externe Bibliotheken (Crates) benötigt, erledigt Cargo das Abrufen, Kompilieren und Verlinken automatisch. Du gibst sie in `Cargo.toml` an.
  * **Standard-Projektstruktur:** Es fördert ein konsistentes Layout (`src/main.rs`, `Cargo.toml`), was deinen Code für andere (und dein zukünftiges Ich) leichter verständlich macht.
  * **Testing:** `cargo test` führt deine Unit- und Integrationstests aus.
  * **Release-Builds:** `cargo run --release` (oder `cargo build --release`) kompiliert mit Optimierungen für die Produktion.
  * **Keine manuelle Bereinigung:** Du musst kompilierte Binärdateien nicht manuell löschen. `cargo clean` erledigt das.

### Was ist mit einem echten "Skripting"-Ansatz wie Pythons `python skript.py`?

Rust ist nicht als interpretierte Skriptsprache konzipiert. Es ist eine kompilierte Systemsprache. Daher wirst du keinen direkten `rust skript.rs`-Befehl erhalten, der kompiliert und ausführt, ohne einen expliziten Kompilierungsschritt.

Es gibt jedoch Community-Tools, die versuchen, diese Lücke für schnelle, einzelne Rust-"Skripte" zu schließen (obwohl sie immer noch im Hintergrund kompilieren):

  * **`cargo-script`**: Ein Cargo-Subcommand, das es dir ermöglicht, einzelne `.rs`-Dateien auszuführen und Abhängigkeiten zu verwalten, falls sie über Kommentare angegeben sind. Du würdest es typischerweise mit `cargo install cargo-script` installieren. Dann könntest du potenziell `cargo script scripts/rust/example.rs` ausführen.
  * **`rust-script`**: Ein weiteres beliebtes Tool zum direkten Ausführen von Rust-Dateien wie Skripten. Installiere es via `cargo install rust-script`. Dann kannst du oft einfach deine `.rs`-Datei ausführbar machen (`chmod +x example.rs`) und sie ausführen: `./example.rs`. Es erledigt die Kompilierung und Ausführung im Hintergrund.

Für deinen Anwendungsfall, `example.rs` schnell zu testen, ist der `rustc ... && ./...`-One-Liner völlig in Ordnung und beantwortet direkt deine Frage zur Verkettung der beiden Befehle. Für jede nicht-triviale Entwicklung wird die Verwendung von Cargo eine produktivere und idiomatischere Rust-Erfahrung sein.