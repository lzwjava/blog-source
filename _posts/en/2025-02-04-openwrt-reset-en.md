---
audio: true
lang: en
layout: post
title: OpenWrt Reset
translated: false
---

## Resetting via the Web Interface

It's recommended to connect to the router via an ethernet cable. After a reset, the Wi-Fi SSID will revert to its default settings, which may not be what you expect.

## Resetting via Command Line (SSH)

You can reset OpenWrt to its default settings using the command line interface (SSH). Here's how:

1.  Connect to your OpenWrt router via SSH.
2.  Run the following command:

    ```bash
    root@OpenWrt:~# firstboot
    This will erase all settings and remove any installed packages. Are you sure? [N/y]
    y
    /dev/ubi0_1 is mounted as /overlay, only erasing files
    root@OpenWrt:~# reboot
    ```
3.  The router will reboot with default settings.

**Explanation of the commands:**

*   `firstboot`: This command initiates the reset process, erasing all configurations and installed packages.
*   `reboot`: This command restarts the router, applying the reset.