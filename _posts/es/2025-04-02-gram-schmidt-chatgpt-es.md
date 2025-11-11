---
audio: false
generated: true
lang: es
layout: post
title: Proceso de Gram-Schmidt
translated: true
type: note
---

El **proceso de Gram-Schmidt** es un método para ortonormalizar un conjunto de vectores linealmente independientes en un espacio con producto interno (típicamente \\(\mathbb{R}^n\\) o \\(\mathbb{C}^n\\)). Convierte una base dada en una **base ortonormal**, donde los vectores son mutuamente ortogonales y tienen longitud unitaria.

---

### **Algoritmo: Proceso de Gram-Schmidt**
Dado un conjunto de vectores **linealmente independientes** \\( \{v_1, v_2, \dots, v_n\} \\) en un espacio con producto interno, construimos una **base ortonormal** \\( \{u_1, u_2, \dots, u_n\} \\) de la siguiente manera:

1. **Paso 1: Calcular el primer vector ortonormal**  
   \\[
   u_1 = \frac{v_1}{\|v_1\|}
   \\]
   
2. **Paso 2: Hacer el segundo vector ortogonal al primero y normalizarlo**  
   \\[
   v_2' = v_2 - \text{proj}_{u_1}(v_2) = v_2 - \frac{\langle v_2, u_1 \rangle}{\langle u_1, u_1 \rangle} u_1
   \\]
   \\[
   u_2 = \frac{v_2'}{\|v_2'\|}
   \\]

3. **Paso 3: Repetir para los vectores restantes**  
   Para \\( k = 3, \dots, n \\):
   \\[
   v_k' = v_k - \sum_{j=1}^{k-1} \frac{\langle v_k, u_j \rangle}{\langle u_j, u_j \rangle} u_j
   \\]
   \\[
   u_k = \frac{v_k'}{\|v_k'\|}
   \\]

Aquí, \\( \text{proj}_{u_j}(v_k) = \frac{\langle v_k, u_j \rangle}{\langle u_j, u_j \rangle} u_j \\) representa la proyección de \\( v_k \\) sobre \\( u_j \\).

---

### **Ejemplo: Aplicando Gram-Schmidt en \\(\mathbb{R}^3\\)**  
Dados los vectores:

\\[
v_1 = (1, 1, 0), \quad v_2 = (1, 0, 1), \quad v_3 = (0, 1, 1)
\\]

#### **Paso 1: Normalizar \\( v_1 \\)**
\\[
u_1 = \frac{v_1}{\|v_1\|} = \frac{(1,1,0)}{\sqrt{2}} = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0\right)
\\]

#### **Paso 2: Ortogonalizar \\( v_2 \\) respecto a \\( u_1 \\)**
\\[
\text{proj}_{u_1}(v_2) = \frac{\langle v_2, u_1 \rangle}{\langle u_1, u_1 \rangle} u_1
\\]

\\[
= \frac{(1,0,1) \cdot (1/\sqrt{2}, 1/\sqrt{2}, 0)}{1} \cdot (1/\sqrt{2}, 1/\sqrt{2}, 0)
\\]

\\[
= \frac{1 \cdot 1/\sqrt{2} + 0 \cdot 1/\sqrt{2} + 1 \cdot 0}{1} \cdot (1/\sqrt{2}, 1/\sqrt{2}, 0)
\\]

\\[
= \frac{1/\sqrt{2}}{1} \cdot (1/\sqrt{2}, 1/\sqrt{2}, 0) = \left(\frac{1}{2}, \frac{1}{2}, 0\right)
\\]

\\[
v_2' = v_2 - \text{proj}_{u_1}(v_2) = \left(1,0,1\right) - \left(\frac{1}{2}, \frac{1}{2}, 0\right) = \left(\frac{1}{2}, -\frac{1}{2}, 1\right)
\\]

\\[
u_2 = \frac{v_2'}{\|v_2'\|}
\\]

\\[
= \frac{\left(\frac{1}{2}, -\frac{1}{2}, 1\right)}{\sqrt{\left(\frac{1}{2}\right)^2 + \left(-\frac{1}{2}\right)^2 + (1)^2}}
\\]

\\[
= \frac{\left(\frac{1}{2}, -\frac{1}{2}, 1\right)}{\sqrt{\frac{1}{4} + \frac{1}{4} + 1}} = \frac{\left(\frac{1}{2}, -\frac{1}{2}, 1\right)}{\sqrt{\frac{3}{2}}}
\\]

#### **Paso 3: Ortogonalizar \\( v_3 \\) respecto a \\( u_1 \\) y \\( u_2 \\)**
Seguir el mismo procedimiento para \\( v_3 \\), proyectando sobre \\( u_1 \\) y \\( u_2 \\), y luego normalizando.

---

### **Resumen**
El **proceso de Gram-Schmidt** transforma un conjunto de vectores linealmente independientes en una **base ortonormal** paso a paso, asegurando que cada vector sea ortogonal a los anteriores y tenga longitud unitaria. Este proceso es fundamental en aplicaciones como:

- La descomposición QR en álgebra lineal numérica.
- La construcción de bases ortonormales para espacios de funciones en análisis de Fourier.
- La mejora de la estabilidad numérica en algoritmos computacionales.

¡Avísame si quieres que desarrolle el ejemplo completo o que aclare alguna parte! 🚀