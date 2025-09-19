---
audio: false
generated: false
image: false
lang: es
layout: post
title: Adaptador de Rayo a Ethernet
translated: true
---

Recientemente probé un nuevo producto que nunca había usado antes. Me costó aproximadamente 44 CNY en JD.com. Productos similares cuestan alrededor de 15 USD en Walmart.com.

Funciona perfectamente y no se necesitan ajustes adicionales. Aparece un elemento de menú "Ethernet" después de conectar el adaptador.

Usé la aplicación Speedtest iOS para probar la velocidad. Los resultados se muestran a continuación.

| Tipo de Red                     | Distancia   | Velocidad de Descarga (MBPS) | Velocidad de Subida (MBPS) | Línea             |
|----------------------------------|------------|-------------------------------|----------------------------|------------------|
| Modem -> TP-LINK Router -> Teléfono | alrededor de 30m | 2.90                   | 4.82                      | Guangzhou -> Macao |
| Modem -> Cable -> Teléfono       | alrededor de 30m | 84.9                   | 59.7                      | Guangzhou -> Macao |

En una prueba, los resultados de la respuesta del ping (ms) se muestran a continuación:

| Métrica  | Valor | Jitter |
|----------|-------|--------|
| Ocioso   | 33    | 68     |
| Descarga | 1885  | 110    |
| Subida   | 127   | 54     |

Esta es una prueba algo ingenua. Sospecho que una razón para la diferencia en las velocidades es que la conexión de Modem -> TP-LINK Router es de aproximadamente 20m, y la conexión de TP-LINK Router -> Teléfono es de aproximadamente 10m. Además, el TP-LINK Router usa un puente inalámbrico para conectarse al módem.

Speedtest es una herramienta útil. Si usas un servidor en Alibaba Cloud y configuras el ancho de banda a 5Mbps, entonces usar la aplicación para probarlo dará resultados de alrededor de 5Mbps.

Lo interesante es que si conectas tanto Wi-Fi como Ethernet, no hay forma de priorizar uno sobre el otro. Solo puedes usar Ethernet en esta configuración. Si quieres usar Wi-Fi, debes desenchufar el adaptador Ethernet.