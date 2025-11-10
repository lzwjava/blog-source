---
audio: false
generated: true
image: false
lang: es
layout: post
title: Registro Detallado de Git
translated: true
type: note
---

Para habilitar el registro detallado en Git, puedes usar banderas específicas o variables de entorno dependiendo del comando y del nivel de detalle que necesites. Aquí están los principales enfoques:

1. **Usa la bandera `--verbose` o `-v`**:
   Muchos comandos de Git admiten la bandera `--verbose` (o `-v`) para proporcionar una salida más detallada. Por ejemplo:
   ```bash
   git commit --verbose
   ```
   Esto muestra el diff de los cambios que se están confirmando además de la salida habitual.

2. **Habilita el modo detallado para comandos específicos**:
   - Para `git push`:
     ```bash
     git push --verbose
     ```
     Esto proporciona detalles sobre el proceso de push, incluyendo las referencias que se están enviando y la comunicación con el servidor.
   - Para `git fetch`:
     ```bash
     git fetch --verbose
     ```
     Esto muestra información detallada sobre lo que se está obteniendo.
   - Para `git clone`:
     ```bash
     git clone --verbose <repositorio>
     ```
     Esto muestra el progreso y detalles adicionales durante la clonación.

3. **Establece la variable de entorno `GIT_TRACE`**:
   Para una depuración más profunda, puedes habilitar la salida de traza de Git para ver detalles de bajo nivel de sus operaciones:
   ```bash
   GIT_TRACE=1 git <comando>
   ```
   Esto genera registros detallados sobre los procesos internos de Git, como la ejecución de comandos y las llamadas al sistema.

4. **Habilita niveles de traza específicos**:
   Puedes usar variables de entorno más granulares para aspectos específicos de Git:
   - `GIT_TRACE_CURL`: Habilita el registro detallado para operaciones HTTP (útil para interacciones remotas):
     ```bash
     GIT_TRACE_CURL=1 git <comando>
     ```
   - `GIT_TRACE_PACKET`: Muestra detalles a nivel de paquete para el protocolo de Git:
     ```bash
     GIT_TRACE_PACKET=1 git <comando>
     ```
   - `GIT_TRACE_PERFORMANCE`: Registra datos de rendimiento:
     ```bash
     GIT_TRACE_PERFORMANCE=1 git <comando>
     ```

5. **Aumenta la verbosidad para comandos relacionados con diff**:
   Para comandos como `git diff` o `git log`, puedes usar opciones para obtener más detalles:
   - `git diff --stat` muestra un resumen de los cambios.
   - `git log --verbose` o `git log -p` incluye el diff completo para cada commit.

6. **Configuración global para salida detallada**:
   Puedes configurar Git para que siempre sea detallado para ciertos comandos estableciendo alias o usando opciones de configuración. Por ejemplo:
   ```bash
   git config --global alias.logv "log --verbose"
   ```
   Luego, ejecutar `git logv` siempre incluirá la salida detallada.

**Ejemplo**:
Para ver la salida detallada de una operación de push con traza completa:
```bash
GIT_TRACE=1 git push --verbose
```

**Notas**:
- La salida detallada puede ser abrumadora, especialmente con `GIT_TRACE`, así que úsala cuando estés depurando problemas específicos.
- Consulta las páginas del manual para comandos específicos (por ejemplo, `man git-push`) para ver si admiten `--verbose` u otras banderas de depuración.
- En Windows, usa la misma sintaxis de variable de entorno en el Símbolo del sistema (`set GIT_TRACE=1`) o en PowerShell (`$env:GIT_TRACE=1`).

¡Si necesitas un registro detallado para un comando o escenario específico de Git, házmelo saber y puedo proporcionar un ejemplo a medida!