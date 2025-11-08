---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configurar Zed con atajos de teclado de Emacs
translated: true
type: note
---

### Configurar Zed Editor con atajos de teclado de Emacs

Parece que te refieres a **Zed** (el editor de código de alto rendimiento), ya que "Zig editor" no se refiere a una herramienta estándar—Zig es un lenguaje de programación sin un editor integrado. Si no era eso lo que querías, ¡aclaralo! Asumiendo que es Zed, este tiene soporte integrado para atajos de teclado de Emacs (etiquetado como "Emacs (Beta)"). Esto cubre muchas funciones básicas listas para usar, como movimiento (`Ctrl-b/f/n/p`) y edición (`Ctrl-d` para borrar carácter, `Ctrl-k` para cortar hasta el final de la línea). Puedes activarlo fácilmente y luego personalizarlo más si es necesario.

#### Paso 1: Activar el mapa de teclas Emacs integrado
El modo Emacs de Zed está predefinido y no requiere configuración manual de enlaces para las funciones básicas. Así es como puedes cambiarlo:

1. Abre la configuración de Zed:
   - macOS: `Cmd-,`
   - Windows/Linux: `Ctrl-,`

2. En la interfaz de configuración, busca "base keymap" y establécelo en **Emacs**.

   *O, edita directamente en `settings.json`* (ábrelo mediante `Cmd-Alt-,` en macOS o `Ctrl-Alt-,` en Windows/Linux):
   ```json
   {
     "base_keymap": "Emacs"
   }
   ```

   Guarda y recarga Zed (`Cmd-R` o `Ctrl-R`). Eso es todo—el mapa de teclas beta de Emacs se activa inmediatamente.

   Alternativamente, usa la paleta de comandos (`Cmd-Shift-P` o `Ctrl-Shift-P`), escribe "toggle base keymap" y selecciona Emacs.

Esto te da la memoria muscular básica de Emacs sin trabajo adicional. Para una lista completa de los enlaces integrados, revisa los archivos de mapa de teclas por defecto de Zed en el código fuente (ej., vía GitHub), pero lo básico incluye:
- **Movimiento**: `Ctrl-b` (carácter izquierda), `Ctrl-f` (carácter derecha), `Ctrl-p` (línea arriba), `Ctrl-n` (línea abajo), `Alt-b/f` (palabra anterior/siguiente).
- **Edición**: `Ctrl-d` (borrar carácter), `Ctrl-k` (cortar hasta final de línea), `Ctrl-y` (pegar), `Ctrl-@` (establecer marca para región), `Ctrl-w` (cortar región).
- **Otros**: `Ctrl-x Ctrl-s` (guardar), `Ctrl-g` (cancelar), `Ctrl-/` (deshacer).

#### Paso 2: Añadir o personalizar enlaces básicos (si es necesario)
Para ajustes o un comportamiento más similar a Emacs (ej., mejor navegación home/end o por párrafos), edita `keymap.json`:
- Ábrelo mediante la paleta de comandos: Escribe "open keymap file."
- Ruta: `~/.config/zed/keymap.json` (macOS/Linux) o `~\AppData\Roaming\Zed\keymap.json` (Windows).

Añade enlaces como un array JSON en contextos como "Editor". Aquí tienes un **ejemplo mínimo** para movimiento y edición básicos (pégalo en el array; está basado en configuraciones de la comunidad para compatibilidad):

```json
[
  {
    "context": "Editor",
    "bindings": {
      // Movimiento básico
      "ctrl-a": "editor::MoveToBeginningOfLine",
      "ctrl-e": "editor::MoveToEndOfLine",
      "ctrl-b": "editor::MoveLeft",
      "ctrl-f": "editor::MoveRight",
      "ctrl-p": "editor::MoveLineUp",
      "ctrl-n": "editor::MoveLineDown",
      "alt-b": "editor::MoveToPreviousWordStart",
      "alt-f": "editor::MoveToNextWordEnd",

      // Edición básica
      "ctrl-d": "editor::DeleteRight",
      "ctrl-k": "editor::CutToEndOfLine",
      "ctrl-y": "editor::Paste",
      "ctrl-w": "editor::Cut",
      "ctrl-@": ["editor::SetSelectionAnchor", { "selection_id": 0 }],  // Establecer marca
      "ctrl-x ctrl-x": "editor::FlipSelectionAnchor",  // Intercambiar punto/marca

      // Extras de navegación
      "ctrl-home": "editor::MoveToBeginning",
      "ctrl-end": "editor::MoveToEnd",
      "ctrl-g": "editor::Cancel"
    }
  }
]
```

- Guarda y recarga Zed. Estos enlaces sobrescriben o se añaden al mapa base de Emacs.
- Prueba en un buffer del editor. Para selecciones, usa `Ctrl-Space` (o `Ctrl-@`) para establecer la marca, luego muévete para seleccionar una región.
- Consejo profesional: Combínalo con `vim_mode: false` en settings.json para evitar conflictos.

#### Consejos
- **Estado beta**: El modo Emacs está mejorando (sigue el progreso [aquí](https://github.com/zed-industries/zed/issues/4856)). Reporta problemas en el GitHub de Zed.
- **Configuraciones personalizadas completas**: Para configuraciones avanzadas (ej., cambiar paneles con `Ctrl-x o`), consulta ejemplos de la comunidad en la discusión a continuación.
- Si quieres modos Vim/Helix además de este, establece `vim_mode: true` o `helix_mode: true` en la configuración—se superponen.

Esto debería darte el 80% de la sensación básica de Emacs. Empieza con la configuración integrada, ¡luego itera!

[Documentación de Atajos de Teclado](https://zed.dev/docs/key-bindings)  
[Configurando Zed](https://zed.dev/docs/configuring-zed)  
[Discusión del Mapa de Teclas Emacs](https://github.com/zed-industries/zed/discussions/6572)  
[Problema de Compatibilidad con Emacs](https://github.com/zed-industries/zed/issues/4856)