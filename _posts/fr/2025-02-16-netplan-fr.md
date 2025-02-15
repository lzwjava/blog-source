---
audio: true
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

Après avoir exécuté `sudo netplan apply`, je n'ai plus pu accéder à la machine via `ssh lzw@192.168.1.128`.

J'ai dû utiliser un clavier et une souris pour me connecter à la machine, supprimer les fichiers et restaurer les paramètres.

J'ai remarqué que `/etc/resolv.conf` avait été modifié.