---
audio: false
generated: true
lang: es
layout: post
title: Estabilización de las Puntuaciones de Atención en los Transformadores
translated: true
type: note
---

Dividir por la raíz cuadrada de la dimensión clave, \\(\sqrt{d_k}\\), en el mecanismo de atención de producto escalar escalado (como en la fórmula \\(\text{Puntuaciones Escaladas} = \frac{Q K^T}{\sqrt{d_k}}\\)) es una elección deliberada para estabilizar los gradientes y prevenir valores grandes, particularmente en el contexto de los transformers. He aquí por qué se usa \\(\sqrt{d_k}\\) en lugar de solo \\(d_k\\):

1.  **Varianza del Producto Punto**:
    - El producto punto \\( Q K^T \\) calcula la similitud entre los vectores query (\\( Q \\)) y key (\\( K \\)), donde cada vector tiene dimensión \\( d_k \\). Si se asume que los elementos de \\( Q \\) y \\( K \\) son independientes y tienen una media de 0 y una varianza de 1 (común después de la inicialización o normalización), el producto punto \\( Q_i \cdot K_j \\) (para un solo par de vectores query y key) tiene una varianza de \\( d_k \\). Esto se debe a que la varianza de la suma de \\( d_k \\) productos independientes de dos variables normales estándar escala linealmente con \\( d_k \\).
    - Sin escalado, la magnitud de \\( Q K^T \\) crece con \\( d_k \\), lo que lleva a valores muy grandes para \\( d_k \\) grandes (común en transformers, donde \\( d_k \\) podría ser 64, 128 o más). Los valores grandes en las puntuaciones de atención pueden causar problemas cuando se pasan por la función softmax.

2.  **Estabilidad del Softmax**:
    - Las puntuaciones de atención \\( \frac{Q K^T}{\sqrt{d_k}} \\) se introducen en un softmax para calcular los pesos de atención. Si las puntuaciones son demasiado grandes (como lo serían sin escalado o con un escalado insuficiente), la función softmax puede producir distribuciones muy pronunciadas, donde un elemento domina (acercándose a 1) y los demás están cerca de 0. Esto conduce a gradientes que se desvanecen para la mayoría de los elementos, dificultando que el modelo aprenda de manera efectiva.
    - Dividir por \\(\sqrt{d_k}\\) asegura que la varianza de las puntuaciones escaladas sea aproximadamente 1, manteniendo las puntuaciones en un rango donde la función softmax se comporta bien, produciendo pesos de atención más equilibrados y gradientes estables.

3.  **¿Por qué no \\( d_k \\)?**:
    - Dividir por \\( d_k \\) en lugar de \\(\sqrt{d_k}\\) sobre-escalaría el producto punto, reduciendo la varianza de las puntuaciones a \\( \frac{1}{d_k} \\). Para \\( d_k \\) grandes, esto haría que las puntuaciones fueran muy pequeñas, causando que el softmax produzca distribuciones casi uniformes (ya que entradas pequeñas al softmax resultan en salidas cercanas a \\( \frac{1}{n} \\)). Esto diluiría la capacidad del mecanismo de atención para enfocarse en las keys relevantes, ya que las diferencias entre las puntuaciones se verían disminuidas.
    - El sobre-escalado con \\( d_k \\) también podría conducir a inestabilidad numérica en algunos casos, ya que los valores muy pequeños podrían ser más difíciles de manejar con precisión en aritmética de punto flotante.

4.  **¿Por qué \\(\sqrt{d_k}\\)?**:
    - Dividir por \\(\sqrt{d_k}\\) normaliza la varianza del producto punto a aproximadamente 1, ya que \\( \text{Var}\left(\frac{Q K^T}{\sqrt{d_k}}\right) = \frac{\text{Var}(Q K^T)}{d_k} = \frac{d_k}{d_k} = 1 \\). Esto mantiene las puntuaciones en un rango razonable, asegurando que el softmax produzca pesos de atención significativos sin ser excesivamente pronunciados o excesivamente uniformes.
    - La raíz cuadrada surge naturalmente de la propiedad matemática de la varianza del producto punto. Logra un equilibrio entre prevenir valores explosivos (que ocurrirían sin escalado) y evitar la supresión excesiva de las puntuaciones (que ocurriría con \\( d_k \\)).

5.  **Efectividad Empírica**:
    - La elección de \\(\sqrt{d_k}\\) fue introducida en el artículo original del Transformer ("Attention is All You Need" por Vaswani et al., 2017) y ha sido validada empíricamente en muchos modelos basados en transformers. Funciona bien en la práctica para una amplia gama de valores de \\( d_k \\), asegurando un entrenamiento estable y un buen rendimiento.

En resumen, dividir por \\(\sqrt{d_k}\\) es una elección motivada matemáticamente que estabiliza la varianza de las puntuaciones de atención, asegura que el softmax opere en un régimen bien comportado y evita los problemas de gradientes explosivos o que se desvanecen. Dividir por \\( d_k \\) reduciría excesivamente las puntuaciones, conduciendo a pesos de atención menos discriminatorios y potencialmente dañando el rendimiento del modelo.