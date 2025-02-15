---
audio: false
lang: hant
layout: post
title: 嘗試 Netplan
translated: true
---

我嘗試了以下配置來為一台 Ubuntu 機器分配靜態 IP 地址。我在該伺服器上運行 OpenWebUI 和 llama.cpp。

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

在運行 `sudo netplan apply` 後，我無法再通過 `ssh lzw@192.168.1.128` 訪問該機器。

我不得不使用鍵盤和鼠標登錄到機器，刪除文件並恢復設置。

我注意到 `/etc/resolv.conf` 已經被更改。