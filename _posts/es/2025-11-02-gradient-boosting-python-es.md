---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Ejemplo Básico de Potenciación del Gradiente en Python
translated: true
type: note
---

### Ejemplo Simple de Gradient Boosting en Python

Aquí hay un ejemplo básico que utiliza `GradientBoostingRegressor` de scikit-learn para implementar la Máquina de Gradient Boosting de Friedman en un conjunto de datos de regresión de juguete. Esto refleja las ideas centrales del artículo de 2001: ajuste secuencial de árboles a pseudo-residuos, con contracción (shrinkage) para regularización.

```python
import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Paso 1: Generar datos sintéticos (como los ejemplos de regresión en el artículo)
X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 2: Inicializar y entrenar el GBM
# Parámetros clave inspirados en el artículo: n_estimators=1000 (muchas iteraciones), learning_rate=0.1 (contracción),
# max_depth=3 (árboles superficiales para aprendices débiles), subsample=0.5 (variante estocástica)
gbm = GradientBoostingRegressor(
    n_estimators=1000,
    learning_rate=0.1,
    max_depth=3,
    subsample=0.5,
    random_state=42
)
gbm.fit(X_train, y_train)

# Paso 3: Predecir y evaluar
y_pred = gbm.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Test MSE: {mse:.4f}")

# Paso 4: Graficar la importancia de las características (de la sección de interpretabilidad del artículo)
importances = gbm.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(8, 5))
plt.title("Importancia de las Características")
plt.bar(range(X.shape[1]), importances[indices])
plt.xticks(range(X.shape[1]), [f'Característica {i}' for i in indices], rotation=45)
plt.tight_layout()
plt.show()

# Opcional: Graficar la curva de aprendizaje (pérdida vs. iteraciones)
test_score = np.zeros((gbm.n_estimators,), dtype=np.float64)
for i, y_pred in enumerate(gbm.staged_predict(X_test)):
    test_score[i] = gbm.loss_(y_test, y_pred)
plt.figure(figsize=(8, 5))
plt.title("Desviación (Pérdida) vs. Número de Iteraciones de Boosting")
plt.plot(test_score, label="Desviación en Test")
plt.xlabel("Número de Iteraciones")
plt.ylabel("Desviación")
plt.legend()
plt.show()
```

### Cómo Funciona (Vinculado al Artículo)
- **Datos**: Datos de regresión sintéticos con ruido, similares a las pruebas empíricas del artículo.
- **Modelo**: Utiliza la pérdida por mínimos cuadrados por defecto, ajustando árboles a los gradientes negativos (residuos).
- **Entrenamiento**: Adición secuencial de árboles con contracción (`learning_rate=0.1`) para prevenir el sobreajuste, como se recomienda.
- **Evaluación**: El MSE coincide con el enfoque del artículo en el error cuadrático; los gráficos muestran la convergencia y la importancia (reducción total de impureza).
- **Ejecútalo**: Copia y pega en un cuaderno de Jupyter o en un script de Python. Requiere `scikit-learn` y `matplotlib`.

Este es un punto de partida práctico: la implementación de scikit-learn sigue de cerca el algoritmo de Friedman. Para una versión desde cero, ¡avísame!

[Documentación de Gradient Boosting en scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)