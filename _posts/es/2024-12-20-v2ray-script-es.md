---
audio: true
lang: es
layout: post
title: "# Script de V2Ray\n\nV2Ray es una herramienta de proxy versátil que se utiliza\
  \ para crear conexiones seguras y privadas. A continuación, te presento un script\
  \ básico para configurar V2Ray en tu servidor.\n\n## Requisitos\n\n- Un servidor\
  \ con acceso root.\n- Conexión a Internet.\n\n## Instalación\n\n1. **Conéctate a\
  \ tu servidor** a través de SSH.\n\n   ```bash\n   ssh root@tu_servidor\n   ```\n\
  \n2. **Descarga el script de instalación** de V2Ray.\n\n   ```bash\n   wget https://install.direct/go.sh\n\
  \   ```\n\n3. **Ejecuta el script** para instalar V2Ray.\n\n   ```bash\n   bash\
  \ go.sh\n   ```\n\n4. **Inicia el servicio** de V2Ray.\n\n   ```bash\n   systemctl\
  \ start v2ray\n   ```\n\n5. **Habilita el servicio** para que se inicie automáticamente\
  \ al arrancar el servidor.\n\n   ```bash\n   systemctl enable v2ray\n   ```\n\n\
  ## Configuración\n\nEl archivo de configuración de V2Ray se encuentra en `/etc/v2ray/config.json`.\
  \ Puedes editarlo para personalizar la configuración según tus necesidades.\n\n\
  ```bash\nnano /etc/v2ray/config.json\n```\n\n### Ejemplo de configuración básica\n\
  \n```json\n{\n  \"inbounds\": [\n    {\n      \"port\": 1080,\n      \"protocol\"\
  : \"socks\",\n      \"settings\": {\n        \"auth\": \"noauth\",\n        \"udp\"\
  : true\n      }\n    }\n  ],\n  \"outbounds\": [\n    {\n      \"protocol\": \"\
  freedom\",\n      \"settings\": {}\n    }\n  ]\n}\n```\n\n## Reiniciar el servicio\n\
  \nDespués de realizar cambios en la configuración, reinicia el servicio de V2Ray\
  \ para aplicar los cambios.\n\n```bash\nsystemctl restart v2ray\n```\n\n## Verificar\
  \ el estado del servicio\n\nPuedes verificar el estado del servicio de V2Ray para\
  \ asegurarte de que esté funcionando correctamente.\n\n```bash\nsystemctl status\
  \ v2ray\n```\n\n## Conclusión\n\nEste script básico te ayudará a configurar V2Ray\
  \ en tu servidor. A partir de aquí, puedes personalizar la configuración según tus\
  \ necesidades específicas. ¡Disfruta de una conexión segura y privada con V2Ray!"
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