---
audio: true
generated: false
image: false
lang: ja
layout: post
title: Arch Linuxのインストール
translated: true
type: post
---

Lenovo Xiaoxing 14IAH8 ノートパソコン。

```bash
$ diskutil list
```

> /dev/disk6 (外部、物理):
>   #:                       TYPE NAME                    SIZE       IDENTIFIER
>   0:     FDisk_partition_scheme                        *30.8 GB    disk6
>   1:             Windows_FAT_32 NO NAME                 30.8 GB    disk6s1

```bash
% diskutil unmountDisk /dev/disk6
```


> disk6 のアンマウントに失敗しました: 少なくとも1つのボリュームをアンマウントできませんでした。
> アンマウントは PID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores) によって拒否されました。
> 拒否者の親 PPID 1 (/sbin/launchd)。

```bash
% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 レコードが入力されました
1179+1 レコードが出力されました
1236303872 バイトが 46.777995 秒で転送されました (26429176 バイト/秒)
```

USBドライブは現在のセキュリティポリシーによってロックされています。

F2キーを押してBIOSに入り、セキュアブートを無効にしてください。

```bash
ip link
iwctl
device list
station wlan0 scan
station wlan0 get-networks
station wlan0 connect SSID
ping archlinux.org
timedatectl
```

何らかの理由で、代わりにUbuntuをインストールすることにしました。
