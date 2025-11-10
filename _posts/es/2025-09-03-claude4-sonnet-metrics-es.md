---
audio: false
generated: true
image: false
lang: es
layout: post
title: Métricas de Finalización de Claude 4 Sonnet Explicadas
translated: true
type: note
---

Versión corta: terminó normalmente.
`finish_reason: "stop"` significa que el modelo llegó al final natural de su respuesta (encontró una secuencia de parada como el token de fin de asistente) y **no** se topó con un límite de longitud, un error o una cancelación.

Esto es lo que te dice el resto del registro, en lenguaje sencillo:

* **Modelo y ruta**
  Llamaste a **anthropic/claude-4-sonnet-20250522** a través de **Google Vertex** (`provider_name: "Google"`). Por eso ves una entrada `provider_responses` con estado 200.

* **Tiempos / velocidad**

  * `latency: 2850` → ~2.85 s hasta que apareció el **primer token**.
  * `generation_time: 76365` → unos **76.4 s** en total para terminar la respuesta.
  * Con `tokens_completion: 2376`, eso es aproximadamente **31 tokens/seg** de rendimiento durante toda la generación (2376 ÷ 76.4 ≈ 31.1).

* **Recuentos de tokens (dos conjuntos)**

  * `tokens_prompt: 8446`, `tokens_completion: 2376` → los recuentos de tu agregador.
  * `native_tokens_prompt: 9007`, `native_tokens_completion: 2511` → la propia contabilidad/tokenizador del **proveedor**. Estos suelen diferir debido a diferentes tokenizadores, wrappers del sistema o tokens de control ocultos.
  * `native_tokens_reasoning: 0` → esta ejecución no usó un medidor de "tokens de razonamiento" (algunos proveedores exponen esto cuando un modo especial de razonamiento está activo).
  * `native_tokens_cached: 0` → no hubo acierto de caché del prompt.

* **Streaming y cancelación**

  * `streamed: true` → los tokens se transmitieron en flujo continuo (streaming) hacia ti.
  * `cancelled: false` → no lo interrumpiste.

* **¿Por qué no "length"?**
  Si hubiera alcanzado el límite máximo de tokens, verías `finish_reason: "length"`. No fue tu caso, así que el modelo completó la respuesta antes de cualquier límite.

* **¿Cuándo sucedió esto?**
  `created_at: "2025-09-02T17:26:45.92824+00:00"` (UTC). En tu zona horaria (Asia/Taipei, UTC+8) eso es **2025-09-03 01:26:45**.

* **Campos de costos/uso**

  * `usage: 0.064686` → la métrica de costo/uso de tu sistema (las unidades dependen de tu capa de facturación).
  * Varios campos `null` simplemente significan que tu router no registró detalles adicionales (latencia de moderación, resultados de búsqueda, etc.).

* **Miscelánea**

  * `finish_reason: "stop"` (de nuevo) es la clave: parada normal mediante token de parada.
  * `origin: ""`, `app_id: null` → sin etiqueta de aplicación específica.
  * `is_byok: false` → no fue una llamada con clave propia (bring-your-own-key).

Si quieres, pega un segundo ejemplo donde hayas visto `length` o `cancelled`, y los contrastaré línea por línea (sin tablas).