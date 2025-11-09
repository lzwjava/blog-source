---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Befreien Sie Speicherplatz auf dem macOS-System
translated: true
type: note
---

### Übersicht zur Bereinigung des macOS-Systemspeichers

Basierend auf den offiziellen Richtlinien von Apple und Expertenempfehlungen umfasst das Freigeben von Speicherplatz auf macOS (Version 15.6.1 wie bei Ihnen) integrierte Tools zur Optimierung des Speichers, das sichere Löschen entfernbarer Caches und das Löschen unnötiger Dateien. Systemdaten umfassen oft Caches, temporäre Dateien und Protokolle – vieles davon kann manuell oder automatisch gelöscht werden, ohne Ihren Mac zu beschädigen. Vermeiden Sie das Löschen kritischer Systemdateien, da dies zu Instabilität führen könnte. Ihr System zeigt etwa 13 GiB verfügbar von 460 GiB Gesamtspeicher an, wobei 45 % belegt sind. Konzentrieren Sie sich daher auf Caches, Downloads und Anhänge, um schnell Platz zu gewinnen.[1][2][3]

### Verwendung der integrierten macOS-Speicherverwaltungstools
Apple bietet integrierte Möglichkeiten, um Speicherplatz zu analysieren und freizugeben, ohne dass Drittanbieter-Apps erforderlich sind.
1.  **Speichernutzung überprüfen**: Gehen Sie zu Apple-Menü > Systemeinstellungen > Allgemein > Speicher. Dies zeigt eine farbcodierte Aufschlüsselung (z. B. Apps, Dokumente, Systemdaten). Klicken Sie auf eine Kategorie, um Empfehlungen zu erhalten.[1]
2.  **Speicher automatisch optimieren**: Aktivieren Sie in den Speichereinstellungen "Speicher optimieren", um nicht verwendete App-Daten auszulagern und Anhänge zu verwalten. Schalten Sie auch "Papierkorb automatisch leeren" nach 30 Tagen ein.[1]
3.  **Papierkorb und Downloads-Ordner leeren**: Systemdaten beinhalten Papierkorb-Inhalte – leeren Sie ihn manuell über den Finder. Überprüfen Sie ~/Downloads auf alte Dateien und löschen Sie diese.[1][2]
4.  **Große Anhänge verwalten**: Gehen Sie zu Speichereinstellungen > Programme > Verwalten > Mail > "Speicher optimieren", um große E-Mail-Anhänge bei Bedarf herunterzuladen.[1]

Für eine gründlichere Reinigung verwenden Sie den Tab "Vorherige Elemente" im Speicher, um kürzliche Backups (wie Time Machine Backups) zu überprüfen und bei Bedarf zu entfernen.[2]

### Identifizieren und Löschen entfernbarer Cache-Dateien
Caches sind temporäre Dateien, die Apps beschleunigen, aber Gigabytes an Speicher belegen können. Löschen Sie Benutzer-Caches sicher über den Finder; vermeiden Sie System-Caches, es sei denn, Sie werden von Apple Support angewiesen, um Probleme zu vermeiden. Die Caches Ihres Macs befinden sich in Library-Ordnern – überprüfen Sie die Größen mit "Informationen" im Finder.

1.  **Benutzer-Cache-Verzeichnis (Am sichersten zu löschen)**:
    *   Navigieren Sie zu Finder > Gehe zu > Gehe zum Ordner, geben Sie `~/Library/Caches` ein und drücken Sie die Eingabetaste.
    *   Dieser Ordner enthält App-Caches (z. B. für Browser, Office-Apps). Wählen Sie alle darin enthaltenen Ordner aus und löschen Sie sie. Diese sind größtenteils sicher und regenerieren sich neu.
    *   Tipp: Überprüfen Sie Unterordner wie `com.apple.*` auf Apple-App-Caches, überspringen Sie diese jedoch, wenn Sie unsicher sind. Leeren Sie anschließend den Papierkorb.[4][2]

2.  **Anwendungsspezifische Caches**:
    *   Browser: In Safari löschen Sie den Verlauf/die Caches über das Safari-Menü > Verlauf löschen. Für Chrome/Google-Apps: Gehen Sie zu Chrome > Einstellungen > Datenschutz und Sicherheit > Browserdaten löschen.
    *   Xcode/Developer: Wenn Sie programmieren, löschen Sie abgeleitete Daten unter Xcode > Einstellungen > Orte > Abgeleitete Daten.
    *   Andere Apps: Überprüfen Sie die App-Einstellungen auf Optionen zum Löschen des Caches oder verwenden Sie den Finder, um die Unterordner von `~/Library/Caches` anzuzeigen.[2][3]

3.  **System- und Library-Caches (Mit Vorsicht vorgehen)**:
    *   `/Library/Caches` kann System-Caches enthalten – löschen Sie hier nur bestimmte Ordner wie veraltete App-Caches, keine Kernsystem-Caches (z. B. vermeiden Sie `com.apple.coreservices`).
    *   Um Größen sicher zu analysieren, verwenden Sie das Terminal, um große Caches aufzulisten: Öffnen Sie das Terminal und führen Sie `du -sh /Library/Caches/* | sort -h` aus.
    *   Letzter Ausweg für tiefe System-Caches: Starten Sie im Wiederherstellungsmodus neu (Befehlstaste+R beim Start) und führen Sie die Datenträgerhilfe > Erste Hilfe aus, starten Sie dann neu und verwenden Sie die Speicher-Tools.[2]

### Zusätzliche Tipps für manuelle und sichere Bereinigung
*   **Temporäre und Protokolldateien entfernen**: Systemdaten beinhalten Protokolle in `/private/var/log`. Verwenden Sie Terminal-Befehle wie `sudo rm -rf /private/var/log/asl/*.asl` für ältere Apple-Protokolle (melden Sie sich zuerst ab und wieder an). Für temporäre Dateien löschen Sie aus `/tmp` via `sudo rm -rf /tmp/*` nach einer Überprüfung.[2]
*   **Auf externen Speicher auslagern**: Verschieben Sie Fotos/Videos über die Speichereinstellungen > "In iCloud speichern" in iCloud oder auf ein externes Laufwerk.[1]
*   **Apps zur sicheren Analyse**: Tools von Drittanbietern wie CleanMyMac (von MacPaw) oder OmniDiskSweeper suchen nach großen Caches/Dateien – verwenden Sie diese zur Orientierung, aber sichern Sie Ihre Daten immer zuerst (z. B. via Time Machine).[3]
*   **Nach der Bereinigung überwachen**: Starten Sie nach größeren Löschvorgängen neu, um den Systemzustand zu aktualisieren. Überprüfen Sie die Speichernutzung erneut; das Löschen von regenerierbaren Caches sollte die Leistung nicht beeinträchtigen.[2]

Wenn die Systemdaten weiterhin hoch bleiben (z. B. 218 GB wie in einigen Berichten), könnte es sich um versteckte Backups oder beschädigte Dateien handeln – der Apple Support schlägt vor, `tmutil thinlocalsnapshots / 10000000000 4` im Terminal für Time Machine-Bereinigungen auszuführen.[5] Stellen Sie sicher, dass Sie Backups haben, bevor Sie fortfahren. Diese Methoden sollten auf Apple Silicon Macs wie Ihrem M2 signifikant Speicherplatz zurückgewinnen, ohne Risiken.[1][2][4]

Quellen:
[1] https://support.apple.com/en-us/102624
[2] https://macpaw.com/how-to/clear-system-storage-mac
[3] https://nektony.com/how-to/clean-up-system-storage-on-mac?srsltid=AfmBOorJjQPPX59Jw3MM47n0NZ8DQlerYQAbkZdymj0rUZM0rtLZlw1s
[4] https://www.reddit.com/r/MacOS/comments/154rp99/how_to_do_i_clear_system_data_on_mac_os/
[5] https://discussions.apple.com/thread/255084458