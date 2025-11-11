---
audio: false
generated: true
lang: de
layout: post
title: Beweis der linearen Unabhängigkeit
translated: true
type: note
---

### Übersetzung:

23. Gegeben sei, dass die Vektoren \\( \alpha_1, \alpha_2, \alpha_3 \\) linear unabhängig sind, und die Vektoren \\( \beta_1 = \alpha_1 + 2\alpha_2 \\), \\( \beta_2 = -\alpha_1 + \alpha_2 - 3\alpha_3 \\), \\( \beta_3 = 3\alpha_1 + 6\alpha_3 \\). Beweisen Sie, dass die Vektoren \\( \beta_1, \beta_2, \beta_3 \\) linear abhängig sind.

### Lösung:
Um zu beweisen, dass die Vektoren \\( \beta_1, \beta_2, \beta_3 \\) linear abhängig sind, müssen wir zeigen, dass es Skalare \\( c_1, c_2, c_3 \\) (nicht alle null) gibt, sodass gilt:

\\[ c_1 \beta_1 + c_2 \beta_2 + c_3 \beta_3 = 0 \\]

Gegeben:
\\[ \beta_1 = \alpha_1 + 2\alpha_2 \\]
\\[ \beta_2 = -\alpha_1 + \alpha_2 - 3\alpha_3 \\]
\\[ \beta_3 = 3\alpha_1 + 6\alpha_3 \\]

Wir müssen Konstanten \\( c_1, c_2, c_3 \\) finden, sodass:

\\[ c_1 (\alpha_1 + 2\alpha_2) + c_2 (-\alpha_1 + \alpha_2 - 3\alpha_3) + c_3 (3\alpha_1 + 6\alpha_3) = 0 \\]

Dies kann umgeschrieben werden als:

\\[ (c_1 - c_2 + 3c_3)\alpha_1 + (2c_1 + c_2)\alpha_2 + (-3c_2 + 6c_3)\alpha_3 = 0 \\]

Da \\( \alpha_1, \alpha_2, \alpha_3 \\) linear unabhängig sind, müssen die Koeffizienten von \\( \alpha_1, \alpha_2, \alpha_3 \\) jeweils null sein:

1. \\( c_1 - c_2 + 3c_3 = 0 \\)
2. \\( 2c_1 + c_2 = 0 \\)
3. \\( -3c_2 + 6c_3 = 0 \\)

Lösen wir dieses Gleichungssystem:

Aus Gleichung 2:
\\[ 2c_1 + c_2 = 0 \implies c_2 = -2c_1 \\]

Aus Gleichung 3:
\\[ -3c_2 + 6c_3 = 0 \implies -3(-2c_1) + 6c_3 = 0 \implies 6c_1 + 6c_3 = 0 \implies c_3 = -c_1 \\]

Setze \\( c_2 = -2c_1 \\) und \\( c_3 = -c_1 \\) in Gleichung 1 ein:
\\[ c_1 - (-2c_1) + 3(-c_1) = 0 \implies c_1 + 2c_1 - 3c_1 = 0 \implies 0 = 0 \\]

Dies gilt für jedes beliebige \\( c_1 \\). Wählen wir \\( c_1 = 1 \\):

Dann:
\\[ c_2 = -2 \\]
\\[ c_3 = -1 \\]

Somit haben wir Konstanten \\( c_1 = 1, c_2 = -2, c_3 = -1 \\) gefunden, sodass gilt:

\\[ 1 \cdot \beta_1 - 2 \cdot \beta_2 - 1 \cdot \beta_3 = 0 \\]

Dies beweist, dass die Vektoren \\( \beta_1, \beta_2, \beta_3 \\) linear abhängig sind.