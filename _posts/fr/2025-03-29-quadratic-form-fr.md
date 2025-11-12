---
audio: false
generated: true
lang: fr
layout: post
title: Forme quadratique
translated: true
type: note
---

En algèbre linéaire, une **forme quadratique** est une fonction $Q: \mathbb{R}^n \rightarrow \mathbb{R}$ qui peut s'exprimer comme :

$Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$

où :
* $\mathbf{x}$ est un vecteur colonne dans $\mathbb{R}^n$ :
    $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}$
* $A$ est une matrice symétrique $n \times n$ à coefficients réels. Cette matrice est appelée la **matrice de la forme quadratique**.
* $\mathbf{x}^T$ est la transposée de $\mathbf{x}$, qui est un vecteur ligne.

**En termes plus simples :**

Une forme quadratique est un polynôme homogène de degré deux en $n$ variables. "Homogène" signifie que chaque terme du polynôme a un degré total de deux.

Par exemple, en deux variables ($n=2$), une forme quadratique ressemble à :
$Q(x_1, x_2) = a x_1^2 + b x_1 x_2 + c x_2^2$

Ceci peut s'écrire sous forme matricielle comme :
$Q(x_1, x_2) = \begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} a & b/2 \\ b/2 & c \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$

Notez que les éléments hors diagonale de la matrice $A$ sont la moitié du coefficient du terme croisé ($x_1 x_2$). Nous utilisons une matrice symétrique $A$ car pour toute matrice $B$, $\mathbf{x}^T B \mathbf{x} = \mathbf{x}^T \left( \frac{B + B^T}{2} \right) \mathbf{x}$, et $\frac{B + B^T}{2}$ est toujours une matrice symétrique. L'utilisation de la forme symétrique simplifie de nombreuses propriétés et théorèmes liés aux formes quadratiques.

**Aspects clés des formes quadratiques :**

* **Représentation matricielle :** Toute forme quadratique peut être représentée de manière unique par une matrice symétrique.
* **Évaluation :** La valeur de la forme quadratique $Q(\mathbf{x})$ est un scalaire obtenu par la multiplication matricielle $\mathbf{x}^T A \mathbf{x}$.
* **Classification :** Les formes quadratiques peuvent être classées en fonction des valeurs qu'elles prennent pour les vecteurs non nuls $\mathbf{x}$ :
    * **Définie positive :** $Q(\mathbf{x}) > 0$ pour tout $\mathbf{x} \neq \mathbf{0}$. Ceci se produit si et seulement si toutes les valeurs propres de $A$ sont positives.
    * **Semi-définie positive :** $Q(\mathbf{x}) \ge 0$ pour tout $\mathbf{x}$. Ceci se produit si et seulement si toutes les valeurs propres de $A$ sont non négatives.
    * **Définie négative :** $Q(\mathbf{x}) < 0$ pour tout $\mathbf{x} \neq \mathbf{0}$. Ceci se produit si et seulement si toutes les valeurs propres de $A$ sont négatives.
    * **Semi-définie négative :** $Q(\mathbf{x}) \le 0$ pour tout $\mathbf{x}$. Ceci se produit si et seulement si toutes les valeurs propres de $A$ sont non positives.
    * **Indéfinie :** $Q(\mathbf{x})$ prend à la fois des valeurs positives et négatives. Ceci se produit si et seulement si $A$ a à la fois des valeurs propres positives et négatives.
* **Changement de variables :** En effectuant un changement de variables linéaire $\mathbf{x} = P\mathbf{y}$, où $P$ est une matrice inversible, la forme quadratique peut être transformée en une nouvelle forme quadratique en termes de $\mathbf{y}$ avec une représentation matricielle différente ($P^T A P$). Un objectif clé est souvent de trouver une transformation orthogonale (où $P$ est une matrice orthogonale) qui diagonalise la matrice $A$, résultant en une forme quadratique sans termes croisés (uniquement des termes carrés). Ceci est lié au théorème des axes principaux.

**Applications des formes quadratiques :**

Les formes quadratiques apparaissent dans divers domaines des mathématiques, de la physique, des statistiques et de l'ingénierie, notamment :

* **Sections coniques et surfaces quadriques :** Les équations de ces objets géométriques peuvent être exprimées à l'aide de formes quadratiques.
* **Optimisation :** Déterminer la nature des points critiques des fonctions multivariables implique souvent l'analyse de la forme quadratique de la matrice hessienne.
* **Analyse de stabilité :** Dans les systèmes dynamiques, les formes quadratiques (comme les fonctions de Lyapunov) sont utilisées pour analyser la stabilité des points d'équilibre.
* **Statistiques :** Les matrices de covariance définissent des formes quadratiques qui décrivent la dispersion et la corrélation des données.
* **Mécanique et physique :** L'énergie cinétique et potentielle dans certains systèmes peut être exprimée sous forme de formes quadratiques.

En résumé, une forme quadratique est un concept fondamental en algèbre linéaire qui fournit un moyen d'exprimer et d'analyser des polynômes quadratiques homogènes en utilisant le langage des vecteurs et des matrices. Sa représentation matricielle et sa classification basée sur la définition sont cruciales pour comprendre ses propriétés et ses applications.