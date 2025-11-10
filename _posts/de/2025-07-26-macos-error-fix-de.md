---
audio: false
generated: true
lang: de
layout: post
title: Beheben von macOS-Dateiberechtigungsfehlern
translated: true
type: note
---

### Den Fehler verstehen
Diese Fehlermeldung erscheint normalerweise auf macOS, wenn Sie versuchen, Dateien oder Ordner zu verschieben, zu kopieren, zu löschen oder anderweitig zu manipulieren (z. B. beim Leeren des Papierkorbs oder beim Ziehen von Elementen), aber das System auf Berechtigungsprobleme, gesperrte Dateien oder Schreibschutzeinschränkungen stößt. Die Meldung selbst bietet die grundlegende Lösung, manchmal sind jedoch zusätzliche Schritte erforderlich, wenn das Problem bestehen bleibt, wie die Verwendung von Terminal-Befehlen, das Reparieren von Datenträgerberechtigungen oder der Umgang mit hartnäckigen Dateien.

### Schritt-für-Schritt-Lösungen
Befolgen Sie diese in der angegebenen Reihenfolge, beginnend mit der einfachsten. Diese Schritte setzen voraus, dass Sie macOS (z. B. Ventura, Sonoma oder neuer) verwenden. Stellen Sie sicher, dass Sie als Administrator-Benutzer angemeldet sind.

1.  **Dateien entsperren und Berechtigungen anpassen (wie in der Fehlermeldung vorgeschlagen)**:
    *   Wählen Sie die problematische Datei oder den Ordner im Finder aus.
    *   Klicken Sie mit der rechten Maustaste (oder Ctrl-Taste) darauf und wählen Sie **Informationen** (oder drücken Sie Command + I).
    *   Im Fenster "Informationen":
        *   Deaktivieren Sie im Abschnitt **Allgemein** das Kästchen **Gesperrt**, falls es aktiviert ist.
        *   Scrollen Sie zum Abschnitt **Freigabe & Berechtigungen** unten.
        *   Klicken Sie auf das Schlosssymbol in der unteren rechten Ecke und geben Sie Ihr Admin-Passwort ein, um Änderungen freizuschalten.
        *   Setzen Sie für Ihren Benutzernamen (oder "jeder", falls nötig) das Privileg auf **Lesen & Schreiben**.
    *   Wenn mehrere Elemente betroffen sind, können Sie alle auswählen, "Informationen" öffnen und die Änderungen anwenden (halten Sie die Befehlstaste gedrückt, um mehrere auszuwählen).
    *   Schließen Sie das Fenster und wiederholen Sie den Vorgang (z. B. Löschen oder Verschieben der Dateien).

2.  **Wenn das Problem mit dem Papierkorb zusammenhängt (häufiges Szenario)**:
    *   Dieser Fehler tritt oft auf, wenn der Papierkorb geleert werden soll, aber Dateien gesperrt sind oder Berechtigungsprobleme haben.
    *   Öffnen Sie zunächst den Papierkorb, wählen Sie die Elemente aus und wenden Sie die oben genannten Schritte unter "Informationen" an, um sie zu entsperren/die Berechtigungen anzupassen.
    *   Wenn das nicht funktioniert, leeren Sie den Papierkorb zwangsweise:
        *   Halten Sie die Wahltaste gedrückt, während Sie mit der rechten Maustaste auf das Papierkorbsymbol im Dock klicken, und wählen Sie **Papierkorb leeren**.
    *   Alternative über das Terminal (falls die grafische Oberfläche versagt):
        *   Öffnen Sie das Terminal (über Programme > Dienstprogramme oder die Spotlight-Suche).
        *   Tippen Sie: `sudo rm -rf ~/.Trash/*` und drücken Sie die Eingabetaste.
        *   Geben Sie Ihr Admin-Passwort ein (es wird nicht angezeigt, während Sie tippen).
        *   Warnung: Dies löscht alles im Papierkorb endgültig – verwenden Sie es mit Vorsicht, da es kein Rückgängig gibt.

3.  **Datenträgerberechtigungen mit dem Festplatten-Dienstprogramm reparieren**:
    *   Öffnen Sie das **Festplatten-Dienstprogramm** (über Programme > Dienstprogramme oder Spotlight).
    *   Wählen Sie Ihr Hauptlaufwerk (z. B. Macintosh HD) in der Seitenleiste aus.
    *   Klicken Sie auf **Erste Hilfe** > **Ausführen** (oder **Datenträgerberechtigungen reparieren** in älteren macOS-Versionen).
    *   Lassen Sie den Vorgang abschließen, starten Sie dann Ihren Mac neu und versuchen Sie es erneut.

4.  **Auf externe Laufwerke oder Netzwerkvolumes prüfen**:
    *   Wenn sich die Dateien auf einem externen Laufwerk, einem USB-Stick oder einer Netzwerkfreigabe befinden:
        *   Werfen Sie das Laufwerk aus und schließen Sie es erneut an.
        *   Stellen Sie im Fenster "Informationen" sicher, dass das Kästchen **Eigentümer ignorieren auf diesem Volume** (unter "Freigabe & Berechtigungen") aktiviert ist.
    *   Bei schreibgeschützten Formaten (z. B. NTFS-Laufwerke) benötigen Sie möglicherweise Tools von Drittanbietern wie Paragon NTFS für Schreibzugriff.

5.  **Erweiterte Terminal-Korrekturen (wenn Berechtigungen hartnäckig sind)**:
    *   Um die Berechtigungen für einen bestimmten Ordner/eine bestimmte Datei zurückzusetzen:
        *   Im Terminal: `sudo chmod -R 777 /pfad/zum/ordner` (ersetzen Sie `/pfad/zum/ordner` mit dem tatsächlichen Pfad; ziehen Sie den Ordner ins Terminal, um ihn automatisch einzufügen).
        *   Dies setzt volle Lese-/Schreib-/Ausführungsrechte für alle – verwenden Sie dies sparsam.
    *   Um alle Dateien in einem Verzeichnis zu entsperren: `sudo chflags -R nouchg /pfad/zum/ordner`.
    *   Starten Sie im abgesicherten Modus neu (halten Sie beim Starten die Umschalttaste gedrückt), um Caches zu leeren, und versuchen Sie es dann erneut.

6.  **Weitere Fehlerbehebungsmöglichkeiten**:
    *   **Starten Sie Ihren Mac neu**: Einfach, aber behebt oft vorübergehende Störungen.
    *   **macOS aktualisieren**: Gehen Sie zu Systemeinstellungen > Allgemein > Softwareupdate.
    *   **Auf Malware/Antiviren-Programm-Interferenz prüfen**: Führen Sie einen Scan mit Malwarebytes oder ähnlicher Software durch.
    *   Wenn Dateien aus Downloads oder Apps stammen, stellen Sie sicher, dass sie nicht unter Quarantäne stehen: Im Terminal: `xattr -d com.apple.quarantine /pfad/zur/datei`.
    *   Wenn nichts funktioniert, starten Sie im Wiederherstellungsmodus (Command + R beim Start), führen Sie "Erste Hilfe" auf dem Datenträger aus, oder ziehen Sie in Betracht, die Berechtigungen über das Terminal im Wiederherstellungsmodus zurückzusetzen.

Wenn der Fehler nach diesen Schritten weiterhin besteht, geben Sie weitere Details an, wie Ihre macOS-Version, welchen Vorgang Sie versuchen (z. B. das Löschen bestimmter Dateien) und ob es sich um den Papierkorb oder einen anderen Ort handelt.

### Referenzen
[Apple Support: Berechtigungen für Dateien, Ordner oder Datenträger auf dem Mac ändern](https://support.apple.com/guide/mac-help/change-permissions-for-files-folders-or-disks-mchlp1203/mac)
[So beheben Sie den Fehler "Vorgang kann nicht abgeschlossen werden" auf dem Mac](https://www.macrumors.com/how-to/fix-operation-cant-be-completed-error-mac/)
[Papierkorb leeren, wenn Dateien als "in Verwendung" angezeigt werden](https://apple.stackexchange.com/questions/52257/empty-trash-when-it-says-files-are-in-use)