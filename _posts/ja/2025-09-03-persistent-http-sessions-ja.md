---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Python Requests を使った永続的 HTTP セッション
translated: true
type: note
---

Pythonの`requests`ライブラリにおける`Session`は、Cookie、ヘッダー、認証情報などの特定のパラメータを複数のHTTPリクエストにわたって保持する方法です。同じサーバーや関連するエンドポイントに対して繰り返しリクエストを行う際に、状態を維持し、効率を向上させ、コードを簡素化する便利なインターフェースを提供します。以下では、`requests.Session`の動作方法、主な機能、および使用例について説明します。

## `requests.Session`とは何か？

`requests`ライブラリは、PythonでHTTPリクエストを行うために広く使用されています。`requests.get()`や`requests.post()`のようなスタンドアロン関数を使用することもできますが、`Session`オブジェクトを使用すると、複数のリクエストにわたって設定（Cookie、ヘッダー、認証情報など）を保持する永続的なセッションを作成できます。これは、ログインセッションの維持など、状態を必要とするWebサイトやAPIとの対話に特に有用です。

`Session`オブジェクトは以下の機能を提供します：
- リクエスト間でCookieを保持する
- 同じホストへの複数リクエストで基盤となるTCP接続を再利用し（コネクションプーリングによる）、パフォーマンスを向上させる
- セッションで行われるすべてのリクエストに適用されるデフォルトパラメータ（ヘッダー、タイムアウトなど）を設定できる
- 認証とカスタム設定をサポートする

## `Session`の動作方法

`Session`オブジェクトを作成すると、HTTPリクエストのコンテナとして機能します。その動作の詳細は以下の通りです：

1. **Cookieの永続化**: `Session`を使用してリクエストを行うと、サーバーによって設定されたCookie（ログイン後のセッションCookieなど）はセッションに保存され、後続のリクエストで自動的に送信されます。これはログイン状態の維持など、状態を維持するために重要です。

2. **コネクションプーリング**: 同じホストへのリクエストの場合、`Session`は同じTCP接続を再利用するため、リクエストごとに新しい接続を作成する場合と比較してレイテンシとオーバーヘッドが減少します。

3. **デフォルトパラメータ**: ヘッダー、認証、タイムアウトなどの属性を`Session`オブジェクトに設定でき、それらは上書きされない限り、そのセッションで行われるすべてのリクエストに適用されます。

4. **カスタマイズ可能**: プロキシ、SSL検証、さらにはカスタムアダプター（リトライやカスタムトランスポート用など）をマウントして、リクエストの処理方法を制御できます。

## 基本的な使用方法

以下は`requests.Session`の使用方法の簡単な例です：

```python
import requests

# セッションを作成
session = requests.Session()

# このセッション内のすべてのリクエストにデフォルトヘッダーを設定
session.headers.update({'User-Agent': 'MyApp/1.0'})

# GETリクエストを実行
response1 = session.get('https://api.example.com/data')
print(response1.json())

# 別のリクエストを実行。Cookieとヘッダーは再利用される
response2 = session.post('https://api.example.com/submit', data={'key': 'value'})
print(response2.json())

# リソースを解放するためにセッションを閉じる
session.close()
```

この例では：
- `Session`が作成され、すべてのリクエストにカスタム`User-Agent`ヘッダーが設定されます
- セッションはCookieを自動的に処理するため、`response1`がCookieを設定した場合、それは`response2`で送信されます
- セッションは`api.example.com`への接続を再利用するため、パフォーマンスが向上します

## 主な機能と例

### 1. **Cookieの永続化**
セッションは、ログインセッションなど、状態を維持するためにCookieを使用するWebサイトで特に有用です。

```python
import requests

# セッションを作成
session = requests.Session()

# ウェブサイトにログイン
login_data = {'username': 'user', 'password': 'pass'}
response = session.post('https://example.com/login', data=login_data)

# 保護されたページにアクセス。セッションは自動的にログインCookieを送信
protected_page = session.get('https://example.com/protected')
print(protected_page.text)

# セッションを閉じる
session.close()
```

ここでは、セッションがログインリクエストからの認証Cookieを保存し、後続の保護されたページへのリクエストでそれを送信します。

### 2. **デフォルトパラメータの設定**
セッション内のすべてのリクエストに対して、デフォルトのヘッダー、認証、その他のパラメータを設定できます。

```python
import requests
import functools

session = requests.Session()

# デフォルトヘッダーを設定
session.headers.update({
    'Authorization': 'Bearer my_token',
    'Accept': 'application/json'
})

# デフォルトタイムアウトを設定
session.request = functools.partial(session.request, timeout=5)

# リクエストを実行。ヘッダーとタイムアウトが自動的に適用される
response1 = session.get('https://api.example.com/endpoint1')
response2 = session.get('https://api.example.com/endpoint2')

session.close()
```

### 3. **コネクションプーリング**
同じホストへの複数のリクエストを行う場合、`Session`は接続を再利用するため、スタンドアロンリクエストよりも効率的です。

```python
import requests
import time

# セッションなし
start = time.time()
for _ in range(5):
    requests.get('https://api.example.com/data')
print(f"セッションなし: {time.time() - start} 秒")

# セッションあり
session = requests.Session()
start = time.time()
for _ in range(5):
    session.get('https://api.example.com/data')
print(f"セッションあり: {time.time() - start} 秒")
session.close()
```

セッションベースのリクエストは通常、TCP接続を再利用するため、より高速です。

### 4. **認証**
セッションは、HTTP Basic認証やカスタムトークンベース認証などの認証処理を簡素化します。

```python
import requests
from requests.auth import HTTPBasicAuth

session = requests.Session()
session.auth = HTTPBasicAuth('user', 'pass')

# すべてのリクエストにBasic認証が含まれる
response = session.get('https://api.example.com/protected')
print(response.json())

session.close()
```

### 5. **カスタムアダプター**
リトライやコネクションプーリングの動作を制御するために、カスタムアダプターをマウントできます。

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()

# リトライを設定
retries = Retry(total=3, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

# リトライロジック付きでリクエストを実行
response = session.get('https://api.example.com/unstable_endpoint')
print(response.json())

session.close()
```

この例では、特定のHTTPエラーコードに対する自動リトライを設定しています。

## `Session`を使用するタイミング

以下の場合に`requests.Session`を使用してください：
- 認証など、複数のリクエストにわたって状態（Cookieなど）を維持する必要がある場合
- 同じホストへの複数リクエストを行い、コネクションプーリングのメリットを得たい場合
- リクエスト間で一貫した設定（ヘッダー、タイムアウトなど）を適用したい場合
- セッションベースの対話を必要とするAPIやWebサイトと対話する場合

単一のリクエストを行う場合や状態を保持する必要がない場合は、スタンドアロンの`requests.get()`や`requests.post()`で十分です。

## セッションのクローズ

リソース（接続など）を解放するために、使用が終了したら常にセッションを閉じてください：

```python
session.close()
```

あるいは、コンテキストマネージャーとしてセッションを使用すると、自動的に閉じられることが保証されます：

```python
with requests.Session() as session:
    session.headers.update({'User-Agent': 'MyApp/1.0'})
    response = session.get('https://api.example.com/data')
    print(response.json())
# ブロックを抜けるとセッションは自動的に閉じられる
```

## 高度な注意点
- **スレッドセーフ**: `Session`オブジェクトはスレッドセーフではありません。マルチスレッドを使用する場合は、各スレッド用に別々の`Session`を作成してください。
- **プロキシ**: `session.proxies = {'http': 'http://proxy.com', 'https': 'https://proxy.com'}`でセッションにプロキシを設定できます。
- **SSL検証**: デフォルトでは、`Session`はSSL証明書を検証します。無効にするには（本番環境では推奨されません）、`session.verify = False`を使用します。

## 参考文献
[Requests Documentation](https://requests.readthedocs.io/en/latest/)  
[Requests Session Objects](https://requests.readthedocs.io/en/latest/user/advanced/#session-objects)