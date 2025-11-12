---
audio: false
generated: true
lang: de
layout: post
title: Konfiguration von qBittorrent für Seeding und automatische Dateiverwaltung
translated: true
type: note
---

Es scheint, als möchtest du qBittorrent so konfigurieren, dass es deine Torrents weiter seedet, während fertige `.mkv`-Dateien automatisch in `/var/www/movies` verschoben werden, um sie auf einem Server bereitzustellen. Im Folgenden führe ich dich durch die Schritte, um dies zu erreichen. Ich gehe davon aus, dass du qBittorrent auf einem System verwendest, auf dem `/var/www/movies` ein gültiges Verzeichnis ist (z. B. ein Linux-Server mit einem Web-Server wie Apache oder Nginx). So kannst du es einrichten:

---

### Schritt-für-Schritt-Anleitung

#### 1. **qBittorrents Dateiverwaltung verstehen**
   - qBittorrent kann Dateien nach Abschluss des Downloads automatisch verschieben und sie gleichzeitig weiter seeden, solange du die integrierten Funktionen "Speicherort festlegen" oder "Verschieben" korrekt verwendest. Wenn du Dateien manuell außerhalb von qBittorrent verschiebst (z. B. über einen Dateimanager), wird das Seeding unterbrochen, es sei denn, du weist qBittorrent erneut auf den neuen Speicherort hin.

#### 2. **qBittorrent-Einstellungen konfigurieren**
   - Öffne qBittorrent.
   - Gehe zu **Werkzeuge > Einstellungen** (oder drücke `Alt + O`).

   ##### a) **Standard-Download-Speicherort festlegen**
   - Unter dem Tab **Downloads**:
     - Setze **Standard-Speicherpfad** auf ein temporäres Verzeichnis, in dem Dateien zunächst heruntergeladen werden (z. B. `/home/user/downloads` oder wo immer du Platz hast). Hier speichert qBittorrent die Dateien während des Downloads und des Seedings, bis sie verschoben werden.
     - Stelle sicher, dass **Unvollständige Dateien behalten in** auf dasselbe oder ein anderes Verzeichnis gesetzt ist, wenn du das bevorzugst (optional).

   ##### b) **Automatisches Verschieben von Dateien aktivieren**
   - Scrolle runter zu **Wenn Torrent fertig ist**:
     - Aktiviere das Kästchen für **Abgeschlossene Downloads automatisch verschieben nach**.
     - Setze den Pfad auf `/var/www/movies`. Dies weist qBittorrent an, die `.mkv`-Dateien nach `/var/www/movies` zu verschieben, sobald der Download abgeschlossen ist.
   - Wichtig: qBittorrent wird nach dem Verschieben vom neuen Speicherort (`/var/www/movies`) aus weiter seeden, du musst dir also keine Sorgen um den Verlust der Seeding-Fähigkeit machen.

   ##### c) **Optional: Nach .mkv-Dateien filtern**
   - Wenn nur `.mkv`-Dateien nach `/var/www/movies` verschoben werden sollen (und nicht andere Dateitypen wie `.txt` oder `.nfo`), kannst du stattdessen die Funktion **Externes Programm ausführen** von qBittorrent verwenden (siehe Schritt 3 unten).

   ##### d) **Seeding-Limits**
   - Unter dem Tab **BitTorrent** oder **Downloads**:
     - Setze Seeding-Limits, falls gewünscht (z. B. seeden bis ein bestimmtes Verhältnis oder eine bestimmte Zeit erreicht ist). Für unbegrenztes Seeding setze **Verhältnis** und **Zeit** auf `0` oder deaktiviere die Limits.
     - Dies stellt sicher, dass qBittorrent deine Seeds unbegrenzt von `/var/www/movies` aus hochlädt.

   - Klicke auf **Übernehmen** und **OK**, um die Einstellungen zu speichern.

#### 3. **Alternative: "Externes Programm ausführen" für mehr Kontrolle verwenden**
   - Wenn du mehr Anpassungsmöglichkeiten benötigst (z. B. nur `.mkv`-Dateien verschieben und andere am ursprünglichen Speicherort seeden lassen), verwende dies:
     - In **Einstellungen > Downloads**, scrolle zu **Externes Programm ausführen**.
     - Aktiviere **Externes Programm bei Torrent-Abschluss ausführen**.
     - Gib einen Befehl wie folgt ein:
       ```
       mv "%F"/*.mkv /var/www/movies/
       ```
       - `%F` ist ein qBittorrent-Platzhalter für den Pfad des Inhaltsordners. Dieser Befehl verschiebt nur `.mkv`-Dateien nach `/var/www/movies`.
     - Hinweis: qBittorrent wird die `.mkv`-Dateien nach dem Verschieben weiterhin von `/var/www/movies` aus seeden, aber andere Dateien (z. B. `.torrent`, `.nfo`) verbleiben am ursprünglichen Speicherort und werden von dort aus weiter geseedet, sofern du keine weiteren Anpassungen vornimmst.

#### 4. **Berechtigungen überprüfen**
   - Stelle sicher, dass qBittorrent Schreibberechtigungen für `/var/www/movies` hat:
     - Unter Linux führe aus:
       ```
       sudo chown -R <qbittorrent-user>:<qbittorrent-group> /var/www/movies
       sudo chmod -R 775 /var/www/movies
       ```
       Ersetze `<qbittorrent-user>` und `<qbittorrent-group>` mit dem Benutzer und der Gruppe, unter der qBittorrent läuft (z. B. dein Benutzername oder `qbittorrent`, wenn es ein Dienst ist).
   - Ohne die richtigen Berechtigungen kann qBittorrent keine Dateien in dieses Verzeichnis verschieben.

#### 5. **Das Setup testen**
   - Füge qBittorrent einen Torrent mit `.mkv`-Dateien hinzu.
   - Warte, bis der Download abgeschlossen ist.
   - Überprüfe Folgendes:
     - Die `.mkv`-Dateien wurden nach `/var/www/movies` verschoben.
     - Der Torrent-Status in qBittorrent wechselt auf **Seeding**, und die Upload-Geschwindigkeit zeigt an, dass die Dateien weiterhin geteilt werden.
   - Besuche `/var/www/movies`, um zu bestätigen, dass die Dateien dort sind und zugänglich sind (z. B. über deinen Web-Server unter `http://<Server-IP>/movies`).

#### 6. **Vorhandene Dateien manuell verschieben (falls nötig)**
   - Für Torrents, die du bereits heruntergeladen hast und ohne Unterbrechung des Seedings nach `/var/www/movies` verschieben möchtest:
     - Klicke in qBittorrent mit der rechten Maustaste auf den Torrent.
     - Wähle **Speicherort festlegen**.
     - Wähle `/var/www/movies` und lass qBittorrent die Dateien verschieben.
     - Nach dem Verschieben wird qBittorrent das Seeding vom neuen Speicherort aus fortsetzen.

#### 7. **Upload-Einstellungen optimieren**
   - Um das Seeding zu maximieren:
     - Gehe zu **Einstellungen > Geschwindigkeit**:
       - Setze **Upload** auf `0` (unbegrenzt) oder einen hohen Wert (z. B. 80 % deiner maximalen Upload-Geschwindigkeit).
     - Gehe zu **Einstellungen > Verbindung**:
       - Stelle sicher, dass **UPnP / NAT-PMP Portweiterleitung aktivieren** aktiviert ist (falls dein Router dies unterstützt) oder leite manuell einen Port für eine bessere Konnektivität weiter.
       - Erhöhe die **Globale maximale Anzahl von Upload-Slots** (z. B. auf 50 oder 100), um mehr Peers die Verbindung zu ermöglichen.

---

### Wichtige Hinweise
- **Kontinuierliches Seeding**: Solange du qBittorrent das Verschieben der Dateien überlässt (über automatisches Verschieben oder "Speicherort festlegen"), aktualisiert es seine interne Nachverfolgung und seedet weiter von `/var/www/movies` aus.
- **Web-Server-Zugriff**: Stelle sicher, dass dein Web-Server (z. B. Apache/Nginx) so konfiguriert ist, dass er Dateien aus `/var/www/movies` bereitstellt. Dies geht über den Rahmen von qBittorrent hinaus, ist aber für dein Server-Ziel entscheidend.
- **Speicherplatz**: Stelle sicher, dass `/var/www/movies` genügend Platz für deine Dateien hat.

Wenn du auf Probleme stößt (z. B. Dateien werden nicht verschoben oder das Seeding stoppt), teile mir bitte die Details deines Setups mit (Betriebssystem, qBittorrent-Version, etc.), und ich werde die Lösung verfeinern!