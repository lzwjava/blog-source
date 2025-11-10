---
audio: false
generated: true
image: false
lang: es
layout: post
title: Métricas de Tiempo de Ejecución de Claude Sonnet Explicadas
translated: true
type: note
---

Lo que estás viendo son **métricas de tiempo de ejecución** de la inferencia de `anthropic/claude-sonnet-4` a través de Google Vertex AI. Permíteme desglosarlo:

* **Latencia del primer token (2.85s):**
  Este es el retraso entre enviar tu prompt y recibir el primer token de salida. Incluye la latencia de red, la cola de solicitudes y el cálculo inicial del modelo. Para modelos grandes como Claude Sonnet, un par de segundos es normal.

* **Rendimiento (32.9 tokens/seg):**
  Después de que se genera el primer token, el modelo transmite los tokens subsiguientes. 32.9 tokens por segundo es una tasa saludable — no es la más rápida posible, pero es buena para un modelo grande. El rendimiento puede variar dependiendo del tamaño del modelo, la carga en el proveedor (Vertex) y la longitud de tu prompt.

* **Motivo de finalización (stop):**
  Esto simplemente indica que el modelo se detuvo naturalmente cuando llegó al final de su texto generado (en lugar de alcanzar un límite de longitud, un corte o un error).

Entonces, **"¿por qué?"** → porque estos números describen las características normales de inferencia de un LLM grande cuando se ejecuta a través de Vertex:

* Se espera cierta latencia inicial (compilación, optimización, enrutamiento).
* El rendimiento se estabiliza una vez que comienza la generación.
* Stop es la condición de finalización prevista.

¿Quieres que también compare estos números con los rangos de rendimiento típicos para otros modelos (como GPT-5, Gemini Pro, DeepSeek, etc.) para que puedas ver si esto fue "rápido" o "lento" en contexto?