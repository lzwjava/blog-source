---
audio: false
generated: false
lang: ja
layout: post
title: V2Rayスクリプト
translated: true
---

これは私がよく使うV2Rayスクリプトです。

```bash
#!/bin/bash
```

# エラー時に終了
set -e

# ステップ1: V2Rayインストールスクリプトをダウンロードする
curl -L https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh > in.sh

# ステップ2: インストールスクリプトを実行可能にする
chmod +x in.sh

# ステップ3: インストールスクリプトを実行する
sudo ./in.sh

# ステップ4: V2Rayサービスを開始する
sudo systemctl start v2ray

# ステップ5: V2Rayが実行中か確認する
echo "V2Rayが実行中か確認しています..."
ps aux | grep v2ray

# ステップ6: config.jsonファイルの内容を記述する
echo "V2Rayの設定を記述しています..."
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

# ステップ7: 変更を適用するためにV2Rayサービスを再起動する
sudo systemctl restart v2ray

# ステップ8: V2Rayサービスのステータスを表示
echo "V2Rayサービスのステータス:"
sudo systemctl status v2ray
```