---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Définition et propriétés du polynôme caractéristique
translated: true
type: note
---

En algèbre linéaire, le **polynôme caractéristique** d'une matrice carrée \\( A \\) (de taille \\( n \times n \\)) est un polynôme qui encode des informations sur les valeurs propres de la matrice. Il est défini par :

\\[
p(\lambda) = \det(A - \lambda I)
\\]

où :
- \\( A \\) est la matrice \\( n \times n \\).
- \\( \lambda \\) est un scalaire (la variable du polynôme).
- \\( I \\) est la matrice identité \\( n \times n \\).
- \\( \det \\) désigne le déterminant.

### Caractéristiques principales
1. **Forme** : Le polynôme caractéristique est un polynôme unitaire de degré \\( n \\), ce qui signifie que son coefficient dominant (pour le terme \\( \lambda^n \\)) est 1.
   - Pour une matrice \\( 2 \times 2 \\) \\( A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \\), le polynôme caractéristique est :
     \\[
     p(\lambda) = \det \begin{bmatrix} a - \lambda & b \\ c & d - \lambda \end{bmatrix} = \lambda^2 - (a + d)\lambda + (ad - bc)
     \\]
     où \\( a + d \\) est la trace et \\( ad - bc \\) est le déterminant.

2. **Valeurs propres** : Les racines du polynôme caractéristique \\( p(\lambda) = 0 \\) sont les valeurs propres de la matrice \\( A \\). Elles peuvent être des nombres réels ou complexes.

3. **Coefficients** : Les coefficients du polynôme sont liés aux propriétés de la matrice :
   - Le coefficient de \\( \lambda^{n-1} \\) est \\( -\text{trace}(A) \\).
   - Le terme constant est \\( (-1)^n \det(A) \\).
   - Les autres coefficients sont déterminés par les sommes des mineurs principaux de \\( A \\).

4. **Invariance** : Le polynôme caractéristique est invariant sous les transformations de similarité. Si \\( B = P^{-1}AP \\), alors \\( A \\) et \\( B \\) ont le même polynôme caractéristique.

5. **Théorème de Cayley-Hamilton** : La matrice \\( A \\) satisfait son propre polynôme caractéristique, c'est-à-dire que si \\( p(\lambda) \\) est le polynôme caractéristique, alors \\( p(A) = 0 \\) (la matrice nulle).

### Exemple
Pour une matrice \\( A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \\) :
- Calculez \\( A - \lambda I = \begin{bmatrix} 1 - \lambda & 2 \\ 3 & 4 - \lambda \end{bmatrix} \\).
- Le polynôme caractéristique est :
  \\[
  p(\lambda) = \det \begin{bmatrix} 1 - \lambda & 2 \\ 3 & 4 - \lambda \end{bmatrix} = (1 - \lambda)(4 - \lambda) - (2)(3) = \lambda^2 - 5\lambda + 4 - 6 = \lambda^2 - 5\lambda - 2
  \\]
- Les valeurs propres sont trouvées en résolvant \\( \lambda^2 - 5\lambda - 2 = 0 \\).

### Applications
- **Calcul des valeurs propres** : Résoudre \\( p(\lambda) = 0 \\) donne les valeurs propres.
- **Propriétés des matrices** : Aide à déterminer la diagonalisabilité, l'inversibilité et d'autres propriétés.
- **Équations différentielles** : Utilisé dans les systèmes d'équations différentielles linéaires pour trouver des solutions.

Si vous avez besoin d'un exemple spécifique ou de plus de détails, faites-le-moi savoir !