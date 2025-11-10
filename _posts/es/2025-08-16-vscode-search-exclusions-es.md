---
audio: false
generated: true
image: false
lang: es
layout: post
title: Personalizar exclusiones de búsqueda en VS Code
translated: true
type: note
---

En VS Code, la búsqueda global de archivos respeta las **exclusiones de búsqueda** que configures. Puedes indicarle que ignore ciertos archivos o carpetas para que no aparezcan en los resultados de búsqueda.

Estas son las principales formas:

---

### 1. Usar `search.exclude` en **settings.json**

Abre tu configuración (`⌘,` / `Ctrl+,` → arriba a la derecha “Abrir configuración (JSON)”) y agrega:

```json
"search.exclude": {
  "**/node_modules": true,
  "**/dist": true,
  "**/*.log": true
}
```

* Las claves son [patrones glob](https://code.visualstudio.com/docs/editor/codebasics#_advanced-search-options).
* `true` significa “excluir de la búsqueda”.
* Ejemplos:

  * `**/node_modules` → todas las carpetas node\_modules
  * `**/*.log` → todos los archivos `.log` en cualquier lugar
  * `**/build/**` → todo lo que esté dentro de carpetas build

---

### 2. Usar `.gitignore`

Si tu proyecto tiene un `.gitignore`, puedes indicarle a VS Code que lo respete durante la búsqueda:

```json
"search.useIgnoreFiles": true
```

De esa manera, cualquier cosa ignorada por Git no aparecerá en los resultados de búsqueda.

---

### 3. Usar `.ignore`

También puedes crear un archivo `.ignore` en la raíz de tu proyecto (con el mismo formato que `.gitignore`) específicamente para las herramientas del editor. VS Code lo respetará si `search.useIgnoreFiles` está habilitado.

---

### 4. Exclusión rápida en la interfaz de búsqueda

Cuando realizas una búsqueda, pasa el cursor sobre un archivo/carpeta en los resultados y haz clic en **“Excluir”**. Esto agrega temporalmente esa ruta a `search.exclude` en la configuración.

---

👉 Por lo tanto, la configuración más común es:

* Agregar exclusiones generales para todo el proyecto en `.gitignore`.
* Agregar exclusiones específicas del editor (como `dist`, `.vscode`) en `search.exclude`.

---

¿Quieres que te muestre cómo **excluir solo durante la búsqueda** pero mantener esos archivos en el Explorador, o también ocultarlos del panel lateral del Explorador?