---
audio: false
lang: hi
layout: post
title: आर्क लिनक्स इंस्टॉल कॉर
translated: true
---

Lenovo Xiaoxing 14IAH8 लैपटॉप।

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

> डिस्क 6 का अनमाउंट करने में विफल: कम से कम एक वॉल्यूम अनमाउंट नहीं किया जा सका। अनमाउंट को पीआईडी 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores) ने अस्वीकार कर दिया। अस्वीकार करने वाले माता-पिता पीपीआईडी 1 (/sbin/launchd)।

```bash
% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 रिकॉर्ड इन
1179+1 रिकॉर्ड आउट
1236303872 बाइटें 46.777995 सेकंड में ट्रांसफर की गईं (26429176 बाइट/सेकंड)
```

यूएसबी ड्राइव की सिक्योरिटी नीति द्वारा लॉक किया गया है।

BIOS में प्रवेश करने के लिए F2 दबाएँ और सिक्योर बूट निष्क्रिय करें।

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