---
audio: true
lang: zh
layout: post
title: 阿里云函数计算
translated: true
---

我已经使用阿里云的函数计算（Function Compute）设置了一个函数。我的目标是生成一些看起来正常的流量，以帮助掩盖我的代理服务器在GFW（防火长城）下的活动。为此，我在代理服务器旁边部署了一个带宽服务器。现在，我使用阿里云的函数计算每分钟向这个带宽API发起请求，从而混合正常流量和代理流量。

```python
from flask import Flask, request, jsonify
import requests
import time

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    # 记录请求ID和其他详细信息
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)
    data = request.stream.read()
    print("Path: " + path)
    print("Data: " + str(data))

    # 初始化计数器
    start_time = time.time()  # 记录开始时间
    duration = 60  # 运行1分钟（60秒）
    total_calls = 0  # 跟踪总API调用次数
    successful_calls = 0  # 跟踪成功的API调用次数

    # 循环1分钟
    while time.time() - start_time < duration:
        try:
            # 调用外部的/bandwidth API
            response = requests.get('https://www.lzwjava.xyz/bandwidth')
            response.raise_for_status()  # 抛出HTTP错误异常
            successful_calls += 1  # 增加成功调用计数器
        except Exception as e:
            print("获取带宽数据时出错:", e)
        finally:
            total_calls += 1  # 增加总调用计数器

        # 等待5秒再进行下一次请求
        time.sleep(5)

    # 记录请求结束
    print("FC Invoke End RequestId: " + rid)

    # 返回调用次数和成功调用次数
    return jsonify({
        "message": "Hello, World!",
        "total_calls": total_calls,
        "successful_calls": successful_calls
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```