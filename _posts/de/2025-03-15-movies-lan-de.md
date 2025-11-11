---
audio: false
generated: true
lang: de
layout: post
title: Streamen von Filmen im lokalen Netzwerk
translated: true
type: note
---

Um auf die mit qBittorrent auf Ihrem Laptop heruntergeladenen Filme von Ihrem iPad aus zuzugreifen, während sich beide Geräte im selben lokalen Netzwerk (LAN) befinden, haben Sie mehrere Möglichkeiten. Sie haben speziell nach der Verwendung von NAS-Software oder der Einrichtung eines Nginx-Media-Servers gefragt, daher gehe ich auf diese ein und biete einen empfohlenen Ansatz basierend auf Benutzerfreundlichkeit und Funktionalität.

---

### Option 1: Verwendung von NAS-Software (Empfohlen: Plex Media Server)
NAS steht für Network Attached Storage und bezeichnet typischerweise ein Gerät, das Dateien über ein Netzwerk speichert und freigibt. Da Sie jedoch Ihren Laptop zum Herunterladen von Filmen verwenden, können Sie Software installieren, um ihn in ein NAS-ähnliches Gerät zu verwandeln. Eine beliebte und benutzerfreundliche Wahl ist **Plex Media Server**, das sowohl als Dateifreigabe-Lösung als auch als Media-Server mit zusätzlichen Funktionen dient, wie z.B. der Organisation Ihrer Filme und dem nahtlosen Streamen.

#### Schritte zur Einrichtung von Plex:
1. **Installieren Sie Plex Media Server auf Ihrem Laptop:**
   - Laden Sie Plex Media Server von [plex.tv](https://www.plex.tv) herunter und installieren Sie es auf Ihrem Laptop (verfügbar für Windows, macOS oder Linux).
   - Folgen Sie dem Setup-Assistenten, um ein Konto zu erstellen (optional für die lokale Verwendung) und den Server zu konfigurieren.

2. **Fügen Sie Ihren Filmordner hinzu:**
   - Weisen Sie Plex während der Einrichtung auf den Ordner hin, in dem qBittorrent Ihre heruntergeladenen Filme speichert. Dies fügt die Filme Ihrer Plex-Bibliothek hinzu, und Plex kann automatisch Metadaten (wie Poster und Beschreibungen) abrufen.

3. **Installieren Sie Plex auf Ihrem iPad:**
   - Laden Sie die kostenlose Plex-App aus dem App Store auf Ihrem iPad herunter.

4. **Greifen Sie auf Ihre Filme zu:**
   - Stellen Sie sicher, dass sich sowohl Ihr Laptop als auch Ihr iPad im selben Wi-Fi-Netzwerk befinden.
   - Öffnen Sie die Plex-App auf Ihrem iPad – sie sollte den auf Ihrem Laptop laufenden Plex-Server automatisch erkennen.
   - Durchsuchen Sie Ihre Filmbibliothek und tippen Sie auf einen Film, um ihn abzuspielen. Die Plex-App streamt das Video direkt von Ihrem Laptop.

#### Vorteile:
- **Benutzerfreundlich:** Bietet eine polierte Oberfläche mit Filmplakaten und Details.
- **Transkodierung:** Wenn ein Filmformat von Ihrem iPad nicht nativ unterstützt wird, kann Plex es on-the-fly konvertieren (erfordert jedoch möglicherweise ausreichende Laptop-Ressourcen).
- **Keine technischen Kenntnisse nötig:** Die Einrichtung ist unkompliziert mit einem geführten Prozess.

#### Zu beachten:
- Die kostenlose Version von Plex ist für das lokale Streaming innerhalb Ihres LANs ausreichend.
- Ihr Laptop muss eingeschaltet und mit dem Netzwerk verbunden bleiben, während Sie Filme schauen.

---

### Option 2: Einfache Dateifreigabe (Ohne zusätzliche Software)
Wenn Sie eine schlanke Lösung ohne zusätzliche Software bevorzugen, können Sie den Filmordner direkt von Ihrem Laptop aus freigeben, indem Sie die integrierten Dateifreigabe-Funktionen Ihres Betriebssystems verwenden. Dies nutzt das SMB-Protokoll (Server Message Block), das von der Dateien-App des iPads unterstützt wird.

#### Schritte zur Einrichtung der Dateifreigabe:
1. **Geben Sie den Ordner auf Ihrem Laptop frei:**
   - **Windows:** Klicken Sie mit der rechten Maustaste auf den Ordner, in dem qBittorrent Filme speichert, wählen Sie "Eigenschaften", gehen Sie zum Tab "Freigabe" und klicken Sie auf "Freigabe". Wählen Sie, ihn für "Jeder" oder bestimmte Benutzer freizugeben, und setzen Sie die Berechtigungen.
   - **macOS:** Öffnen Sie Systemeinstellungen > Allgemein > Freigabe, aktivieren Sie "Dateifreigabe" und fügen Sie den Filmordner hinzu, wobei Sie die Berechtigungen nach Bedarf festlegen.
   - **Linux:** Installieren und konfigurieren Sie Samba, um den Ordner freizugeben (erfordert einige Kommandozeilen-Einrichtung).

2. **Finden Sie die IP-Adresse Ihres Laptops:**
   - Öffnen Sie auf Ihrem Laptop eine Eingabeaufforderung oder ein Terminal und geben Sie `ipconfig` (Windows) oder `ifconfig`/`ip addr` (Linux/macOS) ein, um die IP-Adresse zu finden (z.B. 192.168.1.100).

3. **Verbinden Sie sich von Ihrem iPad aus:**
   - Öffnen Sie die **Dateien**-App auf Ihrem iPad.
   - Tippen Sie auf die drei Punkte (...) in der oberen rechten Ecke und wählen Sie "Mit Server verbinden".
   - Geben Sie `smb://<Laptop-IP>` ein (z.B. `smb://192.168.1.100`) und tippen Sie auf "Verbinden". Geben Sie bei Aufforderung Anmeldedaten ein (z.B. den Benutzernamen und das Passwort Ihres Laptops).
   - Navigieren Sie zum freigegebenen Ordner.

4. **Spielen Sie die Filme ab:**
   - Tippen Sie auf eine Filmdatei, um sie im Standard-Player der Dateien-App zu öffnen, oder verwenden Sie eine Drittanbieter-App wie **VLC for Mobile** (im App Store erhältlich) für eine breitere Formatunterstützung.

#### Vorteile:
- **Einfach:** Keine zusätzliche Software erforderlich, außer dem, was bereits auf Ihrem Laptop vorhanden ist.
- **Schnelle Einrichtung:** Funktioniert mit Ihrem vorhandenen System.

#### Zu beachten:
- Das Durchsuchen von Dateien ist weniger intuitiv als bei Plex – Sie sehen eine einfache Ordnerstruktur.
- Die Wiedergabe hängt davon ab, ob das Filmformat vom iPad unterstützt wird (z.B. MP4 mit H.264 funktioniert nativ gut; VLC kann mehr Formate verarbeiten).
- Ihr Laptop muss eingeschaltet und mit dem LAN verbunden sein.

---

### Option 3: Einrichtung eines Nginx-Media-Servers
Nginx ist ein schlanker Web-Server, der Dateien über HTTP bereitstellen kann. Sie können ihn auf Ihrem Laptop konfigurieren, um Ihren Filmordner über einen Webbrowser oder Media-Player auf Ihrem iPad zugänglich zu machen.

#### Schritte zur Einrichtung von Nginx:
1. **Installieren Sie Nginx auf Ihrem Laptop:**
   - Laden Sie Nginx von [nginx.org](https://nginx.org) herunter und installieren Sie es (verfügbar für Windows, macOS oder Linux) oder verwenden Sie einen Paketmanager (z.B. `sudo apt install nginx` auf Ubuntu).

2. **Konfigurieren Sie Nginx:**
   - Bearbeiten Sie die Nginx-Konfigurationsdatei (z.B. `/etc/nginx/nginx.conf` unter Linux oder einen ähnlichen Ort):
     ```
     server {
         listen 80;
         server_name localhost;
         location /movies {
             root /pfad/zu/ihrem/filmordner;
             autoindex on; # Aktiviert Verzeichnisauflistung
         }
     }
     ```
   - Ersetzen Sie `/pfad/zu/ihrem/filmordner` mit dem tatsächlichen Pfad, in dem qBittorrent Filme speichert.

3. **Starten Sie Nginx:**
   - Führen Sie `nginx` (Windows) oder `sudo systemctl start nginx` (Linux) aus, um den Server zu starten.

4. **Greifen Sie von Ihrem iPad aus zu:**
   - Öffnen Sie Safari oder einen anderen Browser auf Ihrem iPad.
   - Geben Sie `http://<Laptop-IP>/movies` ein (z.B. `http://192.168.1.100/movies`).
   - Sie sehen eine Liste der Filmdateien. Tippen Sie auf eine, um sie im Browser abzuspielen, oder kopieren Sie den Link und öffnen Sie ihn in einem Media-Player wie VLC.

#### Vorteile:
- **Schlank:** Verbraucht weniger Ressourcen als Plex.
- **Anpassbar:** Sie können die Nginx-Einstellungen nach Bedarf anpassen.

#### Zu beachten:
- **Technische Einrichtung:** Erfordert das Bearbeiten von Konfigurationsdateien und einige Server-Kenntnisse.
- **Grundlegendes Erlebnis:** Keine ansprechende Oberfläche – nur eine Dateiliste im Browser.
- **Wiedergabe:** Hängt davon ab, ob der Browser oder die App das Filmformat unterstützt; es steht keine Transkodierung zur Verfügung.

---

### Empfehlung
Angesichts Ihrer Optionen empfehle ich, **Plex Media Server** als Ihre "NAS-Software"-Lösung zu verwenden. Hier ist der Grund:
- **Benutzerfreundlichkeit:** Plex ist einfacher einzurichten als Nginx und bietet ein viel besseres Erlebnis als die einfache Dateifreigabe.
- **Funktionen:** Es organisiert Ihre Filme, unterstützt bei Bedarf Transkodierung und bietet eine dedizierte iPad-App für nahtloses Streaming.
- **LAN-Fokus:** Funktioniert perfekt innerhalb Ihres lokalen Netzwerks, wie von Ihnen angegeben.

Wenn Sie die Installation von Software vermeiden möchten, ist die **Dateifreigabe**-Methode eine gute Alternative – geben Sie einfach den Ordner frei und verwenden Sie die Dateien-App mit VLC auf Ihrem iPad. **Nginx** ist für diesen Anwendungsfall jedoch übertrieben, es sei denn, Sie sind mit der Server-Konfiguration vertraut und bevorzugen einen minimalen Aufbau.

#### Endgültige Antwort
Für die beste Erfahrung installieren Sie Plex Media Server auf Ihrem Laptop, fügen Ihren qBittorrent-Download-Ordner hinzu und verwenden Sie die Plex-App auf Ihrem iPad, um Ihre Filme über Ihr LAN anzusehen. Alternativ, für einen einfacheren Ansatz, geben Sie den Ordner via SMB frei und greifen Sie mit der Dateien-App und VLC auf Ihrem iPad darauf zu.