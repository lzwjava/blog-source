---
audio: false
generated: true
lang: hant
layout: post
title: 阿里雲上的函數計算
translated: true
---

我正在使用阿里雲的函數計算來生成看似正常的流量，這有助於隱藏我的代理伺服器活動，使其不被防火長城（GFW）察覺。我在代理伺服器旁部署了一個頻寬伺服器，這個函數計算功能每分鐘都會向頻寬API發送請求。這樣就產生了正常流量和代理流量的混合。

```python
from flask import Flask, request, jsonify
import requests
import concurrent.futures

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

# 呼叫外部API的函數
def call_bandwidth_api():
    try:
        response = requests.get('https://www.lzwjava.xyz/bandwidth')
        response.raise_for_status()  # 對HTTP錯誤引發異常
        return True  # 表示成功
    except Exception as e:
        print("獲取頻寬數據時出錯:", e)
        return False  # 表示失敗

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    # 記錄請求ID和其他詳細信息
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC調用開始 RequestId: " + rid)
    data = request.stream.read()
    print("路徑: " + path)
    print("數據: " + str(data))

    # 初始化計數器
    total_calls = 10  # 總共要進行的API呼叫次數
    successful_calls = 0  # 追蹤成功的API呼叫

    # 使用ThreadPoolExecutor並行呼叫API 10次
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 向執行器提交任務
        futures = [executor.submit(call_bandwidth_api) for _ in range(total_calls)]

        # 等待所有任務完成並計算成功次數
        for future in concurrent.futures.as_completed(futures):
            if future.result():  # 如果呼叫成功
                successful_calls += 1

    # 記錄請求結束
    print("FC調用結束 RequestId: " + rid)

    # 返回呼叫次數和成功次數
    return jsonify({
        "message": "你好，世界！",
        "total_calls": total_calls,
        "successful_calls": successful_calls
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```