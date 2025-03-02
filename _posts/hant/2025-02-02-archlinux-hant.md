---
audio: false
generated: true
lang: hant
layout: post
title: 裝載 Arch Linux
translated: true
---

Lenovo 小星 14IAH8 筆記型電腦。

```bash
$ diskutil list
```

> /dev/disk6 (external, physical):
>   #:                       TYPE NAME                    SIZE       IDENTIFIER
>   0:     FDisk_partition_scheme                        *30.8 GB    disk6
>   1:             Windows_FAT_32 NO NAME                 30.8 GB    disk6s1

```bash
% diskutil unmountDisk /dev/disk6
```

> 卸載 disk6 失敗：至少有一個卷未能卸載。
> 卸載被 PID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores) 拒絕。
> 拒絕者父進程 PPID 1 (/sbin/launchd)。

```bash
% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 records in
1179+1 records out
1236303872 bytes transferred in 46.777995 secs (26429176 bytes/sec)
```

USB 磁碟因目前的安全政策而被鎖定。

按 F2 鍵進入 BIOS 並禁用 Secure Boot。

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

不知為何，我決定安裝 Ubuntu。