---
audio: false
lang: ar
layout: post
title: تثبيت أرش لينكس
translated: true
---

Lenovo Xiaoxing 14IAH8 لابتوب.

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

> فشل فك الارتباط من القرص 6: لم يتم فك الارتباط من واحد من الأقراص.
> تم رفض فك الارتباط بواسطة PID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores).
> والد PID 1 (/sbin/launchd).

```bash
% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 سجلات في
1179+1 سجلات خارج
1236303872 بايت نقلت في 46.777995 ثوان (26429176 بايت/ثانية)
```

الوحدة usb مقفلة من قبل الساسة الأمنية الحالية.

اضغط على F2 للدخول إلى BIOS وتعطيل التحقق من الأمان.

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