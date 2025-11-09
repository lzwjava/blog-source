---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Datenbankversionskontrolle für Git
translated: true
type: note
---

### Wahl zwischen JSON (oder CSV) und SQLite für git-freundliche Versionskontrolle

Für eine kleine Datenbank mit 1-2 Tabellen und 10k-100k Datensätzen sind sowohl JSON als auch SQLite geeignete Optionen, da die gesamte Dateigröße handhabbar bleiben sollte (wahrscheinlich unter 10-50 MB, selbst bei dichteren Daten). Die Hauptherausforderung, der Sie gegenüberstehen – dass Git Diffs die gesamte Datei bei jedem Update als binären Block behandelt – ist bei Datenbanken üblich. Git ist hervorragend bei textbasierten Diffs, daher glänzen Formate wie JSON hier, während SQLite (eine einzelne Binärdatei) Workarounds für lesbare Änderungen erfordert.

Ich werde es anhand von Vor- und Nachteilen aufschlüsseln und dann eine Empfehlung basierend auf Ihren Prioritäten geben.

#### Schneller Vergleich

| Aspekt              | JSON (oder CSV)                                                                 | SQLite                                                                 |
|---------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------------|
| **Dateiformat**    | Textbasiert (menschenlesbar). Einfache zeilenweise Diffs in Git.                  | Binärdatei. Git zeigt gesamte Dateiänderungen; Diffs sind standardmäßig unlesbar. |
| **Größe für 10k-100k Datensätze** | Klein, wenn die Datensätze einfach sind (z.B. 1-5 KB pro Datensatz → 10-500 MB gesamt). Komprimiert sich gut in Git. | Ähnliche Größe, aber keine Komprimierungsgewinne durch Text-Diffs.                |
| **Git-Erfahrung** | Exzellent: Exakt hinzugefügte/bearbeitete Zeilen sehen. Tools wie `git diff --word-diff` für strukturierte Änderungen nutzen. Daten konsistent sortieren für saubere Diffs. | Schlecht direkt nutzbar. Beheben mit benutzerdefinierter Git-Konfiguration (z.B. DB in SQL dumpen beim Diff). Oder Erweiterungen wie Dolt für git-ähnliche Datenbank-Versionskontrolle nutzen. |
| **Updates**        | Vollständiges Neuschreiben beim Speichern, aber Diffs heben Änderungen hervor, wenn Sie selektiv laden/bearbeiten/speichern (z.B. via Skripte). | Atomare Transaktionen, aber jeder Commit sieht in Git wie ein vollständiger Ersatz aus. |
| **Abfragen/Funktionen** | Basis (Filtern mit Code wie jq/Python). Keine Indizierung/Transaktionen. Gut für flache Daten. | Vollständiges SQL: Abfragen, Joins (für 2 Tabellen), Indizes, Constraints. Besser für jedes "Datenbank"-Gefühl. |
| **Anwendungsfall-Passung**   | Ideal, wenn Ihre App/Skript CRUD im Speicher handhabt und Sie Kollaboration/Diffs priorisieren. | Besser, wenn Sie echte Datenbankoperationen benötigen; Diffs sind sekundär.                   |
| **Benötigte Tools**   | Natives Git + jq (für JSON) oder csvkit (für CSV).                               | sqlite3 CLI + Git-Attribute für benutzerdefinierte Diffs.                         |

#### Empfehlungen
- **Nutzen Sie JSON (oder CSV), wenn einfache Diffs Ihre Top-Priorität sind**: Dies hält alles textbasiert und git-nativ. Für 1-2 Tabellen:
  - Verwenden Sie **eine JSON-Datei** als Array von Objekten (z.B. `[{"id":1, "name":"foo", ...}, ...]`). Es ist flexibel für einfache Beziehungen (eine Tabelle in der anderen einbetten).
  - Oder **CSV-Dateien** (eine pro Tabelle) für strengere tabellarische Daten – extrem leichtgewichtig und diff-freundlich. Tools wie Pandas können sie laden/bearbeiten/exportieren.
  - **Workflow-Tipp**: Sortieren Sie Datensätze immer nach ID/Schlüssel vor dem Speichern (z.B. in Python: `df.sort_values('id').to_csv(...)`). Dies bewirkt, dass Diffs nur echte Änderungen zeigen, kein Rauschen durch Neusortierung. Für Updates: lesen → bestimmte Zeilen modifizieren → sortieren → schreiben. Die Dateigröße bleibt klein und der Git-Verlauf ist sauber.
  - Nachteil: Bei 100k Datensätzen könnte das Laden der gesamten Datei in den Speicher jedes Mal ohne Optimierung langsam sein (z.B. Streaming-Bibliotheken wie ijson verwenden).

- **Verwenden Sie SQLite, wenn Sie Datenbankfunktionalität benötigen**: Es ist robuster für Abfragen/Joins, und das Single-File-Setup ist einfach für Git-Commits. Um das Diff-Problem zu beheben:
  - Fügen Sie eine `.gitattributes`-Datei hinzu: `*.db diff=sqlite` und ein `.gitconfig`-Snippet, um die DB beim Diff in SQL zu dumpen (z.B. via `sqlite3 db .dump`). Dies wandelt binäre Änderungen in lesbare SQL-Inserts/Updates um.
  - Beispiel-Setup-Skript (in bash/Python): Beim Commit Schema/Daten als SQL-Dateien zur Überprüfung exportieren.
  - Für fortgeschrittene Anforderungen ziehen Sie Dolt in Betracht – es ist wie "Git für Datenbanken" mit verzweigbaren Tabellen und richtigen Diffs, aber es ist schwergewichtiger für kleine Setups.

Beginnen Sie der Einfachheit halber mit JSON/CSV – es ist für kleinere Maßstäbe "gut genug" und entspricht Ihrer Git-Anforderung. Wenn Sie hinauswachsen (z.B. komplexe Abfragen benötigen), migrieren Sie später zu SQLite. Prototypisieren Sie beide: Speichern Sie Beispieldaten in Dateien und testen Sie einige Git-Commits.

Wenn Ihre Datensätze eine bestimmte Struktur haben, teilen Sie mehr Details für maßgeschneiderte Code-Snippets mit.

[Versioning SQLite in Git](https://dunkels.com/adam/git-diff-sqlite3/)  
[JSON vs DB for Small Data](https://www.reddit.com/r/flask/comments/lvccgo/using_a_database_such_as_sqlite3_versus_json_to/)  
[Data Version Control Options](https://dolthub.com/blog/2022-04-27-data-version-control/)