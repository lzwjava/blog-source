---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Red Hat Enterprise Linux Standard-Texteditor
translated: true
type: note
---

### Standard-Texteditor in Red Hat Enterprise Linux

In Red Hat Enterprise Linux (RHEL) ist der standardmäßige Texteditor **Vi** (häufig als Alias für **Vim**, was für "Vi IMproved" steht, eingerichtet). Vi ist ein modaler, kommandozeilenbasierter Texteditor, der seit den 1970er Jahren der Standard auf Unix-ähnlichen Systemen ist. Er ist leichtgewichtig, allgegenwärtig und auf den meisten RHEL-Systemen standardmäßig über das Paket `vim-minimal` oder `vim-enhanced` vorinstalliert.

#### Warum Vi/Vim?
- Er ist effizient in Serverumgebungen, in denen GUI-Editoren nicht praktikabel sind.
- Die Befehle sind tastaturbasiert: Einfügemodus zum Tippen (`i`) und Befehlsmodus zum Bearbeiten (z.B. `dd` zum Löschen einer Zeile, `:wq` zum Speichern und Beenden).
- Für Neulinge ist die Bedienung zunächst gewöhnungsbedürftig, aber sehr leistungsstark, sobald man sie beherrscht.

#### Überprüfung und Verwendung
- Führen Sie `vi dateiname.txt` (oder `vim dateiname.txt`) aus, um eine Datei zu öffnen.
- Um Ihren aktuellen Standardeditor zu überprüfen: `echo $EDITOR` (gibt in der Regel `/usr/bin/vi` aus).
- Wenn Sie etwas anderes bevorzugen (wie z.B. Emacs aus Ihrer vorherigen Anfrage), setzen Sie es mit `export EDITOR=emacs` in Ihrer `~/.bashrc`-Datei.

Für einen schnellen Einstieg geben Sie `vimtutor` ein, um ein interaktives Tutorial zu starten.

[How to get started with the Vi editor - Red Hat](https://www.redhat.com/en/blog/get-started-vi-editor)  
[Linux skills: 9 tutorials to get more from your text editor - Red Hat](https://www.redhat.com/en/blog/text-editor-roundup-2022)