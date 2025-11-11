---
audio: false
generated: true
lang: es
layout: post
title: Descarga de VSIX para VS Code
translated: true
type: note
---

Para descargar manualmente un archivo `.vsix` para una extensión de Visual Studio Code (VS Code), puedes usar Visual Studio Marketplace, que aloja todas las extensiones oficiales. El archivo `.vsix` es el formato empaquetado para las extensiones de VS Code, y aunque el Marketplace no siempre proporciona un botón de descarga directa, puedes construir la URL de descarga o usar métodos alternativos. Aquí te explicamos cómo hacerlo paso a paso:

### Pasos para Descargar Manualmente un Archivo `.vsix`

1.  **Encuentra la Extensión en Visual Studio Marketplace**
    - Ve a [Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode) en tu navegador web.
    - Busca la extensión que deseas (por ejemplo, "Python" de Microsoft, "Prettier - Code formatter", etc.).
    - Abre la página de la extensión. Por ejemplo, la URL de la extensión Python podría verse así:
      `https://marketplace.visualstudio.com/items?itemName=ms-python.python`.

2.  **Identifica el Publicador y el Nombre de la Extensión**
    - En la página de la extensión, toma nota del **publicador** y el **identificador de la extensión**. Estos forman parte de la URL o se muestran en la página.
    - Por ejemplo, en `ms-python.python`, `ms-python` es el publicador y `python` es el nombre de la extensión.

3.  **Construye la URL de Descarga**
    - El archivo `.vsix` se puede descargar directamente usando un patrón de URL específico proporcionado por el Marketplace. El formato general es:
      ```
      https://<publisher>.gallery.vsassets.io/_apis/public/gallery/publisher/<publisher>/extension/<extension-name>/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
      ```
    - Reemplaza `<publisher>` con el nombre del publicador y `<extension-name>` con el nombre de la extensión.
    - Para la extensión Python (`ms-python.python`), la URL sería:
      ```
      https://ms-python.gallery.vsassets.io/_apis/public/gallery/publisher/ms-python/extension/python/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
      ```
    - Pega esta URL en tu navegador, y se activará la descarga del archivo `.vsix`.

4.  **Alternativa: Usar el Enlace "Descargar Extensión" en la Página del Marketplace (si está disponible)**
    - Algunas páginas de extensiones incluyen un enlace "Descargar Extensión" en la sección **Recursos** o en otro lugar. Si está presente, haz clic en él para descargar el archivo `.vsix` directamente. Sin embargo, esto es menos común, por lo que el método de la URL es más confiable.

5.  **Verifica la Descarga**
    - El archivo descargado tendrá una extensión `.vsix` (por ejemplo, `ms-python.python-<version>.vsix`).
    - Verifica el tamaño y el nombre del archivo para asegurarte de que coincida con la extensión y la versión que esperas.

6.  **Instalar el Archivo `.vsix` en VS Code (Opcional)**
    - Abre VS Code.
    - Ve a la vista de Extensiones (`Ctrl+Shift+X` o `Cmd+Shift+X` en macOS).
    - Haz clic en el menú de tres puntos (`...`) en la parte superior derecha del panel de Extensiones.
    - Selecciona **Instalar desde VSIX**, luego navega y selecciona el archivo `.vsix` descargado.

### Ejemplo Práctico
Digamos que quieres la extensión **ESLint** de Dirk Baeumer:
- URL del Marketplace: `https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint`
- Publicador: `dbaeumer`
- Nombre de la extensión: `vscode-eslint`
- URL de descarga:
  ```
  https://dbaeumer.gallery.vsassets.io/_apis/public/gallery/publisher/dbaeumer/extension/vscode-eslint/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
  ```
- Abre esta URL en tu navegador, y el archivo `.vsix` (por ejemplo, `dbaeumer.vscode-eslint-<version>.vsix`) se descargará.

### Notas
-   **Versión**: La parte `/latest/` de la URL garantiza que obtengas la versión más reciente. Si necesitas una versión específica, normalmente necesitarás acceso al número de versión (visible en la pestaña "Historial de versiones" del Marketplace) y podrías necesitar ajustar la URL o usar una herramienta como `ovsx` (ver más abajo), aunque la API del Marketplace no siempre expone versiones anteriores fácilmente mediante URL directa.
-   **Descargas Bloqueadas**: Si la URL no funciona, el publicador podría restringir el acceso directo, o tu navegador/red podría bloquearlo. En tales casos, prueba con un navegador diferente o un administrador de descargas.
-   **Herramientas Alternativas**: Puedes usar una herramienta de línea de comandos como `ovsx` (del Open VSX Registry) para descargar extensiones. Instálalo via npm (`npm install -g ovsx`), luego ejecuta:
    ```
    ovsx download ms-python.python
    ```
    Esto descarga el archivo `.vsix` de manera programática.

### Respuesta Final
Para descargar manualmente un archivo `.vsix` para una extensión de VS Code:
1.  Ve a la página de la extensión en [Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode).
2.  Identifica el publicador y el nombre de la extensión (por ejemplo, `ms-python.python`).
3.  Usa este formato de URL en tu navegador:
    ```
    https://<publisher>.gallery.vsassets.io/_apis/public/gallery/publisher/<publisher>/extension/<extension-name>/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
    ```
4.  Descarga el archivo `.vsix` y opcionalmente instálalo en VS Code.