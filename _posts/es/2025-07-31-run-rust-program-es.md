---
audio: false
generated: true
image: false
lang: es
layout: post
title: Ejecutar un programa Rust desde un directorio
translated: true
type: note
---

Para ejecutar un programa simple de Rust desde la estructura de directorios que proporcionaste, parece que estás trabajando en un proyecto de Rust (`lzwjava.github.io/rust`) con una carpeta `src` que contiene `main.rs` y `simple.rs`. Aquí te explicamos cómo ejecutar un programa simple de Rust, asumiendo que quieres ejecutar el código en `main.rs` o `simple.rs`.

### Pasos para ejecutar un programa de Rust

1. **Verificar la estructura del proyecto**:
   - Tu proyecto tiene un archivo `Cargo.toml`, lo que indica que es un proyecto de Rust gestionado por Cargo, la herramienta de compilación de Rust.
   - El archivo `src/main.rs` es el punto de entrada predeterminado para una aplicación binaria de Rust.
   - El archivo `simple.rs` probablemente sea un módulo u otro archivo fuente, pero no se ejecutará directamente a menos que esté referenciado en `main.rs` o configurado como un binario en `Cargo.toml`.

2. **Ejecutar el programa usando Cargo**:
   - Si quieres ejecutar el código en `src/main.rs`, usa el siguiente comando desde la raíz del proyecto (`~/projects/lzwjava.github.io/rust`):
     ```bash
     cargo run
     ```
     Este comando:
     - Compila el proyecto (resolviendo dependencias y construyendo el código).
     - Ejecuta el binario generado desde `src/main.rs`.
     - La salida aparecerá en la terminal.

3. **Si quieres ejecutar `simple.rs`**:
   - Por defecto, Cargo espera que el punto de entrada principal sea `src/main.rs`. Si `simple.rs` es un módulo, necesitas referenciarlo en `main.rs`. Por ejemplo, en `src/main.rs`:
     ```rust
     mod simple; // Declara el módulo simple

     fn main() {
         simple::some_function(); // Llama a una función desde simple.rs
     }
     ```
     Luego ejecuta `cargo run` como se indicó arriba.
   - Si `simple.rs` está destinado a ser un binario independiente, necesitas configurarlo en `Cargo.toml`. Añade lo siguiente a `Cargo.toml`:
     ```toml
     [[bin]]
     name = "simple"
     path = "src/simple.rs"
     ```
     Luego ejecuta:
     ```bash
     cargo run --bin simple
     ```

4. **Alternativa: Ejecutar sin Cargo**:
   - Si quieres compilar y ejecutar un solo archivo (por ejemplo, `simple.rs`) sin Cargo, asegúrate de que tenga una función `main` y usa el compilador `rustc`:
     ```bash
     rustc src/simple.rs
     ./simple
     ```
     Esto genera un ejecutable llamado `simple` en el directorio actual y lo ejecuta. Nota: Este enfoque no maneja dependencias, por lo que solo es adecuado para programas simples y autocontenidos.

5. **Verificar errores**:
   - Si encuentras errores, asegúrate de:
     - Tener Rust y Cargo instalados (verifica con `rustc --version` y `cargo --version`).
     - Que `Cargo.toml` esté configurado correctamente con las dependencias necesarias.
     - Que el código en `main.rs` o `simple.rs` tenga una función `fn main()` válida.
   - Ejecuta `cargo check` para verificar el código sin construir el binario:
     ```bash
     cargo check
     ```

6. **Ejemplo de `simple.rs`**:
   Si `simple.rs` contiene algo como:
   ```rust
   fn main() {
       println!("Hello from simple!");
   }
   ```
   Y lo has añadido como un binario en `Cargo.toml`, ejecutar `cargo run --bin simple` imprimirá `Hello from simple!`.

### Notas
- El directorio `target/debug` contiene los artefactos compilados. Puedes ejecutar el binario directamente con `./target/debug/<nombre_del_proyecto>` (reemplaza `<nombre_del_proyecto>` con el nombre en `Cargo.toml`), pero `cargo run` es preferible ya que maneja la compilación y ejecución.
- Si `simple.rs` es un módulo, asegúrate de que esté correctamente integrado en `main.rs` con `mod simple;`.
- Para configuraciones más complejas o código específico en `simple.rs`, comparte el contenido de `simple.rs` o `Cargo.toml` para una guía más específica.

Si te referías a algo específico con "ejecutar simple aquí" (por ejemplo, una función o configuración específica), ¡por favor proporciona más detalles y ajustaré la respuesta!