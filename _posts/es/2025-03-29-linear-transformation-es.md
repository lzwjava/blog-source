---
audio: false
generated: true
lang: es
layout: post
title: Transformaciones Lineales
translated: true
type: note
---

**Definición, Ejemplos, Representación Matricial, Núcleo, Imagen, Propiedades (Inyectividad, Sobreyectividad)**

Las transformaciones lineales son fundamentales en el álgebra lineal, proporcionando un puente entre los espacios vectoriales y las matrices. Este tutorial cubre:
- **Definición** de transformaciones lineales
- **Ejemplos** de transformaciones lineales comunes
- **Representación matricial** de transformaciones lineales
- **Núcleo (espacio nulo)** e **Imagen (rango)**
- **Propiedades**: Inyectividad (uno a uno) y Sobreyectividad (sobre)

---

## **1. Definición de una Transformación Lineal**
Una **transformación lineal** (o aplicación lineal) entre dos espacios vectoriales \\( V \\) y \\( W \\) sobre un campo \\( \mathbb{F} \\) (usualmente \\( \mathbb{R} \\) o \\( \mathbb{C} \\)) es una función \\( T: V \to W \\) que satisface:
1. **Aditividad**:
   \\[
   T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \quad \forall \mathbf{u}, \mathbf{v} \in V
   \\]
2. **Homogeneidad (Multiplicación por Escalar)**:
   \\[
   T(c \mathbf{v}) = c T(\mathbf{v}) \quad \forall c \in \mathbb{F}, \mathbf{v} \in V
   \\]

**Idea Clave**: Las transformaciones lineales preservan la suma de vectores y la multiplicación por escalar.

---

## **2. Ejemplos de Transformaciones Lineales**

### **(a) Transformación Cero**
- \\( T(\mathbf{v}) = \mathbf{0} \\) para todo \\( \mathbf{v} \in V \\).

### **(b) Transformación Identidad**
- \\( T(\mathbf{v}) = \mathbf{v} \\) para todo \\( \mathbf{v} \in V \\).

### **(c) Rotación en \\( \mathbb{R}^2 \\**
- Rotar un vector por un ángulo \\( \theta \\):
  \\[
  T \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}
  \\]

### **(d) Derivación (Espacio de Polinomios)**
- \\( T: P_n \to P_{n-1} \\) donde \\( T(p(x)) = p'(x) \\).

### **(e) Multiplicación Matricial**
- Para una matriz fija \\( m \times n \\) \\( A \\), \\( T: \mathbb{R}^n \to \mathbb{R}^m \\) se define por \\( T(\mathbf{x}) = A\mathbf{x} \\).

---

## **3. Representación Matricial de Transformaciones Lineales**
Toda transformación lineal \\( T: \mathbb{R}^n \to \mathbb{R}^m \\) puede representarse por una matriz \\( m \times n \\) \\( A \\) tal que:
\\[
T(\mathbf{x}) = A\mathbf{x}
\\]

### **Cómo Encontrar la Matriz \\( A \\)**
1. Aplicar \\( T \\) a los vectores de la base estándar \\( \mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n \\) de \\( \mathbb{R}^n \\).
2. Las columnas de \\( A \\) son \\( T(\mathbf{e}_1), T(\mathbf{e}_2), \dots, T(\mathbf{e}_n) \\).

**Ejemplo**:
Sea \\( T: \mathbb{R}^2 \to \mathbb{R}^2 \\) definida por:
\\[
T \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 2x + y \\ x - 3y \end{pmatrix}
\\]
- Calcular \\( T(\mathbf{e}_1) = T(1, 0) = (2, 1) \\)
- Calcular \\( T(\mathbf{e}_2) = T(0, 1) = (1, -3) \\)
- Por lo tanto, la matriz \\( A \\) es:
  \\[
  A = \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix}
  \\]

---

## **4. Núcleo (Espacio Nulo) e Imagen (Rango)**

### **(a) Núcleo (Espacio Nulo)**
El **núcleo** de \\( T \\) es el conjunto de todos los vectores en \\( V \\) que se mapean a \\( \mathbf{0} \\):
\\[
\ker(T) = \{ \mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0} \}
\\]

**Propiedades**:
- \\( \ker(T) \\) es un subespacio de \\( V \\).
- \\( T \\) es **inyectiva (uno a uno)** si y solo si \\( \ker(T) = \{ \mathbf{0}}\\).

**Ejemplo**:
Para \\( T(\mathbf{x}) = A\mathbf{x} \\) donde \\( A = \begin{pmatrix} 1 & 2 \\ 3 & 6 \end{pmatrix} \\),
\\[
\ker(T) = \text{Span} \left\{ \begin{pmatrix} -2 \\ 1 \end{pmatrix} \right\}
\\]

### **(b) Imagen (Rango)**
La **imagen** de \\( T \\) es el conjunto de todas las salidas en \\( W \\):
\\[
\text{Im}(T) = \{ T(\mathbf{v}) \mid \mathbf{v} \in V \}
\\]

**Propiedades**:
- \\( \text{Im}(T) \\) es un subespacio de \\( W \\).
- \\( T \\) es **sobreyectiva (sobre)** si y solo si \\( \text{Im}(T) = W \\).

**Ejemplo**:
Para \\( T(\mathbf{x}) = A\mathbf{x} \\) donde \\( A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix} \\),
\\[
\text{Im}(T) = \text{Span} \left\{ \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \right\}
\\]

---

## **5. Propiedades: Inyectividad y Sobreyectividad**

### **(a) Inyectividad (Uno a Uno)**
Una transformación lineal \\( T \\) es **inyectiva** si:
\\[
T(\mathbf{u}) = T(\mathbf{v}) \implies \mathbf{u} = \mathbf{v}
\\]
**Prueba**:
- \\( T \\) es inyectiva \\( \iff \ker(T) = \{ \mathbf{0} \} \\).
- Si \\( \dim(V) < \dim(W) \\), \\( T \\) puede no ser inyectiva.

### **(b) Sobreyectividad (Sobre)**
Una transformación lineal \\( T \\) es **sobreyectiva** si:
\\[
\forall \mathbf{w} \in W, \exists \mathbf{v} \in V \text{ tal que } T(\mathbf{v}) = \mathbf{w}
\\]
**Prueba**:
- \\( T \\) es sobreyectiva \\( \iff \text{Im}(T) = W \\).
- Si \\( \dim(V) > \dim(W) \\), \\( T \\) puede no ser sobreyectiva.

### **(c) Teorema de la Nulidad y el Rango**
Para \\( T: V \to W \\),
\\[
\dim(V) = \dim(\ker(T)) + \dim(\text{Im}(T))
\\]
- **Rango** \\( = \dim(\text{Im}(T)) \\)
- **Nulidad** \\( = \dim(\ker(T)) \\)

**Ejemplo**:
Si \\( T: \mathbb{R}^3 \to \mathbb{R}^2 \\) tiene \\( \dim(\ker(T)) = 1 \\), entonces \\( \dim(\text{Im}(T)) = 2 \\).

---

## **Resumen**

| Concepto | Definición | Propiedad Clave |
|---------|------------|--------------|
| **Transformación Lineal** | \\( T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \\) y \\( T(c\mathbf{v}) = cT(\mathbf{v}) \\) | Preserva la estructura lineal |
| **Representación Matricial** | \\( T(\mathbf{x}) = A\mathbf{x} \\) donde las columnas de \\( A \\) son \\( T(\mathbf{e}_i) \\) | Codifica la transformación |
| **Núcleo** | \\( \ker(T) = \{ \mathbf{v} \mid T(\mathbf{v}) = \mathbf{0} \} \\) | Mide la inyectividad |
| **Imagen** | \\( \text{Im}(T) = \{ T(\mathbf{v}) \mid \mathbf{v} \in V \} \\) | Mide la sobreyectividad |
| **Inyectividad** | \\( \ker(T) = \{ \mathbf{0} \} \\) | Uno a uno |
| **Sobreyectividad** | \\( \text{Im}(T) = W \\) | Sobre |

---

## **Problemas de Práctica**
1. Encuentra la representación matricial de \\( T(x, y, z) = (2x - y, y + 3z) \\).
2. Determina si \\( T(\mathbf{x}) = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \mathbf{x} \\) es inyectiva/sobreyectiva.
3. Calcula \\( \ker(T) \\) e \\( \text{Im}(T) \\) para \\( T(x, y) = (x + y, 2x - y, x) \\).

---

Este tutorial cubre los conceptos centrales de las transformaciones lineales como se enseñan típicamente en un curso de pregrado de álgebra lineal. ¡Avísame si necesitas más aclaraciones o ejemplos adicionales!