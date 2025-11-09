---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Pegar en Vim en Windows
translated: true
type: note
---

## Pegar en Vim dentro de Git Bash en Windows

Ah, ya veo el problema—el comando `p` de Vim en Git Bash (que se ejecuta en Windows) puede ser complicado, especialmente al tratar con el portapapeles del sistema o texto externo. Esto es un problema común porque Git Bash usa MinTTY como su emulador de terminal, y el comportamiento predeterminado de Vim no siempre funciona bien con el portapapeles de Windows. El comando `p` solo pega desde el búfer de yank *interno* de Vim (lo que copiaste con `y` dentro de la misma sesión de Vim). Para cualquier cosa de fuera de Vim (como copiar desde el Bloc de notas o un navegador), necesitas la integración con el portapapeles o la función de pegar de la terminal.

No te preocupes—aquí te explico cómo manejarlo paso a paso, adaptado a tu flujo de trabajo de "seleccionar todo, borrar y pegar en texto nuevo". Cubriré el pegado interno (que ya debería funcionar) y el pegado externo.

### Comprobación Rápida: ¿Tu Vim Admite el Portapapeles del Sistema?
Primero, verifica si tu Vim puede acceder directamente al portapapeles de Windows (esto arregla mucho):
1. Abre Git Bash.
2. Ejecuta `vim --version | grep clipboard` (o abre Vim con `vim`, luego escribe `:version` y busca `+clipboard`).
   - Si muestra `+clipboard`, genial—puedes usar `"+p` para pegar desde el portapapeles de Windows.
   - Si muestra `-clipboard` o nada, no es compatible (común en el Vim incluido con Git Bash). Salta a los métodos de pegado de terminal a continuación.

Si no es compatible, considera instalar un Vim completo para Windows (por ejemplo, via Chocolatey: `choco install vim`) o usar Neovim/WSL para una mejor integración.

### 1. Pegado Interno (Yank Dentro de Vim, Pegar en la Misma Sesión)
Esto es a lo que se dirigían mis instrucciones anteriores—copiar *dentro* de Vim y pegar en un archivo nuevo en la *misma* sesión. `p` debería funcionar bien aquí, sin peculiaridades de Git Bash:
- En `oldfile.txt`: `gg` (arriba), `yG` (yank todo).
- `:e newfile.txt` (abrir nuevo archivo en el mismo Vim).
- `p` (pegar). Coloca el contenido justo después del cursor.
- `:wq` para guardar.

Si `p` aún falla (por ejemplo, no pega nada o el texto sale corrupto), podría ser un problema del yank—prueba `"+yG` en lugar de `yG` si el portapapeles es compatible, luego `"+p`.

### 2. Pegar Texto Externo en Vim (Desde Aplicaciones de Windows)
Si estás copiando desde fuera (por ejemplo, seleccionar todo en el Bloc de notas, Ctrl+C, luego quieres pegar en Vim):
- **Método 1: Usar la Función de Pegar Integrada de Git Bash (Más Fácil, No Requiere Cambios en Vim)**
  1. Abre tu archivo: `vim newfile.txt`.
  2. Entra en modo inserción: Presiona `i`.
  3. Haz clic derecho en la ventana de Git Bash (esto pega directamente desde el portapapeles de Windows en la terminal/Vim).
     - Atajos alternativos: Tecla `Insert`, o habilita el modo Quick Edit en Git Bash (clic derecho en la barra de título > Options > Quick Edit) luego usa Ctrl+Shift+V.
  4. Presiona `Esc` para salir del modo inserción.
  - *Consejo Profesional:* Si pegar texto de múltiples líneas se ve raro (saltos de línea o sangrías adicionales), a menudo se debe a los finales de línea de Windows (CRLF vs. LF). Arréglalo con `:set ff=unix` en Vim antes de pegar, o usa `:%s/\r$//g` después para eliminar los retornos de carro.

- **Método 2: Si +clipboard es Compatible (Directamente en Vim)**
  1. Copia el texto externamente (Ctrl+C).
  2. En modo comando de Vim: `"+p` (pega desde el portapapeles del sistema después del cursor) o `"+P` (antes).
  3. Para tu flujo de trabajo: Después de borrar en el archivo antiguo, cambia al archivo nuevo y `"+p`.

### 3. Copiar desde Vim al Exterior (Yank Hacia Windows)
- El yank interno (`y`) se queda en Vim—usa la copia de la terminal para el exterior.
- Selecciona texto en Vim: `v` (modo visual), mueve el cursor para seleccionar todo (`ggVG`), luego `y`.
- Para copiar a Windows: Clic derecho > Edit > Copy (o resaltar y clic derecho > Copy).
- Con +clipboard: `"+y` en lugar de `y`, luego Ctrl+V en otro lugar.

### Solución de Problemas Comunes de Pegado en Git Bash + Vim
- **Texto Corrupto (por ejemplo, Líneas Parciales o Espacios Extra):** Desactiva el bracketed paste en Vim (`:set paste` antes de entrar al modo inserción, luego pega, luego `:set nopaste`). O añade `set paste` a `~/.vimrc` para siempre activo (pero desactiva algunas características como el auto-indentado).
- **No Pega Nada:** Asegúrate de estar en modo inserción para el pegado de terminal—`p` en modo comando es solo interno.
- **Interferencia del Ratón:** Si el clic derecho selecciona en lugar de pegar, alterna con clic derecho en la barra de título > Options > Mouse > Quick Edit.
- **Para Borrar Todo Antes de Pegar:** En tu flujo de trabajo, después de hacer yank, usa `:%d` para limpiar el nuevo archivo, luego pega.

¡Esto debería permitirte pegar sin problemas! Si aún no funciona (por ejemplo, comparte qué sucede exactamente cuando intentas `p`), o si estás pegando específicamente *desde* fuentes externas, házmelo saber para más ajustes.

[How do you copy and paste into Git Bash](https://stackoverflow.com/questions/2304372/how-do-you-copy-and-paste-into-git-bash)  
[Copying from Windows clipboard in Vim](https://vi.stackexchange.com/questions/37599/copying-from-windows-clipboard)  
[How to copy paste contents in the vi editor](https://askubuntu.com/questions/256782/how-to-copy-paste-contents-in-the-vi-editor)