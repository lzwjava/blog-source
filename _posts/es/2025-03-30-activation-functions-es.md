---
audio: false
generated: true
lang: es
layout: post
title: Funciones de Activación en Redes Neuronales
translated: true
type: note
---

La **sigmoid**, **ReLU** y **Leaky ReLU** son todas funciones de activación utilizadas en redes neuronales. Cada una tiene características únicas y es adecuada para diferentes tareas dependiendo del tipo de problema que se esté resolviendo. Aquí hay un desglose de las diferencias:

### 1. **Sigmoid**:
   - **Fórmula**:  
     \\[
     \sigma(x) = \frac{1}{1 + e^{-x}}
     \\]
   - **Rango**: (0, 1)
   - **Ventajas**:
     - Gradiente suave, lo que ayuda con la optimización.
     - La salida está acotada entre 0 y 1, lo que la hace buena para probabilidades o clasificación binaria.
   - **Desventajas**:
     - **Problema del gradiente vanishing**: Para valores de entrada muy grandes o muy pequeños, el gradiente se vuelve muy pequeño (casi cero), lo que puede ralentizar el entrenamiento, especialmente en redes profundas.
     - Las salidas no están centradas en cero, lo que puede llevar a problemas cuando las actualizaciones del gradiente están dominadas por una dirección.
   - **Caso de uso**: Se utiliza a menudo en la capa de salida para tareas de clasificación binaria (por ejemplo, en regresión logística).

### 2. **ReLU (Unidad Lineal Rectificada)**:
   - **Fórmula**:  
     \\[
     f(x) = \max(0, x)
     \\]
   - **Rango**: [0, ∞)
   - **Ventajas**:
     - **Rápida y simple**: Fácil de calcular y eficiente en la práctica.
     - Resuelve el problema del gradiente vanishing al permitir que los gradientes se propaguen bien.
     - Fomenta la dispersión (muchas neuronas pueden volverse inactivas).
   - **Desventajas**:
     - **Problema del ReLU moribundo**: Las neuronas pueden "morir" durante el entrenamiento si su salida es siempre cero (es decir, para entradas negativas). Esto puede hacer que algunas neuronas no se activen nunca más.
   - **Caso de uso**: Muy comúnmente utilizada en las capas ocultas de redes profundas, especialmente en redes neuronales convolucionales y profundas.

### 3. **Leaky ReLU**:
   - **Fórmula**:  
     \\[
     f(x) = \max(\alpha x, x)
     \\]
     Donde \\( \alpha \\) es una constante pequeña (por ejemplo, 0.01).
   - **Rango**: (-∞, ∞)
   - **Ventajas**:
     - Previene el **problema del ReLU moribundo** al permitir una pequeña pendiente negativa para valores negativos de \\( x \\).
     - Al igual que ReLU, ayuda con el problema del gradiente vanishing y fomenta la dispersión.
   - **Desventajas**:
     - Todavía tiene cierto potencial para salidas negativas, pero es mucho menos problemático que el ReLU estándar.
     - La elección de \\( \alpha \\) puede ser complicada y a veces requiere ajuste.
   - **Caso de uso**: Se utiliza en muchos modelos de aprendizaje profundo para evitar problemas con ReLU, especialmente en redes donde podría ocurrir el problema del ReLU moribundo.

---

### **Resumen de Comparación**:

- **Sigmoid**:  
  La mejor para capas de salida en tareas de clasificación binaria, pero sufre del problema del gradiente vanishing.

- **ReLU**:  
  Una buena función de activación de propósito general para capas ocultas. Acelera el entrenamiento y funciona bien para redes grandes, pero puede sufrir el problema de la neurona moribunda.

- **Leaky ReLU**:  
  Una modificación de ReLU que aborda el problema del ReLU moribundo al permitir un gradiente pequeño y distinto de cero para entradas negativas. Se utiliza ampliamente para modelos más profundos.

### **En la práctica**:
- **Sigmoid** se usa a menudo cuando la salida debe estar en el rango de (0, 1), como en la capa final de tareas de clasificación binaria.
- **ReLU** suele ser la opción por defecto para las capas ocultas debido a su simplicidad y su capacidad para manejar bien los gradientes vanishing.
- **Leaky ReLU** se utiliza en lugar de ReLU cuando existen preocupaciones sobre que las neuronas "mueran" durante el entrenamiento.

¡Cada una de estas funciones de activación tiene su lugar dependiendo de la estructura y los objetivos de la red neuronal que estés construyendo