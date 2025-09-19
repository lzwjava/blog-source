---
audio: true
generated: false
image: false
lang: fr
layout: post
title: Installer Arch Linux
translated: true
---

Lenovo Xiaoxing 14IAH8 Ordinateur portable.

```bash
$ diskutil list
```

> /dev/disk6 (extern, physique) :
>   #:                       TYPE NOM                    TAILLE       IDENTIFIER
>   0:     FDisk_partition_scheme                        *30.8 Go    disk6
>   1:             Windows_FAT_32 PAS DE NOM                 30.8 Go    disk6s1

```bash
% diskutil unmountDisk /dev/disk6
```

> Le démontage de disk6 a échoué : au moins un volume n'a pas pu être démonté.
> Le démontage a été refusé par PID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores).
> PPID parent du contradicteur 1 (/sbin/launchd).

```bash
% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 enregistrements en
1179+1 enregistrements out
1236303872 octets transférés en 46.777995 secs (26429176 octets/sec)
```

Le lecteur USB est verrouillé par la politique de sécurité actuelle.

Appuyez sur F2 pour entrer dans le BIOS et désactiver Secure Boot.

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

Pour une raison quelconque, j'ai décidé d'installer Ubuntu à la place.