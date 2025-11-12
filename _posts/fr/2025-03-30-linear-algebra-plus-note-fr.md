---
audio: false
generated: true
lang: fr
layout: post
title: Algèbre Linéaire Note Plus
translated: true
type: note
---

En algèbre linéaire, deux matrices carrées \\( A \\) et \\( B \\) sont dites semblables s'il existe une matrice inversible \\( P \\) telle que :

\\[ B = P^{-1}AP \\]

Cette relation est connue sous le nom de transformation de similarité. La matrice \\( P \\) est appelée la matrice de changement de base, et elle transforme la matrice \\( A \\) en la matrice \\( B \\).

### Propriétés Clés des Matrices Semblables :
1. **Mêmes Valeurs Propres** : Les matrices semblables ont les mêmes valeurs propres. En effet, les valeurs propres sont préservées par les transformations de similarité.
2. **Même Déterminant** : Le déterminant des matrices semblables est le même car \\(\det(P^{-1}AP) = \det(A)\\).
3. **Même Trace** : La trace (somme des éléments diagonaux) des matrices semblables est la même car \\(\text{tr}(P^{-1}AP) = \text{tr}(A)\\).
4. **Même Rang** : Les matrices semblables ont le même rang.
5. **Même Polynôme Caractéristique** : Les matrices semblables partagent le même polynôme caractéristique.

### Intuition :
Les matrices semblables représentent la même transformation linéaire mais dans des bases différentes. La matrice \\( P \\) peut être vue comme un changement de coordonnées, transformant la base dans laquelle la transformation linéaire est représentée.

### Exemple :
Considérons deux matrices \\( A \\) et \\( B \\) :

\\[ A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}, \quad B = \begin{pmatrix} 3 & 0 \\ 2 & 1 \end{pmatrix} \\]

Pour vérifier si elles sont semblables, nous devons trouver une matrice inversible \\( P \\) telle que \\( B = P^{-1}AP \\).

Souhaitez-vous voir un exemple de la manière de trouver une telle matrice \\( P \\) pour des matrices spécifiques \\( A \\) et \\( B \\) ?

---

Oui, la matrice :

\\[
A = \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\\]

a effectivement une Décomposition en Valeurs Singulières (SVD). Suivons le processus pour trouver la SVD de cette matrice.

### Étape 1 : Calculer \\( A^T A \\)

Premièrement, nous calculons la matrice \\( A^T A \\) :

\\[
A^T = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}
\\]

Maintenant, multiplions \\( A^T \\) et \\( A \\) :

\\[
A^T A = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = \begin{bmatrix} 1 + 9 & 2 + 12 \\ 2 + 12 & 4 + 16 \end{bmatrix} = \begin{bmatrix} 10 & 14 \\ 14 & 20 \end{bmatrix}
\\]

### Étape 2 : Valeurs Propres et Vecteurs Propres de \\( A^T A \\)

Pour trouver les valeurs singulières, nous avons besoin des valeurs propres de \\( A^T A \\). Nous résolvons l'équation caractéristique \\( \text{det}(A^T A - \lambda I) = 0 \\) :

\\[
\text{det}\begin{bmatrix} 10 - \lambda & 14 \\ 14 & 20 - \lambda \end{bmatrix} = 0
\\]

Ce qui donne :

\\[
(10 - \lambda)(20 - \lambda) - 14 \times 14 = 0
\\]

\\[
\lambda^2 - 30\lambda + 100 - 196 = 0
\\]

\\[
\lambda^2 - 30\lambda - 96 = 0
\\]

En résolvant cette équation quadratique :

\\[
\lambda = \frac{-(-30) \pm \sqrt{(-30)^2 - 4(1)(-96)}}{2(1)} = \frac{30 \pm \sqrt{900 + 384}}{2} = \frac{30 \pm \sqrt{1284}}{2}
\\]

\\[
\lambda = \frac{30 \pm 35.86}{2}
\\]

Ainsi, les valeurs propres sont :

\\[
\lambda_1 \approx 32.93 \quad \text{et} \quad \lambda_2 \approx 0.93
\\]

### Étape 3 : Calculer les Valeurs Singulières

Les valeurs singulières sont les racines carrées des valeurs propres de \\( A^T A \\). Par conséquent, nous avons :

\\[
\sigma_1 = \sqrt{32.93} \approx 5.73 \quad \text{et} \quad \sigma_2 = \sqrt{0.93} \approx 0.96
\\]

### Étape 4 : Calculer les Matrices \\( U \\) et \\( V \\)

Pour trouver les matrices \\( U \\) et \\( V \\), nous devons calculer les vecteurs propres de \\( A^T A \\) et \\( A A^T \\), mais comme cela nécessite des étapes détaillées qui vont au-delà du calcul de base, on les résout typiquement numériquement.

Cependant, sur la base des valeurs propres ci-dessus, nous savons que les valeurs singulières sont \\( 5.73 \\) et \\( 0.96 \\), et \\( U \\) et \\( V \\) seraient des matrices orthogonales correspondant aux vecteurs propres de \\( A A^T \\) et \\( A^T A \\).

Ainsi, la SVD de la matrice \\( A \\) est :

\\[
A = U \Sigma V^T
\\]

Où :

- \\( \Sigma = \begin{bmatrix} 5.73 & 0 \\ 0 & 0.96 \end{bmatrix} \\)
- \\( U \\) et \\( V \\) sont des matrices orthogonales correspondant aux vecteurs propres de \\( A A^T \\) et \\( A^T A \\).

Vous pouvez trouver les valeurs exactes pour \\( U \\) et \\( V \\) en résolvant les problèmes aux valeurs propres pour \\( A^T A \\) et \\( A A^T \\).

---

L'énoncé décrit le comportement de la matrice en tant que transformation linéaire. Décomposons-le pour comprendre pourquoi cela se produit :

### Matrice comme Transformation Linéaire :
- **Espace d'Entrée** : La matrice opère sur des vecteurs d'un espace à 3 dimensions (puisqu'elle a 3 colonnes). Cela signifie qu'elle prend des vecteurs à 3 composantes en entrée.
- **Espace de Sortie** : La matrice transforme ces vecteurs en un espace à 2 dimensions (puisqu'elle a 2 lignes). Cela signifie qu'elle produit des vecteurs à 2 composantes en sortie.

### Noyau :
- **Définition** : Le noyau (ou espace nul) d'une matrice est constitué de tous les vecteurs qui, multipliés par la matrice, donnent le vecteur zéro.
- **Dimension** : La nullité de la matrice est la dimension de ce noyau. Dans ce cas, la nullité est 1, ce qui signifie qu'il existe un sous-espace vectoriel de dimension 1 des vecteurs qui sont transformés en zéro.
- **Interprétation** : Ce sous-espace de dimension 1 représente une ligne (dans l'espace d'entrée à 3 dimensions) de vecteurs qui sont "écrasés" ou "réduits" au vecteur zéro dans l'espace de sortie à 2 dimensions.

### Pourquoi Cela Se Produit :
- **Théorème du Rang** : Le théorème stipule que pour toute matrice \\(m \times n\\), le rang (dimension de l'espace des colonnes) plus la nullité (dimension du noyau) est égal au nombre de colonnes \\(n\\). Ici, le rang est 2 et le nombre de colonnes est 3, donc la nullité doit être 1.
- **Dépendance Linéaire** : L'existence d'un noyau de dimension 1 indique qu'il y a une redondance ou une dépendance linéaire parmi les colonnes de la matrice. Cela signifie que l'une des colonnes peut être exprimée comme une combinaison linéaire des deux autres.

### Visualisation :
- Imaginez un espace 3D où tous les points sur une ligne spécifique (le noyau) sont transformés en l'origine dans un espace 2D. Cette ligne représente les vecteurs qui sont "perdus" ou "ignorés" par la transformation linéaire définie par la matrice.

Ce comportement est un aspect fondamental des transformations linéaires et met en lumière comment les matrices peuvent réduire la dimensionnalité de l'espace sur lequel elles agissent.

---

Pour déterminer quelle option est nécessaire pour qu'une matrice soit diagonalisable, je vais examiner chaque énoncé.

Une matrice carrée A est diagonalisable si et seulement s'il existe une matrice inversible P telle que P⁻¹AP est une matrice diagonale. Cela se produit précisément lorsque A possède un ensemble complet de vecteurs propres linéairement indépendants.

Analysons chaque option :

a) La matrice doit avoir au moins une valeur propre.
Bien que toutes les matrices n×n aient au moins une valeur propre (dans le corps complexe), cela seul ne garantit pas la diagonalisabilité. Une matrice pourrait avoir des valeurs propres mais ne pas être diagonalisable si elle n'a pas assez de vecteurs propres linéairement indépendants.

b) La matrice doit avoir des valeurs propres distinctes.
Avoir des valeurs propres distinctes est suffisant mais pas nécessaire pour la diagonalisabilité. Une matrice avec des valeurs propres répétées peut toujours être diagonalisable si elle a suffisamment de vecteurs propres linéairement indépendants associés à ces valeurs propres répétées.

c) La matrice doit avoir suffisamment de vecteurs propres linéairement indépendants.
C'est exactement la condition nécessaire et suffisante pour la diagonalisabilité. Spécifiquement, une matrice n×n est diagonalisable si et seulement si elle possède n vecteurs propres linéairement indépendants, formant une base pour l'espace vectoriel.

Par conséquent, l'option c) est la bonne réponse : une matrice est diagonalisable si et seulement si elle a suffisamment de vecteurs propres linéairement indépendants.