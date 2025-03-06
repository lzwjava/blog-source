---
audio: false
generated: false
lang: de
layout: post
title: 'Proxy-Tool: Squid und Danted'
translated: true
---

## Danted

Befehlszeilenanweisungen:

```bash
sudo apt-get install dante-server
sudo apt install net-tools
ifconfig
danted
tail -f danted.log
```

Konfiguration von `/etc/danted.conf`:

```bash
logoutput: /home/lzwjava/danted.log

internal: 0.0.0.0 port = 1080  # Auf allen Schnittstellen lauschen
external: ens4
# Authentifizierung (erlaube alle ohne Anmeldeinformationen)
method: none

# Regeln
client pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    method: none  # Explizit keine Authentifizierung erlauben
}

socks pass {  # Verwende "socks pass" anstelle des veralteten "pass"
    from: 0.0.0.0/0 to: 0.0.0.0/0
    protocol: tcp udp
    method: none  # Erforderlich für keine Authentifizierung
}
```

## Squid-Konfiguration

```bash
acl all src all
http_access allow all
http_access deny all
http_port 1128
```

Versuch fehlgeschlagen. Muss zuerst `squid.conf` bereinigen.

```
1737725543.236   1822 14.31.165.22 TCP_TUNNEL/200 1232 CONNECT 91.108.56.121:443 - HIER_DIRECT/91.108.56.121 -
```

## Google Cloud Befehlszeilen

```bash
gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS

gcloud compute ssh --zone "asia-east1-a" "i25" --project "graphite-ally-445108-k3"
```