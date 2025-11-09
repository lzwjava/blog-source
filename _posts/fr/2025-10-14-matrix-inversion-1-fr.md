---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Inversion d'une matrice 3x3
translated: true
type: note
---

D'accord — décomposons cela clairement et intuitivement, sans aucun formatage de tableau pour que ce soit facile à lire ligne par ligne.

---

### 1. Quel est l'objectif
Nous voulons trouver l'inverse d'une matrice 3×3, généralement notée A⁻¹.
L'inverse est la matrice qui « annule » A, ce qui signifie
A × A⁻¹ = I,
où I est la matrice identité.

---

### 2. La formule de base
La formule générale pour toute matrice carrée inversible est

A⁻¹ = (1 / det(A)) × adj(A).

Nous avons donc besoin de deux ingrédients :
- le déterminant det(A), et
- la matrice adjointe adj(A), qui est la transposée de la matrice des cofacteurs.

---

### 3. Déterminant d'une matrice 3×3
Si
A =
[a  b  c]
[d  e  f]
[g  h  i],

alors

det(A) = a(ei − fh) − b(di − fg) + c(dh − eg).

Cette valeur indique si la matrice est inversible :
- si det(A) = 0 → pas d'inverse (la matrice est singulière),
- si det(A) ≠ 0 → l'inverse existe.

---

### 4. Cofacteurs
Pour construire adj(A), nous trouvons d'abord le cofacteur de chaque élément.
Le cofacteur de l'entrée aᵢⱼ est
Cᵢⱼ = (−1)^(i+j) × Mᵢⱼ,
où Mᵢⱼ est le déterminant de la sous-matrice 2×2 obtenue après suppression de la ligne i et de la colonne j.

Faire cela pour les neuf positions donne la « matrice des cofacteurs ».
Pour le cas général ci-dessus :

C₁₁ = ei − fh
C₁₂ = −(di − fg)
C₁₃ = dh − eg

C₂₁ = −(bi − ch)
C₂₂ = ai − cg
C₂₃ = −(ah − bg)

C₃₁ = bf − ce
C₃₂ = −(af − cd)
C₃₃ = ae − bd

---

### 5. Transposer la matrice des cofacteurs
Maintenant, prenez cette matrice des cofacteurs et transposez-la — ce qui signifie échanger les lignes et les colonnes.
Cette nouvelle matrice est appelée l'**adjointe** de A, notée adj(A).
Si vous pensez visuellement, cette « transposition » est comme une rotation de la matrice : ce qui était dans la première ligne devient la première colonne, et ainsi de suite.

---

### 6. Multiplier par 1/det(A)
Enfin, mettez à l'échelle la matrice adjointe en divisant chaque terme par det(A).
Cela vous donne A⁻¹.

Symboliquement :
A⁻¹ = (1/det(A)) × adj(A).

---

### 7. Pourquoi cela fonctionne
Cette formule provient d'une propriété fondamentale des déterminants et des cofacteurs :

A × adj(A) = det(A) × I.

Si vous divisez les deux côtés par det(A), vous obtenez exactement
A × [(1/det(A)) × adj(A)] = I.

Ainsi, le facteur de droite doit être l'inverse.

La raison pour laquelle cette identité est vraie est que lorsque vous multipliez A par sa matrice des cofacteurs, chaque terme diagonal devient le déterminant lui-même (puisque c'est le développement le long de cette ligne), et chaque terme non diagonal devient zéro en raison des signes alternés des cofacteurs — c'est l'annulation algébrique à l'œuvre.

---

### 8. Exemple
Soit
A =
[1  2  3]
[0  1  4]
[5  6  0].

Calculez det(A) :
= 1(1×0 − 4×6) − 2(0×0 − 4×5) + 3(0×6 − 1×5)
= (−24) − (−40) + (−15)
= −24 + 40 − 15 = 1.

Donc det(A) = 1.

Ensuite, trouvez tous les cofacteurs (un peu fastidieux, mais simple), transposez-les pour obtenir adj(A), et puisque det(A) = 1, l'adjointe est déjà l'inverse.

---

### 9. Intuition résumée
- Déterminant → une mesure de la façon dont la matrice « met à l'échelle l'espace ».
- Cofacteur → capture la contribution de chaque élément à cette mise à l'échelle.
- Transposition → aligne ces contributions pour que la multiplication reconstruise l'identité.
- Division par le déterminant → normalise la mise à l'échelle.

---

Souhaitez-vous que je montre les calculs détaillés des cofacteurs pour cet exemple (celui avec [1 2 3; 0 1 4; 5 6 0]) afin que vous puissiez voir chaque mineur et signe ?