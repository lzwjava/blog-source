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
| Entrada (acierto en caché)  | 946,816   |
| Entrada (fallo en caché) | 2,753,752 |
| Salida            | 3,100,977 |

El cálculo es el siguiente:

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

Por lo tanto, dependiendo de la tarea, el uso de tokens depende en gran medida de la entrada (fallo en caché) y la salida.

Este resultado coincide con el costo esperado.

[Precios de la API de DeepSeek](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centrado }
![](assets/images/deepseek/d.jpg)
*Fuente: Captura de pantalla propia*{: .pie-de-imagen }

## Mistral

En un día, mi uso de la cuenta de Mistral fue el siguiente (Modelo: `mistral-large-2411`):

| Tipo   | Tokens  | Costo (USD) |
|--------|---------|------------|
| Total  | 772,284 | 3.44       |
| Salida | 474,855 | 2.85       |
| Entrada| 297,429 | 0.59       |

Los precios para los modelos de Mistral son los siguientes:

| Modelo                 | Entrada (USD por millón de tokens) | Salida (USD por millón de tokens) |
|-----------------------|------------------------------|---------------------------------|
| `mistral-large-2411`  | 2                            | 6                               |
| `mistral-small-latest`| 0.2                          | 0.6                             |