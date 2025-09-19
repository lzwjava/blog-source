---
audio: true
generated: false
image: false
lang: ar
layout: post
title: تثبيت أرش لينكس
translated: true
---

Lenovo Xiaoxing 14IAH8 لاب توب.

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

> تم إلغاء تثبيت القرص 6: لا يمكن إلغاء تثبيت واحد على الأقل من الأقراص.
> تم رفض إلغاء التثبيت من قبل PID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores).
> PPID 1 (/sbin/launchd) للآداة.

```bash
% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 records in
1179+1 records out
1236303872 bytes transferred in 46.777995 secs (26429176 bytes/sec)
```

يحتجز القرص USB حاليًا من قبل السياسات الأمنية الحالية.

اضغط على F2 للدخول إلى BIOS وإلغاء Secure Boot.

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

من أجل سبب ما قررت تثبيت Ubuntu بدلاً من ذلك.