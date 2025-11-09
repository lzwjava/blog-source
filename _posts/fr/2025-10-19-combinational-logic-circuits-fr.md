---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide des circuits logiques combinatoires
translated: true
type: note
---

Ce guide couvre les concepts clés du chapitre sur les circuits logiques combinatoires dans *Fondamentaux de la technologie électronique (III)*. Les circuits logiques combinatoires sont des systèmes numériques où la sortie dépend uniquement des entrées actuelles, sans éléments de mémoire (contrairement aux circuits séquentiels). Nous le décomposerons en sections spécifiées : l'analyse et la conception, les modules courants, et les aléas avec les méthodes d'élimination. L'accent est mis sur la compréhension pratique, avec des exemples et des explications étape par étape.

## 1. Analyse et conception des circuits logiques combinatoires

### Analyse
L'analyse consiste à déterminer le comportement en sortie d'un circuit donné à partir de sa description au niveau des portes.

- **Tables de vérité** : La base de l'analyse. Lister toutes les combinaisons d'entrées possibles et calculer les sorties.
  - Pour un circuit avec *n* entrées, il y a 2^n lignes.
  - Exemple : Analyser un circuit ET-OU à 2 entrées : Sortie = (A · B) + (A' · B') (où ' désigne NON).

    | A | B | A · B | A' · B' | Sortie |
    |---|---|-------|---------|--------|
    | 0 | 0 |   0   |    1    |   1    |
    | 0 | 1 |   0   |    0    |   0    |
    | 1 | 0 |   0   |    0    |   0    |
    | 1 | 1 |   1   |    0    |   1    |

    Cela se simplifie en A XOR B (OU exclusif).

- **Tableaux de Karnaugh (K-Maps)** : Outil visuel pour simplifier les expressions booléennes lors de l'analyse.
  - Représenter les mintermes (1) sur une grille ; regrouper les 1 adjacents (puissances de 2) pour trouver les impliquants premiers.
  - Réduit à la forme somme de produits (SOP) ou produit de sommes (POS).

### Conception
La conception part d'un cahier des charges (par exemple, une table de vérité ou une description textuelle) et construit le circuit.

- **Étapes** :
  1. Déduire la table de vérité à partir des spécifications.
  2. Écrire l'expression canonique SOP/POS (somme/produit des mintermes/maxtermes).
  3. Simplifier en utilisant les K-Maps ou la méthode de Quine-McCluskey.
  4. Implémenter avec des portes (ET, OU, NON, NAND, NOR).

- **Exemple de conception** : Concevoir un circuit pour un voteur majoritaire (sortie 1 si au moins deux des trois entrées A, B, C sont à 1).
  - Table de vérité (partielle) :

    | A | B | C | Sortie |
    |---|---|---|--------|
    | 0 | 0 | 0 |   0    |
    | 0 | 0 | 1 |   0    |
    | 0 | 1 | 1 |   1    |
    | 1 | 0 | 1 |   1    |
    | 1 | 1 | 0 |   1    |
    | 1 | 1 | 1 |   1    |

  - K-Map (pour SOP) :
    ```
    CD\AB | 00 | 01 | 11 | 10
    ------|----|----|----|----
    00    | 0  | 0  | 0  | 0
    01    | 0  | 0  | 1  | 0
    11    | 0  | 1  | 1  | 1
    10    | 0  | 1  | 1  | 0
    ```
    (Lignes/colonnes étiquetées en code Gray.)

  - Simplifiée : F = AB + AC + BC.
  - Implémentation avec portes : Trois portes ET pour chaque terme, une porte OU.

Conseil : Toujours vérifier par simulation ou ré-analyser le circuit final.

## 2. Modules courants

Ce sont des blocs de construction standard pour des systèmes plus grands, réduisant la complexité de la conception.

### Encodeurs
- Convertissent une ou plusieurs entrées actives en code binaire.
- Exemple : Encodeur de priorité 4 vers 2 (entrées : Y3, Y2, Y1, Y0 ; sorties : A1, A0 ; drapeau valide V).
  - Table de vérité :

    | Y3 | Y2 | Y1 | Y0 | A1 | A0 | V |
    |----|----|----|----|----|----|---|
    | 0  | 0  | 0  | 1  | 0  | 0  | 1 |
    | 0  | 0  | 1  | X  | 0  | 1  | 1 |
    | 0  | 1  | X  | X  | 1  | 0  | 1 |
    | 1  | X  | X  | X  | 1  | 1  | 1 |
    | 0  | 0  | 0  | 0  | X  | X  | 0 |

  - Logique : A1 = Y3 + Y2; A0 = Y3 + Y1; V = Y3 + Y2 + Y1 + Y0.
  - Utilisation : Conversion d'entrée clavier en binaire.

### Décodeurs
- Opposé des encodeurs : Entrée binaire vers sortie one-hot (active une ligne).
- Exemple : Décodeur 2 vers 4 (entrées : A1, A0 ; sorties : D0-D3).
  - Table de vérité :

    | A1 | A0 | D3 | D2 | D1 | D0 |
    |----|----|----|----|----|----|
    | 0  | 0  | 0  | 0  | 0  | 1  |
    | 0  | 1  | 0  | 0  | 1  | 0  |
    | 1  | 0  | 0  | 1  | 0  | 0  |
    | 1  | 1  | 1  | 0  | 0  | 0  |

  - Logique : D0 = A1' · A0'; D1 = A1' · A0; etc.
  - Utilisation : Adressage de mémoire, pilotes d'afficheurs 7 segments.

### Multiplexeurs (MUX)
- Sélectionnent une entrée parmi plusieurs vers une sortie unique en fonction de lignes de sélection.
- Exemple : MUX 4 vers 1 (entrées : I0-I3 ; sélections : S1, S0 ; sortie : Y).
  - Table de vérité :

    | S1 | S0 | Y  |
    |----|----|----|
    | 0  | 0  | I0 |
    | 0  | 1  | I1 |
    | 1  | 0  | I2 |
    | 1  | 1  | I3 |

  - Logique : Y = (S1' · S0' · I0) + (S1' · S0 · I1) + (S1 · S0' · I2) + (S1 · S0 · I3).
  - Cascadage : Construire des MUX plus grands (par exemple, 8 vers 1 à partir de deux 4 vers 1).
  - Utilisation : Routage de données, générateurs de fonctions (implémenter toute fonction à n variables avec un MUX 2^n vers 1).

## 3. Aléas et méthodes d'élimination

Les aléas sont des glitches indésirables (sorties temporairement incorrectes) dus à des différences de temporisation dans les délais des portes, même si la logique en régime permanent est correcte.

### Types d'aléas
- **Aléa statique** : La sortie devrait rester constante (0→0 ou 1→1) mais présente un glitch.
  - Statique-1 : Dû à un terme produit manquant dans SOP (par exemple, transition où deux termes se chevauchent insuffisamment).
- **Aléa dynamique** : La sortie devrait changer (0→1 ou 1→0) mais oscille plusieurs fois.
  - Plus complexe, souvent dû à plusieurs aléas statiques.

- **Détection** : Utiliser des diagrammes temporels ou des couvertures d'aléas sur les K-Maps (vérifier les 1 adjacents pour les changements de variable unique).

Exemple : Circuit SOP F = AB + A'C (aléa statique-1 sur A=1, B:0→1, C=1 ; glitch si le terme AB est retardé).

### Méthodes d'élimination
- **Ajouter des termes redondants (Couvertures d'aléas)** :
  - Dans le K-Map, ajouter des impliquants supplémentaires pour couvrir les transitions (par exemple, ajouter AC pour l'exemple : F = AB + A'C + AC).
  - Assure un chevauchement pendant les changements ; augmente le nombre de portes mais élimine les glitches.

- **Utiliser des implémentations sans aléas** :
  - Impliquants premiers essentiels (EPI) + termes de consensus.
  - Pour les dynamiques : S'assurer d'une seule transition par variable.

- **Autres techniques** :
  - Délais équilibrés (égaliser les chemins des portes, peu pratique en VLSI).
  - Corrections basées sur des verrous (mais c'est séquentiel).
  - Outils de simulation pour la vérification.

Conseils : Les aléas sont critiques dans les conceptions haute vitesse ; toujours vérifier les changements d'une seule entrée.

## Résumé et conseils pratiques
- **Point clé** : La logique combinatoire consiste à mapper efficacement les entrées vers les sorties. Maîtrisez les tables de vérité et les K-Maps — ils sont utilisés partout.
- **Pratique** : Concevoir un additionneur complet en utilisant un MUX ; analyser un décodeur pour les aléas.
- **Prochaines étapes** : Passer à la logique séquentielle pour les éléments de mémoire.

Pour approfondir, reportez-vous aux textes standard comme *Digital Design* de Mano.

[Digital Design par M. Morris Mano](https://www.pearson.com/us/higher-education/program/Morris-Mano-Digital-Design-with-an-Introduction-to-the-Verilog-HDL-5th-Edition/PGM110392.html)  
[Fundamentals of Digital Logic with Verilog Design par Brown et Vranesic](https://www.mheducation.com/highered/product/fundamentals-digital-logic-verilog-design-brown-vranesic/M9780073380544.html)