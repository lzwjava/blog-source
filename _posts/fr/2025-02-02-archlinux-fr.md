---
audio: false
lang: fr
layout: post
title: Installer Arch Linux
translated: true
---

Lenovo Xiaoxing 14IAH8 ordinateur portable.

```bash
$ diskutil list
```

> /dev/disk6 (external, physical):
>   #:                       TYPE NAME                    SIZE       IDENTIFIER
>   0:     FDisk_partition_scheme                        *30,8 Go    disk6
>   1:             Windows_FAT_32 NO NAME                 30.8 Go    disk6s1

```bash
% diskutil unmountDisk /dev/disk6

Démontage de disk6 a échoué : au moins un volume n'a pas pu être démonté.
Le démontage a été dissous par PID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores).
Parent PPID dissident 1 (/sbin/launchd).

% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 records in
1179+1 records out
1236303872 bytes transferred in 46.777995 secs (26429176 bytes/sec)
```

Le lecteur USB est verrouillé par la politique de sécurité actuelle.

Appuyez sur F2 pour entrer dans le BIOS et désactiver le démarrage sécurisé.