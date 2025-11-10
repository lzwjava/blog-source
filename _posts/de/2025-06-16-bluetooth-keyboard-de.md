---
audio: false
generated: true
lang: de
layout: post
title: Behebung von Bluetooth-Tastatur-Verbindungsproblemen
translated: true
type: note
---

Basierend auf der `bluetoothctl`-Ausgabe, die `[DEL] Device` beim Verbindungsversuch anzeigt, hier eine präzise Lösung:

### Sofortige Lösung für das Verbindungs-Lösch-Problem
1. **Bestehende Geräteeinträge entfernen** (kritisch für veraltete Konfigurationen):
   ```bash
   bluetoothctl
   remove F4:73:35:78:28:4E  # Tastatur entfernen
   remove 24:27:30:24:C8:31   # Potenziell störendes Gerät entfernen
   exit
   ```

2. **Bluetooth-Stack zurücksetzen**:
   ```bash
   sudo systemctl stop bluetooth
   sudo rm -rf /var/lib/bluetooth/*
   sudo systemctl start bluetooth
   ```

3. **Reparatur mit korrekter Reihenfolge**:
   ```bash
   bluetoothctl
   power on
   discoverable on
   pairable on
   agent on  # Passkey-Agent aktivieren
   scan on
   ```
   - **K380 in Pairing-Modus versetzen** (LED blinkt schnell)
   - Wenn die Tastatur erscheint:
     ```bash
     pair F4:73:35:78:28:4E
     ```
   - **Sofort den 6-stelligen Passcode** (z.B. `123456`), der auf dem Bildschirm angezeigt wird, **auf der Tastatur eingeben** und Enter drücken

4. **Erst nach erfolgreichem Pairing verbinden**:
   ```bash
   connect F4:73:35:78:28:4E
   trust F4:73:35:78:28:4E
   scan off
   quit
   ```

### Warum das passiert
- Das `[DEL] Device` tritt auf, weil:
  - Der Bluetooth-Stack einen Verbindungsfehler erkennt und den Geräteeintrag löscht
  - **Fehlender Pairing-Schritt** vor dem Verbindungsversuch
  - Mögliche RF-Interferenz durch andere Geräte (wie das `midea`-Gerät)

### Zusätzliche kritische Checks
1. **Antennenverbindung überprüfen**:
   - Sicherstellen, dass Bluetooth-Antennen auf der MSI-Motherboard-Rückseite festgeschraubt sind

2. **Kernel-Treiber überprüfen**:
   ```bash
   dmesg | grep -i bluetooth
   ```
   Nach Fehlern wie `hci0: command timeout` oder `Firmware failed to start` suchen

3. **Firmware aktualisieren** (falls Timeout-Fehler auftreten):
   ```bash
   sudo apt install linux-firmware
   ```

4. **Test mit minimaler Umgebung**:
   ```bash
   sudo rfkill unblock all
   sudo systemctl stop NetworkManager  # Temporär anhalten
   sudo systemctl restart bluetooth
   ```

### Falls es weiterhin fehlschlägt
1. **Alternative Pairing-Methode** (Agent umgehen):
   ```bash
   echo -e 'remove F4:73:35:78:28:4E\npair F4:73:35:78:28:4E\nconnect F4:73:35:78:28:4E\ntrust F4:73:35:78:28:4E' | bluetoothctl
   ```

2. **Tastaturbatterie überprüfen** (kritisch für Bluetooth):
   - Batterie wechseln, wenn die Spannung niedrig ist (K380 verwendet CR2032 x 2)

3. **USB-Bluetooth-Adapter test**:
   - Falls internes Bluetooth problematisch ist, einen CSR4.0 USB-Adapter (ca. 10$) ausprobieren

**Erwartete Erfolgsindikatoren**:
- `Pairing successful`-Meldung
- `Connection successful` in bluetoothctl
- `dmesg` zeigt `HIDP: Bluetooth HID device driver`

Nach dem Pairing sollte Ihre K380 Neustarts überstehen. Bei erneuten Trennungen, überprüfen Sie `journalctl -u bluetooth -f` auf Echtzeit-Fehler.