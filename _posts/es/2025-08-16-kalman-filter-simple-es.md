---
audio: false
generated: true
image: false
lang: es
layout: post
title: Filtro de Kalman Explicado de Forma Sencilla
translated: true
type: note
---

Aquí tienes una **guía completa sobre el Filtro de Kalman (卡尔曼滤波)** en inglés, estructurada para mayor claridad:

---

# 1. Introducción

El **filtro de Kalman** es un **algoritmo** que proporciona estimaciones de variables desconocidas combinando mediciones ruidosas de sensores con predicciones de un modelo del sistema. Es ampliamente utilizado en **sistemas de control, navegación, robótica, visión por computadora y finanzas**.

Idea clave:
Funciona de forma recursiva, lo que significa que actualiza continuamente su estimación a medida que llegan nuevas mediciones, en lugar de esperar a todo el conjunto de datos.

---

# 2. Conceptos Básicos

### Estado

El conjunto de variables que queremos estimar (por ejemplo, posición, velocidad).

### Modelo del Proceso

Describe cómo evoluciona el estado en el tiempo, generalmente con cierta incertidumbre.

### Modelo de Medición

Relaciona las mediciones reales del sensor con el estado subyacente.

### Ruido

Tanto el proceso como las mediciones tienen incertidumbre (ruido aleatorio). El filtro de Kalman modela esto explícitamente usando probabilidades.

---

# 3. Formulación Matemática

El filtro de Kalman asume un **sistema lineal** con ruido gaussiano.

* **Ecuación de estado (predicción):**

  $$
  x_k = A x_{k-1} + B u_k + w_k
  $$

  * $x_k$: estado en el tiempo $k$
  * $A$: matriz de transición de estado
  * $B u_k$: entrada de control
  * $w_k$: ruido del proceso (Gaussiano, covarianza $Q$)

* **Ecuación de medición (observación):**

  $$
  z_k = H x_k + v_k
  $$

  * $z_k$: medición
  * $H$: matriz de observación
  * $v_k$: ruido de medición (Gaussiano, covarianza $R$)

---

# 4. Los Dos Pasos Principales

### Paso 1: Predicción

* Predice el estado hacia adelante en el tiempo.
* Predice la incertidumbre (covarianza del error).

### Paso 2: Actualización (Corrección)

* Compara la medición predicha con la medición real.
* Calcula la **Ganancia de Kalman** (cuánta confianza depositar en la medición vs. la predicción).
* Actualiza la estimación y reduce la incertidumbre.

---

# 5. Ecuaciones del Filtro de Kalman (Caso Lineal)

1. **Predecir el estado:**

   $$
   \hat{x}_k^- = A \hat{x}_{k-1} + B u_k
   $$

2. **Predecir la covarianza:**

   $$
   P_k^- = A P_{k-1} A^T + Q
   $$

3. **Ganancia de Kalman:**

   $$
   K_k = P_k^- H^T (H P_k^- H^T + R)^{-1}
   $$

4. **Actualizar el estado:**

   $$
   \hat{x}_k = \hat{x}_k^- + K_k (z_k - H \hat{x}_k^-)
   $$

5. **Actualizar la covarianza:**

   $$
   P_k = (I - K_k H) P_k^-
   $$

Donde:

* $\hat{x}_k^-$: estado predicho antes de la actualización
* $\hat{x}_k$: estado actualizado
* $P_k$: matriz de covarianza (incertidumbre en la estimación)

---

# 6. Intuición

* Si la medición es **muy ruidosa** ($R$ grande), la Ganancia de Kalman se vuelve pequeña → confiar más en la predicción.
* Si el modelo es **incierto** ($Q$ grande), la Ganancia de Kalman aumenta → confiar más en las mediciones.
* Con el tiempo, encuentra el **equilibrio óptimo** entre confiar en el modelo y confiar en los sensores.

---

# 7. Variantes

* **Filtro de Kalman Extendido (EKF):** Para sistemas no lineales, utiliza linealización (Jacobiano).
* **Filtro de Kalman Unscented (UKF):** Para sistemas no lineales, utiliza muestreo determinista.
* **Filtro de Información:** Trabaja con covarianza inversa para mayor eficiencia.
* **Filtro de Kalman por Conjuntos:** Utilizado en pronósticos del tiempo y sistemas de alta dimensión.

---

# 8. Aplicaciones

* **Navegación:** Fusión de GPS + acelerómetro para el seguimiento de posición.
* **Robótica:** SLAM (Localización y Mapeo Simultáneos).
* **Finanzas:** Estimación de variables ocultas como la volatilidad.
* **Visión por Computadora:** Seguimiento de objetos en videos.
* **Sistemas de Control:** Estabilización de aeronaves y naves espaciales.

---

# 9. Ejemplo de Escenario

Imagina un coche autónomo estimando su posición:

* El modelo predice la posición usando la velocidad + el estado anterior.
* El GPS proporciona una medición ruidosa de la posición.
* El filtro de Kalman combina la predicción y el GPS para obtener una posición más suave y precisa.

Con el tiempo, el coche puede rastrear su ubicación incluso si el GPS se interrumbre brevemente.

---

# 10. Fortalezas y Limitaciones Clave

**Fortalezas:**

* Recursivo, eficiente (solo necesita el último estado, no toda la historia).
* Óptimo para sistemas lineales gaussianos.
* Ampliamente probado y robusto.

**Limitaciones:**

* Requiere modelos precisos de la dinámica y el ruido.
* Puramente lineal — los casos no lineales necesitan EKF/UKF.
* Puede divergir si se violan las suposiciones.

---

✅ En resumen: El **filtro de Kalman** es una forma matemáticamente elegante de fusionar predicciones y mediciones bajo incertidumbre, equilibrando la confianza entre modelos y sensores para producir la mejor estimación posible en tiempo real.

---

¿Te gustaría que también te diera un **ejemplo de implementación paso a paso en Python** (como rastrear posición con ruido), para que puedas ver cómo funciona en la práctica?