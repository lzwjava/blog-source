---
audio: false
generated: true
image: false
lang: es
layout: post
title: Excluir archivos ignorados en VS Code
translated: true
type: note
---

Puedes hacer que "Ir a Archivo" (Apertura Rápida, Ctrl + P) incluya archivos que están en tu `.gitignore` ajustando tres configuraciones en tu `settings.json`:

1. **Indica a la búsqueda que ignore las reglas de tu `.gitignore`**

   ```jsonc
   "search.useIgnoreFiles": false,      // no respetar .gitignore
   "search.useGlobalIgnoreFiles": false // no respetar tu gitignore global
   ```
2. **Asegúrate de que tus exclusiones globales no oculten esos archivos**
   Por defecto, VS Code hereda todos los patrones de `files.exclude` en `search.exclude`. Si has excluido manualmente directorios del `.gitignore` allí, vuelve a habilitarlos:

   ```jsonc
   "search.exclude": {
     "**/.git": false,          // sí indexar .git (si lo deseas)
     "**/.gitignore": false     // definitivamente no ocultes tu archivo .gitignore en sí
     // …cualquier otro patrón que desees anular
   }
   ```
3. **Recarga la ventana**
   Después de guardar tu configuración de usuario o del espacio de trabajo, ejecuta **Developer: Reload Window** (⇧ ⌘ P → "Reload Window") para que el indexador de archivos recoja el cambio.

Ahora, cuando presiones Ctrl + P, verás *todos* los archivos por nombre, ignorados o no. ([stackoverflow.com][1])

[1]: https://stackoverflow.com/questions/62855190/how-do-you-include-git-ignored-files-in-vscode-quick-search?utm_source=chatgpt.com "How do you include git ignored files in VSCode quick search"