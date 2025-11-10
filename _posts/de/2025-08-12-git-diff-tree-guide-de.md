---
audio: false
generated: true
image: false
lang: de
layout: post
title: Leitfaden zu Git Diff-Tree
translated: true
type: note
---

Hier ist eine praktische, umfassende Anleitung zu `git diff-tree` – was es ist, wann man es verwendet und welche Optionen man in der Praxis tatsächlich benötigt. Ich verzichte auf große Tabellen und konzentriere mich auf präzise Erklärungen mit kopierfähigen Beispielen.

# Was `git diff-tree` tatsächlich macht

* Es vergleicht **Tree-Objekte**. Im alltäglichen Gebrauch bedeutet das meist: „Zeige mir, was sich in einem **Commit** im Vergleich zu seinem/seinem Eltern-Commit(s) geändert hat.“
* Es ist **Plumbing** (skriptfreundlich), im Gegensatz zu `git show`/`git log`, die Porcelain (benutzerorientiert) sind.
* Es schaut niemals in Ihr Arbeitsverzeichnis; es vergleicht nur Trees, die im Repo gespeichert sind (Commits, Tags, die auf Commits zeigen, oder rohe Tree-IDs).

# Grundlegende Formen, die Sie verwenden werden

1. Einen Commit mit seinem Eltern-Commit vergleichen

```bash
git diff-tree -p <commit>
```

Wenn `<commit>` einen Eltern-Commit hat, sehen Sie einen normalen Patch. Wenn es ein Merge-Commit ist, sehen Sie standardmäßig nichts, es sei denn, Sie fragen explizit nach Merges (siehe unten).

2. Zwei Trees/Commits explizit vergleichen

```bash
git diff-tree -p <alter-tree-oder-commit> <neuer-tree-oder-commit>
```

Ideal, wenn Sie zwei beliebige Punkte vergleichen möchten, nicht nur „Commit vs. Eltern-Commit“.

3. Nur Dateinamen anzeigen (kein Patch)

```bash
git diff-tree --name-only -r <commit>
```

Fügen Sie `-r` hinzu, um Unterverzeichnisse rekursiv zu durchsuchen, sodass Sie eine flache Liste erhalten.

4. Namen mit Änderungstyp anzeigen

```bash
git diff-tree --name-status -r <commit>
# Gibt Zeilen aus wie:
# A pfad/zu/neuedatei
# M pfad/zu/geaenderte
# D pfad/zu/geloeschte
```

5. Einen Patch anzeigen (vollständiger Diff)

```bash
git diff-tree -p <commit>            # Unified Diff wie `git show`
git diff-tree -U1 -p <commit>        # Weniger Kontext (1 Zeile)
```

# Wichtige Optionen (mit Grund/Einsatzzweck)

* `-r` — Rekursiv in Sub-Trees eintauchen, damit Sie alle verschachtelten Pfade sehen. Ohne diese Option wird ein geändertes Verzeichnis möglicherweise als einzelne Zeile angezeigt.
* `--no-commit-id` — Unterdrückt den „commit <sha>“-Header, wenn Sie die Ausgabe pro Commit für Skripte aufbereiten.
* `--root` — Wenn ein Commit **keinen Eltern-Commit** hat (Initial-Commit), trotzdem seine Änderungen im Vergleich zum leeren Tree anzeigen.
* `-m` — Für Merge-Commits die Diffs **gegen jeden Eltern-Commit** anzeigen (erzeugt mehrere Diffs).
* `-c` / `--cc` — Kombinierter Merge-Diff. `--cc` ist eine verfeinerte Ansicht (was `git show` für Merges verwendet).
* `--name-only` / `--name-status` / `--stat` / `--numstat` — Verschiedene Zusammenfassungsstile. `--numstat` ist skriptfreundlich (Anzahl der hinzugefügten/entfernten Zeilen).
* `--diff-filter=<set>` — Nach Änderungstypen filtern, z.B. `--diff-filter=AM` (nur Hinzugefügt oder Geändert); gebräuchliche Buchstaben: `A`dd (Hinzugefügt), `M`odified (Geändert), `D`eleted (Gelöscht), `R`enamed (Umbenannt), `C`opied (Kopiert), `T`ype changed (Typ geändert).
* `-M` / `-C` — Umbenennungen und Kopien erkennen. Ein optionaler Ähnlichkeitsschwellenwert kann angegeben werden, z.B. `-M90%`.
* `--relative[=<pfad>]` — Die Ausgabe auf ein Unterverzeichnis beschränken; ohne Argument wird das aktuelle Arbeitsverzeichnis verwendet.
* `-z` — Pfade **NUL-terminieren** für eine eindeutige maschinelle Verarbeitung (verarbeitet Zeilenumbrüche oder Tabs in Dateinamen).
* `--stdin` — Eine Liste von Commits (oder Paaren) von der Standardeingabe lesen. Dies ist das Erfolgsgeheimnis für schnelle Stapelverarbeitungen.

# Kanonische Skriptmuster

### 1) Geänderte Dateien für einen einzelnen Commit auflisten

```bash
git diff-tree --no-commit-id --name-status -r <commit>
```

### 2) Stapelverarbeitung für viele Commits (schnell!)

```bash
git rev-list main --since="2025-08-01" |
  git diff-tree --stdin -r --no-commit-id --name-status
```

`--stdin` vermeidet das separate Starten von `git` pro Commit und ist für große Bereiche viel schneller.

### 3) Nur Hinzufügungen und Änderungen in einem Verzeichnis

```bash
git diff-tree -r --no-commit-id --name-status \
  --diff-filter=AM <commit> -- src/backend/
```

### 4) Geänderte Zeilen pro Datei zählen (skriptfreundlich)

```bash
git diff-tree -r --no-commit-id --numstat <commit>
# Gibt aus: "<hinzugefügt>\t<entfernt>\t<pfad>"
```

### 5) Umbenennungen in einem Commit erkennen und anzeigen

```bash
git diff-tree -r --no-commit-id -M --name-status <commit>
# Zeilen wie: "R100 alter/name.txt\tneuer/name.txt"
```

### 6) Patch für einen Merge-Commit

```bash
git diff-tree -m -p <merge-commit>     # Patches pro Eltern-Commit
git diff-tree --cc <merge-commit>      # Kombinierte Ansicht (einzelner Patch)
```

### 7) Initialer Commit (kein Eltern-Commit)

```bash
git diff-tree --root -p <initial-commit>
```

# Das Rohdatenformat verstehen (falls Sie von Hand parsen)

Verwenden Sie `--raw` (wird implizit von einigen Modi verwendet), um minimale, stabile Datensätze zu erhalten:

```
:100644 100644 <oldsha> <newsha> M<TAB>pfad
```

* Zahlen sind Dateimodi: `100644` reguläre Datei, `100755` ausführbar, `120000` Symlink, `160000` Gitlink (Submodul).
* Status ist ein einzelner Buchstabe (`A`, `M`, `D`, etc.), möglicherweise mit einer Bewertung (z.B. `R100`).
* Für Umbenennungen/Kopien sehen Sie zwei Pfade. Mit `-z` sind die Felder NUL-getrennt; ohne `-z` sind sie Tabulator-getrennt.

**Tipp:** Wenn Sie zuverlässige Tools erstellen, verwenden Sie immer `-z` und trennen Sie an NUL-Zeichen. Dateinamen mit Zeilenumbrüchen existieren.

# `git diff-tree` mit verwandten Befehlen vergleichen (damit Sie den richtigen wählen)

* `git diff`: vergleicht **Index/Arbeitsverzeichnis** mit HEAD oder zwei beliebige Commits/Trees; für die interaktive Entwicklung.
* `git show <commit>`: eine übersichtliche Hülle für „Diff vs. Eltern-Commit + Metadaten“. Ideal für Menschen.
* `git log -p`: Verlauf plus Patches. Für Bereiche ist es oft bequemer als manuelles `diff-tree`-Looping.
* `git diff-tree`: Plumbing für **präzise, skriptbare Diffs pro Commit**, stapelbar mit `--stdin`.

# Beispiele aus der Praxis

### „Was hat sich in diesem PR-Merge-Commit geändert?“

```bash
git diff-tree --cc <merge-commit> | less
```

Wenn Sie detailierte Informationen pro Eltern-Commit benötigen:

```bash
git diff-tree -m -p <merge-commit> | less
```

### „Eine saubere Liste der Dateien, die vom letzten Commit geändert wurden, für einen CI-Schritt bereitstellen“

```bash
git diff-tree --no-commit-id --name-only -r HEAD > changed.txt
```

### „Nur Java-Dateien, die in den letzten 20 Commits hinzugefügt oder geändert wurden“

```bash
git rev-list -n 20 HEAD |
  git diff-tree --stdin -r --no-commit-id --name-only --diff-filter=AM |
  grep -E '\.java$'
```

### „Zusammenfassung der Änderungen (hinzugefügte/entfernte Zeilen) für ein Release-Tag“

```bash
git diff-tree -r --no-commit-id --numstat v1.2.0..v1.3.0
```

### „Sichere Verarbeitung von Dateinamen mit Sonderzeichen“

```bash
git diff-tree -z -r --no-commit-id --name-status <commit> |
  awk -v RS='\0' 'NR%2{status=$0; next}{printf "%s %s\n", status, $0}'
```

# Leistungshinweise

* Bevorzugen Sie `--stdin` mit `git rev-list` für große Bereiche; es vermeidet Prozess-Overhead.
* Überspringen Sie Patches (`--name-only`/`--name-status`), wenn Sie keine Zeilenänderungen benötigen.
* Vermeiden Sie die Erkennung von Umbenennungen (`-M`, `-C`), wenn Ihnen Geschwindigkeit über Genauigkeit geht.

# Fallstricke & Grenzfälle

* **Keine Ausgabe für Merges standardmäßig.** Sie müssen `-m` (pro Eltern-Commit) oder `--cc`/`-c` (kombiniert) übergeben.
* **Initialer Commit ist „leerer Tree vs. Tree“. Verwenden Sie `--root`, um einen Diff zu erzwingen.
* **Submodule** zeigen den Modus `160000` und eine SHA (Gitlink) an. Sie sehen keine inneren Diffs, es sei denn, Sie diffen innerhalb des Submodule-Repos.
* **Pathspecs stehen nach `--`.** Wenn Sie nach Pfaden filtern, stellen Sie sie nach `--`, um Mehrdeutigkeiten zu vermeiden.
* **Dateinamen mit Leerzeichen/Zeilenvorschüben.** Fügen Sie immer `-z` hinzu, wenn Sie parsen.

# Schnelle „Cheat-Snippets“, die Sie tatsächlich wiederverwenden werden

```bash
# Geänderte Dateien (flache Liste)
git diff-tree --no-commit-id --name-only -r <commit>
```