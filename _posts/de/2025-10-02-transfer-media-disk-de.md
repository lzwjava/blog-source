---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Medien auf externe Festplatte übertragen
translated: true
type: note
---

### Fotos und Videos auf ein portables Laufwerk unter macOS verschieben

Basierend auf Ihren Systeminformationen haben Sie ein macOS 15.6.1 System mit einem portablen Laufwerk, das unter `/Volumes/Untitled` eingehängt ist (2,0 TB Gesamtkapazität, 1,5 TB verfügbar). Das Verschieben von Fotos und Videos beinhaltet die Übertragung von Dateien vom Speicher Ihres Macs (z.B. in `~/Pictures` für Fotos oder `~/Movies` für Videos) auf das externe Laufwerk. Dies kann über die grafische Oberfläche (Finder) oder Befehlszeilen-Tools wie das Terminal erfolgen, je nach Präferenz. Ich werde beide Methoden unten behandeln, unter der Annahme, dass Sie Dateien verschieben und nicht die gesamte Photos-App-Bibliothek (falls dies benötigt wird, exportieren Sie sie zuerst aus der Photos-App).

**Wichtige Hinweise:**
- **Zuerst sichern:** Stellen Sie sicher, dass Sie Backups Ihrer Dateien haben, um Datenverlust bei Fehlern zu vermeiden.
- **Berechtigungen:** Sie benötigen möglicherweise Administratorberechtigungen für bestimmte Aktionen. Führen Sie Terminal-Befehle als Admin aus, wenn dazu aufgefordert.
- **Platz prüfen:** Vergewissern Sie sich, dass die Dateigröße den verfügbaren Platz auf dem portablen Laufwerk (in Ihrem Fall 1,5 TB) nicht überschreitet.
- **Dateipfade:** Standardpfade sind `~/Pictures` für Fotos und `~/Movies` für Videos. Wenn sie sich in anderen Verzeichnissen befinden (z.B. Downloads), passen Sie die Pfade entsprechend an.
- **Sicher auswerfen:** Werfen Sie das Laufwerk nach dem Verschieben sicher aus über Finder > Auswerfen oder `diskutil unmount /Volumes/Untitled`, um Beschädigungen zu vermeiden.

#### 1. Finder verwenden (Grafische Methode - Einsteigerfreundlich)
Dies ist die einfachste Methode für die meisten Benutzer. Sie beinhaltet Drag-and-Drop über den Dateimanager von macOS.

1. **Portables Laufwerk und Dateien lokalisieren:**
   - Öffnen Sie den Finder (klicken Sie auf das Smiley-Gesicht-Symbol im Dock).
   - In der Seitenleiste unter "Ort" sehen Sie "Untitled" (Ihr portables Laufwerk). Klicken Sie darauf, um den Inhalt zu durchsuchen.
   - Öffnen Sie ein separates Finder-Fenster (Befehlstaste + N) und navigieren Sie dorthin, wo Ihre Fotos/Videos gespeichert sind (z.B. Ihren Bilder- oder Filme-Ordner).

2. **Dateien verschieben:**
   - Wählen Sie die Fotos/Videos aus, die Sie verschieben möchten (halten Sie die Befehlstaste gedrückt, um mehrere auszuwählen).
   - Ziehen Sie sie von ihrem aktuellen Speicherort in das Fenster des portablen Laufwerks (z.B. erstellen Sie zuerst einen Ordner wie "PhotosBackup" auf dem Laufwerk zur Organisation).
   - Um zu **verschieben** (dauerhaft umzulagern und Speicherplatz auf Ihrem Mac freizugeben), halten Sie die Wahltaste gedrückt, während Sie ziehen. Um zu **kopieren** (zu duplizieren), ziehen Sie sie einfach normal.
     - Alternativ können Sie die ausgewählten Dateien auch nach dem Kopieren mit der rechten Maustaste anklicken > "In den Papierkorb verschieben", um sie effektiv zu "verschieben", indem die Originale nach dem Kopieren gelöscht werden.
   - Wenn Sie organisieren möchten, erstellen Sie Ordner auf dem Laufwerk (Rechtsklick > Neuer Ordner) wie "Photos" und "Videos".

3. **Überprüfen und auswerfen:**
   - Öffnen Sie das portable Laufwerk im Finder und vergewissern Sie sich, dass die Dateien dort sind.
   - Ziehen Sie das Laufwerkssymbol auf den Papierkorb (oder Rechtsklick > Auswerfen), um es sicher auszuwerfen, bevor Sie die Verbindung trennen.

Diese Methode erhält Metadaten (z.B. Erstellungsdaten) und verarbeitet große Dateien effizient.

#### 2. Terminal verwenden (Befehlszeilen-Methode - Effizient für Massenvorgänge)
Wenn Sie Skripte bevorzugen oder Befehle verwenden möchten (wie in Ihren Python-Skripten gezeigt), verwenden Sie das Terminal für Präzision. Dies ist nützlich für automatisierte oder rekursive Verschiebevorgänge.

1. **Zu Ihren Dateien und dem Laufwerk navigieren:**
   - Öffnen Sie das Terminal (Programme > Dienstprogramme > Terminal).
   - Überprüfen Sie Ihr aktuelles Verzeichnis: Führen Sie `pwd` aus und navigieren Sie bei Bedarf (z.B. `cd ~/Pictures`, um auf Fotos zuzugreifen).
   - Bestätigen Sie, dass das Laufwerk eingehängt ist: Führen Sie `ls /Volumes` aus, um "Untitled" zu sehen. Basierend auf der bereitgestellten Ausgabe ist Ihr Laufwerk bereits eingehängt.

2. **Dateien verschieben:**
   - Um Dateien zu **verschieben** (dauerhaft umzulagern und vom ursprünglichen Speicherort zu löschen):
     - Für einzelne Dateien: `mv /pfad/zum/foto.jpg /Volumes/Untitled/Photos/`
     - Für Verzeichnisse (z.B. gesamten Photos-Ordner): `mv ~/Pictures/PhotosLibrary /Volumes/Untitled/`
     - Beispiel für vollständiges Verschieben: `mv ~/Pictures/* /Volumes/Untitled/Photos/` (verschiebt alle Inhalte von Pictures in einen neuen Ordner auf dem Laufwerk; fügen Sie Optionen wie `-v` für ausführliche Ausgabe hinzu).
   - Um stattdessen zu **kopieren** (zu duplizieren ohne Originale zu löschen): Verwenden Sie `cp` mit `-r` für rekursive Verzeichnisse.
     - Beispiel: `cp -r ~/Pictures/PhotosLibrary /Volumes/Untitled/Photos/` (kopiert rekursiv; ideal für Backups, bei denen Sie die Originale behalten möchten).
   - Für Videos in Movies: `cp -r ~/Movies/Videos/ /Volumes/Untitled/Videos/`
   - Um versteckte Dateien oder Berechtigungen zu behandeln: Fügen Sie `sudo` hinzu, falls benötigt (z.B. `sudo mv ~/Pictures/photo.jpg /Volumes/Untitled/`).
   - Zur Sicherheit können Sie eine Vorschau anzeigen, was Sie verschieben werden: `ls -la ~/Pictures`, um Dateien aufzulisten.

3. **Überprüfen und auswerfen:**
   - Überprüfen Sie das Laufwerk: `ls /Volumes/Untitled`, um die Übertragungen zu bestätigen.
   - Werfen Sie sicher aus: `diskutil unmount /Volumes/Untitled` und trennen Sie dann das Laufwerk physisch.

**Erweiterte Tipps:**
- **Rsync für Synchronisation verwenden:** Für inkrementelle Backups (nur neue/geänderte Dateien): `rsync -av ~/Pictures /Volumes/Untitled/Photos` (installieren Sie rsync, falls nicht vorhanden, aber es ist in macOS integriert).
- **Automatisierung:** Integrieren Sie dies in Ihre Python-Skripte (z.B. mit `subprocess`, um `cp`- oder `mv`-Befehle basierend auf der Ausgabe von `list_portable_disks.py` auszuführen).
- **MacBook spezifisch:** Auf Ihrem M2 MacBook Air (Modell Mac14,2) sollten Übertragungen via USB-C schnell sein. Überwachen Sie bei Bedarf Akku/Temperatur (z.B. via Aktivitätsmonitor).

Wenn Sie auf Probleme stoßen (z.B. Berechtigungsfehler), geben Sie bitte genauere Details wie exakte Dateipfade oder Fehlermeldungen für eine maßgeschneiderte Beratung an. Dieser Prozess sollte auf Ihrem Setup zuverlässig funktionieren.