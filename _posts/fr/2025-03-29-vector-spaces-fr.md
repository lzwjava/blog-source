---
audio: false
generated: true
lang: fr
layout: post
title: Tutoriel sur les espaces vectoriels en algèbre linéaire
translated: true
type: note
---

Ce tutoriel couvre les concepts clés liés aux **espaces vectoriels**, y compris les **sous-espaces, la base, la dimension et l'indépendance linéaire**. Ces sujets sont fondamentaux en algèbre linéaire et sont essentiels pour comprendre des concepts plus avancés.

---

### **1. Espaces Vectoriels**
Un **espace vectoriel** (ou espace linéaire) est un ensemble de vecteurs qui satisfait certaines propriétés sous l'addition vectorielle et la multiplication scalaire.

#### **Définition**
Un espace vectoriel \\( V \\) sur un corps \\( \mathbb{F} \\) (par exemple, les nombres réels \\( \mathbb{R} \\) ou les nombres complexes \\( \mathbb{C} \\)) est un ensemble d'éléments (vecteurs) avec deux opérations :
- **Addition Vectorielle :** \\( \mathbf{u} + \mathbf{v} \\) pour \\( \mathbf{u}, \mathbf{v} \in V \\).
- **Multiplication Scalaire :** \\( c \mathbf{v} \\) pour \\( c \in \mathbb{F} \\) et \\( \mathbf{v} \in V \\).

Ces opérations doivent satisfaire les **axiomes** suivants :
1. **Associativité de l'Addition :** \\( (\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w}) \\).
2. **Commutativité de l'Addition :** \\( \mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u} \\).
3. **Existence du Vecteur Zéro :** Il existe un vecteur \\( \mathbf{0} \\) tel que \\( \mathbf{v} + \mathbf{0} = \mathbf{v} \\) pour tout \\( \mathbf{v} \\).
4. **Existence des Inverses Additifs :** Pour tout \\( \mathbf{v} \\), il existe \\( -\mathbf{v} \\) tel que \\( \mathbf{v} + (-\mathbf{v}) = \mathbf{0} \\).
5. **Distributivité de la Multiplication Scalaire sur l'Addition Vectorielle :** \\( c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v} \\).
6. **Distributivité de la Multiplication Scalaire sur l'Addition du Corps :** \\( (a + b) \mathbf{v} = a\mathbf{v} + b\mathbf{v} \\).
7. **Associativité de la Multiplication Scalaire :** \\( a(b\mathbf{v}) = (ab)\mathbf{v} \\).
8. **Identité Multiplicative :** \\( 1 \mathbf{v} = \mathbf{v} \\).

#### **Exemples d'Espaces Vectoriels**
1. \\( \mathbb{R}^n \\) (espace euclidien à n dimensions)
2. L'espace des polynômes de degré \\( \leq n \\).
3. L'ensemble des matrices \\( m \times n \\).
4. L'ensemble des fonctions continues.

---

### **2. Sous-espaces**
Un **sous-espace** est un sous-ensemble \\( W \\) d'un espace vectoriel \\( V \\) qui est lui-même un espace vectoriel sous les mêmes opérations.

#### **Conditions de Sous-espace**
Un sous-ensemble non vide \\( W \\) de \\( V \\) est un sous-espace si :
1. **Stable par addition :** Si \\( \mathbf{u}, \mathbf{v} \in W \\), alors \\( \mathbf{u} + \mathbf{v} \in W \\).
2. **Stable par multiplication scalaire :** Si \\( \mathbf{v} \in W \\) et \\( c \in \mathbb{F} \\), alors \\( c\mathbf{v} \in W \\).

#### **Exemples de Sous-espaces**
1. L'ensemble de tous les vecteurs dans \\( \mathbb{R}^3 \\) de la forme \\( (x, 0, 0) \\).
2. L'ensemble de tous les polynômes avec uniquement des termes de degré pair.
3. L'ensemble des solutions d'une équation linéaire homogène.

---

### **3. Indépendance Linéaire**
Un ensemble de vecteurs \\( \{ \mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \} \\) dans \\( V \\) est **linéairement dépendant** s'il existe des scalaires \\( c_1, c_2, \dots, c_k \\), **non tous nuls**, tels que :

\\[
c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \dots + c_k \mathbf{v}_k = 0
\\]

Si la seule solution de cette équation est \\( c_1 = c_2 = \dots = c_k = 0 \\), les vecteurs sont **linéairement indépendants**.

#### **Exemples**
- Les vecteurs \\( (1,0) \\) et \\( (0,1) \\) dans \\( \mathbb{R}^2 \\) sont **linéairement indépendants**.
- Les vecteurs \\( (1,1) \\), \\( (2,2) \\) dans \\( \mathbb{R}^2 \\) sont **linéairement dépendants** car \\( 2(1,1) - (2,2) = (0,0) \\).

---

### **4. Base d'un Espace Vectoriel**
Une **base** d'un espace vectoriel \\( V \\) est un ensemble de **vecteurs linéairement indépendants** qui **engendrent** \\( V \\). Cela signifie :
1. Les vecteurs de base sont linéairement indépendants.
2. Tout vecteur dans \\( V \\) peut être exprimé comme une combinaison linéaire des vecteurs de base.

#### **Exemples**
1. La **base canonique** pour \\( \mathbb{R}^2 \\) est \\( \{ (1,0), (0,1) \} \\).
2. La **base canonique** pour \\( \mathbb{R}^3 \\) est \\( \{ (1,0,0), (0,1,0), (0,0,1) \} \\).

---

### **5. Dimension d'un Espace Vectoriel**
La **dimension** d'un espace vectoriel \\( V \\), notée \\( \dim(V) \\), est le nombre de vecteurs dans n'importe quelle base de \\( V \\).

#### **Exemples**
- \\( \dim(\mathbb{R}^n) = n \\).
- L'espace des polynômes de degré \\( \leq 2 \\) a une dimension **3**, avec la base \\( \{1, x, x^2\} \\).
- L'ensemble des solutions d'un système homogène de 3 équations à 5 inconnues forme un sous-espace de dimension **2**.

---

### **Résumé des Points Clés**

| Concept | Définition |
|---------|-----------|
| **Espace Vectoriel** | Un ensemble de vecteurs stable par addition et multiplication scalaire. |
| **Sous-espace** | Un sous-ensemble d'un espace vectoriel qui est lui-même un espace vectoriel. |
| **Indépendance Linéaire** | Un ensemble de vecteurs est indépendant si aucun vecteur ne peut être écrit comme une combinaison linéaire des autres. |
| **Base** | Un ensemble minimal de vecteurs qui engendre l'espace vectoriel. |
| **Dimension** | Le nombre de vecteurs dans une base de l'espace. |

---

### **Problèmes Pratiques**
1. Déterminer si l'ensemble de vecteurs \\( \{(1,2,3), (4,5,6), (7,8,9)\} \\) dans \\( \mathbb{R}^3 \\) est linéairement indépendant.
2. Trouver une base pour le sous-espace de \\( \mathbb{R}^3 \\) engendré par \\( \{(1,2,3), (2,4,6)\} \\).
3. Trouver la dimension de l'espace des solutions du système :
   \\[
   x + y + z = 0
   \\]
   \\[
   2x + 3y + 5z = 0
   \\]
4. Vérifier si l'ensemble \\( \{1, x, x^2, x^3\} \\) forme une base pour l'espace des polynômes de degré \\( \leq 3 \\).

Faites-moi savoir si vous avez besoin d'explications pour l'un de ces problèmes ! 🚀