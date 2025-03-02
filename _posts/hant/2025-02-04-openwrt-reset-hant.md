---
audio: true
generated: false
lang: hant
layout: post
title: OpenWrt 重設
translated: true
---

## 經網頁介面重設

建議使用乙太網路線纜連接路由器。重設後，Wi-Fi SSID 會回復至其預設設定，這可能與您的預期不符。

## 經命令列 (SSH) 重設

您可以使用命令列介面 (SSH) 將 OpenWrt 重設為其預設設定。方法如下：

1.  透過 SSH 連接您的 OpenWrt 路由器。
2.  執行以下命令：

    ```bash
    root@OpenWrt:~# firstboot
    This will erase all settings and remove any installed packages. Are you sure? [N/y]
    y
    /dev/ubi0_1 is mounted as /overlay, only erasing files
    root@OpenWrt:~# reboot
    ```
3.  路由器將以預設設定重新啟動。

**命令說明：**

*   `firstboot`：此命令啟動重設程序，清除所有組態和已安裝的套件。
*   `reboot`：此命令重新啟動路由器，套用重設。
