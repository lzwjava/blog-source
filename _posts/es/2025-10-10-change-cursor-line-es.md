---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Cursor de VS Code a Línea
translated: true
type: note
---

### Cómo arreglar el cursor de bloque (rectángulo) en VS Code

Entendido—parece que tu cursor ha cambiado al estilo de bloque/rectángulo (común en modo sobrescritura o configuraciones por defecto), pero prefieres el estilo de **línea** vertical fina para una edición más fácil. Esto es un ajuste rápido en la configuración. Sigue estos pasos exactamente:

#### Mediante la Interfaz de Configuración (Más Fácil):
1. Abre VS Code.
2. Presiona `Ctrl + ,` (Windows/Linux) o `Cmd + ,` (macOS) para abrir Configuración.
3. En la caja de búsqueda superior, escribe: **cursor style**.
4. Busca **Editor: Cursor Style** (bajo Text Editor > Cursor).
5. Haz clic en el menú desplegable y selecciona **Line** (puede que actualmente diga "Block").
6. El cambio ocurre instantáneamente—prueba a escribir en un archivo para ver el cursor de línea fina.

Si aún no se actualiza, cierra y reabre VS Code, o reinícialo completamente.

#### Mediante settings.json (Para Precisión):
1. Abre la Paleta de Comandos: `Ctrl + Shift + P` (o `Cmd + Shift + P` en macOS).
2. Escribe y selecciona: **Preferences: Open User Settings (JSON)**.
3. Añade o actualiza esta línea dentro de las `{}` (crédala si está vacía):
   ```json:disable-run
   "editor.cursorStyle": "line"
   ```
4. Guarda el archivo (`Ctrl + S` o `Cmd + S`).

#### Consejos Adicionales:
- **¿Modo Sobrescritura?** Si estás accidentalmente en "sobrescritura" (donde bloquea caracteres), presiona la tecla **Insert** en tu teclado para volver al modo inserción.
- **¿Problema de Parpadeo?** Si la línea se ve entrecortada, busca **cursor blinking** en la configuración y ajústalo a **Blink** o **Smooth**.
- **¿Extensiones Interfiriendo?** Deshabilita extensiones como Vim temporalmente (Vista Extensiones > clic derecho > Disable) para probar.

Esto debería darte ese cursor de línea limpio inmediatamente. Si sigue teniendo forma de rectángulo después de esto, comparte tu SO o una captura de pantalla para una ayuda más específica.

[Documentación del Cursor en VS Code](https://code.visualstudio.com/docs/editor/codebasics#_cursor-style)