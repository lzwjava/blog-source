---
audio: false
generated: true
image: false
lang: es
layout: post
title: Extensión de Host de Lanzamiento en VSCode
translated: true
type: note
---

Para presionar **F5** en Visual Studio Code (VSCode) para iniciar el **Extension Development Host** y desarrollar una extensión de VSCode, sigue estos pasos:

1. **Abre tu proyecto de extensión en VSCode**:
   - Asegúrate de tener un proyecto de extensión de VSCode configurado. Esto típicamente incluye un archivo `package.json` con las configuraciones necesarias para la extensión (por ejemplo, `contributes`, `activationEvents`).
   - Abre la carpeta que contiene tu proyecto de extensión en VSCode seleccionando `File > Open Folder` o usando `Ctrl+K, Ctrl+O` (Windows/Linux) o `Cmd+K, Cmd+O` (Mac).

2. **Verifica la configuración de tu extensión**:
   - Asegúrate de tener un archivo `package.json` válido en la raíz de tu proyecto con al menos los siguientes campos:
     ```json
     {
       "name": "your-extension-name",
       "displayName": "Your Extension Name",
       "description": "Description of your extension",
       "version": "0.0.1",
       "engines": {
         "vscode": "^1.60.0"
       },
       "categories": ["Other"],
       "activationEvents": ["*"],
       "main": "./extension.js",
       "contributes": {}
     }
     ```
   - Asegúrate de tener un archivo `extension.js` (o equivalente) como punto de entrada para el código de tu extensión.
   - Instala las dependencias ejecutando `npm install` en la terminal integrada (`Ctrl+``) si tu extensión utiliza módulos de Node.js.

3. **Presiona F5 para iniciar el Extension Development Host**:
   - Presiona **F5** en tu teclado mientras tu proyecto de extensión esté abierto en VSCode.
   - Esto inicia el **Extension Development Host**, una ventana separada de VSCode donde se carga tu extensión para realizar pruebas.
   - VSCode automáticamente:
     - Compilará tu extensión (si usas TypeScript, compila los archivos `.ts` a `.js`).
     - Lanzará una nueva instancia de VSCode con tu extensión activada.
     - Abrirá un depurador adjunto al proceso del Extension Host.

4. **Configuración de depuración**:
   - VSCode utiliza un archivo `launch.json` en la carpeta `.vscode` para configurar la depuración. Si no existe, VSCode lo creará automáticamente cuando presiones F5 por primera vez.
   - Un `launch.json` típico para una extensión se ve así:
     ```json
     {
       "version": "0.2.0",
       "configurations": [
         {
           "name": "Run Extension",
           "type": "extensionHost",
           "request": "launch",
           "args": ["--extensionDevelopmentPath=${workspaceFolder}"],
           "outFiles": ["${workspaceFolder}/out/**/*.js"],
           "preLaunchTask": "npm: watch"
         }
       ]
     }
     ```
   - Asegúrate de que la `preLaunchTask` (si está presente) coincida con una tarea en tu `tasks.json` (por ejemplo, para compilar TypeScript).

5. **Prueba tu extensión**:
   - En la ventana del Extension Development Host, tu extensión debería estar activa. Prueba su funcionalidad (por ejemplo, comandos, contribuciones de UI) según lo definido en tu `package.json` y código.
   - Usa la **Debug Console** en la ventana principal de VSCode para ver los registros o errores de tu extensión.

6. **Solución de problemas**:
   - Si F5 no funciona:
     - Asegúrate de que Node.js y npm estén instalados, ya que son requeridos para el desarrollo de extensiones.
     - Verifica que tengas instaladas las dependencias de la API de Extensión de VSCode (`npm install @types/vscode`).
     - Comprueba que la configuración de `launch.json` apunte a las rutas correctas.
     - Si ves errores, revisa el panel **Output** (selecciona "Extension" en el menú desplegable) en la ventana del Extension Development Host.
   - Si el Extension Host no se inicia, asegúrate de que tu proyecto no tenga errores de sintaxis en `package.json` o en tu archivo de extensión principal.

**Notas adicionales**:
- También puedes iniciar el Extension Development Host abriendo el panel **Run and Debug** (`Ctrl+Shift+D` o `Cmd+Shift+D` en Mac) y seleccionando "Run Extension" del menú desplegable, luego haciendo clic en el botón de reproducción verde.
- Para recargar el Extension Host después de hacer cambios, usa `Ctrl+R` (Windows/Linux) o `Cmd+R` (Mac) en la ventana del Extension Development Host, o reinícialo con F5.

Para más detalles, consulta la guía oficial de desarrollo de extensiones de VSCode:  
[VS Code Extension Development](https://code.visualstudio.com/api/get-started/your-first-extension)