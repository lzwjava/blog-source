---
audio: false
date: 2025-09-07
generated: true
image: false
lang: es
layout: post
title: Optimización de su Enrutador de Código para Múltiples Modelos
translated: true
type: note
---

Respuesta corta: sí—tu "enrutador de múltiples modelos" definitivamente puede tener un rendimiento inferior en comparación con una pila estrechamente integrada como Codex (el asistente de código de OpenAI) que está ajustada de extremo a extremo en una familia de modelos más un contexto profundo del IDE. He aquí por qué y cómo solucionarlo rápidamente.

### Por qué Codex puede sentirse mejor

* **Un cerebro por tarea.** Permanecer en un único modelo preserva su plan latente y estilo de codificación. Saltar entre modelos a mitad de tarea reinicia ese plan y a menudo introduce convenciones conflictivas.
* **Integración vertical.** Codex (OpenAI) controla modelo → llamadas a herramientas → índice del repositorio → tests → ediciones en línea. Ese circuito cerrado le proporciona señales más ricas (gráfico de símbolos, mapas de calor de archivos, tests fallidos) con menos latencia por código de unión.
* **Alineación de prompt y política.** Sus prompts, formateadores de código y heurísticas de "crear un diff mínimo y compilable" están co-diseñados para la familia GPT-5. Un enrutador general puede especificar incorrectamente la temperatura, las secuencias de parada o el formato del parche para algunos modelos.
* **Latencia/rendimiento.** Cada salto extra (proxy, middleware de OpenRouter, negociación de modelos) añade fluctuación. Los flujos de trabajo de codificación son de retroalimentación rápida; 300–800 ms de latencia añadida por turno perjudica notablemente el "flujo".
* **Calidad del contexto.** Las integraciones de IDE que computan un mapa del repositorio (topología de archivos, símbolos, cambios recientes) superan a "simplemente volcar contexto largo". Los contextos largos sin estructura desperdician tokens y diluyen la atención.

### Qué en tu configuración probablemente te está perjudicando

* **Progresión descontrolada de modelos.** Estás mezclando modelos generalistas, codificadores y de razonamiento. Las variantes de "razonamiento" (ej., `claude-3.7-sonnet:thinking`, `deepseek-r1`) son geniales para pruebas pero más lentas y verbosas para ediciones de código.
* **Incompatibilidad de la ruta por defecto.** `default: "openrouter,x-ai/grok-code-fast-1"` parece indicar que quieres Grok Code Fast, pero no está listado en tu array `models`. Eso puede causar una falla silenciosa e inconsistencia.
* **Intenciones sin alcance.** Un valor "default" para todo significa que las pequeñas ediciones, refactorizaciones pesadas y lecturas de contexto largo luchan por pasar a través de la misma ruta.
* **Deriva de temperatura/formato.** Si no aplicas temperatura baja + formato de parche estricto por modelo, las salidas varían enormemente entre proveedores.

### Haz que tu enrutador se sienta "similar a Codex"

1.  **Elige un modelo principal y mantente en él por tarea.** Elige un buen codificador como predeterminado (ej., `openai/gpt-5` o `x-ai/grok-code-fast-1` o `qwen/qwen3-coder`) y cambia solo por razones claras (contexto muy largo o matemáticas pesadas).
2.  **Divide por intención (no por marca).**

    *   *Edición pequeña / solución rápida:* modelo rápido (GPT-5-mini o Gemini-Flash).
    *   *Refactorización / cambio multiarchivo:* GPT-5 (o Claude Sonnet 3.7 sin razonamiento).
    *   *Lectura de contexto ultra largo:* Kimi-K2.
    *   *Razonamiento complejo antes de codificar:* DeepSeek-R1 para esbozar → pasar a un modelo codificador para producir el parche.
3.  **Aplica un contrato de parche estricto.** Pide siempre un diff unificado o un JSON explícito "ApplyPatch" con rutas de archivo + fragmentos. Rechaza cualquier otra cosa y repregunta automáticamente.
4.  **Reduce la aleatoriedad para código.** `temperature: 0–0.2`, sin penalizaciones de frecuencia/presencia, y limita `top_p` ~0.9.
5.  **Proporciona un mapa del repositorio, no solo tokens.** Proporciona un índice de símbolos compacto: puntos de entrada, clases/funciones clave, objetivos de test, diffs recientes. Esto es mejor que volcar 200k tokens de archivos en bruto.
6.  **Mantén el bucle de herramientas ajustado.** Un modelo propone un parche → ejecutas build/tests/linters → devuelves solo los fallos al *mismo* modelo para iterar. Evita cambiar de modelo a mitad del bucle.
7.  **Reduce la lista de modelos.** Mantén un máximo de 3–5. Cada extra aumenta la varianza y los errores de enrutamiento.
8.  **Elimina los modelos de "razonamiento" de las rutas críticas.** Úsalos solo para producir un breve plan de diseño, luego cambia a un codificador para las ediciones reales.

### Una configuración más ligera (idea lista para usar; adapta los nombres a tu framework)

```json
{
  "PROXY_URL": "http://127.0.0.1:7890",
  "LOG": true,
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "",
      "models": [
        "openai/gpt-5",
        "openai/gpt-5-mini",
        "x-ai/grok-code-fast-1",
        "moonshotai/kimi-k2",
        "anthropic/claude-3.7-sonnet",
        "qwen/qwen3-coder"
      ],
      "transformer": {"use": ["openrouter"]}
    }
  ],
  "Router": {
    "default": "openrouter,openai/gpt-5",
    "quickEdit": "openrouter,openai/gpt-5-mini",
    "refactor": "openrouter,openai/gpt-5",
    "reasonPlan": "openrouter,anthropic/claude-3.7-sonnet",
    "longContext": "openrouter,moonshotai/kimi-k2",
    "longContextThreshold": 220000,
    "webSearch": "openrouter,qwen/qwen3-coder"
  }
}
```

### Andamiajes de prompt que estabilizan las salidas (sin tablas)

*   **Sistema:** "Eres un ingeniero de software senior. Produce parches mínimos y compilables. Mantén el estilo consistente con el repositorio. Si no estás seguro, haz una única pregunta aclaratoria, de lo contrario, procede."
*   **Reglas:** "SALIDA SOLO un diff unificado (formato git). Nunca incluyas comentarios. Si un archivo no existe, créalo e inclúyelo en el diff. Preserva las cabeceras de licencia."
*   **Bloque de contexto:** mapa del repositorio (archivos, símbolos clave), errores actuales, objetivos de test.
*   **Bucle de herramienta:** después del diff, ejecuta automáticamente `build + tests + lints`; devuelve solo los fallos al mismo modelo.

### Higiene práctica

*   Reduce tu lista de modelos y corrige el valor por defecto a un modelo que realmente exista en `models`.
*   Establece temperaturas por ruta; mantén el código en 0–0.2.
*   Guarda en caché el mapa del repositorio entre turnos; no reenvíes contextos gigantes a menos que los archivos hayan cambiado.
*   Evita los cambios de modelo a mitad de tarea.
*   Prefiere "diff" sobre "reemplazar este archivo completo" para reducir importaciones alucinadas.

Si quieres, pega los prompts y configuraciones de temperatura de tu enrutador, y los ajustaré para cada ruta para que Claude Code y tu pila se comporten de manera más consistente con la fiabilidad estilo Codex.