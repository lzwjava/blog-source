---
audio: false
generated: true
lang: es
layout: post
title: Flashear Firmware Pico mediante UF2
translated: true
type: note
---

Para flashear el firmware en tu Raspberry Pi Pico (o placa basada en RP2040) en modo BOOTSEL copiando un archivo `.uf2` a la unidad `RPI-RP2`, sigue estos pasos:

### Guía Paso a Paso
1. **Confirma que el Dispositivo está en Modo BOOTSEL**:
   - Tu dispositivo debe aparecer como una unidad USB llamada `RPI-RP2` cuando se conecta a tu computadora. Esto confirma que está en modo BOOTSEL (como se indica en `Bus 001 Device 009: ID 2e8a:0003 Raspberry Pi RP2 Boot`).
   - Si no está en modo BOOTSEL, desenchufa el dispositivo, mantén presionado el botón BOOTSEL en la Pico y conéctala al puerto USB de tu computadora mientras mantienes el botón presionado. Suelta el botón después de unos segundos.

2. **Obtén un Archivo `.uf2` Válido**:
   - **MicroPython**: Descarga el firmware más reciente de MicroPython para Raspberry Pi Pico desde el [sitio web oficial de MicroPython](https://micropython.org/download/rp2-pico/). Elige el archivo `.uf2` para la Pico o Pico W (por ejemplo, `rp2-pico-latest.uf2`).
   - **CircuitPython**: Descarga el firmware de CircuitPython desde el [sitio web de CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) para la Pico o Pico W.
   - **Programa Personalizado**: Si has escrito un programa (por ejemplo, en C/C++ usando el Pico SDK), compílalo para generar un archivo `.uf2`. Por ejemplo, usa el Pico SDK o Arduino IDE para construir tu proyecto.
   - Guarda el archivo `.uf2` en una ubicación de fácil acceso en tu computadora (por ejemplo, el Escritorio o la carpeta de Descargas).

3. **Localiza la Unidad RPI-RP2**:
   - En tu computadora, abre el explorador de archivos:
     - **Windows**: Busca `RPI-RP2` en "Este equipo" como una unidad extraíble.
     - **macOS**: La unidad debería aparecer en el Escritorio o en el Finder bajo "Dispositivos".
     - **Linux**: Revisa en `/media` o `/mnt`, o usa `lsblk` para listar las unidades conectadas.
   - Si la unidad no aparece, asegúrate de que el cable USB sea capaz de transferir datos (no solo de energía) y prueba con un puerto USB o cable diferente.

4. **Copia el Archivo `.uf2` a la Unidad RPI-RP2**:
   - Arrastra y suelta el archivo `.uf2` en la unidad `RPI-RP2`, o cópialo y pégalo usando tu explorador de archivos.
   - Alternativamente, usa un comando de terminal (en Linux/macOS):
     ```bash
     cp /ruta/a/tu/archivo.uf2 /media/tu_usuario/RPI-RP2/
     ```
     Reemplaza `/ruta/a/tu/archivo.uf2` con la ruta a tu archivo `.uf2` y ajusta el punto de montaje según sea necesario.

5. **Espera el Proceso de Flasheo**:
   - Una vez que se copia el archivo `.uf2`, la Raspberry Pi Pico flashea el firmware automáticamente. La unidad `RPI-RP2` desaparecerá (se desmontará) cuando el dispositivo se reinicie, lo que indica que el proceso ha terminado.
   - Esto normalmente toma unos segundos. No desenchufes el dispositivo durante este tiempo.

6. **Verifica el Dispositivo**:
   - Después del flasheo, la Pico debería salir del modo BOOTSEL y ejecutar el nuevo firmware.
   - Para MicroPython o CircuitPython, conéctate al dispositivo usando una terminal (por ejemplo, PuTTY, screen o Thonny IDE) a través del puerto serie USB (por ejemplo, `COM3` en Windows o `/dev/ttyACM0` en Linux/macOS). Deberías ver un prompt de Python REPL.
   - Para programas personalizados, verifica el comportamiento esperado (por ejemplo, un LED parpadeante, salida serie, etc.).
   - Si la unidad `RPI-RP2` reaparece, el flasheo pudo haber fallado. Prueba con un archivo `.uf2` diferente o revisa si hay problemas de hardware (por ejemplo, cable USB, chip de memoria flash).

### Resolución de Problemas
- **La Unidad No Aparece**: Asegúrate de que la Pico esté en modo BOOTSEL y de que el cable USB admita transferencia de datos. Intenta presionar BOOTSEL y luego presionar brevemente el botón RESET (si está disponible) mientras está conectada.
- **La Copia Falla o la Unidad Reaparece**: El archivo `.uf2` puede estar corrupto o la memoria flash podría ser defectuosa. Descarga un archivo `.uf2` nuevo o prueba con uno mínimo, como el de MicroPython. Si el problema persiste, usa `picotool` para diagnosticar:
  ```bash
  picotool info
  ```
  Instala `picotool` desde el [Raspberry Pi Pico SDK](https://github.com/raspberrypi/picotool).
- **No Hay Respuesta Después del Flasheo**: Si usas MicroPython/CircuitPython, asegúrate de que tu IDE (por ejemplo, Thonny) esté configurado en el puerto serie correcto. Para programas personalizados, verifica que el código se compiló correctamente.

### Ejemplo: Flasheando MicroPython
1. Descarga el archivo `.uf2` de MicroPython desde [micropython.org](https://micropython.org/download/rp2-pico/).
2. Mantén presionado BOOTSEL, enchufa la Pico y suelta BOOTSEL.
3. Abre tu explorador de archivos, encuentra la unidad `RPI-RP2` y copia el archivo `.uf2` en ella.
4. Espera a que la unidad desaparezca.
5. Abre Thonny IDE, selecciona el puerto serie de la Pico y comienza a programar en MicroPython.

Si necesitas ayuda con un archivo `.uf2` específico, una herramienta o una configuración (por ejemplo, instalando `picotool` o usando Thonny), ¡avísame!