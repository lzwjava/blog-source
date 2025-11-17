---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Monitoreo del Uso de GPU con nvidia-smi
translated: true
type: note
---

Para monitorear el uso de la GPU a lo largo del tiempo con `nvidia-smi`, solo necesitas el flag de bucle:

**Actualización en vivo básica**

```
nvidia-smi -l 1
```

Esto se actualiza cada 1 segundo. Puedes reemplazar el `1` con cualquier intervalo en segundos.

**Si quieres estadísticas más detalladas (uso por proceso)**

```
nvidia-smi pmon -s um -d 1
```

Esto muestra la utilización de la GPU (`u`) y la memoria (`m`) por proceso cada segundo.

**Si quieres estadísticas completas de la GPU repetidamente**

```
nvidia-smi --query-gpu=timestamp,utilization.gpu,utilization.memory,memory.used,memory.total --format=csv -l 1
```

Esto imprime una línea compacta cada segundo con la utilización y la memoria.

Dime si quieres que la salida se guarde en un archivo o necesitas un formato personalizado.