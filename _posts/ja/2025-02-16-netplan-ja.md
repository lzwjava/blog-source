---
audio: true
generated: true
lang: ja
layout: post
title: Netplanを試す
translated: true
---

以下の設定を使用して、Ubuntuマシンに静的IPアドレスを割り当てようとしました。そのサーバーでOpenWebUIとllama.cppを実行しています。

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

`sudo netplan apply`を実行した後、`ssh lzw@192.168.1.128`経由でマシンにアクセスできなくなりました。

キーボードとマウスを使用してマシンにログインし、ファイルを削除し、設定を元に戻しました。

`/etc/resolv.conf`が変更されました。