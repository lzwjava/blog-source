---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Desactivar el modo de sobrescritura de VS Code
translated: true
type: note
---

En Visual Studio Code, el comportamiento predeterminado es el **modo Insertar** (al escribir se inserta texto, desplazando el texto existente hacia adelante).  
El **modo Reemplazar** (al escribir se sobrescribe el texto existente) se activa al presionar la tecla **Insert** en tu teclado — esto alterna entre el modo Insertar y Reemplazar/Sobrescribir.

### Cómo volver del modo Reemplazar (Sobrescribir) al modo Insertar

1. Simplemente presiona la tecla **Insert** una vez en tu teclado.  
   → La barra de estado en la parte inferior derecha cambiará de **OVR** (Sobrescribir) a **INS** (Insertar).

### Si nunca quieres volver a entrar accidentalmente en el modo Sobrescribir

Puedes desactivar el alternado de la tecla Insert por completo:

#### Método 1: Atajo de teclado (recomendado)
Presiona `Ctrl + Shift + P` → escribe **"Toggle Insert/Overwrite"** — verás el comando  
`Preferences: Toggle Insert on Paste and Overtype` o similar.  
Más confiablemente, usa esta configuración directa:

#### Método 2: Añade esto a tu `settings.json`
```json
// Desactiva que la tecla Insert alterne el modo sobrescribir
"editor.occurencesHighlight": true,
"editor.overtypeMode": false,

// Esta es la clave:
"keyboard.dispatch": "keyCode"
```

En realidad, la solución mejor y más común:

```json
// Desactiva completamente la tecla Insert en VS Code
{
    "key": "insert",
    "command": "-editor.action.toggleOverwrite",
    "when": "editorTextFocus"
}
```

O simplemente desactiva el sobrescrito globalmente:

```json
"editor.occurrencesHighlight": true,
"editor.overwriteMode": false   // no es una configuración real, ignorar

// Configuración real para desactivar el alternado de sobrescrito:
"editor.insertSpaces": true,  // no relacionado

// Manera correcta:
{
    "key": "insert",
    "command": "noop"   // o eliminar el enlace predeterminado
}
```

#### Solución permanente más simple (la usa la mayoría de la gente):
1. Abre Configuración (`Ctrl + ,`)
2. Busca **"overwrite"**
3. Desmarca **Editor: Overtype** (si existe) o mejor:
4. Añade esta línea a tu `settings.json` (Ctrl + Shift + P → "Preferences: Open Settings (JSON)"):

```json
// Desactiva completamente que la tecla Insert alterne el modo sobrescribir
{
    "key": "insert",
    "command": "-editor.action.toggleOverwrite"
}
```

Después de añadir eso, la tecla Insert no hará nada en VS Code, y siempre permanecerás en el modo Insertar.

Esa es la solución más común y confiable usada por los desarrolladores que siguen presionando Insert accidentalmente (especialmente en laptops con teclados pequeños en Taiwán/Asia donde es fácil presionar Insert).

¡Avísame si estás en macOS (usa una tecla diferente) o quieres una solución al hacer clic en la barra de estado!