---
audio: false
generated: true
image: false
lang: de
layout: post
title: Rust-Programm aus Verzeichnis ausführen
translated: true
type: note
---

Um ein einfaches Rust-Programm aus der von Ihnen bereitgestellten Verzeichnisstruktur auszuführen, sieht es so aus, als würden Sie in einem Rust-Projekt (`lzwjava.github.io/rust`) arbeiten, mit einem `src`-Ordner, der `main.rs` und `simple.rs` enthält. So können Sie ein einfaches Rust-Programm ausführen, unter der Annahme, dass Sie den Code in `main.rs` oder `simple.rs` ausführen möchten.

### Schritte zum Ausführen eines Rust-Programms

1.  **Überprüfen Sie die Projektstruktur**:
    - Ihr Projekt verfügt über eine `Cargo.toml`-Datei, was darauf hindeutet, dass es sich um ein von Cargo, dem Build-Tool von Rust, verwaltetes Projekt handelt.
    - Die Datei `src/main.rs` ist der standardmäßige Einstiegspunkt für eine Rust-Binäranwendung.
    - Die Datei `simple.rs` ist wahrscheinlich ein Modul oder eine andere Quelldatei, wird aber nicht direkt ausgeführt, es sei denn, sie wird in `main.rs` referenziert oder in `Cargo.toml` als Binärdatei konfiguriert.

2.  **Führen Sie das Programm mit Cargo aus**:
    - Wenn Sie den Code in `src/main.rs` ausführen möchten, verwenden Sie den folgenden Befehl aus dem Projektstammverzeichnis (`~/projects/lzwjava.github.io/rust`):
      ```bash
      cargo run
      ```
      Dieser Befehl:
      - Kompiliert das Projekt (löst Abhängigkeiten auf und baut den Code).
      - Führt die aus `src/main.rs` generierte Binärdatei aus.
      - Die Ausgabe erscheint im Terminal.

3.  **Wenn Sie `simple.rs` ausführen möchten**:
    - Standardmäßig erwartet Cargo, dass der Haupteinstiegspunkt `src/main.rs` ist. Wenn `simple.rs` ein Modul ist, müssen Sie es in `main.rs` referenzieren. Zum Beispiel in `src/main.rs`:
      ```rust
      mod simple; // Deklariert das simple-Modul

      fn main() {
          simple::some_function(); // Ruft eine Funktion aus simple.rs auf
      }
      ```
      Führen Sie dann wie oben `cargo run` aus.
    - Wenn `simple.rs` eine eigenständige Binärdatei sein soll, müssen Sie sie in `Cargo.toml` konfigurieren. Fügen Sie Folgendes zur `Cargo.toml` hinzu:
      ```toml
      [[bin]]
      name = "simple"
      path = "src/simple.rs"
      ```
      Führen Sie dann aus:
      ```bash
      cargo run --bin simple
      ```

4.  **Alternative: Ausführung ohne Cargo**:
    - Wenn Sie eine einzelne Datei (z.B. `simple.rs`) ohne Cargo kompilieren und ausführen möchten, stellen Sie sicher, dass sie eine `main`-Funktion hat, und verwenden Sie den `rustc`-Compiler:
      ```bash
      rustc src/simple.rs
      ./simple
      ```
      Dies erzeugt eine ausführbare Datei namens `simple` im aktuellen Verzeichnis und führt sie aus. Hinweis: Dieser Ansatz behandelt keine Abhängigkeiten und ist daher nur für einfache, in sich geschlossene Programme geeignet.

5.  **Überprüfen Sie auf Fehler**:
    - Wenn Sie auf Fehler stoßen, stellen Sie sicher:
      - Rust und Cargo sind installiert (überprüfen Sie mit `rustc --version` und `cargo --version`).
      - `Cargo.toml` ist korrekt mit den notwendigen Abhängigkeiten konfiguriert.
      - Der Code in `main.rs` oder `simple.rs` hat eine gültige `fn main()`-Funktion.
    - Führen Sie `cargo check` aus, um den Code zu überprüfen, ohne die Binärdatei zu erstellen:
      ```bash
      cargo check
      ```

6.  **Beispiel `simple.rs`**:
    Wenn `simple.rs` etwa Folgendes enthält:
    ```rust
    fn main() {
        println!("Hello from simple!");
    }
    ```
    Und Sie sie als Binärdatei in `Cargo.toml` hinzugefügt haben, gibt `cargo run --bin simple` `Hello from simple!` aus.

### Hinweise
- Das Verzeichnis `target/debug` enthält kompilierte Artefakte. Sie können die Binärdatei direkt mit `./target/debug/<project_name>` ausführen (ersetzen Sie `<project_name>` durch den Namen in `Cargo.toml`), aber `cargo run` wird bevorzugt, da es Kompilierung und Ausführung handhabt.
- Wenn `simple.rs` ein Modul ist, stellen Sie sicher, dass es korrekt mit `mod simple;` in `main.rs` integriert ist.
- Für komplexere Setups oder spezifischen Code in `simple.rs` teilen Sie bitte die Inhalte von `simple.rs` oder `Cargo.toml` mit, um eine maßgeschneiderte Anleitung zu erhalten.

Wenn Sie mit "run simple here" etwas Bestimmtes gemeint haben (z.B. eine bestimmte Funktion oder Konfiguration), geben Sie bitte mehr Details an, und ich werde die Antwort verfeinern!