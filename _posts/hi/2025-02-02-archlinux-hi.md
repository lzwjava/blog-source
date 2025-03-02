---
audio: true
generated: false
lang: hi
layout: post
title: Arch Linux स्थापित करना
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
```

> disk6 का अटचिंग नाकाम हो गया: कम से कम एक वॉल्यूम अटच नहीं हो सका।
> अटचिंग पर रोक लगा दी PID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores से).
> रोक लगाने वाले पैरेंट PPID 1 (/sbin/launchd).

```bash
% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 रिकॉर्ड इन
1179+1 रिकॉर्ड आउट
1236303872 बाइट्स ट्रांसफर्ड कर दिए 46.777995 सेकेंड (26429176 बाइट्स/सेकेंड)
```

यूएसबी ड्राइव को वर्तमान सुरक्षा नीति द्वारा लॉक कर दिया गया है।

BIOS में प्रवेश करने के लिए F2 दबाएं और Secure Boot को अक्षम करें।

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

किसी कारण से, मैंने Ubuntu का इंस्टॉल करने का फैसला किया।