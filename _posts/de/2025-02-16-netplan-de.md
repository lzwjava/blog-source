---
audio: true
generated: false
lang: de
layout: post
title: Netplan ausprobieren
translated: true
---

Ich habe die folgende Konfiguration versucht, um einer Ubuntu-Maschine eine statische IP-Adresse zuzuweisen. Ich betreibe OpenWebUI und llama.cpp auf diesem Server.

```
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.128/32
      gateway4: 192.168.1.1
```

Nach dem Ausführen von `sudo netplan apply` konnte der Zugriff auf die Maschine über `ssh lzw@192.168.1.128` nicht mehr erfolgen.

Tastatur und Maus wurden verwendet, um sich bei der Maschine anzumelden, die Dateien zu entfernen und die Einstellungen zurückzusetzen.

`/etc/resolv.conf` wurde geändert.