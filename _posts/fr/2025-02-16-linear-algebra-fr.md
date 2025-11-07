---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Algèbre linéaire
translated: true
type: post
---

- La **Singular Value Decomposition** (SVD) peut être utilisée pour la compression d'images.

- Le **déterminant** d'une matrice indique combien l'aire change lorsque la matrice est appliquée à une forme.

- Les **valeurs propres** sont définies par l'équation \\[ \det(\lambda I - A) = 0 \\].

- Le package `linalg` de **NumPy** peut être utilisé pour étudier et résoudre des problèmes d'**algèbre linéaire**.

- Utilisez les **transformations d'algèbre linéaire** dans un **espace** à n dimensions pour comprendre les matrices.

- Une **matrice** est un groupe de nombres disposés en lignes et en colonnes.

- L'équation \\[ Ax = B \\] a une solution lorsque \\[ \text{rang}(A) = \text{rang}([A \mid B]) \\].

- Le **rang** d'une matrice est le nombre de lignes (ou colonnes) linéairement indépendantes dans sa **forme échelonnée**.

---

À quoi sert le concept de **rang** ?
Il nous indique combien de lignes conservent leur information lors d'une **transformation linéaire**. En revanche, la **nullité** (dimension de l'**espace nul**) compte combien de lignes sont envoyées vers zéro.

Quelle est la différence entre une matrice et un simple tableau de nombres ?
Un tableau n'a pas de direction inhérente, alors qu'une matrice en a une.

Quelle est la différence entre une matrice et un vecteur ?
Un **vecteur** est une colonne unidimensionnelle de nombres et possède une direction.

La **multiplication de matrices** suit une règle fixe : le nombre de colonnes de la première matrice doit être égal au nombre de lignes de la deuxième matrice. Une matrice 2×3 multipliée par une matrice 3×4 donne une matrice 2×4. Dans la matrice résultante, la valeur à la position (i, j) est le **produit scalaire** de la i-ème ligne de la matrice A et de la j-ème colonne de la matrice B.

Le **déterminant** d'une matrice a une signification : s'il n'est pas égal à 0, la matrice est **inversible**.