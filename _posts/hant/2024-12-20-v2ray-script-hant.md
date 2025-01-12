---
audio: true
lang: hant
layout: post
title: V2Ray 脚本
---

这是我经常使用的一个V2Ray脚本。

```bash
#!/bin/bash
```

# 出错时退出
set -e

# 第一步：下载V2Ray安装脚本
curl -L https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh > in.sh

# 第二步：使安装脚本可執行
chmod +x in.sh

# 第三步：运行安装脚本
sudo ./in.sh

# 步骤4：启动V2Ray服务
sudo systemctl start v2ray

# 第五步：检查V2Ray是否正在运行
echo "正在检查V2Ray是否正在运行..."
ps aux | grep v2ray

# 步驟6：撰寫config.json文件內容
echo "正在寫入V2Ray配置..."
cat << EOF | sudo tee /usr/local/etc/v2ray/config.json > /dev/null
{
    "inbounds": [
        {
            "port": 1080,
            "listen": "0.0.0.0",
            "protocol": "vmess",
            "settings": {
                "clients": [
                    {
                        "id": "9f02f6b2-1d7d-4b10-aada-69e050f1be6b",
                        "level": 0,
                        "alterId": 0,
                        "email": "example@v2ray.com",
                        "security": "auto"
                    }
                ]
            },
            "streamSettings": {
                "network": "tcp"
            },
            "sniffing": {
                "enabled": true,
                "destOverride": [
                    "http",
                    "tls"
                ]
            },
            "tag": "vmess-inbound",
            "udp": true
        }
    ],
    "outbounds": [
        {
            "protocol": "freedom",
            "settings": {},
            "tag": "outbound-freedom",
            "udp": true
        }
    ],
    "log": {
        "loglevel": "debug",
        "access": "/var/log/v2ray/access.log",
        "error": "/var/log/v2ray/error.log"
    },
    "stats": {
        "enabled": false
    },
    "environment": {
        "v2ray.vmess.aead.forced": "false"
    }
}
EOF

# 步骤7：重启V2Ray服务以应用更改
sudo systemctl restart v2ray

# 步驟8：顯示V2Ray服務狀態
echo "V2Ray服務狀態："
sudo systemctl status v2ray
```