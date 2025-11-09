---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Abrir Sublime Text desde la CLI
translated: true
type: note
---

### Abrir Sublime Text desde la Línea de Comandos (CLI)

Sublime Text no incluye un comando `sublime` (o `subl`) integrado por defecto en macOS (que parece ser el sistema que usas, basado en la referencia a `open -a`). Sin embargo, existe una manera oficial y sencilla de agregarlo usando el script `subl` incluido con Sublime. Esto es más limpio que depender del comando `open`. Te guiaré a través de las opciones a continuación, comenzando con el enfoque recomendado.

#### 1. **Instalar el Comando Oficial `subl` para CLI (Recomendado)**
Sublime Text incluye un ejecutable `subl` en su paquete de aplicación que puedes enlazar simbólicamente a un directorio en tu PATH (como `/usr/local/bin`). Esto te permite ejecutar `subl .` (para abrir el directorio actual) o `subl archivo.txt` desde cualquier lugar en la terminal.

**Pasos para macOS (Sublime Text 3 o 4):**
- Abre Terminal.
- Ejecuta este comando para crear el enlace simbólico (requiere privilegios de administrador, por lo que se te pedirá tu contraseña):
  ```
  sudo ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl
  ```
  - Si estás usando Sublime Text 3, la ruta podría ser ligeramente diferente: `"/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl"` (ajusta el número de versión según sea necesario).
  - Si `/usr/local/bin` no está en tu PATH, agrégalo a tu perfil de shell (por ejemplo, `~/.zshrc` o `~/.bash_profile`):
    ```
    echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```

- Pruébalo: Navega a un directorio (por ejemplo, `cd ~/Desktop`) y ejecuta:
  ```
  subl .
  ```
  Esto debería abrir Sublime Text con la carpeta actual cargada.

Si la ruta del enlace simbólico no funciona (por ejemplo, debido a diferencias de versión), verifica la ubicación exacta:
- Ejecuta `find /Applications/Sublime\ Text.app -name subl` para localizar el binario.

**Por qué esto es bueno:**
- Es oficial y ligero—no se necesitan herramientas de terceros.
- Funciona en todo el sistema, como un CLI real.
- Sublime Text 4 incluso tiene una opción en la consola (View > Show Console) para ejecutar `sublime_installation` o similar, pero el enlace simbólico es el más confiable.

**Si estás en Linux o Windows:**
- Linux: Proceso similar de enlace simbólico—por ejemplo, `sudo ln -s /opt/sublime_text/sublime_text /usr/local/bin/subl`.
- Windows: Agrega `C:\Program Files\Sublime Text\sublime_text.exe` a tu PATH, o usa un archivo por lotes para `subl`.

#### 2. **Alternativa: Usar el Comando `open` (No Requiere Instalación)**
Si no quieres lidiar con enlaces simbólicos o PATH, el comando `open` integrado en macOS funciona bien para uso básico. Ya está disponible en todas partes.

- Para abrir el directorio actual en Sublime:
  ```
  open -a "Sublime Text" .
  ```
  - Nota: Usa `"Sublime Text"` (con espacio) si ese es el nombre de tu aplicación. Si es solo "Sublime.app", ajústalo según corresponda. Puedes verificar el nombre exacto en `/Applications/`.

- Para abrir un archivo específico:
  ```
  open -a "Sublime Text" nombrearchivo.txt
  ```

- Crea un alias para mayor comodidad: Agrega esto a tu perfil de shell (`~/.zshrc` o `~/.bash_profile`) para imitar `subl`:
  ```
  alias subl='open -a "Sublime Text"'
  ```
  Luego recárgalo con `source ~/.zshrc` y usa `subl .` como siempre.

**Pros/Contras:**
- Súper simple y sin configuración.
- Pero es exclusivo de macOS y menos flexible (por ejemplo, no hay una manera fácil de especificar líneas o proyectos como con `subl`).

#### Solución de Problemas
- **¿Comando no encontrado?** Asegúrate de que tu PATH incluya `/usr/local/bin` (ejecuta `echo $PATH` para verificar).
- **¿Aplicación no encontrada?** Verifica que Sublime esté en `/Applications/`. Si está en otro lugar (por ejemplo, via Homebrew: `brew install --cask sublime-text`), ajusta las rutas.
- **¿Problemas de permisos?** El enlace simbólico necesita sudo, pero una vez establecido, está bien.
- Si estás usando un gestor de paquetes como Homebrew, puedes instalar Sublime via `brew install --cask sublime-text`, y podría manejar el CLI por ti.

¡Esto debería ponerte en marcha sin problemas! Si encuentras errores o especificas tu SO/versión, puedo refinar los pasos.