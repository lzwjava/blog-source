---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de poche d'algèbre linéaire avec NumPy
translated: true
type: note
---

En tant que tuteur axé sur l'ingénierie, ce guide s'appuie sur les formulations explicites avec indices précédentes en intégrant des démonstrations pratiques NumPy via `import numpy as np` et `np.linalg`. Toutes les mathématiques restent vérifiables avec des indices (par ex., \\( A = [a_{ij}]_{i=1}^2, j=1^2 \\)) ; le code utilise des tableaux explicites pour plus de clarté. Les sorties proviennent d'exécutions vérifiées (par ex., pour \\( A = \begin{pmatrix} a_{11}=1 & a_{12}=2 \\ a_{21}=3 & a_{22}=4 \end{pmatrix} \\), \\( B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} \\)). Utilisez-les pour des calculs rapides lors de la préparation aux examens—concentrez-vous sur l'interprétation des sorties par rapport aux formules.

## 1. Opérations Matricielles
Les mathématiques comme avant : \\( (AB)_{ij} = \sum_{k=1}^2 a_{ik} b_{kj} \\), etc.

**Démo NumPy** :
```python
import numpy as np
A = np.array([[1, 2], [3, 4]], dtype=float)
B = np.array([[5, 6], [7, 8]], dtype=float)
```
- Addition : `A + B` donne \\( \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix} \\) (terme à terme \\( a_{ij} + b_{ij} \\)).
- Scalaire : `2 * A` donne \\( \begin{pmatrix} 2 & 4 \\ 6 & 8 \end{pmatrix} \\) (\\( c a_{ij} \\)).
- Multiplication : `A @ B` (ou `np.dot(A, B)`) donne \\( \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix} \\) (vérifiez : somme ligne1-col1 \\( 1\cdot5 + 2\cdot7 = 19 \\)). Notez la non-commutativité : `np.allclose(A @ B, B @ A)` est `False`.
- Transposée : `A.T` donne \\( \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} \\) (\\( (A^T)_{ij} = a_{ji} \\)).
- Inverse : `np.linalg.inv(A)` donne \\( \begin{pmatrix} -2 & 1 \\ 1.5 & -0.5 \end{pmatrix} \\) (vérifiez : `A @ inv_A` ≈ \\( I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \\), avec de petites erreurs de type float ~1e-16).

## 2. Déterminants
Maths : \\( \det A = \sum_{j=1}^2 a_{1j} C_{1j} \\), \\( C_{1j} = (-1)^{1+j} \det(M_{1j}) \\) (par ex., \\( M_{11} = [4] \\), donc \\( C_{11} = 4 \\) ; complet \\( \det A = 1\cdot4 - 2\cdot3 = -2 \\)).

**Démo NumPy** (suite de ci-dessus) :
- `np.linalg.det(A)` : -2.0 (correspond à la formule ; précision float -2.0000000000000004).
- Produit : `np.linalg.det(A @ B)` = 4.0 ; `det_A * np.linalg.det(B)` ≈ 4.0 (vérifie \\( \det(AB) = \det A \cdot \det B \\)).
- Transposée : `np.linalg.det(A.T)` = -2.0 (vérifie \\( \det(A^T) = \det A \\)).

Pour le lien adjointe/inverse : L'inverse utilise le det au dénominateur, comme dans la formule \\( A^{-1} = \frac{1}{\det A} \adj A \\).

## 3. Systèmes Linéaires & Élimination de Gauss
Maths : Augmenter \\( [A | b] \\) avec \\( b = [b_i]_{i=1}^2 = [5, 11]^T \\) ; résoudre via substitution arrière après REF.

**Démo NumPy** :
- `np.linalg.solve(A, b)` donne [1. 2.] (exact : \\( x_1 = \frac{\det A_1}{\det A} \\), où \\( A_1 \\) échange col1 avec b, det= -2 identique ; vérifie Cramer).
- Vérification : `A @ x` = [5. 11.] (résiduel 0).
- Rang : `np.linalg.matrix_rank(A)` = 2 (plein ; pour singulier, rang < 2 implique des solutions infinies/aucune).

Le `solve` de NumPy effectue une factorisation de type LU en interne (pas besoin de code Gaussien explicite ; pour du code personnalisé, utilisez `scipy.linalg.lu` mais restez sur np.linalg ici).

## 4. Espaces Vectoriels
Maths : rang A = # pivots = dim Col(A) ; nullité = 2 - rang A.

**Démo NumPy** :
- Rang comme ci-dessus : 2.
- Estimation de la nullité via SVD : `U, S, Vt = np.linalg.svd(A)` ; compter les valeurs singulières > 1e-10 : 2, donc nullité = 2 - 2 = 0 (Nul(A) = {0}). Pour la base, les vecteurs de l'espace nul proviennent des lignes de Vt avec un petit S.

## 5. Transformations Linéaires
Maths : T(x)_i = \\( \sum_j a_{ij} x_j \\) ; la représentation matricielle est A.

**Lien NumPy** : Identique aux opérations matricielles ; par ex., `T_x = A @ x` applique la transformation (vectorisée).

## 6. Valeurs Propres
Maths : Résoudre det(A - λ I) = 0, (A - λ I)_{ij} = a_{ij} - λ δ_{ij} ; puis (A - λ I) v = 0 pour v_j.

**Démo NumPy** :
- `eigvals, eigvecs = np.linalg.eig(A)` : eigvals ≈ [-0.372, 5.372] (racines de λ² - tr(A)λ + det A = λ² - 5λ -2 =0).
- Colonnes des vecteurs propres : par ex., col0 ≈ [-0.825, 0.566]^T pour λ≈-0.372.
- Vérification : `A @ eigvecs[:,0]` ≈ λ eigvecs[:,0] (vérification mise à l'échelle : `A @ eigvecs[:,0] / eigvals[0]` correspond à eigvecs[:,0]).

Pour diagonalisable : Matrice pleine rang des vecteurs propres (det ≠0).

## 7. Produits Scalaires & Orthogonalisation
Maths : <u,v> = \\( \sum_i u_i v_i \\) ; proj = (<v,w>/<w,w>) w (multiplication scalaire sur w_i).

**Démo NumPy** (u=[1,2], v=[3,4]) :
- `np.dot(u, v)` = 11 (ou `u @ v`).
- `np.linalg.norm(u)` ≈ 2.236 (√<u,u>).

Gram-Schmidt : Utiliser `np.linalg.qr(V)` pour la matrice V (colonnes comme vecteurs de base) ; Q = orthonormée.
- Exemple V = \\( \begin{pmatrix} 3 & 0 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix} \\) (cols v^{(1)}=[3,1,0]^T, etc.).
- `ortho = np.linalg.qr(V)[0]` donne ≈ \\( \begin{pmatrix} -0.949 & -0.316 & 0 \\ -0.316 & 0.949 & 0 \\ 0 & 0 & 1 \end{pmatrix} \\) (les changements de signe sont acceptables).
- Vérification : `np.allclose(ortho.T @ ortho, np.eye(3))` = True (δ_{ij}).

Forme Quadratique : `u @ A @ u` = 27.0 (x^T A x avec x_i = u_i ; pour défini positif, toutes les eigvals >0—ici signes mixtes).

**Astuce de Vérification Rapide** : Toujours utiliser `np.allclose` pour les floats ; réduire manuellement pour les petits n, puis comparer avec `solve` ou `eig`. Entraînez-vous : Remplacez par vos matrices 3×3.

[Documentation NumPy linalg](https://numpy.org/doc/stable/reference/routines.linalg.html)  
[Algèbre Linéaire dans NumPy - SciPy Lecture Notes](https://scipy-lectures.org/intro/numpy/auto_examples/plot_linear_algebra.html)