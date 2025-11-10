---
audio: false
generated: true
lang: es
layout: post
title: Opciones de Ubicación de Salida de Rust
translated: true
type: note
---

¡Estás haciendo una gran pregunta que aborda cómo se estructuran y construyen típicamente los proyectos en Rust!

Cuando usas `rustc` directamente, tienes dos opciones principales para especificar la ubicación de salida:

1.  **`-o <nombre_archivo_salida>`**: Esta opción especifica la *ruta y nombre de archivo exactos* para el ejecutable o biblioteca compilado.

    ```bash
    rustc scripts/rust/example.rs -o test/example
    ```

    Esto compilará `example.rs` y colocará el ejecutable llamado `example` directamente en el directorio `test/`. Si `test/` no existe, `rustc` lo creará.

2.  **`--out-dir <directorio_salida>`**: Esta opción especifica un *directorio* donde `rustc` debe colocar todos los archivos de salida generados (el ejecutable/biblioteca, junto con cualquier archivo intermedio como `.d`, `.rmeta`, etc.).

    ```bash
    rustc scripts/rust/example.rs --out-dir test/
    ```

    En este caso, `rustc` compilará `example.rs` y colocará el ejecutable (que se llamará `example` por defecto, derivado del nombre del archivo fuente) dentro del directorio `test/`.

**Recomendación: Usa Cargo para Proyectos**

Si bien `rustc` directamente te da un control detallado, para la mayoría de los proyectos de Rust, querrás usar **Cargo**. Cargo es el sistema de compilación y gestor de paquetes de Rust, y simplifica la gestión de dependencias, la compilación, las pruebas y la ejecución de tu código.

Con Cargo, los binarios de salida se colocan típicamente en un directorio `target` dentro de la raíz de tu proyecto. Por ejemplo, si tienes un proyecto configurado con Cargo:

```
mi_proyecto/
├── Cargo.toml
└── src/
    └── main.rs
```

Cuando ejecutas `cargo build` o `cargo run`, el ejecutable compilado se colocará en `mi_proyecto/target/debug/mi_proyecto` (para compilaciones de depuración) o `mi_proyecto/target/release/mi_proyecto` (para compilaciones de release).

Si quieres controlar el directorio `target` para Cargo, puedes:

  * **Variable de entorno `CARGO_TARGET_DIR`**:

    ```bash
    CARGO_TARGET_DIR=./test cargo build
    ```

    Esto colocará todo el directorio `target` (que contiene `debug`, `release`, etc.) dentro de tu directorio `test/`. El ejecutable estaría entonces en `test/debug/mi_proyecto`.

  * **Opción de línea de comandos `--target-dir` para Cargo**:

    ```bash
    cargo build --target-dir test/
    ```

    Esto hace lo mismo que la variable de entorno.

  * **`.cargo/config.toml`**: Puedes establecer un `target-dir` predeterminado para todos los proyectos de Cargo en tu máquina o para un workspace específico agregándolo a un archivo `.cargo/config.toml`.

**¿Por qué usar Cargo?**

  * **Disposición de Proyecto Estandarizada:** Cargo impone una estructura de proyecto común, facilitando que otros desarrolladores de Rust entiendan tu código.
  * **Gestión de Dependencias:** Cargo maneja la descarga y compilación de las dependencias de tu proyecto automáticamente.
  * **Pruebas y Evaluación Comparativa:** Cargo tiene comandos integrados para ejecutar pruebas (`cargo test`) y benchmarks (`cargo bench`).
  * **Gestión de Lanzamientos:** Cargo ayuda con la creación de compilaciones de release (`cargo build --release`) y la publicación de crates en crates.io.

A menos que tengas una razón muy específica para no hacerlo, es muy recomendable organizar tu código Rust en un proyecto de Cargo.

**Dada tu salida de `git status`:**

Tu `git status` muestra `example` y `scripts/rust/` como no rastreados. Esto sugiere que podrías estar compilando `scripts/rust/example.rs` directamente con `rustc` fuera de un proyecto de Cargo.

Si `example` es el binario compilado, entonces el comando anterior `rustc scripts/rust/example.rs` lo colocó en el directorio actual (`lzwjava.github.io`).

Para lograr tu objetivo de ponerlo en `test/example` (asumiendo que `test` es un directorio en la raíz de `lzwjava.github.io`), usarías:

```bash
rustc scripts/rust/example.rs -o test/example
```

Esta es la forma más directa de obtener la ruta de salida específica que pediste usando `rustc`.