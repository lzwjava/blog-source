---
audio: false
generated: true
image: false
lang: es
layout: post
model: google/gemini-2.5-flash
title: Extracción de los últimos diez minutos de audio
translated: true
type: note
---

Para obtener los últimos 10 minutos del archivo de audio `lobby-zh.ogg`, necesitas usar la siguiente información:

1.  **Duración Total:** La duración del archivo de entrada es `00:33:34.40`.
2.  **Longitud del Segmento Deseado:** 10 minutos (o 600 segundos).
3.  **Cálculo del Tiempo de Inicio:** Necesitas calcular el punto 10 minutos *antes* del final del archivo.

### Cálculo

*   Duración total en segundos:
    $$(33 \times 60) + 34.40 = 1980 + 34.40 = 2014.40 \text{ segundos}$$
*   Tiempo de inicio:
    $$2014.40 \text{ segundos} - 600 \text{ segundos} = 1414.40 \text{ segundos}$$

En formato `HH:MM:SS.sss`:
$$1414.40 \text{ segundos} = 23 \text{ minutos y } 34.40 \text{ segundos} \quad (1414.40 / 60 = 23.5733\dots)$$
$$\text{Tiempo de Inicio} = 00:23:34.40$$

### Comando FFmpeg

Usarás la opción de entrada `-ss` (buscar posición) combinada con la opción `-t` (duración).

1.  `-ss 00:23:34.40`: Establece la posición de inicio para la extracción.
2.  `-t 00:10:00`: Establece la duración del segmento de salida a exactamente 10 minutos.

```bash
ffmpeg -i lobby-zh.ogg -ss 00:23:34.40 -t 00:10:00 last_10_minutes.ogg
```

**Nota:** Si deseas usar la configuración original de bitrate/códec del archivo de salida, puedes agregar `-c copy` para un procesamiento más rápido:

```bash
ffmpeg -i lobby-zh.ogg -ss 00:23:34.40 -t 00:10:00 -c copy last_10_minutes_copy.ogg
```