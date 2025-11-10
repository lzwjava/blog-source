---
audio: false
generated: true
image: false
lang: es
layout: post
title: OpenRouter frente al Costo de la API Directa
translated: true
type: note
---

Sí, usar las APIs de OpenRouter para acceder a los mismos modelos generalmente es más costoso que usar las APIs oficiales directamente de proveedores como DeepSeek, Mistral, Google (para Gemini) o xAI (para Grok). OpenRouter afirma transferir la tarificación del proveedor subyacente sin agregar un margen de ganancia sobre los costos de inferencia en sí, pero cobra tarifas adicionales que aumentan el gasto total:

- Una tarifa del 5.5% (con un mínimo de $0.80) al comprar créditos mediante métodos de pago estándar, más un 5% adicional para pagos con criptomonedas.
- Incluso si usas tus propias claves API (BYOK) para proveedores compatibles, OpenRouter deduce una tarifa del 5% (basada en su costo estimado del modelo) de tus créditos de OpenRouter.

Estas tarifas hacen que OpenRouter sea efectivamente un 5-5.5% más caro que acceder directamente, además de cualquier mínimo fijo, dependiendo de tu uso y método de pago. El acceso directo evita estos extras, ya que solo pagas las tarifas por token del proveedor.

### Ejemplos de Comparación de Costos
Aquí hay una comparación aproximada basada en datos de precios disponibles (en USD por millón de tokens; ten en cuenta que las tarifas pueden variar según la versión del modelo, la hora del día, el caching o la región—siempre verifica los sitios oficiales para obtener los detalles más recientes). Las tarifas base por token de OpenRouter coinciden con las de los proveedores (transferencia directa), pero agregan las tarifas mencionadas anteriormente.

- **DeepSeek**:
  - Directo: Entrada ~$0.14–$0.55 (acierto/fallo de cache), Salida ~$1.10–$2.19 (varía según el modelo y períodos de descuento).
  - OpenRouter: Mismas tarifas base + tarifas del 5–5.5%.

- **Mistral**:
  - Directo: Entrada ~$2.00 (para Large 2), Salida ~$6.00 (estimado basado en tarifas combinadas; modelos anteriores como Small eran ~$0.15 entrada/$0.50 salida).
  - OpenRouter: Mismas tarifas base + tarifas del 5–5.5%.

- **Gemini (Google)**:
  - Directo: Varía ampliamente según el modelo (ej., Gemini 1.5 Pro: Entrada $1.25–$2.50, Salida $5.00–$10.00; Gemini 1.5 Flash: Entrada $0.075–$0.15, Salida $0.30–$0.60).
  - OpenRouter: Mismas tarifas base + tarifas del 5–5.5% (BYOK puede ser compatible con Google).

- **Grok (xAI)**:
  - Para detalles sobre los precios y el acceso a la API de Grok, visita https://x.ai/api. Según información pública, las tarifas son aproximadamente Entrada $3.00/Salida $15.00 para Grok-3/Grok-4, o Entrada $0.30/Salida $0.50 para Grok-3-mini.
  - OpenRouter: Mismas tarifas base + tarifas del 5–5.5% (BYOK no se menciona típicamente para xAI).

Si tu uso es de alto volumen, las tarifas porcentuales se acumulan rápidamente. Para uso bajo o pruebas, la diferencia podría ser mínima, pero el acceso directo sigue siendo más barato. El valor de OpenRouter radica en su API unificada y funciones de enrutamiento, lo que podría justificar el costo adicional por conveniencia.

[OpenRouter FAQ](https://openrouter.ai/docs/faq)
[DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing)
[Mistral AI Pricing](https://mistral.ai/pricing)
[Google Gemini API Pricing](https://ai.google.dev/pricing)
[xAI API](https://x.ai/api)
[Mistral Large 2 Analysis](https://artificialanalysis.ai/models/mistral-large-2)
[DeepSeek Pricing Guide](https://team-gpt.com/blog/deepseek-pricing/)