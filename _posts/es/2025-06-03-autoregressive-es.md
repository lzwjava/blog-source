---
audio: false
generated: true
lang: es
layout: post
title: Generación de Modelos Autoregresivos
translated: true
type: note
---

En el contexto de modelos como GPT (Generative Pre-trained Transformer), el término "autoregresivo" se refiere al método por el cual el modelo genera secuencias de salida. Específicamente, significa que el modelo genera cada elemento de una secuencia uno a la vez, utilizando sus salidas anteriores como contexto de entrada adicional para generar el siguiente elemento.

Aquí hay un desglose de cómo funciona el proceso autoregresivo en dichos modelos:

1.  **Generación Secuencial**: El modelo genera texto de manera secuencial. Comienza con una entrada inicial (a menudo llamada *prompt*) y genera un *token* (que puede ser una palabra, parte de una palabra o un carácter) a la vez.

2.  **Dependencia de los *Tokens* Anteriores**: Para cada nuevo *token* que genera, el modelo considera todos los *tokens* generados previamente. Esto significa que la salida en cada paso depende de las salidas de todos los pasos anteriores.

3.  **Bucle de Retroalimentación**: El modelo utiliza un bucle de retroalimentación donde la salida del modelo en el paso de tiempo \\( t \\) se realimenta como entrada en el paso de tiempo \\( t+1 \\). Esto permite al modelo mantener coherencia y contexto en secuencias más largas.

4.  **Distribución de Probabilidad**: En cada paso, el modelo genera una distribución de probabilidad sobre los posibles *tokens* siguientes y selecciona uno basado en esta distribución (a menudo utilizando técnicas como *sampling* o seleccionando el *token* más probable).

En resumen, "autoregresivo" en el contexto de GPT y modelos similares significa que el modelo genera secuencias paso a paso, donde cada paso depende de los anteriores, permitiéndole producir texto coherente y relevante en su contexto.