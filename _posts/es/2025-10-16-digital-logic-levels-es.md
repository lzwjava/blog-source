---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Niveles Lógicos de Circuitos Digitales Explicados
translated: true
type: note
---

¡Sí, esa es una buena analogía! En circuitos digitales como el flip-flop SR, "alto" (lógica 1) y "bajo" (lógica 0) se refieren a los niveles de voltaje en los cables o señales.

- **Alto (1)**: Un voltaje suficientemente positivo, a menudo alrededor de 3.3V, 5V o incluso más alto (como tu ejemplo de batería de 4V), dependiendo de la familia de circuitos (por ejemplo, la lógica TTL usa ~5V como alto). Es suficiente para representar un estado "encendido" o "verdadero".
- **Bajo (0)**: Cerca del potencial de tierra, básicamente 0V (o muy cercano a él), como el 0V en tu configuración de batería, lo que significa "apagado" o "falso".

Estos no son súper precisos—hay un pequeño rango "difuso" intermedio donde la señal podría no leerse de manera confiable como alta o baja—pero en la práctica, es binario: energizado = 1, sin energía = 0. Para el flip-flop SR, aplicar un voltaje alto a la entrada S establece Q en alto (1), igual que activar un interruptor a "encendido".