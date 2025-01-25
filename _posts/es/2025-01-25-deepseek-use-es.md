---
audio: true
lang: es
layout: post
title: Uso de la API de DeepSeek
translated: true
---

En un mes, 15 millones de tokens me costaron aproximadamente 23.5 CNY.

Este fue mi uso en un día:

| Tipo              | Tokens    |
|-------------------|-----------|
| Entrada (Cache Hit)  | 946,816   |
| Entrada (Cache Miss) | 2,753,752 |
| Salida            | 3,100,977 |

El cálculo es el siguiente:

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

Por lo tanto, dependiendo de la tarea, el uso de tokens depende en gran medida de la entrada (cache miss) y la salida.

Este resultado coincide con el costo esperado.

[Precios de la API de DeepSeek](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg){: .responsive }
*Fuente: Captura propia*{: .caption }