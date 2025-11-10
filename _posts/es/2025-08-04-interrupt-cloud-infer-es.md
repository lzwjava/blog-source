---
audio: false
generated: true
image: false
lang: es
layout: post
title: Las Interrupciones No Cancelan La Inferencia En La Nube
translated: true
type: note
---

Cuando interrumpes (por ejemplo, con Ctrl-C) tu script de Python mientras está esperando en la llamada `generate_images()`, esto es aproximadamente lo que sucede:

1. **Comportamiento en el lado del cliente**
   – Tan pronto como terminas el proceso de Python, la conexión HTTP/gRPC subyacente se interrumpe.
   – La biblioteca cliente de GenAI normalmente detectará la tubería rota o el restablecimiento de conexión y generará una excepción (que verás en tu script).

2. **Qué sucede en el lado de Google**
   – Para cuando cancelas, tu solicitud ya ha llegado al servicio de inferencia de Google y ha sido encolada (o ya ha comenzado a ejecutarse).
   – La mayoría de los endpoints de inferencia en la nube **no** cancelan automáticamente el trabajo solo porque el cliente desapareció. Continuarán ejecutando tu trabajo de generación de imágenes hasta su finalización (consumiendo GPU/TPU y generando costos), aunque no haya una conexión activa para devolver el resultado.
   – Una vez que el trabajo finaliza, la imagen generada se descarta—no hay una callback para ti a menos que hayas configurado una operación de larga duración o un webhook.

3. **Cómo influye Nginx (u otro proxy)**
   – Si hay un proxy inverso de Nginx frente al servicio de inferencia, su comportamiento predeterminado es observar la conexión del cliente. Tan pronto como el cliente aborta, Nginx cierra su conexión ascendente al proceso de inferencia (enviando un FIN/RST).
   – El proceso ascendente entonces ve un socket roto cuando eventualmente intenta escribir la respuesta. En ese momento puede registrar un error de E/S, pero—crucialmente— **no** rebobina y detiene el cálculo que solicitaste; simplemente no puede entregar los bytes.
   – Puedes ajustar la directiva `proxy_ignore_client_abort` de Nginx—si la configuras como `on`, Nginx mantendrá la conexión ascendente activa incluso después de que el cliente se desconecte (lo que puede permitirte terminar completamente de escribir registros u otra limpieza).

4. **Conclusiones clave para tu script**

   * **Las interrupciones no "deshacen"** o cancelan el modelo en los servidores de Google—seguirás siendo facturado por la inferencia completa.
   * Si necesitas una inferencia cancelable, tendrías que usar un patrón diferente: por ejemplo,

     1. Enviar un lote no bloqueante o una operación de larga duración,
     2. Consultar su estado o cancelarlo explícitamente mediante una llamada API separada.

En resumen: terminar tu script a los 5 s detiene tu espera local y cierra el socket, pero la inferencia de Google aún se ejecuta hasta su finalización en su hardware (y Nginx o similar simplemente descartará la respuesta a ninguna una vez que esté lista).