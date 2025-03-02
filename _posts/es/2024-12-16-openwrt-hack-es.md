---
audio: false
generated: false
lang: es
layout: post
title: Mejorando OpenWRT con OpenClash y Shadowsocks
translated: true
---

### Actualización de Listas de Paquetes

```bash
root@OpenWrt:~# opkg update
Descargando https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt7621/packages/Packages.gz
Lista de paquetes disponibles actualizada en /var/opkg-lists/openwrt_core
Descargando https://downloads.openwrt.org/releases/22.03.3/targets/ramips/mt7621/packages/Packages.sig
Verificación de firma exitosa.
Descargando https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/base/Packages.gz
Lista de paquetes disponibles actualizada en /var/opkg-lists/openwrt_base
Descargando https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/base/Packages.sig
Verificación de firma exitosa.
Descargando https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/Packages.gz
Lista de paquetes disponibles actualizada en /var/opkg-lists/openwrt_luci
Descargando https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/Packages.sig
Verificación de firma exitosa.
root@OpenWrt:~#
```

### Instalación del Plugin de Shadowsocks

Para instalar el complemento `luci-app-shadowsocks-libev`:

```bash
root@OpenWrt:~# opkg install luci-app-shadowsocks-libev
Instalando luci-app-shadowsocks-libev (git-22.066.30464-cea4277) en root...
Descargando https://downloads.openwrt.org/releases/22.03.3/packages/mipsel_24kc/luci/luci-app-shadowsocks-libev_git-22.066.30464-cea4277_all.ipk
Configurando luci-app-shadowsocks-libev.
```

### Instalación de OpenClash

Consulte el [repositorio de GitHub](https://github.com/vernesong/OpenClash?tab=readme-ov-file) de OpenClash para obtener más detalles. A continuación se detallan los pasos para instalar los componentes necesarios.

1. Instala el servidor SFTP de OpenSSH:

```bash
opkg install openssh-sftp-server
```

2. Usa `scp` para copiar el paquete de OpenClash al router:

```bash
scp luci-app-openclash_0.46.050-beta_all.ipk root@192.168.1.1:~/
```

### Configuración de ejemplo de OpenClash

A continuación se muestra una configuración de ejemplo para OpenClash:

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

```yaml
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
```

```yaml
proxies:
  - name: "Mi Proxy SS"
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

```yaml
rules:
  - GEOIP,CN,DIRECT
  - MATCH,Proxy
```

Con estos pasos, puedes mejorar tu dispositivo OpenWRT para admitir configuraciones de red avanzadas y funcionalidades de proxy. Siempre consulta la documentación oficial para obtener actualizaciones y mejores prácticas.