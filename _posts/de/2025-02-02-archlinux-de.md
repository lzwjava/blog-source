---
audio: false
lang: de
layout: post
title: Arch Linux installieren
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
```

> Das Abmelden von disk6 ist fehlgeschlagen: mindestens ein Volumen konnte nicht abgekoppelt werden.
> Die Abmeldung wurde von PID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores) abgelehnt.
> Elternprozess PID 1 (/sbin/launchd).

```bash
% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 records in
1179+1 records out
1236303872 bytes transferred in 46.777995 secs (26429176 bytes/sec)
```

Der USB-Laufwerk ist durch die aktuelle Sicherheitsrichtlinie gesperrt.

Drücken Sie F2, um in das BIOS zu gelangen und Secure Boot zu deaktivieren.

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