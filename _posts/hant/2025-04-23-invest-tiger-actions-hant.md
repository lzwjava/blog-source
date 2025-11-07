---
audio: true
generated: false
image: false
lang: hant
layout: post
title: 每週股票投資與TigerOpen API
translated: true
type: post
---

我開發了一個 Python 腳本和一個 GitHub Actions 工作流程來自動化我的每週投資策略，每週三晚上十時三十五分中國標準時間 (CST) 購買一隻 NVIDIA 股票。我選擇週三是因為在 2025 年，該日沒有假期，確保一致執行。

## 概述

這個腳本使用 TigerOpen API 來下單 NVIDIA 股票市場訂單，並監控其狀態。GitHub Actions 工作流程按計劃運行腳本，安全地處理設置和驗證。以下是兩個組件的詳細資料。

## Python 腳本

這個腳本下單購買一隻 NVIDIA 股票，檢查其狀態最多 60 秒，如果未成交則取消。

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

# 下單函數
def place_order():
    client_config = get_client_config()
    trade_client = TradeClient(client_config)
    account = client_config.account  # 存儲帳戶以供後續使用

    contract = stock_contract(symbol='NVDA', currency='USD')
    stock_order = market_order(
        account=account, contract=contract, action='BUY', quantity=1
    )
    # 下單
    order_id = trade_client.place_order(stock_order)
    print(f"已下單，訂單編號: {order_id}")

    # 追蹤時間
    start_time = time.time()
    while time.time() - start_time < 60:  # 1 分鐘超時
        # 获取訂單並找到我們剛剛下的訂單
        order = trade_client.get_order(id=order_id)
        if str(order.id) == str(order_id):
            print(f"訂單編號匹配！檢查訂單狀態: {order.status}")
            # 使用 OrderStatus 枚舉值檢查訂單狀態
            if order.status == OrderStatus.FILLED:
                print("訂單成功完成。")
                return
            elif order.status == OrderStatus.REJECTED:
                print(f"訂單被拒絕: {order_id}")
                raise Exception(f"訂單 {order_id} 被拒絕")
            elif order.status in [
                OrderStatus.PENDING_NEW,
                OrderStatus.NEW,
                OrderStatus.HELD,
                OrderStatus.PENDING_CANCEL
            ]:
                print(f"訂單正在處理中，狀態: {order.status}")
            else:
                print(f"訂單狀態是: {order.status}")

        # 等待後再檢查
        time.sleep(5)  # 每 5 秒檢查一次

    # 如果訂單在 1 分鐘內未完成，則取消訂單
    print("訂單在 1 分鐘內未完成。取消訂單。")
    trade_client.cancel_order(id=order_id)
    print(f"訂單已取消: {order_id}")

if __name__ == '__main__':
    place_order()
```

## GitHub Actions 工作流程

這個工作流程每週三 14:35 UTC (10:35 PM UTC) 運行一次，設置環境，安裝依賴項，並執行腳本。

```yaml
name: Regular Invest

on:
  schedule:
    - cron: '35 14 * * 3'  # 每週三 14:35 UTC 運行
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
      - name: 檢查存儲庫
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: 設置 Python 3.13.2
        uses: actions/setup-python@v4
        with:
          python-version: "3.13.2"

      - name: 安裝依賴項
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: 設置 Tiger PEM 文件
        run: |
          echo "${{ secrets.TIGER_PEM_CONTENT }}" > tiger.pem
          chmod 600 tiger.pem

      - name: 運行 Tiger 腳本
        id: tiger_update
        run: python invest.py
        env:
          TIGER_TIGER_ID: ${{ secrets.TIGER_TIGER_ID }}
          TIGER_ACCOUNT: ${{ secrets.TIGER_ACCOUNT }}
          TIGER_PEM: "tiger.pem"
```