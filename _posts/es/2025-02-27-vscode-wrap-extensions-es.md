---
audio: true
lang: es
layout: post
title: Habilitar el ajuste de texto solo para extensiones de archivo específicas
translated: true
---

Supongo que estás preguntando cómo configurar Visual Studio Code (VS Code) para habilitar el ajuste de línea solo para extensiones de archivo específicas. Aquí te dejo cómo hacerlo:

1. **Abrir la configuración de VS Code**:
   - Presiona `Ctrl + ,` (o `Cmd + ,` en macOS) para abrir la configuración, o ve a `File > Preferences > Settings`.

2. **Usar el archivo de configuración JSON**:
   - En la interfaz de configuración, haz clic en el ícono `{}` en la esquina superior derecha para abrir el archivo `settings.json`. Esto permite un control más detallado.

3. **Configurar el ajuste de línea por tipo de archivo**:
   - Agrega una configuración usando la sintaxis `"[filetype]": {}` para especificar configuraciones para extensiones de archivo específicas. Por ejemplo, para habilitar el ajuste de línea solo para archivos `.md` (Markdown) y `.txt` (Texto), puedes agregar algo como esto:

   ```json
   {
       "editor.wordWrap": "off", // Predeterminado: sin ajuste de línea para todos los archivos
       "[markdown]": {
           "editor.wordWrap": "on" // Ajuste de línea solo para archivos .md
       },
       "[plaintext]": {
           "editor.wordWrap": "on" // Ajuste de línea solo para archivos .txt
       }
   }
   ```

4. **Explicación**:
   - `"editor.wordWrap": "off"` establece el valor predeterminado global sin ajuste de línea.
   - `"[markdown]"` y `"[plaintext]"` son identificadores de lenguaje para archivos Markdown y texto plano, respectivamente. Puedes reemplazarlos con otros identificadores de lenguaje como `[javascript]`, `[python]`, etc., según las extensiones de archivo que desees dirigir.
   - `"editor.wordWrap": "on"` habilita el ajuste de línea para esos tipos de archivo específicos.

5. **Encontrar identificadores de lenguaje**:
   - Si no estás seguro del identificador de lenguaje para una extensión de archivo, abre un archivo de ese tipo en VS Code, haz clic en el modo de lenguaje en la esquina inferior derecha (por ejemplo, "Texto Plano" o "Python") y toma nota del identificador mostrado en la paleta de comandos al seleccionar un lenguaje.

6. **Guardar y probar**:
   - Guarda el archivo `settings.json` y VS Code aplicará las configuraciones inmediatamente. Abre archivos con diferentes extensiones para confirmar el comportamiento.

Este enfoque asegura que el ajuste de línea esté habilitado solo para los tipos de archivo que especifiques, dejando a todos los demás sin cambios. ¡Hazme saber si necesitas ayuda con extensiones específicas!

---

Si estás trabajando con archivos `.log` en Visual Studio Code y quieres habilitar el ajuste de línea específicamente para ellos, necesitarás asegurarte de que VS Code reconozca estos archivos como un modo de lenguaje distinto. Por defecto, los archivos `.log` pueden no tener un identificador de lenguaje único como `[log]`—a menudo se tratan como texto plano (`[plaintext]`). Sin embargo, puedes configurar este comportamiento. Aquí te dejo cómo hacerlo:

### Opción 1: Usar `[plaintext]` si los archivos `.log` son texto plano
Si tus archivos `.log` están siendo reconocidos como texto plano (verifica el modo de lenguaje en la esquina inferior derecha de VS Code cuando un archivo `.log` está abierto), puedes simplemente usar `[plaintext]`:

```json
{
    "editor.wordWrap": "off", // Predeterminado: sin ajuste de línea
    "[plaintext]": {
        "editor.wordWrap": "on" // Habilitar para archivos .txt y .log (si se reconocen como texto plano)
    }
}
```

- **Nota**: Esto se aplicará a todos los archivos de texto plano (por ejemplo, `.txt`, `.log`), no solo a los archivos `.log`. Si eso es demasiado amplio, pasa a la Opción 2.

### Opción 2: Asociar archivos `.log` con un modo de lenguaje personalizado
Si quieres que `[log]` funcione como un identificador específico, necesitas decirle a VS Code que asocie los archivos `.log` con un modo de lenguaje "Log". Aquí te dejo cómo:

1. **Instalar una extensión de archivo de registro (opcional)**:
   - Instala una extensión como "Log File Highlighter" desde el mercado de VS Code. Esta extensión a menudo asigna a los archivos `.log` un modo de lenguaje específico (por ejemplo, `log`).
   - Después de instalar, verifica el modo de lenguaje para un archivo `.log` (esquina inferior derecha). Si dice "Log" o algo similar, puedes usar `[log]` directamente.

2. **Asociar manualmente archivos `.log`**:
   - Si no quieres una extensión, puedes asociar manualmente `.log` con un modo de lenguaje a través de `files.associations` en `settings.json`:
   ```json
   {
       "files.associations": {
           "*.log": "log" // Asocia .log con el modo de lenguaje "log"
       },
       "editor.wordWrap": "off", // Predeterminado: sin ajuste de línea
       "[log]": {
           "editor.wordWrap": "on" // Habilitar solo para archivos .log
       }
   }
   ```
   - **Caveat**: El modo de lenguaje `log` debe existir (por ejemplo, proporcionado por una extensión o VS Code). Si no existe, VS Code podría revertir a texto plano y `[log]` no funcionará como se espera sin una mayor personalización.

3. **Verificar el modo de lenguaje**:
   - Abre un archivo `.log`, haz clic en el modo de lenguaje en la esquina inferior derecha y observa a qué está configurado. Si es `log` después de tus cambios, `[log]` funcionará. Si sigue siendo `plaintext`, usa `[plaintext]` o ajusta la asociación.

### Opción 3: Ajustar con patrones de archivo (más preciso)
Para un control total, puedes usar la configuración `"files.associations"` para dirigir archivos `.log` específicamente y luego confiar en un modo de lenguaje de respaldo como `plaintext` solo para `.log`:

```json
{
    "files.associations": {
        "*.log": "plaintext" // Forzar archivos .log a tratarse como texto plano
    },
    "editor.wordWrap": "off", // Predeterminado: sin ajuste de línea
    "[plaintext]": {
        "editor.wordWrap": "on" // Habilitar para .log (y .txt, si lo deseas)
    }
}
```

- **Para excluir `.txt`**: Si quieres que `.log` pero no `.txt` se ajuste, necesitarás una extensión personalizada o una configuración más avanzada (por ejemplo, una extensión de VS Code para definir un modo `log` único), ya que VS Code no distingue `.log` de `.txt` sin una configuración adicional.

### Probar `[log]` directamente
Si no estás seguro de si `[log]` funciona de inmediato (debido a una extensión o el comportamiento integrado de VS Code), intenta esto:

```json
{
    "editor.wordWrap": "off",
    "[log]": {
        "editor.wordWrap": "on"
    }
}
```

Abre un archivo `.log` y verifica si el ajuste de línea se aplica. Si no, el modo de lenguaje no es `log` y necesitarás usar una de las opciones anteriores.

### Recomendación
- **Más simple**: Usa `[plaintext]` si estás de acuerdo con que `.txt` y `.log` ambos se ajusten.
- **Específico**: Instala una extensión "Log File Highlighter", confirma que el modo es `log` y usa `[log]`.
- ¡Hazme saber qué modo de lenguaje muestran tus archivos `.log` y puedo afinar la solución aún más!

---

Probé la configuración a continuación y funciona muy bien.

```json
   {
       "editor.wordWrap": "off", // Predeterminado: sin ajuste de línea
       "[log]": {
           "editor.wordWrap": "on" // Habilitar solo para archivos .log
       }
   }
```