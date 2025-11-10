---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 使用 Python Requests 實現持久 HTTP 會話
translated: true
type: note
---

在 Python 的 `requests` 函式庫中，`Session` 是一種能在多個 HTTP 請求間保持特定參數（如 cookies、headers 和驗證資訊）的方式。它為向同一伺服器或相關端點重複發送請求提供了便利的介面，同時能維持狀態、提升效率並簡化程式碼。以下我將說明 `requests.Session` 的運作原理、主要功能，並提供範例來說明其用法。

## 什麼是 `requests.Session`？

`requests` 函式庫在 Python 中被廣泛用於發送 HTTP 請求。雖然你可以使用獨立函式如 `requests.get()` 或 `requests.post()`，但 `Session` 物件能讓你建立一個持久化的會話，在多個請求間保留配置（例如 cookies、headers 或驗證憑證）。這在需要狀態互動的網站或 API 互動中特別有用，例如維持登入狀態或重複使用 TCP 連線。

`Session` 物件：
- 在請求間保持 cookies 的持久性。
- 重複使用底層 TCP 連線（透過連線池），在向同一主機發送多個請求時提升效能。
- 允許你設定預設參數（例如 headers、timeouts），這些參數會套用至該 session 的所有請求。
- 支援驗證和自訂配置。

## `Session` 如何運作？

當你建立 `Session` 物件時，它會作為你 HTTP 請求的容器。以下是其運作方式的分解：

1. **持久化 Cookies**：當你使用 `Session` 發送請求時，伺服器設定的任何 cookies（例如登入後的 session cookies）都會儲存在 session 中，並在後續請求中自動發送。這是維持狀態（例如保持登入）的關鍵。

2. **連線池**：對於向同一主機的請求，`Session` 會重複使用相同的 TCP 連線，與為每個請求建立新連線相比，減少了延遲和開銷。

3. **預設參數**：你可以在 `Session` 物件上設定屬性，如 headers、驗證或 timeout，這些設定將套用至該 session 的所有請求，除非被覆寫。

4. **可自訂性**：你可以配置代理、SSL 驗證，甚至掛載自訂適配器（例如用於重試或自訂傳輸）以控制請求的處理方式。

## 基本用法

以下是使用 `requests.Session` 的簡單範例：

```python
import requests

# 建立 session
session = requests.Session()

# 為此 session 中的所有請求設定預設 headers
session.headers.update({'User-Agent': 'MyApp/1.0'})

# 發送 GET 請求
response1 = session.get('https://api.example.com/data')
print(response1.json())

# 發送另一個請求；cookies 和 headers 會被重複使用
response2 = session.post('https://api.example.com/submit', data={'key': 'value'})
print(response2.json())

# 關閉 session 以釋放資源
session.close()
```

在此範例中：
- 建立了一個 `Session`，並為所有請求設定了自訂的 `User-Agent` header。
- session 會自動處理 cookies，因此如果 `response1` 設定了 cookie，它會隨 `response2` 一起發送。
- session 重複使用連至 `api.example.com` 的連線，從而提升效能。

## 主要功能與範例

### 1. **保持 Cookies**
Session 在使用 cookies 維持狀態的網站中特別有用，例如登入 session。

```python
import requests

# 建立 session
session = requests.Session()

# 登入網站
login_data = {'username': 'user', 'password': 'pass'}
response = session.post('https://example.com/login', data=login_data)

# 存取受保護頁面；session 會自動發送登入 cookie
protected_page = session.get('https://example.com/protected')
print(protected_page.text)

# 關閉 session
session.close()
```

此處，session 儲存了登入請求中的驗證 cookie，並在後續請求至受保護頁面時發送。

### 2. **設定預設參數**
你可以為 session 中的所有請求設定預設 headers、驗證或其他參數。

```python
import requests

session = requests.Session()

# 設定預設 headers
session.headers.update({
    'Authorization': 'Bearer my_token',
    'Accept': 'application/json'
})

# 設定預設 timeout
session.request = functools.partial(session.request, timeout=5)

# 發送請求；headers 和 timeout 會自動套用
response1 = session.get('https://api.example.com/endpoint1')
response2 = session.get('https://api.example.com/endpoint2')

session.close()
```

### 3. **連線池**
當向同一主機發送多個請求時，`Session` 會重複使用連線，這比獨立請求更有效率。

```python
import requests
import time

# 不使用 session
start = time.time()
for _ in range(5):
    requests.get('https://api.example.com/data')
print(f"Without session: {time.time() - start} seconds")

# 使用 session
session = requests.Session()
start = time.time()
for _ in range(5):
    session.get('https://api.example.com/data')
print(f"With session: {time.time() - start} seconds")
session.close()
```

基於 session 的請求通常更快，因為它們重複使用 TCP 連線。

### 4. **驗證**
Session 簡化了驗證處理，例如 HTTP Basic Auth 或自訂的 token-based 驗證。

```python
import requests
from requests.auth import HTTPBasicAuth

session = requests.Session()
session.auth = HTTPBasicAuth('user', 'pass')

# 所有請求都將包含 Basic Auth
response = session.get('https://api.example.com/protected')
print(response.json())

session.close()
```

### 5. **自訂適配器**
你可以掛載自訂適配器以控制重試或連線池行為等。

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()

# 配置重試
retries = Retry(total=3, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

# 發送帶有重試邏輯的請求
response = session.get('https://api.example.com/unstable_endpoint')
print(response.json())

session.close()
```

此範例為特定的 HTTP 錯誤碼設定了自動重試。

## 何時使用 `Session`

在以下情況使用 `requests.Session`：
- 你需要跨多個請求維持狀態（例如 cookies），例如用於驗證。
- 你向同一主機發送多個請求，並希望受益於連線池。
- 你希望在請求間套用一致的配置（headers、timeouts 等）。
- 你與需要基於 session 互動的 API 或網站進行互動。

如果你只發送單一請求或不需要保持狀態，使用獨立的 `requests.get()` 或 `requests.post()` 即可。

## 關閉 Session

完成後請務必關閉 session 以釋放資源（例如連線）：

```python
session.close()
```

或者，將 session 作為 context manager 使用，以確保其自動關閉：

```python
with requests.Session() as session:
    session.headers.update({'User-Agent': 'MyApp/1.0'})
    response = session.get('https://api.example.com/data')
    print(response.json())
# Session 會在區塊結束時自動關閉
```

## 進階注意事項
- **執行緒安全**：`Session` 物件並非執行緒安全。如果你使用多執行緒，請為每個執行緒建立獨立的 `Session`。
- **代理**：你可以透過 `session.proxies = {'http': 'http://proxy.com', 'https': 'https://proxy.com'}` 在 session 上設定代理。
- **SSL 驗證**：預設情況下，`Session` 會驗證 SSL 憑證。若要停用（不建議在生產環境中使用），請使用 `session.verify = False`。

## 參考資料
[Requests Documentation](https://requests.readthedocs.io/en/latest/)  
[Requests Session Objects](https://requests.readthedocs.io/en/latest/user/advanced/#session-objects)