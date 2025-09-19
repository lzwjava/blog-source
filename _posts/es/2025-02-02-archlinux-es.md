---
audio: false
generated: false
image: false
lang: es
layout: post
title: Instalando Arch Linux
translated: true
---

Lenovo Xiaoxing 14IAH8 portátil.

```bash
$ diskutil list
```

> /dev/disk6 (externo, físico):
>   #:                       TYPE NAME                    SIZE       IDENTIFIER
>   0:     FDisk_partition_scheme                        *30.8 GB    disk6
>   1:             Windows_FAT_32 NO NAME                 30.8 GB    disk6s1

```bash
% diskutil unmountDisk /dev/disk6
```

> El desmontaje de disk6 falló: al menos un volumen no pudo ser desmontado.
> El desmontaje fue disuadido por PID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores).
> Proceso padre del disuador PPID 1 (/sbin/launchd).

```bash
% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 registros en
1179+1 registros fuera
1236303872 bytes transferidos en 46.777995 secs (26429176 bytes/sec)
```

La unidad USB está bloqueada por la política de seguridad actual.

Presione F2 para entrar en la BIOS y deshabilitar Secure Boot.

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

Por alguna razón, decidí instalar Ubuntu en su lugar.