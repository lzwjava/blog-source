---
audio: false
generated: true
lang: de
layout: post
title: Medienwiedergabe auf Ubuntu über VLC überwachen
translated: true
type: note
---

Um Filme auf Ihrem Monitor mit Ihrem zweiten Laptop (auf dem Ubuntu mit einem Nginx-Server läuft) ohne großen Aufwand anzuschauen, hier ist der beste Ansatz basierend auf dem, was Sie bereits haben. Sie möchten den Kauf zusätzlicher Geräte wie eines Fire TV Sticks oder Apple TV vermeiden, und obwohl ein langes HDMI-Kabel funktioniert, würden Sie es vorziehen, nicht ständig mit dem Laptop interagieren zu müssen, um Videos auszuwählen und abzuspielen. Richten wir eine Lösung ein, die einfach und bequem ist und Ihr bestehendes Setup nutzt.

Da Ihre Filme auf Ihrem Ubuntu-Laptop gespeichert sind und dieser bereits einen Nginx-Server betreibt, ist der einfachste Weg, diesen Laptop direkt per HDMI mit Ihrem Monitor zu verbinden und die Wiedergabesteuerung mühelos zu gestalten. So können Sie das machen:

### Lösung: Laptop mit Monitor verbinden und VLC mit Fernsteuerung verwenden

#### Was Sie benötigen
- **HDMI-Kabel**: Um Ihren Ubuntu-Laptop mit dem Monitor zu verbinden.
- **VLC media player**: Wahrscheinlich bereits auf Ubuntu installiert oder einfach zu installieren.
- **Smartphone oder ein anderes Gerät**: Um die Wiedergabe remote über Ihr Heimnetzwerk zu steuern.

#### Schritte zur Einrichtung
1. **Verbinden Sie den Laptop mit dem Monitor**
   - Stecken Sie ein Ende eines HDMI-Kabels in den HDMI-Anschluss Ihres Ubuntu-Laptops und das andere Ende in den HDMI-Eingang Ihres Monitors.
   - Schalten Sie den Monitor ein und wählen Sie den korrekten HDMI-Eingang. Die Anzeige des Laptops sollte jetzt auf dem Monitor erscheinen, inklusive Video und Audio (falls Ihr Monitor Lautsprecher hat; andernfalls verwenden Sie die Lautsprecher des Laptops oder schließen externe an).

2. **Installieren Sie VLC (falls noch nicht installiert)**
   - Öffnen Sie ein Terminal auf Ihrem Ubuntu-Laptop und führen Sie aus:
     ```
     sudo apt update
     sudo apt install vlc
     ```
   - So stellen Sie sicher, dass VLC, ein vielseitiger Media-Player, einsatzbereit ist.

3. **Aktivieren Sie die VLC-Weboberfläche für die Fernsteuerung**
   - Öffnen Sie VLC auf Ihrem Ubuntu-Laptop.
   - Gehen Sie zu **Extras > Einstellungen**.
   - Klicken Sie unten links auf **"Alle"**, um erweiterte Einstellungen anzuzeigen.
   - Navigieren Sie zu **Schnittstelle > Hauptschnittstellen** und aktivieren Sie das Kästchen **"Web"**, um die HTTP-Schnittstelle zu aktivieren.
   - Gehen Sie zu **Schnittstelle > Hauptschnittstellen > Lua** und setzen Sie ein Passwort (z.B. "meinpasswort") in das Feld **Lua HTTP Passwort**.
   - Klicken Sie auf **Speichern** und starten Sie VLC dann neu.

4. **Laden Sie Ihre Filme in VLC**
   - Gehen Sie in VLC zu **Wiedergabe > Wiedergabeliste**.
   - Ziehen Sie Ihre Filmdateien per Drag & Drop aus ihrem Ordner (wo sie auf dem Laptop gespeichert sind) in die VLC-Wiedergabeliste, oder verwenden Sie **Medien > Datei öffnen**, um sie einzeln hinzuzufügen.
   - Speichern Sie die Wiedergabeliste (z.B. "Meine Filme") über **Strg+Y** für einen schnellen Zugriff später.

5. **Ermitteln Sie die IP-Adresse Ihres Laptops**
   - Geben Sie im Terminal ein:
     ```
     ip addr show
     ```
   - Suchen Sie nach der IP-Adresse unter Ihrer Netzwerkverbindung (z.B. `192.168.1.100` unter `wlan0` für Wi-Fi). Darüber verbindet sich Ihr Telefon mit dem Laptop.

6. **Steuern Sie die Wiedergabe von Ihrem Telefon aus**
   - Stellen Sie sicher, dass sich Ihr Telefon und Ihr Laptop im selben Wi-Fi-Netzwerk befinden.
   - Öffnen Sie einen Webbrowser auf Ihrem Telefon und geben Sie ein: `http://<laptop-ip>:8080` (z.B. `http://192.168.1.100:8080`).
   - Wenn Sie dazu aufgefordert werden, lassen Sie das Benutzerfeld leer und geben Sie das von Ihnen festgelegte Passwort ein (z.B. "meinpasswort").
   - Sie sehen die VLC-Weboberfläche. Verwenden Sie diese, um die Wiedergabe zu starten, zu pausieren, zu stoppen oder den nächsten Film aus Ihrer Wiedergabeliste auszuwählen.

7. **Starten Sie die Wiedergabe**
   - Starten Sie auf dem Laptop einen Film in VLC (doppelklicken Sie auf einen Eintrag in der Wiedergabeliste).
   - Schalten Sie VLC in den Vollbildmodus (**Ansicht > Vollbild** oder drücken Sie `F`).
   - Lehnen Sie sich zurück und verwenden Sie Ihr Telefon, um die Wiedergabe zu steuern, ohne den Laptop berühren zu müssen.

#### Warum dies für Sie funktioniert
- **Keine zusätzlichen Kosten**: Verwendet Ihren vorhandenen Laptop, Monitor und Ihr Telefon – Sie müssen nichts Neues kaufen.
- **Minimaler Aufwand**: Nach der Erstinstallation schalten Sie einfach den Laptop und den Monitor ein, öffnen VLC und steuern alles von Ihrem Telefon aus.
- **Lokale Wiedergabe**: Da sich die Filme auf dem mit dem Monitor verbundenen Laptop befinden, müssen Sie nicht über das Netzwerk streamen (obwohl Nginx eingerichtet ist, ist es hier nicht notwendig). VLC spielt die Dateien direkt ab und gewährleistet so eine flüssige Wiedergabe.

#### Optionale Verbesserungen
- **Drahtlose Steuerung**: Wenn Sie eine drahtlose Maus oder Tastatur haben, könnten Sie diese anstelle Ihres Telefons verwenden, aber das Telefon ist aus der Entfernung bequemer.
- **Autostart**: Um es noch einfacher zu machen, richten Sie ein, dass VLC Ihre Wiedergabeliste automatisch startet, wenn der Laptop hochfährt:
  - Fügen Sie VLC mit Ihrer Wiedergabeliste zu den **Startprogramme** von Ubuntu hinzu (suchen Sie nach "Startprogramme" in Ubuntu, klicken Sie auf "Hinzufügen" und geben Sie ein: `vlc /pfad/zu/ihrer/wiedergabeliste.m3u`).
- **Audio-Check**: Wenn Ihr Monitor keine Lautsprecher hat, stellen Sie sicher, dass der Ton über den Laptop kommt oder schließen Sie externe Lautsprecher über die Audio-Buchse des Laptops an.

### Alternative: Nginx und einen Browser verwenden (falls bevorzugt)
Wenn Sie lieber den Nginx-Server nutzen möchten:
- Richten Sie eine einfache HTML-Seite in Ihrem Nginx-Verzeichnis ein (z.B. `/var/www/html/filme`) mit Links zu Ihren Filmdateien (z.B. `<a href="film1.mp4">Film 1</a>`).
- Verbinden Sie den Laptop mit dem Monitor, öffnen Sie einen Browser und gehen Sie zu `http://localhost/filme`.
- Klicken Sie auf einen Link, um einen Film im Browser abzuspielen, und verwenden Sie den Vollbildmodus.
- Dies erlaubt jedoch keine einfache Steuerung per Telefon, es sei denn, Sie rufen die gleiche Seite von Ihrem Telefon aus auf und übertragen sie, was möglicherweise zusätzliche Einrichtung oder Hardware erfordert.

### Empfehlung zum Schluss
Die VLC-Methode ist die beste Wahl. Sie ist unkompliziert, nutzt Ihr aktuelles Setup und ermöglicht es Ihnen, "den Monitor einschalten und dann ohne großen Aufwand schauen" zu können, indem Sie alles von Ihrem Telefon aus steuern. Nach der einmaligen Einrichtung müssen Sie nur noch VLC starten und Ihr Telefon verwenden, um Filme auszuwählen – einfach und effektiv!