---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Comprensión del Cálculo del Voltaje RMS
translated: true
type: note
---

### Explicación

El voltaje de la raíz cuadrática media (RMS), \\( V_{RMS} \\), representa el valor efectivo de un voltaje alterno que produce la misma disipación de potencia en una carga resistiva que un voltaje de corriente continua (DC) de la misma magnitud. Para una forma de onda sinusoidal \\( v(t) = V_{max} \sin(\omega t) \\), donde \\( V_{max} \\) es el voltaje pico (máximo), el valor RMS se deriva de la siguiente manera:

1. **Valor cuadrático medio**: El voltaje instantáneo al cuadrado durante un período \\( T \\) es \\( v^2(t) = V_{max}^2 \sin^2(\omega t) \\). El promedio (media) de \\( \sin^2(\omega t) \\) durante un período es \\( \frac{1}{2} \\), por lo que el voltaje cuadrático medio es \\( \frac{V_{max}^2}{2} \\).

2. **Cálculo del RMS**: Se toma la raíz cuadrada del valor cuadrático medio:  
   \\[
   V_{RMS} = \sqrt{\frac{V_{max}^2}{2}} = \frac{V_{max}}{\sqrt{2}}
   \\]

3. **Aproximación numérica**: Dado que \\( \sqrt{2} \approx 1.414 \\), entonces \\( \frac{1}{\sqrt{2}} \approx 0.707 \\). Por lo tanto, \\( V_{RMS} \approx 0.707 \times V_{max} \\).

Esto confirma la opción **B**. Las otras opciones son incorrectas:  
- A sobreestima (ignora el promedio).  
- C invierte el factor (eso es \\( V_{max} = \sqrt{2} \times V_{RMS} \\)).  
- D subestima (ese es el valor promedio para un seno rectificado de onda completa, no el RMS).