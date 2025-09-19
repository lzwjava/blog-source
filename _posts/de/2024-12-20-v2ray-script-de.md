---
audio: false
generated: false
image: false
lang: de
layout: post
title: V2Ray-Skript
translated: true
---

Dies ist ein V2Ray-Skript, das ich oft verwende.

```bash
#!/bin/bash
```

# Bei Fehler beenden
set -e

# Schritt 1: Laden Sie das V2Ray-Installationsskript herunter
curl -L https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh > in.sh

# Schritt 2: Machen Sie das Installationsskript ausführbar
chmod +x in.sh

# Schritt 3: Führen Sie das Installationsskript aus
sudo ./in.sh

# Schritt 4: V2Ray-Dienst starten
sudo systemctl start v2ray

# Schritt 5: Überprüfen, ob V2Ray läuft
echo "Überprüfe, ob V2Ray läuft..."
ps aux | grep v2ray

# Schritt 6: Schreiben Sie den Inhalt der config.json-Datei
echo "Schreibe V2Ray-Konfiguration..."
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

# Schritt 7: V2Ray-Dienst neu starten, um die Änderungen zu übernehmen
sudo systemctl restart v2ray

# Schritt 8: Status des V2Ray-Dienstes anzeigen
echo "Status des V2Ray-Dienstes:"
sudo systemctl status v2ray
```