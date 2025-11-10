---
audio: false
generated: true
image: false
lang: es
layout: post
title: Mejores Modelos para la Guía de Limpieza de Transcripciones
translated: true
type: note
---

Excelente caso de uso. Para la **limpieza de transcripciones largas con formato estricto y "sin comentarios adicionales"**, esto es lo que funciona mejor actualmente en OpenRouter, por escenario.

**Caballo de batalla rápido y económico (EN/zh, archivos largos): DeepSeek-V3.1**
Fuerte en seguir instrucciones, maneja un contexto de 128k, y puedes desactivar el "razonamiento" para mayor velocidad o activarlo cuando el texto esté desordenado. Buen rendimiento bilingüe para la eliminación de muletillas y etiquetas de hablante consistentes. ([DeepSeek API Docs][1], [OpenRouter][2])

**Entrevistas con mucho chino y coloquialismos: Kimi K2 Instruct**
El K2 (MoE) de Moonshot es particularmente fluido con la jerga y el estilo chino; ideal para transcripciones principalmente en chino manteniendo los sustantivos técnicos intactos. ([OpenRouter][3])

**Mayor cumplimiento en instrucciones de edición: Claude Sonnet (3.7/4)**
La línea Sonnet de Anthropic es excelente en "solo generar el texto refinado, sin metadatos", y tiende a ser conservadora con los cambios de significado—ideal para tus restricciones de listas de pasos. Usa Sonnet 4 si está disponible; la 3.7 también funciona bien. ([OpenRouter][4])

**Sesiones ultra largas o pasadas únicas de proyectos completos: GPT-5**
Cuando quieres manejar contextos muy grandes y mantener las alucinaciones bajas, GPT-5 es la opción más segura entre los modelos frontera en OpenRouter (listado con un contexto muy grande; razonamiento y edición sólidos). Úsalo para transcripciones maratónicas o pasadas finales de "pulido". ([OpenRouter][5])

**También fuerte, pero cuidado con los perfiles de costo: Gemini 2.5 Pro**
Muy capaz en razonamiento y edición de contexto largo. Es sólido para el refinamiento, pero considera el precio/cuotas dependiendo de tu ruta de proveedor. ([OpenRouter][6])

---

### Una receta práctica de enrutamiento (sin tablas)

* **≤128k tokens, mezcla EN/zh, la velocidad importa:** DeepSeek-V3.1 (sin pensamiento). Cambia a pensamiento solo cuando los párrafos sean caóticos. ([DeepSeek API Docs][1])
* **Transcripciones principalmente en chino:** Kimi K2 Instruct. ([OpenRouter][3])
* **Comportamiento de "editor" estricto (sin comentarios), tono legal/financiero:** Claude Sonnet. ([OpenRouter][4])
* **Archivos gigantescos o pulido final de una sola pasada:** GPT-5. ([OpenRouter][5])

---

### Ajustes rápidos de código para hacer esto robusto

* **Hacer el modelo seleccionable**: añadir el flag CLI `--model`; por defecto `deepseek-v3.1`.
* **Auto-enrutar por tamaño/idioma**: detectar el conteo de tokens y la proporción de zh; elegir K2 para contenido muy zh, GPT-5 para entradas enormes, Claude para el modo "edición estricta".
* **Alternar razonamiento** (DeepSeek): añadir un parámetro para configurar `reasoning.enabled` en tu llamada a OpenRouter para pasajes difíciles. ([DeepSeek API Docs][1])
* **Corregir errores menores**: ese `print(".1f")` extraviado; y ampliar la regex de etiquetas de hablante para permitir `A：` (dos puntos de ancho completo) y variantes sin espacios.
* **Barreras de protección**: si el delta de longitud es >10%, reintentar automáticamente con un recordatorio de "no eliminar contenido"; si no se encuentran `A:`/`B:`, reintentar automáticamente con un empujón de "etiquetar hablantes".

Si quieres, puedo reescribir tu script para añadir el flag `--model` y la lógica de enrutamiento inteligente ahora mismo.

[1]: https://api-docs.deepseek.com/quick_start/pricing?utm_source=chatgpt.com "Models & Pricing"
[2]: https://openrouter.ai/deepseek/deepseek-chat-v3.1?utm_source=chatgpt.com "DeepSeek V3.1 - API, Providers, Stats"
[3]: https://openrouter.ai/moonshotai/kimi-k2?utm_source=chatgpt.com "Kimi K2 - API, Providers, Stats"
[4]: https://openrouter.ai/anthropic/claude-3.7-sonnet?utm_source=chatgpt.com "Claude 3.7 Sonnet - API, Providers, Stats"
[5]: https://openrouter.ai/openai/gpt-5?utm_source=chatgpt.com "GPT-5 - API, Providers, Stats"
[6]: https://openrouter.ai/google/gemini-2.5-pro?utm_source=chatgpt.com "Gemini 2.5 Pro - API, Providers, Stats"