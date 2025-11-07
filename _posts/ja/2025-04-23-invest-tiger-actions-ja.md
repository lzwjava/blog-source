---
audio: true
generated: false
image: false
lang: ja
layout: post
title: 週次株式投資 TigerOpen API
translated: true
type: post
---

私は、毎週水曜日の22時35分（中国標準時、CST）にNVIDIA株を1株購入する投資戦略を自動化するためのPythonスクリプトとGitHub Actionsワークフローを開発しました。2025年には水曜日に祝日がないため、一貫した実行を確保するために水曜日に設定しました。

## 概要

このスクリプトは、TigerOpen APIを使用してNVIDIA株の市場注文を出し、その状態を監視します。GitHub Actionsワークフローは、スクリプトをスケジュールに従って実行し、セットアップと認証を安全に処理します。以下に、両方のコンポーネントの詳細を示します。

## Pythonスクリプト

このスクリプトは、NVIDIA株を1株購入する注文を出し、60秒間その状態を確認し、埋まらなかった場合はキャンセルします。

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

# 注文を出す関数
def place_order():
    client_config = get_client_config()
    trade_client = TradeClient(client_config)
    account = client_config.account  # 後で使用するためにアカウントを保存

    contract = stock_contract(symbol='NVDA', currency='USD')
    stock_order = market_order(
        account=account, contract=contract, action='BUY', quantity=1
    )
    # 注文を出す
    order_id = trade_client.place_order(stock_order)
    print(f"注文ID: {order_id} で注文が出されました")

    # 時間を追跡
    start_time = time.time()
    while time.time() - start_time < 60:  # 1分タイムアウト
        # 注文を取得し、先ほど出したものを見つける
        order = trade_client.get_order(id=order_id)
        if str(order.id) == str(order_id):
            print(f"注文IDが一致しました！注文状態を確認中: {order.status}")
            # OrderStatus列挙値を使用して注文状態を確認
            if order.status == OrderStatus.FILLED:
                print("注文が正常に完了しました。")
                return
            elif order.status == OrderStatus.REJECTED:
                print(f"注文が拒否されました: {order_id}")
                raise Exception(f"注文 {order_id} が拒否されました")
            elif order.status in [
                OrderStatus.PENDING_NEW,
                OrderStatus.NEW,
                OrderStatus.HELD,
                OrderStatus.PENDING_CANCEL
            ]:
                print(f"注文が保留中です、状態: {order.status}")
            else:
                print(f"注文状態は: {order.status}")

        # 再度確認する前に待機
        time.sleep(5)  # 5秒ごとに確認

    # 注文が1分以内に完了しない場合はキャンセル
    print("注文が1分以内に完了しませんでした。注文をキャンセルします。")
    trade_client.cancel_order(id=order_id)
    print(f"注文がキャンセルされました: {order_id}")

if __name__ == '__main__':
    place_order()
```

## GitHub Actionsワークフロー

このワークフローは、毎週水曜日の14:35 UTC（22:35 UTC）に実行され、環境をセットアップし、依存関係をインストールし、スクリプトを実行します。

```yaml
name: 定期投資

on:
  schedule:
    - cron: '35 14 * * 3'  # 毎週水曜日の14:35 UTCに実行
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
      - name: リポジトリをチェックアウト
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Python 3.13.2をセットアップ
        uses: actions/setup-python@v4
        with:
          python-version: "3.13.2"

      - name: 依存関係をインストール
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Tiger PEMファイルをセットアップ
        run: |
          echo "${{ secrets.TIGER_PEM_CONTENT }}" > tiger.pem
          chmod 600 tiger.pem

      - name: Tigerスクリプトを実行
        id: tiger_update
        run: python invest.py
        env:
          TIGER_TIGER_ID: ${{ secrets.TIGER_TIGER_ID }}
          TIGER_ACCOUNT: ${{ secrets.TIGER_ACCOUNT }}
          TIGER_PEM: "tiger.pem"
```