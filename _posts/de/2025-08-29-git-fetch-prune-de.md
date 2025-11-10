---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Übersicht zu Git Fetch und Prune
translated: true
type: note
---

### Was ist `git fetch`?
`git fetch` lädt die neuesten Änderungen (Commits, Branches, Tags) aus einem Remote-Repository herunter, ohne sie in Ihren aktuellen Branch zu mergen. Es aktualisiert Ihre lokalen Remote-Tracking-Branches (z.B. `origin/main`), um sie an den Zustand des Remote-Repositorys anzupassen. Dies hält Ihr lokales Repository synchron, verändert aber nicht Ihre Arbeitsdateien oder lokalen Branches.

### Was ist die `--prune`-Option?
Das Flag `--prune` weist Git an, Remote-Tracking-Branches zu entfernen, die im Remote-Repository nicht mehr existieren. Wenn beispielsweise jemand einen Branch auf GitHub löscht, bleibt Ihre lokale Kopie (z.B. `origin/old-branch`) bestehen, es sei denn, Sie führen einen Prune-Vorgang durch.

### Wie funktioniert `git fetch --prune`?
- **Ausführung**: Führen Sie es als `git fetch --prune` aus (oder kurz `git fetch -p`). Es kombiniert Fetch und Prune in einem Befehl.
- **Schritte**:
  1. Git verbindet sich mit dem Remote-Repository und holt Updates, aktualisiert Remote-Tracking-Branches, um neue Commits, hinzugefügte oder gelöschte Branches widerzuspiegeln.
  2. Es sucht nach veralteten Remote-Tracking-Branches (solche ohne ein Gegenstück im Remote-Repository) und löscht diese lokal.
- **Ergebnis**: Ihr lokales Repository bleibt aktuell und sauber. Es findet kein Merging statt – es ist ein schreibgeschützter Synchronisationsvorgang.

### Praktisches Beispiel
Angenommen, Sie haben:
- Lokalen Branch: `main`, der `origin/main` tracked.
- Einen veralteten lokalen Remote-Tracking-Branch: `origin/deleted-feature`.

Durch Ausführen von `git fetch --prune` für `origin`:
- Werden neue Commits geholt.
- Wird `origin/deleted-feature` entfernt (da er im Remote-Repository gelöscht wurde).
- Werden Ihre lokalen Branches nicht verändert.

### Was es bedeutet
Es bedeutet "Hole die neuesten Remote-Daten und räume veraltete Referenzen in Ihrem lokalen Repository auf". Verwenden Sie es regelmäßig, um Verwirrung durch alte Branch-Referenzen zu vermeiden. Es entspricht `git fetch` gefolgt von `git remote prune origin`, aber bequem kombiniert. Aus Sicherheitsgründen betrifft es nur Remote-Tracking-Branches, nicht Ihre eigene Arbeit.