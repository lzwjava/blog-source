---
audio: false
generated: true
lang: es
layout: post
title: Instalar Rust en macOS con rustup
translated: true
type: note
---

## Instalación de Rust usando rustup

1. **Abre Terminal**  
    Puedes encontrar Terminal en **Aplicaciones > Utilidades** o buscarlo usando Spotlight.

2. **Instala rustup y Rust**  
    Ejecuta el siguiente comando para descargar y ejecutar el script de instalación de rustup:

    ```sh
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```

    El script te pedirá que procedas. Presiona `1` para la instalación por defecto.

3. **Configura tu Shell**  
    Después de la instalación, puede que necesites agregar Rust a la variable de sistema `PATH`. El instalador proporcionará un comando similar a:

    ```sh
    source $HOME/.cargo/env
    ```

    Agrega esta línea a tu archivo de configuración del shell (por ejemplo, `.zshrc`, `.bashrc`, o `.bash_profile`) para que Rust esté disponible en sesiones futuras.

4. **Verifica la Instalación**  
    Comprueba que Rust esté instalado correctamente:

    ```sh
    rustc --version
    ```

    Deberías ver la versión del compilador de Rust si la instalación fue exitosa.

---

## Usando Homebrew para Instalar Rust

Alternativamente, puedes usar [Homebrew](https://brew.sh/) para instalar Rust, aunque generalmente se recomienda `rustup` para actualizaciones y gestión de versiones más sencillas.

1. **Instala Homebrew** (si aún no está instalado):

    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **Instala Rust con Homebrew**:

    ```sh
    brew install rust
    ```

3. **Verifica la Instalación**:

    ```sh
    rustc --version
    ```

---

## Compilando Código Rust

1. **Escribe un Programa en Rust**  
    Crea un archivo llamado `main.rs` con el siguiente contenido:

    ```rust
    fn main() {
         println!("Hello, World!");
    }
    ```

2. **Compila el Programa**  
    En la terminal, navega al directorio que contiene tu archivo y ejecuta:

    ```sh
    rustc main.rs
    ```

3. **Ejecuta el Programa Compilado**:

    ```sh
    ./main
    ```

---

Esta configuración debería permitirte comenzar con el desarrollo en Rust en macOS. Si tienes algún problema, ¡no dudes en preguntar!