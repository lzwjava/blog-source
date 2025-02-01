---
audio: false
lang: zh
layout: post
title: 安装 Arch Linux
translated: true
---

联想小新 14IAH8 笔记本电脑。

```bash
$ diskutil list
```

> /dev/disk6 (external, physical):
>   #:                       TYPE NAME                    SIZE       IDENTIFIER
>   0:     FDisk_partition_scheme                        *30.8 GB    disk6
>   1:             Windows_FAT_32 NO NAME                 30.8 GB    disk6s1

```bash
% diskutil unmountDisk /dev/disk6

卸载 disk6 失败：至少有一个卷无法卸载。
卸载被 PID 319 (/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mds_stores) 否决。
否决者父进程 PPID 1 (/sbin/launchd)。

% diskutil unmountDisk force /dev/disk6
```

```bash
sudo dd if=archlinux-2025.02.01-x86_64.iso of=/dev/rdisk6 bs=1m

1179+1 记录输入
1179+1 记录输出
1236303872 字节在 46.777995 秒内传输 (26429176 字节/秒)
```

USB 驱动器被当前的安全策略锁定。

按 F2 进入 BIOS 并禁用安全启动。