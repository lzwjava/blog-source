---
audio: true
generated: false
image: false
lang: de
layout: post
title: Wöchentliche Aktieninvestitionen mit TigerOpen API
translated: true
type: post
---

Ich habe ein Python-Skript und einen GitHub Actions Workflow entwickelt, um meine wöchentliche Investitionsstrategie zu automatisieren, indem ich jeden Mittwoch um 22:35 Uhr China Standard Time (CST) eine NVIDIA-Aktie kaufe. Ich habe Mittwoch gewählt, weil es im Jahr 2025 an diesem Tag keine Feiertage gibt, was eine konsistente Ausführung gewährleistet.

## Übersicht

Das Skript verwendet die TigerOpen API, um eine Marktorder für NVIDIA-Aktien zu platzieren und deren Status zu überwachen. Der GitHub Actions Workflow führt das Skript nach einem Zeitplan aus, wobei die Einrichtung und Authentifizierung sicher gehandhabt werden. Im Folgenden finden Sie die Details beider Komponenten.

## Python-Skript

Dieses Skript platziert eine Kauforder für eine NVIDIA-Aktie, überprüft deren Status für bis zu 60 Sekunden und storniert sie, wenn sie nicht ausgeführt wird.

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

# Funktion zum Platzieren einer Order
def place_order():
    client_config = get_client_config()
    trade_client = TradeClient(client_config)
    account = client_config.account  # Konto für späteren Gebrauch speichern

    contract = stock_contract(symbol='NVDA', currency='USD')
    stock_order = market_order(
        account=account, contract=contract, action='BUY', quantity=1
    )
    # Order platzieren
    order_id = trade_client.place_order(stock_order)
    print(f"Order mit ID: {order_id} platziert")

    # Zeit verfolgen
    start_time = time.time()
    while time.time() - start_time < 60:  # 1-Minuten-Timeout
        # Order abrufen und diejenige finden, die wir gerade platziert haben
        order = trade_client.get_order(id=order_id)
        if str(order.id) == str(order_id):
            print(f"Order-ID übereinstimmend! Überprüfung des Order-Status: {order.status}")
            # Überprüfung des Order-Status mit den Enum-Werten von OrderStatus
            if order.status == OrderStatus.FILLED:
                print("Order erfolgreich abgeschlossen.")
                return
            elif order.status == OrderStatus.REJECTED:
                print(f"Order abgelehnt: {order_id}")
                raise Exception(f"Order {order_id} wurde abgelehnt")
            elif order.status in [
                OrderStatus.PENDING_NEW,
                OrderStatus.NEW,
                OrderStatus.HELD,
                OrderStatus.PENDING_CANCEL
            ]:
                print(f"Order ist ausstehend, Status: {order.status}")
            else:
                print(f"Order-Status ist: {order.status}")

        # Vor dem erneuten Überprüfen schlafen
        time.sleep(5)  # Jede 5 Sekunden überprüfen

    # Wenn die Order nicht innerhalb von 1 Minute abgeschlossen wird, stornieren
    print("Order nicht innerhalb von 1 Minute abgeschlossen. Order wird storniert.")
    trade_client.cancel_order(id=order_id)
    print(f"Order storniert: {order_id}")

if __name__ == '__main__':
    place_order()
```

## GitHub Actions Workflow

Der Workflow wird jeden Mittwoch um 14:35 Uhr UTC (22:35 Uhr UTC) ausgeführt und richtet die Umgebung ein, installiert Abhängigkeiten und führt das Skript aus.

```yaml
name: Regelmäßige Investition

on:
  schedule:
    - cron: '35 14 * * 3'  # Jeden Mittwoch um 14:35 Uhr UTC ausführen
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
      - name: Repository auschecken
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Python 3.13.2 einrichten
        uses: actions/setup-python@v4
        with:
          python-version: "3.13.2"

      - name: Abhängigkeiten installieren
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Tiger PEM-Datei einrichten
        run: |
          echo "${{ secrets.TIGER_PEM_CONTENT }}" > tiger.pem
          chmod 600 tiger.pem

      - name: Tiger-Skript ausführen
        id: tiger_update
        run: python invest.py
        env:
          TIGER_TIGER_ID: ${{ secrets.TIGER_TIGER_ID }}
          TIGER_ACCOUNT: ${{ secrets.TIGER_ACCOUNT }}
          TIGER_PEM: "tiger.pem"
```