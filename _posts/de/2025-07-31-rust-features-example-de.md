---
audio: false
generated: true
image: false
lang: de
layout: post
title: Hauptmerkmale von Rust Beispiel
translated: true
type: note
---

Hier ist ein einfaches Rust-Codebeispiel, das mehrere wichtige Funktionen demonstriert, darunter Borrowing, Mutability, Ownership, Structs, Enums, Pattern Matching und mehr. Ich halte es knapp aber dennoch anschaulich, mit Kommentaren, die jede Funktion erklären.

```rust
// Definiere ein Struct zur Darstellung eines Point
struct Point {
    x: i32,
    y: i32,
}

// Definiere ein Enum für verschiedene Shapes
enum Shape {
    Circle(Point, f32), // Mittelpunkt und Radius
    Rectangle(Point, i32, i32), // Oberer linker Punkt, Breite, Höhe
}

// Implementiere Methoden für Point
impl Point {
    // Immutable Borrow zur Berechnung der Entfernung vom Ursprung
    fn distance_from_origin(&self) -> f32 {
        ((self.x.pow(2) + self.y.pow(2)) as f32).sqrt()
    }

    // Mutable Borrow zur Verschiebung des Punkts
    fn translate(&mut self, dx: i32, dy: i32) {
        self.x += dx;
        self.y += dy;
    }
}

// Funktion zur Demonstration von Ownership und Borrowing
fn describe_shape(shape: &Shape) -> String {
    match shape {
        Shape::Circle(center, radius) => {
            // Immutable Borrow von center
            format!(
                "Kreis bei ({}, {}) mit Radius {}",
                center.x, center.y, radius
            )
        }
        Shape::Rectangle(top_left, width, height) => {
            // Immutable Borrow von top_left
            format!(
                "Rechteck bei ({}, {}) mit Breite {}, Höhe {}",
                top_left.x, top_left.y, width, height
            )
        }
    }
}

fn main() {
    // Mutable Variable Binding
    let mut point = Point { x: 3, y: 4 };
    
    // Immutable Borrow zum Aufruf der Methode
    println!("Entfernung vom Ursprung: {}", point.distance_from_origin());
    
    // Mutable Borrow zur Modifikation des Punkts
    point.translate(2, 1);
    println!("Nach Verschiebung: ({}, {})", point.x, point.y);
    
    // Erstelle eine Shape (Ownership wird an Variable übergeben)
    let circle = Shape::Circle(point, 5.0);
    
    // Immutable Borrow der Shape zur Beschreibung
    println!("Shape: {}", describe_shape(&circle));
    
    // Vector mit Ownership der Elemente
    let mut shapes: Vec<Shape> = Vec::new();
    shapes.push(circle);
    shapes.push(Shape::Rectangle(Point { x: 0, y: 0 }, 10, 20));
    
    // Iteriere mit Immutable Borrow
    for shape in &shapes {
        println!("Shape im Vektor: {}", describe_shape(shape));
    }
    
    // Option und Pattern Matching
    let maybe_number: Option<i32> = Some(42);
    match maybe_number {
        Some(num) => println!("Erhielt eine Zahl: {}", num),
        None => println!("Keine Zahl"),
    }
    
    // Result für Fehlerbehandlung
    let result: Result<i32, &str> = Ok(100);
    if let Ok(value) = result {
        println!("Result Wert: {}", value);
    }
}
```

### Demonstrierte Hauptfunktionen:
1. **Structs**: `Point` Struct zur Darstellung eines 2D-Punkts.
2. **Enums**: `Shape` Enum zur Darstellung verschiedener Shapes (Circle, Rectangle).
3. **Ownership**: Die Variable `circle` übernimmt Ownership von `point` bei der Erstellung.
4. **Borrowing**:
   - Immutable Borrow (`&self`) in `distance_from_origin`.
   - Mutable Borrow (`&mut self`) in `translate`.
   - Immutable Borrow (`&Shape`) in `describe_shape`.
5. **Mutability**: `mut` Schlüsselwort für mutable Variablen (`point`, `shapes`).
6. **Pattern Matching**: Verwendet mit `match` in `describe_shape` und für `Option`.
7. **Methods**: Definiert im `impl Point` Block.
8. **Vectors**: `Vec<Shape>` zum Speichern einer Sammlung von Shapes.
9. **Option**: Behandlung optionaler Werte mit `Some` und `None`.
10. **Result**: Grundlegende Fehlerbehandlung mit `Ok` und `Err`.
11. **String Formatting**: Verwendung von `format!` für dynamische Strings.

### Ausgabe (bei Ausführung):
```
Entfernung vom Ursprung: 5
Nach Verschiebung: (5, 5)
Shape: Kreis bei (5, 5) mit Radius 5
Shape im Vektor: Kreis bei (5, 5) mit Radius 5
Shape im Vektor: Rechteck bei (0, 0) mit Breite 10, Höhe 20
Erhielt eine Zahl: 42
Result Wert: 100
```

Dieser Code ist knapp, zeigt aber Rusts Kernkonzepte wie Ownership, Borrowing und Mutability, zusammen mit seinem Typsystem und Fehlerbehandlung. Sie können ihn mit `rustc` oder einem Rust-Projekt mit `cargo run` ausführen. Lassen Sie mich wissen, wenn Sie eine tiefergehende Erklärung zu einer bestimmten Funktion wünschen!