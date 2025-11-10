---
audio: false
generated: true
lang: es
layout: post
title: VSCode Pico-W-Go para MicroPython
translated: true
type: note
---

Utilizar la extensión **Raspberry Pi Pico** en Visual Studio Code (VSCode) es una excelente opción para el desarrollo con MicroPython en tu Raspberry Pi Pico, ya que proporciona un flujo de trabajo optimizado similar a Thonny pero dentro del potente entorno de edición de VSCode. La extensión a la que probablemente te refieres es **Pico-W-Go** (o una extensión similar como **Pico-Go**), que está específicamente diseñada para el desarrollo con Raspberry Pi Pico y Pico W usando MicroPython. A continuación, te guiaré a través de la configuración y el uso de la extensión **Pico-W-Go** (la opción más popular y mantenida) para cargar un programa simple de MicroPython en tu Pico, asumiendo que MicroPython ya está instalado (a partir del archivo `RPI_PICO-20250415-v1.25.0.uf2` que usaste).

---

### Prerrequisitos
1.  **MicroPython Instalado**: Tu Pico tiene MicroPython instalado, como ya has indicado.
2.  **VSCode Instalado**: Asegúrate de tener VSCode instalado ([code.visualstudio.com](https://code.visualstudio.com)).
3.  **Python Instalado**: Requerido para las dependencias de Pico-W-Go:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
4.  **Conexión USB**: El Pico está conectado mediante un cable USB con capacidad de transferencia de datos.

---

### Guía Paso a Paso para Usar la Extensión Raspberry Pi Pico (Pico-W-Go) en VSCode

1.  **Instalar la Extensión Pico-W-Go**:
    - Abre VSCode.
    - Ve a la vista de Extensiones (`Ctrl+Shift+X` o `Cmd+Shift+X` en macOS).
    - Busca **Pico-W-Go** e instálala (desarrollada por Paul Obermeier y otros).
    - Nota: Si te referías a otra extensión (por ejemplo, Pico-Go), házmelo saber, pero Pico-W-Go es la más comúnmente utilizada para el desarrollo con MicroPython en Pico.

2.  **Instalar las Dependencias de Pico-W-Go**:
    - Pico-W-Go requiere `pyserial` y `esptool` para la comunicación serial y la instalación de firmware:
      ```bash
      pip3 install pyserial esptool
      ```
    - Asegúrate de que estén instalados en tu entorno de Python (usa `pip3 list` para verificar).

3.  **Configurar Pico-W-Go**:
    - Abre la Paleta de Comandos en VSCode (`Ctrl+Shift+P` o `Cmd+Shift+P`).
    - Escribe y selecciona **Pico-W-Go > Configure Project**.
    - Sigue las indicaciones:
      - **Puerto Serial**: Selecciona el puerto del Pico (por ejemplo, `/dev/ttyACM0`). Encuéntralo ejecutando:
        ```bash
        ls /dev/tty*
        ```
        Busca `/dev/ttyACM0` o similar, que aparece cuando el Pico está conectado.
      - **Intérprete**: Elige MicroPython (Raspberry Pi Pico).
      - **Carpeta del Proyecto**: Selecciona o crea una carpeta para tu proyecto (por ejemplo, `~/PicoProjects/MiProyecto`).
    - Pico-W-Go crea un archivo de configuración `.picowgo` en tu carpeta de proyecto para almacenar los ajustes.

4.  **Escribir un Programa Simple de MicroPython**:
    - En VSCode, abre tu carpeta de proyecto (Archivo > Abrir Carpeta).
    - Crea un nuevo archivo llamado `main.py` (MicroPython ejecuta `main.py` automáticamente al arrancar).
    - Añade un programa simple, por ejemplo, para hacer parpadear el LED integrado:
      ```python
      from machine import Pin
      import time

      led = Pin(25, Pin.OUT)  # Usa "LED" para Pico W
      while True:
          led.on()
          time.sleep(0.5)
          led.off()
          time.sleep(0.5)
      ```
    - Guarda el archivo (`Ctrl+S`).

5.  **Cargar el Programa al Pico**:
    - Asegúrate de que el Pico esté conectado y el puerto correcto seleccionado (vuelve a ejecutar **Pico-W-Go > Configure Project** si es necesario).
    - Abre la Paleta de Comandos (`Ctrl+Shift+P`).
    - Selecciona **Pico-W-Go > Upload Project to Pico**.
      - Esto carga todos los archivos en tu carpeta de proyecto (por ejemplo, `main.py`) al sistema de archivos del Pico.
    - Alternativamente, para cargar un solo archivo:
      - Haz clic derecho en `main.py` en el explorador de archivos de VSCode.
      - Selecciona **Pico-W-Go > Upload File to Pico**.
    - El archivo se transfiere al Pico, y si es `main.py`, se ejecutará automáticamente al arrancar.

6.  **Ejecutar y Probar el Programa**:
    - **Ejecución Automática**: Si cargaste `main.py`, reinicia el Pico (desconéctalo y vuelve a conectarlo, o presiona el botón RESET si está disponible). El LED debería empezar a parpadear.
    - **Ejecución Manual**:
      - Abre la Paleta de Comandos y selecciona **Pico-W-Go > Run**.
      - Esto ejecuta el archivo actual en el Pico.
    - **Usar el REPL**:
      - Abre la Paleta de Comandos y selecciona **Pico-W-Go > Open REPL**.
      - El REPL aparece en la terminal de VSCode, donde puedes probar comandos:
        ```python
        from machine import Pin
        led = Pin(25, Pin.OUT)
        led.on()
        ```
      - Presiona `Ctrl+C` para detener un programa en ejecución en el REPL.

7.  **Gestionar Archivos en el Pico**:
    - **Listar Archivos**: Usa **Pico-W-Go > Download Project from Pico** para ver o recuperar archivos del sistema de archivos del Pico.
    - **Eliminar Archivos**: Abre la Paleta de Comandos y selecciona **Pico-W-Go > Delete All Files** para limpiar el sistema de archivos del Pico, o usa el REPL:
      ```python
      import os
      os.remove('main.py')
      ```
    - **Ver la Salida**: La salida del programa (por ejemplo, sentencias `print`) aparece en el REPL o en la terminal de VSCode si está configurado.

---

### Resolución de Problemas
-   **Puerto No Detectado**:
    - Ejecuta `ls /dev/tty*` para confirmar el puerto del Pico (por ejemplo, `/dev/ttyACM0`).
    - Asegúrate de que el cable USB admita transferencia de datos y prueba un puerto diferente.
    - Reconfigura el puerto en **Pico-W-Go > Configure Project**.
-   **Falla la Carga**:
    - Verifica que `pyserial` y `esptool` estén instalados (`pip3 list`).
    - Comprueba que MicroPython esté ejecutándose (debería ser accesible el REPL).
    - Reinstala MicroPython si es necesario volviendo al modo BOOTSEL y copiando el archivo `.uf2`.
-   **El LED No Parpadea**:
    - Confirma el pin GPIO correcto (`25` para Pico, `"LED"` para Pico W).
    - Prueba en el REPL:
      ```python
      from machine import Pin
      led = Pin(25, Pin.OUT)
      led.on()
      ```
-   **Faltan Comandos de Pico-W-Go**: Asegúrate de que la extensión esté instalada y activada. Reinicia VSCode si es necesario.

---

### Ventajas de Pico-W-Go en VSCode
-   **Flujo de Trabajo Integrado**: Combina edición de código, gestión de archivos y acceso al REPL en VSCode.
-   **Características Avanzadas**: Aprovecha la integración con Git, extensiones y personalización de VSCode.
-   **Multiplataforma**: Funciona en Linux, Windows y macOS.

### Limitaciones en Comparación con Thonny
-   La configuración es un poco más compleja (por ejemplo, instalar `pyserial`, configurar el puerto).
-   La integración del REPL puede parecer menos fluida que la interfaz todo en uno de Thonny.
-   Menos amigable para principiantes que usan MicroPython por primera vez.

---

### Extensiones Alternativas
Si te referías a otra extensión (por ejemplo, **Pico-Go**), ten en cuenta que Pico-Go es una alternativa más antigua a Pico-W-Go y puede tener menos funciones o actualizaciones. La configuración es similar, pero se recomienda Pico-W-Go por su desarrollo activo y soporte tanto para Pico como para Pico W. Si estás usando otra extensión específica, por favor acláralo y puedo adaptar las instrucciones.

---

### Ejemplo de Flujo de Trabajo
1.  Instala Pico-W-Go y sus dependencias.
2.  Configura el proyecto con el puerto serial correcto (`/dev/ttyACM0`).
3.  Escribe y guarda `main.py` con el código de parpadeo del LED.
4.  Usa **Pico-W-Go > Upload Project to Pico** para cargarlo.
5.  Reinicia el Pico o usa **Pico-W-Go > Run** para ver el LED parpadear.
6.  Usa el REPL para probar o depurar interactivamente.

Si necesitas ayuda con comandos específicos de Pico-W-Go, otro ejemplo de programa o resolución de problemas (por ejemplo, problemas de puerto, errores de extensión), ¡házmelo saber