---
audio: false
generated: true
lang: es
layout: post
title: Subir MicroPython a Pico
translated: true
type: note
---

Después de flashear MicroPython en tu Raspberry Pi Pico (usando el archivo `.uf2` como se describió), puedes cargar y ejecutar un programa simple de MicroPython usando una herramienta como Thonny IDE, que es amigable para principiantes y ampliamente utilizada para el desarrollo con MicroPython. A continuación se detallan los pasos para configurar MicroPython y cargar un programa simple a tu Pico.

---

### Prerrequisitos
1.  **MicroPython Flasheado**: Ya has copiado `RPI_PICO-20250415-v1.25.0.uf2` a la unidad `RPI-RP2`, y el Pico se ha reiniciado (la unidad `RPI-RP2` ya no debería aparecer).
2.  **Conexión USB**: El Pico está conectado a tu computadora mediante un cable USB que admita transferencia de datos.
3.  **Thonny IDE**: Instala Thonny si aún no lo has hecho:
    - **Linux**: Instala Thonny usando tu gestor de paquetes o descárgalo desde [thonny.org](https://thonny.org).
      ```bash
      sudo apt update
      sudo apt install thonny
      ```
    - Alternativamente, usa `pip`:
      ```bash
      pip install thonny
      ```
    - Para Windows/macOS, descarga e instala desde [thonny.org](https://thonny.org).

---

### Guía Paso a Paso para Cargar un Programa Simple de MicroPython

1.  **Conecta el Pico y Abre Thonny**:
    - Conecta tu Pico al puerto USB de tu computadora.
    - Abre Thonny IDE.

2.  **Configura Thonny para MicroPython**:
    - En Thonny, ve a **Tools > Options > Interpreter** (o **Run > Select interpreter**).
    - Selecciona **MicroPython (Raspberry Pi Pico)** del menú desplegable de intérprete.
    - Si el puerto serial del Pico (ej. `/dev/ttyACM0` en Linux) no aparece automáticamente:
      - Verifica los puertos disponibles en el menú desplegable o ejecuta `ls /dev/tty*` en una terminal para identificar el puerto del Pico (usualmente `/dev/ttyACM0` o similar).
      - Selecciona el puerto correcto manualmente.
    - Haz clic en **OK** para guardar.

3.  **Verifica que MicroPython esté Ejecutándose**:
    - En la **Shell** de Thonny (panel inferior), deberías ver un prompt de REPL de MicroPython como:
      ```
      >>>
      ```
    - Pruébalo escribiendo un comando simple, ej.:
      ```python
      print("Hello, Pico!")
      ```
      Presiona Enter, y deberías ver la salida en la Shell.

4.  **Escribe un Programa Simple de MicroPython**:
    - En el editor principal de Thonny, crea un nuevo archivo y escribe un programa simple. Por ejemplo, un programa para hacer parpadear el LED integrado del Pico (en GPIO 25 para Pico, o "LED" para Pico W):
      ```python
      from machine import Pin
      import time

      # Inicializa el LED integrado
      led = Pin(25, Pin.OUT)  # Usa "LED" en lugar de 25 para Pico W

      # Hace parpadear el LED
      while True:
          led.on()           # Enciende el LED
          time.sleep(0.5)    # Espera 0.5 segundos
          led.off()          # Apaga el LED
          time.sleep(0.5)    # Espera 0.5 segundos
      ```
    - Nota: Si usas un Pico W, reemplaza `Pin(25, Pin.OUT)` con `Pin("LED", Pin.OUT)`.

5.  **Guarda el Programa en el Pico**:
    - Haz clic en **File > Save As**.
    - En el diálogo, selecciona **Raspberry Pi Pico** como destino (no tu computadora).
    - Nombra el archivo `main.py` (MicroPython ejecuta `main.py` automáticamente al arrancar) o con otro nombre como `blink.py`.
    - Haz clic en **OK** para guardar el archivo en el sistema de archivos del Pico.

6.  **Ejecuta el Programa**:
    - Haz clic en el botón verde **Run** (o presiona **F5**) en Thonny para ejecutar el programa.
    - Alternativamente, si lo guardaste como `main.py`, reinicia el Pico (desconéctalo y vuelve a conectarlo, o presiona el botón RESET si está disponible), y el programa se ejecutará automáticamente.
    - Deberías ver el LED integrado parpadeando cada 0.5 segundos.

7.  **Detén el Programa** (si es necesario):
    - Para detener el programa, presiona **Ctrl+C** en la Shell de Thonny para interrumpir el script en ejecución.
    - Para evitar que `main.py` se ejecute automáticamente, elimínalo del Pico:
      - En Thonny, ve a **View > Files**, selecciona el sistema de archivos del Pico, haz clic derecho en `main.py` y elige **Delete**.

---

### Pruebas y Solución de Problemas
-   **No hay Prompt REPL**: Si Thonny no muestra el REPL de MicroPython:
    - Asegúrate de que el puerto correcto esté seleccionado en la configuración del intérprete.
    - Verifica que MicroPython se haya flasheado correctamente. Si no, reflashea el archivo `.uf2` como se describió anteriormente.
    - Revisa el cable USB (debe admitir datos) y prueba un puerto diferente.
-   **El LED no Parpadea**: Asegúrate de usar el pin GPIO correcto (`25` para Pico, `"LED"` para Pico W). Si aún no funciona, prueba el LED con un comando simple en el REPL:
    ```python
    from machine import Pin
    led = Pin(25, Pin.OUT)
    led.on()
    ```
-   **El Archivo no se Guarda**: Asegúrate de que Thonny esté conectado al Pico y de que el intérprete esté configurado como MicroPython (Raspberry Pi Pico).

---

### Consejos Adicionales
-   **Usando Otras Herramientas**: Además de Thonny, puedes usar `rshell` o `ampy` para gestionar archivos en el Pico:
    ```bash
    pip install rshell
    rshell --port /dev/ttyACM0
    cp blink.py /pyboard/main.py
    ```
-   **Más Programas de Ejemplo**:
    - Leer un pulsador (ej., en GPIO 14):
      ```python
      from machine import Pin
      button = Pin(14, Pin.IN, Pin.PULL_UP)
      while True:
          print(button.value())
      ```
    - Controla un LED externo u otros periféricos ajustando el número de pin GPIO.
-   **Ejecución Automática**: Guardar un archivo como `main.py` hace que se ejecute automáticamente al arrancar. Usa `boot.py` para código de configuración que se ejecute antes de `main.py`.

Si encuentras problemas específicos (ej., detección de puerto, errores en Thonny o problemas de hardware), o quieres probar un programa diferente, ¡avísame y te guiaré más!