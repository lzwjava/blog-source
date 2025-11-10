---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Python Certifi SSL 證書指南
translated: true
type: note
---

**`certifi`** 套件在 PyPI 上是一個提供 **Mozilla 受信任根憑證** 套裝組合的小型函式庫。它常被 Python 函式庫如 `requests`、`urllib3` 或任何需要驗證 SSL/TLS 憑證的 HTTPS 客戶端所使用。

使用方法如下：

---

### 1. 安裝 `certifi`

```bash
pip install certifi
```

---

### 2. 取得 CA 套裝路徑

在 Python 中：

```python
import certifi

print(certifi.where())
```

這會列印出 CA 憑證套裝組合（一個 `.pem` 檔案）的完整路徑。例如：

```
/usr/local/lib/python3.11/site-packages/certifi/cacert.pem
```

---

### 3. 與 `requests` 或 `urllib3` 一起使用

```python
import requests
import certifi

response = requests.get("https://example.com", verify=certifi.where())
print(response.status_code)
```

預設情況下，`requests` 內部已使用 `certifi`，但明確傳入 `verify=certifi.where()` 可確保其使用更新的套裝組合。

---

### 4. 在其他 HTTPS 函式庫中使用

若直接使用 `urllib3`：

```python
import urllib3
import certifi

http = urllib3.PoolManager(
    cert_reqs="CERT_REQUIRED",
    ca_certs=certifi.where()
)

response = http.request("GET", "https://example.com")
print(response.status)
```

---

### 5. 系統層級使用（可選）

有時您可能希望將應用程式指向使用 certifi 的 CA 套裝組合：

```bash
export SSL_CERT_FILE=$(python -m certifi)
```

---

👉 簡而言之：

* 使用 `pip install certifi` 安裝
* 使用 `certifi.where()` 取得憑證套裝路徑
* 將其傳遞給需要憑證驗證的函式庫

---

您是否也希望我示範 **如何讓整個 Python 環境預設使用 certifi 的憑證**，這樣您就無需個別設定每個函式庫？