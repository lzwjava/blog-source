---
audio: false
generated: true
lang: es
layout: post
title: Selección Rápida de Código y Edición con IA
translated: true
type: note
---

A continuación se presenta un resumen de cómo seleccionar rápidamente una función o método usando atajos en **Visual Studio Code (VS Code)**, **Cursor** e **IntelliJ IDEA**, seguido de cómo aprovechar sus funciones de IA para corregir o editar el código seleccionado.

### Visual Studio Code (VS Code)
VS Code no tiene un atajo directo para seleccionar una función/método completa cuando el cursor está dentro de ella, pero puedes usar los siguientes enfoques:
- **Expandir Selección**: Presiona `Ctrl+Shift+.` (Windows/Linux) o `Cmd+Shift+.` (Mac) para expandir el alcance de la selección. Presionar repetidamente selecciona el bloque contenedor (por ejemplo, el cuerpo de la función, luego la función completa). Esto funciona bien para JavaScript, Python, etc.
- **Selección Inteligente**: Usa `Ctrl+Shift+Flecha derecha` (Windows/Linux) o `Cmd+Shift+Flecha derecha` (Mac) para expandir la selección basada en la sintaxis (puede requerir múltiples pulsaciones para capturar la función completa).
- **Extensión: Select By**: Instala la extensión "Select By" y configura un atajo de teclado (por ejemplo, `Ctrl+K, Ctrl+S`) para seleccionar la función/método contenedor basado en patrones específicos del lenguaje.

**Edición con IA usando GitHub Copilot**:
- Después de seleccionar la función, presiona `Ctrl+I` (Windows/Linux) o `Cmd+I` (Mac) para abrir el chat inline de Copilot. Escribe un prompt como "fix bugs in this function" o "refactor to use arrow functions".
- Alternativamente, haz clic derecho en la selección, elige "Copilot > Fix" o "Copilot > Refactor" para obtener sugerencias de IA.
- En la vista Copilot Chat (`Ctrl+Alt+I`), pega el código seleccionado y pide ediciones (por ejemplo, "optimize this function").

### Cursor AI Code Editor
Cursor, construido sobre VS Code, mejora la selección y la integración con IA:
- **Seleccionar Bloque Contenedor**: Presiona `Ctrl+Shift+.` (Windows/Linux) o `Cmd+Shift+.` (Mac) para expandir la selección a la función/método contenedor, similar a VS Code. La conciencia del modelo de lenguaje de Cursor a menudo hace esto más preciso para lenguajes como Python o TypeScript.
- **Atajos de Teclado Personalizados**: Puedes establecer un atajo personalizado en `settings.json` (por ejemplo, `editor.action.selectToBracket`) para seleccionar el alcance de la función directamente.

**Edición con IA en Cursor**:
- Después de seleccionar la función, presiona `Ctrl+K` (Windows/Linux) o `Cmd+K` (Mac), luego describe los cambios (por ejemplo, "add error handling to this function"). Cursor muestra una vista previa diff de las ediciones generadas por IA.
- Usa `Ctrl+I` para el Modo Agente para corregir u optimizar la función de forma autónoma a través de archivos, con retroalimentación iterativa.
- El Modo Composer (accesible a través de la UI) permite ediciones multi-archivo si la función impacta otras partes del código base.

### IntelliJ IDEA
IntelliJ IDEA ofrece atajos robustos para seleccionar funciones/métodos:
- **Seleccionar Bloque de Código**: Con tu cursor dentro de un método, presiona `Ctrl+W` (Windows/Linux) o `Cmd+W` (Mac) para seleccionar incrementalmente el bloque contenedor. Presionar repetidamente expande la selección a todo el método (incluyendo la firma). Esto funciona en Java, Kotlin, Python, etc.
- **Reducir Selección**: Usa `Ctrl+Shift+W` (Windows/Linux) o `Cmd+Shift+W` (Mac) para reducir la selección si te pasas.
- **Selección Consciente de la Estructura**: Presiona `Ctrl+Alt+Shift+Flecha arriba` (Windows/Linux) o `Cmd+Option+Shift+Flecha arriba` (Mac) para seleccionar el método contenedor directamente a través del árbol de estructura.

**Edición con IA con JetBrains AI Assistant**:
- Después de seleccionar el método, presiona `Alt+Enter` o haz clic derecho y elige "AI Actions" > "Fix with AI" o "Suggest Refactoring". AI Assistant proporciona sugerencias conscientes del contexto en un visor de diferencias (diff).
- Usa el prompt inline (escribe `/` seguido de tu petición, por ejemplo, `/refactor to use streams`, luego presiona `Tab`) para editar el método seleccionado directamente.
- Abre la ventana de herramientas AI Assistant para describir cambios complejos (por ejemplo, "add logging to this method") y aplicar el código generado.

### Resumen
- **VS Code**: Usa `Ctrl+Shift+.` para expandir la selección, luego `Ctrl+I` para ediciones con IA de Copilot.
- **Cursor**: El mismo atajo de selección (`Ctrl+Shift+.`) con `Ctrl+K` para ediciones precisas impulsadas por IA.
- **IntelliJ IDEA**: Usa `Ctrl+W` para una selección rápida de métodos, luego `Alt+Enter` para correcciones con AI Assistant.

IntelliJ tiene el atajo incorporado más preciso para seleccionar métodos (`Ctrl+W`), mientras que la integración de IA de Cursor es la más fluida para editar código seleccionado. VS Code es flexible pero puede requerir extensiones para una selección de funciones más rápida.

Referencias:  
[Code Navigation in Visual Studio Code](https://code.visualstudio.com/docs/editor/editingevolved)  
[Cursor AI: A Guide With 10 Practical Examples](https://www.datacamp.com/tutorial/cursor-ai-code-editor)  
[Code Editing in IntelliJ IDEA](https://www.jetbrains.com/help/idea/working-with-source-code.html)  
[Use AI in editor | IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/use-ai-in-editor.html)