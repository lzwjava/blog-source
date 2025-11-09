---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Analyse einer Emitterschaltung
translated: true
type: note
---

### Kollektorstrom \\( I_C \\)

Der Eingangswiderstand \\( R_{in} \\) für einen BJT-Verstärker in Emitterschaltung mit geerdetem Emitter ist ungefähr der Kleinsignal-Basiswiderstand \\( r_\pi = \frac{\beta V_T}{I_C} \\), wobei \\( V_T = 0.026 \\) V (Thermospannung bei Raumtemperatur) und \\( \beta = 100 \\) ist.

Gegeben ist \\( R_{in} = 1 \\) k\\( \Omega = 1000 \\) \\( \Omega \\),

\\[
r_\pi = \frac{100 \times 0.026}{I_C} = 1000
\\]

\\[
\frac{2.6}{I_C} = 1000
\\]

\\[
I_C = \frac{2.6}{1000} = 0.0026 \text{ A} = 2.6 \text{ mA}
\\]

Dieser Arbeitspunkt ergibt eine Kollektor-Emitter-Spannung \\( V_{CE} = V_{CC} - I_C R_C = 12 - (0.0026 \times 2200) \approx 12 - 5.72 = 6.28 \\) V, was in der Nähe der Mitte der Versorgungsspannung für eine vernünftige Linearität liegt.

### Spannungsverstärkung \\( A_V \\)

Die Kleinsignal-Spannungsverstärkung für einen Verstärker in Emitterschaltung (ohne Emitterwiderstand) ist \\( A_V = -g_m R_C \\), wobei die Steilheit \\( g_m = \frac{I_C}{V_T} \\) ist.

\\[
g_m = \frac{0.0026}{0.026} = 0.1 \text{ A/V (oder S)}
\\]

\\[
A_V = - (0.1 \times 2200) = -220
\\]

Das negative Vorzeichen zeigt eine Phasenumkehr an.