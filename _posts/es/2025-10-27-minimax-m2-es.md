---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Modelo de IA de Código Abierto MiniMax M2
translated: true
type: note
---

### ¿Qué es MiniMax M2?

MiniMax M2 es un modelo de lenguaje grande (LLM) de código abierto recién lanzado por MiniMax AI, una empresa china de IA centrada en modelos base para texto, audio, imagen y video. Lanzado hace apenas unas horas (a 27 de octubre de 2025), es un modelo Mixture of Experts (MoE) optimizado para flujos de trabajo de programación y agentes—piensa en agentes de IA autónomos que planifican, ejecutan herramientas y manejan tareas complejas como desarrollo full-stack, análisis de datos o investigación multi-etapa. No es un modelo generalista como GPT o Claude, sino que destaca en aplicaciones de programación de extremo a extremo y agentes, integrandoce perfectamente con herramientas como Claude Code, Cursor o intérpretes de navegador/terminal.

Especificaciones clave:
- **Parámetros**: 230 mil millones en total, pero solo 10 mil millones activos (para eficiencia).
- **Longitud de contexto**: Hasta 128K tokens.
- **Despliegue**: Disponible en Hugging Face bajo licencia MIT; es compatible con frameworks como SGLang y vLLM para auto-hospedaje.
- **Acceso**: Prueba gratuita de la API hasta el 7 de noviembre de 2025 a través de MiniMax Agent (agent.minimax.io). La API de pago cuesta $0.30 por millón de tokens de entrada y $1.20 por millón de tokens de salida—aproximadamente el 8% del coste de Claude 3.5 Sonnet.

Está impulsado por un enfoque de "pensamiento intercalado" (usando etiquetas `