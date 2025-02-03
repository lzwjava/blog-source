---
audio: false
lang: en
layout: post
title: Openwrt Reset
translated: false
---

## Reset in UI Interace

Need to have a cable to directly connect the router. Otherwise once reset, it won't open WIFI SSID as default.

## Only Command Line

```bash
root@OpenWrt:~# firstboot
This will erase all settings and remove any installed packages. Are you sure? [N/y]
y
/dev/ubi0_1 is mounted as /overlay, only erasing files
root@OpenWrt:~# reboot
```

