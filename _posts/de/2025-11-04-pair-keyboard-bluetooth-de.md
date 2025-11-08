---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Logitech-Tastatur über Bluetooth-CLI koppeln
translated: true
type: note
---

### Voraussetzungen
- Stellen Sie sicher, dass Ihr Bluetooth-5.3-Emitter (Dongle) an den USB-3.0-Anschluss angeschlossen ist und von Ubuntu erkannt wird. Führen Sie `lsusb` im Terminal aus, um dies zu überprüfen (suchen Sie nach "Bluetooth" oder der Vendor-ID). Falls nicht, versuchen Sie einen anderen USB-Anschluss oder starten Sie den Rechner neu.
- Installieren Sie die Bluetooth-Tools, falls noch nicht geschehen:  
  ```
  sudo apt update
  sudo apt install bluez bluetooth bluez-tools
  ```
- Entsperren Sie Bluetooth bei Bedarf:  
  ```
  rfkill unblock bluetooth
  ```
- Starten Sie den Bluetooth-Dienst neu:  
  ```
  sudo systemctl restart bluetooth
  ```

### Pairing-Schritte mit bluetoothctl (Empfohlen für die CLI)
Das Tool `bluetoothctl` ist die Standardmethode zur Verwaltung von Bluetooth unter Linux/Ubuntu. Logitech-Tastaturen (wie MX Keys, K380 oder ähnliche) erfordern oft die Eingabe eines Pairing-PINs auf der Tastatur selbst.

1. **Öffnen Sie die Bluetooth-Konsole**:  
   ```
   bluetoothctl
   ```
   Dies startet eine interaktive Shell (die Eingabeaufforderung ändert sich zu `[bluetooth]#`).

2. **Aktivieren Sie den Adapter**:  
   ```
   power on
   ```
   (Falls "No default controller available" angezeigt wird, führen Sie `list` aus, um Ihren Adapter zu sehen, und `select <Adapter_MAC>`, falls mehrere vorhanden sind.)

3. **Richten Sie den Pairing-Agenten ein**:  
   ```
   agent on
   default-agent
   ```
   Dies aktiviert die PIN-Behandlung und macht Ihre Sitzung zum Standard für das Pairing.

4. **Starten Sie die Suche nach Geräten**:  
   ```
   scan on
   ```
   Lassen Sie dies laufen. Ihre Logitech-Tastatur sollte nach ca. 10-20 Sekunden erscheinen (z.B. als "Logitech K380" oder ähnlich, mit einer MAC-Adresse wie `XX:XX:XX:XX:XX:XX`).

5. **Versetzen Sie Ihre Logitech-Tastatur in den Pairing-Modus**:  
   - Schalten Sie sie ein (falls sie einen Netzschalter hat).  
   - Drücken und halten Sie die Bluetooth-Pairing-Taste (normalerweise an der Seite oder oben – prüfen Sie Ihr Modell; bei Multi-Device-Modellen wie MX Keys halten Sie den Kanal-Button 1/2/3 für 3-5 Sekunden gedrückt, bis die LED schnell blinkt).  
   - Bei Single-Device-Modellen halten Sie die Haupt-Pairing-Taste gedrückt.

6. **Koppeln Sie das Gerät**:  
   Sobald es im Scan erscheint (drücken Sie Enter, um zu aktualisieren), führen Sie aus:  
   ```
   pair <MAC_ADRESSE>
   ```
   - Beispiel: `pair 12:34:56:78:9A:BC`  
   - Ubuntu fordert Sie zur Eingabe eines PINs auf (oft 0000 oder 1234 für Logitech – versuchen Sie zuerst die Standardwerte).  
   - **Wichtiger Schritt für Logitech**: Geben Sie den PIN direkt auf der *physischen Tastatur* ein und drücken Sie die Eingabetaste. (Falls keine GUI-Benachrichtigungen erscheinen, ist dies entscheidend – einige Benutzer berichten, dass sie Systembenachrichtigungen über `gnome-control-center` > Benachrichtigungen aktivieren müssen, aber die CLI umgeht dies oft.)

7. **Vertrauen und verbinden**:  
   ```
   trust <MAC_ADRESSE>
   connect <MAC_ADRESSE>
   ```
   - Dies verbindet automatisch bei zukünftiger Verwendung.

8. **Beenden Sie die Konsole**:  
   ```
   exit
   ```

### Fehlerbehebung
- **Gerät wird nicht gescannt**: Stellen Sie sicher, dass sich die Tastatur im Pairing-Modus befindet (blinkende LED). Führen Sie `scan off` und dann erneut `scan on` aus. Warten Sie bis zu 30 Sekunden.
- **Pairing fehlgeschlagen (z.B. "AuthenticationCanceled")**: Entfernen Sie das Gerät zuerst (`remove <MAC>`), und versuchen Sie es erneut. Bei hartnäckigen Logitech-Modellen versuchen Sie, die Pairing-Taste länger gedrückt zu halten oder die Kanäle umzuschalten.
- **Keine PIN-Eingabeaufforderung**: Einige Tastaturen koppeln ohne PIN – fahren Sie mit dem Verbinden fort. Falls hängengeblieben, prüfen Sie die Logs: `sudo journalctl -u bluetooth -f` während des Pairings.
- **Adapter-Probleme**: Wenn Sie einen USB-Bluetooth-5.3-Dongle verwenden, bestätigen Sie die Kernel-Unterstützung (Ubuntu 22.04+ handhabt BT 5.3 gut). Aktualisieren Sie den Kernel bei älteren Ubuntu-Versionen: `sudo apt install linux-generic-hwe-22.04`.
- **GUI-Alternative**: Öffnen Sie Einstellungen > Bluetooth, schalten Sie es ein und koppeln Sie von dort aus – aber die CLI ist zuverlässiger für Logitech-Eigenheiten.
- Test: Geben Sie nach dem Pairing in einem Terminal etwas ein. Wenn es funktioniert, fügen Sie es zur automatischen Verbindung beim Start über `bluetoothctl` oder Crontab hinzu.

Falls Ihr spezifisches Logitech-Modell (z.B. MX Keys Mini) einzigartige Probleme aufweist, geben Sie das genaue Modell für maßgeschneiderte Schritte an.

### Referenzen
- [Pairing LOGITECH K380 in Ubuntu 20.04](https://unix.stackexchange.com/questions/590221/pairing-logitech-k380-in-ubuntu-20-04)  
- [Logitech MX Keys won't pair with Bluetooth](https://askubuntu.com/questions/1270419/20-04-logitech-mx-keys-wont-pair-with-bluetooth)  
- [Pair Logitech MX Keys with Xubuntu via Bluetooth](https://zroupas.github.io/linux/2021/08/25/pair_mxkeys_xubuntu_bt.html)  
- [Ubuntu 20.04 cannot pair Bluetooth Keyboard](https://askubuntu.com/questions/1398096/ubuntu-20-04-cannot-pair-bluetooth-keyboard)