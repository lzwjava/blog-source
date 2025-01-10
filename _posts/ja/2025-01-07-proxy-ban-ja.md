---
audio: true
lang: ja
layout: post
title: プロキシサーバーの禁止分析
translated: true
---

## プロキシサーバーのAPIはGFWの禁止を回避できるか？

私はShadowsocksインスタンス上で、以下のコードを使ってシンプルなサーバーを実行しています：

```python
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
```

```python
app = Flask(__name__)
CORS(app)  # すべてのルートに対してCORSを有効にする
```

```python
@app.route('/bandwidth', methods=['GET'])
def get_bandwidth():
    # eth0の5分間隔のトラフィック統計を取得するためにvnstatコマンドを実行
    result = subprocess.run(['vnstat', '-i', 'eth0', '-5', '--json'], capture_output=True, text=True)
    data = result.stdout
```

    # キャプチャしたデータをJSONレスポンスとして返す
    return jsonify(data)

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

そして、以下のようにnginxを使用してポート443を提供しています：

```bash
server {
    listen 443 ssl;
    server_name www.some-domain.xyz;
```

    ssl_certificate /etc/letsencrypt/live/www.some-domain.xyz/fullchain.pem; # managed by 
    # ...
    location / {

```nginx
        proxy_pass http://127.0.0.1:5000/;
        # ...
    }
}
```

このサーバープログラムはネットワークデータを提供し、私はそのサーバーをプロキシサーバーとして使用しています。これにより、ブログ上でネットワークデータを使って自分のオンラインステータスを表示することができます。

興味深いことに、このサーバーは数日間、Great Firewall（GFW）やその他のネットワーク制御システムによってブロックされていません。通常、私が設定したプロキシサーバーは1日か2日でブロックされてしまいます。このサーバーはポート51939などでShadowsocksプログラムを実行しており、Shadowsocksのトラフィックと通常のAPIトラフィックが混在しています。この混合により、GFWはこのサーバーが専用のプロキシではなく、通常のサーバーであると認識し、IPをブロックしないようです。

この観察は興味深いものです。GFW（Great Firewall）は、プロキシトラフィックと通常のトラフィックを区別するために特定のロジックを使用しているようです。TwitterやYouTubeなどの多くのウェブサイトが中国でブロックされている一方で、国際的な大学や企業のウェブサイトなど、多くの外国のウェブサイトはアクセス可能なままです。

これは、GFWが通常のHTTP/HTTPSトラフィックとプロキシ関連のトラフィックを区別するルールに基づいて動作している可能性を示唆しています。両方のタイプのトラフィックを処理するサーバーは禁止を回避しているように見えますが、プロキシトラフィックのみを処理するサーバーはブロックされる可能性が高いです。

一つの疑問は、GFWがデータを蓄積してブロックするための時間範囲がどれくらいか、つまり1日なのか1時間なのかということです。この時間範囲内で、トラフィックがプロキシからのものだけかどうかを検出します。もしそうであれば、そのサーバーのIPはブロックされます。

私はよく自分のブログを訪れて、書いた内容を振り返りますが、これから数週間はブログ記事を書くことよりも他のタスクに集中する予定です。これにより、ポート443を通じて`bandwidth` APIにアクセスする頻度が減ることになります。もし再びブロックされてしまうようなことがあれば、GFWを欺くために定期的にこのAPIにアクセスするプログラムを書くべきかもしれません。

以下は、構造と明瞭さを改善したテキストの洗練されたバージョンです：

## グレート・ファイアウォール（GFW）の仕組み

### ステップ1: リクエストのロギング

```python
import time
```

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

`log_request`関数は、送信元IP、宛先IP、宛先ポート、リクエストボディ、タイムスタンプなどの重要な情報と共に、受信したリクエストを記録します。

### ステップ2: IPの確認と禁止

```python
# リクエストをチェックし、IPをブロックする関数
def check_and_ban_ips():
    banned_ips = set()
```

    # ログに記録されたすべてのリクエストを反復処理する
    for request in request_log:
        if is_illegal(request):
            banned_ips.add(request['target_ip'])
        else:
            banned_ips.discard(request['target_ip'])

    # 特定されたすべてのIPに禁止を適用する
    ban_ips(banned_ips)
```

`check_and_ban_ips`関数は、ログに記録されたすべてのリクエストを繰り返し処理し、違法な活動に関連付けられたIPアドレスを特定して禁止します。

### ステップ3: 違法なリクエストの定義

```python
# リクエストが違法かどうかをシミュレートする関数
def is_illegal(request):
    # 実際の違法リクエストチェックロジックのプレースホルダー
    # 例: リクエストの本文やターゲットをチェックする
    return "illegal" in request['body']
```

ここで、`is_illegal`はリクエストボディに「illegal」という単語が含まれているかどうかをチェックします。これは、違法行為と見なされる内容に応じて、より洗練されたロジックに拡張することができます。

### ステップ4: 特定されたIPのブロック

```python
# IPリストをブロックする関数
def ban_ips(ip_set):
    for ip in ip_set:
        print(f"IPをブロック中: {ip}")
```

不正なIPアドレスが特定されると、`ban_ips`関数はそれらのIPアドレスを表示して（または、実際のシステムではブロックするなどして）禁止します。

### ステップ5: 80%の不正リクエストに基づくIPのチェックと禁止の代替方法

```python
# 80%の不正リクエストに基づいてIPをチェックし、禁止する関数
def check_and_ban_ips():
    banned_ips = set()
    illegal_count = 0
    total_requests = 0
```

    # ログに記録されたすべてのリクエストを繰り返し処理する
    for request in request_log:
        total_requests += 1
        if is_illegal(request):
            illegal_count += 1

    # リクエストの80%以上が不正な場合、それらのIPを禁止する
    if total_requests > 0 and (illegal_count / total_requests) >= 0.8:
        for request in request_log:
            if is_illegal(request):
                banned_ips.add(request['target_ip'])

    # 特定されたすべてのIPに禁止を適用する
    ban_ips(banned_ips)
```

この代替方法では、IPアドレスからの不正なリクエストの割合に基づいて、そのIPを禁止するかどうかを評価します。あるIPからのリクエストの80%以上が不正な場合、そのIPは禁止されます。

### ステップ6: 不正なリクエストの強化チェック（例: ShadowsocksおよびTrojanプロトコルの検出）

```python
def is_illegal(request):
    # リクエストがShadowsocksプロトコルを使用しているか確認（ボディにバイナリのようなデータが含まれているか）
    if request['target_port'] == 443:
        if is_trojan(request):
            return True
    elif is_shadowsocks(request):
        return True
    return False
```

`is_illegal`関数は、ShadowsocksやTrojanなどの特定のプロトコルもチェックするようになりました：
- **Shadowsocks**: リクエストボディ内に暗号化されたデータやバイナリのようなデータがあるかどうかをチェックします。
- **Trojan**: リクエストがポート443（HTTPS）経由で送信され、特定のパターン（例：Trojanのトラフィック特性）に一致する場合、違法と判定されます。

### ステップ7: 法的リクエストの例

例えば、`GET https://some-domain.xyz/bandwidth` のようなリクエストは確実に合法であり、禁止メカニズムを引き起こすことはありません。

### ステップ8: プロキシサーバーのトラフィック特性

プロキシサーバーは、通常のウェブサーバーやAPIサーバーとは非常に異なるトラフィック特性を持っています。GFW（Great Firewall）は、通常のウェブサーバーのトラフィックとプロキシサーバーのトラフィックを区別する必要がありますが、これらは全く異なる見た目をしていることがあります。

### ステップ9: スマート検出のための機械学習とAIモデル

インターネットを通過する多様なリクエストとレスポンスを考慮すると、GFWはAIや機械学習モデルを活用してトラフィックパターンを分析し、違法行為を知的に検出することが可能です。システムを様々なトラフィックタイプで訓練し、高度な技術を用いることで、観察されたパターンに基づいてトラフィックをより効果的に禁止またはフィルタリングすることができるでしょう。

