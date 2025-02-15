---
audio: false
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

Nach dem Ausführen von `sudo netplan apply` konnte ich den Computer nicht mehr über `ssh lzw@192.168.1.128` erreichen.

Ich musste eine Tastatur und eine Maus verwenden, um mich bei dem Computer anzumelden, die Dateien zu entfernen und die Einstellungen zurückzusetzen.

Ich bemerkte, dass `/etc/resolv.conf` geändert worden war.