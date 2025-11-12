---
audio: false
generated: true
lang: fr
layout: post
title: Sous-espace
translated: true
type: note
---

Pour déterminer lequel des ensembles donnés est un sous-espace vectoriel de $\mathbb{R}^2$, nous devons vérifier s'ils satisfont aux trois conditions pour être un sous-espace :

1.  **Le vecteur nul est dans le sous-espace.**
2.  **Le sous-espace est fermé pour l'addition vectorielle.** Si $\mathbf{u}$ et $\mathbf{v}$ sont dans le sous-espace, alors $\mathbf{u} + \mathbf{v}$ est aussi dans le sous-espace.
3.  **Le sous-espace est fermé pour la multiplication par un scalaire.** Si $\mathbf{u}$ est dans le sous-espace et $c$ est un scalaire quelconque, alors $c\mathbf{u}$ est aussi dans le sous-espace.

Examinons chaque option :

**a) La droite y = x + 1**

1.  **Vecteur nul :** Le vecteur nul dans $\mathbb{R}^2$ est $\begin{pmatrix} 0 \\ 0 \end{pmatrix}$. Pour que ce vecteur soit sur la droite, il doit satisfaire l'équation $y = x + 1$. En substituant $x=0$ et $y=0$, on obtient $0 = 0 + 1$, c'est-à-dire $0 = 1$. C'est faux, donc le vecteur nul n'est pas sur la droite $y = x + 1$.

Puisque la première condition n'est pas satisfaite, la droite $y = x + 1$ n'est pas un sous-espace vectoriel de $\mathbb{R}^2$.

**b) La droite y = 2x**

1.  **Vecteur nul :** Pour que le vecteur nul $\begin{pmatrix} 0 \\ 0 \end{pmatrix}$ soit sur la droite, il doit satisfaire l'équation $y = 2x$. En substituant $x=0$ et $y=0$, on obtient $0 = 2(0)$, c'est-à-dire $0 = 0$. C'est vrai, donc le vecteur nul est sur la droite $y = 2x$.

2.  **Clôture pour l'addition vectorielle :** Soient $\mathbf{u} = \begin{pmatrix} x_1 \\ y_1 \end{pmatrix}$ et $\mathbf{v} = \begin{pmatrix} x_2 \\ y_2 \end{pmatrix}$ deux vecteurs sur la droite $y = 2x$. Cela signifie que $y_1 = 2x_1$ et $y_2 = 2x_2$.
    Leur somme est $\mathbf{u} + \mathbf{v} = \begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}$. Nous devons vérifier si ce vecteur se trouve sur la droite $y = 2x$. En substituant les composantes, on obtient $y_1 + y_2 = 2(x_1 + x_2)$. Puisque $y_1 = 2x_1$ et $y_2 = 2x_2$, on a $2x_1 + 2x_2 = 2x_1 + 2x_2$, ce qui est vrai. Ainsi, la droite est fermée pour l'addition vectorielle.

3.  **Clôture pour la multiplication par un scalaire :** Soit $\mathbf{u} = \begin{pmatrix} x \\ y \end{pmatrix}$ un vecteur sur la droite $y = 2x$, donc $y = 2x$. Soit $c$ un scalaire quelconque. Alors $c\mathbf{u} = \begin{pmatrix} cx \\ cy \end{pmatrix}$. Nous devons vérifier si ce vecteur se trouve sur la droite $y = 2x$. En substituant les composantes, on obtient $cy = 2(cx)$. Puisque $y = 2x$, on a $c(2x) = 2(cx)$, c'est-à-dire $2cx = 2cx$. C'est vrai, donc la droite est fermée pour la multiplication par un scalaire.

Puisque les trois conditions sont satisfaites, la droite $y = 2x$ est un sous-espace vectoriel de $\mathbb{R}^2$.

**c) Le cercle unité**

Le cercle unité dans $\mathbb{R}^2$ est défini par l'équation $x^2 + y^2 = 1$.

1.  **Vecteur nul :** Le vecteur nul est $\begin{pmatrix} 0 \\ 0 \end{pmatrix}$. En substituant dans l'équation, on obtient $0^2 + 0^2 = 1$, c'est-à-dire $0 = 1$. C'est faux, donc le vecteur nul n'est pas sur le cercle unité.

Puisque la première condition n'est pas satisfaite, le cercle unité n'est pas un sous-espace vectoriel de $\mathbb{R}^2$.

Réponse finale : La réponse finale est $\boxed{La droite y = 2x}$

---

L'exigence selon laquelle "Le vecteur nul est dans le sous-espace" est l'une des **trois conditions fondamentales** qu'un sous-ensemble d'un espace vectoriel doit satisfaire pour être considéré comme un **sous-espace vectoriel**. Décomposons *pourquoi* cette condition est nécessaire.

Le concept de sous-espace vectoriel consiste à identifier des ensembles plus petits à l'intérieur d'un espace vectoriel plus grand qui se comportent eux-mêmes comme des espaces vectoriels. Pour se comporter comme un espace vectoriel, ces ensembles plus petits doivent hériter de certaines propriétés essentielles. L'une des propriétés les plus fondamentales de tout espace vectoriel est l'existence d'un **vecteur nul** (souvent noté $\mathbf{0}$). Ce vecteur a la propriété cruciale que, lorsqu'il est ajouté à tout autre vecteur de l'espace, il laisse ce vecteur inchangé : $\mathbf{v} + \mathbf{0} = \mathbf{v}$ pour tous les vecteurs $\mathbf{v}$ de l'espace.

Voici pourquoi le vecteur nul doit être dans un sous-espace vectoriel :

1.  **Héritage de la structure d'espace vectoriel :** Un sous-espace vectoriel est destiné à être un "mini-espace vectoriel" à l'intérieur d'un plus grand. Si un sous-ensemble ne contient pas le vecteur nul, il manque un élément crucial nécessaire pour satisfaire les axiomes d'espace vectoriel. Sans vecteur nul, le concept d'inverse additif (un autre axiome important) devient problématique.

2.  **Clôture pour la multiplication par un scalaire :** Considérons un sous-ensemble non vide $W$ d'un espace vectoriel $V$ qui est fermé pour la multiplication par un scalaire. Si $\mathbf{w}$ est un vecteur quelconque dans $W$, et que $W$ est un sous-espace vectoriel, alors pour tout scalaire $c$, le vecteur $c\mathbf{w}$ doit aussi être dans $W$. Si nous choisissons le scalaire $c = 0$, alors $0\mathbf{w} = \mathbf{0}$ (c'est une propriété des espaces vectoriels). Par conséquent, si un sous-espace vectoriel est fermé pour la multiplication par un scalaire et contient au moins un vecteur, il *doit* contenir le vecteur nul.

3.  **Garantie des inverses additifs :** Bien que la présence du vecteur nul seul ne garantisse pas l'existence d'inverses additifs dans le sous-espace, son absence crée un problème fondamental. Si un vecteur $\mathbf{v}$ est dans le sous-espace, et que le sous-espace est fermé pour la multiplication par un scalaire, alors $(-1)\mathbf{v} = -\mathbf{v}$ doit aussi être dans le sous-espace (c'est l'inverse additif de $\mathbf{v}$). Pour que l'addition de $\mathbf{v}$ et $-\mathbf{v}$ donne un vecteur *à l'intérieur* du sous-espace, le vecteur résultant doit être le vecteur nul. Si le vecteur nul n'est pas dans le sous-ensemble, alors la clôture pour l'addition pourrait être violée même si les inverses additifs existent dans l'espace vectoriel plus grand.

En termes plus simples, si un sous-ensemble ne contient même pas "l'élément neutre" pour l'addition vectorielle (qui est le vecteur nul), il ne peut pas vraiment fonctionner comme un système autonome sous l'addition vectorielle et la multiplication par un scalaire, qui sont les opérations définissant un espace vectoriel.

Par conséquent, la condition selon laquelle le vecteur nul doit être dans le sous-espace vectoriel n'est pas arbitraire ; c'est une conséquence directe de l'exigence qu'un sous-espace vectoriel doit hériter de la structure algébrique essentielle de l'espace vectoriel plus grand dans lequel il réside.