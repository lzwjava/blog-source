---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Optimierung der Git-Garbage-Collection erklärt
translated: true
type: note
---

### Was Git GC macht
Git GC (Garbage Collection) ist ein Wartungsbefehl, der Ihr Git-Repository optimiert, indem er unnötige Dateien bereinigt und Daten komprimiert, um Speicherplatz zu sparen und die Leistung zu verbessern. Es arbeitet im `.git`-Verzeichnis, das den gesamten Verlauf, alle Objekte und Metadaten für ein Repo speichert.

Wichtige Aktionen, die es durchführt:
- **Entfernen unerreichbarer Objekte**: Entfernt Commits, Trees und Blobs, auf die nicht mehr verwiesen wird (z. B. nach einem Rebase oder dem Löschen von Branches). Diese werden zu "loose objects" in `.git/objects`, und GC räumt sie auf.
- **Neuverpacken von Objekten**: Komprimiert loose objects (einzeln gespeichert) in Pack-Dateien (`.git/objects/pack`), die effizienter sind. Dabei wird Delta-Kompression verwendet, um Unterschiede zwischen ähnlichen Dateien zu speichern, was den Plattenverbrauch reduziert.
- **Aktualisieren von Referenzen**: Aktualisiert den internen Zustand des Repositorys, z. B. durch das Neuschreiben des Pack-Index für schnellere Lookups.
- **Ausführen verwandter Tools**: Es ruft oft Befehle wie `git prune`, `git repack` und `git rerere` (für Wiederverwendungsauflösung) als Teil des Prozesses auf.

Beleg: Laut der offiziellen Git-Dokumentation (z. B. `git gc --help`) ist GC dafür konzipiert, Repositorys "hauszuhalten". Ein Repository mit 10.000 loose objects könnte beispielsweise von mehreren hundert MB auf einen Bruchteil schrumpfen, sobald es gepackt wird, da die Delta-Kompression Ähnlichkeiten (z. B. zwischen Dateiversionen in einer Code-Historie) ausnutzt.

### Wie es intern funktioniert
1. **Auslöser**: GC läuft manuell via `git gc` oder automatisch, wenn Git bestimmte Bedingungen erkennt (siehe unten). Es läuft nicht bei jedem Befehl, um Verlangsamungen zu vermeiden.
2. **Prozess**:
   - Zählt loose objects und Pack-Dateien.
   - Wenn Schwellenwerte überschritten werden (standardmäßig z. B. >6.700 loose objects, konfigurierbar via `gc.auto`), packt es aggressiv neu.
   - Es erstellt temporäre Dateien (z. B. `.git/objects/tmp_*`), um Datenverlust zu vermeiden, und tauscht sie dann atomar aus.
   - Mildere Modi wie `git gc --auto` entfernen nur Objekte ohne vollständiges Neuverpacken.
3. **Kompressionsdetails**: Verwendet zlib zur Kompression. Beim Neuverpacken werden Pack-Dateien erstellt, in denen Objekte als Deltas (Unterschiede) von Basisobjekten gespeichert werden, was es effizient für Repositorys mit sich entwickelndem Code macht – z. B. erzeugt das Hinzufügen einer Zeile zu einer Datei in einer großen Codebase ein kleines Delta, anstatt die gesamte Datei zu duplizieren.

Dies wird durch den Git-Quellcode (verfügbar auf GitHub) gestützt, der GC als eine Reihe von Shell-Aufrufen an Bereinigungs- und Pack-Utilities für Zuverlässigkeit implementiert.

### Warum es plötzlich läuft
GC löst oft "plötzlich" aus, weil es automatisch und nicht in Echtzeit abläuft, um die Leistung im Gleichgewicht zu halten. Häufige Gründe:
- **Schwellenwerte erreicht**: Nach dem Anhäufen von loose objects (z. B. durch häufige Commits oder Fetches ohne Packen). Git prüft dies nach Operationen wie `git commit`, `git merge` oder `push`. Wenn loose objects den `gc.auto`-Grenzwert (Standard: ca. 6.700) überschreiten, läuft es. Deshalb kann es nach einer Phase hoher Aktivität passieren und "plötzlich" erscheinen.
- **Bereinigungszeitplan**: Wenn `gc.prune` gesetzt ist, bereinigt es periodisch veraltete Referenzen, aber die Haupt-Auto-GC basiert auf Objektanzahlen.
- **Große Operationen**: Umfangreiche Rebasing- oder Cloning-Vorgänge können schnell viele loose objects erzeugen und es auslösen.
- **Post-Command-Hooks**: Einige Workflows oder Tools (z. B. Git-Hooks oder IDEs) könnten `git gc` nach großen Änderungen aufrufen.

Um es zu steuern: Passen Sie Einstellungen wie `git config --global gc.auto 0` an, um Auto-GC zu deaktivieren, wenn Sie manuelle Läufe bevorzugen, oder erhöhen Sie den Schwellenwert, um Unterbrechungen zu reduzieren. Das Ausführen verhindert, dass Repositorys ausufern – z. B. verwendet das Linux-Kernel-Repo GC, um die Historie trotz seines massiven Umfangs handhabbar zu halten. Falls Probleme bestehen bleiben, prüfen Sie `git count-objects -v` für Statistiken zu loose objects.