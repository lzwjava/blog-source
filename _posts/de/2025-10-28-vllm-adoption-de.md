---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Verbreitung von vLLM unter KI-Anbietern
translated: true
type: note
---

### Verwendung von vLLM durch KI-Anbieter

vLLM ist eine Open-Source-Inferenz-Engine, die häufig für das effiziente Bereitstellen von Open-Weight-Modellen empfohlen wird. Ihre Einführung in Produktionsdiensten variiert jedoch. Im Folgenden finden Sie eine Aufschlüsselung basierend auf den verfügbaren Informationen:

| Anbieter/Modell | Verwendet vLLM in der Produktion? | Details |
|---------------|---------------------------|---------|
| **Claude (Anthropic)** | Nein | Anthropic verlässt sich auf proprietäre Infrastruktur für die Bereitstellung der Claude-Modelle. vLLM bietet Kompatibilität für lokale oder Drittanbieter-Bereitstellungen, die die Anthropic-API nachahmen, aber es gibt keine Hinweise auf eine interne Nutzung. |
| **OpenAI (GPT-Modelle)** | Nein | OpenAI verwendet maßgeschneiderte, hausinterne Serving-Systeme, die für Skalierbarkeit optimiert sind. vLLM unterstützt OpenAI-kompatible APIs für lokale Inferenz, aber OpenAI basiert seine Produktion nicht auf vLLM. |
| **Minimax AI** | Nein | MiniMax veröffentlicht Modelle wie MiniMax-M1/M2 als Open Source und empfiehlt vLLM für Benutzerbereitstellungen aufgrund seiner Leistung. Es gibt keine Bestätigung für die Nutzung von vLLM in ihrer Kern-Produktions-API; sie verwenden möglicherweise Forks oder benutzerdefinierte Setups. |
| **Kimi (Moonshot AI)** | Nein | Moonshot empfiehlt vLLM für das Self-Hosting von Kimi-K2, und ihr Checkpoint-Engine-Tool integriert sich mit diesem für Gewichtsaktualisierungen. Ihre Produktionsinferenz verwendet jedoch wahrscheinlich proprietäre Optimierungen neben Engines wie SGLang oder TensorRT-LLM. |
| **DeepSeek AI** | Ja | DeepSeek hat eine benutzerdefinierte Inferenz-Engine, die direkt auf vLLM aufbaut, als Open Source veröffentlicht und integriert Optimierungen aus ihrer Forschung. Diese wird für Modelle wie DeepSeek-V3 und R1 verwendet, mit Beiträgen zurück zum vLLM-Projekt. |

### Referenzen
- [DeepSeek Open-Sources Custom Inference Engine Built on vLLM](https://www.ainews.com/p/deepseek-open-sources-custom-inference-engine-built-on-vllm)
- [The path to open-sourcing the DeepSeek inference engine](https://news.ycombinator.com/item?id=43682088)
- [MiniMax-M1 Hybrid Architecture Meets vLLM](https://blog.vllm.ai/2025/06/30/minimax-m1.html)
- [Kimi K2: Open Agentic Intelligence](https://moonshotai.github.io/Kimi-K2/)
- [OpenAI-Compatible Server - vLLM](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html)
- [Support Anthropic API `/v1/messages` endpoint · Issue #21313 · vllm-project/vllm](https://github.com/vllm-project/vllm/issues/21313)