---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Référence Rapide pour l'Examen d'Algèbre Linéaire
translated: true
type: note
---

Aide-mémoire des concepts clés et formules. Se concentre sur les matrices, déterminants, systèmes linéaires, espaces vectoriels, transformations, valeurs propres et formes quadratiques — sujets principaux des examens précédents. Revoir les définitions, propriétés et calculs.

## 1. Matrices
- **Définition** : \\( A = [a_{ij}] \in \mathbb{R}^{m \times n} \\).
- **Opérations** :
  - Addition : \\( (A + B)_{ij} = a_{ij} + b_{ij} \\).
  - Scalaire : \\( (cA)_{ij} = c a_{ij} \\).
  - Multiplication : \\( (AB)_{ij} = \sum_k a_{ik} b_{kj} \\) (si tailles compatibles).
- **Transposée** : \\( (A^T)_{ij} = a_{ji} \\); \\( (AB)^T = B^T A^T \\), \\( (A^T)^T = A \\).
- **Inverse** (carrée) : \\( AA^{-1} = I \\); \\( (AB)^{-1} = B^{-1} A^{-1} \\); \\( (A^T)^{-1} = (A^{-1})^T \\).
- **Types** :
  - Diagonale : Non nulle uniquement sur la diagonale.
  - Triangulaire Supérieure/Inférieure : Zéros en dessous/au-dessus de la diagonale.
  - Symétrique : \\( A = A^T \\).
  - Orthogonale : \\( A^T A = I \\) (colonnes orthonormées).

## 2. Déterminants (det A)
- **Propriétés** :
  - \\( \det(AB) = \det A \cdot \det B \\); \\( \det(A^T) = \det A \\); \\( \det(cA) = c^n \det A \\).
  - Échange de ligne/colonne : Multiplie par -1.
  - Ajout d'un multiple d'une ligne/colonne : Pas de changement.
  - Mise à l'échelle d'une ligne/colonne par c : Multiplie par c.
  - \\( \det I = 1 \\); \\( \det A = 0 \\) si singulière (lignes/colonnes dépendantes).
- **Calcul** :
  - 2x2 : \\( \det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc \\).
  - Développement par cofacteurs (ligne i) : \\( \det A = \sum_j a_{ij} C_{ij} \\), où \\( C_{ij} = (-1)^{i+j} M_{ij} \\) (déterminant mineur).
  - Triangulaire : Produit des éléments diagonaux.
- **Adjointe/Inverse** : \\( A^{-1} = \frac{1}{\det A} \adj A \\), où \\( \adj A = C^T \\) (transposée des cofacteurs).
- **Règle de Cramer** (pour \\( Ax = b \\), det A ≠ 0) : \\( x_i = \frac{\det A_i}{\det A} \\) (A_i remplace la i-ème colonne par b).

## 3. Systèmes Linéaires (Ax = b)
- **Élimination de Gauss** : Réduction de lignes de [A | b] vers REF/RREF.
  - REF : Pivots (1 principaux) en escalier vers le bas-droite ; zéros sous les pivots.
  - Rétro-substitution pour solution unique.
- **Solutions** :
  - Unique : rang A = n (plein rang colonne), noyau {0}.
  - Infinie : rang A = rang [A|b] < n (variables libres).
  - Aucune : rang A < rang [A|b].
- **Solution Complète** : Solution particulière + base du noyau (solutions homogènes).
- **Décomposition LU** (sans pivot) : A = LU (L triangulaire inférieure unitaire, U triangulaire supérieure) ; résoudre Ly = b, Ux = y.
- **Moindres Carrés** (sur-déterminé) : \\( \hat{x} = (A^T A)^{-1} A^T b \\) (si plein rang).

## 4. Espaces Vectoriels & Sous-espaces
- **Espace Vectoriel** : Fermé par addition/multiplication scalaire ; axiomes (ex : vecteur 0, inverses).
- **Sous-espaces** : Étendue de vecteurs ; fermé, contient 0.
  - Espace Colonne : Col(A) = Vect(colonnes de A) ; dim = rang A.
  - Espace Ligne : Row(A) = Col(A^T) ; dim = rang A.
  - Noyau : Nul(A) = {x | Ax = 0} ; dim = n - rang A.
  - Noyau Gauche : Nul(A^T).
- **Indépendance Linéaire** : c1 v1 + ... + ck vk = 0 ⇒ tous ci = 0.
- **Base** : Ensemble générateur linéairement indépendant.
- **Dimension** : # vecteurs dans une base ; dim Col(A) + dim Nul(A) = n (théorème du rang).
- **Rang** : # colonnes pivots = dim Col(A) = dim Row(A).

## 5. Transformations Linéaires
- **Définition** : T: V → W linéaire si T(u + v) = T u + T v, T(cu) = c T u.
- **Rep. Matricielle** : [T] relativement aux bases = A où T(x) = A x (base standard).
- **Noyau** : Ker T = Nul(A) ; Image : Im T = Col(A).
- **Isomorphisme** : Bijectif (matrice inversible).
- **Théorème du Rang** : dim Ker T + dim Im T = dim V.

## 6. Valeurs Propres & Vecteurs Propres
- **Définition** : A v = λ v (v ≠ 0 vecteur propre, λ valeur propre).
- **Éq. Caractéristique** : det(A - λ I) = 0 ; racines λi (multiplicité algébrique).
- **Vecteurs Propres** : Résoudre (A - λ I) v = 0 ; multiplicité géom. = dim espace propre.
- **Diagonalisable** : n vecteurs propres lin. indép. ⇒ A = X Λ X^{-1} (Λ diag(λi), X = [v1 ... vn]).
  - A Symétrique : Toujours diagonalisable ; vecteurs propres orthogonaux (A = Q Λ Q^T, Q orthogonale).
- **Trace** : tr A = ∑ λi.
- **Dét** : det A = ∏ λi.
- **Matrices Semblables** : A ~ B si A = P B P^{-1} ; mêmes valeurs propres, trace, dét.

## 7. Produits Scalaires & Formes Quadratiques
- **Produit Scalaire** : <u, v> = u^T v (Euclidien) ; ||v|| = √<v,v>.
- **Orthogonal** : <u,v> = 0 ; Base orthonormée : <ei, ej> = δij.
- **Gram-Schmidt** : Orthogonaliser la base {v1,...,vn} → {u1,...,un}.
  - u1 = v1 ; uk = vk - proj_{Vect(u1..u_{k-1})} vk ; proj_w v = (<v,w>/<w,w>) w.
- **Forme Quadratique** : q(x) = x^T A x (A symétrique).
  - Définie Positive : q(x) > 0 pour x ≠ 0 (tous λi > 0).
  - Diagonaliser : q(x) = ∑ λi yi^2 (y = Q^T x).

## Conseils Rapides
- Calculer le rang : Réduire les lignes pour trouver le # de pivots.
- Vérifier diagonalisable : Mult. géom. = mult. alg. pour chaque λ.
- Pour les examens : S'entraîner à la réduction de lignes, développement du dét, problèmes de valeurs propres sur matrices 2x2/3x3.
- Erreurs Courantes : Oublier la multiplicité ; signe dans les cofacteurs ; multiplication non commutative.

Bonne chance pour demain — concentrez-vous sur la compréhension plutôt que sur la mémorisation !

[Linear Algebra Cheat Sheet - Laurent Lessard](https://laurentlessard.com/teaching/ece532/cheat_sheet.pdf)  
[Linear Algebra Review - Yiping Lu](https://2prime.github.io/files/linear/finalsheet.pdf)  
[2023 Self-Exam Linear Algebra Questions](https://doc.quark.cn/preview/jiaoyukaoshi-shijuan-gaokao/1130FC966EE595249D3822AFF5DF0167)