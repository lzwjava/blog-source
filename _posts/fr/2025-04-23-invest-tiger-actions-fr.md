---
audio: true
generated: false
image: false
lang: fr
layout: post
title: Investissements hebdomadaires en actions avec l'API TigerOpen
translated: true
---

J'ai développé un script Python et un workflow GitHub Actions pour automatiser ma stratégie d'investissement hebdomadaire, achetant une action NVIDIA chaque mercredi à 22h35 en heure normale de Chine (CST). J'ai choisi les mercredis car, en 2025, il n'y a pas de jours fériés ce jour-là, assurant une exécution cohérente.

## Aperçu

Le script utilise l'API TigerOpen pour passer une commande de marché pour les actions NVIDIA et surveille son statut. Le workflow GitHub Actions exécute le script selon un planning, gérant la configuration et l'authentification de manière sécurisée. Voici les détails des deux composants.

## Script Python

Ce script passe une commande d'achat pour une action NVIDIA, vérifie son statut pendant jusqu'à 60 secondes, et l'annule si elle n'est pas exécutée.

```python
import time
import os
from tigeropen.common.consts import Language, OrderStatus
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.common.util.signature_utils import read_private_key
from tigeropen.trade.trade_client import TradeClient
from tigeropen.common.util.order_utils import market_order
from tigeropen.common.util.contract_utils import stock_contract

def get_client_config(sandbox=False):
    client_config = TigerOpenClientConfig(sandbox_debug=sandbox)
    client_config.private_key = read_private_key(os.environ.get('TIGER_PEM'))
    client_config.tiger_id = os.environ.get('TIGER_TIGER_ID')
    client_config.account = os.environ.get('TIGER_ACCOUNT')
    client_config.language = Language.zh_CN
    return client_config

# Fonction pour passer une commande
def place_order():
    client_config = get_client_config()
    trade_client = TradeClient(client_config)
    account = client_config.account  # Stocker le compte pour une utilisation ultérieure

    contract = stock_contract(symbol='NVDA', currency='USD')
    stock_order = market_order(
        account=account, contract=contract, action='BUY', quantity=1
    )
    # Passer la commande
    order_id = trade_client.place_order(stock_order)
    print(f"Commande passée avec l'ID: {order_id}")

    # Suivre le temps
    start_time = time.time()
    while time.time() - start_time < 60:  # Délai d'attente de 1 minute
        # Obtenir la commande et trouver celle que nous venons de passer
        order = trade_client.get_order(id=order_id)
        if str(order.id) == str(order_id):
            print(f"ID de la commande correspondante! Vérification du statut de la commande: {order.status}")
            # Vérifier le statut de la commande en utilisant les valeurs de l'énumération OrderStatus
            if order.status == OrderStatus.FILLED:
                print("Commande complétée avec succès.")
                return
            elif order.status == OrderStatus.REJECTED:
                print(f"Commande rejetée: {order_id}")
                raise Exception(f"La commande {order_id} a été rejetée")
            elif order.status in [
                OrderStatus.PENDING_NEW,
                OrderStatus.NEW,
                OrderStatus.HELD,
                OrderStatus.PENDING_CANCEL
            ]:
                print(f"La commande est en attente, statut: {order.status}")
            else:
                print(f"Le statut de la commande est: {order.status}")

        # Pause avant de vérifier à nouveau
        time.sleep(5)  # Vérifier toutes les 5 secondes

    # Si la commande n'est pas complétée en 1 minute, l'annuler
    print("La commande n'a pas été complétée en 1 minute. Annulation de la commande.")
    trade_client.cancel_order(id=order_id)
    print(f"Commande annulée: {order_id}")

if __name__ == '__main__':
    place_order()
```

## Workflow GitHub Actions

Le workflow s'exécute tous les mercredis à 14h35 UTC (22h35 UTC) et configure l'environnement, installe les dépendances et exécute le script.

```yaml
name: Investissement Régulier

on:
  schedule:
    - cron: '35 14 * * 3'  # S'exécute tous les mercredis à 14h35 UTC
  workflow_dispatch:

concurrency:
  group: 'trading'
  cancel-in-progress: false

permissions:
  id-token: write
  contents: write
  pages: write

jobs:
  invest:
    runs-on: ubuntu-latest
    steps:
      - name: Vérifier le dépôt
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Configurer Python 3.13.2
        uses: actions/setup-python@v4
        with:
          python-version: "3.13.2"

      - name: Installer les dépendances
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Configurer le fichier PEM Tiger
        run: |
          echo "${{ secrets.TIGER_PEM_CONTENT }}" > tiger.pem
          chmod 600 tiger.pem

      - name: Exécuter le script Tiger
        id: tiger_update
        run: python invest.py
        env:
          TIGER_TIGER_ID: ${{ secrets.TIGER_TIGER_ID }}
          TIGER_ACCOUNT: ${{ secrets.TIGER_ACCOUNT }}
          TIGER_PEM: "tiger.pem"
```