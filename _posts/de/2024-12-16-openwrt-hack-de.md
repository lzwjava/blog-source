---
audio: false
generated: false
lang: de
layout: post
title: Verbesserung von OpenWRT mit OpenClash und Shadowsocks
translated: true
---

### Paketlisten aktualisieren

```bash
root@OpenWrt:~# opkg update
Downloading https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt7621/packages/Packages.gz
Aktualisierte Liste der verfügbaren Pakete in /var/opkg-lists/openwrt_core
Downloading https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt7621/packages/Packages.sig
Signaturprüfung bestanden.
Downloading https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/base/Packages.gz
Aktualisierte Liste der verfügbaren Pakete in /var/opkg-lists/openwrt_base
Downloading https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/base/Packages.sig
Signaturprüfung bestanden.
Downloading https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/Packages.gz
Aktualisierte Liste der verfügbaren Pakete in /var/opkg-lists/openwrt_luci
Downloading https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/Packages.sig
Signaturprüfung bestanden.
root@OpenWrt:~#
```

### Installation des Shadowsocks-Plugins

Um das `luci-app-shadowsocks-libev`-Plugin zu installieren:

```bash
root@OpenWrt:~# opkg install luci-app-shadowsocks-libev
Installation von luci-app-shadowsocks-libev (git-22.066.30464-cea4277) auf root...
Lade https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/luci-app-shadowsocks-libev_git-22.066.30464-cea4277_all.ipk herunter
Konfiguriere luci-app-shadowsocks-libev.
```

### OpenClash Installation

Weitere Details finden Sie im [GitHub-Repository](https://github.com/vernesong/OpenClash?tab=readme-ov-file) von OpenClash. Im Folgenden sind die Schritte zur Installation der erforderlichen Komponenten aufgeführt.

1. Installieren Sie den OpenSSH SFTP-Server:

   ```bash
   opkg install openssh-sftp-server
   ```

2. Verwenden Sie `scp`, um das OpenClash-Paket auf den Router zu kopieren:

   ```bash
   scp luci-app-openclash_0.46.050-beta_all.ipk root@192.168.1.1:~/
   ```

### Beispielkonfiguration für OpenClash

Unten ist eine Beispielkonfiguration für OpenClash:

```yaml
port: 7890
socks-port: 7891
mixed-port: 7892
allow-lan: true
mode: Rule
log-level: info
external-controller: 0.0.0.0:9090
experimental:
  ignore-resolve-fail: true
```

dns:
  enable: true
  # ipv6: false
  listen: 0.0.0.0:53
  fake-ip-range: 198.18.0.1/16
  default-nameserver:
    - 119.29.29.29
    - 223.5.5.5
    #- 223.6.6.6
  nameserver:
    - https://223.5.5.5/dns-query
    - https://1.12.12.12/dns-query
    #- https://doh.pub/dns-query
    #- https://dns.alidns.com/dns-query
  fake-ip-filter:
    - "*.lan"
    - "*.localdomain"
    - "*.example"
    - "*.invalid"
    - "*.localhost"
    - "*.test"
    - "*.local"

```yaml
proxies:
  - name: "Mein SS-Proxy"
    type: ss
    server: 209.97.0.0
    port: 57500
    cipher: chacha20-ietf-poly1305
    password: "jHLE54zNC000000"
    udp: true
    plugin: ""
    plugin-opts: {}
```

```yaml
proxy-groups:
  - name: "Proxy"
    type: select
    proxies:
      - "My SS Proxy"
```

rules:
  - GEOIP,CN,DIRECT
  - MATCH,Proxy
```

Mit diesen Schritten können Sie Ihr OpenWRT-Gerät erweitern, um erweiterte Netzwerkkonfigurationen und Proxy-Funktionen zu unterstützen. Konsultieren Sie immer die offizielle Dokumentation für Updates und Best Practices.