---
audio: false
generated: false
lang: es
layout: post
title: 'Herramienta de Proxy: Squid y Danted'
translated: true
---

## Danted

Instrucciones de línea de comandos:

```bash
sudo apt-get install dante-server
sudo apt install net-tools
ifconfig
danted
tail -f danted.log
```

Configuración de `/etc/danted.conf`:

```bash
logoutput: /home/lzwjava/danted.log

internal: 0.0.0.0 port = 1080  # Escuchar en todas las interfaces
external: ens4
# Autenticación (permitir todo sin credenciales)
method: none

# Reglas
client pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    method: none  # Permitir explícitamente sin autenticación
}

socks pass {  # Usar "socks pass" en lugar del obsoleto "pass"
    from: 0.0.0.0/0 to: 0.0.0.0/0
    protocol: tcp udp
    method: none  # Requerido para sin autenticación
}
```

## Configuración de Squid

```bash
acl all src all
http_access allow all
http_access deny all
http_port 1128
```

No se pudo probar. Es necesario limpiar `squid.conf` primero.

```
1737725543.236   1822 14.31.165.22 TCP_TUNNEL/200 1232 CONNECT 91.108.56.121:443 - HIER_DIRECT/91.108.56.121 -
```

## Líneas de Comando de Google Cloud

```bash
gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS

gcloud compute ssh --zone "asia-east1-a" "i25" --project "graphite-ally-445108-k3"
```