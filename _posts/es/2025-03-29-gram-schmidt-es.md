---
audio: false
generated: true
lang: es
layout: post
title: Proceso de Gram-Schmidt
translated: true
type: note
---

El **proceso de Gram-Schmidt** es un método en álgebra lineal utilizado para convertir un conjunto de vectores linealmente independientes en un conjunto ortonormal de vectores que generan el mismo subespacio. Esto es particularmente útil en varias aplicaciones como la descomposición QR, la resolución de problemas de mínimos cuadrados y la simplificación de cálculos en espacios vectoriales.

### **Conceptos Clave**

- **Vectores Linealmente Independientes**: Vectores que no pueden expresarse como una combinación lineal entre sí.
- **Vectores Ortogonales**: Vectores que son perpendiculares entre sí, lo que significa que su producto escalar es cero.
- **Conjunto Ortonormal**: Un conjunto de vectores que son tanto ortogonales como de longitud unitaria (norma igual a 1).

### **Propósito del Proceso de Gram-Schmidt**

- **Ortogonalización**: Transformar un conjunto de vectores en un conjunto donde cada vector es ortogonal a los demás.
- **Normalización**: Ajustar la longitud de cada vector para convertirlo en un vector unitario.
- **Simplificación**: Facilitar cálculos más sencillos en proyecciones, descomposiciones y transformaciones dentro de espacios vectoriales.

### **El Proceso Explicado**

Dado un conjunto de vectores linealmente independientes \\( \{ \mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \} \\) en un espacio con producto interno (como \\( \mathbb{R}^n \\)), el proceso de Gram-Schmidt construye un conjunto ortonormal \\( \{ \mathbf{q}_1, \mathbf{q}_2, \ldots, \mathbf{q}_n \} \\) siguiendo estos pasos:

1. **Inicializar el Primer Vector**:
   \\[
   \mathbf{u}_1 = \mathbf{v}_1
   \\]
   Normalizar para obtener:
   \\[
   \mathbf{q}_1 = \frac{\mathbf{u}_1}{\| \mathbf{u}_1 \|}
   \\]

2. **Ortogonalización y Normalización Iterativas** para \\( k = 2 \\) a \\( n \\):
   - **Ortogonalizar**:
     \\[
     \mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \text{proj}_{\mathbf{q}_j} \mathbf{v}_k
     \\]
     donde la proyección \\( \text{proj}_{\mathbf{q}_j} \mathbf{v}_k \\) se calcula como:
     \\[
     \text{proj}_{\mathbf{q}_j} \mathbf{v}_k = (\mathbf{v}_k \cdot \mathbf{q}_j) \mathbf{q}_j
     \\]
   - **Normalizar**:
     \\[
     \mathbf{q}_k = \frac{\mathbf{u}_k}{\| \mathbf{u}_k \|}
     \\]

### **Pasos Detallados**

1. **Calcular \\( \mathbf{u}_1 \\) y \\( \mathbf{q}_1 \\)**:
   - \\( \mathbf{u}_1 = \mathbf{v}_1 \\)
   - \\( \mathbf{q}_1 = \frac{\mathbf{u}_1}{\| \mathbf{u}_1 \|} \\)

2. **Para cada vector subsiguiente \\( \mathbf{v}_k \\)**:
   - **Restar las proyecciones sobre todos los \\( \mathbf{q}_j \\) anteriores**:
     \\[
     \mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} (\mathbf{v}_k \cdot \mathbf{q}_j) \mathbf{q}_j
     \\]
   - **Normalizar \\( \mathbf{u}_k \\) para obtener \\( \mathbf{q}_k \\)**:
     \\[
     \mathbf{q}_k = \frac{\mathbf{u}_k}{\| \mathbf{u}_k \|}
     \\]

### **Ejemplo**

Apliquemos el proceso de Gram-Schmidt a los vectores \\( \mathbf{v}_1 = [1, 1] \\) y \\( \mathbf{v}_2 = [1, 0] \\) en \\( \mathbb{R}^2 \\).

1. **Primer Vector**:
   - \\( \mathbf{u}_1 = \mathbf{v}_1 = [1, 1] \\)
   - Normalizar:
     \\[
     \| \mathbf{u}_1 \| = \sqrt{1^2 + 1^2} = \sqrt{2}
     \\]
     \\[
     \mathbf{q}_1 = \frac{[1, 1]}{\sqrt{2}} = \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right]
     \\]

2. **Segundo Vector**:
   - Calcular la proyección de \\( \mathbf{v}_2 \\) sobre \\( \mathbf{q}_1 \\):
     \\[
     \text{proj}_{\mathbf{q}_1} \mathbf{v}_2 = (\mathbf{v}_2 \cdot \mathbf{q}_1) \mathbf{q}_1
     \\]
     \\[
     \mathbf{v}_2 \cdot \mathbf{q}_1 = [1, 0] \cdot \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right] = \frac{1}{\sqrt{2}}
     \\]
     \\[
     \text{proj}_{\mathbf{q}_1} \mathbf{v}_2 = \frac{1}{\sqrt{2}} \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right] = \left[ \frac{1}{2}, \frac{1}{2} \right]
     \\]
   - Restar la proyección:
     \\[
     \mathbf{u}_2 = \mathbf{v}_2 - \text{proj}_{\mathbf{q}_1} \mathbf{v}_2 = [1, 0] - \left[ \frac{1}{2}, \frac{1}{2} \right] = \left[ \frac{1}{2}, -\frac{1}{2} \right]
     \\]
   - Normalizar \\( \mathbf{u}_2 \\):
     \\[
     \| \mathbf{u}_2 \| = \sqrt{\left( \frac{1}{2} \right)^2 + \left( -\frac{1}{2} \right)^2} = \frac{1}{\sqrt{2}}
     \\]
     \\[
     \mathbf{q}_2 = \frac{\left[ \frac{1}{2}, -\frac{1}{2} \right]}{\frac{1}{\sqrt{2}}} = \left[ \frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2} \right]
     \\]

### **Resultado**

El conjunto ortonormal es:
\\[
\mathbf{q}_1 = \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right], \quad \mathbf{q}_2 = \left[ \frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2} \right]
\\]

Estos vectores son ortogonales (\\( \mathbf{q}_1 \cdot \mathbf{q}_2 = 0 \\)) y de longitud unitaria (\\( \| \mathbf{q}_1 \| = \| \mathbf{q}_2 \| = 1 \\)).

### **Aplicaciones**

- **Descomposición QR**: Descomponer una matriz en una matriz ortogonal \\( Q \\) y una matriz triangular superior \\( R \\).
- **Problemas de Mínimos Cuadrados**: Encontrar la solución de mejor aproximación para sistemas sobredeterminados.
- **Métodos Numéricos**: Mejorar la estabilidad y eficiencia en algoritmos computacionales.

### **Resumen**

El proceso de Gram-Schmidt es un método sistemático para ortonormalizar un conjunto de vectores en un espacio con producto interno, asegurando que el nuevo conjunto sea más fácil de manejar mientras se preserva el espacio generado por los vectores originales. Es fundamental en álgebra lineal y tiene aplicaciones de amplio alcance en matemáticas, física e ingeniería.