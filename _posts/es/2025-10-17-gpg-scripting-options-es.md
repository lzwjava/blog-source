---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Opciones de Comando GPG para Scripts
translated: true
type: note
---

### Explicación de las Opciones del Comando GPG

Las opciones `--batch`, `--yes`, `-o` y `--pinentry-mode` son indicadores comunes utilizados con el comando `gpg` (GNU Privacy Guard) para operaciones no interactivas o automatizadas, como el cifrado, descifrado o firma. Aquí tienes un desglose de cada una:

- **`--batch`**: Habilita el modo por lotes (batch), que evita que `gpg` haga preguntas interactivas o permita comandos interactivos. Esto es útil para scripts o automatización donde la entrada del usuario no es posible. Se puede deshabilitar con `--no-batch`.

- **`--yes`**: Asume automáticamente "sí" como respuesta a la mayoría de las peticiones de confirmación (por ejemplo, sobrescribir archivos). Esto evita que la ejecución se detenga debido a preguntas de sí/no.

- **`-o` (o `--output`)**: Especifica el archivo de salida para la operación. Debe ir seguido de un nombre de archivo, por ejemplo, `-o salida.txt`. Sin esta opción, la salida podría ir a la salida estándar (stdout) o a una ubicación por defecto.

- **`--pinentry-mode`**: Controla cómo el agente de GPG maneja la entrada del PIN (solicitud de frase de contraseña). Acepta un valor de modo como `ask` (por defecto: muestra una ventana gráfica o de consola), `loopback` (permite frases de contraseña a través de stdin para scripts, sin una ventana emergente), `cancel` (cancela las operaciones que requieren un PIN) o `error` (devuelve un error en lugar de solicitar el PIN). Esto se usa a menudo con `loopback` en scripts por lotes para una entrada de frase de contraseña segura y no interactiva.

Estas opciones se combinan frecuentemente en scripts, por ejemplo, `gpg --batch --yes -o descifrado.txt --pinentry-mode loopback --decrypt cifrado.gpg`, para ejecutarse de forma completamente automatizada.

#### Referencias
- [Página del Manual de GPG](https://linux.die.net/man/1/gpg)
- [Opciones del Agente de GnuPG](https://www.gnupg.org/documentation/manuals/gnupg/Agent-Options.html)
- [Manual de GnuPG](https://www.gnupg.org/documentation/manuals/gnupg/index.html)