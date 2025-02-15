---
audio: true
lang: en
layout: post
title: Trying Netplan
translated: false
---

I tried the configuration below to assign a static IP address to an Ubuntu machine. I run OpenWebUI and llama.cpp on that server.

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

After running `sudo netplan apply`, I could no longer access the machine via `ssh lzw@192.168.1.128`.

I had to use a keyboard and mouse to log in to the machine, remove the files, and revert the settings.

I noticed that `/etc/resolv.conf` had been changed.