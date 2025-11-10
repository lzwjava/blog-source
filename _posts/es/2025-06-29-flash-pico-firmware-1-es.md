---
audio: false
generated: true
lang: es
layout: post
title: Flashear Pico con Archivo UF2
translated: true
type: note
---

Para flashear el archivo `RPI_PICO-20250415-v1.25.0.uf2` en tu Raspberry Pi Pico, que está montado en `/media/lzw/RPI-RP2`, usa el siguiente comando:

```bash
cp ~/Downloads/RPI_PICO-20250415-v1.25.0.uf2 /media/lzw/RPI-RP2/
```

### Explicación
- `cp`: Copia el archivo.
- `~/Downloads/RPI_PICO-20250415-v1.25.0.uf2`: La ruta a tu archivo `.uf2` en el directorio de Descargas.
- `/media/lzw/RPI-RP2/`: El punto de montaje de la unidad `RPI-RP2` del Pico, como se muestra en tu salida.

### Después de Ejecutar el Comando
- El archivo `.uf2` se copiará al Pico, y el dispositivo flasheará el firmware automáticamente.
- La unidad `RPI-RP2` se desmontará (desaparecerá) una vez que el flasheo se complete, lo que indica éxito.
- Si la unidad reaparece, el flasheo puede haber fallado. Verifica que el archivo `.uf2` sea válido o prueba con un cable/puerto USB diferente.

Si encuentras problemas o necesitas más ayuda, ¡avísame!