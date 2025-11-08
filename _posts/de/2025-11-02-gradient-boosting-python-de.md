---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Grundlegendes Gradient Boosting Beispiel in Python
translated: true
type: note
---

### Einfaches Gradient Boosting-Beispiel in Python

Hier ist ein grundlegendes Beispiel, das scikit-learns `GradientBoostingRegressor` verwendet, um Friedmans Gradient Boosting Machine auf einem synthetischen Regressionsdatensatz zu implementieren. Dies spiegelt die Kernideen des Papers von 2001 wider: sequentielles Anpassen von Bäumen an Pseudo-Residuen, mit Shrinkage zur Regularisierung.

```python
import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Schritt 1: Synthetische Daten erzeugen (ähnlich den Regressionsbeispielen im Paper)
X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Schritt 2: GBM initialisieren und trainieren
# Wichtige Parameter, inspiriert vom Paper: n_estimators=1000 (viele Iterationen), learning_rate=0.1 (Shrinkage),
# max_depth=3 (flache Bäume für schwache Lernalgorithmen), subsample=0.5 (stochastische Variante)
gbm = GradientBoostingRegressor(
    n_estimators=1000,
    learning_rate=0.1,
    max_depth=3,
    subsample=0.5,
    random_state=42
)
gbm.fit(X_train, y_train)

# Schritt 3: Vorhersagen treffen und auswerten
y_pred = gbm.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Test MSE: {mse:.4f}")

# Schritt 4: Feature-Importance plotten (aus dem Interpretierbarkeitsabschnitt des Papers)
importances = gbm.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(8, 5))
plt.title("Feature Importances")
plt.bar(range(X.shape[1]), importances[indices])
plt.xticks(range(X.shape[1]), [f'Feature {i}' for i in indices], rotation=45)
plt.tight_layout()
plt.show()

# Optional: Lernkurve plotten (Loss vs. Iterationen)
test_score = np.zeros((gbm.n_estimators,), dtype=np.float64)
for i, y_pred in enumerate(gbm.staged_predict(X_test)):
    test_score[i] = gbm.loss_(y_test, y_pred)
plt.figure(figsize=(8, 5))
plt.title("Deviance (Loss) vs. Anzahl der Boosting-Iterationen")
plt.plot(test_score, label="Test Deviance")
plt.xlabel("Anzahl der Iterationen")
plt.ylabel("Deviance")
plt.legend()
plt.show()
```

### So funktioniert es (bezogen auf das Paper)
- **Daten**: Synthetische Regressionsdaten mit Rauschen, ähnlich den empirischen Tests im Paper.
- **Modell**: Verwendet standardmäßig den Least-Squares-Loss, passt Bäume an negative Gradienten (Residuen) an.
- **Training**: Sequentielles Hinzufügen von Bäumen mit Shrinkage (`learning_rate=0.1`), um Overfitting zu verhindern, wie empfohlen.
- **Evaluation**: MSE entspricht dem Fokus des Papers auf quadratische Fehler; Plots zeigen Konvergenz und Importance (Gesamtreduktion der Unreinheit).
- **Ausführen**: Kopiere den Code in ein Jupyter Notebook oder Python-Skript. Erfordert `scikit-learn` und `matplotlib`.

Dies ist ein praktischer Ausgangspunkt – scikit-learns Implementierung folgt eng Friedmans Algorithmus. Für eine Version von Grund auf, lass es mich wissen!

[scikit-learn Gradient Boosting Docs](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)