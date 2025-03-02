---
audio: true
generated: true
lang: hi
layout: post
title: Hetzner Cloud में फ्लोटिंग IPs
translated: true
---

## आईपी

```bash
sudo ip addr add 78.47.144.0 dev eth0
```

## नेटप्लान

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
