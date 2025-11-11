---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Los Mejores Modelos de Codificación Económicos en OpenRouter
translated: true
type: note
---

### Mejores Modelos Económicos para Programación con Codex CLI via OpenRouter

Basado en benchmarks recientes, discusiones de usuarios y rankings de modelos a partir de 2025, aquí hay algunas de las mejores y más asequibles alternativas a GPT-5-Codex para tareas de programación en Codex CLI. GPT-5-Codex es ciertamente costoso (a menudo en el rango de $20-50 entrada / $60-150 salida por millón de tokens, dependiendo del proveedor), por lo que estas opciones se centran en ser rentables con un buen rendimiento en programación. El modelo de pago por uso de OpenRouter significa que solo pagas por los tokens procesados, y muchos tienen niveles gratuitos o tarifas muy bajas (menos de $1 por millón de tokens combinados para entrada/salida).

He priorizado modelos con puntuaciones altas en benchmarks de programación como SWE-Bench, HumanEval o Aider, siendo baratos o gratuitos. Los ID de los modelos están formateados para un uso fácil en tu `config.toml` (ej., `model = "proveedor/nombre-del-modelo"`). Para los precios exactos actuales, consulta la página de modelos de OpenRouter, ya que las tarifas pueden fluctuar ligeramente.

#### Recomendaciones Principales:
- **Grok Code Fast (xAI)**  
  ID del Modelo: `xai/grok-code-fast`  
  Por qué: Encabeza los rankings LLM de OpenRouter para programación, sobresale en velocidad y tareas agenticas (ej., #1 en la Olimpiada Internacional de Informática). A menudo es gratuito para uso básico, lo que lo convierte en el modelo más utilizado en la plataforma. Ideal para flujos de trabajo de programación iterativos.  
  Precio: Gratuito o ~$0.50/$2.00 por 1M de tokens (entrada/salida). Contexto: 128K tokens.

- **Kat Coder Pro (KwaiPilot)**  
  ID del Modelo: `kwaipilot/kat-coder-pro:free`  
  Por qué: Modelo de programación especializado con 73.4% en SWE-Bench Verified, cercano a los mejores modelos propietarios. Gratuito por tiempo limitado, ideal para razonamiento complejo y generación de código.  
  Precio: Gratuito (promoción). Contexto: 256K tokens, salida de hasta 32K.

- **DeepSeek Coder V3 (DeepSeek)**  
  ID del Modelo: `deepseek/deepseek-coder-v3`  
  Por qué: Excelente valor con ~71% en puntuaciones de codificación Aider, fuerte para implementación y depuración. Frecuentemente recomendado en foros para programación económica.  
  Precio: Muy barato (~$0.14/$0.28 por 1M). Contexto: 128K tokens.

- **Llama 4 Maverick (Meta)**  
  ID del Modelo: `meta/llama-4-maverick`  
  Por qué: El mejor en el nivel gratuito para calidad de programación e integración con VS Code (ej., con herramientas como RooCode). Funciona bien en tareas de código del mundo real.  
  Precio: Nivel gratuito disponible, o de bajo costo (~$0.20/$0.80 por 1M). Contexto: 128K tokens.

- **Mistral Devstral Small (Mistral)**  
  ID del Modelo: `mistral/devstral-small`  
  Por qué: Optimizado por precio, alto rendimiento y bueno en implementación de código. A menudo se combina con modelos más grandes para flujos de trabajo híbridos.  
  Precio: Barato (~$0.25/$1.00 por 1M). Contexto: 128K tokens.

- **Qwen3 235B (Qwen)**  
  ID del Modelo: `qwen/qwen3-235b`  
  Por qué: Alto rendimiento en benchmarks de programación, recomendado para configuraciones optimizadas en costos. Maneja bien proyectos de código a gran escala.  
  Precio: Asequible (~$0.50/$2.00 por 1M). Contexto: 128K tokens.

- **Gemini 2.5 Flash (Google)**  
  ID del Modelo: `google/gemini-2.5-flash`  
  Por qué: #3 en los rankings, rápido y de bajo costo para programación iterativa. Bueno para tareas multimodales si tu código involucra visualización de datos.  
  Precio: Barato (~$0.35/$1.05 por 1M). Contexto: 1M tokens.

Estos modelos son compatibles con OpenAI, por lo que funcionarán perfectamente en Codex CLI después de configurar el proveedor como "openrouter" y tu clave API. Comienza con los gratuitos como Grok Code Fast o Kat Coder para probar. Para uso específico de programación, revisa las puntuaciones de SWE-Bench: más alto significa mejor capacidad para resolver problemas reales de GitHub. Si necesitas más contexto o velocidad, combínalo con el enrutamiento de OpenRouter para el cambio automático a modelos más baratos.

Para integrar: En tu `config.toml`, añade un perfil como `[profiles codificador-economico]` con `model_provider = "openrouter"` y `model = "uno-de-los-IDs-de-arriba"`.

[Top AI Models on OpenRouter 2025: Performance vs Cost Guide](https://www.teamday.ai/blog/top-ai-models-openrouter-2025)  
[Best Budget Coding LLMs 2025: DeepSeek R1 vs Gemini vs GPT](https://llmx.de/blog/budget-coding-llms-2025/)  
[What are the best LLMs available on OpenRouter to use for coding](https://medium.com/@okreitz/what-are-the-best-llms-available-on-openrouter-to-use-for-coding-with-kilo-ca04e75a84ee)  
[Best Free AI Models You Can Use on OpenRouter](https://apidog.com/blog/free-ai-models/)  
[Top AI Coding Models in 2025](https://www.veerotech.net/blog/top-ai-coding-models-in-2025-boost-your-development-workflow-with-these-game-changers/)  
[LLM Rankings - OpenRouter](https://openrouter.ai/rankings)  
[Top 5 AI Coding Models of March 2025](https://dev.to/apipie-ai/top-5-ai-coding-models-of-march-2025-5f04)  
[Models - OpenRouter](https://openrouter.ai/models)  
[whats the best coding model on openrouter? - Reddit](https://www.reddit.com/r/RooCode/comments/1kdu7we/whats_the_best_coding_model_on_openrouter/)