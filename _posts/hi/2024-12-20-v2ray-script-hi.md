---
audio: false
generated: false
image: false
lang: hi
layout: post
title: V2Ray स्क्रिप्ट
translated: true
---

यह एक V2Ray स्क्रिप्ट है जिसका मैं अक्सर उपयोग करता हूँ।

```bash
#!/bin/bash
```

# त्रुटि पर बाहर निकलें
set -e

# चरण 1: V2Ray इंस्टॉलेशन स्क्रिप्ट डाउनलोड करें
curl -L https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh > in.sh

# चरण 2: इंस्टॉलेशन स्क्रिप्ट को एक्जीक्यूटेबल बनाएं
chmod +x in.sh

# चरण 3: इंस्टॉलेशन स्क्रिप्ट चलाएं
sudo ./in.sh

# चरण 4: V2Ray सेवा शुरू करें
sudo systemctl start v2ray

# चरण 5: जांचें कि क्या V2Ray चल रहा है
echo "जांच रहे हैं कि क्या V2Ray चल रहा है..."
ps aux | grep v2ray

# चरण 6: config.json फ़ाइल की सामग्री लिखें
echo "V2Ray कॉन्फ़िगरेशन लिख रहे हैं..."
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

# चरण 7: परिवर्तनों को लागू करने के लिए V2Ray सेवा को पुनः आरंभ करें
sudo systemctl restart v2ray

# चरण 8: V2Ray सेवा की स्थिति दिखाएं
echo "V2Ray सेवा की स्थिति:"
sudo systemctl status v2ray
```