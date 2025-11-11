---
audio: false
generated: true
lang: fr
layout: post
title: Questions d'algèbre linéaire
translated: true
type: note
---

**18. Soit les matrices X et A qui satisfont la relation XA = X + A. Si $A = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix}$, trouver la matrice X.**

**Réponse :**
Nous avons l'équation $XA = X + A$.
Nous pouvons la réécrire comme $XA - X = A$, donc $X(A - I) = A$.
Si $(A - I)$ est inversible, alors $X = A(A - I)^{-1}$.

Calculons d'abord $A - I$ :

$A - I = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\\ 0 & 1 & 0 \\\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\\ 2 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$.

Ensuite, trouvons l'inverse de $(A - I)$. Soit $B = A - I$.
Le déterminant de B est $\det(B) = 0(0 - 0) - (-3)(2 - 0) + 0(0 - 0) = 6$.
Puisque $\det(B) \neq 0$, B est inversible.

La matrice adjointe de B est :
$adj(B) = \begin{pmatrix} C_{11} & C_{21} & C_{31} \\\ C_{12} & C_{22} & C_{32} \\\ C_{13} & C_{23} & C_{33} \end{pmatrix}$
$C_{11} = \begin{vmatrix} 0 & 0 \\\ 0 & 1 \end{vmatrix} = 0$
$C_{12} = -\begin{vmatrix} 2 & 0 \\\ 0 & 1 \end{vmatrix} = -2$
$C_{13} = \begin{vmatrix} 2 & 0 \\\ 0 & 0 \end{vmatrix} = 0$
$C_{21} = -\begin{vmatrix} -3 & 0 \\\ 0 & 1 \end{vmatrix} = 3$
$C_{22} = \begin{vmatrix} 0 & 0 \\\ 0 & 1 \end{vmatrix} = 0$
$C_{23} = -\begin{vmatrix} 0 & -3 \\\ 0 & 0 \end{vmatrix} = 0$
$C_{31} = \begin{vmatrix} -3 & 0 \\\ 0 & 0 \end{vmatrix} = 0$
$C_{32} = -\begin{vmatrix} 0 & 0 \\\ 2 & 0 \end{vmatrix} = 0$
$C_{33} = \begin{vmatrix} 0 & -3 \\\ 2 & 0 \end{vmatrix} = 6$

La matrice des cofacteurs est $C = \begin{pmatrix} 0 & -2 & 0 \\\ 3 & 0 & 0 \\\ 0 & 0 & 6 \end{pmatrix}$.
La matrice adjointe est $adj(B) = C^T = \begin{pmatrix} 0 & 3 & 0 \\\ -2 & 0 & 0 \\\ 0 & 0 & 6 \end{pmatrix}$.

Alors, $(A - I)^{-1} = \frac{1}{\det(B)} adj(B) = \frac{1}{6} \begin{pmatrix} 0 & 3 & 0 \\\ -2 & 0 & 0 \\\ 0 & 0 & 6 \end{pmatrix} = \begin{pmatrix} 0 & 1/2 & 0 \\\ -1/3 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$.

Maintenant, calculons $X = A(A - I)^{-1}$ :
$X = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix} \begin{pmatrix} 0 & 1/2 & 0 \\\ -1/3 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$
$X = \begin{pmatrix} (1)(0) + (-3)(-1/3) + (0)(0) & (1)(1/2) + (-3)(0) + (0)(0) & (1)(0) + (-3)(0) + (0)(1) \\\ (2)(0) + (1)(-1/3) + (0)(0) & (2)(1/2) + (1)(0) + (0)(0) & (2)(0) + (1)(0) + (0)(1) \\\ (0)(0) + (0)(-1/3) + (2)(0) & (0)(1/2) + (0)(0) + (2)(0) & (0)(0) + (0)(0) + (2)(1) \end{pmatrix}$
$X = \begin{pmatrix} 0+1+0 & 1/2+0+0 & 0+0+0 \\\ 0-1/3+0 & 1+0+0 & 0+0+0 \\\ 0+0+0 & 0+0+0 & 0+0+2 \end{pmatrix}$
$X = \begin{pmatrix} 1 & 1/2 & 0 \\\ -1/3 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix}$.

**19. Déterminer la valeur de k pour laquelle les vecteurs $\alpha_1 = (1, 1, k)^T$, $\alpha_2 = (1, k, 1)^T$, $\alpha_3 = (k, 1, 1)^T$ sont linéairement dépendants. Trouver un ensemble maximal de vecteurs linéairement indépendants et exprimer le(s) vecteur(s) restant(s) comme une combinaison linéaire de cet ensemble.**

**Réponse :**
Les vecteurs $\alpha_1, \alpha_2, \alpha_3$ sont linéairement dépendants si le déterminant de la matrice formée par ces vecteurs est nul.
Soit $A = \begin{pmatrix} 1 & 1 & k \\\ 1 & k & 1 \\\ k & 1 & 1 \end{pmatrix}$.
$\det(A) = 1(k - 1) - 1(1 - k) + k(1 - k^2)$
$= k - 1 - 1 + k + k - k^3$
$= -k^3 + 3k - 2$.
Nous devons trouver $k$ tel que $-k^3 + 3k - 2 = 0$, ou $k^3 - 3k + 2 = 0$.
Nous pouvons tester les racines entières qui sont des diviseurs de 2 (c'est-à-dire $\pm 1, \pm 2$).
Si $k=1$, $1^3 - 3(1) + 2 = 1 - 3 + 2 = 0$. Donc, $(k-1)$ est un facteur.
Si $k=-2$, $(-2)^3 - 3(-2) + 2 = -8 + 6 + 2 = 0$. Donc, $(k+2)$ est un facteur.
En utilisant la division polynomiale ou la division synthétique pour $(k^3 - 3k + 2) / (k-1)$ :
$(k-1)(k^2+k-2) = 0$
$(k-1)(k+2)(k-1) = 0$
Donc, les racines sont $k=1$ (racine double) et $k=-2$.
Les vecteurs sont linéairement dépendants si $k=1$ ou $k=-2$.

Cas 1 : $k=1$
$\alpha_1 = (1, 1, 1)^T$, $\alpha_2 = (1, 1, 1)^T$, $\alpha_3 = (1, 1, 1)^T$.
Dans ce cas, les trois vecteurs sont identiques.
Un ensemble maximal de vecteurs linéairement indépendants peut être $\{\alpha_1\}$.
Alors $\alpha_2 = 1 \cdot \alpha_1$ et $\alpha_3 = 1 \cdot \alpha_1$.

Cas 2 : $k=-2$
$\alpha_1 = (1, 1, -2)^T$, $\alpha_2 = (1, -2, 1)^T$, $\alpha_3 = (-2, 1, 1)^T$.
Vérifions si $\alpha_1$ et $\alpha_2$ sont linéairement indépendants. Ils ne sont pas des multiples scalaires l'un de l'autre, donc ils sont linéairement indépendants. Ainsi, un ensemble maximal de vecteurs linéairement indépendants peut être $\{\alpha_1, \alpha_2\}$.
Nous voulons exprimer $\alpha_3$ comme une combinaison linéaire de $\alpha_1$ et $\alpha_2$ :
$\alpha_3 = c_1 \alpha_1 + c_2 \alpha_2$
$(-2, 1, 1)^T = c_1 (1, 1, -2)^T + c_2 (1, -2, 1)^T$
Cela donne le système d'équations :
1) $c_1 + c_2 = -2$
2) $c_1 - 2c_2 = 1$
3) $-2c_1 + c_2 = 1$
Soustraire (2) de (1) : $(c_1 + c_2) - (c_1 - 2c_2) = -2 - 1 \Rightarrow 3c_2 = -3 \Rightarrow c_2 = -1$.
Substituer $c_2 = -1$ dans (1) : $c_1 - 1 = -2 \Rightarrow c_1 = -1$.
Vérifier avec (3) : $-2(-1) + (-1) = 2 - 1 = 1$. C'est cohérent.
Donc, $\alpha_3 = -1 \cdot \alpha_1 - 1 \cdot \alpha_2$.

**20. Résoudre le système d'équations linéaires { $x_1 - x_2 - 3x_4 = -2$ ; $x_1 + 2x_3 - 2x_4 = -1$ ; $2x_1 - 2x_2 + x_3 - 6x_4 = -5$ ; $-x_1 + 2x_2 + 3x_3 + 4x_4 = 2$ } (Trouver une solution particulière et la base fondamentale de solutions pour le système homogène correspondant).**

**Réponse :**
La matrice augmentée est :
$\begin{pmatrix} 1 & -1 & 0 & -3 & | & -2 \\\ 1 & 0 & 2 & -2 & | & -1 \\\ 2 & -2 & 1 & -6 & | & -5 \\\ -1 & 2 & 3 & 4 & | & 2 \end{pmatrix}$

$R_2 \leftarrow R_2 - R_1$
$R_3 \leftarrow R_3 - 2R_1$
$R_4 \leftarrow R_4 + R_1$
$\begin{pmatrix} 1 & -1 & 0 & -3 & | & -2 \\\ 0 & 1 & 2 & 1 & | & 1 \\\ 0 & 0 & 1 & 0 & | & -1 \\\ 0 & 1 & 3 & 1 & | & 0 \end{pmatrix}$

$R_1 \leftarrow R_1 + R_2$
$R_4 \leftarrow R_4 - R_2$
$\begin{pmatrix} 1 & 0 & 2 & -2 & | & -1 \\\ 0 & 1 & 2 & 1 & | & 1 \\\ 0 & 0 & 1 & 0 & | & -1 \\\ 0 & 0 & 1 & 0 & | & -1 \end{pmatrix}$

$R_1 \leftarrow R_1 - 2R_3$
$R_2 \leftarrow R_2 - 2R_3$
$R_4 \leftarrow R_4 - R_3$
$\begin{pmatrix} 1 & 0 & 0 & -2 & | & 1 \\\ 0 & 1 & 0 & 1 & | & 3 \\\ 0 & 0 & 1 & 0 & | & -1 \\\ 0 & 0 & 0 & 0 & | & 0 \end{pmatrix}$

Le système est équivalent à :
$x_1 - 2x_4 = 1 \Rightarrow x_1 = 1 + 2x_4$
$x_2 + x_4 = 3 \Rightarrow x_2 = 3 - x_4$
$x_3 = -1$
Soit $x_4 = t$ (variable libre).
La solution générale est :
$x_1 = 1 + 2t$
$x_2 = 3 - t$
$x_3 = -1$
$x_4 = t$
Sous forme vectorielle : $X = \begin{pmatrix} 1 \\\ 3 \\\ -1 \\\ 0 \end{pmatrix} + t \begin{pmatrix} 2 \\\ -1 \\\ 0 \\\ 1 \end{pmatrix}$.

Une solution particulière est obtenue en posant $t=0$ : $X_p = \begin{pmatrix} 1 \\\ 3 \\\ -1 \\\ 0 \end{pmatrix}$.

Le système homogène correspondant a pour solution $X_h = t \begin{pmatrix} 2 \\\ -1 \\\ 0 \\\ 1 \end{pmatrix}$.
La base fondamentale de solutions pour le système homogène est $\{\begin{pmatrix} 2 \\\ -1 \\\ 0 \\\ 1 \end{pmatrix}\}$.

**21. Soit la matrice A = \begin{pmatrix} x & 0 & y \\\ 0 & 2 & 0 \\\ y & 0 & -2 \end{pmatrix} qui a une valeur propre de -3, et |A| = -12. Trouver les valeurs de x et y.**

**Réponse :**
L'équation caractéristique est $\det(A - \lambda I) = 0$.
$A - \lambda I = \begin{pmatrix} x-\lambda & 0 & y \\\ 0 & 2-\lambda & 0 \\\ y & 0 & -2-\lambda \end{pmatrix}$.
$\det(A - \lambda I) = (x-\lambda)[(2-\lambda)(-2-\lambda) - 0] - 0 + y[0 - y(2-\lambda)]$
$= (x-\lambda)(2-\lambda)(-2-\lambda) - y^2(2-\lambda)$
$= (2-\lambda)[(x-\lambda)(-2-\lambda) - y^2]$
$= (2-\lambda)[-2x - x\lambda + 2\lambda + \lambda^2 - y^2] = 0$.
Les valeurs propres sont $\lambda_1 = 2$, et les racines de $\lambda^2 + (2-x)\lambda - (2x+y^2) = 0$.
On nous donne qu'une valeur propre est -3.
Si $2 = -3$, c'est faux. Donc, -3 doit être une racine de $\lambda^2 + (2-x)\lambda - (2x+y^2) = 0$.
Substituer $\lambda = -3$ :
$(-3)^2 + (2-x)(-3) - (2x+y^2) = 0$
$9 - 6 + 3x - 2x - y^2 = 0$
$3 + x - y^2 = 0 \Rightarrow x - y^2 = -3$ (Équation 1)

On nous donne aussi que $\det(A) = -12$.
$\det(A) = x(2(-2) - 0) - 0 + y(0 - 2y)$
$= -4x - 2y^2 = -12$
Diviser par -2 : $2x + y^2 = 6$ (Équation 2)

Maintenant nous avons un système de deux équations avec x et y :
1) $x - y^2 = -3$
2) $2x + y^2 = 6$
Ajouter l'Équation 1 et l'Équation 2 :
$(x - y^2) + (2x + y^2) = -3 + 6$
$3x = 3 \Rightarrow x = 1$.
Substituer $x=1$ dans l'Équation 1 :
$1 - y^2 = -3$
$-y^2 = -4$
$y^2 = 4 \Rightarrow y = \pm 2$.

Donc les valeurs sont $x=1$ et $y=2$, ou $x=1$ et $y=-2$.

Vérifions les valeurs propres pour les deux cas.
Le polynôme caractéristique se factorise comme $(2-\lambda)[\lambda^2 + (2-x)\lambda - (2x+y^2)] = 0$.
Si $x=1, y=2$ :
$(2-\lambda)[\lambda^2 + (2-1)\lambda - (2(1)+2^2)] = 0$
$(2-\lambda)[\lambda^2 + \lambda - (2+4)] = 0$
$(2-\lambda)(\lambda^2 + \lambda - 6) = 0$
$(2-\lambda)(\lambda+3)(\lambda-2) = 0$.
Les valeurs propres sont $\lambda = 2, -3, 2$. Ceci est cohérent avec une valeur propre étant -3.

Si $x=1, y=-2$ :
$(2-\lambda)[\lambda^2 + (2-1)\lambda - (2(1)+(-2)^2)] = 0$
$(2-\lambda)[\lambda^2 + \lambda - (2+4)] = 0$
$(2-\lambda)(\lambda^2 + \lambda - 6) = 0$
$(2-\lambda)(\lambda+3)(\lambda-2) = 0$.
Les valeurs propres sont $\lambda = 2, -3, 2$. Ceci est également cohérent.

Les deux paires $(x,y) = (1,2)$ et $(x,y) = (1,-2)$ satisfont les conditions.

**22. Soit la forme quadratique à 3 variables $f(x_1, x_2, x_3) = t(x_1^2 + x_2^2 + x_3^2) + 2x_1x_2 + 2x_1x_3 - 2x_2x_3$. Déterminer pour quelle(s) valeur(s) de t cette forme quadratique est définie positive.**

**Réponse :**
La matrice de la forme quadratique A est :
$A = \begin{pmatrix} t & 1 & 1 \\\ 1 & t & -1 \\\ 1 & -1 & t \end{pmatrix}$.
Pour que la forme quadratique soit définie positive, tous les mineurs principaux dominants de A doivent être positifs.

1. Le premier mineur principal dominant est $M_1 = t$.
Pour la définition positive, $t > 0$.

2. Le deuxième mineur principal dominant est $M_2 = \det \begin{pmatrix} t & 1 \\\ 1 & t \end{pmatrix} = t^2 - 1$.
Pour la définition positive, $t^2 - 1 > 0 \Rightarrow t^2 > 1$.
Puisque nous avons déjà $t > 0$, cela implique $t > 1$.

3. Le troisième mineur principal dominant est $M_3 = \det(A)$.
$M_3 = t(t^2 - 1) - 1(t - (-1)) + 1(-1 - t)$
$= t(t^2 - 1) - (t + 1) - (1 + t)$
$= t^3 - t - t - 1 - 1 - t$
$= t^3 - 3t - 2$.
Pour la définition positive, $t^3 - 3t - 2 > 0$.

Nous savons d'après la question 19 que $k^3 - 3k - 2 = (k+1)^2(k-2)$. (Ici $k$ est $t$)
Donc, $t^3 - 3t - 2 = (t+1)^2(t-2)$.
Nous avons besoin de $(t+1)^2(t-2) > 0$.
Puisque $(t+1)^2 \ge 0$, et pour qu'il ne soit pas nul, $t \neq -1$.
Donc nous avons besoin de $t-2 > 0$, ce qui signifie $t > 2$.

En combinant les conditions :
1) $t > 0$
2) $t > 1$
3) $t > 2$

L'intersection de ces conditions est $t > 2$.
Par conséquent, la forme quadratique est définie positive lorsque $t > 2$.