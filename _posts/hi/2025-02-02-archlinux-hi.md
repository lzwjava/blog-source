---
audio: false
lang: hi
layout: post
title: Arch Linux Install Karna
translated: true
---

Lenovo Xiaoxing 14IAH8 लैपटॉप।

```bash
$ diskutil list
```

> /dev/disk6 (बाहरी, भौतिक):
>   #:                       TYPE NAME                    SIZE       IDENTIFIER
>   0:     FDisk_partition_scheme                        *30.8 GB    disk6
>   1:             Windows_FAT_32 NO NAME                 30.8 GB    disk6s1

```bash
% diskutil unmountDisk /dev/disk6

Unmount of disk6 failed: at least one volume could not be unmounted.
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

USB ड्राइव को वर्तमान सुरक्षा नीति द्वारा ताला लगाया गया है।

F2 दबाएं BIOS में प्रवेश करने के लिए और Secure Boot को अक्षम करें।