---
audio: false
generated: true
lang: es
layout: post
title: VSCode para Raspberry Pi Pico MicroPython
translated: true
type: note
---

Sí, puedes usar Visual Studio Code (VSCode) para escribir, cargar y ejecutar programas de MicroPython en tu Raspberry Pi Pico, de manera similar a como lo harías con Thonny. VSCode es un editor potente y, con las extensiones y herramientas adecuadas, puede manejar el desarrollo con MicroPython de forma efectiva. A continuación, se presenta una guía paso a paso para configurar VSCode y cargar un programa simple de MicroPython en tu Pico, asumiendo que MicroPython ya está instalado (como has hecho con el archivo `.uf2`).

---

### Prerrequisitos
1.  **MicroPython Instalado**: Tu Pico tiene MicroPython instalado (por ejemplo, desde el archivo `RPI_PICO-20250415-v1.25.0.uf2`).
2.  **VSCode Instalado**: Descarga e instala VSCode desde [code.visualstudio.com](https://code.visualstudio.com) si aún no lo tienes.
3.  **Python Instalado**: Instala Python (necesario para las herramientas de MicroPython) mediante:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
4.  **Conexión USB**: El Pico está conectado a tu computadora mediante un cable USB con capacidad de datos.

---

### Guía Paso a Paso para Usar VSCode con MicroPython en Raspberry Pi Pico

1.  **Instalar las Extensiones Necesarias para VSCode**:
    - Abre VSCode.
    - Ve a la vista de Extensiones (`Ctrl+Shift+X` o `Cmd+Shift+X` en macOS).
    - Instala las siguientes extensiones:
        - **Python** (de Microsoft): Para resaltado de sintaxis de Python y MicroPython e IntelliSense.
        - **Pico-W-Go** (opcional pero recomendada): Una extensión dedicada para el desarrollo con Raspberry Pi Pico y MicroPython. Busca "Pico-W-Go" e instálala.
            - Nota: Pico-W-Go simplifica la transferencia de archivos y el acceso al REPL, pero requiere configuración adicional (descrita a continuación).
        - Alternativamente, puedes usar extensiones de propósito general como **Remote-SSH** o **Serial Monitor** si prefieres un control manual.

2.  **Configurar Pico-W-Go (Recomendado)**:
    - **Instalar Dependencias**: Pico-W-Go requiere `pyserial` y `esptool`. Instálalos via pip:
      ```bash
      pip3 install pyserial esptool
      ```
    - **Configurar Pico-W-Go**:
        - Abre la Paleta de Comandos de VSCode (`Ctrl+Shift+P` o `Cmd+Shift+P`).
        - Escribe y selecciona **Pico-W-Go > Configure Project**.
        - Sigue las instrucciones para configurar tu proyecto:
            - Elige el puerto serie del Pico (ej. `/dev/ttyACM0`). Ejecuta `ls /dev/tty*` en una terminal para encontrarlo.
            - Selecciona MicroPython como el intérprete.
            - Crea una nueva carpeta de proyecto o usa una existente.
        - Pico-W-Go crea un espacio de trabajo con un archivo de configuración `.picowgo`.

3.  **Escribir un Programa Simple de MicroPython**:
    - En VSCode, crea un nuevo archivo (ej. `main.py`) en tu carpeta de proyecto.
    - Escribe un programa simple, como hacer parpadear el LED integrado:
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
    - Guarda el archivo (`Ctrl+S` o `Cmd+S`).

4.  **Cargar el Programa al Pico**:
    - **Usando Pico-W-Go**:
        - Asegúrate de que el Pico esté conectado y el puerto correcto seleccionado (verifica en `Pico-W-Go > Configure Project` si es necesario).
        - Abre la Paleta de Comandos (`Ctrl+Shift+P`).
        - Selecciona **Pico-W-Go > Upload Project to Pico**.
        - Esto carga todos los archivos en tu carpeta de proyecto (ej. `main.py`) al sistema de archivos del Pico.
        - Si nombraste el archivo `main.py`, se ejecutará automáticamente al arrancar.
    - **Carga Manual con `rshell`** (si no usas Pico-W-Go):
        - Instala `rshell`:
          ```bash
          pip3 install rshell
          ```
        - Conéctate al Pico:
          ```bash
          rshell --port /dev/ttyACM0
          ```
        - Copia el archivo al Pico:
          ```bash
          cp main.py /pyboard/main.py
          ```
        - Sal de `rshell` con `exit`.

5.  **Ejecutar y Probar el Programa**:
    - **Usando Pico-W-Go**:
        - Abre la Paleta de Comandos y selecciona **Pico-W-Go > Run**.
        - Esto ejecuta el archivo actual o abre el REPL para comandos manuales.
        - Deberías ver el LED parpadeando si usas el ejemplo anterior.
    - **Usando la Terminal o REPL de VSCode**:
        - Abre el REPL con Pico-W-Go (`Pico-W-Go > Open REPL`) o usa `rshell`:
          ```bash
          rshell --port /dev/ttyACM0 repl
          ```
        - Prueba comandos directamente, ej.:
          ```python
          from machine import Pin
          led = Pin(25, Pin.OUT)
          led.on()
          ```
        - Presiona `Ctrl+C` para detener un programa en ejecución en el REPL.
    - Si el archivo es `main.py`, reinicia el Pico (desconecta y vuelve a conectar, o presiona el botón RESET) para ejecutarlo automáticamente.

6.  **Depurar y Gestionar Archivos**:
    - **Pico-W-Go**: Usa **Pico-W-Go > Download Project from Pico** para recuperar archivos del Pico o **Pico-W-Go > Delete All Files** para limpiar el sistema de archivos.
    - **rshell**: Lista los archivos con:
      ```bash
      rshell ls /pyboard
      ```
      Elimina archivos con:
      ```bash
      rshell rm /pyboard/main.py
      ```
    - Revisa la salida del programa en la terminal o REPL de VSCode.

---

### Alternativa: Flujo de Trabajo Manual Sin Pico-W-Go
Si prefieres no usar Pico-W-Go, puedes gestionar el desarrollo de MicroPython manualmente:
1.  Escribe tu código en VSCode y guárdalo como `main.py`.
2.  Usa `ampy` (otra herramienta de MicroPython) para cargar:
    ```bash
    pip3 install adafruit-ampy
    ampy --port /dev/ttyACM0 put main.py
    ```
3.  Accede al REPL con una herramienta de terminal como `minicom` o `screen`:
    ```bash
    screen /dev/ttyACM0 115200
    ```
    Presiona `Ctrl+C` para detener un programa en ejecución y entrar al REPL.

---

### Resolución de Problemas
-   **Puerto No Encontrado**: Ejecuta `ls /dev/tty*` para verificar el puerto del Pico (ej. `/dev/ttyACM0`). Asegúrate de que el Pico esté conectado y MicroPython esté instalado.
-   **Errores de Pico-W-Go**: Verifica que `pyserial` y `esptool` estén instalados y que el puerto correcto esté seleccionado. Reinicia VSCode si es necesario.
-   **Programa No Se Ejecuta**: Asegúrate de que el archivo esté guardado como `main.py` para su ejecución automática, o ejecútalo manualmente via el REPL o `ampy run main.py`.
-   **LED No Parpadea**: Verifica el pin GPIO (`25` para Pico, `"LED"` para Pico W). Prueba en el REPL:
    ```python
    from machine import Pin
    led = Pin(25, Pin.OUT)
    led.on()
    ```

---

### Ventajas de VSCode sobre Thonny
-   Mejores funciones de edición de código (ej. IntelliSense, integración con Git, flujos de trabajo personalizables).
-   Soporta proyectos más grandes con múltiples archivos.
-   Pico-W-Go proporciona una experiencia similar a Thonny pero con la potencia de VSCode.

### Limitaciones
-   La configuración es ligeramente más compleja que con Thonny.
-   La integración del REPL puede parecer menos fluida en comparación con la interfaz todo-en-uno de Thonny.

¡Si necesitas ayuda con configuraciones específicas de VSCode, la instalación de herramientas o la escritura de programas de MicroPython más complejos, házmelo saber