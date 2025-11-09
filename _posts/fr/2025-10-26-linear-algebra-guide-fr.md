---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de poche d'algèbre linéaire précis
translated: true
type: note
---

En tant que tuteur axé sur l'ingénierie, ce guide met l'accent sur des calculs vérifiables et explicites par indice pour les matrices \\( A = [a_{ij}]_{i=1}^m, j=1^n \in \mathbb{R}^{m \times n} \\) (lignes indexées par \\( i \\), colonnes par \\( j \\), base 1). Toutes les étapes sont montrées avec des indices pour plus de clarté ; les exemples annotent les entrées en ligne. Révision via la réduction de lignes et la résolution de valeurs propres sur des cas 2×2/3×3.

## 1. Opérations Matricielles
- **Addition** : \\( (A + B)_{ij} = a_{ij} + b_{ij} \\) pour tous \\( i,j \\).
- **Multiplication par un Scalaire** : \\( (cA)_{ij} = c a_{ij} \\) pour un scalaire \\( c \\), tous \\( i,j \\).
- **Multiplication Matricielle** (si \\( m \times p \\) et \\( p \times n \\)) : \\( (AB)_{ij} = \sum_{k=1}^p a_{ik} b_{kj} \\) pour tous \\( i=1^m \\), \\( j=1^n \\).
- **Transposée** : \\( (A^T)_{ij} = a_{ji} \\); ainsi \\( (AB)^T_{ij} = \sum_k b_{ki} a_{kj} = (B^T A^T)_{ij} \\).
- **Inverse** (pour une matrice carrée \\( n \times n \\), \\( \det A \neq 0 \\)) : \\( A^{-1} \\) satisfait \\( \sum_k a_{ik} (A^{-1})_{kj} = \delta_{ij} \\) (delta de Kronecker : 1 si \\( i=j \\), 0 sinon). Propriétés : \\( (AB)^{-1}_{ij} = \sum_k (B^{-1})_{ik} (A^{-1})_{kj} = (B^{-1} A^{-1})_{ij} \\); \\( (A^T)^{-1}_{ij} = \sum_k (A^{-1})_{ki} (A^T)_{kj} ? Attendez, non : (A^{-1})^T_{ij} = (A^{-1})_{ji} \\), donc \\( [(A^T)^{-1}]_{ij} = (A^{-1})_{ji} \\).

**Exemple (Annotation de l'Inverse 2×2)** : Soit \\( A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \\). Alors \\( A^{-1} = \frac{1}{\det A} \begin{pmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{pmatrix} \\), où \\( \det A = a_{11} a_{22} - a_{12} a_{21} \\).

## 2. Déterminants
- **Définition** : Pour une matrice carrée \\( A \\), \\( \det A \\) via le développement par cofacteurs le long de la ligne \\( i \\) : \\( \det A = \sum_{j=1}^n a_{ij} C_{ij} \\), où le mineur \\( M_{ij} \\) est la sous-matrice obtenue en supprimant la ligne \\( i \\) et la colonne \\( j \\) (donc \\( M_{ij} = [m_{pq}] \\) avec \\( p=1^{n-1} \setminus i \\), \\( q=1^{n-1} \setminus j \\), renuméroté en base 1), le cofacteur \\( C_{ij} = (-1)^{i+j} \det(M_{ij}) \\).
- **Propriétés** :
  - \\( \det(AB) = \det A \cdot \det B \\); \\( \det(A^T) = \det A \\) (car le développement est symétrique).
  - \\( \det(cA) = c^n \det A \\).
  - Échange de lignes : \\( \det \\) multiplié par -1 ; ajout d'un multiple de la ligne \\( k \\) à la ligne \\( i \neq k \\) : inchangé ; mise à l'échelle de la ligne \\( i \\) par \\( c \\) : multiplié par \\( c \\).
  - \\( \det I = 1 \\) (1 sur la diagonale) ; singulier si \\( \det A = 0 \\) (rang < n).
- **Adjointe** : \\( \adj(A)_{ij} = C_{ji} = [C^T]_{ij} \\), où \\( C = [C_{pq}] \\). Inverse : \\( A^{-1} = \frac{1}{\det A} \adj A \\), donc \\( (A^{-1})_{ij} = \frac{1}{\det A} \sum_k \delta_{ik} C_{kj} ? Non : la forme matricielle vérifie \\( A \adj A = (\det A) I \\).

**Exemple (Cofacteurs 2×2)** : Pour la matrice \\( A \\) ci-dessus, \\( M_{11} = [a_{22}] \\), \\( C_{11} = (-1)^{1+1} a_{22} = a_{22} \\); \\( M_{12} = [a_{21}] \\), \\( C_{12} = (-1)^{1+2} a_{21} = -a_{21} \\); de même \\( C_{21} = -a_{12} \\), \\( C_{22} = a_{11} \\). Ainsi \\( \adj A = \begin{pmatrix} C_{11} & C_{21} \\ C_{12} & C_{22} \end{pmatrix} = \begin{pmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{pmatrix} \\).

- **Règle de Cramer** (pour \\( \sum_j a_{ij} x_j = b_i \\), \\( i=1^n \\), \\( \det A \neq 0 \\)) : \\( x_r = \frac{\det A_r}{\det A} \\), où \\( A_r \\) remplace la colonne \\( r \\) de \\( A \\) par \\( [b_i]_{i=1}^n \\), donc \\( (A_r)_{ij} = a_{ij} \\) si \\( j \neq r \\), sinon \\( b_i \\).

## 3. Systèmes Linéaires & Élimination de Gauss
- **Matrice Augmentée** : \\( [A | b] = [a_{ij} | b_i] \\) pour \\( i=1^m \\), \\( j=1^n \\).
- **Réduction de Lignes vers REF** : Appliquer les opérations élémentaires (échanger les lignes \\( p \leftrightarrow q \\) ; mettre à l'échelle la ligne \\( p \\) par \\( c \neq 0 \\) : ligne \\( p \leftarrow c \\) ligne \\( p \\) ; ajouter \\( c \\) ligne \\( q \\) à la ligne \\( p \\)) pour obtenir la forme échelonnée en lignes : entrée principale (pivot) dans la ligne \\( i \\) à la colonne \\( p_i \geq p_{i-1} \\), zéros en dessous des pivots.
- **Vers RREF** : Continuer pour obtenir des zéros au-dessus des pivots, mettre les pivots à l'échelle 1.
- **Rang** : Nombre de lignes non nulles dans REF (ou pivots).
- **Solutions** :
  - Unique si rang \\( A = n \\), rang \\( [A|b] = n \\) (nullité 0).
  - Infinie si rang \\( A = \\) rang \\( [A|b] = r < n \\) (n-r variables libres).
  - Incompatible si rang \\( A < \\) rang \\( [A|b] \\).
- **Solution Générale** : \\( x = x_p + x_h \\), solution particulière \\( x_p \\) de RREF, solution homogène \\( x_h \\) engendre l'espace nul (base des variables libres).
- **Exemple d'Étape (Annotation du Système 2×2)** : Résoudre \\( a_{11} x_1 + a_{12} x_2 = b_1 \\), \\( a_{21} x_1 + a_{22} x_2 = b_2 \\). Ligne2 ← Ligne2 - (a_{21}/a_{11}) Ligne1 : nouvelle ligne2 = [0, a_{22} - (a_{21} a_{12}/a_{11}), b_2 - (a_{21} b_1 / a_{11}) ]. Remontée : \\( x_2 = \\) ... / terme det, etc.

## 4. Espaces Vectoriels
- **Sous-espaces** : Col(A) = Vect{ col j de A, j=1^n } = { \\( \sum_j x_j \\) col j | x } ; dim = rang A.
- **Espace des Lignes** : Row(A) = Col(A^T); dim = rang A.
- **Espace Nul** : Nul(A) = { x | \\( \sum_j a_{ij} x_j = 0 \\) ∀ i } ; base à partir des colonnes libres de RREF.
- **Théorème du Rang** : rang A + dim Nul(A) = n.

## 5. Transformations Linéaires
- **Représentation Matricielle** : T(x)_i = \\( \sum_j a_{ij} x_j \\).
- **Noyau** : Ker T = Nul(A); Im T = Col(A).

## 6. Valeurs Propres
- **Polynôme Caractéristique** : det(A - λ I) = 0, où (A - λ I)_{ij} = a_{ij} - λ δ_{ij}.
- **Vecteurs Propres** : Pour λ, résoudre \\( \sum_j (a_{ij} - λ δ_{ij}) v_j = 0 \\), v = [v_j] ≠ 0.
- **Diagonalisable** : Si mult alg(λ_k) = mult géo(λ_k) ∀ k (dimension complète de l'espace propre), alors A = P D P^{-1}, D_{ij} = λ_i δ_{ij}, colonnes de P = vecteurs propres.
- **Symétrique** : A = A^T ⇒ diagonalisation orthogonale : A = Q D Q^T, Q^T Q = I.

## 7. Produits Scalaires & Orthogonalisation
- **Euclidien** : <u,v> = \\( \sum_i u_i v_i = u^T v \\).
- **Étape de Gram-Schmidt** : Pour une base {v^{(k)}}, u^{(1)} = v^{(1)}; u^{(k)} = v^{(k)} - \sum_{m=1}^{k-1} \proj_{u^{(m)}} v^{(k)}, où \proj_w v = \frac{<v,w>}{<w,w>} w (composante \\( \sum_i ... \\)).

**Astuce de Vérification Rapide** : Toujours réduire [A - λI | 0] pour les espaces propres ; vérifier det via le développement si n≤3.

[Linear Algebra Cheat Sheet - Indexed Formulas](https://laurentlessard.com/teaching/ece532/cheat_sheet.pdf)  
[Self-Exam 02198 Review](https://doc.quark.cn/preview/jiaoyukaoshi-shijuan-gaokao/1130FC966EE595249D3822AFF5DF0167)