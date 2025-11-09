---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Comprendre le calcul de la tension efficace
translated: true
type: note
---

### Explication

La tension efficace (RMS), \\( V_{RMS} \\), représente la valeur efficace d'une tension alternative qui produit la même dissipation de puissance dans une charge résistive qu'une tension de courant continu (DC) de même magnitude. Pour une forme d'onde sinusoïdale \\( v(t) = V_{max} \sin(\omega t) \\), où \\( V_{max} \\) est la tension de crête (maximale), la valeur RMS est dérivée comme suit :

1. **Valeur quadratique moyenne** : La tension instantanée au carré sur une période \\( T \\) est \\( v^2(t) = V_{max}^2 \sin^2(\omega t) \\). La moyenne de \\( \sin^2(\omega t) \\) sur une période est \\( \frac{1}{2} \\), donc la tension quadratique moyenne est \\( \frac{V_{max}^2}{2} \\).

2. **Calcul de la valeur RMS** : Prenez la racine carrée de la valeur quadratique moyenne :  
   \\[
   V_{RMS} = \sqrt{\frac{V_{max}^2}{2}} = \frac{V_{max}}{\sqrt{2}}
   \\]

3. **Approximation numérique** : Puisque \\( \sqrt{2} \approx 1.414 \\), alors \\( \frac{1}{\sqrt{2}} \approx 0.707 \\). Ainsi, \\( V_{RMS} \approx 0.707 \times V_{max} \\).

Ceci confirme l'option **B**. Les autres options sont incorrectes :  
- A surestime (ignore la mise en moyenne).  
- C inverse le facteur (c'est \\( V_{max} = \sqrt{2} \times V_{RMS} \\)).  
- D sous-estime (c'est la valeur moyenne pour une sinusoïdale redressée onde complète, pas la valeur RMS).