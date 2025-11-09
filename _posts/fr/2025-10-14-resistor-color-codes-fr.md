---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Décoder les codes de couleurs des résistances
translated: true
type: note
---

### Comprendre les codes couleur des résistances

Les résistances sont de petits composants électroniques qui limitent le flux du courant électrique, et leur valeur de résistance (mesurée en ohms, Ω) est souvent indiquée par des bandes colorées sur leur corps. Ces bandes suivent un système de code couleur standardisé. La plupart des résistances ont 4, 5 ou 6 bandes, mais les types à 4 et 5 bandes sont les plus courants. Lisez toujours les bandes de gauche à droite, en commençant par la bande la plus proche d'une extrémité (l'"extrémité de lecture"). La bande de tolérance (souvent dorée ou argentée) est généralement sur le côté droit—si vous n'êtes pas sûr, tournez la résistance de manière à ce que toute bande métallique soit sur la droite.

#### Tableau des codes couleur
Chaque couleur représente un chiffre (0-9) pour les chiffres significatifs, ou un multiplicateur (puissance de 10) pour mettre à l'échelle la valeur. Voici la correspondance standard :

| Couleur  | Valeur numérique | Multiplicateur (Puissance de 10) |
|----------|------------------|-----------------------------------|
| Noir     | 0                | ×10⁰ (1)                         |
| Marron   | 1                | ×10¹ (10)                        |
| Rouge    | 2                | ×10² (100)                       |
| Orange   | 3                | ×10³ (1 000)                     |
| Jaune    | 4                | ×10⁴ (10 000)                    |
| Vert     | 5                | ×10⁵ (100 000)                   |
| Bleu     | 6                | ×10⁶ (1 000 000)                 |
| Violet   | 7                | ×10⁷ (10 000 000)                |
| Gris     | 8                | ×10⁸ (100 000 000)               |
| Blanc    | 9                | ×10⁹ (1 000 000 000)             |
| Or       | -                | ×10⁻¹ (0.1)                      |
| Argent   | -                | ×10⁻² (0.01)                     |

#### Bandes de tolérance
La ou les dernière(s) bande(s) indique(nt) la tolérance (précision de la valeur de résistance) :
- Marron : ±1 %
- Rouge : ±2 %
- Vert : ±0.5 %
- Bleu : ±0.25 %
- Violet : ±0.1 %
- Gris : ±0.05 %
- Or : ±5 %
- Argent : ±10 %
- Aucune bande : ±20 %

#### Comment lire une résistance à 4 bandes
1. Identifiez les deux premières bandes comme les chiffres significatifs (par exemple, marron-noir = 10).
2. La troisième bande est le multiplicateur—multipliez les chiffres par cette puissance de 10 (par exemple, rouge = ×100, donc 10 × 100 = 1 000 Ω).
3. La quatrième bande est la tolérance (par exemple, or = ±5 %).

**Exemple** : Marron (1), noir (0), rouge (×100), or (±5 %) = 10 × 100 = 1 000 Ω ±5 % (ou 1 kΩ).

#### Comment lire une résistance à 5 bandes
Elles offrent une plus grande précision avec un chiffre significatif supplémentaire.
1. Identifiez les trois premières bandes comme les chiffres significatifs (par exemple, marron-noir-rouge = 102).
2. La quatrième bande est le multiplicateur (par exemple, orange = ×1 000, donc 102 × 1 000 = 102 000 Ω).
3. La cinquième bande est la tolérance (par exemple, marron = ±1 %).

**Exemple** : Marron (1), noir (0), rouge (2), orange (×1 000), marron (±1 %) = 102 × 1 000 = 102 000 Ω ±1 % (ou 102 kΩ).

#### Notes
- Pour les résistances à 6 bandes, les cinq premières bandes suivent le motif à 5 bandes, et la sixième indique le coefficient de température (comment la résistance change avec la chaleur, par exemple, marron = 100 ppm/°C).
- Si les bandes sont décolorées ou peu claires, utilisez un multimètre pour mesurer la résistance réelle.
- Les résistances de zéro ohm (cavaliers) peuvent avoir une seule bande noire.

[How To Read Resistor Color Codes | Arrow.com](https://www.arrow.com/en/research-and-events/articles/resistor-color-code)  
[RESISTOR COLOR CODE GUIDE (PDF)](https://neurophysics.ucsd.edu/courses/physics_120/resistorcharts.pdf)