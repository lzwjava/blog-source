---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: 'vLLM: Motor Eficiente para Servicio de LLM'
translated: true
type: note
---

### Invención de vLLM

vLLM (abreviatura de "virtual LLM") es una biblioteca de código abierto para la inferencia y el servicio de modelos de lenguaje grandes (LLMs) de alto rendimiento y eficiencia de memoria. Fue inventado a principios de 2023 por investigadores del Sky Computing Lab en el RISELab de UC Berkeley. El proyecto comenzó como un motor de inferencia especializado optimizado para GPUs NVIDIA A100 y un conjunto limitado de modelos, abordando desafíos clave en el servicio de LLMs como la fragmentación de memoria y el bajo rendimiento.

Hitos iniciales clave:
- **Mediados de abril de 2023**: Primera integración pública con FastChat, impulsando las demostraciones de Vicuna de LMSYS y Chatbot Arena.
- **Junio de 2023**: Lanzamiento oficial y publicación del repositorio público en GitHub.
- **12 de septiembre de 2023**: Artículo de investigación fundamental, "Efficient Memory Management for Large Language Model Serving with PagedAttention", publicado en arXiv, introduciendo el mecanismo central PagedAttention que permite el procesamiento por lotes continuo y un desperdicio de caché KV casi nulo.

El repositorio de GitHub (vllm-project/vllm) se creó alrededor de mayo-junio de 2023, alineándose con el impulso inicial de desarrollo.

### Aumento de la Popularidad

vLLM comenzó a ganar una tracción significativa en 2024, evolucionando de una herramienta de investigación de nicho al estándar de facto para el servicio de LLMs de código abierto. Su popularidad explotó debido a las rápidas adiciones de funciones (por ejemplo, cuantización, decodificación especulativa, soporte multimodal), expansiones de hardware (NVIDIA, AMD, Google TPUs, etc.) y adopciones en producción por empresas como Amazon (impulsando a Rufus durante el Prime Day 2024) y LinkedIn.

Indicadores clave de crecimiento desde 2024:
- **Estrellas en GitHub**: Creció 2.3x, de 14,000 (inicios de 2024) a 32,600 (finales de 2024).
- **Descargas Mensuales**: Se disparó 4.5x, de 6,000 a 27,000.
- **Uso de GPU**: Aumentó ~10x en la segunda mitad de 2024.
- **Comunidad**: Los colaboradores aumentaron 3.9x hasta 740, con horas de oficina quincenales y asociaciones (por ejemplo, con NVIDIA, IBM, AWS).

A mediados de 2024, tenía ~20,000 estrellas y se discutía frecuentemente en las comunidades de IA por superar a las alternativas en rendimiento. El impulso continuó en 2025:
- Se unió al ecosistema PyTorch en diciembre de 2024.
- Ingresó a la incubación de LF AI & Data en octubre de 2024.
- Alcanzó las 50,000 estrellas en junio de 2025.

Hoy (octubre de 2025), tiene más de 55,000 estrellas y soporta casi 100 arquitecturas de modelos, convirtiéndose en una piedra angular para los despliegues de IA escalables.

[Artículo de arXiv sobre PagedAttention](https://arxiv.org/abs/2309.06180)  
[Repositorio GitHub de vLLM](https://github.com/vllm-project/vllm)  
[Blog Retrospectivo de vLLM 2024](https://blog.vllm.ai/2025/01/10/vllm-2024-wrapped-2025-vision.html)  
[Anuncio de Integración con PyTorch](https://pytorch.org/blog/vllm-joins-pytorch/)