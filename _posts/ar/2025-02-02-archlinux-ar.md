---
audio: false
lang: ar
layout: post
title: تثبيت Arch Linux
translated: true
---

Lenovo Xiaoxing 14IAH8 حاسوب محمول.

```bash
$ diskutil list
```

> /dev/disk6 (external, physical):
>   #:                       TYPE NAME                    SIZE       IDENTIFIER
>   0:     FDisk_partition_scheme                        *30.8 GB    disk6
>   1:             Windows_FAT_32 NO NAME                 30.8 GB    disk6s1

```bash
% diskutil unmountDisk /dev/disk6

Failed to unmount disk6: at least one volume could not be unmounted.
Unmount was dissented by PID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores).
Dissenter parent PPID 1 (/sbin/launchd).

% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 records in
1179+1 records out
1236303872 bytes transferred in 46.777995 secs (26429176 bytes/sec)
```

الوسيط USB معلق بواسطة السياسات الأمنية الحالية.

Pressure F2 to enter the BIOS and disable Secure Boot.