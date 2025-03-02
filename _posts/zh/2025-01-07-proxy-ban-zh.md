---
audio: true
generated: false
lang: zh
layout: post
title: 代理服务器封禁分析
translated: true
---

## 代理服务器中的API能否避免GFW的封锁？

我在我的Shadowsocks实例上运行了一个简单的服务器，代码如下：

```python
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # 为所有路由启用CORS

@app.route('/bandwidth', methods=['GET'])
def get_bandwidth():
    # 运行vnstat命令获取eth0的5分钟间隔流量统计
    result = subprocess.run(['vnstat', '-i', 'eth0', '-5', '--json'], capture_output=True, text=True)
    data = result.stdout

    # 将捕获的数据作为JSON响应返回
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

并且我使用nginx来服务443端口，如下所示：

```bash
server {
    listen 443 ssl;
    server_name www.some-domain.xyz;

    ssl_certificate /etc/letsencrypt/live/www.some-domain.xyz/fullchain.pem; # 由
    # ...
    location / {

        proxy_pass http://127.0.0.1:5000/;
        # ...
    }
}
```

这个服务器程序提供网络数据，我将该服务器用作我的代理服务器，使我能够利用网络数据在我的博客上显示我的在线状态。

有趣的是，这个服务器已经连续几天没有被防火墙（GFW）或其他网络控制系统封锁。通常情况下，我设置的代理服务器会在一两天内被封锁。该服务器在51939等端口上运行Shadowsocks程序，因此它混合了Shadowsocks流量和常规API流量。这种混合似乎让GFW认为该服务器不是专用代理，而是一个普通服务器，从而避免了对IP的封锁。

这一观察非常有趣。似乎GFW使用特定的逻辑来区分代理流量和常规流量。虽然许多网站如Twitter和YouTube在中国被封锁，但许多外国网站——如国际大学和公司的网站——仍然可以访问。

这表明GFW可能基于规则来区分正常的HTTP/HTTPS流量和代理相关的流量。处理这两种流量的服务器似乎可以避免被封锁，而仅处理代理流量的服务器则更有可能被封锁。

一个问题是GFW使用多长时间范围来累积数据以进行封锁——是一天还是一小时。在这个时间范围内，它会检测流量是否完全来自代理。如果是，服务器的IP就会被封锁。

我经常访问我的博客以查看我写的内容，但在接下来的几周里，我的注意力将转移到其他任务上，而不是写博客文章。这将减少我通过443端口访问`bandwidth` API的次数。如果我发现再次被封锁，我应该编写一个程序来定期访问这个API，以欺骗GFW。

以下是经过改进和清晰化的文本版本：

## 防火墙（GFW）的工作原理

### 第一步：记录请求

```python
import time

# 存储请求数据的数据库
request_log = []

# 记录请求的函数
def log_request(source_ip, target_ip, target_port, body):
    request_log.append({
        'source_ip': source_ip,
        'target_ip': target_ip,
        'target_port': target_port,
        'body': body,
        'timestamp': time.time()
    })
```

`log_request`函数记录传入的请求，包括源IP、目标IP、目标端口、请求体和时间戳等关键信息。

### 第二步：检查并封锁IP

```python
# 检查请求并封锁IP的函数
def check_and_ban_ips():
    banned_ips = set()

    # 遍历所有记录的请求
    for request in request_log:
        if is_illegal(request):
            banned_ips.add(request['target_ip'])
        else:
            banned_ips.discard(request['target_ip'])

    # 对所有识别的IP应用封锁
    ban_ips(banned_ips)
```

`check_and_ban_ips`函数遍历所有记录的请求，识别并封锁与非法活动相关的IP。

### 第三步：定义什么是非法请求

```python
# 模拟检查请求是否非法的函数
def is_illegal(request):
    # 实际非法请求检查逻辑的占位符
    # 例如，检查请求体或目标
    return "illegal" in request['body']
```

在这里，`is_illegal`检查请求体中是否包含单词“illegal”。这可以根据非法活动的定义扩展到更复杂的逻辑。

### 第四步：封锁识别的IP

```python
# 封锁IP列表的函数
def ban_ips(ip_set):
    for ip in ip_set:
        print(f"封锁IP: {ip}")
```

一旦识别出非法IP，`ban_ips`函数通过打印其IP地址（或在真实系统中，可以阻止它们）来封锁它们。

### 第五步：基于80%非法请求的检查和封锁IP的替代方法

```python
# 基于80%非法请求检查和封锁IP的函数
def check_and_ban_ips():
    banned_ips = set()
    illegal_count = 0
    total_requests = 0

    # 遍历所有记录的请求
    for request in request_log:
        total_requests += 1
        if is_illegal(request):
            illegal_count += 1

    # 如果80%或更多的请求是非法请求，则封锁这些IP
    if total_requests > 0 and (illegal_count / total_requests) >= 0.8:
        for request in request_log:
            if is_illegal(request):
                banned_ips.add(request['target_ip'])

    # 对所有识别的IP应用封锁
    ban_ips(banned_ips)
```

这种替代方法根据非法请求的百分比评估是否应封锁IP。如果来自某个IP的80%或更多的请求是非法请求，则封锁该IP。

### 第六步：增强的非法请求检查（例如，Shadowsocks和Trojan协议检测）

```python
def is_illegal(request):
    # 检查请求是否使用Shadowsocks协议（请求体包含类似二进制数据）
    if request['target_port'] == 443:
        if is_trojan(request):
            return True
    elif is_shadowsocks(request):
        return True
    return False
```

`is_illegal`函数现在还检查特定协议，如Shadowsocks和Trojan：
- **Shadowsocks**：我们可能会检查请求体中是否包含加密或类似二进制数据。
- **Trojan**：如果请求通过443端口（HTTPS）并且匹配特定模式（例如，Trojan流量特征），则标记为非法。

### 第七步：合法请求示例

例如，像`GET https://some-domain.xyz/bandwidth`这样的请求肯定是合法的，不会触发封锁机制。

### 第八步：代理服务器流量的特征

代理服务器的流量特征与常规Web或API服务器非常不同。GFW需要区分正常Web服务器流量和代理服务器流量，这两者可能看起来完全不同。

### 第九步：用于智能检测的机器学习和AI模型

鉴于通过互联网传递的请求和响应种类繁多，GFW可以采用AI和机器学习模型来分析流量模式，并智能地检测非法行为。通过在多种流量类型上训练系统并使用先进技术，它可以更有效地根据观察到的模式封锁或过滤流量。

## 更新

尽管我做出了努力，我的代理服务器仍然被封锁。为了缓解这个问题，我使用了Digital Ocean的反向IP功能，每当发生封锁时，我可以快速分配一个新的IP地址。