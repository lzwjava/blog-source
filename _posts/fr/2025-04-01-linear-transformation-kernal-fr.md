---
audio: false
generated: true
lang: fr
layout: post
title: Noyau d'une application linéaire
translated: true
type: note
---

Le **noyau** d'une transformation linéaire est l'ensemble de tous les vecteurs d'entrée que la transformation envoie sur le vecteur nul.

### Définition :
Si \\( T: V \to W \\) est une transformation linéaire entre deux espaces vectoriels \\( V \\) et \\( W \\), alors le **noyau** (ou **espace nul**) de \\( T \\) est :

\\[
\ker(T) = \{ v \in V \mid T(v) = 0 \}
\\]

### Propriétés clés :
1. **Sous-espace** : Le noyau d'une transformation linéaire est toujours un sous-espace du domaine \\( V \\).
2. **Dimension** : La dimension du noyau est appelée la **nullité** de la transformation.
3. **Relation avec l'injectivité** :
   - Si \\( \ker(T) = \{0\} \\), alors \\( T \\) est **injective** (ou univoque).
   - Si \\( \ker(T) \\) a une dimension supérieure à zéro, alors \\( T \\) n'est pas injective.

### Exemple :
Considérons la transformation matricielle \\( T: \mathbb{R}^3 \to \mathbb{R}^2 \\) donnée par :

\\[
T(x, y, z) = (x + y, y + z)
\\]

En l'écrivant sous forme matricielle :

<div>
$$
T \begin{bmatrix} x \\ y \\ z \end{bmatrix} =
\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix}
$$
</div>

Pour trouver le noyau, résolvez :

\\[
\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
\\]

Cela donne le système :

\\[
x + y = 0
\\]
\\[
y + z = 0
\\]

En résolvant pour \\( x, y, z \\) :

\\[
x = -y, \quad z = -y
\\]

Ainsi, le noyau est constitué de tous les vecteurs de la forme :

<div>
$$
\ker(T) = \text{span} \left\{ \begin{bmatrix} -1 \\ 1 \\ -1 \end{bmatrix} \right\}
$$
</div>

ce qui est un sous-espace de dimension un de \\( \mathbb{R}^3 \\).

N'hésitez pas à me demander si vous avez besoin de plus de précisions !