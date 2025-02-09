---
audio: true
lang: hant
layout: post
title: Hetzner Cloud 的浮動 IP
translated: true
---

## IP

```bash
sudo ip addr add 78.47.144.0 dev eth0
```

## Netplan

```bash
touch /etc/netplan/60-floating-ip.yaml
nano /etc/netplan/60-floating-ip.yaml
```

```yaml
network:
   version: 2
   renderer: networkd
   ethernets:
     eth0:
       addresses:
       - 78.47.144.0/32
```

```bash
sudo netplan apply
```
