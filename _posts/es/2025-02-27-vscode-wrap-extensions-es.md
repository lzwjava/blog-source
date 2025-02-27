---
audio: false
lang: es
layout: post
title: Habilitar el ajuste de texto solo para extensiones de archivo específicas
translated: true
---

Asumo que me preguntas cómo configurar Visual Studio Code (VS Code) para habilitar el ajuste de palabras solo para extensiones de archivo específicas. Aquí te dejo cómo hacerlo:

1. **Abrir la configuración de VS Code**:
   - Presiona `Ctrl + ,` (o `Cmd + ,` en macOS) para abrir la configuración, o ve a `Archivo > Preferencias > Configuración`.

2. **Usar el archivo de configuración JSON**:
   - En la interfaz de configuración, haz clic en el ícono `{}` en la esquina superior derecha para abrir el archivo `settings.json`. Esto permite un control más detallado.

3. **Configurar el ajuste de palabras por tipo de archivo**:
   - Agrega una configuración utilizando la sintaxis `"[filetype]": {}` para especificar configuraciones para extensiones de archivo específicas. Por ejemplo, para habilitar el ajuste de palabras solo para archivos `.md` (Markdown) y `.txt` (Texto), puedes agregar algo como esto:

   ```json
   {
       "editor.wordWrap": "off", // Predeterminado: sin ajuste para todos los archivos
       "[markdown]": {
           "editor.wordWrap": "on" // Ajuste solo para archivos .md
       },
       "[plaintext]": {
           "editor.wordWrap": "on" // Ajuste solo para archivos .txt
       }
   }
   ```

4. **Explicación**:
   - `"editor.wordWrap": "off"` establece el valor predeterminado global sin ajuste.
   - `"[markdown]"` y `"[plaintext]"` son identificadores de lenguaje para archivos Markdown y de texto plano, respectivamente. Puedes reemplazarlos con otros identificadores de lenguaje como `[javascript]`, `[python]`, etc., según las extensiones de archivo que desees dirigir.
   - `"editor.wordWrap": "on"` habilita el ajuste para esos tipos de archivo específicos.

5. **Encontrar identificadores de lenguaje**:
   - Si no estás seguro del identificador de lenguaje para una extensión de archivo, abre un archivo de ese tipo en VS Code, haz clic en el modo de lenguaje en la esquina inferior derecha (por ejemplo, "Texto Plano" o "Python") y toma nota del identificador mostrado en el menú de comandos al seleccionar un lenguaje.

6. **Guardar y probar**:
   - Guarda el archivo `settings.json` y VS Code aplicará las configuraciones de inmediato. Abre archivos con diferentes extensiones para confirmar el comportamiento.

Este enfoque asegura que el ajuste de palabras esté habilitado solo para los tipos de archivo que especifiques, dejando a todos los demás sin cambios. ¡Hazme saber si necesitas ayuda con extensiones específicas!