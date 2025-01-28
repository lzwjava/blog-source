---
audio: true
lang: es
layout: post
title: Uso de la API DeepSeek
translated: true
---

## DeepSeek

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

{: .centrado }
![](assets/images/deepseek/d.jpg)
*Fuente: Captura de pantalla propia*{: .caption }

## Mistral

Modelo: `mistral-large-2411`

En un día, mi cuenta de Mistral consumió los siguientes tokens:

| Tipo   | Tokens  | Costo (USD) |
|--------|---------|------------|
| Total  | 772,284 | 3.44       |
| Salida | 474,855 | 2.85       |
| Entrada| 297,429 | 0.59       |

Los precios para Mistral Large son los siguientes:

*   Entrada: 2 USD por millón de tokens
*   Salida: 6 USD por millón de tokens