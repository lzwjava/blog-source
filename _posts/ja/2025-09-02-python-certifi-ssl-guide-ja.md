---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Python Certifi SSL 証明書ガイド
translated: true
type: note
---

**`certifi`** パッケージは、PyPIで提供されている小さなライブラリで、**Mozillaが信頼するルート証明書**をバンドル形式で提供します。`requests`や`urllib3`などのPythonライブラリ、あるいはSSL/TLS証明書の検証が必要なHTTPSクライアントで広く利用されています。

使用方法は以下の通りです：

---

### 1. `certifi`のインストール

```bash
pip install certifi
```

---

### 2. CAバンドルのパスを取得

Pythonで：

```python
import certifi

print(certifi.where())
```

これにより、CA証明書バンドル（`.pem`ファイル）へのフルパスが表示されます。例：

```
/usr/local/lib/python3.11/site-packages/certifi/cacert.pem
```

---

### 3. `requests`または`urllib3`での使用

```python
import requests
import certifi

response = requests.get("https://example.com", verify=certifi.where())
print(response.status_code)
```

デフォルトでは`requests`は内部で`certifi`を使用しますが、明示的に`verify=certifi.where()`を渡すことで更新されたバンドルが使用されます。

---

### 4. その他のHTTPSライブラリでの使用

`urllib3`を直接使用する場合：

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

### 5. システム全体での使用（オプション）

アプリケーションにcertifiのCAバンドルを使用させる場合：

```bash
export SSL_CERT_FILE=$(python -m certifi)
```

---

👉 要約：

* `pip install certifi`でインストール
* `certifi.where()`で証明書バンドルのパスを取得
* 証明書検証が必要なライブラリにパスを渡す

---

**各ライブラリを個別に設定する必要なく、Python環境全体でcertifiの証明書をデフォルトで使用する方法**もご紹介しましょうか？