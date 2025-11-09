---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: .envを使用したPython Requestsプロキシの設定
translated: true
type: note
---

### `.env`ファイルを使用してPython RequestsのHTTP/HTTPSプロキシを設定する

Pythonの`requests`ライブラリは、プロキシ設定のために`HTTP_PROXY`や`HTTPS_PROXY`といった標準的な環境変数を自動的に認識します。これらを安全に管理するには（スクリプト内にハードコードせず）、`.env`ファイルに保存し、`python-dotenv`ライブラリを使用して読み込むことができます。これにより、機密性の高いプロキシ情報がコードから分離されます。

#### ステップ1: 必要なパッケージをインストール
`requests`（まだインストールされていない場合）と`.env`ファイルを読み込むための`python-dotenv`が必要です。

```bash
pip install requests python-dotenv
```

#### ステップ2: `.env`ファイルを作成
プロジェクトのルートディレクトリに、`.env`（拡張子なし）という名前のファイルを作成し、プロキシ設定を追加します。プロキシURLには`http://`または`https://`形式を使用し、必要に応じてユーザー名とパスワードを含めます。

`.env`ファイルの内容例:
```
HTTP_PROXY=http://username:password@proxy-host:port
HTTPS_PROXY=https://username:password@proxy-host:port
NO_PROXY=localhost,127.0.0.1,example.com  # オプション: プロキシをバイパスするホスト/IPのカンマ区切りリスト
```

- `HTTP_PROXY`: HTTPトラフィック用
- `HTTPS_PROXY`: HTTPSトラフィック用（多くの場合`HTTP_PROXY`と同じ）
- `NO_PROXY`: プロキシをバイパスするホスト/IPのカンマ区切りリスト
- 注意: 環境変数は大文字小文字を区別しませんが、大文字が慣例です

機密情報のコミットを防ぐため、`.env`を`.gitignore`に追加してください。

#### ステップ3: Pythonスクリプトで`.env`ファイルを読み込む
スクリプトの先頭で環境変数を読み込みます:

```python
from dotenv import load_dotenv
import requests

# .envファイルから変数を読み込み
load_dotenv()  # デフォルトでカレントディレクトリの.envを探します

# これでリクエストを実行 - プロキシが自動的に適用されます
response = requests.get('https://httpbin.org/ip')
print(response.json())
```

- `load_dotenv()`は`.env`ファイルを読み込み、変数を`os.environ`に設定します
- `requests`は`HTTP_PROXY`/`HTTPS_PROXY`を自動的に検出します - 上書きしない限り`proxies`辞書を渡す必要はありません

#### ステップ4: プロキシ使用を確認（オプション）
プロキシが正しく動作しているか確認するには、httpbin.orgなどのサービスでテストします:

```python
import requests
from dotenv import load_dotenv

load_dotenv()

proxies = requests.utils.get_environ_proxies('https://httpbin.org/ip')  # 読み込まれたプロキシを検査
print("読み込まれたプロキシ:", proxies)

response = requests.get('https://httpbin.org/ip')
print("プロキシ経由のあなたのIP:", response.json())
```

設定が正しければ、プロキシサーバーのIPアドレスが表示されるはずです。

#### よくある問題とヒント
- **プロキシ認証**: 必要な場合はURLに`username:password@`を含めてください
- **SOCKSプロキシ**: `socks5://`プレフィックスを使用します（`requests[socks]`エクストラが必要: `pip install requests[socks]`）
- **リクエストごとの上書き**: 特定の呼び出しで異なるプロキシが必要な場合は、辞書を渡します:
  ```python:disable-run
  proxies = {'http': 'http://custom-proxy:port', 'https': 'https://custom-proxy:port'}
  response = requests.get('url', proxies=proxies)
  ```
- **環境**: Windows/Linux/macOSで動作します。Windowsでは、cmdで`set`を使用するか、PowerShellの同等のコマンドを使用します
- **セキュリティ**: `.env`をバージョン管理にコミットしないでください

このセットアップはシンプルで安全であり、環境ベースの設定におけるベストプラクティスに従っています。

[Requestsドキュメント: プロキシ](https://requests.readthedocs.io/en/latest/user/advanced/#proxies)  
[python-dotenvドキュメント](https://github.com/theskumar/python-dotenv)