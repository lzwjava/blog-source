---
audio: false
date: 2025-09-10
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: APIテストの一意性と冪等性戦略
translated: true
type: note
---

良い質問ですね。まずは全体像を把握した後、API/統合テストにおける「一意性」について実践的に考えていきましょう。

# 基本の整理（簡単におさらい）

* **URL（パス + クエリ）**

  * パスは通常**リソースの識別子**: `/orders/123`
  * クエリパラメータは**フィルター/修飾子**: `/orders?status=PAID&page=2`

* **メソッド**

  * `GET/HEAD` は安全（safe）
  * `PUT` は**冪等**（同じ呼び出し、同じ結果）
  * `POST` は、**Idempotency-Key** スキームを追加しない限り、冪等**ではありません**
  * `PATCH` は冪等性が保証されていない

* **ヘッダー**

  * `Content-Type`: **ボディ**のエンコード方法

    * `application/json` → JSONボディ
    * `application/x-www-form-urlencoded` → `a=1&b=2` 形式のボディ
    * `multipart/form-data; boundary=----abcd` → ファイルアップロード & 複数パート
  * `Content-Disposition` は**multipartパート内**に現れ、トップレベルのリクエストには現れない。典型的なパート:

    ```
    --Boundary123
    Content-Disposition: form-data; name="file"; filename="x.png"
    Content-Type: image/png

    <binary bytes>
    --Boundary123--
    ```
  * 便利なカスタムヘッダー:

    * **Idempotency-Key**: 副作用を伴うPOSTの重複排除
    * **X-Request-ID / Correlation-ID**: 単一リクエストをサービス間でトレース/ログ記録

* **ボディ**

  * JSON: シリアライズされたドキュメント
  * `form-urlencoded`: クエリ文字列のようなキーと値のペア（ボディ内）
  * `multipart/form-data`: `boundary` 区切り文字（`----WebKitFormBoundary...` はブラウザで一般的）で区切られた複数の「パート」

# 識別子はどこに置くべきか？

* **リソース識別子** → **URLパス**（`/users/{id}`）。安定していてブックマーク可能なため
* **操作の修飾子** → クエリまたはヘッダー
* **書き込む表現/状態** → ボディ

書き込み操作（例：大きなJSONを持つPOST）で、リクエストの一意性をURLのみで表現しようとするのは、しばしば失敗します。代わりに、**2つのレイヤー**で考えてみましょう：

1. **リクエスト識別子（フィンガープリント）**:
   以下の要素から決定論的に生成されるハッシュ:

   * HTTP **メソッド**
   * **正規化されたパス**（テンプレート + 具体的な値）
   * **正規化されたクエリ**（ソート済み）
   * **選択されたヘッダー**（セマンティクスに影響するもののみ。例: `Accept`, `Content-Language`。`Date` などは含まない）
   * **ボディ**（正規化されたJSON、またはmultipartの場合はパートごとのダイジェスト）

2. **操作識別子（ビジネス冪等性）**:
   副作用を伴う操作（作成/課金/転送）では、**Idempotency-Key**（*ビジネス意図*ごとのUUID）を使用する。サーバーはそのキーで最初の結果を保存し、リトライ時にはそれを返す。

これらは異なる問題を解決します：フィンガープリントは**テスト**と**オブザーバビリティ**を助け、冪等性キーは**本番環境**を重複効果から保護します。

# 「一意性」のためのテスト戦略

1. **リクエストフィンガープリント関数を定義する**（クライアント/テスト側）。ロジックの例:

   * ヘッダー名を小文字化。安全な許可リストに含まれるもののみを含める
   * クエリパラメータをソート。ボディを安定したJSON文字列化（空白を除去、キーをソート）
   * `METHOD\nPATH\nQUERY\nHEADERS\nBODY` に対してSHA-256を適用

2. **すべてのテストに Correlation ID を付与する**

   * テストケースごとにUUIDを生成: `X-Request-ID: test-<suite>-<uuid>`
   * サーバー側でログ記録し、ログを特定のテストに関連付けられるようにする

3. **必要に応じて Idempotency-Key を使用する**

   * リソースを作成したり課金したりするPOSTの場合:

     * `Idempotency-Key: <uuid>`
     * サーバーは、同じキーによるリトライに対して、保持期間内は同じ200/201とボディを返すべき

4. **テストデータは一意だが最小限に保つ**

   * シード済みの決定論的ID（例：メールアドレス `user+T001@example.com`）を使用するか、テストUUIDをサフィックスとして付与する
   * クリーンアップするか、可能であればシード済みIDに対してPUT/DELETEを使用してテストを**冪等**に設計する方が良い

5. **適切なレベルでアサーションする**

   * **冪等**操作の場合: **ステータス**、**表現**、**副作用**（例：繰り返し時にレコード数が変化しない）をアサート
   * Idempotency-Key付きの**非冪等**POSTの場合: 最初の呼び出しは201、その後のリトライは同じボディで200（または同じリソースで201が繰り返される）をアサート

# 実用的なスニペット

**cURL の例**

* JSON POST:

  ```bash
  curl -X POST https://api.example.com/orders \
    -H 'Content-Type: application/json' \
    -H 'Idempotency-Key: 4b6f2d1a-...' \
    -H 'X-Request-ID: test-orders-create-...' \
    -d '{"customerId":"C123","items":[{"sku":"ABC","qty":1}]}'
  ```
* マルチパートアップロード:

  ```bash
  curl -X POST https://api.example.com/uploads \
    -H 'X-Request-ID: test-upload-...' \
    -F 'file=@/path/pic.png' \
    -F 'meta={"purpose":"avatar"};type=application/json'
  ```

  (curl は `Content-Type: multipart/form-data; boundary=----...` を設定し、各パートは独自の `Content-Disposition` を持つ)

**Python テスト側リクエストフィンガープリント（概念実証）:**

```python
import hashlib, json, urllib.parse

def canonical_json(obj):
    return json.dumps(obj, separators=(',', ':'), sort_keys=True)

def normalize_query(url):
    parsed = urllib.parse.urlsplit(url)
    q = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    q.sort()
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, urllib.parse.urlencode(q), '')), q

def request_fingerprint(method, url, headers=None, body_bytes=b''):
    headers = headers or {}
    # セマンティクスに影響するヘッダーの許可リスト
    allow = {'accept', 'content-type', 'content-language'}
    norm_headers = {k.lower(): v.strip() for k, v in headers.items() if k.lower() in allow}
    header_line = '\n'.join(f'{k}:{norm_headers[k]}' for k in sorted(norm_headers))
    url_no_query, q_pairs = normalize_query(url)
    query_line = '&'.join(f'{k}={v}' for k, v in q_pairs)
    h = hashlib.sha256()
    h.update((method.upper() + '\n').encode())
    h.update((url_no_query + '\n').encode())
    h.update((query_line + '\n').encode())
    h.update((header_line + '\n').encode())
    h.update(body_bytes or b'')
    return h.hexdigest()
```

* JSONボディの場合: `body_bytes=canonical_json(payload).encode()` を渡す
* マルチパートの場合、境界文字列のノイズを避けるために、各パートをハッシュし、それらを連結したものをハッシュする

# 核心のアイデアに答える

> 「URLが一意ならリクエストも一意なのか？ パラメータやボディも大きく寄与する — API/統合テストにおける一意性についてどう考えればよいか？」

* テストにおける一意性に関して、**URLだけ**では**不十分**であると考える。ヘッダーとボディが意味的に重要だから
* テストにおける重複排除/トレースのために、上記のような**リクエストフィンガープリント**を構築する
* **POST**のビジネスレベルの重複排除には、URLではなく**Idempotency-Key**に依存する
* 明確さとテストの決定性を高めるために、**リソース識別子**はパスに保持する

# 今日から導入できる小さなチェックリスト

* [ ] すべてのテストリクエストに `X-Request-ID` (UUID) を追加する
* [ ] リソース作成/課金を行うPOSTに `Idempotency-Key` を追加する
* [ ] リクエストフィンガープリントを計算し、各アサーションと共にログ記録するテストヘルパーを実装する
* [ ] ハッシュ化前にJSONを正規化する。クエリパラメータをソートする。意味的ヘッダーの許可リストを使用する
* [ ] テストを冪等にするために、upsertにはPUTを優先する。真の作成にはPOSTを予約する
* [ ] マルチパートの場合、生の境界バイトではなく、**サーバー側で解析されたパート**（名前、ファイル名、コンテンツタイプ）に対してアサートする

現在使用しているテストスタック（pytest/unittest + requests/httpx、または Java/Kotlin）を共有していただければ、それに合わせてすぐに使えるヘルパーを提供できます。