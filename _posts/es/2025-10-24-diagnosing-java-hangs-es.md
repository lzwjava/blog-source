---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Diagnóstico de Bloqueos en Java con jstack
translated: true
type: note
---

### Uso de jstack para Diagnosticar Bloqueos o Aplicaciones Java Atascadas

jstack es una herramienta de línea de comandos incluida en el JDK que genera volcados de hilos (thread dumps) para una Máquina Virtual Java (JVM) en ejecución. Los volcados de hilos capturan el estado de todos los hilos en un momento dado, lo cual es crucial para identificar causas de bloqueos, como interbloqueos (deadlocks), bucles infinitos, E/S bloqueadas u operaciones intensivas de CPU. Es especialmente útil en sistemas Linux/Unix o entornos multiplataforma.

#### Pasos para Usar jstack:
1.  **Identificar el ID de Proceso Java (PID):**
    - Ejecuta `jps` (también parte del JDK) para listar todos los procesos Java:
      ```
      jps -l
      ```
      Esto genera una salida como `12345 MyApp.jar`. Toma nota del PID (ej. 12345).

    - Alternativamente, usa comandos del sistema operativo como `ps aux | grep java` en Linux/macOS.

2.  **Generar un Volcado de Hilos:**
    - Ejecuta jstack con el PID para enviar el volcado a un archivo:
      ```
      jstack <PID> > thread-dump.txt
      ```
      - Reemplaza `<PID>` con tu ID de proceso.
      - Para un volcado más detallado (incluyendo cerrojos), usa `jstack -l <PID> > thread-dump.txt`.
      - Si la JVM no responde a las señales, usa `jhsdb jstack --pid <PID>` (disponible en JDK 8+).

3.  **Capturar Múltiples Volcados para el Análisis:**
    - Los bloqueos a menudo requieren comparación a lo largo del tiempo. Toma de 3 a 5 volcados con intervalos de 10 a 30 segundos:
      ```
      jstack <PID> > dump1.txt
      sleep 10
      jstack <PID> > dump2.txt
      sleep 10
      jstack <PID> > dump3.txt
      ```
      - Automatiza esto en un bucle si es necesario (ej. usando un script bash).

4.  **Analizar el Volcado:**
    - Abre el archivo de texto en un editor o IDE.
    - Busca:
      - **Estados de los Hilos:** Enfócate en hilos en `RUNNABLE` (activo), `BLOCKED` (esperando un cerrojo, posible interbloqueo), `WAITING` (espera inactiva) o `TIMED_WAITING`.
      - **Interbloqueos (Deadlocks):** Busca "deadlock" o usa herramientas como `jstack -l` que los marcan.
      - **Trazas de Pila (Stack Traces):** Identifica patrones repetitivos o hilos atascados en métodos específicos (ej. un bucle infinito).
      - **Marcos Nativos (Native Frames):** Si los hilos están atascados en código nativo, podría indicar problemas con JNI o bloqueos a nivel del sistema operativo.
    - Herramientas para un análisis más profundo: VisualVM, Eclipse MAT, o analizadores en línea como fastThread.io. Por ejemplo, en VisualVM, carga el archivo de volcado en la pestaña "Thread" para visualizar cerrojos y estados.

Si la JVM no responde (ej. no hay salida de `kill -3 <PID>` en Unix), el bloqueo podría estar a nivel del sistema operativo—considera realizar volcados completos de memoria (core dumps) mediante `gcore <PID>`.

### Uso de ProcDump para Diagnosticar Bloqueos o Procesos Atascados

ProcDump es una herramienta gratuita de Sysinternals para Windows que crea volcados de memoria o CPU de procesos. Es excelente para capturar instantáneas de bloqueos en cualquier aplicación (incluyendo Java), especialmente cuando el proceso no responde. Úsalo para obtener volcados completos de memoria y analizarlos con herramientas como WinDbg o Visual Studio.

#### Pasos para Usar ProcDump:
1.  **Descargar y Configurar:**
    - Obtén ProcDump desde el sitio de Microsoft Sysinternals (procdump.exe).
    - Ejecuta el Símbolo del sistema (Command Prompt) como Administrador.
    - Navega a la carpeta que contiene procdump.exe.

2.  **Identificar el Proceso:**
    - Usa el Administrador de tareas o `tasklist | findstr <nombre-del-proceso>` para obtener el PID o el nombre de la imagen (ej. `java.exe`).

3.  **Capturar un Volcado por Bloqueo:**
    - Para un volcado completo de memoria inmediato (útil para procesos atascados):
      ```
      procdump -ma <nombre-del-proceso-o-PID>
      ```
      - `-ma`: Volcado completo de memoria (incluye todos los hilos y el heap).
      - Ejemplo: `procdump -ma java.exe` o `procdump -ma 12345`.

    - Para detección automática de bloqueos (se activa por falta de respuesta):
      ```
      procdump -h <nombre-del-proceso-o-PID> -o
      ```
      - `-h`: Monitorea bloqueos (proceso no responde a mensajes de ventana por más de 5 segundos; para servicios sin ventanas, usa umbrales de CPU como `-h 80` para 80% de CPU).
      - `-o`: Sobrescribe volcados existentes.
      - Para servicios: Combina con `-e` para excepciones o monitorea la CPU: `procdump -c 80 -h <servicio-exe>`.

    - Toma múltiples volcados: Añade `-n 3` para 3 volcados en intervalos (ej. `-t 10` para un retraso de 10 segundos):
      ```
      procdump -ma -n 3 -t 10 <PID>
      ```

4.  **Analizar el Volcado:**
    - Los volcados se guardan como archivos `.dmp` en el directorio actual.
    - Ábrelos en WinDbg (gratuito de Microsoft) o Visual Studio Debugger.
    - Comandos clave en WinDbg:
      - `!threads`: Lista hilos y estados (busca los bloqueados/en espera).
      - `~<id-hilo>s`: Cambia a un hilo y usa `k` para la traza de pila.
      - `!analyze -v`: Auto-analiza en busca de bloqueos/interbloqueos.
    - Para análisis específicos de Java, carga el volcado en Eclipse MAT o usa `jhat` en un volcado del heap (si se capturó con la bandera `-mh`).

ProcDump funciona bien para procesos no interactivos como servicios; si el bloqueo está relacionado con la CPU, usa `-c` para activarse con un uso alto de CPU.

### Consejos Generales para Ambas Herramientas
- **Seguridad:** Los volcados pueden ser grandes (GBs para memoria completa); asegura espacio en disco.
- **Combina Herramientas:** Para Java en Windows, usa jstack primero (más ligero), luego ProcDump para obtener información más profunda a nivel del sistema operativo.
- **Prevención:** Habilita banderas de la JVM como `-XX:+PrintGCDetails` para registro, o usa agentes como JFR para profiling.
- Si los volcados no muestran un problema claro, verifica los recursos del sistema (CPU, memoria, E/S) con herramientas como `top` o el Monitor de rendimiento.

[Guía de Resolución de Problemas de Oracle Java](https://docs.oracle.com/en/java/javase/17/troubleshoot/troubleshoot-process-hangs-and-loops.html)  
[Tomar un Volcado por Bloqueo con ProcDump](https://www.poppastring.com/blog/taking-a-hang-dump-or-crash-dump-with-procdump)  
[Análisis de Volcados de Hilos Java](https://www.baeldung.com/java-analyze-thread-dumps)  
[Uso de ProcDump para Bloqueos](https://learn.microsoft.com/en-us/sysinternals/downloads/procdump)