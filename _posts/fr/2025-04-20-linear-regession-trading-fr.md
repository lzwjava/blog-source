---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser la régression linéaire pour le trading
translated: true
type: note
---

Excellente question ! Vous combinez ici deux tâches :

1. **Récupérer des données historiques d'actions (par exemple, Tencent) en utilisant l'API TigerOpen**
2. **Utiliser ces données avec votre code de régression linéaire existant basé sur numpy**

---

## Est-ce que cela fonctionnera tel quel ?

**Non, pas directement.** Votre code de ML actuel s'attend à ce que `x_train` et `y_train` soient des tableaux numpy de valeurs numériques représentant des caractéristiques et des étiquettes (par exemple, la population par rapport au profit). Mais l'API TigerOpen renvoie des **barres historiques d'actions** (données OHLCV), qui sont une série temporelle avec plusieurs champs par horodatage.

Vous devez :

- Extraire et prétraiter correctement les données boursières pour obtenir des tableaux `x_train` et `y_train` adaptés.
- Adapter votre modèle et votre code au contexte des données boursières (par exemple, prédire le prix de clôture à partir des jours précédents).

---

## Comment adapter vos données boursières pour votre modèle de régression linéaire ?

### Étape 1 : Récupérer les données historiques pour Tencent (symbole `'00700'`)

```python
bars_dict = quote_client.get_bars(
    symbols=['00700'],
    period=BarPeriod.DAY,
    begin_time='2024-01-01',
    end_time=datetime.now().strftime('%Y-%m-%d'),
    limit=100,
    right=QuoteRight.BR
)

bars = bars_dict.get('00700', [])
```

### Étape 2 : Extraire les caractéristiques et les étiquettes

Une approche simple :

- Utiliser l'indice du jour comme `x_train` (par exemple, 0, 1, 2, ...)
- Utiliser le prix de clôture comme `y_train`

```python
import numpy as np

x_train = np.array([i for i in range(len(bars))])
y_train = np.array([bar.close for bar in bars])
```

Alternativement, vous pouvez utiliser le cours de clôture du jour précédent comme caractéristique pour prédire celui du jour suivant, ou des caractéristiques plus sophistiquées.

### Étape 3 : Utiliser votre code de régression linéaire

Maintenant, vos `x_train` et `y_train` sont des tableaux numpy de nombres, donc votre code devrait fonctionner correctement après avoir corrigé vos fonctions `compute_cost` et `compute_gradient` (qui renvoient actuellement zéro ou des gradients nuls).

---

## Exemple : Implémenter compute_cost et compute_gradient

```python
def compute_cost(x, y, w, b):
    m = x.shape[0]
    total_cost = 0.5 * np.sum((w * x + b - y) ** 2) / m
    return total_cost

def compute_gradient(x, y, w, b):
    m = x.shape[0]
    error = w * x + b - y
    dj_dw = np.sum(error * x) / m
    dj_db = np.sum(error) / m
    return dj_dw, dj_db
```

---

## Résumé

- Récupérez les données historiques boursières avec l'API TigerOpen
- Convertissez les données de séries temporelles en tableaux numériques (`x_train`, `y_train`)
- Implémentez ou corrigez vos fonctions de coût et de gradient
- Ensuite, votre code de descente de gradient et de tracé fonctionnera pour ajuster un modèle linéaire aux données de prix boursiers

---

## Bonus : Tracer les prix des actions

Votre nuage de points montrera le prix de clôture au fil des jours, et la ligne de régression ajustera une tendance.

---

Si vous le souhaitez, je peux vous aider à écrire un exemple complet intégrant la récupération de données TigerOpen avec votre code de régression linéaire numpy ! Il suffit de demander.