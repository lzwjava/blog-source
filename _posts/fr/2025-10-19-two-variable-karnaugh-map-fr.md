---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Exemple de Tableau de Karnaugh à Deux Variables
translated: true
type: note
---

### Exemple simple de carte de Karnaugh : fonction à 2 variables

Prenons une fonction booléenne très basique à 2 variables : f(A, B) = A'B + AB' + AB (somme des mintermes m(1, 2, 3)). C'est la porte OR : f = A + B, mais nous allons la "découvrir" en utilisant une carte de K.

#### Étape 1 : Construire la carte de K
Une carte de K à 2 variables est une grille 2x2. Lignes pour A (0, 1), colonnes pour B (0, 1) en code Gray (déjà simple). Placez des 1 pour les mintermes :

| A \ B | 0 (B') | 1 (B) |
|-------|--------|-------|
| **0 (A')** | 0 (m0) | 1 (m1) |
| **1 (A)**  | 1 (m2) | 1 (m3) |

#### Étape 2 : Grouper les 1 adjacents
Recherchez les plus grands groupes de 1 (puissances de 2 : 1, 2, 4...). Adjacent signifie partager un côté (pas de diagonales).

- **Groupe 1** : Colonne de droite (m1 et m3) — une paire verticale. Commun : B (A varie, donc sans importance).
- **Groupe 2** : Ligne du bas (m2 et m3) — une paire horizontale. Commun : A (B varie).

(Le chevauchement sur m3 est acceptable.)

#### Étape 3 : Déduire l'expression minimisée
Chaque groupe donne un terme :
- Groupe 1 : **B**
- Groupe 2 : **A**

Expression minimisée : f = A + B

Cela simplifie l'expression de 3 termes (9 littéraux à l'origine, en fait non : 3 termes avec 2 littéraux chacun) à 2 termes avec 1 littéral chacun — moins de portes logiques !

Cela correspond à la fonction OR. Pour un exercice encore plus simple, essayez avec uniquement des 1 : les groupes se réduisent à 1 (vrai).

[All About Circuits: Karnaugh Maps](https://www.allaboutcircuits.com/textbook/digital/chpt-7/karnaugh-mapping/)