---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Analyse de l'amplificateur à émetteur commun
translated: true
type: note
---

### Courant de collecteur \\( I_C \\)

La résistance d'entrée \\( R_{in} \\) pour un amplificateur à BJT en émetteur commun avec un émetteur à la masse est approximativement la petite résistance de base du signal \\( r_\pi = \frac{\beta V_T}{I_C} \\), où \\( V_T = 0,026 \\) V (tension thermique à température ambiante) et \\( \beta = 100 \\).

Étant donné \\( R_{in} = 1 \\) k\\( \Omega = 1000 \\) \\( \Omega \\),

\\[
r_\pi = \frac{100 \times 0,026}{I_C} = 1000
\\]

\\[
\frac{2,6}{I_C} = 1000
\\]

\\[
I_C = \frac{2,6}{1000} = 0,0026 \text{ A} = 2,6 \text{ mA}
\\]

Ce point de polarisation donne une tension collecteur-émetteur \\( V_{CE} = V_{CC} - I_C R_C = 12 - (0,0026 \times 2200) \approx 12 - 5,72 = 6,28 \\) V, ce qui est proche du milieu de l'alimentation pour une linéarité raisonnable.

### Gain en tension \\( A_V \\)

Le petit gain en tension de signal pour un amplificateur en émetteur commun (sans résistance d'émetteur) est \\( A_V = -g_m R_C \\), où la transconductance \\( g_m = \frac{I_C}{V_T} \\).

\\[
g_m = \frac{0,0026}{0,026} = 0,1 \text{ A/V (ou S)}
\\]

\\[
A_V = - (0,1 \times 2200) = -220
\\]

Le signe négatif indique une inversion de phase.