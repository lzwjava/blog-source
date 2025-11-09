---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Dérive du point zéro en électronique
translated: true
type: note
---

### Dérive du point zéro : Définition et explication

La dérive du point zéro (également appelée dérive de l'offset ou dérive de la tension de décalage) est une erreur dans les circuits électroniques, les capteurs ou les systèmes de mesure où la sortie produit une tension de décalage ou un niveau de signal non désiré, même lorsque l'entrée est exactement zéro. Cela se traduit par un "décalage de sortie non désiré à une entrée nulle", déplaçant la ligne de base par rapport au point zéro idéal. C'est comme une balance qui affiche lentement "1 kg" lorsqu'il n'y a rien dessus ; la lecture dérive avec le temps ou les conditions.

#### Caractéristiques principales
- **Manifestation** : La sortie ne revient pas au vrai zéro sans signal d'entrée, provoquant des erreurs cumulatives dans les systèmes multi-étages (par exemple, les amplificateurs) où de petits décalages sont amplifiés.
- **Fréquent dans** : Les amplificateurs opérationnels (ampli-ops), les amplificateurs d'instrumentation, les thermocouples, les jauges de contrainte et les circuits à couplage direct (sans condensateurs pour bloquer la composante continue).
- **Mesure** : Souvent quantifiée en μV/°C (volts par degré Celsius) pour la dérive thermique ou en ppm/°C pour les changements relatifs.

#### Causes principales
- **Variations de température** : La plus courante ; les paramètres des transistors ou des résistances (par exemple, la tension base-émetteur) changent avec la chaleur, entraînant des décalages du point de polarisation.
- **Vieillissement des composants** : Dégradation graduelle des semiconducteurs ou des composants passifs au fil du temps.
- **Fluctuations de l'alimentation électrique** : Ondulations de tension instables affectant les points de polarisation.
- **Désaccords de paramètres** : Dans les amplificateurs multi-étages, de légères différences dans les gains des transistors ou les résistances amplifient les décalages.

#### Effets et atténuation
- **Impact** : Déforme les signaux de faible niveau, réduit la précision dans les applications exigeantes comme les dispositifs médicaux ou l'audio (par exemple, un bourdonnement ou un buzz lors des "silences").
- **Solutions** :
  - Circuits d'auto-zéro ou de stabilisation par hachage (chopper) pour réinitialiser périodiquement les décalages.
  - Composants appariés ou potentiomètres de réglage pour l'étalonnage.
  - Compensation thermique (par exemple, avec des thermistances).
  - Couplage AC pour bloquer la composante continue dans les applications non DC.

Dans les amplificateurs multi-étages à couplage direct (comme discuté précédemment), c'est particulièrement problématique car les signaux DC traversent tous les étages, amplifiant les dérives infimes.

[Zero Drift Amplifiers Explained](https://www.analog.com/en/resources/analog-dialogue/articles/zero-drift-amplifiers.html)  
[Offset Drift in Op-Amps](https://www.ti.com/lit/an/sboa275/sboa275.pdf)  
[Wikipedia: Offset (electronics)](https://en.wikipedia.org/wiki/Offset_(electronics))