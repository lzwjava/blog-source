---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Usando la Herramienta de Línea de Comandos Subl
translated: true
type: note
---

### Uso del comando `subl` en Sublime Text

¡Buenas noticias—tu CLI `subl` ya está instalado y funcionando (como lo demuestra la salida de `--help`)! Esta es la versión de Sublime Text build 4200 (una versión reciente), y `subl` es la interfaz de línea de comandos oficial para abrir archivos, directorios y más. Es súper versátil para desarrolladores y usuarios avanzados.

Lo desglosaré con ejemplos prácticos. Ejecuta estos desde cualquier directorio en tu terminal. La sintaxis básica es:
```
subl [argumentos] [archivos o directorios]
```

#### 1. **Uso Básico: Abrir Archivos o Directorios**
- **Abrir el directorio actual** (lo carga como un proyecto/carpeta en Sublime):
  ```
  subl .
  ```
  - Esto abre una nueva ventana con el contenido de la carpeta actual.

- **Abrir un archivo específico**:
  ```
  subl miarchivo.txt
  ```
  - Abre `miarchivo.txt` en la ventana predeterminada (o en una nueva si así lo deseas).

- **Abrir múltiples archivos/directorios**:
  ```
  subl archivo1.txt archivo2.js ~/Documents/miproyecto/
  ```
  - Abre todos ellos en Sublime.

- **Abrir en una línea/columna específica** (útil para saltar a errores):
  ```
  subl miarchivo.py:42          # Abre en la línea 42
  subl miarchivo.py:42:5        # Abre en la línea 42, columna 5
  ```

#### 2. **Argumentos Comunes (De la Ayuda)**
Aquí están las banderas más útiles con ejemplos. Combínalas según sea necesario (ej. `subl -n archivo.txt`).

- **`-n` o `--new-window`**: Siempre abre en una ventana nueva.
  ```
  subl -n miarchivo.txt
  ```
  - Útil si quieres mantener tus sesiones existentes de Sublime separadas.

- **`-a` o `--add`**: Añade archivos/carpetas a tu ventana *actual* de Sublime (si ya está abierta).
  ```
  subl -a nuevacarpeta/
  ```
  - Esto no crea una nueva ventana—ideal para construir un espacio de trabajo.

- **`-w` o `--wait`**: Espera a que cierres el/los archivo(s) en Sublime antes de que el comando del terminal finalice.
  ```
  subl -w miarchivo.txt
  ```
  - Útil en scripts (ej., después de ejecutar un build, abrir y esperar la revisión). Implícito cuando se lee desde stdin.

- **`-b` o `--background`**: Abre sin llevar Sublime al primer plano (mantiene el foco en tu terminal).
  ```
  subl -b miarchivo.txt
  ```

- **`-s` o `--stay`**: Mantiene Sublime en foco después de cerrar el archivo (solo relevante con `-w`).
  ```
  subl -w -s miarchivo.txt
  ```
  - Evita que vuelva automáticamente al terminal.

- **`--project <project>`**: Abre un archivo de proyecto específico de Sublime (`.sublime-project`).
  ```
  subl --project MiProyecto.sublime-project
  ```
  - Los proyectos guardan espacios de trabajo, configuraciones, etc. Crea uno mediante File > Save Project en Sublime.

- **`--command <command>`**: Ejecuta un comando de Sublime (ej., una acción de un plugin) sin abrir archivos.
  ```
  subl --command "build"    # Dispara el comando de build si tienes un sistema de build configurado
  ```
  - Revisa la consola de Sublime (View > Show Console) para ver los comandos disponibles.

- **`--launch-or-new-window`**: Solo abre una nueva ventana si Sublime no se está ejecutando.
  ```
  subl --launch-or-new-window .
  ```
  - Eficiente para comprobaciones rápidas sin saturar tu pantalla.

- **Soporte para Stdin** (editar entrada canalizada):
  ```
  echo "Hello World" | subl -   # Abre stdin en Sublime para editar
  subl - > salida.txt          # Edita stdin y guarda los cambios en salida.txt
  ```
  - Después de editar en Sublime, guarda y cierra para continuar.

- **`--safe-mode`**: Inicia Sublime sin plugins ni configuraciones personalizadas (para resolver problemas).
  ```
  subl --safe-mode miarchivo.txt
  ```

- **Otras Banderas**:
  - `-h` o `--help`: Muestra la ayuda que ya viste.
  - `-v` o `--version`: Imprime la versión (ej., `subl -v`).

#### 3. **Consejos para el Uso Diario**
- **Archivos que comienzan con `-`**: Si un nombre de archivo parece una bandera (ej., `-config`), usa `--` para separar:
  ```
  subl -- -config.json
  ```
- **Alias para Conveniencia**: Añade accesos directos a tu perfil de shell (`~/.zshrc` para zsh, o `~/.bash_profile` para bash):
  ```
  alias st='subl'     # Alias más corto
  alias stt='subl -n' # Para nuevas pestañas/ventanas
  ```
  Recarga con `source ~/.zshrc`.
- **En Scripts/GIT**: Úsalo en hooks o alias, ej., `git diff | subl -` para revisar cambios.
- **Vs. `open`**: Ahora que `subl` está configurado, es mejor que `open -a "Sublime Text"` porque soporta líneas, proyectos y más características avanzadas.
- **Resolución de Problemas**:
  - Si `subl` deja de funcionar, vuelve a ejecutar la instalación del enlace simbólico de mi respuesta anterior.
  - Para proyectos grandes, usa `-a` para evitar múltiples ventanas.
  - En macOS, si surgen problemas de enfoque, intenta primero sin `-b`.

¡Esto cubre el 90% de lo que necesitarás! Comienza con `subl .` en una carpeta de proyecto y experimenta. Si tienes un flujo de trabajo específico o un error, comparte más detalles para un consejo personalizado.