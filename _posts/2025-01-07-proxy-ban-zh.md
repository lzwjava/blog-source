---
audio: true
lang: zh
layout: post
title: 代理服务器封禁分析
---

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

我使用nginx来服务443端口，如下所示：

```bash
server {
    listen 443 ssl;
    server_name www.some-domain.xyz;

    ssl_certificate /etc/letsencrypt/live/www.some-domain.xyz/fullchain.pem; # 由Let's Encrypt管理
    # ...
    location / {

        proxy_pass http://127.0.0.1:5000/;
        # ...
    }
}
```

这个服务器程序提供网络数据，我将其作为我的代理服务器，利用网络数据在博客上展示我的在线状态。

有趣的是，这个服务器已经好几天没有被防火长城（GFW）或其他网络控制系统封禁了。通常，我设置的代理服务器会在一两天内被封禁。该服务器运行Shadowsocks程序，端口像51939，因此它同时处理Shadowsocks流量和常规API流量。这种混合似乎让GFW认为该服务器不是专用的代理服务器，而是一个正常的服务器，从而避免了封禁该IP。

这一观察结果令人感兴趣。看起来，GFW使用特定的逻辑来区分代理流量和常规流量。尽管像Twitter和YouTube等网站在中国被封锁，但许多外国网站——如国际大学和公司的网站——仍然可以访问。

这表明，GFW可能根据规则区分正常的HTTP/HTTPS流量和代理相关流量。处理两种类型流量的服务器似乎能够避免封禁，而仅处理代理流量的服务器更容易被封锁。

有一个问题是，GFW使用什么时间范围来积累数据以进行封禁——是一天还是一小时。在这个时间范围内，它会检测流量是否仅来自代理。如果是，那么服务器的IP会被封禁。

我经常访问我的博客，回顾我写的内容，但在接下来的几周里，我的重点将转向其他任务，而不是写博客文章。这将减少我通过443端口访问`bandwidth` API的次数。如果我发现自己再次被封禁，我应该编写一个程序，定期访问这个API来欺骗GFW。
