---
audio: true
generated: true
lang: fr
layout: post
title: Essayer Netplan
translated: true
---

J'ai essayé la configuration ci-dessous pour attribuer une adresse IP statique à une machine Ubuntu. J'exécute OpenWebUI et llama.cpp sur ce serveur.

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

Après avoir exécuté `sudo netplan apply`, la machine ne pouvait plus être accédée via `ssh lzw@192.168.1.128`.

Le clavier et la souris ont été utilisés pour se connecter à la machine, supprimer les fichiers et revenir aux paramètres d'origine.

`/etc/resolv.conf` a été modifié.