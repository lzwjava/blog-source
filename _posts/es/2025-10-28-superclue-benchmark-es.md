---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: 'SuperCLUE: Evaluación Comparativa de Modelos de Lenguaje Grandes Chinos'
translated: true
type: note
---

SuperCLUE es un conjunto integral de benchmarks diseñado para evaluar los grandes modelos de lenguaje (LLM) en chino. Se basa en el benchmark original CLUE (Chinese Language Understanding Evaluation), expandiéndolo para evaluar capacidades avanzadas en LLMs en lugar de solo modelos más pequeños. Desarrollado por el equipo CLUEbenchmark—un esfuerzo colaborativo que involucra a investigadores de instituciones como la Universidad Tsinghua y empresas del ecosistema chino de IA—SuperCLUE se introdujo por primera vez en 2023 para abordar las lagunas en la evaluación de los LLM chinos según estándares internacionales.

### Características Clave
- **Áreas de Enfoque**: Evalúa los modelos en cuatro cuadrantes principales:
  - Comprensión y generación del lenguaje (p. ej., comprensión lectora, resumen).
  - Habilidades y conocimientos profesionales (p. ej., razonamiento matemático, programación).
  - Inteligencia de agente (p. ej., uso de herramientas, planificación).
  - Seguridad (p. ej., detección de sesgos, alineación ética).
- **Estructura**: Dividido en 12 tareas centrales, con conjuntos de datos como SuperCLUE-Math6 para problemas matemáticos de múltiples pasos.
- **Propósito**: Ayuda a rastrear el progreso en la IA china, destacando tanto las fortalezas (p. ej., manejo de matices culturales) como las lagunas en comparación con modelos globales como la serie GPT.
- **Actualizaciones**: A mediados de 2025, se utiliza para evaluaciones periódicas, con tablas de clasificación que muestran que modelos chinos como Qwen y GLM están cerrando la brecha con los internacionales.

El benchmark es de código abierto y se mantiene activamente, y las evaluaciones a menudo se comparten a través de artículos de arXiv y GitHub.

[SuperCLUE: A Comprehensive Chinese Large Language Model Benchmark](https://arxiv.org/abs/2307.15020)  
[SuperCLUE GitHub Repository](https://github.com/CLUEbenchmark/SuperCLUE)  
[ChinAI: SuperCLUE Benchmarks —2025 Midyear Check-in](https://chinai.substack.com/p/chinai-324-superclue-large-model)