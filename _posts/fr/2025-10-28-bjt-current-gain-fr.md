---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Gain en courant d'un transistor bipolaire
translated: true
type: note
---

### Principes de base des transistors bipolaires (BJT)

Pour comprendre le gain en courant \\( \beta \\) dans ce problème de transistor, commençons par les principes fondamentaux. Un **transistor bipolaire (BJT)** est un dispositif semi-conducteur à trois terminaux utilisé pour l'amplification et la commutation dans les circuits électroniques. Il existe deux types principaux : NPN (le plus courant) et PNP, mais les principes sont similaires. Les terminaux sont :

- **Émetteur (E)** : Libère les porteurs de charge dans le circuit.
- **Base (B)** : Une couche mince qui contrôle le flux des porteurs.
- **Collecteur (C)** : Collecte la majorité des porteurs.

Dans un BJT NPN, le courant circule du collecteur vers l'émetteur lorsque la jonction base-émetteur est polarisée en direct (tension positive sur la base par rapport à l'émetteur) et que la jonction base-collecteur est polarisée en inverse (tension négative sur la base par rapport au collecteur). Cette configuration définit la **région active** de fonctionnement, où le transistor agit comme un amplificateur de courant.

#### Régions de fonctionnement clés
Les BJT ont trois régions de fonctionnement principales :
1.  **Région de blocage** : Les deux jonctions sont polarisées en inverse. Aucun courant significatif ne circule (\\( I_B \approx 0 \\), \\( I_C \approx 0 \\)). Le transistor est "éteint".
2.  **Région active** (ou active directe) : Base-émetteur polarisée en direct, base-collecteur polarisée en inverse. Ici, un petit courant de base \\( I_B \\) contrôle un courant de collecteur \\( I_C \\) beaucoup plus grand. C'est le mode d'amplification.
3.  **Région de saturation** : Les deux jonctions sont polarisées en direct. Le courant est maximal ; le transistor est "allumé" comme un interrupteur fermé, mais il n'y a pas d'amplification.

Le problème spécifie que le transistor est dans la **région active**, nous avons donc affaire à un comportement d'amplification.

#### Courants dans un BJT
Dans la région active :
- **Courant de base (\\( I_B \\))** : Petit courant injecté dans la base, principalement pour fournir des porteurs minoritaires.
- **Courant de collecteur (\\( I_C \\))** : Courant beaucoup plus important circulant du collecteur vers l'émetteur, proportionnel à \\( I_B \\).
- **Courant d'émetteur (\\( I_E \\))** : Courant total sortant de l'émetteur, où \\( I_E = I_B + I_C \\) (selon la loi des nœuds de Kirchhoff).

La relation est approximativement linéaire : \\( I_C \approx \beta I_B \\), où \\( \beta \\) (bêta) est le **gain en courant continu** ou **facteur d'amplification en courant**. C'est un rapport sans dimension, typiquement de 50 à 300 pour les transistors discrets, selon le dispositif.

- \\( \beta \\) n'est pas parfaitement constant—il varie légèrement avec la température, la tension et les niveaux de courant—mais dans l'analyse de base, nous supposons qu'il est constant dans la région active.
- Le courant de collecteur a également une petite composante de fuite (\\( I_{CBO} \\)), mais elle est négligeable : \\( I_C = \beta I_B + (1 + \beta) I_{CBO} \approx \beta I_B \\).

#### Gain en courant continu vs. Gain petit signal (incrémental)
- **\\( \beta \\) continu** : Calculé à un point de fonctionnement spécifique en utilisant les courants instantanés : \\( \beta = \frac{I_C}{I_B} \\).
- **\\( \beta \\) petit signal (ou \\( h_{fe} \\))** : Pour les changements dynamiques (par exemple, signaux AC), c'est le rapport des petites variations : \\( \beta \approx \frac{\Delta I_C}{\Delta I_B} \\). Ceci est utile lorsque le transistor est polarisé en un point et que nous appliquons une petite variation, car \\( \beta \\) est supposé constant sur cette petite plage.

Dans des problèmes comme celui-ci, où les courants "passent de" une valeur à une autre, l'approche incrémentale donne souvent le \\( \beta \\) "approximatif" si le changement est petit par rapport au point de fonctionnement.

### Application au problème
Le scénario : Transistor en région active. Le courant de base augmente de \\( I_{B1} = 12 \, \mu\text{A} \\) à \\( I_{B2} = 22 \, \mu\text{A} \\). Le courant de collecteur passe de \\( I_{C1} = 1 \, \text{mA} \\) à \\( I_{C2} = 2 \, \text{mA} \\).

Tout d'abord, convertissez les unités pour la cohérence (1 mA = 1000 μA) :
- \\( I_{B1} = 0,012 \, \text{mA} \\), \\( I_{B2} = 0,022 \, \text{mA} \\).
- \\( \Delta I_B = I_{B2} - I_{B1} = 0,022 - 0,012 = 0,010 \, \text{mA} \\) (ou 10 μA).
- \\( \Delta I_C = I_{C2} - I_{C1} = 2 - 1 = 1 \, \text{mA} \\).

#### \\( \beta \\) continu à chaque point
- Au point initial : \\( \beta_1 = \frac{I_{C1}}{I_{B1}} = \frac{1}{0,012} \approx 83,33 \\).
- Au point final : \\( \beta_2 = \frac{I_{C2}}{I_{B2}} = \frac{2}{0,022} \approx 90,91 \\).

Ces valeurs correspondent de près aux options A (83) et B (91), mais \\( \beta \\) n'est pas constant ici—il a légèrement augmenté, ce qui peut se produire dans les transistors réels en raison de facteurs comme l'effet Early (modulation de la largeur de base). Cependant, le problème demande "son gain en courant \\( \beta \\) est approximativement", ce qui implique une valeur unique, et les changements sont significatifs (augmentation de 83% de \\( I_B \\), 100% de \\( I_C \\)), donc les points de fonctionnement seuls ne capturent pas un \\( \beta \\) "constant".

#### \\( \beta \\) incrémental (Petit signal)
En supposant que \\( \beta \\) est à peu près constant sur la plage de fonctionnement, la meilleure estimation est la pente de la ligne \\( I_C \\) vs. \\( I_B \\) :
\\[
\beta \approx \frac{\Delta I_C}{\Delta I_B} = \frac{1 \, \text{mA}}{0,010 \, \text{mA}} = 100.
\\]

Cela correspond exactement à l'option C. Pourquoi utiliser cela ?
- Dans le modèle de la région active, \\( I_C = \beta I_B \\) est linéaire, donc le rapport des changements reflète directement le gain.
- La moyenne des points de fonctionnement continu est \\( \frac{83,33 + 90,91}{2} \approx 87 \\), mais ce n'est pas une option et ignore l'hypothèse de linéarité.
- L'option D (183) pourrait provenir d'un mauvais calcul comme \\( \frac{2}{0,011} \\) ou du doublement de quelque chose, mais c'est incorrect.

Graphiquement, si vous tracez \\( I_C \\) en fonction de \\( I_B \\) :
- Points : (0,012, 1) et (0,022, 2).
- Pente = montée/course = \\( \frac{1}{0,01} = 100 \\).

Ce \\( \beta \\) incrémental est ce que les concepteurs de circuits utilisent souvent pour l'analyse du point de polarisation ou les modèles petit signal.

### Pourquoi c'est important en pratique
Dans les amplificateurs, vous polarisez le transistor dans la région active (par exemple, à des courants de point milieu) afin que les petites variations de signal restent linéaires autour de \\( \\beta \\). Ici, le changement est important, mais le problème teste la compréhension de la relation proportionnelle.

Si \\( \beta \\) variait de manière plus importante, nous aurions besoin d'une simulation SPICE complète, mais pour les QCM, 100 est la réponse attendue.

Pour une lecture plus approfondie :  
[All About Circuits: BJT Fundamentals](https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/bipolar-junction-transistor-bjt/)  
[Electronics Tutorials: Transistor as an Amplifier](https://www.electronics-tutorials.ws/amplifier/transistor-amplifier.html)