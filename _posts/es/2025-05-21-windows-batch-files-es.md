---
audio: false
generated: true
lang: es
layout: post
title: Escribir Archivos Por Lotes De Windows
translated: true
type: note
---

Un archivo por lotes de Windows (.bat o .cmd) es un archivo de script que contiene una serie de comandos ejecutados por el Símbolo del sistema de Windows (cmd.exe). Los archivos por lotes automatizan tareas repetitivas, gestionan operaciones del sistema o ejecutan programas. A continuación se presenta una introducción completa para escribir archivos por lotes de Windows, cubriendo su propósito, sintaxis, comandos comunes y mejores prácticas.

### ¿Qué es un Archivo por Lotes?
Un archivo por lotes es un archivo de texto plano con extensión `.bat` o `.cmd` que contiene comandos interpretados por el Símbolo del sistema de Windows. Cuando se ejecuta, los comandos se ejecutan secuencialmente, permitiendo la automatización de tareas como gestión de archivos, configuración del sistema o instalación de software.

### ¿Por Qué Usar Archivos por Lotes?
- **Automatización**: Ejecuta múltiples comandos con un solo script.
- **Sencillez**: No se requieren conocimientos avanzados de programación.
- **Gestión del Sistema**: Realiza tareas como copias de seguridad, gestión de usuarios o configuración del entorno.
- **Compatibilidad**: Funciona en todas las versiones de Windows con Símbolo del sistema.

### Crear un Archivo por Lotes
1. **Escribir el Script**: Usa un editor de texto (p. ej., Notepad, VS Code) para escribir los comandos.
2. **Guardar con la Extensión Correcta**: Guarda el archivo con una extensión `.bat` o `.cmd` (p. ej., `script.bat`).
3. **Ejecutar**: Haz doble clic en el archivo o ejecútalo mediante el Símbolo del sistema.

### Sintaxis y Estructura Básica
- **Comandos**: Los archivos por lotes usan comandos del Símbolo del sistema (p. ej., `dir`, `copy`, `del`) y comandos específicos por lotes (p. ej., `echo`, `set`, `goto`).
- **Comentarios**: Usa `REM` o `::` para añadir comentarios para mayor claridad.
- **Insensibilidad a Mayúsculas**: Los comandos y las variables no distinguen entre mayúsculas y minúsculas.
- **Ejecución por Línea**: Los comandos se ejecutan línea por línea a menos que se controlen con comandos de flujo como `if`, `for` o `goto`.

### Comandos y Características Comunes
#### 1. **Comandos Básicos**
- `ECHO`: Controla el eco de comandos o muestra texto.
  - Ejemplo: `ECHO ¡Hola, Mundo!` muestra "¡Hola, Mundo!".
  - `ECHO OFF`: Suprime la visualización de comandos durante la ejecución.
- `CLS`: Limpia la pantalla del Símbolo del sistema.
- `PAUSE**: Pausa la ejecución, esperando la entrada del usuario.
- `EXIT`: Termina el script o la sesión del Símbolo del sistema.

#### 2. **Variables**
- **Establecer Variables**: Usa `SET` para crear o modificar variables.
  - Ejemplo: `SET MI_VAR=Hola` crea una variable `MI_VAR`.
- **Usar Variables**: Referencia con `%NOMBRE_VARIABLE%`.
  - Ejemplo: `ECHO %MI_VAR%` muestra "Hola".
- **Variables de Entorno**: Variables integradas como `%PATH%`, `%USERNAME%` o `%DATE%`.

#### 3. **Entrada y Salida**
- **Entrada del Usuario**: Usa `SET /P` para solicitar entrada.
  - Ejemplo: `SET /P NOMBRE=Ingresa tu nombre: ` almacena la entrada del usuario en `NOMBRE`.
- **Redirigir Salida**: Usa `>` para escribir la salida en un archivo o `>>` para añadir.
  - Ejemplo: `DIR > listado_archivos.txt` guarda el listado del directorio en `listado_archivos.txt`.

#### 4. **Sentencias Condicionales**
- Usa `IF` para ejecutar comandos basados en condiciones.
  - Sintaxis: `IF condición comando [ELSE comando]`
  - Ejemplo: `IF "%NOMBRE%"=="Admin" ECHO Bienvenido, Admin! ELSE ECHO Acceso denegado.`

#### 5. **Bucles**
- **Bucle FOR**: Itera sobre archivos, directorios o valores.
  - Ejemplo: `FOR %i EN (*.txt) DO ECHO %i` lista todos los archivos `.txt`.
  - Nota: En archivos por lotes, usa `%%i` en lugar de `%i` para variables.
- **Bucles tipo WHILE**: Simula con `GOTO` e `IF`.

#### 6. **Subrutinas y Etiquetas**
- **Etiquetas**: Usa `:etiqueta` para marcar una sección de código.
- **GOTO**: Salta a una sección etiquetada.
  - Ejemplo: `GOTO :EOF` salta al final del archivo.
- **CALL**: Invoca otro archivo por lotes o subrutina.
  - Ejemplo: `CALL :miSubrutina` ejecuta una subrutina etiquetada.

#### 7. **Manejo de Errores**
- Verifica el éxito del comando con `%ERRORLEVEL%`.
  - Ejemplo: `IF %ERRORLEVEL% NEQ 0 ECHO El comando falló.`

### Mejores Prácticas
- **Usar `ECHO OFF`**: Reduce el desorden ocultando la salida de comandos.
- **Añadir Comentarios**: Usa `REM` o `::` para documentar el código.
- **Probar Incrementalmente**: Ejecuta secciones pequeñas para depurar.
- **Manejar Errores**: Verifica `%ERRORLEVEL%` para fallos.
- **Usar Comillas para Rutas**: Encierra las rutas de archivos entre comillas para manejar espacios (p. ej., `"C:\Archivos de Programa\"`).
- **Evitar Nombres Reservados**: No uses nombres como `CON`, `NUL` o `PRN` para archivos o variables.
- **Usar `@` para Silenciar**: Prefija comandos con `@` para suprimir el eco de comandos individuales (p. ej., `@ECHO OFF`).

### Ejemplo de Archivo por Lotes
A continuación se muestra un archivo por lotes de ejemplo que demuestra características comunes: solicitar entrada del usuario, crear un directorio y registrar la salida.

@echo off
REM Archivo por lotes de ejemplo para crear un directorio y registrar acciones
ECHO Iniciando script...

:: Solicitar nombre del directorio
SET /P NOMBREDIR=Ingresa el nombre del directorio: 

:: Verificar si la entrada está vacía
IF "%NOMBREDIR%"=="" (
    ECHO Error: No se proporcionó nombre de directorio.
    PAUSE
    EXIT /B 1
)

:: Crear directorio y registrar resultado
MKDIR "%NOMBREDIR%"
IF %ERRORLEVEL%==0 (
    ECHO Directorio "%NOMBREDIR%" creado exitosamente.
    ECHO %DATE% %TIME%: Directorio "%NOMBREDIR%" creado >> log.txt
) ELSE (
    ECHO Falló al crear el directorio "%NOMBREDIR%".
    ECHO %DATE% %TIME%: Falló al crear el directorio "%NOMBREDIR%" >> log.txt
)

::mettere:PAUSE
ECHO Hecho.
EXIT /B

### Ejecutar el Archivo por Lotes
- Guarda el código anterior como `ejemplo.bat`.
- Haz doble clic o ejecuta mediante el Símbolo del sistema (`cmd.exe /c ejemplo.bat`).

### Consejos Avanzados
- **Expansión Retardada**: Usa `SETLOCAL EnableDelayedExpansion` para variables actualizadas en bucles (p. ej., `!VAR!` en lugar de `%VAR%`).
- **Niveles de Error**: Prueba comandos con `IF ERRORLEVEL n` para códigos de salida específicos.
- **Herramientas Externas**: Integra herramientas como `PowerShell` o `curl` para funcionalidad avanzada.
- **Seguridad**: Evita ejecutar archivos por lotes de fuentes no confiables para prevenir código malicioso.

### Limitaciones
- **Complejidad**: Los archivos por lotes son menos potentes que PowerShell o Python para tareas complejas.
- **Manejo de Errores**: Limitado en comparación con lenguajes de scripting modernos.
- **Multiplataforma**: Los archivos por lotes son específicos de Windows.

### Recursos
- **Documentación Oficial**: Referencia de Símbolo del sistema de Microsoft (comando `help` en cmd.exe).
- **Tutoriales**: Sitios web como SS64.com proporcionan referencias detalladas de comandos.
- **Comunidad**: Busca ejemplos de archivos por lotes en X o foros como Stack Overflow.

Esta introducción proporciona una base para escribir archivos por lotes. Practica con scripts simples y explora comandos mediante `help` en el Símbolo del sistema para expandir tus habilidades.