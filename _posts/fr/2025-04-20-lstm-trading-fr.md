---
audio: false
generated: true
lang: fr
layout: post
title: Intégration des données historiques avec les LSTM
translated: true
type: note
---

Combiner les données historiques du marché boursier de l'API TigerOpen avec un modèle LSTM pour l'analyse est réalisable et constitue une approche courante dans la prédiction des séries temporelles financières. Le second script récupère les données historiques du marché boursier (par exemple, les barres OHLCV), qui peuvent être utilisées pour construire un ensemble de données pour entraîner un modèle LSTM similaire à celui du premier script. Ci-dessous, je décris comment vous pouvez intégrer ces deux éléments, aborder les défis potentiels et fournir une approche de haut niveau pour analyser les données boursières à l'aide d'un LSTM.

### Approche de Haut Niveau pour Combiner les Deux

1.  **Récupérer les Données Historiques** :
    - Utilisez la fonction `get_history_data` du second script pour récupérer les données historiques du marché boursier (par exemple, pour le symbole '00700' ou d'autres).
    - Les données incluent les prix d'ouverture, haut, bas, de clôture, le volume et les horodatages, qui peuvent être utilisés comme caractéristiques pour le LSTM.

2.  **Prétraiter les Données pour le LSTM** :
    - Convertissez les données historiques dans un format adapté au modèle LSTM. Cela implique :
        - La normalisation des données (par exemple, mettre à l'échelle les prix et les volumes sur [0, 1]).
        - La création de séquences de données historiques (par exemple, utiliser les 60 derniers jours pour prédire le prix de clôture du jour suivant).
        - L'encodage des caractéristiques (par exemple, prix de clôture, volume) dans un format tensoriel compatible avec l'entrée du LSTM.

3.  **Adapter le Modèle LSTM** :
    - Modifiez la classe `Net` du premier script pour qu'elle gère les données de séries temporelles financières au lieu de séquences de texte.
    - Ajustez la taille d'entrée pour qu'elle corresponde au nombre de caractéristiques (par exemple, prix de clôture, volume, etc.) au lieu de `vocab_size`.
    - Mettez à jour la couche de sortie pour prédire une valeur continue (par exemple, le prix de clôture du jour suivant) ou une classification (par exemple, augmentation/diminution du prix).

4.  **Entraîner le Modèle** :
    - Divisez les données historiques en ensembles d'entraînement, de validation et de test.
    - Entraînez le LSTM en utilisant les données prétraitées, de manière similaire à la boucle d'entraînement du premier script.
    - Utilisez une fonction de perte comme l'Erreur Quadratique Moyenne (MSE) pour les tâches de régression ou la Perte d'Entropie Croisée pour la classification.

5.  **Analyser et Prédire** :
    - Utilisez le LSTM entraîné pour prédire les futurs prix du marché boursier ou les tendances basées sur des données historiques récentes.
    - Visualisez les prédictions parallèlement aux données réelles en utilisant `matplotlib`.

6.  **Intégrer avec le Trading** :
    - Utilisez les prédictions pour éclairer les décisions de trading dans la fonction `place_order`.
    - Par exemple, passez un ordre d'achat si le LSTM prédit une augmentation de prix supérieure à un certain seuil.

### Exemple de Code : Combiner les Données Historiques avec le LSTM

Ci-dessous un extrait de code exemple qui intègre les deux scripts, en se concentrant sur le prétraitement des données historiques et l'adaptation du LSTM pour la prédiction du prix des actions.

```python
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tigeropen.common.consts import Language, Market, BarPeriod, QuoteRight
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.common.util.signature_utils import read_private_key
import os
from datetime import datetime

# --- Configuration de l'API TigerOpen ---
def get_client_config(sandbox=False):
    client_config = TigerOpenClientConfig(sandbox_debug=sandbox)
    client_config.private_key = read_private_key(os.environ.get('TIGER_PEM'))
    client_config.tiger_id = os.environ.get('TIGER_TIGER_ID')
    client_config.account = os.environ.get('TIGER_ACCOUNT')
    client_config.language = Language.zh_CN
    return client_config

def get_history_data(symbol='00700', period=BarPeriod.DAY, begin_time='2024-01-01', end_time=None, limit=100):
    client_config = get_client_config()
    quote_client = QuoteClient(client_config)
    if not end_time:
        end_time = datetime.now().strftime('%Y-%m-%d')
    bars_dict = quote_client.get_bars(
        symbols=[symbol], period=period, begin_time=begin_time, end_time=end_time, limit=limit, right=QuoteRight.BR
    )
    bars = bars_dict.get(symbol, [])
    return pd.DataFrame([{
        'time': bar.time,
        'open': bar.open,
        'high': bar.high,
        'low': bar.low,
        'close': bar.close,
        'volume': bar.volume
    } for bar in bars])

# --- Modèle LSTM ---
class StockLSTM(nn.Module):
    def __init__(self, input_size, hidden_size=50, num_layers=1):
        super(StockLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, bidirectional=False)
        self.l_out = nn.Linear(in_features=hidden_size, out_features=1)  # Prédire le prochain prix de clôture

    def forward(self, x):
        x, (h, c) = self.lstm(x)
        x = x[:, -1, :]  # Prendre le dernier pas de temps
        x = self.l_out(x)
        return x

# --- Prétraitement des Données ---
def prepare_data(df, sequence_length=60, target_col='close'):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[[target_col]].values)
    
    X, y = [], []
    for i in range(len(scaled_data) - sequence_length):
        X.append(scaled_data[i:i + sequence_length])
        y.append(scaled_data[i + sequence_length])
    
    X = np.array(X)
    y = np.array(y)
    
    # Diviser en entraînement et test
    train_size = int(0.8 * len(X))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    
    return torch.Tensor(X_train), torch.Tensor(y_train), torch.Tensor(X_test), torch.Tensor(y_test), scaler

# --- Boucle d'Entraînement ---
def train_model(model, X_train, y_train, X_test, y_test, num_epochs=50, lr=3e-4):
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    
    training_loss, validation_loss = [], []
    
    for epoch in range(num_epochs):
        model.train()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        training_loss.append(loss.item())
        
        model.eval()
        with torch.no_grad():
            val_outputs = model(X_test)
            val_loss = criterion(val_outputs, y_test)
            validation_loss.append(val_loss.item())
        
        if epoch % 5 == 0:
            print(f'Epoch {epoch}, Training Loss: {training_loss[-1]:.4f}, Validation Loss: {validation_loss[-1]:.4f}')
    
    return training_loss, validation_loss

# --- Exécution Principale ---
if __name__ == '__main__':
    # Récupérer les données historiques
    df = get_history_data(symbol='00700', limit=1000)
    
    # Préparer les données
    sequence_length = 60
    X_train, y_train, X_test, y_test, scaler = prepare_data(df, sequence_length=sequence_length, target_col='close')
    
    # Initialiser et entraîner le LSTM
    model = StockLSTM(input_size=1, hidden_size=50, num_layers=1)
    training_loss, validation_loss = train_model(model, X_train, y_train, X_test, y_test, num_epochs=50)
    
    # Tracer la perte d'entraînement et de validation
    plt.figure()
    plt.plot(training_loss, 'r', label='Perte d\'Entraînement')
    plt.plot(validation_loss, 'b', label='Perte de Validation')
    plt.legend()
    plt.xlabel('Epoch')
    plt.ylabel('Perte MSE')
    plt.show()
    
    # Faire des prédictions
    model.eval()
    with torch.no_grad():
        predicted = model(X_test).numpy()
    
    # Transformation inverse des prédictions
    predicted = scaler.inverse_transform(predicted)
    y_test_actual = scaler.inverse_transform(y_test.numpy())
    
    # Tracer les prédictions vs les valeurs réelles
    plt.figure()
    plt.plot(y_test_actual, 'b', label='Prix de Clôture Réel')
    plt.plot(predicted, 'r', label='Prix de Clôture Prédit')
    plt.legend()
    plt.xlabel('Temps')
    plt.ylabel('Prix de Clôture')
    plt.show()
```

### Modifications Clés et Notes

1.  **Récupération des Données** :
    - La fonction `get_history_data` est utilisée pour récupérer les données historiques du marché boursier pour un symbole donné (par exemple, '00700' pour Tencent).
    - Les données sont converties en un DataFrame pandas pour une manipulation facile.

2.  **Prétraitement** :
    - Les données sont normalisées en utilisant `MinMaxScaler` pour mettre à l'échelle les prix de clôture sur [0, 1].
    - Des séquences de `sequence_length` (par exemple, 60 jours) sont créées pour prédire le prix de clôture du jour suivant.
    - Les données sont divisées en ensembles d'entraînement (80 %) et de test (20 %).

3.  **Modèle LSTM** :
    - La classe `StockLSTM` est adaptée pour gérer une seule caractéristique (prix de clôture) ou plusieurs caractéristiques (par exemple, clôture, volume) en ajustant `input_size`.
    - La couche de sortie prédit une seule valeur (prix de clôture du jour suivant) en utilisant une couche linéaire.

4.  **Entraînement** :
    - La boucle d'entraînement utilise la perte MSE pour la régression, adaptée à la prédiction de valeurs continues comme les prix des actions.
    - Le modèle est évalué sur l'ensemble de test pour suivre la perte de validation.

5.  **Visualisation** :
    - Les pertes d'entraînement et de validation sont tracées pour évaluer la convergence du modèle.
    - Les prix de clôture prédits et réels sont tracés côte à côte pour évaluer la performance du modèle.

### Défis Potentiels et Considérations

1.  **Qualité et Quantité des Données** :
    - La quantité de données historiques (par exemple, `limit=1000` barres) peut être insuffisante pour un entraînement robuste du LSTM. Envisagez de récupérer plus de données ou d'utiliser une `sequence_length` plus petite.
    - Les données boursières peuvent être bruyantes, et les modèles LSTM peuvent avoir du mal avec les dépendances à long terme ou les changements soudains du marché.

2.  **Ingénierie des Caractéristiques** :
    - L'exemple n'utilise que le prix de clôture. Inclure des caractéristiques supplémentaires (par exemple, volume, moyennes mobiles, indicateurs techniques comme le RSI) peut améliorer la performance du modèle.
    - La sélection des caractéristiques et le prétraitement (par exemple, gestion des données manquantes, valeurs aberrantes) sont critiques.

3.  **Complexité du Modèle** :
    - L'architecture LSTM est simple (1 couche, 50 unités cachées). Pour des données financières complexes, envisagez des modèles plus profonds, du dropout pour la régularisation, ou d'autres architectures comme GRU ou Transformer.

4.  **Sur-apprentissage** :
    - Surveillez la perte d'entraînement par rapport à la perte de validation pour détecter le sur-apprentissage. Ajoutez du dropout ou une décroissance de poids si nécessaire.

5.  **Intégration en Temps Réel** :
    - Pour utiliser le modèle pour le trading en temps réel, récupérez les données récentes, prétraitez-les et injectez-les dans le LSTM entraîné pour générer des prédictions.
    - Combinez les prédictions avec une stratégie de trading (par exemple, acheter si le prix prédit > prix actuel de X %).

6.  **Limitations de l'API** :
    - Assurez-vous que vos identifiants API TigerOpen sont correctement définis dans les variables d'environnement (`TIGER_PEM`, `TIGER_TIGER_ID`, `TIGER_ACCOUNT`).
    - Soyez conscient des limites de débit de l'API et de la disponibilité des données pour certains symboles ou périodes.

### Exemple de Sortie
En supposant que le code s'exécute avec succès, vous pourriez voir :
- Une sortie console affichant la perte d'entraînement et de validation par époque (par exemple, `Epoch 0, Training Loss: 0.1234, Validation Loss: 0.1345`).
- Un graphique de la perte d'entraînement et de validation sur les époques, indiquant la convergence.
- Un graphique comparant les prix de clôture prédits et réels pour l'ensemble de test, montrant dans quelle mesure le LSTM capture les tendances.

### Prochaines Étapes
-   **Améliorer les Caractéristiques** : Intégrez des indicateurs techniques (par exemple, MACD, Bandes de Bollinger) ou des données de sentiment des posts X (si disponibles via la recherche).
-   **Backtesting** : Testez les prédictions du LSTM dans un environnement de trading simulé en utilisant des données historiques pour évaluer la rentabilité.
-   **Intégration au Trading** : Utilisez la fonction `place_order` pour exécuter des trades basés sur les prédictions du LSTM, avec une gestion des risques appropriée.
-   **Réglage des Hyperparamètres** : Expérimentez avec `sequence_length`, `hidden_size`, `num_layers` et le taux d'apprentissage pour optimiser les performances.

### Est-ce que Cela Fonctionnerait ?
Oui, combiner les données historiques du marché boursier avec un LSTM pour l'analyse est une approche viable, largement utilisée dans le trading algorithmique. Cependant, le succès dépend de :
- Données suffisantes et propres.
- Un prétraitement et une ingénierie des caractéristiques appropriés.
- Un modèle LSTM bien réglé.
- Une stratégie de trading robuste pour agir sur les prédictions.

Les marchés financiers sont intrinsèquement bruyants et influencés par des facteurs externes (par exemple, les actualités, les événements macroéconomiques), donc les prédictions LSTM doivent être utilisées avec prudence, idéalement dans le cadre d'une stratégie plus large avec des contrôles de risque.

Si vous souhaitez approfondir une partie (par exemple, ajouter des caractéristiques, backtesting, ou trading en temps réel), faites-le moi savoir !