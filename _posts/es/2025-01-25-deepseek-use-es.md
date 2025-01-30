---
audio: false
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
| Input (Cache Hit)  | 946,816   |
| Input (Cache Miss) | 2,753,752 |
| Output            | 3,100,977 |

El cálculo es el siguiente:

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

Por lo tanto, dependiendo de la tarea, el uso de tokens depende en gran medida del input (cache miss) y del output.

Este resultado coincide con el costo esperado.

[DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*Fuente: Captura de pantalla propia*{: .caption }

## Mistral

Los precios para los modelos Mistral son los siguientes:

| Modelo                | Input (USD por millón de tokens) | Output (USD por millón de tokens) |
|-----------------------|--------------------------------|---------------------------------|
| `mistral-large-2411`  | 2                              | 6                               |
| `mistral-small-latest`| 0.2                           | 0.6                             |

En un día, el uso de mi cuenta de Mistral fue el siguiente (Modelo: `mistral-large-2411`):

| Tipo   | Tokens  | Costo (USD) |
|--------|---------|------------|
| Total  | 772,284 | 3.44       |
| Output | 474,855 | 2.85       |
| Input  | 297,429 | 0.59       |

Para el modelo `mistral-small-2409`, el uso total fue de 1,022,407 tokens.

Asumiendo que 1/3 de estos fueron tokens de entrada y 2/3 fueron tokens de salida:

Había 340,802 tokens de entrada y 681,605 tokens de salida.

Por lo tanto, el costo total se calcula como 340,802 * 0.2 / 1,000,000 + 681,605 * 0.6 / 1,000,000 = 0.07 + 0.41 = 0.48 USD.

La consola de Mistral informa un costo total de uso de 0.43 USD, que aproximadamente coincide con nuestro cálculo.