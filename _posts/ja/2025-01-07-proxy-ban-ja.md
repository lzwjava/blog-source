---
audio: false
generated: false
lang: ja
layout: post
title: プロキシサーバーの禁止に関する分析
translated: true
---

## プロキシサーバーのAPIはGFWのブロックを回避できるか？

私はShadowsocksインスタンス上で以下のコードを使って簡単なサーバーを実行しています：

```python
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # すべてのルートでCORSを有効にする

@app.route('/bandwidth', methods=['GET'])
def get_bandwidth():
    # vnstatコマンドを実行してeth0の5分間隔のトラフィック統計を取得
    result = subprocess.run(['vnstat', '-i', 'eth0', '-5', '--json'], capture_output=True, text=True)
    data = result.stdout

    # 取得したデータをJSONレスポンスとして返す
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

そして、以下のようにnginxを使ってポート443を提供しています：

```bash
server {
    listen 443 ssl;
    server_name www.some-domain.xyz;

    ssl_certificate /etc/letsencrypt/live/www.some-domain.xyz/fullchain.pem; # managed by 
    # ...
    location / {

        proxy_pass http://127.0.0.1:5000/;
        # ...
    }
}
```

このサーバープログラムはネットワークデータを提供し、私はこのサーバーをプロキシサーバーとして使用し、ネットワークデータを使ってブログに自分のオンラインステータスを表示しています。

興味深いことに、このサーバーは数日間、Great Firewall（GFW）やその他のネットワーク制御システムによってブロックされていません。通常、私が設定したプロキシサーバーは1日か2日でブロックされます。このサーバーは51939のようなポートでShadowsocksプログラムを実行しているため、Shadowsocksのトラフィックと通常のAPIトラフィックが混在しています。この混在により、GFWはこのサーバーが専用のプロキシではなく通常のサーバーであると認識し、IPをブロックしないようです。

この観察は興味深いものです。GFWは特定のロジックを使ってプロキシトラフィックと通常のトラフィックを区別しているようです。TwitterやYouTubeのような多くのウェブサイトは中国でブロックされていますが、多くの外国のウェブサイト—例えば国際的な大学や企業のウェブサイト—はアクセス可能です。

これは、GFWが通常のHTTP/HTTPSトラフィックとプロキシ関連のトラフィックを区別するルールに基づいて動作していることを示唆しています。両方のタイプのトラフィックを処理するサーバーはブロックを回避するようですが、プロキシトラフィックのみを処理するサーバーはブロックされる可能性が高いです。

一つ疑問なのは、GFWがブロックのためにデータを蓄積する時間範囲が1日なのか1時間なのかということです。この時間範囲内で、トラフィックがプロキシからのものであるかどうかを検出します。もしそうであれば、サーバーのIPがブロックされます。

私はよく自分のブログを訪れて書いた内容を確認しますが、今後数週間はブログ記事を書くのではなく他のタスクに集中する予定です。これにより、ポート443を通じて`bandwidth` APIにアクセスする回数が減ります。もし再びブロックされることがわかったら、このAPIに定期的にアクセスするプログラムを書いてGFWを欺くべきでしょう。

以下は、テキストの構造と明瞭さを改善したバージョンです：

## Great Firewall（GFW）の仕組み

### ステップ1: リクエストのロギング

```python
import time

# リクエストデータを保存するデータベース
request_log = []

# リクエストをログに記録する関数
def log_request(source_ip, target_ip, target_port, body):
    request_log.append({
        'source_ip': source_ip,
        'target_ip': target_ip,
        'target_port': target_port,
        'body': body,
        'timestamp': time.time()
    })
```

`log_request`関数は、送信元IP、ターゲットIP、ターゲットポート、リクエストボディ、タイムスタンプなどの重要な情報を含む着信リクエストを記録します。

### ステップ2: IPのチェックとブロック

```python
# リクエストをチェックし、IPをブロックする関数
def check_and_ban_ips():
    banned_ips = set()

    # すべてのログに記録されたリクエストを繰り返し処理
    for request in request_log:
        if is_illegal(request):
            banned_ips.add(request['target_ip'])
        else:
            banned_ips.discard(request['target_ip'])

    # 識別されたすべてのIPにブロックを適用
    ban_ips(banned_ips)
```

`check_and_ban_ips`関数は、すべてのログに記録されたリクエストを繰り返し処理し、違法な活動に関連するIPを識別してブロックします。

### ステップ3: リクエストが違法かどうかを定義

```python
# リクエストが違法かどうかをチェックする関数
def is_illegal(request):
    # 実際の違法リクエストチェックロジックのプレースホルダー
    # 例えば、リクエストボディやターゲットをチェック
    return "illegal" in request['body']
```

ここで、`is_illegal`はリクエストボディに「illegal」という単語が含まれているかどうかをチェックします。これは、違法な活動を構成するものに応じて、より洗練されたロジックに拡張できます。

### ステップ4: 識別されたIPをブロック

```python
# IPリストをブロックする関数
def ban_ips(ip_set):
    for ip in ip_set:
        print(f"Banning IP: {ip}")
```

違法なIPが識別されると、`ban_ips`関数はそれらのIPをブロックします（実際のシステムでは、それらをブロックする可能性があります）。

### ステップ5: 80%の違法リクエストに基づくIPのチェックとブロックの代替方法

```python
# 80%以上の違法リクエストに基づいてIPをチェックし、ブロックする関数
def check_and_ban_ips():
    banned_ips = set()
    illegal_count = 0
    total_requests = 0

    # すべてのログに記録されたリクエストを繰り返し処理
    for request in request_log:
        total_requests += 1
        if is_illegal(request):
            illegal_count += 1

    # リクエストの80%以上が違法であれば、それらのIPをブロック
    if total_requests > 0 and (illegal_count / total_requests) >= 0.8:
        for request in request_log:
            if is_illegal(request):
                banned_ips.add(request['target_ip'])

    # 識別されたすべてのIPにブロックを適用
    ban_ips(banned_ips)
```

この代替方法は、IPがブロックされるべきかどうかを違法リクエストの割合に基づいて評価します。IPからのリクエストの80%以上が違法であれば、そのIPはブロックされます。

### ステップ6: 違法リクエストチェックの強化（例：ShadowsocksとTrojanプロトコルの検出）

```python
def is_illegal(request):
    # リクエストがShadowsocksプロトコルを使用しているかチェック（ボディにバイナリのようなデータが含まれているか）
    if request['target_port'] == 443:
        if is_trojan(request):
            return True
    elif is_shadowsocks(request):
        return True
    return False
```

`is_illegal`関数は、ShadowsocksやTrojanのような特定のプロトコルもチェックするようになりました：
- **Shadowsocks**: リクエストボディに暗号化されたデータやバイナリのようなデータが含まれているかどうかをチェックするかもしれません。
- **Trojan**: リクエストがポート443（HTTPS）経由で送信され、特定のパターン（例：Trojanトラフィックの特性）に一致する場合、違法としてフラグが立てられます。

### ステップ7: 合法リクエストの例

例えば、`GET https://some-domain.xyz/bandwidth`のようなリクエストは確実に合法であり、ブロックメカニズムをトリガーしません。

### ステップ8: プロキシサーバーのトラフィック特性

プロキシサーバーは、通常のウェブサーバーやAPIサーバーとは非常に異なるトラフィック特性を持っています。GFWは、通常のウェブサーバートラフィックとプロキシサーバートラフィックを区別する必要があり、これらは完全に異なるように見えることがあります。

### ステップ9: スマート検出のための機械学習とAIモデル

インターネットを通過するさまざまなリクエストとレスポンスの範囲を考えると、GFWはAIや機械学習モデルを使用してトラフィックパターンを分析し、違法な行動をインテリジェントに検出する可能性があります。システムをさまざまなタイプのトラフィックでトレーニングし、高度な技術を使用することで、観察されたパターンに基づいてトラフィックをより効果的にブロックまたはフィルタリングできます。

## 更新

私の努力にもかかわらず、私のプロキシサーバーは引き続きブロックされています。これを緩和するために、Digital Oceanの逆IP機能を使用して、ブロックが発生するたびに迅速に新しいIPアドレスを割り当てる回避策を実装しました。