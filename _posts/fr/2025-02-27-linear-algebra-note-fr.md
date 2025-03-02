---
audio: false
generated: false
lang: fr
layout: post
title: Algèbre Linéaire Note
translated: true
---

Décortiquons davantage avec un exemple concret pour aider à clarifier le concept de la forme canonique d'une forme quadratique.

### Exemple

Considérons la forme quadratique en deux variables \[x\] et \[y\]:

\[ Q(x, y) = 2x^2 + 4xy + 3y^2 \]

#### Transformation Étape par Étape en Forme Canonique

1. **Représentation Matricielle :**
   - Écrivez la forme quadratique sous forme d'équation matricielle. La matrice \[A\] associée à cette forme quadratique est :

   \[
   A = \begin{pmatrix}
   2 & 2 \\
   2 & 3
   \end{pmatrix}
   \]

   Notez que les éléments hors diagonale sont la moitié du coefficient du terme \[xy\].

2. **Trouver les Valeurs Propres et les Vecteurs Propres :**
   - Calculez les valeurs propres de \[A\] en résolvant l'équation caractéristique \[\det(A - \lambda I) = 0\].
   - Pour chaque valeur propre, trouvez le vecteur propre correspondant.

3. **Diagonalisation :**
   - Construisez une matrice \[P\] dont les colonnes sont les vecteurs propres de \[A\].
   - Calculez \[D = P^TAP\], qui sera une matrice diagonale avec les valeurs propres de \[A\] sur la diagonale.

4. **Changement de Variables :**
   - Définissez de nouvelles variables \[u\] et \[v\] telles que :

   \[
   \begin{pmatrix}
   x \\
   y
   \end{pmatrix} = P \begin{pmatrix}
   u \\
   v
   \end{pmatrix}
   \]

   - Substituez ces nouvelles variables dans la forme quadratique originale pour obtenir une nouvelle forme en termes de \[u\] et \[v\].

5. **Forme Canonique :**
   - La forme quadratique résultante sera sous forme canonique, qui est une somme de carrés :

   \[
   Q(u, v) = \lambda_1 u^2 + \lambda_2 v^2
   \]

   où \[\lambda_1\] et \[\lambda_2\] sont les valeurs propres de \[A\].

### Interprétation

- La forme canonique révèle la nature géométrique de la forme quadratique.
- Si les deux valeurs propres sont positives, la forme est définie positive.
- Si elles sont toutes négatives, elle est définie négative.
- Si elles ont des signes différents, la forme est indéfinie.

Ce processus simplifie la forme quadratique et la rend plus facile à analyser.

---

Dans le contexte des formes quadratiques, le terme "二次型的规范形" se traduit par "forme canonique d'une forme quadratique" en anglais. Comprendre ce concept implique de reconnaître comment une forme quadratique peut être simplifiée ou transformée en une forme standard par des techniques d'algèbre linéaire.

### Formes Quadratiques
Une forme quadratique est un polynôme homogène de degré deux en plusieurs variables. Par exemple, en deux variables \[x\] et \[y\], une forme quadratique pourrait ressembler à :

\[ Q(x, y) = ax^2 + bxy + cy^2 \]

### Forme Canonique
La forme canonique d'une forme quadratique est une version simplifiée qui révèle des propriétés essentielles, telles que le rang et la signature (le nombre de valeurs propres positives, négatives et nulles). Pour obtenir cette forme, nous effectuons généralement un changement de variables, souvent par diagonalisation ou d'autres transformations orthogonales.

#### Étapes pour Trouver la Forme Canonique :
1. **Représentation Matricielle :** Représentez la forme quadratique sous forme de matrice symétrique \[A\]. Pour l'exemple ci-dessus, la matrice serait :
   \[
   A = \begin{pmatrix}
   a & \frac{b}{2} \\
   \frac{b}{2} & c
   \end{pmatrix}
   \]

2. **Diagonalisation :** Trouvez une matrice orthogonale \[P\] telle que \[P^TAP\] soit une matrice diagonale \[D\]. Ce processus implique de trouver les valeurs propres et les vecteurs propres de \[A\].

3. **Changement de Variables :** Utilisez la matrice \[P\] pour changer de variables, transformant la forme quadratique originale en une somme de carrés, chacun correspondant à une valeur propre.

4. **Forme Canonique :** La matrice diagonale résultante \[D\] représente la forme canonique de la forme quadratique, où chaque entrée diagonale est une valeur propre de \[A\].

La forme canonique aide à analyser les propriétés de la forme quadratique, telles que déterminer si elle est définie positive, définie négative ou indéfinie, ce qui est crucial en optimisation et autres applications mathématiques.

---

La **forme normale d'une forme quadratique** fait référence à la représentation simplifiée standard d'une forme quadratique après avoir appliqué un changement de variables approprié. Cette transformation rend la structure de la forme quadratique plus claire et plus facile à analyser.

---

### **1. Définition d'une Forme Quadratique**
Une **forme quadratique** en \[ n \] variables est une fonction de la forme :

\[
Q(x) = x^T A x
\]

où :
- \[ x = (x_1, x_2, \dots, x_n)^T \] est un vecteur colonne de dimension \[ n \],
- \[ A \] est une matrice symétrique de dimension \[ n \times n \].

L'objectif est de transformer cette forme quadratique en une forme plus simple et standardisée.

---

### **2. Trouver la Forme Normale**
Pour simplifier la forme quadratique, nous utilisons un changement de variables orthogonal :

1. **Trouver les Valeurs Propres et les Vecteurs Propres de \[ A \] :**
   - Calculez les valeurs propres \[ \lambda_1, \lambda_2, \dots, \lambda_n \].
   - Trouvez une base orthonormale de vecteurs propres.

2. **Diagonalisation de \[ A \] :**
   - Puisque \[ A \] est symétrique, il peut être diagonalisé sous la forme \[ A = P D P^T \], où :
     - \[ P \] est une matrice orthogonale (dont les colonnes sont les vecteurs propres de \[ A \]).
     - \[ D \] est une matrice diagonale avec les valeurs propres \[ \lambda_1, \lambda_2, \dots, \lambda_n \] sur la diagonale.

3. **Changement de Variables :**
   - Définissez une nouvelle variable \[ y = P^T x \], alors :

     \[
     Q(x) = x^T A x = (P y)^T A (P y) = y^T (P^T A P) y = y^T D y
     \]

   - Puisque \[ D \] est diagonale, la forme quadratique se simplifie en :

     \[
     Q(y) = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \dots + \lambda_n y_n^2
     \]

   Ceci est la **forme normale de la forme quadratique**.

---

### **3. Interprétation de la Forme Normale**
- La forme normale exprime la forme quadratique comme une somme de termes carrés, pondérés par les valeurs propres.
- Les **signes des valeurs propres** déterminent la nature de la forme quadratique :
  - Si toutes les valeurs propres sont positives, la forme est **définie positive**.
  - Si elles sont toutes négatives, elle est **définie négative**.
  - Si les signes sont mélangés, elle est **indéfinie**.

Ce processus est essentiel dans les **sections coniques, l'optimisation et les équations différentielles**, car il aide à classifier les surfaces et fonctions quadratiques.

Souhaitez-vous un exemple plus détaillé ?