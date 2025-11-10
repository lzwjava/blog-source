---
audio: false
generated: true
image: false
lang: ja
layout: post
title: プロキシスキームはサポートされていません
translated: true
type: note
---

このエラーは、`gitmessageai.py`スクリプト内の`openai`クライアントが使用する`httpx`ライブラリが、プロキシURL `socks://127.0.0.1:7891/`でプロキシを設定しようとしているが、スキーム`socks`がサポートされていないか認識されず、`ValueError: Unknown scheme for proxy URL`が発生していることを示しています。これは、環境またはコードからプロキシ設定が取得されており、サポートされていないSOCKSプロキシスキームが使用されていることを示唆しています。

プロキシの発生源とその修正方法について見ていきましょう。

### プロキシはどこから来ているのか？

プロキシ設定（`socks://127.0.0.1:7891/`）は、以下のいずれかの場所から取得されている可能性があります：

1. **環境変数**
   - `httpx`ライブラリは、環境変数`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`、またはそれらの小文字版（`http_proxy`、`https_proxy`、`all_proxy`）から自動的にプロキシ設定をチェックします。
   - `socks://127.0.0.1:7891/`のような値は、SOCKSプロキシ（ShadowsocksやVPNツールで一般的）がこれらの変数のいずれかに設定されていることを示唆しています。
   - これらの変数が設定されているか確認するには、ターミナルで以下を実行します：
     ```bash
     env | grep -i proxy
     ```
     `HTTP_PROXY=socks://127.0.0.1:7891` や `HTTPS_PROXY=socks://127.0.0.1:7891` のような変数を探してください。

2. **システム全体のプロキシ設定**
   - Linuxシステムを使用している場合、プロキシ設定がグローバルに設定されている可能性があります（例：`/etc/environment`、`/etc/profile`、またはシェル設定ファイル`~/.bashrc`、`~/.zshrc`、`~/.profile`）。
   - これらのファイルで以下のような行を確認してください：
     ```bash
     export HTTP_PROXY="socks://127.0.0.1:7891"
     export HTTPS_PROXY="socks://127.0.0.1:7891"
     ```
   - 以下のコマンドでこれらのファイルを表示できます：
     ```bash
     cat ~/.bashrc | grep -i proxy
     cat ~/.zshrc | grep -i proxy
     cat /etc/environment | grep -i proxy
     ```

3. **プロキシツール内のプロキシ設定**
   - アドレス`127.0.0.1:7891`は、プロキシやVPNツール（Shadowsocks、V2Ray、Clashなど）で一般的に使用され、これらのツールは多くの場合、ポート7890や7891でSOCKS5プロキシを使用するようにデフォルト設定されています。
   - このようなツールをインストールまたは設定した場合、環境変数やシステムのプロキシ設定を自動的に設定している可能性があります。

4. **コード内の明示的なプロキシ設定**
   - 可能性は低いですが、`gitmessageai.py`スクリプトまたはそれが使用するライブラリが、明示的にプロキシを設定している可能性があります。エラーが`httpx`で発生しているため、スクリプトが`OpenAI`クライアントまたは`httpx`クライアントにプロキシを渡しているか確認してください。
   - スクリプト内で`proxy`、`proxies`、`httpx.Client`などの用語を検索してください：
     ```bash
     grep -r -i proxy /home/lzwjava/bin/gitmessageai.py
     ```

5. **Pythonライブラリの設定**
   - 一部のPythonライブラリ（例：`requests`や`httpx`）は、設定ファイルや以前の設定からプロキシ設定を継承する可能性があります。ただし、`httpx`は主に環境変数または明示的なコードに依存します。

### なぜ`socks://`が問題を引き起こすのか？

- `httpx`ライブラリ（`openai`で使用）は、追加の依存関係（`httpx-socks`など）がインストールされていない限り、ネイティブで`socks`スキーム（SOCKS4/SOCKS5プロキシ）をサポートしていません。
- エラー`Unknown scheme for proxy URL`は、`httpx`が`http://`や`https://`のようなスキームのプロキシを期待しているのに対し、`socks://`が使用されているために発生します。

### 問題の修正方法

プロキシが不要な場合は**プロキシを削除またはバイパス**するか、使用する必要がある場合は**SOCKSプロキシをサポート**するかの2つのオプションがあります。

#### オプション1：プロキシを削除またはバイパスする

DeepSeek APIにプロキシが不要な場合は、プロキシ設定を無効化またはバイパスできます。

1. **環境変数の設定を解除**
   - プロキシが環境変数に設定されている場合、セッションからそれらを解除します：
     ```bash
     unset HTTP_PROXY
     unset HTTPS_PROXY
     unset ALL_PROXY
     unset http_proxy
     unset https_proxy
     unset all_proxy
     ```
   - これを恒久的にするには、`~/.bashrc`、`~/.zshrc`、`/etc/environment`、または他のシェル設定ファイルから対応する`export`行を削除します。

2. **プロキシなしでスクリプトを実行**
   - 一時的にプロキシ設定なしでスクリプトを実行します：
     ```bash
     HTTP_PROXY= HTTPS_PROXY= ALL_PROXY= python3 /home/lzwjava/bin/gitmessageai.py
     ```
   - これが動作する場合、プロキシが問題でした。

3. **コード内でプロキシをバイパス**
   - `gitmessageai.py`スクリプトを修正して、`OpenAI`クライアントで明示的にプロキシを無効化します：
     ```python
     from openai import OpenAI
     import httpx

     def call_deepseek_api(prompt):
         api_key = os.getenv("DEEPSEEK_API_KEY")
         if not api_key:
             raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
         client = OpenAI(
             api_key=api_key,
             base_url="https://api.deepseek.com",
             http_client=httpx.Client(proxies=None)  # プロキシを無効化
         )
         # API呼び出しロジック
         response = client.chat.completions.create(
             model="deepseek",  # 正しいモデルに置き換え
             messages=[{"role": "user", "content": prompt}]
         )
         return response.choices[0].message.content
     ```
   - `proxies=None`を設定すると、`httpx`は環境変数のプロキシ設定を無視します。

#### オプション2：SOCKSプロキシをサポートする

SOCKSプロキシを使用する必要がある場合（例：VPNまたはプロキシサーバー経由でDeepSeek APIにアクセスするため）、`httpx`にSOCKSサポートを追加する必要があります。

1. **`httpx-socks`をインストール**
   - `httpx-socks`パッケージをインストールしてSOCKS4/SOCKS5プロキシサポートを有効にします：
     ```bash
     pip install httpx-socks
     ```
   - これにより、`httpx`が`socks://`および`socks5://`スキームを処理できるようになります。

2. **コードを更新**
   - スクリプトを修正して、明示的にSOCKSプロキシを使用するようにします：
     ```python
     from openai import OpenAI
     import httpx
     from httpx_socks import SyncProxyTransport

     def call_deepseek_api(prompt):
         api_key = os.getenv("DEEPSEEK_API_KEY")
         if not api_key:
             raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
         # SOCKS5プロキシを設定
         proxy_transport = SyncProxyTransport.from_url("socks5://127.0.0.1:7891")
         client = OpenAI(
             api_key=api_key,
             base_url="https://api.deepseek.com",
             http_client=httpx.Client(transport=proxy_transport)
         )
         # API呼び出しロジック
         response = client.chat.completions.create(
             model="deepseek",  # 正しいモデルに置き換え
             messages=[{"role": "user", "content": prompt}]
         )
         return response.choices[0].message.content
     ```
   - プロキシがSOCKS4を使用する場合は、`socks5://`を`socks4://`に置き換えてください。

3. **プロキシサーバーを確認**
   - `127.0.0.1:7891`のプロキシサーバーが実行されていることを確認してください。ClashやShadowsocksなどのツールを使用している場合、そのステータスを確認します：
     ```bash
     netstat -tuln | grep 7891
     ```
   - ポート7891をリッスンしているプロセスがない場合、プロキシツールを起動するか、プロキシURLのポートを修正してください。

### 追加のデバッグ手順

- **プロキシツールの設定を確認**
  - ClashやShadowsocksなどのプロキシツールを使用している場合、設定ファイル（例：`~/.config/clash/config.yaml`）を確認して、SOCKS5に`127.0.0.1:7891`を使用するように設定されていることを確認します。
  - ツールが実行中でアクセス可能であることを確認します。

- **プロキシ接続をテスト**
  - `curl`などのツールでプロキシをテストします（SOCKSサポート付きでビルドされた`curl`が必要）：
    ```bash
    curl --socks5 127.0.0.1:7891 https://api.deepseek.com
    ```
  - これが失敗する場合、プロキシサーバーがダウンしているか、誤って設定されています。

- **プロキシ使用状況をログに記録**
   - スクリプトにロギングを追加して、どのプロキシが使用されているかを確認します：
     ```python
     import logging
     logging.basicConfig(level=logging.DEBUG)
     ```

### 推奨される修正

プロキシが不要な場合、最も簡単な修正は環境変数を解除して以下を実行することです：
```bash
HTTP_PROXY= HTTPS_PROXY= ALL_PROXY= python3 /home/lzwjava/bin/gitmessageai.py
```

プロキシが必要な場合は、`httpx-socks`をインストールし、上記のように`SyncProxyTransport`を使用するようにコードを更新してください。

### 参考資料
- [httpx Documentation](https://www.python-httpx.org/advanced/#proxy-support)
- [httpx-socks GitHub](https://github.com/romis2012/httpx-socks)
- [DeepSeek API Documentation](https://platform.deepseek.com/docs)