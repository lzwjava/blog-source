---
audio: false
generated: true
lang: de
layout: post
title: Ein Infuse-Problem
translated: true
type: note
---

Der Fehler "Failed to open input stream in demuxing stream" in Infuse deutet normalerweise darauf hin, dass die App nicht richtig auf die Videodatei zugreifen oder sie verarbeiten kann, die Sie streamen möchten. Da Sie `.mkv`-Dateien von Ihrem Nginx-Server streamen (z.B. `http://192.168.1.27/movies/yourfile.mkv`) und es mit VLC funktioniert, aber nicht mit Infuse, könnte das Problem auf Netzwerkprobleme, Dateikompatibilität oder Infuse-spezifische Eigenheiten zurückzuführen sein. So beheben Sie das Problem:

### 1. Netzwerkkonnektivität überprüfen
Infuse zeigt diesen Fehler oft aufgrund von Netzwerkunterbrechungen oder Fehlkonfigurationen an.
- **Erreichbarkeit testen**: Stellen Sie von Ihrem iPad (oder wo auch immer Infuse läuft) sicher, dass die URL funktioniert:
  - Öffnen Sie Safari und gehen Sie zu `http://192.168.1.27/movies/`. Sie sollten die Dateiliste sehen.
  - Tippen Sie auf `yourfile.mkv` – sie wird vielleicht nicht abgespielt, aber bestätigen Sie, dass der Link erreichbar ist.
- **Server anpingen**: Verwenden Sie auf Ihrem iPad eine App wie **Network Ping Lite** (kostenlos im App Store), um `192.168.1.27` zu pingen. Falls dies fehlschlägt, überprüfen Sie Ihr Wi-Fi oder die Server-Firewall.
- **Firewall-Check**: Auf Ihrem Ubuntu-Server:
  ```bash
  sudo ufw status
  ```
  Stellen Sie sicher, dass Port 80 offen ist (`80/tcp ALLOW`). Falls nicht:
  ```bash
  sudo ufw allow 80
  sudo systemctl restart nginx
  ```

### 2. Infuse und Gerät neu starten
Vorübergehende Störungen können diesen Fehler verursachen.
- **Infuse schließen**: Drücken Sie zweimal auf den Home-Button (oder wischen Sie auf neueren iPads nach oben) und wischen Sie Infuse weg.
- **Erneut öffnen**: Starten Sie Infuse und versuchen Sie den Stream erneut.
- **iPad neu starten**: Halten Sie den Power-Button gedrückt, schieben Sie zum Ausschalten und starten Sie das Gerät neu. Testen Sie es erneut.

### 3. Dateikompatibilität prüfen
Obwohl Infuse `.mkv` unterstützt, könnte der Fehler mit den Codecs oder der Struktur der Datei zusammenhängen.
- **Eine andere Datei testen**: Laden Sie eine kleine, bekannte funktionierende `.mkv`-Datei (z.B. kodiert mit H.264-Video und AAC-Audio) nach `/var/www/movies/` hoch:
  ```bash
  sudo mv /pfad/zur/testdatei.mkv /var/www/movies/
  sudo chown www-data:www-data /var/www/movies/testfile.mkv
  sudo chmod 644 /var/www/movies/testfile.mkv
  ```
  Versuchen Sie, `http://192.168.1.27/movies/testfile.mkv` in Infuse zu streamen.
- **Codec-Check**: Da VLC die Datei abspielt, ist sie wahrscheinlich streamfähig, aber Infuse könnte Probleme mit seltenen Codecs haben (z.B. VP9, Opus). Verwenden Sie VLC auf Ihrem Mac zur Überprüfung:
  - Öffnen Sie die `.mkv`-Datei, drücken Sie `Cmd + I` (Werkzeuge > Codec-Information) und notieren Sie sich die Video-/Audiocodecs.
  - Falls es nicht H.264/AAC ist, enkodieren Sie die Datei mit HandBrake (kostenlos, handbrake.fr) neu:
    - Laden Sie die `.mkv`-Datei, wählen Sie "H.264 (x264)" für Video und "AAC" für Audio und konvertieren Sie sie.

### 4. Nginx-Konfiguration anpassen
Infuse benötigt möglicherweise spezielle Header oder Einstellungen für ein reibungsloses Streaming.
- **Konfiguration aktualisieren**: Bearbeiten Sie Ihre Nginx-Datei (z.B. `/etc/nginx/sites-enabled/default`):
  ```nginx
  server {
      listen 80;
      server_name 192.168.1.27 localhost;

      location /movies/ {
          alias /var/www/movies/;
          autoindex on;
          add_header Accept-Ranges bytes;  # Stellt sicher, dass Range Requests funktionieren
          add_header Content-Disposition "inline";  # Hilft beim Streaming
      }
  }
  ```
- **Neu laden**:
  ```bash
  sudo nginx -t
  sudo systemctl reload nginx
  ```
- **Warum**: `Accept-Ranges` stellt sicher, dass Infuse Teile der Datei anfordern kann (kritisch für Streaming).

### 5. Diagnosebericht senden
Die Entwickler von Infuse schlagen dies bei anhaltenden Problemen vor.
- **Schritte**:
  1. Gehen Sie in Infuse zu **Einstellungen > Allgemein**.
  2. Tippen Sie auf **Diagnosebericht senden**.
  3. Notieren Sie sich den angezeigten Code.
  4. Besuchen Sie das [Firecore Community Forum](https://community.firecore.com/), posten Sie den Code und beschreiben Sie Ihr Setup (Nginx, `.mkv`, HTTP-Streaming).
- **Warum**: Die Entwickler können so eingrenzen, ob es sich um einen Bug oder ein Konfigurationsproblem handelt.

### 6. Alternative Problemumgehung
Falls Infuse weiterhin fehlschlägt:
- **VLC verwenden**: Bleiben Sie bei VLC for Mobile auf Ihrem iPad (da es zuverlässig funktioniert).
- **App wechseln**: Versuchen Sie es mit **nPlayer** oder **PlayerXtreme** (App Store) mit der gleichen URL.

### Wahrscheinliche Ursache
Da VLC den Stream problemlos abspielt, handelt es sich wahrscheinlich um ein Netzwerkproblem oder um die strengere Handhabung des HTTP-Streams durch Infuse. Die Nginx-Anpassung (Schritt 4) und eine Testdatei (Schritt 3) lösen das Problem oft. Falls nicht, wird der Diagnosebericht Klarheit schaffen.

Lassen Sie mich wissen, was Sie nach dem Ausprobieren dieser Schritte feststellen – insbesondere alle Log-Fehler oder den Diagnose-Code!