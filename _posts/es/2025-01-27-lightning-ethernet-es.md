---
audio: true
lang: es
layout: post
title: Adaptador de Lightning a Ethernet
translated: true
---

Recientemente probé un nuevo producto que nunca había usado antes. Me costó alrededor de 44 CNY en JD.com. Productos similares cuestan alrededor de 15 USD en Walmart.com.

Funciona perfectamente y no se necesitan configuraciones adicionales. Un elemento de menú "Ethernet" aparece después de conectar el adaptador.

Utilicé la aplicación Speedtest para iOS para probar la velocidad. Los resultados se muestran a continuación.

| Tipo de Red                     | Distancia   | Velocidad de Descarga (MBPS) | Velocidad de Subida (MBPS) | Línea             |
|----------------------------------|------------|-----------------------|---------------------|------------------|
| Módem -> Router TP-LINK -> Teléfono | alrededor de 30m | 2.90                  | 4.82                | Guangzhou -> Macao |
| Módem -> Cable -> Teléfono          | alrededor de 30m | 84.9                  | 59.7                | Guangzhou -> Macao |

En una prueba, los resultados de la capacidad de respuesta del ping (ms) se muestran a continuación:

| Métrica   | Valor | Jitter |
|----------|-------|--------|
| Inactivo     | 33    | 68     |
| Descarga | 1885  | 110    |
| Subida   | 127   | 54     |

Esta es una prueba algo ingenua. Sospecho que una de las razones de la diferencia en las velocidades es que la conexión desde el Módem -> Router TP-LINK es de aproximadamente 20m, y la conexión desde el Router TP-LINK -> Teléfono es de aproximadamente 10m. Además, el Router TP-LINK utiliza un puente inalámbrico para conectarse al módem.

Lo interesante es que si conectas tanto Wi-Fi como Ethernet, no hay forma de priorizar uno sobre el otro. Solo puedes usar Ethernet en esta configuración. Si deseas usar Wi-Fi, tienes que desconectar el adaptador Ethernet.

{: .centered }
![](assets/images/lightning/l1.jpg){: .responsive }
*Fuente: iOS*{: .caption }

{: .centered }
![](assets/images/lightning/l2.jpg){: .responsive }
*Fuente: Walmart.com*{: .caption }

{: .centered }
![](assets/images/lightning/n.jpg){: .responsive }
*Fuente: network_plot.py*{: .caption }