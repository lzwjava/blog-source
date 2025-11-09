---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Adopción de vLLM por Proveedores de IA
translated: true
type: note
---

### Uso de vLLM por Proveedores de IA

vLLM es un motor de inferencia de código abierto comúnmente recomendado para servir modelos de peso abierto de manera eficiente. Sin embargo, su adopción en servicios de producción varía. A continuación se presenta un desglose basado en la información disponible:

| Proveedor/Modelo | ¿Utiliza vLLM en Producción? | Detalles |
|---------------|---------------------------|---------|
| **Claude (Anthropic)** | No | Anthropic depende de infraestructura propietaria para servir sus modelos Claude. vLLM ofrece compatibilidad para despliegues locales o de terceros que imitan la API de Anthropic, pero no hay evidencia de uso interno. |
| **OpenAI (modelos GPT)** | No | OpenAI utiliza sistemas de servicio personalizados y propios, optimizados para escala. vLLM es compatible con APIs similares a las de OpenAI para inferencia local, pero OpenAI no basa su producción en vLLM. |
| **Minimax AI** | No | MiniMax publica modelos de código abierto como MiniMax-M1/M2 y recomienda vLLM para despliegues de usuarios debido a su rendimiento. No hay confirmación del uso de vLLM en su API de producción central; es posible que utilicen forks o configuraciones personalizadas. |
| **Kimi (Moonshot AI)** | No | Moonshot recomienda vLLM para el auto-alojamiento de Kimi-K2, y su herramienta Checkpoint-Engine se integra con él para actualizaciones de pesos. Sin embargo, es probable que su inferencia en producción utilice optimizaciones propietarias junto con motores como SGLang o TensorRT-LLM. |
| **DeepSeek AI** | Sí | DeepSeek ha publicado como código abierto un motor de inferencia personalizado construido directamente sobre vLLM, incorporando optimizaciones de su investigación. Se utiliza para modelos como DeepSeek-V3 y R1, con contribuciones de vuelta al proyecto vLLM. |

### Referencias
- [DeepSeek Open-Sources Custom Inference Engine Built on vLLM](https://www.ainews.com/p/deepseek-open-sources-custom-inference-engine-built-on-vllm)
- [The path to open-sourcing the DeepSeek inference engine](https://news.ycombinator.com/item?id=43682088)
- [MiniMax-M1 Hybrid Architecture Meets vLLM](https://blog.vllm.ai/2025/06/30/minimax-m1.html)
- [Kimi K2: Open Agentic Intelligence](https://moonshotai.github.io/Kimi-K2/)
- [OpenAI-Compatible Server - vLLM](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html)
- [Support Anthropic API `/v1/messages` endpoint · Issue #21313 · vllm-project/vllm](https://github.com/vllm-project/vllm/issues/21313)