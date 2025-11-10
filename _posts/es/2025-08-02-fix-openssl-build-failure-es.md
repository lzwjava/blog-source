---
audio: false
generated: true
image: false
lang: es
layout: post
title: Corrección de Error de Compilación de OpenSSL
translated: true
type: note
---

Te estás topando con el clásico error de compilación de "openssl-sys" porque no tienes instalada la herramienta `pkg-config` del sistema ni los headers de desarrollo de OpenSSL. En Ubuntu/Debian, la solución más simple es:

1. **Instalar pkg-config y los headers de desarrollo de OpenSSL**

   ```bash
   sudo apt update
   sudo apt install pkg-config libssl-dev
   ```

   * `pkg-config` permite que el script de compilación de Rust detecte dónde está OpenSSL.
   * `libssl-dev` proporciona los headers y bibliotecas (el paquete "–dev").

2. **Reinicia tu compilación**

   ```bash
   cargo clean
   cargo run
   ```

---

### Alternativa: usar la funcionalidad "vendored"

Si no quieres depender de OpenSSL del sistema (o no tienes acceso de root), puedes pedirle al crate que compile una copia empaquetada de OpenSSL desde el código fuente:

1. En tu **Cargo.toml**, cambia tu dependencia a:

   ```toml
   [dependencies]
   openssl = { version = "0.10", features = ["vendored"] }
   ```
2. Luego compila de nuevo:

   ```bash
   cargo clean
   cargo run
   ```

Esto compilará OpenSSL y se enlazará contra esa versión, evitando la necesidad de una instalación en el sistema.

---

### (Opcional) Instalación personalizada de OpenSSL

Si tienes OpenSSL instalado en una ubicación no estándar, puedes dirigir la compilación hacia ella:

```bash
export OPENSSL_DIR=/ruta/a/tu/openssl
export OPENSSL_LIB_DIR=$OPENSSL_DIR/lib
export OPENSSL_INCLUDE_DIR=$OPENSSL_DIR/include
```

Luego ejecuta de nuevo `cargo run`. Esto le indica a openssl-sys exactamente dónde encontrar los headers y las bibliotecas.

---

> **Nota:** La advertencia sobre que `edition2024` está estabilizada es inofensiva—puedes eliminar esa funcionalidad de tu `Cargo.toml`, pero no bloqueará tu compilación.