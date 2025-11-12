---
audio: false
generated: true
lang: ja
layout: post
title: Pythonリクエストライブラリ
translated: true
type: note
---

PostmanをPythonの`requests`ライブラリで完全に置き換えるには、さまざまな種類のリクエスト送信、ヘッダーの取り扱い、JSONデータの操作、ファイルアップロード、プロキシの使用、レスポンスのアサートなど、一般的なHTTP操作をすべて実行できます。以下では、これらの機能それぞれについてステップバイステップで例を示し、完全で実践的なガイドを提供します。

### ステップ1: Requestsライブラリのインストール
始める前に、`requests`ライブラリがインストールされていることを確認してください。ターミナルで次のコマンドを実行します：

```bash
pip install requests
```

それでは、例を見ていきましょう。

---

### HTTPリクエストの送信
`requests`ライブラリはGET、POST、PUT、DELETEなどすべてのHTTPメソッドをサポートしています。以下は、簡単なGETリクエストとPOSTリクエストを送信する方法です：

#### GETリクエスト
```python
import requests

# GETリクエストを送信
response = requests.get('https://api.example.com/data')

# ステータスコードとレスポンスボディを表示
print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

#### POSTリクエスト
```python
# データなしでPOSTリクエストを送信
response = requests.post('https://api.example.com/submit')

print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

---

### ヘッダーの追加
ヘッダーは、認証、コンテンツタイプ、カスタムメタデータなどによく使用されます。ヘッダーを辞書として`headers`パラメータに渡します。

```python
# カスタムヘッダーを定義
headers = {
    'Authorization': 'Bearer my_token',
    'Content-Type': 'application/json',
    'User-Agent': 'MyApp/1.0'
}

# ヘッダー付きでGETリクエストを送信
response = requests.get('https://api.example.com/data', headers=headers)

print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Response Body:", response.text)
```

---

### JSONデータの送信
POSTリクエストでJSONデータを送信するには（PostmanのボディタブでJSONを選択するのと同様）、`json`パラメータを使用します。これにより、`Content-Type`が自動的に`application/json`に設定されます。

```python
# JSONデータを定義
data = {
    'key1': 'value1',
    'key2': 'value2'
}

# JSONデータ付きでPOSTリクエストを送信
response = requests.post('https://api.example.com/submit', json=data, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
```

---

### ファイルのアップロード
ファイルをアップロードするには（Postmanのform-dataオプションと同様）、`files`パラメータを使用します。ファイルをバイナリモード（`'rb'`）で開き、必要に応じて追加のフォームデータを含めます。

#### 簡単なファイルアップロード
```python
# アップロード用のファイルを準備
files = {
    'file': open('myfile.txt', 'rb')
}

# ファイル付きでPOSTリクエストを送信
response = requests.post('https://api.example.com/upload', files=files)

print("Status Code:", response.status_code)
print("Response Body:", response.text)

# ファイルを手動で閉じる
files['file'].close()
```

#### フォームデータ付きファイルアップロード（推奨アプローチ）
`with`文を使用すると、ファイルが自動的に閉じられます：
```python
# 追加のフォームデータ
form_data = {
    'description': 'My file upload'
}

# ファイルを開いてアップロード
with open('myfile.txt', 'rb') as f:
    files = {
        'file': f
    }
    response = requests.post('https://api.example.com/upload', data=form_data, files=files)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

---

### プロキシの使用
リクエストをプロキシ経由でルーティングするには（Postmanのプロキシ設定と同様）、`proxies`パラメータに辞書を使用します。

```python
# プロキシ設定を定義
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# プロキシ経由でリクエストを送信
response = requests.get('https://api.example.com/data', proxies=proxies)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
```

---

### レスポンスの処理とアサート
`requests`ライブラリは、ステータスコード、JSONデータ、ヘッダー、クッキーなどのレスポンス詳細への簡単なアクセスを提供します。Pythonの`assert`文を使用してレスポンスを検証できます（Postmanのテストスクリプトと同様）。

#### JSONレスポンスの解析
```python
response = requests.get('https://api.example.com/data')

# ステータスコードをチェックし、JSONを解析
if response.status_code == 200:
    data = response.json()  # レスポンスをPythonのdict/listに変換
    print("JSON Data:", data)
else:
    print("Error:", response.status_code)
```

#### レスポンス詳細のアサート
```python
response = requests.get('https://api.example.com/data')

# ステータスコードをアサート
assert response.status_code == 200, f"Expected 200, got {response.status_code}"

# JSONを解析してコンテンツをアサート
data = response.json()
assert 'key' in data, "Key not found in response"
assert data['key'] == 'expected_value', "Value does not match"

# レスポンスヘッダーをチェック
assert 'Content-Type' in response.headers, "Content-Type header missing"
assert response.headers['Content-Type'] == 'application/json', "Unexpected Content-Type"

# クッキーをチェック
cookies = response.cookies
assert 'session_id' in cookies, "Session ID cookie missing"

print("All assertions passed!")
```

#### エラーの処理
リクエストを`try-except`ブロックで囲み、ネットワークやHTTPエラーをキャッチします：
```python
try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # 4xx/5xxエラーに対して例外を発生させる
    data = response.json()
    print("Data:", data)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
```

---

### 総合的な例
以下は、ヘッダー、ファイルアップロード、プロキシ、レスポンスアサートを組み合わせた完全な例です：

```python
import requests

# ヘッダーを定義
headers = {
    'Authorization': 'Bearer my_token'
}

# フォームデータとファイル
form_data = {
    'description': 'My file upload'
}

# プロキシ設定
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# ファイルアップロード付きでリクエストを送信
try:
    with open('myfile.txt', 'rb') as f:
        files = {'file': f}
        response = requests.post(
            'https://api.example.com/upload',
            headers=headers,
            data=form_data,
            files=files,
            proxies=proxies
        )
        response.raise_for_status()  # HTTPエラーをチェック

        # レスポンスを解析してアサート
        data = response.json()
        assert 'upload_id' in data, "Upload ID not found in response"
        print("Upload successful, ID:", data['upload_id'])

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
```

---

### 再利用可能な関数（Postmanコレクションの置き換え）
Postmanの保存されたリクエストやコレクションを模倣するには、ロジックを関数にカプセル化します：

```python
def upload_file(file_path, description, token, proxy=None):
    headers = {'Authorization': f'Bearer {token}'}
    data = {'description': description}
    proxies = {'http': proxy, 'https': proxy} if proxy else None

    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(
                'https://api.example.com/upload',
                headers=headers,
                data=data,
                files=files,
                proxies=proxies
            )
            response.raise_for_status()
            data = response.json()
            assert 'upload_id' in data, "Upload ID not found"
            return data['upload_id']
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None

# 使用例
upload_id = upload_file('myfile.txt', 'My file upload', 'my_token', 'http://myproxy:8080')
if upload_id:
    print("Upload successful, ID:", upload_id)
```

---

### 追加機能
- **セッション**: `requests.Session()`を使用して、リクエスト間でクッキーやヘッダーを永続化します。
- **タイムアウト**: リクエストに`timeout=5`（秒）を追加して、ハングを防ぎます。
- **リダイレクト**: `allow_redirects=True/False`で制御します。

---

### まとめ
`requests`ライブラリを使用すると、以下のことができます：
- HTTPリクエストの送信（`get`、`post`など）
- ヘッダー、JSONデータ、ファイルアップロードの含め込み
- プロキシの使用
- レスポンスの解析とアサート（ステータス、JSON、ヘッダー、クッキー）
- コードを再利用可能な関数に整理

これにより、スクリプト作成と自動化に適した、Postmanに対するプログラム的で柔軟な代替手段が得られます！