---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Inversion d'une matrice 3x3
translated: true
type: note
---

Oui, tu es sur la bonne voie ! Tu décris la méthode standard pour trouver l'inverse d'une matrice 3×3 \\( A \\) (souvent noté \\( A^{-1} \\)) en utilisant la **matrice des cofacteurs** (ou plus précisément, la **matrice adjointe**, qui est la transposée de la matrice des cofacteurs). La partie "diviseur 1/valeur * matrice" fait référence à la mise à l'échelle par \\( 1/\det(A) \\), où \\( \det(A) \\) est le déterminant de \\( A \\). Et "rotation" pourrait vouloir dire "transposition" (transformer les lignes en colonnes) — c'est aussi une étape clé.

Je vais expliquer la méthode étape par étape, pourquoi elle fonctionne, et comment la calculer pour une matrice 3×3 générale. Cela découle de la formule générale pour l'inverse d'une matrice : \\( A^{-1} = \frac{1}{\det(A)} \adj(A) \\), où \\( \adj(A) \\) est l'adjointe.

### Méthode Étape par Étape pour une Matrice 3×3
Supposons que ta matrice soit :
\\[
A = \begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{pmatrix}
\\]

1.  **Calculer le Déterminant \\( \det(A) \\)** (la "valeur" par laquelle on divise) :
    \\[
    \det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
    \\]
    Si \\( \det(A) = 0 \\), la matrice n'a pas d'inverse (elle est singulière). Sinon, on continue.

2.  **Trouver la Matrice des Cofacteurs \\( C \\)** :
    - Le cofacteur \\( C_{ij} \\) pour l'élément \\( a_{ij} \\) est \\( (-1)^{i+j} \\) fois le déterminant de la sous-matrice 2×2 obtenue en supprimant la ligne \\( i \\) et la colonne \\( j \\).
    - Tu n'as pas besoin de calculer *tous* les cofacteurs à partir de zéro — tu peux les calculer le long d'une ligne (ou d'une colonne) et utiliser des propriétés pour remplir le reste, mais pour une 3×3, c'est rapide de tous les faire.

    Les cofacteurs sont :
    \\[
    C_{11} = (-1)^{2} \det\begin{pmatrix} e & f \\ h & i \end{pmatrix} = ei - fh
    \\]
    \\[
    C_{12} = (-1)^{3} \det\begin{pmatrix} d & f \\ g & i \end{pmatrix} = -(di - fg)
    \\]
    \\[
    C_{13} = (-1)^{4} \det\begin{pmatrix} d & e \\ g & h \end{pmatrix} = dh - eg
    \\]
    \\[
    C_{21} = (-1)^{3} \det\begin{pmatrix} b & c \\ h & i \end{pmatrix} = -(bi - ch)
    \\]
    \\[
    C_{22} = (-1)^{4} \det\begin{pmatrix} a & c \\ g & i \end{pmatrix} = ai - cg
    \\]
    \\[
    C_{23} = (-1)^{5} \det\begin{pmatrix} a & b \\ g & h \end{pmatrix} = -(ah - bg)
    \\]
    \\[
    C_{31} = (-1)^{4} \det\begin{pmatrix} b & c \\ e & f \end{pmatrix} = bf - ce
    \\]
    \\[
    C_{32} = (-1)^{5} \det\begin{pmatrix} a & c \\ d & f \end{pmatrix} = -(af - cd)
    \\]
    \\[
    C_{33} = (-1)^{6} \det\begin{pmatrix} a & b \\ d & e \end{pmatrix} = ae - bd
    \\]

    Donc la matrice des cofacteurs est :
    \\[
    C = \begin{pmatrix}
    ei-fh & -(di-fg) & dh-eg \\
    -(bi-ch) & ai-cg & -(ah-bg) \\
    bf-ce & -(af-cd) & ae-bd
    \end{pmatrix}
    \\]

3.  **Transposer pour Obtenir l'Adjointe \\( \adj(A) = C^T \\)** (c'est l'étape de "rotation" — échanger les lignes et les colonnes) :
    \\[
    \adj(A) = \begin{pmatrix}
    ei-fh & -(bi-ch) & bf-ce \\
    -(di-fg) & ai-cg & -(af-cd) \\
    dh-eg & -(ah-bg) & ae-bd
    \end{pmatrix}
    \\]

4.  **Mettre à l'échelle par \\( 1/\det(A) \\)** pour Obtenir l'Inverse :
    \\[
    A^{-1} = \frac{1}{\det(A)} \adj(A)
    \\]
    Chaque entrée de \\( \adj(A) \\) est multipliée par \\( 1/\det(A) \\).

### Exemple
Soit \\( A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix} \\).

-   \\( \det(A) = 1(1\cdot0 - 4\cdot6) - 2(0\cdot0 - 4\cdot5) + 3(0\cdot6 - 1\cdot5) = 1(-24) - 2(-20) + 3(-5) = -24 + 40 - 15 = 1 \\).
-   Cofacteurs (rapidement) : \\( C = \begin{pmatrix} -24 & 20 & -5 \\ -15 & -15 & 5 \\ -14 & -10 & 1 \end{pmatrix} \\) (je passe le calcul complet ici, mais tu peux vérifier).
-   \\( \adj(A) = C^T = \begin{pmatrix} -24 & -15 & -14 \\ 20 & -15 & -10 \\ -5 & 5 & 1 \end{pmatrix} \\).
-   \\( A^{-1} = \frac{1}{1} \adj(A) = \begin{pmatrix} -24 & -15 & -14 \\ 20 & -15 & -10 \\ -5 & 5 & 1 \end{pmatrix} \\).

Tu peux vérifier : \\( A \cdot A^{-1} = I \\) (la matrice identité).

### Pourquoi Cela Fonctionne-t-il ?
La raison principale est une propriété des déterminants et des cofacteurs : pour toute matrice carrée \\( A \\),
\\[
A \cdot \adj(A) = \det(A) \cdot I
\\]
(où \\( I \\) est la matrice identité). Cela découle du **développement de Laplace** du déterminant le long des lignes/colonnes. Chaque entrée dans \\( A \cdot \adj(A) \\) se développe en une somme qui est égale à \\( \det(A) \\) sur la diagonale et 0 ailleurs (car les termes hors diagonale s'annulent via les signes des cofacteurs).

Pour obtenir l'inverse, on divise les deux côtés par \\( \det(A) \\) (en supposant qu'il est non nul) :
\\[
A \cdot \left( \frac{1}{\det(A)} \adj(A) \right) = I \implies A^{-1} = \frac{1}{\det(A)} \adj(A)
\\]
De même, \\( \adj(A) \cdot A = \det(A) \cdot I \\), donc cela fonctionne des deux côtés.

Cette méthode se généralise à toute matrice \\( n \times n \\), mais pour une 3×3, elle est efficace. Pour des matrices plus grandes, l'élimination de Gauss est souvent plus rapide d'un point de vue computationnel.

Si tu as une matrice spécifique que tu aimerais que j'inverse ou si tu souhaites que je clarifie une étape, partage-la simplement !