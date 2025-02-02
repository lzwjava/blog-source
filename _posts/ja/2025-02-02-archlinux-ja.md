---
audio: false
lang: ja
layout: post
title: Arch Linux のインストール
translated: true
---

Lenovo Xiaoxing 14IAH8ノートパソコン。

```bash
$ diskutil list
```

> /dev/disk6 (外部、物理):
>   #:                       TYPE NAME                    SIZE       IDENTIFIER
>   0:     FDisk_partition_scheme                        *30.8 GB    disk6
>   1:             Windows_FAT_32 NO NAME                 30.8 GB    disk6s1

```bash
% diskutil unmountDisk /dev/disk6

ディスク6のアンマウントに失敗しました: 少なくとも1つのボリュームはアンマウントできませんでした。
アンマウントは PID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores) によって拒否されました。
拒否者親 PPID 1 (/sbin/launchd)。

% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 記錄
1179+1 記錄が出力されました
1236303872 バイトが 46.777995 秒で転送されました (26429176 バイト/秒)
```

このUSBドライブは、現在のセキュリティポリシーによってロックされています。

F2を押して BIOS に入り、セキュアブートを無効にしてください。