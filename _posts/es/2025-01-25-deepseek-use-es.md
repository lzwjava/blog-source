---
audio: false
generated: true
lang: es
layout: post
title: Uso de la API de Deepseek y Mistral
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

[DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*Fuente: Captura de pantalla propia*{: .caption }

## Mistral

La tarificación para los modelos Mistral es la siguiente:

| Modelo                 | Entrada (USD por millón de tokens) |  Salida (USD por millón de tokens) |
|-----------------------|------------------------------|---------------------------------|
| `mistral-large-2411`  | 2                            | 6                               |
| `mistral-small-latest`| 0.2                          | 0.6                             |

En un día, mi uso de la cuenta Mistral fue el siguiente (Modelo: `mistral-large-2411`):

| Tipo   | Tokens  | Costo (USD) |
|--------|---------|------------|
| Total  | 772,284 | 3.44       |
| Salida | 474,855 | 2.85       |
| Entrada | 297,429 | 0.59       |

Para el modelo `mistral-small-2409`, el uso total fue de 1,022,407 tokens.

Supongamos que 1/3 de estos eran tokens de entrada y 2/3 eran tokens de salida:

Hubo 340,802 tokens de entrada y 681,605 tokens de salida.

Por lo tanto, el costo total se calcula como 340,802 * 0.2 / 1,000,000 + 681,605 * 0.6 / 1,000,000 = 0.07 + 0.41 = 0.48 USD.

La consola de Mistral informa un costo de uso total de 0.43 USD, que aproximadamente coincide con nuestro cálculo.

## Grok

| Modelo         | Entrada (USD por millón de tokens) | Salida (USD por millón de tokens) |
|---------------|------------------------------|---------------------------------|
| `grok-2-latest` | 2                            | 10                              |