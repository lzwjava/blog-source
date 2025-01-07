---
audio: true
lang: zh
layout: post
title: 代理服务器封禁分析
---

## 代理服务器中的API能避免GFW封禁吗？

我在我的Shadowsocks实例上运行了一个简单的服务器，代码如下：

```python
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # 启用所有路由的CORS

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

然后，我使用nginx将443端口进行代理，如下所示：

```bash
server {
    listen 443 ssl;
    server_name www.some-domain.xyz;

    ssl_certificate /etc/letsencrypt/live/www.some-domain.xyz/fullchain.pem; # 由Let’s Encrypt管理
    # ...
    location / {

        proxy_pass http://127.0.0.1:5000/;
        # ...
    }
}
```

该服务器程序提供网络数据，我将其用作我的代理服务器，允许我使用网络数据在我的博客上显示在线状态。

有趣的是，这个服务器几天来没有被中国的防火长城（GFW）或任何其他网络控制系统封禁。通常，我设置的代理服务器会在一两天内被封禁。该服务器运行在像51939这样的端口上，运行Shadowsocks程序，因此它的流量混合了Shadowsocks流量和常规API流量。这种混合似乎让GFW认为该服务器不是一个专门的代理服务器，而是一个普通服务器，从而防止了其封禁该IP。

这个观察结果很有意思。似乎GFW使用特定的逻辑来区分代理流量和常规流量。虽然许多网站如Twitter和YouTube在中国被封锁，但许多外国网站——如国际大学和公司的官网——仍然可以访问。

这表明，GFW很可能基于规则区分正常的HTTP/HTTPS流量和代理相关的流量。处理两种流量的服务器似乎能够避免封禁，而仅处理代理流量的服务器更可能被封锁。

一个问题是GFW用来积累封禁数据的时间范围是什么——是一天还是一小时。在这个时间范围内，GFW会检测流量是否完全来自代理。如果是，服务器的IP会被封禁。

我经常访问我的博客，回顾我写的内容，但在接下来的几周里，我的重点将转向其他任务，而不是写博客文章。这将减少我通过443端口访问`bandwidth` API的次数。如果我发现再次被封禁，我应该写一个程序定期访问此API，以欺骗GFW。

这是你文本的改进版本，结构和清晰度得到提升：

## GFW是如何工作的

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

`log_request`函数记录传入请求的关键信息，如源IP、目标IP、目标端口、请求体和时间戳。

### 第二步：检查并封禁IP

```python
# 检查请求并封禁IP的函数
def check_and_ban_ips():
    banned_ips = set()

    # 遍历所有记录的请求
    for request in request_log:
        if is_illegal(request):
            banned_ips.add(request['target_ip'])
        else:
            banned_ips.discard(request['target_ip'])

    # 对所有被识别的IP执行封禁
    ban_ips(banned_ips)
```

`check_and_ban_ips`函数遍历所有记录的请求，识别并封禁与非法活动相关的IP。

### 第三步：定义什么请求是非法的

```python
# 模拟检查请求是否非法的函数
def is_illegal(request):
    # 这是检查非法请求的占位符逻辑
    # 例如，检查请求体或目标
    return "illegal" in request['body']
```

`is_illegal`检查请求体是否包含“illegal”字样。这可以根据定义非法活动的具体逻辑进行扩展。

### 第四步：封禁被识别的IP

```python
# 封禁一组IP的函数
def ban_ips(ip_set):
    for ip in ip_set:
        print(f"封禁IP: {ip}")
```

一旦识别出非法IP，`ban_ips`函数会封禁它们，打印其IP地址（在实际系统中，可以阻止这些IP）。

### 第五步：基于80%非法请求的封禁方式

```python
# 基于80%非法请求的比例检查并封禁IP
def check_and_ban_ips():
    banned_ips = set()
    illegal_count = 0
    total_requests = 0

    # 遍历所有记录的请求
    for request in request_log:
        total_requests += 1
        if is_illegal(request):
            illegal_count += 1

    # 如果80%或更多的请求是非法的，封禁这些IP
    if total_requests > 0 and (illegal_count / total_requests) >= 0.8:
        for request in request_log:
            if is_illegal(request):
                banned_ips.add(request['target_ip'])

    # 对所有被识别的IP执行封禁
    ban_ips(banned_ips)
```

这种替代方法基于非法请求的比例评估是否应封禁IP。如果某个IP的非法请求占80%或更多，它会被封禁。

### 第六步：增强的非法请求检查（例如Shadowsocks和Trojan协议检测）

```python
def is_illegal(request):
    # 检查请求是否使用Shadowsocks协议（请求体包含类似二进制的数据）
    if request['target_port'] == 443:
        if is_trojan(request):
            return True
    elif is_shadowsocks(request):
        return True
    return False
```

`is_illegal`函数现在还检查特定的协议，如Shadowsocks和Trojan：
- **Shadowsocks**：我们可能会检查请求体中是否包含加密或类似二进制的数据。
- **Trojan**：如果请求通过端口443（HTTPS）传输，并且匹配特定模式（如Trojan流量特征），则会被标记为非法。

### 第七步：合法请求示例

例如，`GET https://some-domain.xyz/bandwidth`这样的请求肯定是合法的，不会触发封禁机制。

### 第八步：代理服务器流量特征

代理服务器的流量特征与常规的Web或API服务器大不相同。GFW需要区分正常的Web服务器流量和代理服务器流量，这两者的表现完全不同。

### 第九步：机器学习和AI模型用于智能检测

考虑到互联网中通过的请求和响应范围广泛，GFW可以采用AI和机器学习模型来分析流量模式，并智能地检测非法行为。通过对各种流量类型进行训练并使用先进的技术，GFW可以更有效地基于观察到的模式封禁或过滤流量。

