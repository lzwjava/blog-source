---
audio: false
generated: true
lang: es
layout: post
title: Comando de Rust de una Línea con Encadenamiento de Shell
translated: true
type: note
---

Estás tocando un deseo común entre desarrolladores experimentados que vienen de lenguajes como Python, Ruby o JavaScript, donde a menudo tienes un solo comando para ejecutar un script directamente. Rust, al ser un lenguaje compilado, tiene un flujo de trabajo ligeramente diferente por defecto.

Sin embargo, definitivamente puedes lograr una sensación de "una sola línea", especialmente para scripts simples o ejercicios, encadenando comandos en tu terminal.

### La "Una Línea" Directa (Encadenamiento en la Terminal)

Ya tienes los componentes: `rustc` para compilación y `./` para ejecución. Puedes combinarlos usando operadores de la terminal:

```bash
rustc scripts/rust/example.rs -o test/example && ./test/example
```

**Explicación:**

  * `rustc scripts/rust/example.rs -o test/example`: Esto compila tu archivo Rust y coloca el ejecutable en `test/example`.
  * `&&`: Este es un **separador condicional de comandos** en bash (y en la mayoría de terminales tipo Unix). El comando *después* de `&&` solo se ejecutará si el comando *antes* de `&&` se completa exitosamente (es decir, devuelve un código de salida 0).
      * Si `rustc` compila sin errores, devolverá 0, y entonces `./test/example` se ejecutará.
      * Si `rustc` encuentra un error de compilación, devolverá un código de salida distinto de cero, y `./test/example` *no* se ejecutará. ¡Este es un buen comportamiento!

### Para una Experiencia Más "Tipo Script" (Cargo)

Si bien el enfoque anterior con `&&` funciona bien para pruebas rápidas, para cualquier cosa más allá de scripts triviales de un solo archivo, la herramienta `cargo` de Rust es la forma recomendada, y *sí* proporciona un comando de una sola línea, similar a Python, para ejecutar código dentro de un proyecto:

1.  **Inicializar un Proyecto Cargo (si aún no lo has hecho):**
    Si tu `scripts/rust/example.rs` es solo un archivo independiente, normalmente comenzarías creando un proyecto Cargo en su directorio padre (o en un directorio nuevo dedicado).

    ```bash
    # Ve al directorio donde quieres tu proyecto (por ejemplo, scripts/rust)
    cd scripts/rust

    # Inicializa un nuevo proyecto binario de Cargo
    cargo init --bin .
    ```

    Esto creará `Cargo.toml` y moverá tu `example.rs` (si era `main.rs`) o ajustará el `Cargo.toml` para que apunte a él (si renombras `example.rs` a `main.rs` dentro de `src/`).

2.  **Ejecutar con Cargo:**
    Una vez que tienes un proyecto Cargo configurado, puedes compilar y ejecutar con un solo comando:

    ```bash
    # Desde la raíz de tu proyecto (por ejemplo, scripts/rust si ejecutaste cargo init allí)
    cargo run
    ```

    `cargo run` hará:

      * Compilará tu código (si no ha sido compilado o si se han realizado cambios).
      * Luego, ejecutará el binario resultante.
      * Por defecto, el binario se coloca en `target/debug/` dentro de tu proyecto, pero no tienes que preocuparte por su ruta específica.

**Por qué se prefiere Cargo:**

  * **Gestión de Dependencias:** Si tu código alguna vez necesita librerías externas (crates), Cargo se encarga de buscarlas, compilarlas y enlazarlas automáticamente. Las especificas en `Cargo.toml`.
  * **Estructura de Proyecto Estándar:** Fomenta un diseño consistente (`src/main.rs`, `Cargo.toml`), lo que hace que tu código sea más fácil de entender para otros (y para tu yo futuro).
  * **Testing:** `cargo test` ejecuta tus pruebas unitarias y de integración.
  * **Builds de Release:** `cargo run --release` (o `cargo build --release`) compila con optimizaciones para producción.
  * **Sin Limpieza Manual:** No tienes que eliminar manualmente los binarios compilados. `cargo clean` se encarga de ello.

### ¿Y un enfoque de "Scripting" verdadero como `python script.py` de Python?

Rust no está diseñado como un lenguaje de scripting interpretado. Es un lenguaje de sistemas compilado. Por lo tanto, no obtendrás un comando directo `rust script.rs` que compile y ejecute sin un paso de compilación explícito.

Sin embargo, existen herramientas de la comunidad que intentan cerrar esta brecha para "scripts" rápidos de Rust de un solo archivo (aunque todavía compilan en segundo plano):

  * **`cargo-script`**: Un subcomando de Cargo que te permite ejecutar archivos `.rs` individuales, manejando las dependencias si se especifican mediante comentarios. Normalmente lo instalarías con `cargo install cargo-script`. Entonces podrías ejecutar `cargo script scripts/rust/example.rs`.
  * **`rust-script`**: Otra herramienta popular para ejecutar archivos Rust directamente como scripts. Instálalo mediante `cargo install rust-script`. Luego, a menudo puedes simplemente hacer que tu archivo `.rs` sea ejecutable (`chmod +x example.rs`) y ejecutarlo: `./example.rs`. Maneja la compilación y ejecución en segundo plano.

Para tu caso de uso de probar rápidamente `example.rs`, el comando de una línea `rustc ... && ./...` está perfectamente bien y responde directamente a tu pregunta sobre encadenar los dos comandos. Para cualquier desarrollo no trivial, adoptar Cargo será una experiencia de Rust más productiva e idiomática.