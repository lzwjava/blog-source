---
audio: false
generated: true
lang: es
layout: post
title: Raspberry Pi Pico en Modo BOOTSEL
translated: true
type: note
---

El dispositivo listado como `Bus 001 Device 009: ID 2e8a:0003 Raspberry Pi RP2 Boot` es un Raspberry Pi Pico (o una placa similar basada en RP2040) en modo BOOTSEL. Aquí hay un desglose:

- **ID 2e8a:0003**: Este es el ID de vendedor USB (2e8a) y el ID de producto (0003) asignado a Raspberry Pi para el microcontrolador RP2040 cuando está en modo BOOTSEL.
- **Raspberry Pi RP2 Boot**: Indica que el dispositivo es un Raspberry Pi Pico (u otra placa basada en RP2040, como el Pico W o una placa personalizada) que ha entrado en su modo bootloader. En este modo, el dispositivo aparece como un dispositivo de almacenamiento masivo USB, permitiéndote cargar firmware (por ejemplo, archivos .uf2) copiándolos a la unidad.

### ¿Qué es el Modo BOOTSEL?
El modo BOOTSEL se activa manteniendo presionado el botón BOOTSEL en el Raspberry Pi Pico mientras lo conectas a un puerto USB o al resetearlo mientras mantienes el botón presionado. Este modo se utiliza para flashear nuevo firmware o programas en el microcontrolador RP2040. Cuando está en este modo, el Pico aparece como una unidad extraíble (llamada `RPI-RP2`) en tu computadora.

### ¿Por qué aparece así?
Es probable que tu dispositivo esté en modo BOOTSEL porque:
1. Presionaste intencionalmente el botón BOOTSEL para actualizar o flashear firmware.
2. El dispositivo no está ejecutando un programa y por defecto entra en modo bootloader (por ejemplo, después de un flasheo fallido o un reset).
3. Podría haber un problema con el firmware o las conexiones, haciendo que se quede en modo bootloader. Por ejemplo, problemas con la memoria flash o un flasheo incorrecto pueden hacer que el dispositivo revierta a este modo.

### ¿Qué hacer a continuación?
- **Si quieres flashear firmware**: Copia un archivo `.uf2` válido (por ejemplo, un firmware de MicroPython o CircuitPython, o un programa compilado) a la unidad `RPI-RP2`. El dispositivo flasheará el firmware automáticamente y se reiniciará, saliendo del modo BOOTSEL.
- **Si está atascado en modo BOOTSEL**: Esto podría indicar un problema con la memoria flash o el firmware. Intenta:
  1. Re-flashear con un archivo `.uf2` conocido y funcional, como el firmware de MicroPython del sitio web oficial de Raspberry Pi.
  2. Verificar el cable USB y el puerto, ya que un cable defectuoso puede causar problemas.
  3. Usar herramientas como `picotool` para verificar el estado del dispositivo o resetearlo. Por ejemplo, ejecuta `picotool info` para revisar el estado del dispositivo.
  4. Si estás usando una placa RP2040 personalizada, asegúrate de que el chip de flash esté correctamente conectado y configurado, ya que problemas con las señales QSPI o los circuitos integrados de flash pueden evitar un flasheo exitoso.
- **Si quieres salir del modo BOOTSEL**: Si el firmware válido ya está flasheado, desenchufa el dispositivo, asegúrate de que el botón BOOTSEL no esté presionado y vuelve a enchufarlo. El dispositivo debería arrancar en su modo programado (por ejemplo, ejecutando un script de MicroPython o un programa en C).

### Notas Adicionales
- El RP2040 es el microcontrolador utilizado en el Raspberry Pi Pico, Pico W y otras placas. La designación `RP2 Boot` se refiere específicamente al modo bootloader del chip RP2040.
- Si estás usando un Raspberry Pi Pico W, ten en cuenta que incluye capacidades inalámbricas, pero estas no están activas en el modo BOOTSEL.
- Si encuentras errores (por ejemplo, que `picotool` falle al verificar o cargar), podría deberse a un problema de hardware (como un chip de flash defectuoso o un problema de soldadura en una placa personalizada) o a un archivo de firmware corrupto.

¡Si necesitas ayuda específica (por ejemplo, flashear firmware, resolver problemas o identificar la placa exacta), házmelo saber con más detalles sobre tu configuración o lo que estás intentando lograr!