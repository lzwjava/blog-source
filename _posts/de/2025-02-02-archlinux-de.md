---
audio: false
lang: de
layout: post
title: Installation von Arch Linux
translated: true
---

Lenovo Xiaoxing 14IAH8 Laptop.

```bash
$ diskutil list
```

> /dev/disk6 (extern, physisch):
>   #:                       TYPE NAME                    SIZE       IDENTIFIER
>   0:     FDisk_partition_scheme                        *30.8 GB    disk6
>   1:             Windows_FAT_32 NO NAME                 30.8 GB    disk6s1

```bash
% diskutil unmountDisk /dev/disk6

Das Unmounting von disk6 ist fehlgeschlagen: mindestens ein Volume konnte nicht unmounted werden.
Das Unmounting wurde von PID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores) abgelehnt.
Dissenter parent PPID 1 (/sbin/launchd).

% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 Datensätze ein
1179+1 Datensätze aus
1236303872 Bytes in 46,777995 Sekunden übertragen (26429176 Bytes/s)
```

Der USB-Stick ist durch die aktuelle Sicherheitsrichtlinie gesperrt.

Drücken Sie F2, um in das BIOS zu gelangen und Secure Boot zu deaktivieren.