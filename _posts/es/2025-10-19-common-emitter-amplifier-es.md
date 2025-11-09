---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Análisis del Amplificador de Emisor Común
translated: true
type: note
---

### Corriente de Colector \\( I_C \\)

La resistencia de entrada \\( R_{in} \\) para un amplificador BJT de emisor común con el emisor a tierra es aproximadamente la pequeña resistencia de señal de la base \\( r_\pi = \frac{\beta V_T}{I_C} \\), donde \\( V_T = 0.026 \\) V (voltaje térmico a temperatura ambiente) y \\( \beta = 100 \\).

Dado \\( R_{in} = 1 \\) k\\( \Omega = 1000 \\) \\( \Omega \\),

\\[
r_\pi = \frac{100 \times 0.026}{I_C} = 1000
\\]

\\[
\frac{2.6}{I_C} = 1000
\\]

\\[
I_C = \frac{2.6}{1000} = 0.0026 \text{ A} = 2.6 \text{ mA}
\\]

Este punto de polarización produce un voltaje colector-emisor \\( V_{CE} = V_{CC} - I_C R_C = 12 - (0.0026 \times 2200) \approx 12 - 5.72 = 6.28 \\) V, que está cerca del punto medio de la fuente para una linealidad razonable.

### Ganancia de Voltaje \\( A_V \\)

La ganancia de voltaje de pequeña señal para un amplificador de emisor común (sin resistencia de emisor) es \\( A_V = -g_m R_C \\), donde la transconductancia \\( g_m = \frac{I_C}{V_T} \\).

\\[
g_m = \frac{0.0026}{0.026} = 0.1 \text{ A/V (o S)}
\\]

\\[
A_V = - (0.1 \times 2200) = -220
\\]

El signo negativo indica inversión de fase.