---
audio: false
lang: hant
layout: post
title: 老虎證券開放 API 範例
translated: true
---

此程式碼片段使用 Tiger Open API 擷取並列印香港交易所部分最大上市公司的即時股價。它初始化客戶端、擷取股價並列印結果。

```python
from tigeropen.common.consts import Language, Market, BarPeriod, QuoteRight
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.common.util.signature_utils import read_private_key
from tigeropen.quote.quote_client import QuoteClient
import os


def get_client_config(sandbox=False):
    client_config = TigerOpenClientConfig(sandbox_debug=sandbox)
    client_config.private_key = read_private_key(os.environ.get('TIGER_PEM'))
    client_config.tiger_id = os.environ.get('TIGER_TIGER_ID')
    client_config.account = os.environ.get('TIGER_ACCOUNT')
    client_config.language = Language.zh_CN
    return client_config


client_config = get_client_config()
quote_client = QuoteClient(client_config)

hong_kong_biggest_companies_codes = [
    '00700',  #騰訊控股有限公司
    '09988',  #阿里巴巴集團控股有限公司
    '01299',  #友邦保險有限公司
    '00941',  #中國移動有限公司
    '00388',  #香港交易及結算所有限公司
    '03690',  #美團
    '01398',  #中國工商銀行股份有限公司
    '02318',  #中國平安保險(集團)股份有限公司
    '01810',  #小米集團
    '03988',  #中國銀行股份有限公司
]

stock_prices = quote_client.get_stock_briefs(hong_kong_biggest_companies_codes)
print(stock_prices)

```
