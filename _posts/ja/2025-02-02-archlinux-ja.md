---
audio: false
lang: ja
layout: post
title: Arch Linux をインストールする
translated: true
---

レノボ 小星 14IAH8 ラップトップ。

```bash
$ diskutil list
```

> /dev/disk6 (外部、物理):
>   #:                       TYPE NAME                    SIZE       IDENTIFIER
>   0:     FDisk_partition_scheme                        *30.8 GB    disk6
>   1:             Windows_FAT_32 NO NAME                 30.8 GB    disk6s1

```bash
% diskutil unmountDisk /dev/disk6

disk6のアンマウントに失敗しました: アンマウントできないボリュームが少なくとも1つあります。
アンマウントはPID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores)によって拒否されました。
拒否者の親PPID 1 (/sbin/launchd)。

% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 records in
1179+1 records out
1236303872 bytes transferred in 46.777995 secs (26429176 bytes/sec)
```

USBドライブは現在のセキュリティポリシーによりロックされています。

F2を押してBIOSに入り、セキュアブートを無効にしてください。