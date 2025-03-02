---
audio: true
generated: true
lang: es
layout: post
title: Intentando Netplan
translated: true
---

Intenté la configuración a continuación para asignar una dirección IP estática a una máquina Ubuntu. Ejecuto OpenWebUI y llama.cpp en ese servidor.

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

Después de ejecutar `sudo netplan apply`, la máquina ya no podía ser accedida a través de `ssh lzw@192.168.1.128`.

Se utilizó el teclado y el mouse para iniciar sesión en la máquina, eliminar los archivos y revertir la configuración.

Se cambió `/etc/resolv.conf`.