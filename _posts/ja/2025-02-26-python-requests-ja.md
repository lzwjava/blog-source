---
audio: false
generated: false
lang: ja
layout: post
title: Python リクエストライブラリ
translated: true
---

PostmanをPythonの`requests`ライブラリで完全に置き換えるには、異なる種類のリクエストを送信し、ヘッダーを処理し、JSONデータを扱い、ファイルをアップロードし、プロキシを使用し、応答を検証するなど、一般的なHTTP操作をすべて実行できます。以下に、これらの機能の各ステップごとの例を示し、完全で実践的なガイドを提供します。

### ステップ1: Requestsライブラリのインストール
始める前に、`requests`ライブラリがインストールされていることを確認してください。ターミナルで次のコマンドを実行します：

```bash
pip install requests
```

それでは、例に入っていきましょう。

---

### HTTPリクエストの送信
`requests`ライブラリは、GET、POST、PUT、DELETEなど、すべてのHTTPメソッドをサポートしています。以下に、簡単なGETリクエストとPOSTリクエストを送信する方法を示します。

#### GETリクエスト
```python
import requests

# GETリクエストを送信
response = requests.get('https://api.example.com/data')

# ステータスコードと応答ボディを表示
print("ステータスコード:", response.status_code)
print("応答ボディ:", response.text)
```

#### POSTリクエスト
```python
# データなしでPOSTリクエストを送信
response = requests.post('https://api.example.com/submit')

print("ステータスコード:", response.status_code)
print("応答ボディ:", response.text)
```

---

### ヘッダーの追加
ヘッダーは、認証、コンテンツタイプ、またはカスタムメタデータに使用されます。これらを`headers`パラメータとして辞書として渡します。

```python
# カスタムヘッダーを定義
headers = {
    'Authorization': 'Bearer my_token',
    'Content-Type': 'application/json',
    'User-Agent': 'MyApp/1.0'
}

# ヘッダー付きのGETリクエストを送信
response = requests.get('https://api.example.com/data', headers=headers)

print("ステータスコード:", response.status_code)
print("応答ヘッダー:", response.headers)
print("応答ボディ:", response.text)
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

# JSONデータ付きのPOSTリクエストを送信
response = requests.post('https://api.example.com/submit', json=data, headers=headers)

print("ステータスコード:", response.status_code)
print("応答JSON:", response.json())
```

---

### ファイルのアップロード
ファイルをアップロードするには（Postmanのform-dataオプションと同様）、`files`パラメータを使用します。ファイルをバイナリモード（`'rb'`）で開き、オプションで追加のフォームデータを含めます。

#### 簡単なファイルアップロード
```python
# アップロード用のファイルを準備
files = {
    'file': open('myfile.txt', 'rb')
}

# ファイル付きのPOSTリクエストを送信
response = requests.post('https://api.example.com/upload', files=files)

print("ステータスコード:", response.status_code)
print("応答ボディ:", response.text)

# ファイルを手動で閉じる
files['file'].close()
```

#### ファイルアップロードとフォームデータ（推奨されるアプローチ）
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

print("ステータスコード:", response.status_code)
print("応答ボディ:", response.text)
```

---

### プロキシの使用
リクエストをプロキシ経由でルーティングするには（Postmanのプロキシ設定と同様）、辞書を使用して`proxies`パラメータを使用します。

```python
# プロキシ設定を定義
proxies = {
    'http': 'http://myproxy:8080',
    'https': 'https://myproxy:8080'
}

# プロキシ経由でリクエストを送信
response = requests.get('https://api.example.com/data', proxies=proxies)

print("ステータスコード:", response.status_code)
print("応答ボディ:", response.text)
```

---

### 応答の処理と検証
`requests`ライブラリは、ステータスコード、JSONデータ、ヘッダー、クッキーなどの応答の詳細に簡単にアクセスできます。Pythonの`assert`ステートメントを使用して応答を検証し、Postmanのテストスクリプトと同様にすることができます。

#### JSON応答の解析
```python
response = requests.get('https://api.example.com/data')

# ステータスコードを確認し、JSONを解析
if response.status_code == 200:
    data = response.json()  # 応答をPythonの辞書/リストに変換
    print("JSONデータ:", data)
else:
    print("エラー:", response.status_code)
```

#### 応答の詳細の検証
```python
response = requests.get('https://api.example.com/data')

# ステータスコードの検証
assert response.status_code == 200, f"200が期待されましたが、{response.status_code}が得られました"

# JSONを解析し、コンテンツを検証
data = response.json()
assert 'key' in data, "応答にキーが見つかりません"
assert data['key'] == 'expected_value', "値が一致しません"

# 応答ヘッダーの確認
assert 'Content-Type' in response.headers, "Content-Typeヘッダーが見つかりません"
assert response.headers['Content-Type'] == 'application/json', "予期せぬContent-Type"

# クッキーの確認
cookies = response.cookies
assert 'session_id' in cookies, "セッションIDクッキーが見つかりません"

print("すべての検証が成功しました！")
```

#### エラーの処理
リクエストを`try-except`ブロックでラップして、ネットワークエラーやHTTPエラーをキャッチします：
```python
try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # 4xx/5xxエラーのために例外を引き起こす
    data = response.json()
    print("データ:", data)
except requests.exceptions.RequestException as e:
    print("リクエストに失敗しました:", e)
```

---

### 総合的な例
ヘッダー、ファイルアップロード、プロキシ、応答の検証を組み合わせた完全な例：

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

# ファイルアップロード付きのリクエストを送信
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
        response.raise_for_status()  # HTTPエラーの確認

        # 応答を解析し、検証
        data = response.json()
        assert 'upload_id' in data, "応答にアップロードIDが見つかりません"
        print("アップロード成功、ID:", data['upload_id'])

except requests.exceptions.RequestException as e:
    print("リクエストに失敗しました:", e)
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
            assert 'upload_id' in data, "アップロードIDが見つかりません"
            return data['upload_id']
    except requests.exceptions.RequestException as e:
        print("リクエストに失敗しました:", e)
        return None

# 使用例
upload_id = upload_file('myfile.txt', 'My file upload', 'my_token', 'http://myproxy:8080')
if upload_id:
    print("アップロード成功、ID:", upload_id)
```

---

### 追加機能
- **セッション**: `requests.Session()`を使用して、リクエスト間でクッキーやヘッダーを保持します。
- **タイムアウト**: リクエストに`timeout=5`（秒）を追加して、ハングアップを防ぎます。
- **リダイレクト**: `allow_redirects=True/False`で制御します。

---

### まとめ
`requests`ライブラリを使用すると、以下ができます：
- HTTPリクエストを送信（`get`、`post`など）
- ヘッダー、JSONデータ、ファイルアップロードを含める
- プロキシを使用
- 応答を解析し、検証（ステータス、JSON、ヘッダー、クッキー）
- コードを再利用可能な関数に組織化

これにより、Postmanのプログラム的で柔軟な代替手段が提供され、スクリプティングや自動化に適しています！