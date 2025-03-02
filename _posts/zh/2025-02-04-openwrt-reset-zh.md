---
audio: true
generated: false
lang: zh
layout: post
title: OpenWrt重置
translated: true
---

## 通过Web界面重置

建议通过以太网线连接路由器。重置后，Wi-Fi SSID 将恢复到其默认设置，这可能与您的预期不符。

## 通过命令行 (SSH) 重置

您可以使用命令行界面 (SSH) 将 OpenWrt 重置为其默认设置。方法如下：

1. 通过 SSH 连接到您的 OpenWrt 路由器。
2. 运行以下命令：

    ```bash
    root@OpenWrt:~# firstboot
    这将清除所有设置并删除所有已安装的软件包。您确定吗？[N/y]
    y
    /dev/ubi0_1 已挂载为 /overlay，仅擦除文件
    root@OpenWrt:~# reboot
    ```
3. 路由器将重新启动并使用默认设置。

**命令解释：**

* `firstboot`：此命令启动重置过程，清除所有配置和已安装的软件包。
* `reboot`：此命令重启路由器，应用重置。
