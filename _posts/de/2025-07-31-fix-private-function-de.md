---
audio: false
generated: true
image: false
lang: de
layout: post
title: Beheben von Fehlern in privaten Funktionen
translated: true
type: note
---

Der Fehler `E0603: function run_simple is private` zeigt an, dass die Funktion `run_simple` in `simple.rs` privat ist (es fehlt das `pub` Schlüsselwort), sodass sie nicht von `main.rs` aus aufgerufen werden kann. In Rust sind Funktionen standardmäßig privat und müssen explizit mit `pub` als öffentlich gekennzeichnet werden, um sie außerhalb ihres Moduls nutzen zu können.

### Schritte zur Fehlerbehebung

1. **Mache `run_simple` öffentlich**:
   - Öffne `src/simple.rs`.
   - Füge das `pub` Schlüsselwort zur Funktion `run_simple` hinzu, um sie öffentlich zugänglich zu machen.
   - Beispiel:
     ```rust
     pub fn run_simple() {
         // Bestehender Funktionsrumpf
         println!("Hello from run_simple!");
     }
     ```

2. **Stelle die korrekte Moduldeklaration sicher**:
   - Stelle in `src/main.rs` sicher, dass du das `simple` Modul korrekt deklariert hast:
     ```rust
     mod simple; // Deklariert das simple Modul

     fn main() {
         simple::run_simple(); // Ruft die öffentliche Funktion auf
     }
     ```

3. **Projekt neu erstellen und ausführen**:
   - Nachdem die Funktion öffentlich gemacht wurde, erstelle das Projekt neu:
     ```bash
     cargo build
     ```
   - Wenn der Build erfolgreich ist, führe das Programm aus:
     ```bash
     cargo run
     ```

4. **Prüfe auf andere Probleme**:
   - Der Fehler erwähnt `src/simple.rs:47:1`, also überprüfe, ob die Funktion `run_simple` in dieser Zeile korrekt definiert ist und keine anderen Probleme aufweist (z.B. Syntaxfehler oder fehlende Abhängigkeiten).
   - Wenn `simple.rs` externe Crates verwendet, stelle sicher, dass diese in `Cargo.toml` unter `[dependencies]` aufgelistet sind.

5. **Cargo Warnung**:
   - Die Warnung bezüglich `edition2024` deutet darauf hin, dass du ein Feature-Flag in `Cargo.toml` verwendest, das nicht mehr benötigt wird, da Rust 1.85 die 2024 Edition stabilisiert hat. Um dies zu bereinigen, öffne `Cargo.toml` und entferne das `edition2024` Feature, falls vorhanden (z.B. unter `[features]` oder `cargo-features`). Setze die Edition stattdessen direkt:
     ```toml
     [package]
     name = "example"
     version = "0.1.0"
     edition = "2024"
     ```
   - Dies stellt sicher, dass dein Projekt die 2024 Edition ohne das veraltete Feature-Flag verwendet.

### Beispiel-Dateien

Zur Verdeutlichung, so sollten deine Dateien aussehen:

**`src/simple.rs`**:
```rust
pub fn run_simple() {
    println!("Hello from run_simple!");
}
```

**`src/main.rs`**:
```rust
mod simple;

fn main() {
    simple::run_simple();
}
```

**`Cargo.toml`** (minimales Beispiel):
```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"
```

### Zusätzliche Hinweise
- Wenn `run_simple` von anderem Code oder Modulen abhängt, stelle sicher, dass diese ebenfalls öffentlich sind, wenn sie von `main.rs` aus aufgerufen werden.
- Wenn der Fehler weiterhin besteht, teile die Inhalte von `src/simple.rs` (insbesondere um Zeile 47) und `src/main.rs` für spezifischere Hilfe.
- Der Befehl `rustc --explain E0603` bietet eine detaillierte Dokumentation zu diesem Fehler, den du für weitere Einblicke ausführen kannst.
- Das Verzeichnis `target/debug` enthält die kompilierte Binärdatei (`example`) nach einem erfolgreichen Build.

Versuche diese Schritte und lass mich wissen, wenn weitere Probleme auftreten!