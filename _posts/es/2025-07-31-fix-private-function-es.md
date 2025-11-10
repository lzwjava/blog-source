---
audio: false
generated: true
image: false
lang: es
layout: post
title: Corrección de Error de Función Privada
translated: true
type: note
---

El error `E0603: function run_simple is private` indica que la función `run_simple` en `simple.rs` es privada (le falta la palabra clave `pub`), por lo que no se puede acceder a ella desde `main.rs`. En Rust, las funciones son privadas por defecto y necesitan hacerse explícitamente públicas con `pub` para ser accesibles fuera de su módulo.

### Pasos para Corregir el Error

1. **Hacer Pública la Función `run_simple`**:
   - Abre `src/simple.rs`.
   - Añade la palabra clave `pub` a la función `run_simple` para hacerla accesible públicamente.
   - Ejemplo:
     ```rust
     pub fn run_simple() {
         // Cuerpo existente de la función
         println!("Hello from run_simple!");
     }
     ```

2. **Asegurar una Declaración Correcta del Módulo**:
   - En `src/main.rs`, asegúrate de haber declarado el módulo `simple` correctamente:
     ```rust
     mod simple; // Declara el módulo simple

     fn main() {
         simple::run_simple(); // Llama a la función pública
     }
     ```

3. **Recompilar y Ejecutar**:
   - Después de hacer pública la función, recompila el proyecto:
     ```bash
     cargo build
     ```
   - Si la compilación tiene éxito, ejecuta el programa:
     ```bash
     cargo run
     ```

4. **Verificar Otros Problemas**:
   - El error menciona `src/simple.rs:47:1`, así que verifica que la función `run_simple` en esa línea esté correctamente definida y no tenga otros problemas (por ejemplo, errores de sintaxis o dependencias faltantes).
   - Si `simple.rs` usa crates externos, asegúrate de que estén listados en `Cargo.toml` bajo `[dependencies]`.

5. **Advertencia de Cargo**:
   - La advertencia sobre `edition2024` sugiere que estás usando un feature flag en `Cargo.toml` que ya no es necesario, ya que Rust 1.85 estabilizó la edición 2024. Para limpiar esto, abre `Cargo.toml` y elimina el feature `edition2024` si está presente (por ejemplo, bajo `[features]` o `cargo-features`). En su lugar, establece la edición directamente:
     ```toml
     [package]
     name = "example"
     version = "0.1.0"
     edition = "2024"
     ```
   - Esto asegura que tu proyecto use la edición 2024 sin el feature flag obsoleto.

### Archivos de Ejemplo

Para aclarar, así es como deberían verse tus archivos:

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

**`Cargo.toml`** (ejemplo mínimo):
```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"
```

### Notas Adicionales
- Si `run_simple` depende de otro código o módulos, asegúrate de que esos también sean públicos si se accede a ellos desde `main.rs`.
- Si el error persiste, comparte el contenido de `src/simple.rs` (especialmente alrededor de la línea 47) y `src/main.rs` para una guía más específica.
- El comando `rustc --explain E0603` proporciona documentación detallada sobre este error, que puedes ejecutar para obtener más información.
- El directorio `target/debug` contendrá el binario compilado (`example`) después de una compilación exitosa.

¡Prueba estos pasos y avísame si encuentras más problemas!