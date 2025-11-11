---
audio: false
generated: true
lang: fr
layout: post
title: Transformations linéaires - Gemini
translated: true
type: note
---

D'accord, approfondissons un tutoriel détaillé sur les transformations linéaires, couvrant la définition, les exemples, la représentation matricielle, le noyau, l'image et les propriétés comme l'injectivité et la surjectivité. C'est un sujet fondamental en algèbre linéaire.

## 6. Transformations Linéaires : Un Tutoriel Détaillé

Une **transformation linéaire** est une fonction entre deux espaces vectoriels qui préserve les opérations d'addition vectorielle et de multiplication scalaire. Soient \\(V\\) et \\(W\\) des espaces vectoriels sur le même corps \\(F\\) (qui est souvent l'ensemble des nombres réels \\(\mathbb{R}\\) ou des nombres complexes \\(\mathbb{C}\\)).

**Définition :** Une fonction \\(T: V \rightarrow W\\) est une transformation linéaire si elle satisfait les deux propriétés suivantes pour tous les vecteurs \\(\mathbf{u}, \mathbf{v} \in V\\) et tous les scalaires \\(c \in F\\) :

1.  **Additivité :** \\(T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})\\)
2.  **Homogénéité (Multiplication Scalaire) :** \\(T(c\mathbf{u}) = cT(\mathbf{u})\\)

Ces deux propriétés peuvent être combinées en une seule condition :
\\(T(c\mathbf{u} + d\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v})\\) pour tous \\(\mathbf{u}, \mathbf{v} \in V\\) et tous les scalaires \\(c, d \in F\\).

**Conséquences Clés de la Linéarité :**

* \\(T(\mathbf{0}_V) = \mathbf{0}_W\\), où \\(\mathbf{0}_V\\) est le vecteur nul dans \\(V\\) et \\(\mathbf{0}_W\\) est le vecteur nul dans \\(W\\). (Preuve : \\(T(\mathbf{0}_V) = T(0\mathbf{u}) = 0T(\mathbf{u}) = \mathbf{0}_W\\) pour tout \\(\mathbf{u} \in V\\)).
* \\(T(-\mathbf{u}) = -T(\mathbf{u})\\). (Preuve : \\(T(-\mathbf{u}) = T((-1)\mathbf{u}) = (-1)T(\mathbf{u}) = -T(\mathbf{u})\\)).

### Exemples de Transformations Linéaires

Examinons quelques exemples pour mieux comprendre le concept.

**Exemple 1 : Transformation dans \\(\mathbb{R}^2\\) (Rotation)**

Considérons une transformation \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) qui fait tourner chaque vecteur dans \\(\mathbb{R}^2\\) dans le sens antihoraire d'un angle \\(\theta\\). Si \\(\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}\\), alors \\(T(\mathbf{v}) = \begin{pmatrix} x\cos\theta - y\sin\theta \\ x\sin\theta + y\cos\theta \end{pmatrix}\\).

Vérifions si c'est une transformation linéaire. Soient \\(\mathbf{u} = \begin{pmatrix} x_1 \\ y_1 \end{pmatrix}\\) et \\(\mathbf{v} = \begin{pmatrix} x_2 \\ y_2 \end{pmatrix}\\), et soit \\(c\\) un scalaire.

* **Additivité :**
    \\(T(\mathbf{u} + \mathbf{v}) = T\left(\begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}\right) = \begin{pmatrix} (x_1 + x_2)\cos\theta - (y_1 + y_2)\sin\theta \\ (x_1 + x_2)\sin\theta + (y_1 + y_2)\cos\theta \end{pmatrix}\\)
    \\(= \begin{pmatrix} (x_1\cos\theta - y_1\sin\theta) + (x_2\cos\theta - y_2\sin\theta) \\ (x_1\sin\theta + y_1\cos\theta) + (x_2