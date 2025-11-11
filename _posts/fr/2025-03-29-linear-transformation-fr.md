---
audio: false
generated: true
lang: fr
layout: post
title: Transformations linéaires
translated: true
type: note
---

**Définition, Exemples, Représentation Matricielle, Noyau, Image, Propriétés (Injectivité, Surjectivité)**

Les transformations linéaires sont fondamentales en algèbre linéaire, fournissant un pont entre les espaces vectoriels et les matrices. Ce tutoriel couvre :
- La **Définition** des transformations linéaires
- Des **Exemples** de transformations linéaires courantes
- La **Représentation matricielle** des transformations linéaires
- Le **Noyau (espace nul)** et l'**Image (image)**
- Les **Propriétés** : Injectivité (application injective) et Surjectivité (application surjective)

---

## **1. Définition d'une Transformation Linéaire**

Une **transformation linéaire** (ou application linéaire) entre deux espaces vectoriels \\( V \\) et \\( W \\) sur un corps \\( \mathbb{F} \\) (généralement \\( \mathbb{R} \\) ou \\( \mathbb{C} \\)) est une fonction \\( T: V \to W \\) qui satisfait :
1. **Additivité** :
   \\[
   T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \quad \forall \mathbf{u}, \mathbf{v} \in V
   \\]
2. **Homogénéité (Multiplication par un Scalaire)** :
   \\[
   T(c \mathbf{v}) = c T(\mathbf{v}) \quad \forall c \in \mathbb{F}, \mathbf{v} \in V
   \\]

**Idée Clé** : Les transformations linéaires préservent l'addition vectorielle et la multiplication par un scalaire.

---

## **2. Exemples de Transformations Linéaires**

### **(a) Transformation Nulle**
- \\( T(\mathbf{v}) = \mathbf{0} \\) pour tout \\( \mathbf{v} \in V \\).

### **(b) Transformation Identité**
- \\( T(\mathbf{v}) = \mathbf{v} \\) pour tout \\( \mathbf{v} \in V \\).

### **(c) Rotation dans \\( \mathbb{R}^2 \\)**
- Rotation d'un vecteur d'un angle \\( \theta \\) :
  \\[
  T \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}
  \\]

### **(d) Dérivation (Espace des Polynômes)**
- \\( T: P_n \to P_{n-1} \\) où \\( T(p(x)) = p'(x) \\).

### **(e) Multiplication Matricielle**
- Pour une matrice fixe \\( m \times n \\) \\( A \\), \\( T: \mathbb{R}^n \to \mathbb{R}^m \\) est définie par \\( T(\mathbf{x}) = A\mathbf{x} \\).

---

## **3. Représentation Matricielle des Transformations Linéaires**

Toute transformation linéaire \\( T: \mathbb{R}^n \to \mathbb{R}^m \\) peut être représentée par une matrice \\( m \times n \\) \\( A \\) telle que :
\\[
T(\mathbf{x}) = A\mathbf{x}
\\]

### **Comment Trouver la Matrice \\( A \\)**
1. Appliquer \\( T \\) aux vecteurs de base standard \\( \mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n \\) de \\( \mathbb{R}^n \\).
2. Les colonnes de \\( A \\) sont \\( T(\mathbf{e}_1), T(\mathbf{e}_2), \dots, T(\mathbf{e}_n) \\).

**Exemple** :
Soit \\( T: \mathbb{R}^2 \to \mathbb{R}^2 \\) définie par :
\\[
T \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 2x + y \\ x - 3y \end{pmatrix}
\\]
- Calculer \\( T(\mathbf{e}_1) = T(1, 0) = (2, 1) \\)
- Calculer \\( T(\mathbf{e}_2) = T(0, 1) = (1, -3) \\)
- Ainsi, la matrice \\( A \\) est :
  \\[
  A = \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix}
  \\]

---

## **4. Noyau (Espace Nul) et Image**

### **(a) Noyau (Espace Nul)**
Le **noyau** de \\( T \\) est l'ensemble de tous les vecteurs de \\( V \\) qui sont envoyés sur \\( \mathbf{0} \\) :
\\[
\ker(T) = \{ \mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0} \}
\\]

**Propriétés** :
- \\( \ker(T) \\) est un sous-espace vectoriel de \\( V \\).
- \\( T \\) est **injective** si et seulement si \\( \ker(T) = \{ \mathbf{0}}\ \\).

**Exemple** :
Pour \\( T(\mathbf{x}) = A\mathbf{x} \\) où \\( A = \begin{pmatrix} 1 & 2 \\ 3 & 6 \end{pmatrix} \\),
\\[
\ker(T) = \text{Span} \left\{ \begin{pmatrix} -2 \\ 1 \end{pmatrix} \right\}
\\]

### **(b) Image**
L'**image** de \\( T \\) est l'ensemble de toutes les sorties dans \\( W \\) :
\\[
\text{Im}(T) = \{ T(\mathbf{v}) \mid \mathbf{v} \in V \}
\\]

**Propriétés** :
- \\( \text{Im}(T) \\) est un sous-espace vectoriel de \\( W \\).
- \\( T \\) est **surjective** si et seulement si \\( \text{Im}(T) = W \\).

**Exemple** :
Pour \\( T(\mathbf{x}) = A\mathbf{x} \\) où \\( A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix} \\),
\\[
\text{Im}(T) = \text{Span} \left\{ \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \right\}
\\]

---

## **5. Propriétés : Injectivité et Surjectivité**

### **(a) Injectivité (Application Injective)**
Une transformation linéaire \\( T \\) est **injective** si :
\\[
T(\mathbf{u}) = T(\mathbf{v}) \implies \mathbf{u} = \mathbf{v}
\\]
**Test** :
- \\( T \\) est injective \\( \iff \ker(T) = \{ \mathbf{0} \} \\).
- Si \\( \dim(V) < \dim(W) \\), \\( T \\) peut ne pas être injective.

### **(b) Surjectivité (Application Surjective)**
Une transformation linéaire \\( T \\) est **surjective** si :
\\[
\forall \mathbf{w} \in W, \exists \mathbf{v} \in V \text{ tel que } T(\mathbf{v}) = \mathbf{w}
\\]
**Test** :
- \\( T \\) est surjective \\( \iff \text{Im}(T) = W \\).
- Si \\( \dim(V) > \dim(W) \\), \\( T \\) peut ne pas être surjective.

### **(c) Théorème du Rang**
Pour \\( T: V \to W \\),
\\[
\dim(V) = \dim(\ker(T)) + \dim(\text{Im}(T))
\\]
- **Rang** \\( = \dim(\text{Im}(T)) \\)
- **Nulité** \\( = \dim(\ker(T)) \\)

**Exemple** :
Si \\( T: \mathbb{R}^3 \to \mathbb{R}^2 \\) a \\( \dim(\ker(T)) = 1 \\), alors \\( \dim(\text{Im}(T)) = 2 \\).

---

## **Résumé**

| Concept | Définition | Propriété Clé |
|---------|------------|--------------|
| **Transformation Linéaire** | \\( T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \\) et \\( T(c\mathbf{v}) = cT(\mathbf{v}) \\) | Préserve la structure linéaire |
| **Représentation Matricielle** | \\( T(\mathbf{x}) = A\mathbf{x} \\) où les colonnes de \\( A \\) sont \\( T(\mathbf{e}_i) \\) | Encode la transformation |
| **Noyau** | \\( \ker(T) = \{ \mathbf{v} \mid T(\mathbf{v}) = \mathbf{0} \} \\) | Mesure l'injectivité |
| **Image** | \\( \text{Im}(T) = \{ T(\mathbf{v}) \mid \mathbf{v} \in V \} \\) | Mesure la surjectivité |
| **Injectivité** | \\( \ker(T) = \{ \mathbf{0} \} \\) | Application injective |
| **Surjectivité** | \\( \text{Im}(T) = W \\) | Application surjective |

---

## **Problèmes Pratiques**
1. Trouvez la représentation matricielle de \\( T(x, y, z) = (2x - y, y + 3z) \\).
2. Déterminez si \\( T(\mathbf{x}) = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \mathbf{x} \\) est injective/surjective.
3. Calculez \\( \ker(T) \\) et \\( \text{Im}(T) \\) pour \\( T(x, y) = (x + y, 2x - y, x) \\).

---

Ce tutoriel couvre les concepts fondamentaux des transformations linéaires tels qu'enseignés typiquement dans un cours d'algèbre linéaire de premier cycle. Faites-moi savoir si vous avez besoin de précisions supplémentaires ou d'exemples complémentaires !