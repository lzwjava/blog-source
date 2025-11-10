---
audio: false
generated: true
lang: es
layout: post
title: Configuración de Raspberry Pi Pico en Ubuntu
translated: true
type: note
---

Para usar un **Raspberry Pi Pico** en **Ubuntu**, necesitas configurar el entorno de desarrollo, instalar el software necesario y configurar las herramientas para programar el Pico. El Pico admite programación en **MicroPython**, **C/C++** o **CircuitPython**. A continuación, describo los pasos y el software requerido para cada enfoque, centrándome en las configuraciones más comunes.

### Prerrequisitos Generales
- **Raspberry Pi Pico** (o Pico W) con un cable USB (Micro-USB para Pico, USB-C para Pico 2).
- Sistema **Ubuntu** (por ejemplo, Ubuntu 20.04, 22.04 o posterior; estas instrucciones asumen una versión reciente como la 24.04).
- Conocimientos básicos de la terminal.

### Opción 1: Programar con MicroPython
MicroPython es la forma más amigable para principiantes de programar el Pico. Es una implementación ligera de Python diseñada para microcontroladores.

#### Software a Instalar
1. **Firmware de MicroPython**
   - Descarga el último archivo de firmware UF2 de MicroPython para Raspberry Pi Pico desde el [sitio web oficial de MicroPython](https://micropython.org/download/rp2-pico/) o la [página de Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).
   - Para Pico W o Pico 2, asegúrate de seleccionar el firmware apropiado (por ejemplo, `rp2-pico-w` para Pico W).

2. **Python 3**
   - Ubuntu normalmente incluye Python 3 por defecto. Verifica con:
     ```bash
     python3 --version
     ```
   - Si no está instalado, instálalo:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

3. **Thonny IDE** (Recomendado para Principiantes)
   - Thonny es un IDE simple para programar el Pico con MicroPython.
   - Instala Thonny:
     ```bash
     sudo apt install thonny
     ```
   - Alternativamente, usa `pip` para la versión más reciente:
     ```bash
     pip3 install thonny
     ```

4. **Opcional: `picotool` (para gestión avanzada)**
   - Útil para gestionar el firmware de MicroPython o inspeccionar el Pico.
   - Instala `picotool`:
     ```bash
     sudo apt install picotool
     ```

#### Pasos de Configuración
1. **Instalar el Firmware de MicroPython**
   - Conecta el Pico a tu máquina Ubuntu via USB mientras mantienes presionado el botón **BOOTSEL** (esto pone al Pico en modo bootloader).
   - El Pico aparece como un dispositivo de almacenamiento USB (por ejemplo, `RPI-RP2`).
   - Arrastra y suelta el archivo `.uf2` de MicroPython descargado en el almacenamiento del Pico. El Pico se reiniciará automáticamente con MicroPython instalado.

2. **Configurar Thonny**
   - Abre Thonny: `thonny` en la terminal o a través del menú de aplicaciones.
   - Ve a **Tools > Options > Interpreter**.
   - Selecciona **MicroPython (Raspberry Pi Pico)** como el intérprete.
   - Elige el puerto correcto (por ejemplo, `/dev/ttyACM0`). Ejecuta `ls /dev/tty*` en la terminal para identificar el puerto si es necesario.
   - Thonny ahora debería conectarse al Pico, permitiéndote escribir y ejecutar scripts de Python.

3. **Probar un Programa**
   - En Thonny, escribe un script simple, por ejemplo:
     ```python
     from machine import Pin
     led = Pin(25, Pin.OUT)  # LED integrado (GP25 para Pico)
     led.toggle()  # Alternar LED encendido/apagado
     ```
   - Haz clic en el botón **Run** para ejecutar el código en el Pico.

4. **Opcional: Usar `picotool`**
   - Verifica el estado del Pico:
     ```bash
     picotool info
     ```
   - Asegúrate de que el Pico esté conectado y en modo bootloader si es necesario.

### Opción 2: Programar con C/C++
Para usuarios más avanzados, el Pico se puede programar en C/C++ usando el **Pico SDK** oficial.

#### Software a Instalar
1. **Pico SDK y Toolchain**
   - Instala las herramientas requeridas para construir programas en C/C++:
     ```bash
     sudo apt update
     sudo apt install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential git
     ```

2. **Pico SDK**
   - Clona el repositorio del Pico SDK:
     ```bash
     git clone -b master https://github.com/raspberrypi/pico-sdk.git
     cd pico-sdk
     git submodule update --init
     ```
   - Establece la variable de entorno `PICO_SDK_PATH`:
     ```bash
     export PICO_SDK_PATH=~/pico-sdk
     echo 'export PICO_SDK_PATH=~/pico-sdk' >> ~/.bashrc
     ```

3. **Opcional: Ejemplos de Pico**
   - Clona los ejemplos de Pico como referencia:
     ```bash
     git clone -b master https://github.com/raspberrypi/pico-examples.git
     ```

4. **Visual Studio Code (Opcional)**
   - Para una mejor experiencia de desarrollo, instala VS Code:
     ```bash
     sudo snap install code --classic
     ```
   - Instala las extensiones **CMake Tools** y **C/C++** en VS Code.

#### Pasos de Configuración
1. **Configurar un Proyecto**
   - Crea un nuevo directorio para tu proyecto, por ejemplo, `my-pico-project`.
   - Copia un `CMakeLists.txt` de ejemplo desde `pico-examples` o crea uno:
     ```cmake
     cmake_minimum_required(VERSION 3.13)
     include($ENV{PICO_SDK_PATH}/pico_sdk_init.cmake)
     project(my_project C CXX ASM)
     pico_sdk_init()
     add_executable(my_project main.c)
     pico_add_extra_outputs(my_project)
     target_link_libraries(my_project pico_stdlib)
     ```
   - Escribe un programa simple en C (por ejemplo, `main.c`):
     ```c
     #include "pico/stdlib.h"
     int main() {
         const uint LED_PIN = 25;
         gpio_init(LED_PIN);
         gpio_set_dir(LED_PIN, GPIO_OUT);
         while (true) {
             gpio_put(LED_PIN, 1);
             sleep_ms(500);
             gpio_put(LED_PIN, 0);
             sleep_ms(500);
         }
     }
     ```

2. **Construir y Flashear**
   - Navega a tu directorio del proyecto:
     ```bash
     cd my-pico-project
     mkdir build && cd build
     cmake ..
     make
     ```
   - Esto genera un archivo `.uf2` (por ejemplo, `my_project.uf2`).
   - Mantén presionado el botón **BOOTSEL** en el Pico, conéctalo via USB y copia el archivo `.uf2` al almacenamiento del Pico:
     ```bash
     cp my_project.uf2 /media/$USER/RPI-RP2/
     ```

3. **Depuración (Opcional)**
   - Instala `openocd` para depuración:
     ```bash
     sudo apt install openocd
     ```
   - Usa un depurador (por ejemplo, otro Pico como sonda de depuración) y ejecuta:
     ```bash
     openocd -f interface/raspberrypi-swd.cfg -f target/rp2040.cfg
     ```

### Opción 3: Programar con CircuitPython
CircuitPython es otra opción basada en Python, similar a MicroPython pero con un enfoque en el ecosistema de Adafruit.

#### Software a Instalar
1. **Firmware de CircuitPython**
   - Descarga el archivo UF2 de CircuitPython para el Pico desde el [sitio web de Adafruit CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/).
   - Para Pico W o Pico 2, selecciona el firmware apropiado.

2. **Python 3 y Herramientas**
   - Igual que para MicroPython (Python 3, Thonny, etc.).

#### Pasos de Configuración
1. **Instalar el Firmware de CircuitPython**
   - Similar a MicroPython: mantén **BOOTSEL**, conecta el Pico y copia el archivo `.uf2` de CircuitPython al almacenamiento del Pico.
   - El Pico se reinicia como una unidad USB llamada `CIRCUITPY`.

2. **Programar con Thonny o un Editor de Texto**
   - Usa Thonny como se describe en la sección de MicroPython, seleccionando **CircuitPython** como el intérprete.
   - Alternativamente, edita `code.py` directamente en la unidad `CIRCUITPY` usando cualquier editor de texto.
   - Ejemplo de `code.py`:
     ```python
     import board
     import digitalio
     import time
     led = digitalio.DigitalInOut(board.LED)
     led.direction = digitalio.Direction.OUTPUT
     while True:
         led.value = True
         time.sleep(0.5)
         led.value = False
         time.sleep(0.5)
     ```

### Notas Adicionales
- **Permisos**: Si el puerto del Pico (por ejemplo, `/dev/ttyACM0`) no es accesible, añade tu usuario al grupo `dialout`:
  ```bash
  sudo usermod -a -G dialout $USER
  ```
  Cierra y vuelve a iniciar sesión para aplicar el cambio.

- **Consideraciones para Pico W**: Para el Pico W, asegúrate de usar firmware específico para él (por ejemplo, MicroPython con soporte Wi-Fi). La programación Wi-Fi requiere bibliotecas adicionales, como `network` para MicroPython.

- **Pico 2**: El nuevo Raspberry Pi Pico 2 (con RP2350) puede requerir versiones actualizadas del firmware o del SDK. Consulta la documentación oficial de Raspberry Pi para ver la compatibilidad.

- **Solución de Problemas**:
  - Si el Pico no aparece en modo bootloader, verifica el cable USB (debe admitir datos, no solo energía).
  - Ejecuta `lsusb` o `dmesg` para confirmar que Ubuntu detecta el Pico.
  - Para construcciones en C/C++, asegúrate de que la ruta del Pico SDK esté configurada correctamente.

### Enfoque Recomendado
- Para **principiantes**: Usa **MicroPython con Thonny** por su simplicidad y configuración rápida.
- Para **usuarios avanzados**: Usa **C/C++ con el Pico SDK** para rendimiento y control de bajo nivel.
- Para **usuarios del ecosistema Adafruit**: Usa **CircuitPython** si planeas usar bibliotecas o hardware de Adafruit.

¡Si tienes un proyecto específico o una preferencia de programación, házmelo saber y puedo adaptar las instrucciones aún más!