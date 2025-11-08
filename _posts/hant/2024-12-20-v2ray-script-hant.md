---
audio: false
generated: false
image: false
lang: hant
layout: post
title: V2Ray 腳本
translated: true
type: post
---

這是我經常使用的一個V2Ray腳本。

```bash
#!/bin/bash

# 錯誤時退出
set -e

# 第一步：下載V2Ray安裝腳本
curl -L https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh > in.sh

# 第二步：使安裝腳本可執行
chmod +x in.sh

# 第三步：運行安裝腳本
sudo ./in.sh

# 第四步：啟動V2Ray服務
sudo systemctl start v2ray

# 第五步：檢查V2Ray是否正在運行
echo "正在檢查V2Ray是否正在運行..."
ps aux | grep v2ray

# 第六步：寫入config.json文件內容
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

# 第七步：重啟V2Ray服務以應用更改
sudo systemctl restart v2ray

# 第八步：顯示V2Ray服務狀態
echo "V2Ray服務狀態："
sudo systemctl status v2ray
```