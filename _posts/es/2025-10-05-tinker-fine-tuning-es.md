---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: API de Tinker Simplifica el Ajuste de Modelos
translated: true
type: note
---

Tinker es una nueva API flexible lanzada por Thinking Machines AI para el fine-tuning de modelos de lenguaje. Está diseñada para permitir a investigadores, desarrolladores y "hackers" experimentar con modelos de pesos abiertos (tanto grandes como Qwen-235B-A22B como más pequeños) dándoles control total sobre los algoritmos y los datos. El servicio maneja la carga pesada del entrenamiento distribuido—como la planificación, asignación de recursos y recuperación de fallos—en sus clusters internos, utilizando técnicas como LoRA para hacerlo eficiente y rentable.

Aspectos destacados:
- **Facilidad de uso**: Cambia de modelos con solo una cadena de texto en el código Python.
- **Primitivas de la API**: Herramientas de bajo nivel como `forward_backward` y `sample` para métodos comunes de post-entrenamiento.
- **Soporte de código abierto**: Incluye la librería Tinker Cookbook en GitHub, con implementaciones modernas de técnicas de fine-tuning.
- **Propósito**: Simplifica la investigación en modelos de vanguardia, reduciendo los dolores de cabeza de infraestructura para que puedas concentrarte en la innovación.

Actualmente está en beta privada (gratuita para empezar, con precios basados en el uso próximamente), y puedes unirte a la lista de espera en [thinkingmachines.ai/tinker](https://thinkingmachines.ai/tinker). Los primeros usuarios incluyen equipos de Princeton, Stanford, Berkeley y Redwood Research.

[Anunciando Tinker](https://thinkingmachines.ai/blog/announcing-tinker/)