---
audio: false
generated: true
lang: de
layout: post
title: Entfernen des Outline VPN Clients unter Ubuntu
translated: true
type: note
---

Es scheint, als ob `apt` kein Paket namens `outline-client` finden kann. Dies bedeutet normalerweise eines von zwei Dingen:

1.  **Sie haben Outline nicht mit `apt` installiert (d.h., es wurde nicht als .deb-Paket installiert).** Dies ist der häufigste Grund für diesen Fehler bei Outline, da viele Benutzer es über das AppImage installieren.
2.  **Der Paketname ist anders, oder das Repository ist nicht konfiguriert.** Dies ist bei Outline weniger wahrscheinlich, aber für andere Software eine Möglichkeit.

Angesichts Ihres vorherigen Versuchs ist es höchstwahrscheinlich, dass Sie es als **AppImage** installiert haben. In diesem Fall müssen Sie es manuell entfernen.

So gehen Sie vor:

**1. Suchen und Löschen der AppImage-Datei:**

Der Outline-Client ist, wenn als AppImage installiert, normalerweise eine einzelne ausführbare Datei. Sie haben sie wahrscheinlich in Ihren `Downloads`-Ordner heruntergeladen oder vielleicht in einen `bin`- oder `Applications`-Ordner in Ihrem Home-Verzeichnis verschoben.

*   **Häufige Orte, die Sie überprüfen sollten:**
    *   `~/Downloads/`
    *   `~/Applications/` (falls Sie einen erstellt haben)
    *   `~/bin/` (falls Sie einen erstellt haben)
    *   Das Verzeichnis, von dem aus Sie es ursprünglich ausgeführt haben.

*   **So finden Sie es:** Sie können den `find`-Befehl verwenden, um danach in Ihrem Home-Verzeichnis zu suchen:
    ```bash
    find ~ -name "Outline-Client*.AppImage" 2>/dev/null
    ```
    Dieser Befehl durchsucht Ihr Home-Verzeichnis nach Dateien, die mit "Outline-Client" beginnen und auf ".AppImage" enden.
    Sobald Sie die Datei gefunden haben, löschen Sie sie:
    ```bash
    rm /pfad/zur/Outline-Client.AppImage
    ```
    (Ersetzen Sie `/pfad/zur/` mit dem tatsächlichen Pfad, den der `find`-Befehl gefunden hat.)

**2. Entfernen verbleibender Konfigurations- und Autostart-Dateien:**

Selbst wenn Sie das AppImage löschen, hat Outline möglicherweise einige Konfigurationsdateien und einen Autostart-Eintrag für sich selbst erstellt.

*   **Konfigurationsverzeichnis entfernen:**
    ```bash
    rm -rf ~/.config/Outline/
    ```
    Dieser Befehl entfernt das gesamte `Outline`-Verzeichnis innerhalb des Konfigurationsordners Ihres Benutzers.

*   **Autostart-Eintrag entfernen (falls erstellt):**
    Falls Outline so eingerichtet war, dass es automatisch mit der Anmeldung startet, könnte eine `.desktop`-Datei dafür existieren.
    ```bash
    rm -f ~/.config/autostart/Outline-Client.AppImage.desktop
    ```

*   **Desktopsymbole entfernen (falls vorhanden):**
    Manchmal erstellen AppImages ein Desktopsymbol in Ihrem lokalen Symbolverzeichnis.
    ```bash
    find ~/.local/share/icons -name "appimagekit-outline-client*.png" -delete
    ```
    Dies löscht alle PNG-Symbole, die mit dem Outline-AppImage zusammenhängen.

**3. Netzwerkkonfiguration überprüfen und wiederherstellen (falls notwendig):**

Outline kann, wie andere VPNs auch, Ihre DNS-Einstellungen verändern. Wenn Sie nach dem Entfernen des AppImages Probleme mit der Internetverbindung haben, überprüfen Sie Ihre `/etc/resolv.conf`-Datei.

*   **`resolv.conf` überprüfen:**
    ```bash
    cat /etc/resolv.conf
    ```
    Suchen Sie nach Zeilen, die so aussehen, als wären sie von Outline hinzugefügt worden (z.B. spezifische IP-Adressen für Nameserver, die Sie nicht als die Ihres Routers oder Ihres ISP-DNS erkennen).

*   **`resolv.conf` wiederherstellen (falls nötig):**
    Falls es so aussieht, als hätte Outline sie verändert:
    *   **Option A (Empfohlen für moderne Ubuntu-Versionen):** Wenn Ihr System `systemd-resolved` verwendet (was in aktuellen Ubuntu-Versionen üblich ist), können Sie dies normalerweise beheben, indem Sie die Symlink-Verbindung neu erstellen:
        ```bash
        sudo rm /etc/resolv.conf
        sudo ln -s /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
        ```
    *   **Option B (Manuelle Bearbeitung - verwenden Sie diese, wenn Option A nicht funktioniert oder für ältere Systeme):**
        Erstellen Sie zuerst ein Backup:
        ```bash
        sudo cp /etc/resolv.conf /etc/resolv.conf.bak
        ```
        Bearbeiten Sie dann die Datei:
        ```bash
        sudo nano /etc/resolv.conf
        ```
        Kommentieren Sie alle `nameserver`-Zeilen aus, die von Outline hinzugefügt wurden, oder entfernen Sie sie. Wenn Sie sich bezüglich des DNS Ihres ISP unsicher sind, können Sie üblicherweise öffentliche DNS-Server wie die von Google (`8.8.8.8` und `8.8.4.4`) oder Cloudflare (`1.1.1.1` und `1.0.0.1`) eintragen.

**4. Starten Sie Ihr System neu:**

Nachdem Sie diese Schritte abgeschlossen haben, wird dringend empfohlen, Ihr Ubuntu-System neu zu starten, um sicherzustellen, dass alle Änderungen wirksam werden und alle Hintergrundprozesse, die mit Outline zusammenhängen, vollständig beendet werden.

```bash
sudo reboot
```

Wenn Sie diese manuellen Deinstallationsschritte befolgen, sollten Sie den Outline VPN-Client vollständig von Ihrem Ubuntu-System entfernen können.