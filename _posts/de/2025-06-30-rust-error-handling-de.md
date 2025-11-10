---
audio: false
generated: true
lang: de
layout: post
title: Fehlerbehandlung in Rust ohne Exceptions
translated: true
type: note
---

Rust hat **keine** Exceptions im traditionellen Sinne, wie Java oder C\#. Stattdessen behandelt es Fehler hauptsächlich über **Rückgabewerte**, ähnlich wie Go's `if err != nil` Muster, aber mit einem robusteren und typsicheren Ansatz.

Hier ist eine Aufschlüsselung, wie Rust mit Fehlern umgeht:

**1. `Result<T, E>` Enum für Behebbare Fehler:**

Dies ist die gebräuchlichste und idiomatische Art, Fehler in Rust zu behandeln.

  * `Result<T, E>` ist eine Enum mit zwei Varianten:
      * `Ok(T)`: Repräsentiert Erfolg und enthält den erfolgreichen Wert vom Typ `T`.
      * `Err(E)`: Repräsentiert einen Fehler und enthält einen Fehlerwert vom Typ `E`.
  * Wenn eine Funktion fehlschlagen könnte, gibt sie ein `Result` zurück. Dies zwingt den Aufrufer explizit, sowohl den Erfolgs- (`Ok`) als auch den Fehlerfall (`Err`) zu behandeln.
  * Man verwendet `match`-Ausdrücke oder verschiedene Hilfsmethoden (wie `map`, `and_then`, `unwrap_or`, `unwrap_or_else`, etc.), um die `Ok`- und `Err`-Varianten zu behandeln.

**Beispiel:**

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problem beim Erstellen der Datei: {:?}", e),
            },
            other_error => panic!("Problem beim Öffnen der Datei: {:?}", other_error),
        },
    };

    println!("Datei erfolgreich geöffnet oder erstellt: {:?}", greeting_file);
}
```

**2. `Option<T>` Enum für Optionale Werte:**

Während nicht streng genommen für "Fehler", ist `Option<T>` ähnlich zu `Result`, da es die *Möglichkeit der Abwesenheit* repräsentiert.

  * `Option<T>` hat zwei Varianten:
      * `Some(T)`: Der Wert ist vorhanden.
      * `None`: Der Wert ist nicht vorhanden.
  * Dies wird verwendet, wenn eine Funktion möglicherweise legitimerweise keinen Wert zurückgibt (z.B. das Finden eines Elements in einer Liste, das nicht existiert).

**3. Der `?` Operator (Fragezeichen-Operator):**

Dies ist eine mächtige syntaktische Vereinfachung, die die Weitergabe von Fehlern viel kompakter macht, ähnlich wie `if err != nil { return err }` in Go üblich ist.

  * Wenn ein `Result`-Wert `Ok` ist, entpackt der `?`-Operator den `Ok`-Wert und die Ausführung wird fortgesetzt.
  * Wenn ein `Result`-Wert `Err` ist, gibt der `?`-Operator sofort den `Err`-Wert aus der aktuellen Funktion zurück.
  * Die Funktion, die `?` verwendet, muss selbst ein `Result` (oder `Option`, wenn sie eine `Option` entpackt) zurückgeben.

**Beispiel mit `?`:**

```rust
use std::fs::File;
use std::io::{self, Read}; // io::Read-Trait importieren

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?; // Gibt Fehler weiter, wenn Datei nicht existiert
    let mut username = String::new();
    username_file.read_to_string(&mut username)?; // Gibt Fehler weiter, wenn Lesen fehlschlägt
    Ok(username)
}

fn main() {
    match read_username_from_file() {
        Ok(username) => println!("Benutzername: {}", username),
        Err(e) => println!("Fehler beim Lesen des Benutzernamens: {}", e),
    }
}
```

**4. `panic!` Makro für Unbehebbare Fehler:**

`panic!` wird für unbehebbare Fehler verwendet, die typischerweise auf einen Bug im Programm hindeuten (z.B. Zugriff auf ein Array außerhalb seiner Grenzen).

  * Wenn `panic!` aufgerufen wird, wird das Programm beendet (oder "entrollt" den Stack, abhängig von der Konfiguration).
  * Es ist generell für behebbare Fehler, die das Programm elegant behandeln sollte, nicht zu empfehlen.

**Wichtige Unterschiede zu Traditionellen Exceptions:**

  * **Explizitheit:** Rusts Fehlerbehandlung ist hochgradig explizit. Die Funktionssignatur zeigt klar an, dass sie einen Fehler zurückgeben kann, und der Compiler *zwingt* Sie, ihn zu behandeln. Sie können einen Fehler nicht versehentlich ignorieren.
  * **Keine "Catch-all"-Blöcke:** Es gibt keine `try-catch`-Blöcke, die stillschweigend jede Exception abfangen. Sie behandeln spezifische Fehlertypen.
  * **Typsicherheit:** Fehler sind Werte spezifischer Typen (`Result<T, E>`), was eine präzise Fehlerbehandlung ermöglicht und die Mehrdeutigkeit generischer Exception-Typen vermeidet.
  * **Performance:** Das Zurückgeben von `Result`-Werten ist im Allgemeinen performanter als das Werfen und Fangen von Exceptions, da Exceptions oft erheblichen Overhead mit sich bringen (Stack-Unwinding, etc.). Rust ist für leistungskritische Anwendungen konzipiert.

Zusammenfassend lässt sich sagen, dass Rusts Fehlerbehandlungsmodell viel näher an der "Check in every level"-Philosophie von Go liegt als an den Exceptions von Java oder C\#. Mit der `Result`-Enum und dem `?`-Operator bietet Rust jedoch mächtige und ergonomische Werkzeuge, um diese explizite Fehlerbehandlung handhabbar und sogar angenehm zu gestalten.