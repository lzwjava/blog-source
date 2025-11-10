---
audio: false
generated: true
image: false
lang: es
layout: post
title: Ejemplo de las Características Principales de Rust
translated: true
type: note
---

Aquí tienes un ejemplo simple de código en Rust que demuestra varias características clave, incluyendo borrowing, mutabilidad, ownership, structs, enums, pattern matching y más. Lo mantendré conciso pero ilustrativo, con comentarios que explican cada característica.

```rust
// Define un struct para representar un Point
struct Point {
    x: i32,
    y: i32,
}

// Define un enum para diferentes shapes
enum Shape {
    Circle(Point, f32), // Punto central y radio
    Rectangle(Point, i32, i32), // Punto superior izquierdo, ancho, alto
}

// Implementa métodos para Point
impl Point {
    // Immutable borrow para calcular distancia desde el origen
    fn distance_from_origin(&self) -> f32 {
        ((self.x.pow(2) + self.y.pow(2)) as f32).sqrt()
    }

    // Mutable borrow para trasladar el punto
    fn translate(&mut self, dx: i32, dy: i32) {
        self.x += dx;
        self.y += dy;
    }
}

// Función que demuestra ownership y borrowing
fn describe_shape(shape: &Shape) -> String {
    match shape {
        Shape::Circle(center, radius) => {
            // Immutable borrow del centro
            format!(
                "Circle en ({}, {}) con radio {}",
                center.x, center.y, radius
            )
        }
        Shape::Rectangle(top_left, width, height) => {
            // Immutable borrow de top_left
            format!(
                "Rectangle en ({}, {}) con ancho {}, alto {}",
                top_left.x, top_left.y, width, height
            )
        }
    }
}

fn main() {
    // Enlace de variable mutable
    let mut point = Point { x: 3, y: 4 };
    
    // Immutable borrow para llamar al método
    println!("Distancia desde el origen: {}", point.distance_from_origin());
    
    // Mutable borrow para modificar el punto
    point.translate(2, 1);
    println!("Después de la traducción: ({}, {})", point.x, point.y);
    
    // Crea un shape (ownership transferido a la variable)
    let circle = Shape::Circle(point, 5.0);
    
    // Immutable borrow del shape para describirlo
    println!("Shape: {}", describe_shape(&circle));
    
    // Vector con ownership de elementos
    let mut shapes: Vec<Shape> = Vec::new();
    shapes.push(circle);
    shapes.push(Shape::Rectangle(Point { x: 0, y: 0 }, 10, 20));
    
    // Itera con immutable borrow
    for shape in &shapes {
        println!("Shape en vec: {}", describe_shape(shape));
    }
    
    // Option y pattern matching
    let maybe_number: Option<i32> = Some(42);
    match maybe_number {
        Some(num) => println!("Obtuve un número: {}", num),
        None => println!("No hay número"),
    }
    
    // Result para manejo de errores
    let result: Result<i32, &str> = Ok(100);
    if let Ok(value) = result {
        println!("Valor del resultado: {}", value);
    }
}
```

### Características Clave Demostradas:
1. **Structs**: Struct `Point` para representar un punto 2D.
2. **Enums**: Enum `Shape` para representar diferentes shapes (Circle, Rectangle).
3. **Ownership**: La variable `circle` toma ownership de `point` cuando se crea.
4. **Borrowing**:
   - Immutable borrow (`&self`) en `distance_from_origin`.
   - Mutable borrow (`&mut self`) en `translate`.
   - Immutable borrow (`&Shape`) en `describe_shape`.
5. **Mutabilidad**: Palabra clave `mut` para variables mutables (`point`, `shapes`).
6. **Pattern Matching**: Usado con `match` en `describe_shape` y para `Option`.
7. **Métodos**: Definidos en el bloque `impl Point`.
8. **Vectores**: `Vec<Shape>` para almacenar una colección de shapes.
9. **Option**: Manejo de valores opcionales con `Some` y `None`.
10. **Result**: Manejo básico de errores con `Ok` y `Err`.
11. **Formateo de Strings**: Usando `format!` para strings dinámicos.

### Salida (cuando se ejecuta):
```
Distancia desde el origen: 5
Después de la traducción: (5, 5)
Shape: Circle en (5, 5) con radio 5
Shape en vec: Circle en (5, 5) con radio 5
Shape en vec: Rectangle en (0, 0) con ancho 10, alto 20
Obtuve un número: 42
Valor del resultado: 100
```

Este código es conciso pero muestra los conceptos centrales de Rust como ownership, borrowing y mutabilidad, junto con su sistema de tipos y manejo de errores. Puedes ejecutarlo usando `rustc` o un proyecto de Rust con `cargo run`. ¡Avísame si te gustaría una explicación más profunda de alguna característica específica!