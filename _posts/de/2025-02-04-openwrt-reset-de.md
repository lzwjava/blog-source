---
audio: true
generated: true
lang: de
layout: post
title: OpenWrt-Reset
translated: true
---

## Zurücksetzen über die Weboberfläche

Es wird empfohlen, sich über ein Ethernet-Kabel mit dem Router zu verbinden. Nach einem Reset wird die Wi-Fi SSID auf ihre Standardeinstellungen zurückgesetzt, die möglicherweise nicht Ihren Erwartungen entsprechen.

## Zurücksetzen über die Kommandozeile (SSH)

Sie können OpenWrt über die Kommandozeilenschnittstelle (SSH) auf die Werkseinstellungen zurücksetzen. So geht's:

1.  Verbinden Sie sich per SSH mit Ihrem OpenWrt-Router.
2.  Führen Sie den folgenden Befehl aus:

    ```bash
    root@OpenWrt:~# firstboot
    Dies löscht alle Einstellungen und entfernt alle installierten Pakete. Sind Sie sicher? [N/y]
    y
    /dev/ubi0_1 ist als /overlay gemountet, es werden nur Dateien gelöscht
    root@OpenWrt:~# reboot
    ```
3.  Der Router startet mit den Standardeinstellungen neu.

**Erläuterung der Befehle:**

*   `firstboot`: Dieser Befehl initiiert den Rücksetzvorgang, löscht alle Konfigurationen und installierten Pakete.
*   `reboot`: Dieser Befehl startet den Router neu und wendet das Zurücksetzen an.
