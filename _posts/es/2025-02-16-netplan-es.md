---
audio: false
lang: es
layout: post
title: Intentando Netplan
translated: true
---

Intenté la configuración a continuación para asignar una dirección IP estática a una máquina Ubuntu. Ejecuto OpenWebUI y llama.cpp en ese servidor.

```yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.128/32
      gateway4: 192.168.1.1
```

Después de ejecutar `sudo netplan apply`, ya no pude acceder a la máquina a través de `ssh lzw@192.168.1.128`.

Tuve que usar un teclado y un ratón para iniciar sesión en la máquina, eliminar los archivos y revertir la configuración.

Noté que `/etc/resolv.conf` había sido modificado.