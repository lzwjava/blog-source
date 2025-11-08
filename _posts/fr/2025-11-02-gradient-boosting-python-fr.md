---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Exemple Fondamental de Boosting par Gradient en Python
translated: true
type: note
---

### Exemple simple de Gradient Boosting en Python

Voici un exemple basique utilisant `GradientBoostingRegressor` de scikit-learn pour implémenter la machine à gradient boosting de Friedman sur un jeu de données de régression synthétique. Cela reflète les idées principales du document de 2001 : l'ajustement séquentiel d'arbres sur les pseudo-résidus, avec un taux d'apprentissage pour la régularisation.

```python
import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Étape 1 : Générer des données synthétiques (comme les exemples de régression dans le document)
X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Étape 2 : Initialiser et entraîner le GBM
# Paramètres clés inspirés du document : n_estimators=1000 (nombreuses itérations), learning_rate=0.1 (taux d'apprentissage),
# max_depth=3 (arbres peu profonds pour les apprenants faibles), subsample=0.5 (variante stochastique)
gbm = GradientBoostingRegressor(
    n_estimators=1000,
    learning_rate=0.1,
    max_depth=3,
    subsample=0.5,
    random_state=42
)
gbm.fit(X_train, y_train)

# Étape 3 : Prédire et évaluer
y_pred = gbm.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Test MSE: {mse:.4f}")

# Étape 4 : Tracer l'importance des caractéristiques (de la section sur l'interprétabilité du document)
importances = gbm.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(8, 5))
plt.title("Importance des caractéristiques")
plt.bar(range(X.shape[1]), importances[indices])
plt.xticks(range(X.shape[1]), [f'Caractéristique {i}' for i in indices], rotation=45)
plt.tight_layout()
plt.show()

# Optionnel : Tracer la courbe d'apprentissage (perte vs. itérations)
test_score = np.zeros((gbm.n_estimators,), dtype=np.float64)
for i, y_pred in enumerate(gbm.staged_predict(X_test)):
    test_score[i] = gbm.loss_(y_test, y_pred)
plt.figure(figsize=(8, 5))
plt.title("Déviance (Perte) vs. Nombre d'itérations de boosting")
plt.plot(test_score, label="Déviance sur le test")
plt.xlabel("Nombre d'itérations")
plt.ylabel("Déviance")
plt.legend()
plt.show()
```

### Comment cela fonctionne (lié au document)
- **Données** : Données de régression synthétiques avec du bruit, similaires aux tests empiriques du document.
- **Modèle** : Utilise la perte des moindres carrés par défaut, ajustant les arbres aux gradients négatifs (résidus).
- **Entraînement** : Ajout séquentiel d'arbres avec un taux d'apprentissage (`learning_rate=0.1`) pour éviter le surapprentissage, comme recommandé.
- **Évaluation** : Le MSE correspond à l'accent mis par le document sur l'erreur quadratique ; les graphiques montrent la convergence et l'importance (réduction totale de l'impureté).
- **Exécution** : Copiez-collez dans un notebook Jupyter ou un script Python. Nécessite `scikit-learn` et `matplotlib`.

Ceci est un point de départ pratique — l'implémentation de scikit-learn suit de près l'algorithme de Friedman. Pour une version à partir de zéro, faites-le moi savoir !

[Documentation scikit-learn sur le Gradient Boosting](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)