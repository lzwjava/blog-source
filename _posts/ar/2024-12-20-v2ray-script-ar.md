---
audio: false
generated: false
lang: ar
layout: post
title: نص V2Ray
translated: true
---

هذا سكريبت V2Ray الذي أستخدمه كثيرًا.

```bash
#!/bin/bash
```

# الخروج عند حدوث خطأ
set -e

# الخطوة 1: تنزيل سكربت تثبيت V2Ray
curl -L https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh > in.sh

# الخطوة 2: جعل نص التثبيت قابلًا للتنفيذ
chmod +x in.sh

# الخطوة 3: تشغيل سكربت التثبيت
sudo ./in.sh

# الخطوة 4: بدء خدمة V2Ray
sudo systemctl start v2ray

# الخطوة 5: التحقق من أن V2Ray يعمل
echo "التحقق من أن V2Ray يعمل..."
ps aux | grep v2ray

# الخطوة 6: كتابة محتوى ملف config.json
echo "جارٍ كتابة إعدادات V2Ray..."
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

# الخطوة 7: إعادة تشغيل خدمة V2Ray لتطبيق التغييرات
sudo systemctl restart v2ray

# الخطوة 8: عرض حالة خدمة V2Ray
echo "حالة خدمة V2Ray:"
sudo systemctl status v2ray
```