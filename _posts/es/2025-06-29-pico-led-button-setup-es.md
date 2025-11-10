---
audio: false
generated: true
lang: es
layout: post
title: Configuración de LED y Botón para Raspberry Pi Pico
translated: true
type: note
---

Para configurar una Raspberry Pi Pico para ejecutar el código MicroPython proporcionado, que controla un LED basado en la pulsación de un botón, sigue estos pasos:

### Requisitos de Hardware
- **Raspberry Pi Pico** (o Pico W)
- **LED** (con una resistencia limitadora de corriente apropiada, p.ej., 220–330 ohmios)
- **Pulsador**
- **Cables jumper**
- **Protoboard** (opcional, para conexiones más fáciles)
- **Cable USB** (para conectar la Pico a tu computadora)

### Configuración del Hardware
1. **Conecta el LED**:
   - Conecta el ánodo del LED (pata larga) al **GPIO 25** (pin físico 30) de la Pico.
   - Conecta el cátodo del LED (pata corta) a un pin de **tierra (GND)** (p.ej., pin físico 3) a través de una resistencia de 220–330 ohmios para limitar la corriente.

2. **Conecta el Botón**:
   - Conecta un lado del pulsador al **GPIO 14** (pin físico 19).
   - Conecta el otro lado del botón a un pin de **3.3V** (p.ej., pin físico 36, 3V3(OUT)).
   - El código utiliza una resistencia pull-down interna (`Pin.PULL_DOWN`), por lo que no se necesita una resistencia pull-down externa. Cuando se presiona el botón, el GPIO 14 leerá HIGH (1); cuando no se presiona, leerá LOW (0).

3. **Verifica las Conexiones**:
   - Asegúrate de que todas las conexiones sean seguras. Usa una protoboard o cableado directo, y verifica dos veces que la polaridad del LED sea correcta y que la resistencia esté colocada correctamente.
   - Consulta el diagrama de pines de la Pico (disponible en línea o en la hoja de datos de la Pico) para confirmar las asignaciones de pines.

### Configuración del Software
1. **Instala MicroPython en la Pico**:
   - Descarga el firmware MicroPython UF2 más reciente para la Raspberry Pi Pico desde el [sitio web oficial de MicroPython](https://micropython.org/download/rp2-pico/).
   - Conecta la Pico a tu computadora mediante un cable USB mientras mantienes presionado el botón **BOOTSEL**.
   - La Pico aparecerá como una unidad USB (RPI-RP2). Arrastra y suelta el archivo `.uf2` descargado en esta unidad.
   - La Pico se reiniciará automáticamente con MicroPython instalado.

2. **Configura un Entorno de Desarrollo**:
   - Instala un IDE compatible con MicroPython, como **Thonny** (recomendado para principiantes):
     - Descarga e instala Thonny desde [thonny.org](https://thonny.org).
     - En Thonny, ve a **Tools > Options > Interpreter**, selecciona **MicroPython (Raspberry Pi Pico)** y elige el puerto apropiado (p.ej., `COMx` en Windows o `/dev/ttyACM0` en Linux/macOS).
   - Alternativamente, puedes usar herramientas como `rshell`, `ampy` o Visual Studio Code con la extensión de MicroPython.

3. **Carga y Ejecuta el Código**:
   - Copia el código proporcionado en un archivo llamado `main.py`:
     ```python
     from machine import Pin
     import time

     led = Pin(25, Pin.OUT)
     button = Pin(14, Pin.IN, Pin.PULL_DOWN)

     while True:
         if button.value():
             led.on()
         else:
             led.off()
         time.sleep(0.05)
     ```
   - En Thonny:
     - Abre un nuevo archivo, pega el código y guárdalo en la Pico como `main.py` (MicroPython ejecuta automáticamente `main.py` al arrancar).
     - Haz clic en el botón **Run** o presiona **F5** para cargar y ejecutar el código.
   - Alternativamente, usa `ampy` para subir el archivo:
     ```bash
     ampy --port /dev/ttyACM0 put main.py
     ```
     Reemplaza `/dev/ttyACM0` con el puerto de tu Pico.

4. **Prueba el Programa**:
   - Una vez que el código se haya cargado, el LED debería encenderse cuando se presiona el botón y apagarse cuando se suelta. El `time.sleep(0.05)` añade un retardo de 50ms para eliminar los rebotes del botón y reducir la carga de la CPU.

### Resolución de Problemas
- **El LED no se enciende**:
  - Comprueba la polaridad del LED (ánodo a GPIO 25, cátodo a GND a través de la resistencia).
  - Verifica que el pin GPIO (25) coincida con el código y la conexión física.
  - Asegúrate de que el LED y la resistencia estén funcionando (pruébalos con un multímetro o en otro circuito).
- **El botón no funciona**:
  - Confirma que el GPIO 14 esté conectado correctamente y que el botón se conecte a 3.3V cuando se presiona.
  - Comprueba que `Pin.PULL_DOWN` sea apropiado; si el botón está cableado de manera diferente (p.ej., a GND), ajusta el código para usar `Pin.PULL_UP` e invertir la lógica (`if not button.value()`).
- **El código no se ejecuta**:
  - Asegúrate de que MicroPython esté instalado correctamente.
  - Verifica que el archivo esté guardado como `main.py` en la Pico.
  - Comprueba la conexión USB y la configuración del puerto en tu IDE.

### Notas
- El código asume que el botón conecta el GPIO 14 a 3.3V cuando se presiona. Si tu botón se conecta a GND en su lugar, modifica el código para usar `Pin.PULL_UP` e invertir la lógica:
  ```python
  button = Pin(14, Pin.IN, Pin.PULL_UP)
  while True:
      if not button.value():  # Botón presionado = LOW
          led.on()
      else:
          led.off()
      time.sleep(0.05)
  ```
- Si experimentas rebotes del botón (LED parpadeante), aumenta el valor de `time.sleep` o implementa un antirrebote por software.
- Para una Pico W, la configuración es idéntica, pero asegúrate de usar los pines GPIO correctos, ya que la distribución de pines es la misma.

Si necesitas más aclaraciones o ayuda con problemas específicos, ¡avísame!