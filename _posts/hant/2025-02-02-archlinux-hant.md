---
audio: false
lang: hant
layout: post
title: Arch Linux 安裝指南
translated: true
---

聯想小新 14IAH8 筆記本電腦。

```bash
$ diskutil list
```

> /dev/disk6 (外部, 物理):
>   #:                       TYPE NAME                    SIZE       IDENTIFIER
>   0:     FDisk_partition_scheme                        *30.8 GB    disk6
>   1:             Windows_FAT_32 NO NAME                 30.8 GB    disk6s1

```bash
% diskutil unmountDisk /dev/disk6

卸載 disk6 失敗: 至少有一個卷無法卸載。
卸載被 PID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores) 拒絕。
拒絕者父進程 PPID 1 (/sbin/launchd).

% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 筆錄入
1179+1 筆錄出
1236303872 位元組在 46.777995 秒內傳輸 (26429176 位元組/秒)
```

USB 驅動器被當前的安全原則鎖定。

按 F2 進入 BIOS 並禁用 Secure Boot。