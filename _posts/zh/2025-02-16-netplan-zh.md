---
audio: true
generated: true
lang: zh
layout: post
title: 尝试 Netplan
translated: true
---

我尝试了以下配置为Ubuntu机器分配静态IP地址。我在该服务器上运行OpenWebUI和llama.cpp。

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

运行`sudo netplan apply`后，无法通过`ssh lzw@192.168.1.128`访问该机器。

使用键盘和鼠标登录到机器，删除文件并恢复设置。

`/etc/resolv.conf`被更改。