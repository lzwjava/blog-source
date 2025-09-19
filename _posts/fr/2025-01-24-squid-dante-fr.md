---
audio: false
generated: false
image: false
lang: fr
layout: post
title: 'Outil de Proxy : Squid et Danted'
translated: true
---

## Danted

Instructions en ligne de commande :

```bash
sudo apt-get install dante-server
sudo apt install net-tools
ifconfig
danted
tail -f danted.log
```

Configuration de `/etc/danted.conf` :

```bash
logoutput: /home/lzwjava/danted.log

internal: 0.0.0.0 port = 1080  # Écoute sur toutes les interfaces
external: ens4
# Authentification (autoriser tous sans identifiants)
method: none

# Règles
client pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    method: none  # Autoriser explicitement sans authentification
}

socks pass {  # Utiliser "socks pass" au lieu de "pass" déprécié
    from: 0.0.0.0/0 to: 0.0.0.0/0
    protocol: tcp udp
    method: none  # Requis pour aucune authentification
}
```

## Configuration de Squid

```bash
acl all src all
http_access allow all
http_access deny all
http_port 1128
```

Échec de la tentative. Il faut d'abord nettoyer `squid.conf`.

```
1737725543.236   1822 14.31.165.22 TCP_TUNNEL/200 1232 CONNECT 91.108.56.121:443 - HIER_DIRECT/91.108.56.121 -
```

## Commandes Google Cloud en ligne de commande

```bash
gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS

gcloud compute ssh --zone "asia-east1-a" "i25" --project "graphite-ally-445108-k3"
```