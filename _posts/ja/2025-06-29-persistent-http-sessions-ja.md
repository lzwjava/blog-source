---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: リクエストセッションを用いた永続的HTTPセッション
translated: true
type: note
---

### requests.Sessionの仕組み

Pythonの`requests`ライブラリにおいて、`requests.Session`は複数のHTTPリクエストにわたって永続的なセッションを維持するためのクラスです。個別の`requests.get()`呼び出しなどと比較して、以下の利点があります：

- **Cookieの永続化**：デフォルトで、サーバーから受信したCookieを自動的に保存し、後続のリクエストで送信します。これにより、一度ログインすれば認証状態を維持するといった、セッションベースのやり取りが可能になります。
- **コネクションプーリング**：同じホストに対する基盤となるTCP接続を再利用するため、新規接続の確立に伴うオーバーヘッドを回避してパフォーマンスを向上させます。
- **設定の共有**：デフォルトのヘッダー、認証情報、プロキシ、その他のパラメータをセッション内のすべてのリクエストに適用するように設定できます。
- **内部動作**：HTTP処理には`urllib3`ライブラリを使用します。`Session`を作成すると、`cookies`（`RequestsCookieJar`インスタンス）、`headers`などの属性が初期化されます。例えば、あるレスポンスからのCookieは、同じドメインへの次のリクエストに自動的に含まれます。

以下はセッションを作成して使用する基本的な例です：

```python
import requests

# セッションを作成
session = requests.Session()

# このセッション内のすべてのリクエストにデフォルトヘッダーを設定
session.headers.update({'User-Agent': 'MyApp/1.0'})

# セッションを共有して複数のリクエストを実行
response1 = session.get('https://example.com/login')
response2 = session.post('https://example.com/data', data={'key': 'value'})

# セッションに保存されたCookieにアクセス
print(session.cookies)
```

これにより、（セッションIDなどの）Cookieが手動での介入なしに透過的に処理されます。

### Java/SpringプロジェクトのAPIをPythonで呼び出す

Java/Spring（通常はSpring MVCまたはSpring Bootを介したRESTfulエンドポイント）を使用して構築されたAPIと対話するには、他のHTTP APIと同様に`requests.Session`を使用します。Springプロジェクトは多くの場合、HTTP/HTTPSを介してAPIを公開しており、`requests`は実装されている認証、CSRFトークン、またはレート制限を処理できます。

- **認証**：Springはフォーム、JWT、またはOAuthを使用したSpring Securityを採用している可能性があります。セッションベースの認証（例：ログインフォーム経由）の場合、`requests.Session`はログインリクエスト後のCookie処理を自動化します。
- **呼び出しの実行**：標準的なHTTPメソッド（`GET`、`POST`など）を使用します。Spring APIがJSONペイロードを必要とする場合は、`json=your_data`を渡します。

Spring認証APIにログインし、別のエンドポイントを呼び出す例：

```python
import requests

session = requests.Session()

# ログイン（ユーザー名/パスワードで /login へPOST送信する想定）
login_payload = {'username': 'user', 'password': 'pass'}
response = session.post('https://spring-api.example.com/login', data=login_payload)

if response.ok:
    # 別のAPIエンドポイントを呼び出し、セッションCookieは維持される
    data_response = session.get('https://spring-api.example.com/api/data')
    print(data_response.json())
else:
    print("ログイン失敗")
```

Spring APIはデフォルトではステートレスですが、（Tomcatや組み込みサーバー内などの）サーバーサイドストレージを介してセッションを管理できます。Pythonクライアントが、Springが必要とするCORS、CSRF、またはカスタムヘッダーを処理するようにしてください。

### Java/Spring側におけるJSESSIONIDとの関係

- **JSESSIONIDとは**：Java Webアプリケーション（Springを含む。Springは多くの場合TomcatなどのServletコンテナ上で動作する）において、JSESSIONIDはユーザーセッションを追跡するためにコンテナが使用する標準的なHTTP Cookieです。セッションが作成されるとき（例：ログイン後）に設定され、レスポンスで送信されます。クライアント側では、ブラウザ（または`requests`のようなHTTPクライアント）は、ユーザー認証やショッピングカートのデータなどの状態を維持するために、後続のリクエストでこれを送信します。
- **requests.Sessionとの関係**：`requests.Session`はJSESSIONIDを他のCookieと同様に扱います。サーバーの「Set-Cookie」ヘッダーから自動的に保存し、将来のリクエストの「Cookie」ヘッダーに含めます。これにより、Cookieを手動で解析/抽出することなく、ステートフルなSpring APIとのシームレスな対話が可能になります。
- **サーバー側の処理**：Java/Spring側では、ServletContextがセッションを管理します。PythonクライアントがJSESSIONIDを含むリクエストを送信すると、SpringのHttpSessionが関連するサーバー側のデータを取得します。有効期限が切れているか無効な場合、Springは再認証を要求する可能性があります。安全なセッションのためには、JSESSIONIDがHTTP経由で盗まれる脆弱性があるため、HTTPSを使用するように設定を確認してください。
- **発生する可能性のある問題**：SpringがCSRFトークンやその他の保護を強制する場合、（例：隠しフォームフィールドから）それらを抽出して含める必要があるかもしれません。ステートレスなJWTベースのSpring APIの場合、`requests.Session`は依然としてヘッダー内の認証トークンを永続化することで役立ちますが、JSESSIONIDは関連性が低くなります。

Spring APIの呼び出し時に特定のエラー（例：401 Unauthorized）が発生した場合は、ネットワークログでCookieの問題を確認するか、`import logging; logging.basicConfig(level=logging.DEBUG)`を使用して`requests`のデバッグを有効にしてください。Spring Securityの詳細については、公式ドキュメントを参照してください。