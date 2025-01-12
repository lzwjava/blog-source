---
audio: true
lang: hant
layout: post
title: 代理服务器封锁分析
---

## 代理服务器中的API能否规避GFW的封锁？

我在Shadowsocks实例上运行了一个简单的服务器，代码如下：

```python
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
```

app = Flask(__name__)
CORS(app)  # 为所有路由启用CORS

@app.route('/bandwidth', methods=['GET'])
def get_bandwidth():
    # 运行vnstat命令以获取eth0接口的5分钟间隔流量统计
    result = subprocess.run(['vnstat', '-i', 'eth0', '-5', '--json'], capture_output=True, text=True)
    data = result.stdout

    # 將捕獲的數據作為 JSON 回應返回
    return jsonify(data)

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

而我使用nginx来提供443端口的服务，如下所示：

```bash
server {
    listen 443 ssl;
    server_name www.some-domain.xyz;
```

    ssl_certificate /etc/letsencrypt/live/www.some-domain.xyz/fullchain.pem; # 由 
    # ...
    location / {

```nginx
        proxy_pass http://127.0.0.1:5000/;
        # ...
    }
}
```

该服务器程序提供网络数据，我将此服务器作为我的代理服务器，使我能够利用这些网络数据在我的博客上展示我的在线状态。

有趣的是，这个服务器已经连续几天没有被防火长城（GFW）或其他网络控制系统封锁了。通常情况下，我设置的代理服务器在一两天内就会被封禁。该服务器在一个端口（如51939）上运行着Shadowsocks程序，因此它的流量是Shadowsocks与常规API流量的混合。这种混合流量似乎让GFW误以为该服务器并非专门的代理服务器，而是一个普通服务器，从而避免了IP被封锁的命运。

这个观察很有意思。GFW似乎使用了特定的逻辑来区分代理流量和正常流量。虽然像Twitter和YouTube这样的许多网站在中国被屏蔽，但许多外国网站——比如国际大学和公司的网站——仍然可以访问。

这表明，GFW 很可能基于区分正常 HTTP/HTTPS 流量和代理相关流量的规则来运作。同时处理这两种流量的服务器似乎能避免被封禁，而仅处理代理流量的服务器则更有可能被封锁。

一个关键问题是，GFW在封禁前累积数据的时间范围是多久——是一天还是一小时。在这个时间段内，它会检测流量是否仅来自代理。如果是，服务器的IP就会被封禁。

我经常访问我的博客以回顾所写内容，但在接下来的几周里，我的注意力将转向其他任务，而非撰写博客文章。这将减少我通过443端口访问`bandwidth` API的机会。如果我发现自己再次被封锁，我应该编写一个程序，定期访问这个API，以此来迷惑防火长城。

以下是您文本的优化版本，结构更佳，表达更清晰：

## 中国防火长城（GFW）的工作原理

### 第一步：记录请求

```python
import time
```

# 用于存储请求数据的数据库
request_log = []

# 記錄請求的函數
def log_request(source_ip, target_ip, target_port, body):
    request_log.append({
        'source_ip': source_ip,
        'target_ip': target_ip,
        'target_port': target_port,
        'body': body,
        'timestamp': time.time()
    })
```

`log_request` 函数记录传入的请求，包含关键信息如源IP、目标IP、目标端口、请求体和时间戳。

### 第二步：检查并封禁IP地址

```python
# 检查请求并封禁IP的函数
def check_and_ban_ips():
    banned_ips = set()
```

    # 遍歷所有記錄的請求
    for request in request_log:
        if is_illegal(request):
            banned_ips.add(request['target_ip'])
        else:
            banned_ips.discard(request['target_ip'])

    # 對所有識別出的IP套用封鎖
    ban_ips(banned_ips)
```

`check_and_ban_ips` 函数会遍历所有记录的请求，识别并封禁与非法活动相关联的IP地址。

### 第三步：定义何为非法请求

```python
# 函數用於模擬檢查請求是否非法
def is_illegal(request):
    # 實際非法請求檢查邏輯的佔位符
    # 例如，檢查請求主體或目標
    return "illegal" in request['body']
```

在这里，`is_illegal` 函数用于检查请求体中是否包含“非法”一词。根据非法活动的具体定义，这一逻辑可以扩展为更为复杂的判断。

### 第四步：封禁已识别的IP地址

```python
# 函數：封鎖一組IP地址
def ban_ips(ip_set):
    for ip in ip_set:
        print(f"正在封鎖IP: {ip}")
```

一旦识别出非法IP地址，`ban_ips`函数就会通过打印这些IP地址来封禁它们（或者，在实际系统中，可以执行封禁操作）。

### 步骤5：基于80%非法请求检查和封禁IP的替代方法

```python
# 函數用於檢查請求並根據80%非法請求封禁IP
def check_and_ban_ips():
    banned_ips = set()
    illegal_count = 0
    total_requests = 0
```

    # 遍歷所有記錄的請求
    for request in request_log:
        total_requests += 1
        if is_illegal(request):
            illegal_count += 1

    # 如果80%或以上的请求是非法的，则封禁这些IP
    if total_requests > 0 and (illegal_count / total_requests) >= 0.8:
        for request in request_log:
            if is_illegal(request):
                banned_ips.add(request['target_ip'])

    # 對所有識別出的IP實施封禁
    ban_ips(banned_ips)
```

此替代方法依据非法请求的比例来判断是否应封禁IP。若某IP发出的请求中有80%及以上为非法，则予以封禁。

### 步骤6：增强非法请求检查（例如，Shadowsocks和Trojan协议检测）

```python
def is_illegal(request):
    # 檢查請求是否使用了Shadowsocks協議（主體包含類似二進制數據）
    if request['target_port'] == 443:
        if is_trojan(request):
            return True
    elif is_shadowsocks(request):
        return True
    return False
```

`is_illegal` 函数现在还会检查特定的协议，如 Shadowsocks 和 Trojan：
- **Shadowsocks**：我们可能会检查请求体中的加密或类似二进制数据。
- **Trojan**：如果请求通过 443 端口（HTTPS）传输，并且匹配特定模式（例如，Trojan 流量的特征），则会被标记为非法。

### 步骤7：法律请求示例

例如，像 `GET https://some-domain.xyz/bandwidth` 这样的请求肯定是合法的，不会触发封禁机制。

### 步骤8：代理服务器流量特征分析

代理服务器的流量特征与常规的网页或API服务器大相径庭。防火墙需具备区分正常网页服务器流量与代理服务器流量的能力，因为两者在流量表现上可能截然不同。

### 第9步：用于智能检测的机器学习与AI模型

鉴于互联网上传递的请求和响应种类繁多，防火墙（GFW）可以利用人工智能和机器学习模型来分析流量模式，智能地检测非法行为。通过训练系统识别多种流量类型，并运用先进技术，它能够基于观察到的模式更有效地禁止或过滤流量。

