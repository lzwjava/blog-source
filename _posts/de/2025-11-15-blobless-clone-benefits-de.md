---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Vorteile eines bloblosen Git-Klons
translated: true
type: note
---

Der Git-Befehl:

```bash
git clone --filter=blob:none <repository-url>
```

ist ein **partieller Clone**, der **so gut wie keine Dateiinhalte** (Blobs) zum Zeitpunkt des Checkouts herunterlädt. Hier ist eine genaue Erläuterung, was er tut und warum er nützlich ist:

### Was `--filter=blob:none` bedeutet
- `--filter=blob:none` weist Git an, **blobless cloning** zu verwenden.
- Git lädt weiterhin herunter:
  - Alle Commits (Verlauf)
  - Alle Tree-Objekte (Verzeichnisstruktur)
  - Alle Refs/Branches/Tags
- Es werden jedoch **keine Dateiinhalte** (Blobs) während des initialen Clones heruntergeladen.
- Wenn Sie später `git checkout` ausführen oder Branches wechseln, lädt Git nur die Blobs (Dateiinhalte) für die Dateien herunter, die tatsächlich in Ihrem Working Tree zu diesem Zeitpunkt benötigt werden.

### Wichtige Vorteile
- Extrem schneller und kleiner initialer Clone (oft nur wenige MB, selbst bei riesigen Repositories wie dem Linux-Kernel, Android oder Windows-Quellcode).
- Verwendet zunächst viel weniger Netzwerkbandbreite und Festplattenspeicher.
- Perfekt für CI/CD, schnelle Nachschlagearbeiten oder wenn Sie nur den Verlauf benötigen (z.B. `git log`, Blame, Diff über Commits hinweg), ohne Dateien auszuchecken.

### Beispielhafter Größenvergleich (aus der Praxis)

| Repository       | Normaler Clone | `blob:none` Clone | Geschwindigkeitsgewinn |
|------------------|----------------|-------------------|------------------------|
| torvalds/linux   | ~5+ GB         | ~300–400 MB       | 10–20× schneller       |
| microsoft/vscode | ~2–3 GB        | ~200 MB           | viel schneller         |

### Häufige Folge-Befehle nach einem blob:none Clone
```bash
# Erstmalig, wenn Sie einen Working Tree benötigen:
git checkout <branch>        # lädt nur benötigte Blobs herunter

# Oder wenn Sie später alles haben möchten:
git fetch --unshallow        # für blobless nicht erforderlich
# Um fehlende Blobs dauerhaft nachzuladen:
git repack -a -d             # optional, erzwingt das Herunterladen aller Blobs
```

### Verwandte Filter, die Sie sehen könnten
- `--filter=blob:none` → zunächst überhaupt keine Blobs (am aggressivsten)
- `--filter=tree:0`    → lädt Trees, aber keine Blobs herunter (ähnliche Wirkung)
- `--filter=sparse:oid=<oid>` → für sparse-checkout mit partiellen Blobs

### Zusammenfassung
```bash
git clone --filter=blob:none https://github.com/example/repo.git
```
= "Gib mir sofort den vollständigen Verlauf und die Struktur, aber lade die Dateiinhalte später bei Bedarf herunter."  
Großartig für riesige Monorepos oder wenn Sie einfach nur den Verlauf durchsuchen möchten, ohne stundenlang zu warten.