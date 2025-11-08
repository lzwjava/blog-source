---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Instalación de Rust en Ubuntu
translated: true
type: note
---

### Instalación de Rust en Ubuntu 22.04 LTS

La mejor forma de instalar Rust es usando `rustup`, el instalador oficial de la cadena de herramientas. Este método es sencillo, permite actualizaciones fáciles y funciona en tu sistema Ubuntu 22.04 de 64 bits. Normalmente no se necesitan dependencias adicionales más allá de una configuración básica de Ubuntu.

#### Instrucciones Paso a Paso

1.  **Actualiza tu lista de paquetes** (opcional pero recomendado):
    ```
    sudo apt update
    ```

2.  **Instala Rust usando rustup**:
    Ejecuta el siguiente comando para descargar y ejecutar el script de instalación:
    ```
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```
    - Esto descargará el script de forma segura a través de HTTPS.
    - Cuando se te solicite, elige la opción de instalación por defecto (presiona `1` y Enter).
    - El instalador agregará los binarios de Rust a `~/.cargo/bin` y actualizará tu perfil de shell (por ejemplo, `~/.bashrc` o `~/.profile`).

3.  **Recarga la configuración de tu shell**:
    Para que los cambios surtan efecto inmediatamente sin reiniciar tu terminal:
    ```
    source ~/.cargo/env
    ```
    Alternativamente, cierra y vuelve a abrir tu terminal.

4.  **Verifica la instalación**:
    Comprueba que Rust se haya instalado correctamente:
    ```
    rustc --version
    cargo --version
    ```
    Deberías ver una salida como `rustc 1.82.0` (o la última versión estable) y similar para Cargo.

#### Notas Adicionales

-   **Desinstalación**: Si es necesario, ejecuta `rustup self uninstall`.
-   **Actualizar Rust**: Usa `rustup update` para obtener la última versión.
-   **IDE/Soporte**: Para desarrollo, considera instalar `rust-analyzer` a través de tu editor (por ejemplo, la extensión de VS Code) para una mejor finalización de código.
-   Esto instala el canal estable por defecto. Para nightly o beta, usa `rustup install nightly` después de la configuración.

Si encuentras algún error (por ejemplo, que no se encuentra curl), instálalo con `sudo apt install curl`.

[Guía Oficial de Instalación de Rust](https://www.rust-lang.org/tools/install)