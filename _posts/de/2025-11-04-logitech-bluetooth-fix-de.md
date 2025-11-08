---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Behebung von Logitech Bluetooth Pairing-Problemen
translated: true
type: note
---

### Fehlerbehebung beim AuthenticationCanceled-Fehler

Dieser Fehler tritt häufig bei Logitech Bluetooth-Tastaturen (Ihre MAC `F4:73:35:78:28:4E` entspricht dem Logitech OUI-Präfix) während des Pairings in Ubuntu auf, verursacht durch Authentifizierungs-Timeouts, fehlende PIN-Eingabeaufforderungen oder Probleme mit dem Agent in BlueZ. Das kurze Verbinden/Trennen in Ihrem Log deutet darauf hin, dass die Tastatur reagiert, aber der Prozess vor dem Abschluss einen Timeout hat. Andere Geräte (wie `54:2B:FC:F1:1C:D8`), die auftauchen, können Interferenzen verursachen – entfernen Sie diese zuerst.

#### Schnelle Vorbereitungsschritte
1.  **Entfernen Sie alle gekoppelten Geräte**, um Konflikte zu vermeiden:  
    Führen Sie in `bluetoothctl` `devices` aus, um sie aufzulisten, dann `remove <MAC>` für jedes Gerät (z.B. `remove 54:2B:FC:F1:1C:D8`). Verlassen Sie mit `exit`.

2.  **Starten Sie den Bluetooth-Dienst neu**:  
    ```
    sudo systemctl restart bluetooth
    sudo systemctl status bluetooth  # Überprüfen, ob er aktiv ist
    ```

3.  **Setzen Sie die Tastatur in den Pairing-Modus**: Drücken und halten Sie die Pairing-Taste (z.B. Easy-Switch-Kanal oder Bluetooth-Taste), bis die LED schnell blinkt. Führen Sie dies bei jedem Versuch erneut durch.

#### Erweiterte Pairing-Schritte in bluetoothctl
Öffnen Sie `bluetoothctl` erneut und befolgen Sie diese Schritte **genau** – die Agent-Einrichtung ist entscheidend, und das vorherige "Trusten" umgeht oft einige Timeouts. Für Logitech-Modelle (z.B. K380, K480, MX Keys) geben Sie einen beliebigen PIN **blind** auf der physischen Tastatur ein (keine Bildschirmrückmeldung), und zwar unmittelbar nach dem `pair`-Befehl.

1.  **bluetoothctl starten**:  
    ```
    bluetoothctl
    ```

2.  **Einschalten und Agent einrichten**:  
    ```
    power on
    agent on
    default-agent
    ```

3.  **Scannen und Gerät bestätigen**:  
    ```
    scan on
    ```  
    Warten Sie, bis `F4:73:35:78:28:4E` erscheint (bei Bedarf mit Enter aktualisieren). Dann:  
    ```
    scan off  # Scannen stoppen, um den Fokus zu setzen
    ```

4.  **Gerät als vertrauenswürdig markieren** (hilft bei automatischer Annahme bei Wiederverbindungen):  
    ```
    trust F4:73:35:78:28:4E
    ```

5.  **Pairing**:  
    ```
    pair F4:73:35:78:28:4E
    ```  
    - Wenn ein PIN/Passkey erscheint (z.B. `[agent] PIN code: 390412` oder `[agent] Passkey: 299595`), **tippen Sie ihn sofort auf der physischen Tastatur** und drücken Sie Enter. Tun Sie dies blind – selbst wenn keine Aufforderung aktiv zu sein scheint.  
    - Wenn kein PIN angezeigt wird (häufig bei einigen Logitech-Geräten), versuchen Sie, `0000` oder `1234` auf der Tastatur einzutippen und drücken Sie trotzdem Enter.  
    - Achten Sie auf `[CHG] Paired: yes`. Wenn sie sich kurz verbindet und dann abbricht, führen Sie direkt danach `connect F4:73:35:78:28:4E` erneut aus.

6.  **Verbinden und als vertrauenswürdig markieren**:  
    ```
    connect F4:73:35:78:28:4E
    trust F4:73:35:78:28:4E  # Falls nicht bereits früher erledigt
    ```

7.  **Beenden und testen**:  
    ```
    exit
    ```  
    Öffnen Sie einen Texteditor oder ein Terminal – tippen Sie zur Überprüfung. Wenn es funktioniert, sollte sie nach dem Aufwecken automatisch wieder eine Verbindung herstellen.

#### Falls es immer noch fehlschlägt
-   **GUI-Alternative**: Verwenden Sie Ubuntu Einstellungen > Bluetooth (einschalten, Gerät auswählen). Dies zeigt oft eine sichtbare PIN-Eingabeaufforderung. Wenn der CLI-Agent fehlschlägt, behandelt die GUI-Pinentry es oft besser.
-   **Blinde PIN-Wiederholung**: Selbst ohne angezeigten Code hatten einige Benutzer Erfolg, indem sie direkt nach `pair` `0000` + Enter eingetippt haben – die Tastatur authentifiziert sich still.
-   **Logs für Hinweise**: Führen Sie `sudo journalctl -u bluetooth -f` in einem anderen Terminal während des Pairings aus. Suchen Sie nach "PIN code" oder Timeout-Meldungen.
-   **BlueZ-Update**: Stellen Sie die neueste Version sicher (Ubuntu 24.04+ hat BlueZ 5.72+ mit besserer Logitech-Unterstützung):  
    ```
    sudo apt update && sudo apt upgrade bluez
    ```
-   **USB-Dongle-Besonderheit**: Ihr BT 5.3-Emitter an USB 3.0 ist in Ordnung, testen Sie aber ggf. an einem USB 2.0-Port – seltene Interferenzen wurden berichtet.
-   **Modellspezifisch**: Wenn es eine K480/MX Keys ist, halten Sie die Pairing-Taste 5+ Sekunden gedrückt. Bei Multi-Device-Tastaturen, wechseln Sie zuerst zu einem unbenutzten Kanal.

Dies sollte das Problem lösen – die meisten Logitech-Fälle liegen am blinden PIN-Schritt. Wenn Sie Ihr genaues Modell oder vollständige Logs teilen, kann ich dies weiter verfeinern.

[Bluetooth Pairing - AuthenticationCanceled (AskUbuntu)](https://askubuntu.com/questions/1373574/bluetooth-pairing-authenticationcanceled)  
[[SOLVED] Bluetooth keyboard: Unable to pair (Arch Linux Forums)](https://bbs.archlinux.org/viewtopic.php?id=174239)  
[Barely able to pair Logitech K480 on bluez 5.72 (GitHub)](https://github.com/bluez/bluez/issues/654)