---
audio: true
generated: false
image: false
lang: ar
layout: post
title: استثمارات الأسهم الأسبوعية مع واجهة برمجة التطبيقات TigerOpen
translated: true
---

تطويرتُ برنامجًا ببيثون وعمليّة عمل GitHub Actions لتتويج استراتيجيتي الاستثمارية الأسبوعية، حيث أشتري سهمًا واحدًا من أسهم شركة NVIDIA كل يوم الأربعاء في الساعة 10:35 مساءً بتوقيت الصين القياسي (CST). اخترت يوم الأربعاء لأنّه في عام 2025 لا يوجد أي عطلات في ذلك اليوم، مما يضمن التنفيذ المستمر.

## نظرة عامة

يستخدم البرنامج واجهة برمجة التطبيقات TigerOpen لتقديم طلب سوقي لشراء أسهم شركة NVIDIA ويراقب حالة الطلب. تقوم عمليّة عمل GitHub Actions بتشغيل البرنامج حسب الجدول الزمني، مع معالجة الإعداد والتأشير بشكل آمن. أدناه تفاصيل كلا المكونين.

## برنامج بيثون

يقدم هذا البرنامج طلب شراء لشراء سهم واحد من أسهم شركة NVIDIA، ويحقق حالة الطلب لمدة تصل إلى 60 ثانية، ويُلغي الطلب إذا لم يتم تنفيذه.

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

# دالة لتقديم الطلب
def place_order():
    client_config = get_client_config()
    trade_client = TradeClient(client_config)
    account = client_config.account  # تخزين الحساب للاستخدام اللاحق

    contract = stock_contract(symbol='NVDA', currency='USD')
    stock_order = market_order(
        account=account, contract=contract, action='BUY', quantity=1
    )
    # تقديم الطلب
    order_id = trade_client.place_order(stock_order)
    print(f"تم تقديم الطلب مع رقم: {order_id}")

    # تتبع الوقت
    start_time = time.time()
    while time.time() - start_time < 60:  # وقت انتظار 1 دقيقة
        # الحصول على الطلب والبحث عن الذي تم تقديمه
        order = trade_client.get_order(id=order_id)
        if str(order.id) == str(order_id):
            print(f"تم مطابقة رقم الطلب! تحقق من حالة الطلب: {order.status}")
            # تحقق من حالة الطلب باستخدام قيم إحصائية حالة الطلب
            if order.status == OrderStatus.FILLED:
                print("تم إكمال الطلب بنجاح.")
                return
            elif order.status == OrderStatus.REJECTED:
                print(f"تم رفض الطلب: {order_id}")
                raise Exception(f"تم رفض الطلب {order_id}")
            elif order.status in [
                OrderStatus.PENDING_NEW,
                OrderStatus.NEW,
                OrderStatus.HELD,
                OrderStatus.PENDING_CANCEL
            ]:
                print(f"الطلب في انتظار، الحالة: {order.status}")
            else:
                print(f"حالة الطلب هي: {order.status}")

        # النوم قبل التحقق مرة أخرى
        time.sleep(5)  # التحقق كل 5 ثوانٍ

    # إذا لم يتم إكمال الطلب في دقيقة واحدة، ألغِ الطلب
    print("لم يتم إكمال الطلب في دقيقة واحدة. إلغاء الطلب.")
    trade_client.cancel_order(id=order_id)
    print(f"تم إلغاء الطلب: {order_id}")

if __name__ == '__main__':
    place_order()
```

## عمليّة عمل GitHub Actions

تجري العمليّة كل يوم الأربعاء في الساعة 14:35 بتوقيت UTC (10:35 مساءً بتوقيت UTC) وتعدّل البيئة، وتثبيت التبعيات، وتنفيذ البرنامج.

```yaml
name: Regular Invest

on:
  schedule:
    - cron: '35 14 * * 3'  # تشغيل كل يوم الأربعاء في الساعة 14:35 بتوقيت UTC
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
      - name: استرجاع المستودع
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: إعداد بيثون 3.13.2
        uses: actions/setup-python@v4
        with:
          python-version: "3.13.2"

      - name: تثبيت التبعيات
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: إعداد ملف Tiger PEM
        run: |
          echo "${{ secrets.TIGER_PEM_CONTENT }}" > tiger.pem
          chmod 600 tiger.pem

      - name: تشغيل برنامج Tiger
        id: tiger_update
        run: python invest.py
        env:
          TIGER_TIGER_ID: ${{ secrets.TIGER_TIGER_ID }}
          TIGER_ACCOUNT: ${{ secrets.TIGER_ACCOUNT }}
          TIGER_PEM: "tiger.pem"
```