---
audio: false
generated: true
lang: es
layout: post
title: Verificación de la Detección de Raspberry Pi Pico en Ubuntu
translated: true
type: note
---

Para verificar si tu Raspberry Pi Pico es detectado por Ubuntu después de conectarlo, sigue estos pasos:

1. **Verificar Dispositivos USB**:
   - Abre una terminal y ejecuta:
     ```bash
     lsusb
     ```
   - Busca una entrada como `Raspberry Pi Pico` o un dispositivo con un ID de vendedor de `2E8A` (el ID de vendedor de Raspberry Pi). Por ejemplo:
     ```
     Bus XXX Device XXX: ID 2e8a:0003 Raspberry Pi Pico
     ```

2. **Verificar Puertos Seriales**:
   - Si el Pico está en modo BOOTSEL (para flashear firmware) o ejecutando un programa de MicroPython/Arduino con salida serial, verifica si hay un puerto serial:
     ```bash
     ls /dev/tty*
     ```
   - Busca un dispositivo como `/dev/ttyACM0` o `/dev/ttyUSB0`. El Pico típicamente aparece como `/dev/ttyACM0` cuando ejecuta MicroPython.

3. **Verificar Dispositivos de Disco (Modo BOOTSEL)**:
   - Si el Pico está en modo BOOTSEL (manteniendo presionado el botón BOOTSEL mientras lo conectas), debería aparecer como un dispositivo de almacenamiento masivo. Ejecuta:
     ```bash
     lsblk
     ```
   - Busca un dispositivo como `/dev/sdb` (o similar) con un punto de montaje, frecuentemente etiquetado `RPI-RP2`.

4. **Usar `dmesg` para Logs del Kernel**:
   - Ejecuta:
     ```bash
     dmesg | tail -n 20
     ```
   - Verifica si hay mensajes que indiquen que el Pico fue detectado, tales como:
     ```
     [1234.567890] usb 1-1: New USB device found, idVendor=2e8a, idProduct=0003
     [1234.567891] usb 1-1: Product: Pico
     [1234.567892] cdc_acm 1-1:1.0: ttyACM0: USB ACM device
     ```
   - Esto confirma que el Pico es reconocido y se le ha asignado un puerto (por ejemplo, `ttyACM0`).

5. **Probar con MicroPython (si está instalado)**:
   - Si estás usando MicroPython, instala una herramienta como `picocom` o `minicom`:
     ```bash
     sudo apt install picocom
     ```
   - Conéctate al puerto serial del Pico:
     ```bash
     picocom /dev/ttyACM0
     ```
   - Si es detectado, deberías ver el prompt de REPL de MicroPython (>>>). Presiona `Ctrl+C` para salir.

**Notas**:
- Asegúrate de que el Pico esté correctamente conectado mediante un buen cable USB (de datos, no solo de energía).
- Si está en modo BOOTSEL, el Pico aparece como un dispositivo de almacenamiento, no como un dispositivo serial.
- Si no es detectado, prueba un puerto USB diferente, un cable diferente, o verifica si los controladores (como `cdc_acm` para serial) están cargados:
  ```bash
  lsmod | grep cdc_acm
  ```

Si no ves el Pico en ninguna de estas verificaciones, ¡cuéntame más detalles (por ejemplo, el modo del Pico, lo que estás intentando hacer) y puedo ayudarte a solucionar el problema!