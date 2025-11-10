---
audio: false
generated: true
image: false
lang: es
layout: post
title: Corrección de Discrepancia en el Esquema de Código de DeepSeek Claude
translated: true
type: note
---

Respuesta breve: discrepancia de esquema.

Claude Code “habla en Anthropic” (espera uso de herramientas estilo Anthropic-Messages como bloques `tool_use` / `tool_result`). DeepSeek V3.1 en OpenRouter “habla en OpenAI” (emite `tool_calls` / function calling estilo OpenAI). Si tu router de Claude Code reenvía una tarea a DeepSeek V3.1 sin transformar la solicitud/respuesta, los mensajes de uso de herramientas del asistente no se analizarán correctamente—y verás errores justo cuando el agente intente planificar/ejecutar herramientas o transmitir la salida. ([Anthropic][1], [OpenRouter][2], [DeepSeek API Docs][3])

Qué hacer (soluciones rápidas):

1. Usa los transformadores del router
   Habilita los transformadores de solicitud/respuesta OpenRouter↔︎Anthropic en tu router de Claude Code para que `tool_calls` ⇄ `tool_use` se mapeen en ambas direcciones. El router comunitario popular admite esto explícitamente; consulta su sección “Request/Response Transformation” y los ejemplos de configuración. ([GitHub][4], [ClaudeLog][5])

2. Elige el slug de modelo correcto
   DeepSeek V3.1 tiene slugs de OpenRouter específicos (por ejemplo, las entradas de la familia V3.1/V3). Un slug incorrecto o antiguo también puede generar errores durante las fases de transmisión o de herramientas. Verifica el id de modelo exacto que se muestra en la página de DeepSeek de OpenRouter y úsalo en el mapeo de tu router. ([OpenRouter][6])

3. Mantente en “chat” (no en “reasoner”) a menos que hayas mapeado sus campos
   Si pruebas una variante de razonamiento que transmite campos de razonamiento especiales, tu router debe traducirlos—o Claude Code fallará. Prefiere el modelo de chat estándar o desactiva la salida adicional de “pensamiento” hasta que tu transformador pueda manejarlo. (La documentación de DeepSeek enfatiza la function calling estilo OpenAI; eso es lo que debes mapear.) ([DeepSeek API Docs][3])

4. Actualiza a la última versión del router
   Las compilaciones comunitarias recientes agregaron ajustes de compatibilidad para proveedores que no son Anthropic; actualiza antes de probar. ([GitHub][4])

Por qué esto solo pasa con V3.1
V3.1 agregó capacidades de agente/uso de herramientas más fuertes por defecto. Eso aumenta la probabilidad de que tu flujo de Claude Code encuentre los mensajes de herramientas no traducidos, que es exactamente donde la discrepancia de esquema afecta. ([DeepSeek API Docs][7])

Si compartes el texto exacto del error, puedo señalar el fragmento preciso del transformador para agregar a tu configuración.

[1]: https://www.anthropic.com/engineering/claude-code-best-practices?utm_source=chatgpt.com "Claude Code: Best practices for agentic coding"
[2]: https://openrouter.ai/docs/features/tool-calling?utm_source=chatgpt.com "Tool & Function Calling"
[3]: https://api-docs.deepseek.com/guides/function_calling?utm_source=chatgpt.com "Function Calling"
[4]: https://github.com/musistudio/claude-code-router?utm_source=chatgpt.com "musistudio/claude-code-router"
[5]: https://claudelog.com/claude-code-mcps/claude-code-router/?utm_source=chatgpt.com "Claude Code Router"
[6]: https://openrouter.ai/models?q=deepseek&utm_source=chatgpt.com "Models: 'deepseek'"
[7]: https://api-docs.deepseek.com/news/news250821?utm_source=chatgpt.com "DeepSeek-V3.1 Release"