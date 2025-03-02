---
audio: false
generated: false
lang: fr
layout: post
title: Script V2Ray
translated: true
---

Voici un script V2Ray que j'utilise fréquemment.

```bash
#!/bin/bash
```

# Quitter en cas d'erreur
set -e

# Étape 1 : Télécharger le script d'installation de V2Ray
curl -L https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh > in.sh

# Étape 2 : Rendre le script d'installation exécutable
chmod +x in.sh

# Étape 3 : Exécuter le script d'installation
sudo ./in.sh

# Étape 4 : Démarrer le service V2Ray
sudo systemctl start v2ray

# Étape 5 : Vérifier si V2Ray est en cours d'exécution
echo "Vérification si V2Ray est en cours d'exécution..."
ps aux | grep v2ray

# Étape 6 : Écrire le contenu du fichier config.json
echo "Écriture de la configuration de V2Ray..."
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

# Étape 7 : Redémarrez le service V2Ray pour appliquer les modifications
sudo systemctl restart v2ray

# Étape 8 : Afficher l'état du service V2Ray
echo "État du service V2Ray :"
sudo systemctl status v2ray
```