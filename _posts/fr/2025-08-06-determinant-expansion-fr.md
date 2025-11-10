---
audio: false
generated: true
image: false
lang: fr
layout: post
title: 'Déterminant : Développement par Linéarité et Alternance'
translated: true
type: note
---

Lorsque vous apprenez que le déterminant est une fonction qui est

1. **multilinéaire** dans les lignes (ou les colonnes), et
2. **alternée** (échanger deux lignes inverse son signe),

la formule de développement par cofacteurs en découle naturellement. Voici un « pourquoi » étape par étape pour le cas 3×3 :

---

### 1. Déterminant via les permutations

La définition la plus générale d'un déterminant 3×3 est

$$
\det A \;=\;
\sum_{\sigma\in S_3}\!\mathrm{sgn}(\sigma)\,a_{1,\sigma(1)}\,a_{2,\sigma(2)}\,a_{3,\sigma(3)},
$$

où l'on somme sur les six permutations σ de {1,2,3}, et sgn(σ) vaut +1 pour les permutations paires et –1 pour les permutations impaires.

Si on les écrit explicitement, on obtient exactement les six termes :

$$
a_{11}a_{22}a_{33},\;a_{12}a_{23}a_{31},\;a_{13}a_{21}a_{32}
\;-\;
\bigl(a_{13}a_{22}a_{31}+a_{11}a_{23}a_{32}+a_{12}a_{21}a_{33}\bigr).
$$

---

### 2. Regroupement par une ligne ou une colonne

Remarquez que vous pouvez **grouper** ces six termes selon l'élément de la première ligne qu'ils utilisent :

* Termes contenant \$a\_{11}\$ :

  $$
    a_{11}\,(a_{22}a_{33} - a_{23}a_{32})
    = a_{11}\det\!\begin{pmatrix}a_{22}&a_{23}\\a_{32}&a_{33}\end{pmatrix}.
  $$
* Termes contenant \$a\_{12}\$ :

  $$
    a_{12}\,(a_{23}a_{31} - a_{21}a_{33})
    = -\,a_{12}\det\!\begin{pmatrix}a_{21}&a_{23}\\a_{31}&a_{33}\end{pmatrix}.
  $$
* Termes contenant \$a\_{13}\$ :

  $$
    a_{13}\,(a_{21}a_{32} - a_{22}a_{31})
    = \;a_{13}\det\!\begin{pmatrix}a_{21}&a_{22}\\a_{31}&a_{32}\end{pmatrix}.
  $$

C'est exactement le **développement par cofacteurs le long de la première ligne** :

$$
\det A
= a_{11}C_{11} \;+\; a_{12}C_{12} \;+\; a_{13}C_{13},
$$

où chaque cofacteur $C_{1j} = (-1)^{1+j}\det(\text{mineur}_{1j})$.

---

### 3. Pourquoi des « mineurs » et des « signes » ?

* **Mineur** : $\det(\text{mineur}_{ij})$ est le déterminant de la sous-matrice 2×2 obtenue en supprimant la ligne i et la colonne j.
* **Facteur de signe** $(−1)^{i+j}$ : garantit que si vous échangez deux lignes de $A$, le signe global s'inverse—exactement comme l'exige la définition par permutation.

Parce que le déterminant doit être linéaire dans chaque ligne, vous pouvez « extraire » un élément d'une ligne, laissant le déterminant de la matrice plus petite multiplié par cet élément. La propriété d'alternance impose ces signes $(−1)$.

---

### 4. Intuition géométrique

Pour une matrice 3×3 dont les lignes sont des vecteurs $\mathbf{u},\mathbf{v},\mathbf{w}\in\mathbb{R}^3$, $\det A$ est le volume signé du parallélépipède qu'ils engendrent.

* Développer le long de, disons, la première ligne, revient à décomposer ce volume en « tranches » perpendiculaires à chaque axe de coordonnées.
* L'aire de chaque tranche est l'aire du parallélogramme engendré par les deux autres vecteurs-lignes (un déterminant 2×2), et vous la mettez à l'échelle avec la coordonnée correspondante $u_j$ de $\mathbf{u}$.
* Le signe $(−1)^{1+j}$ garde une trace de l'orientation.

---

### 5. Généralisation à $n\times n$

Tout cela fonctionne de la même manière pour n'importe quelle taille $n$ : la définition par permutation a $n!$ termes, vous les regroupez par une ligne ou une colonne, et chaque groupe se réduit à

$$
a_{ij}\,(-1)^{i+j}\det(\text{mineur}_{ij}).
$$

C'est le principe du **développement par cofacteurs**.

---

**En bref :**
Le développement par cofacteurs est simplement la définition du déterminant par une somme de permutations, réorganisée selon une ligne (ou une colonne), combinée aux exigences de linéarité et d'alternance de signe. Il offre un moyen récursif de calculer—et une image géométrique claire—du déterminant.