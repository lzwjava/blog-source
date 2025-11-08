---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Presentación de las Máquinas de Potenciación del Gradiente
translated: true
type: note
---

### Resumen
El artículo de 2001 *"Greedy Function Approximation: A Gradient Boosting Machine"* de Jerome H. Friedman presenta las Máquinas de Potenciación del Gradiente (GBMs), un potente método de aprendizaje conjunto para tareas supervisadas como regresión y clasificación. Enmarca el boosting como una forma de descenso de gradiente funcional, donde aprendices "débiles" simples (a menudo árboles de decisión) se añaden secuencialmente a un modelo aditivo para minimizar una función de pérdida especificada. Este enfoque generaliza algoritmos de boosting anteriores (por ejemplo, AdaBoost) y enfatiza la optimización greedy en el espacio de funciones, lo que conduce a modelos muy precisos, robustos e interpretables.

### Abstract (Parafraseado)
Las GBMs construyen modelos predictivos flexibles combinando aprendices débiles de forma secuencial y aditiva para aproximar el minimizador de una función de pérdida diferenciable. El uso de árboles de regresión como aprendices base produce procedimientos competitivos y robustos para regresión y clasificación. El método supera a alternativas como multivariate adaptive regression splines (MARS) en pruebas empíricas, con bajas tasas de error en diversos conjuntos de datos.

### Métodos Clave
La idea central es ajustar iterativamente nuevos aprendices al *gradiente negativo* (pseudo-residuales) de la pérdida con respecto a las predicciones del modelo actual, imitando el descenso de gradiente en el espacio de funciones.

- **Estructura del Modelo**: El modelo final es \\( F_M(x) = \sum_{m=1}^M \beta_m h_m(x) \\), donde cada \\( h_m(x) \\) es un aprendiz débil (por ejemplo, un pequeño árbol de regresión).
- **Regla de Actualización**: En la iteración \\( m \\), calcular los residuales \\( r_{im} = -\left[ \frac{\partial L(y_i, F(x_i))}{\partial F(x_i)} \right]_{F=F_{m-1}} \\), luego ajustar \\( h_m \\) a estos residuales mediante mínimos cuadrados. El tamaño del paso \\( \gamma_m \\) se optimiza mediante búsqueda en línea: \\( \gamma_m = \arg\min_\gamma \sum_i L(y_i, F_{m-1}(x_i) + \gamma h_m(x_i)) \\).
- **Contracción (Shrinkage)**: Escalar las adiciones por \\( \nu \in (0,1] \\) (por ejemplo, \\( \nu = 0.1 \\)) para reducir el sobreajuste y permitir más iteraciones.
- **Variante Estocástica**: Submuestrear los datos (por ejemplo, 50%) en cada paso para un entrenamiento más rápido y una mejor generalización.
- **Algoritmo TreeBoost** (Esquema del Pseudocódigo):
  1. Inicializar \\( F_0(x) \\) como la constante que minimiza la pérdida.
  2. Para \\( m = 1 \\) a \\( M \\):
     - Calcular pseudo-residuales \\( r_{im} \\).
     - Ajustar el árbol \\( h_m \\) a \\( \{ (x_i, r_{im}) \} \\).
     - Encontrar el \\( \gamma_m \\) óptimo mediante búsqueda en línea.
     - Actualizar \\( F_m(x) = F_{m-1}(x) + \nu \gamma_m h_m(x) \\).
  3. Parar basándose en iteraciones o mejora de la pérdida.

Las pérdidas soportadas incluyen:
- Mínimos cuadrados (regresión): \\( L(y, F) = \frac{1}{2}(y - F)^2 \\), residuales = \\( y - F \\).
- Desviación absoluta mínima (regresión robusta): \\( L(y, F) = |y - F| \\).
- Log-verosimilitud (clasificación binaria): \\( L = -\sum [y \log p + (1-y) \log(1-p)] \\), con \\( p = \frac{1}{1 + e^{-F}} \\); residuales = \\( y - p \\).
- Pérdida de Huber (robusta a valores atípicos).

Variantes como LogitBoost adaptan esto para pérdidas específicas (por ejemplo, la desviación binomial).

### Contribuciones
- **Marco Unificado**: Extiende el boosting a cualquier pérdida diferenciable mediante gradientes, unificando AdaBoost (pérdida exponencial) y LogitBoost.
- **Mejoras Prácticas**: Introduce la contracción (shrinkage) y el submuestreo estocástico para un mejor control del sobreajuste y la computación.
- **Flexibilidad**: Funciona con varios aprendices base y tareas (regresión, clasificación, ranking); los árboles permiten manejar datos de alta dimensión de manera eficiente.
- **Herramientas de Interpretabilidad**: Discute la importancia de las variables (mediante la reducción total de impureza) y los gráficos de dependencia parcial.

### Hallazgos Principales
- **Rendimiento**: Las GBMs sobresalen empíricamente, reduciendo las tasas de error entre un 10-50% respecto a líneas base como árboles simples, bagging, redes neuronales y MARS en conjuntos de datos del mundo real (por ejemplo, finanzas, simulaciones de física).
- **Robustez**: La GBM estocástica converge más rápido; árboles más profundos (6-8 niveles) aumentan la precisión pero necesitan regularización. Las pérdidas LAD/Huber mitigan mejor los valores atípicos que los mínimos cuadrados.
- **Eficiencia**: Rápido para datos grandes; las configuraciones óptimas usan \\( \nu = 0.1 \\), 1000+ iteraciones y submuestreo.
- Los gráficos muestran una rápida convergencia de la pérdida y una varianza/ sesgo bajos en comparación con las alternativas.

Este artículo sentó las bases para implementaciones modernas como XGBoost y LightGBM.

### Referencias
- [Greedy Function Approximation: A Gradient Boosting Machine (PDF)](https://jerryfriedman.su.domains/ftp/trebst.pdf)