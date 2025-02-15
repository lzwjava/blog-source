---
audio: false
lang: ja
layout: post
title: Netplanを試す
translated: true
---

私は以下の設定を試して、Ubuntuマシンに静的IPアドレスを割り当てました。そのサーバーでOpenWebUIとllama.cppを実行しています。

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

`sudo netplan apply`を実行した後、`ssh lzw@192.168.1.128`でマシンにアクセスできなくなりました。

キーボードとマウスを使ってマシンにログインし、ファイルを削除して設定を元に戻す必要がありました。

`/etc/resolv.conf`が変更されていることに気づきました。