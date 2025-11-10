---
audio: false
generated: true
lang: es
layout: post
title: Guía de Cable USB para Raspberry Pi Pico en Ubuntu
translated: true
type: note
---

Para tu **Raspberry Pi Pico (con cabezales)** de la **Raspberry Pi Foundation** (asumiendo que "duistou" es un error tipográfico o una marca de reventa), necesitas el cable USB correcto para configurarlo con Ubuntu. Esto es lo que necesitas:

### Requisitos del Cable USB
1. **Tipo**: Cable USB a Micro-USB
   - La Raspberry Pi Pico (original, con cabezales) utiliza un puerto **Micro-USB** para alimentación y datos.
   - Asegúrate de que el cable admita **transferencia de datos**, no solo carga. Algunos cables Micro-USB baratos son solo para energía y no funcionarán para programación o comunicación.

2. **Especificaciones del Cable**:
   - **Conector**: USB-A (o USB-C, dependiendo de los puertos de tu computadora) a Micro-USB.
   - **Calidad**: Usa un cable de alta calidad para evitar problemas de conexión. Un cable de una marca reconocida (por ejemplo, Anker, Belkin, o el incluido con dispositivos como teléfonos o tabletas) funciona bien.
   - **Longitud**: Un cable de 1-3 pies (30-100 cm) es ideal para minimizar problemas de señal.

3. **Puerto de la Computadora**:
   - Si tu máquina con Ubuntu tiene puertos **USB-A**, usa un cable USB-A a Micro-USB.
   - Si solo tiene puertos **USB-C**, usa un cable USB-C a Micro-USB o un concentrador/adaptador USB-C con un cable USB-A a Micro-USB.

### Notas de Configuración
- **Conexión**: Enchufa el extremo Micro-USB en el puerto Micro-USB del Pico y el otro extremo en tu computadora con Ubuntu.
- **Modo**:
  - **Modo Normal**: Enchufa el Pico directamente para conectarlo para programación (por ejemplo, MicroPython, C/C++).
  - **Modo BOOTSEL**: Mantén presionado el botón **BOOTSEL** en el Pico mientras lo enchufas para entrar en modo de almacenamiento masivo y actualizar el firmware (aparece como una unidad llamada `RPI-RP2`).
- **Verificación**: Después de conectarlo, usa los pasos de mi respuesta anterior para confirmar que Ubuntu detecta el Pico (por ejemplo, `lsusb`, `ls /dev/tty*`, o `lsblk`).

### Solución de Problemas con el Cable
- Si el Pico no es detectado (no aparece `/dev/ttyACM0` o la unidad `RPI-RP2`), prueba con un cable o puerto USB diferente.
- Evita usar concentradores USB, ya que a veces pueden causar problemas de detección.
- Verifica el cable probándolo con otro dispositivo (por ejemplo, un teléfono) para confirmar que admite transferencia de datos.

Si no estás seguro sobre tu cable o aún tienes problemas, describe tu configuración (por ejemplo, puertos de la computadora, tipo de cable, lo que ves al enchufarlo), ¡y puedo guiarte más!