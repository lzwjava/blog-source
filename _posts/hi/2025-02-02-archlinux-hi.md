---
audio: false
lang: hi
layout: post
title: Arch Linux स्थापित करना
translated: true
---

Lenovo Xiaoxing 14IAH8 Laptop.

```bash
$ diskutil list
```

> /dev/disk6 (bāhya, vyāvahārika):
>   #:                       TYPE NAME                    SIZE       IDENTIFIER
>   0:     FDisk_partition_scheme                        *30.8 GB    disk6
>   1:             Windows_FAT_32 NO NAME                 30.8 GB    disk6s1

```bash
% diskutil unmountDisk /dev/disk6

disk6 ke unmount karne mein vipatti: kām se kam ek volyum unmount nahin kiya ja sakā.

PID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores) dwāra unmount ko khānā kiya.

Dissenter parent PPID 1 (/sbin/launchd).

% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 rēcord in
1179+1 rēcord out
1236303872 bytes transferred in 46.777995 secs (26429176 bytes/sec)
```

USB drive vārtmān laabhāyukt nīti dwāra lōk kar rāha hai.

BIOS prāvēś kīyē aur Secure Boot ko disable karein.