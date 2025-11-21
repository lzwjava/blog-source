---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Preguntas de Entrevista para Ingeniero Senior de IA 2024-2025
translated: true
type: note
---

Aquí tienes las preguntas de entrevista más comunes y típicas que encontrarás para un puesto de **Ingeniero Senior de IA/Agentes/LLM** en 2024-2025, especialmente en las mejores empresas (nivel FAANG, laboratorios de IA como Anthropic/OpenAI/xAI, scale-ups como Adept, Imbue, etc.).

Están agrupadas por categoría y dificultad (la mayoría son de nivel senior, que esperan una comprensión profunda + experiencia en producción).

### Diseño de Sistemas & Arquitectura
1.  Diseña un sistema escalable para servir inferencias de LLM que pueda manejar 10k+ QPS con una latencia p99 <200ms.
2.  ¿Cómo diseñarías un agente de IA en tiempo real que pueda navegar por la web, usar herramientas y mantener memoria a largo plazo?
3.  Diseña un pipeline de generación aumentada por recuperación (RAG) desde cero (elección de base de datos vectorial, fragmentación, reranking, búsqueda híbrida, evaluación).
4.  ¿Cómo reduces el costo de inferencia de un modelo de 70B en 5-10x manteniendo la degradación de la calidad <2%?
5.  Diseña un framework de evaluación para tareas de agentes de respuesta abierta (ej: compras web, investigación).
6.  ¿Cómo construirías un sistema multi-agente donde los agentes colaboren (debate, jerarquía, etc.)?

### Fundamentos de LLM & Uso Avanzado
-   Explica cómo funciona la atención desde cero (incluyendo Rotary Positional Embeddings, Grouped-Query Attention, Sliding Window Attention).
-   ¿Por qué Llama 3/4 usa RoPE en lugar de ALiBi? Pros y contras.
-   Deriva las leyes de escalamiento (Kaplan, Hoffmann "Chinchilla", DeepMind "Emergent Abilities").
-   ¿Qué causa el "lost in the middle" en modelos de contexto largo? ¿Cómo lo solucionas?
-   Compara arquitecturas Mixture-of-Experts (MoE) (Mixtral, DeepSeek, Grok-1, Qwen-2.5-MoE). ¿Por qué la escasez de activación es difícil en la práctica?
-   ¿Cómo funciona realmente la cuantización (GPTQ, AWQ, SmoothQuant, bitsandbytes)? Compromisos entre 4-bit, 3-bit, 2-bit.
-   ¿Cuál es la diferencia entre RLHF, DPO, KTO, PPO, GRPO y cuándo usarías cada uno?

### Agentes & Uso de Herramientas
-   ¿Cómo implementas tool calling / function calling confiable con JSON mode vs ReAct vs OpenAI tools?
-   Explica ReAct, Reflexion, ReWOO, Toolformer, DEPS, Chain-of-Verification.
-   ¿Cómo previenes bucles infinitos en la ejecución de agentes?
-   ¿Cómo evalúas el rendimiento de un agente en benchmarks como GAIA, WebArena, AgentBench?
-   ¿Cómo añadirías memoria a largo plazo a un agente (vector store vs key-value store vs episodic memory)?

### Entrenamiento, Fine-tuning & Alineación
-   Repasa el stack completo de fine-tuning: LoRA, QLoRA, DoRA, LoftQ, LLaMA-Adapter, IA³.
-   ¿Cómo funciona QLoRA internamente (NF4, double quantization, pagined optimizers)?
-   Tienes 10k ejemplos de instrucciones de alta calidad y quieres hacer fine-tuning a un modelo de 70B en 8×H100s. Da la receta exacta.
-   Explica constitutional AI, RLAIF, self-critique, process vs outcome supervision.
-   ¿Cómo detectas y mitigas el reward hacking en RLHF?

### Codificación & Implementación (Live coding o take-home)
-   Implementa un agente ReAct simple desde cero (Python).
-   Implementa sliding-window attention eficiente con caché estilo flash-attention.
-   Construye un sistema RAG básico con LangChain / LlamaIndex (juzgarán la arquitectura).
-   Optimiza un pase hacia adelante de transformer para un contexto de 128k (memory efficient).
-   Escribe una función autograd personalizada de PyTorch para un nuevo kernel de cuantización.

### Fundamentos de ML (todavía preguntan a seniors)
-   ¿Por qué AdamW funciona mejor que Adam? Deriva la formulación de weight-decay.
-   Explica label smoothing, teacher forcing, sequence-level vs token-level training objectives.
-   ¿Cuál es la diferencia entre BLEU, ROUGE, BERTScore, LLM-as-a-judge, G-Eval?
-   Deriva la función de pérdida del transformer y explica por qué ignoramos los tokens de relleno.

### Producción & MLOps
-   ¿Cómo monitoreas las salidas de los LLM en producción (drift, toxicidad, fuga de PII, prompt injection)?
-   Notas que el 5% de tus usuarios están haciendo jailbreaking al modelo. ¿Cómo lo detectas y te defiendes?
-   Compara vLLM, TGI, TensorRT-LLM, lmdeploy, Outlines, Guidance para velocidad de inferencia.
-   ¿Cómo haces continuous fine-tuning / online learning de forma segura?

### Conductual / Experiencia
-   Cuéntame sobre el problema de producción más difícil que solucionaste con LLMs.
-   ¿Cómo lanzaste un producto con agentes que los usuarios reales adoraron?
-   Describe una ocasión en la que redujiste el costo de inferencia en >50%.
-   ¿Cuál es el peor desastre por alucinación que has visto y cómo lo solucionaste?

### Temas de Actualidad (2025)
-   ¿Cómo funcionan los métodos de escalamiento en tiempo de prueba (DeepSeek R1, o1-style reasoning, process reward models)?
-   Compara chain-of-thought, tree-of-thought, graph-of-thought, process vs outcome reward.
-   ¿Cuáles son los mejores modelos de razonamiento de código abierto actuales (Llama-3.1-405B, Qwen-2.5-72B-Instruct, DeepSeek-V3, Gemma-2-27B)?
-   Opiniones sobre los bucles de generación de datos sintéticos (Self-Refine, STaR, Quiet-STaR, MCTS-based data synth).

Empresas que hacen las preguntas más difíciles actualmente: OpenAI, Anthropic, xAI, Adept, Scale AI, Helion, Imbue, Character.AI, Cohere, Mistral.

Prepárate para hacer diseños de sistemas en una pizarra y para codificar en un portátil (sin internet). La mayoría de los procesos para senior son de 5 a 7 rondas con mucho diseño de sistemas y codificación en profundidad.

¡Buena suerte!