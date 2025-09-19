---
audio: false
generated: false
image: false
lang: es
layout: post
title: V2ray
translated: true
---

Este es un script de V2Ray que uso con frecuencia.

```bash
#!/bin/bash
```

# Salir en caso de error
set -e

# Paso 1: Descargar el script de instalación de V2Ray
curl -L https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh > in.sh

# Paso 2: Hacer que el script de instalación sea ejecutable
chmod +x in.sh

# Paso 3: Ejecutar el script de instalación
sudo ./in.sh

# Paso 4: Iniciar el servicio de V2Ray
sudo systemctl start v2ray

# Paso 5: Verificar si V2Ray está en ejecución
echo "Verificando si V2Ray está en ejecución..."
ps aux | grep v2ray

# Paso 6: Escribir el contenido del archivo config.json
echo "Escribiendo la configuración de V2Ray..."
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

# Paso 7: Reiniciar el servicio de V2Ray para aplicar los cambios
sudo systemctl restart v2ray

# Paso 8: Mostrar el estado del servicio V2Ray
echo "Estado del servicio V2Ray:"
sudo systemctl status v2ray
```