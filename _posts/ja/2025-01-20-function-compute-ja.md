---
audio: false
generated: false
lang: ja
layout: post
title: Alibaba CloudのFunction Compute
translated: true
---

私はAlibaba CloudのFunction Computeを使用して、通常のトラフィックのように見えるトラフィックを生成しています。これにより、プロキシサーバーの活動をGFWから隠蔽するのに役立っています。プロキシと一緒に帯域幅サーバーをデプロイし、このFunction Compute関数は毎分帯域幅APIにリクエストを送信します。これにより、通常のトラフィックとプロキシトラフィックが混在します。

```python
from flask import Flask, request, jsonify
import requests
import concurrent.futures

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

# 外部APIを呼び出す関数
def call_bandwidth_api():
    try:
        response = requests.get('https://www.lzwjava.xyz/bandwidth')
        response.raise_for_status()  # HTTPエラーが発生した場合に例外を発生させる
        return True  # 成功を示す
    except Exception as e:
        print("帯域幅データの取得中にエラーが発生しました:", e)
        return False  # 失敗を示す

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    # リクエストIDとその他の詳細をログに記録
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)
    data = request.stream.read()
    print("Path: " + path)
    print("Data: " + str(data))

    # カウンターを初期化
    total_calls = 10  # 実行するAPI呼び出しの総数
    successful_calls = 0  # 成功したAPI呼び出しを追跡

    # ThreadPoolExecutorを使用してAPIを10回並行して呼び出す
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # タスクをエグゼキューターに提出
        futures = [executor.submit(call_bandwidth_api) for _ in range(total_calls)]

        # すべてのタスクが完了するのを待ち、成功をカウント
        for future in concurrent.futures.as_completed(futures):
            if future.result():  # 呼び出しが成功した場合
                successful_calls += 1

    # リクエストの終了をログに記録
    print("FC Invoke End RequestId: " + rid)

    # 呼び出し回数と成功回数を返す
    return jsonify({
        "message": "Hello, World!",
        "total_calls": total_calls,
        "successful_calls": successful_calls
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```