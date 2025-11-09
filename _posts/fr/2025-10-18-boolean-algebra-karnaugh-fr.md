---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Simplification de l'algèbre de Boole par les tables de Karnaugh
translated: true
type: note
---

### Que sont les cartes de Karnaugh ?

Les cartes de Karnaugh (souvent abrégées en K-map) sont un outil graphique utilisé dans la conception de logique numérique pour simplifier les expressions d'algèbre booléenne. Elles fournissent une méthode visuelle pour minimiser les fonctions logiques, facilitant ainsi la réduction du nombre de portes nécessaires dans un circuit. Inventées par Maurice Karnaugh en 1953, les K-maps sont particulièrement utiles pour les fonctions comportant jusqu'à 4 ou 5 variables (au-delà, des algorithmes informatiques comme Quine-McCluskey sont préférés).

#### Concepts Clés
- **Simplification d'expression booléenne** : Les K-maps aident à convertir une table de vérité ou une forme de somme de produits (SOP) en une expression minimisée en identifiant des motifs de 1 (sorties vraies) dans la fonction.
- **Structure en grille** : La carte est une grille rectangulaire où chaque cellule représente une combinaison d'entrées possible (minterme). Les lignes et les colonnes sont étiquetées avec des valeurs binaires dans l'ordre du code Gray (pour garantir que les cellules adjacentes ne diffèrent que d'un seul bit).
- **Règle de regroupement** : Pour simplifier, regroupez les 1 adjacents par puissances de 2 (1, 2, 4, 8, etc.). Chaque groupe représente un terme produit dans l'expression simplifiée. Les chevauchements de groupes sont autorisés, et l'objectif est de couvrir tous les 1 avec le moins de groupes possible, les plus grands possibles.
- **Adjacence** : Les cellules sont adjacentes si elles partagent une arête (y compris le bouclage sur les bords de la carte, comme un tore).

Les K-maps fonctionnent mieux pour les formes SOP (somme de produits) ou POS (produit de sommes) et supposent que la fonction est donnée sous forme canonique.

#### Exemple Simple : K-Map à 2 variables
Considérons la fonction booléenne \\( f(A, B) = \sum m(0, 1, 3) \\) (mintermes où la sortie est 1).

La K-map ressemble à ceci :

|       | B=0 | B=1 |
|-------|-----|-----|
| **A=0** | 1   | 1   |
| **A=1** | 0   | 1   |

- Groupes : Un groupe de deux 1 dans la ligne du haut (couvre \\( A' \\)), et un seul 1 en bas à droite (couvre \\( AB \\)).
- Expression simplifiée : \\( f(A, B) = A' + AB \\), qui peut être encore simplifiée en \\( A' + B \\) (mais la carte montre directement les impliquants premiers).

#### Exemple à 3 variables
Pour \\( f(A, B, C) = \sum m(1, 2, 6, 7) \\) :

|         | BC=00 | BC=01 | BC=11 | BC=10 |
|---------|-------|-------|-------|-------|
| **A=0** | 0     | 1     | 0     | 1     |
| **A=1** | 0     | 0     | 1     | 1     |

- Groupes : Un groupe de quatre 1 (quad) qui s'enroule : cellules pour m1, m2, m6, m7, couvrant \\( B \\).
- Simplifiée : \\( f(A, B, C) = B \\).

#### Avantages et Limites
- **Avantages** : Intuitif pour les petites fonctions, réduit les erreurs dans la simplification manuelle, visualise les cas indifférents (marqués X, qui peuvent être traités comme 1 ou 0 pour agrandir les groupes).
- **Inconvénients** : Ne passe pas à l'échelle pour de nombreuses variables ; ne gère pas bien le XOR sans modifications.

Les K-maps sont un pilier des programmes d'ingénierie informatique et sont pratiques pour la conception FPGA/ASIC.

Pour plus de détails, voir [Carte de Karnaugh sur Wikipédia](https://fr.wikipedia.org/wiki/Tableau_de_Karnaugh).