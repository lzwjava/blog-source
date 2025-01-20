---
audio: true
lang: hant
layout: post
title: 阿里雲上的函數計算
translated: true
---

我已經使用阿里雲的函數計算設置了一個功能。我的目標是生成一些看起來正常的流量，以幫助隱藏我的代理服務器活動，避免被防火長城（GFW）檢測到。為此，我在代理服務器旁邊部署了一個帶寬服務器。現在，我正在使用阿里雲的函數計算每分鐘向這個帶寬API發送請求，從而創造出正常流量和代理流量的混合。

```python
from flask import Flask, request, jsonify
import requests
import time

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    # 記錄請求ID和其他詳細信息
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC 調用開始 RequestId: " + rid)
    data = request.stream.read()
    print("路徑: " + path)
    print("數據: " + str(data))

    # 初始化計數器
    start_time = time.time()  # 記錄開始時間
    duration = 60  # 運行1分鐘（60秒）
    total_calls = 0  # 跟踪總API調用次數
    successful_calls = 0  # 跟踪成功的API調用次數

    # 循環1分鐘
    while time.time() - start_time < duration:
        try:
            # 調用外部的/bandwidth API
            response = requests.get('https://www.lzwjava.xyz/bandwidth')
            response.raise_for_status()  # 對HTTP錯誤引發異常
            successful_calls += 1  # 增加成功調用計數器
        except Exception as e:
            print("獲取帶寬數據時出錯:", e)
        finally:
            total_calls += 1  # 增加總調用計數器

        # 在下一次請求前等待5秒
        time.sleep(5)

    # 記錄請求結束
    print("FC 調用結束 RequestId: " + rid)

    # 返回調用次數和成功調用次數
    return jsonify({
        "message": "你好，世界！",
        "total_calls": total_calls,
        "successful_calls": successful_calls
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```