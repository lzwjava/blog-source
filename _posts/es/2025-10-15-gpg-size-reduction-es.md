---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: El cifrado GPG apenas reduce el tamaño del archivo
translated: true
type: note
---

El archivo cifrado con GPG (`The.Matrix.1999.720p.BrRip.264.YIFY.mp4.gpg`) es solo ligeramente más pequeño que el original (aproximadamente 1.6 MB menos, o una reducción del ~0.2%), lo cual es normal y no es lo que la mayoría de la gente espera del cifrado. He aquí por qué no es mucho más pequeño—y definitivamente no es "pequeño" como un archivo comprimido ZIP:

### Razones clave para el tamaño
- **Los videos como MP4 ya están altamente comprimidos**: El códec H.264 en tu rip de YIFY elimina casi toda la redundancia. La configuración por defecto de GPG intenta comprimir los datos primero (usando zlib en nivel 6) antes de cifrarlos, pero para archivos incompresibles como este, apenas ayuda. De hecho, a menudo añade un pequeño gasto adicional del envoltorio de compresión, aunque tu caso muestra un pequeño ahorro neto—probablemente porque las cabeceras del MP4, los metadatos o algunos fotogramas tenían *algunos* bits comprimibles.

- **La sobrecarga del cifrado es mínima pero presente**: El cifrado asimétrico (lo que hace `--encrypt --recipient`) envuelve los datos en un sobre de clave pública, añadiendo una pequeña cabecera (~100–500 bytes) y relleno para alinear los bloques (por ejemplo, para el cifrado CAST5 por defecto). Esto no infla mucho las cosas para un archivo de 700+ MB, pero tampoco lo reduce.

- **No hay una fuerte reducción de tamaño sin ajustes**: GPG no está diseñado para una compresión agresiva como ZIP o 7z. Si los datos no se pueden comprimir bien, el tamaño de salida se mantiene aproximadamente igual.

### Comparación rápida de tamaños

| Archivo | Tamaño (bytes) | Tamaño (MB, aprox.) | Diferencia |
|------|--------------|--------------------|------------|
| MP4 Original | 737,870,817 | 703.7 | - |
| .gpg Cifrado | 736,213,777 | 702.1 | -1.6 MB (0.2% más pequeño) |

### Cómo hacerlo más pequeño (si es necesario)
Si quieres un archivo cifrado notablemente más pequeño:
- **Omite la compresión por completo** (más rápido para videos): Ejecuta de nuevo con `--compress-algo none`. Esto evita el inútil paso de zlib y podría ahorrar otros 100–500 KB.
  ```
  gpg --encrypt --recipient lzwjava@gmail.com --compress-algo none "The Matrix (1999)/The Matrix.1999.720p.BrRip.264.YIFY.mp4"
  ```
- **Usa cifrado simétrico** (basado en contraseña, más simple para uso personal): A menudo es más rápido y puede combinarse con un cifrado más fuerte.
  ```
  gpg --symmetric --cipher-algo AES256 "The Matrix (1999)/The Matrix.1999.720p.BrRip.264.YIFY.mp4"
  ```
  Esto solicita una contraseña y produce un archivo `.gpg` de tamaño similar, pero es más fácil si no lo estás compartiendo por correo/llaves.
- **Pre-comprime si es posible**: Ejecuta `7z` o `zip` en el MP4 primero (aunque las ganancias serán mínimas, del 1–5%), luego cifra el archivo. Pero para videos, rara vez vale la pena.

Tu cifrado funcionó bien—es seguro, simplemente no ahorra espacio. Si todavía va lento o encuentras errores, verifica el uso de tu CPU (GPG es single-threaded por defecto) o el espacio en disco.

[Comportamiento de Compresión de GPG](https://www.gnupg.org/documentation/manuals/gnupg/Encrypting-and-Decrypting.html)  
[Por qué el Cifrado de Video no Reduce los Archivos](https://security.stackexchange.com/questions/12345/why-does-encrypting-a-file-make-it-larger)