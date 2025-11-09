---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Adoption de vLLM par les fournisseurs d'IA
translated: true
type: note
---

### Utilisation de vLLM par les fournisseurs d'IA

vLLM est un moteur d'inférence open-source couramment recommandé pour servir efficacement les modèles à poids ouvert. Cependant, son adoption dans les services de production varie. Voici un aperçu basé sur les informations disponibles :

| Fournisseur/Modèle | Utilise vLLM en production ? | Détails |
|---------------|---------------------------|---------|
| **Claude (Anthropic)** | Non | Anthropic s'appuie sur une infrastructure propriétaire pour servir les modèles Claude. vLLM offre une compatibilité pour les déploiements locaux ou tiers imitant l'API d'Anthropic, mais il n'y a aucune preuve d'utilisation interne. |
| **OpenAI (modèles GPT)** | Non | OpenAI utilise des systèmes de service personnalisés et internes optimisés pour l'échelle. vLLM prend en charge les API compatibles OpenAI pour l'inférence locale, mais OpenAI ne base pas sa production sur vLLM. |
| **Minimax AI** | Non | MiniMax open-source des modèles comme MiniMax-M1/M2 et recommande vLLM pour les déploiements utilisateurs en raison de ses performances. Aucune confirmation de l'utilisation de vLLM dans leur API de production principale ; ils peuvent utiliser des forks ou des configurations personnalisées. |
| **Kimi (Moonshot AI)** | Non | Moonshot recommande vLLM pour l'autohébergement de Kimi-K2, et leur outil Checkpoint-Engine s'intègre avec lui pour les mises à jour des poids. Cependant, leur inférence en production utilise probablement des optimisations propriétaires aux côtés de moteurs comme SGLang ou TensorRT-LLM. |
| **DeepSeek AI** | Oui | DeepSeek a open-sourcé un moteur d'inférence personnalisé construit directement sur vLLM, incorporant des optimisations issues de leurs recherches. Celui-ci est utilisé pour des modèles comme DeepSeek-V3 et R1, avec des contributions retournées au projet vLLM. |

### Références
- [DeepSeek Open-Sources Custom Inference Engine Built on vLLM](https://www.ainews.com/p/deepseek-open-sources-custom-inference-engine-built-on-vllm)
- [The path to open-sourcing the DeepSeek inference engine](https://news.ycombinator.com/item?id=43682088)
- [MiniMax-M1 Hybrid Architecture Meets vLLM](https://blog.vllm.ai/2025/06/30/minimax-m1.html)
- [Kimi K2: Open Agentic Intelligence](https://moonshotai.github.io/Kimi-K2/)
- [OpenAI-Compatible Server - vLLM](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html)
- [Support Anthropic API `/v1/messages` endpoint · Issue #21313 · vllm-project/vllm](https://github.com/vllm-project/vllm/issues/21313)