---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Tutorial für grundlegende Vim-Befehle
translated: true
type: note
---

Vim (kurz für Vi IMproved) ist ein leistungsstarker, modaler Texteditor, der auf vielen Linux-Systemen wie Red Hat der Standard ist. Er ist tastaturgesteuert und effizient, sobald man die Grundlagen gelernt hat. Vim hat drei Hauptmodi: **Normal** (für Navigation und Befehle, Standard), **Insert** (zum Texteingeben) und **Visual** (zum Auswählen von Text). Drücke `Esc`, um von überall zurück in den Normalmodus zu gelangen.

Der beste Weg, um praktisch zu lernen, ist `vimtutor` in deinem Terminal auszuführen – es startet ein interaktives Tutorial.

## 1. Vim öffnen und schließen
- Datei öffnen oder erstellen: `vim dateiname.txt` (z.B. `vim notizen.txt`).
- Ohne Speichern beenden: Im Normalmodus `:q!` eingeben und Enter drücken.
- Vim beenden: Siehe Abschnitt zum Speichern unten.

## 2. Modi
- **Normalmodus**: Standard – für Befehle verwenden. Drücke `Esc`, um ihn zu aktivieren.
- **Insertmodus**: Drücke `i` (vor dem Cursor einfügen) oder `a` (nach dem Cursor anhängen) zum Aktivieren. Du siehst `-- INSERT --` unten.
- **Visualmodus**: Drücke `v`, um Text auszuwählen.
- **Kommandozeilenmodus**: Drücke `:`, um ihn zu aktivieren (für Speichern, Beenden, Suchen).

## 3. Navigation (im Normalmodus)
Verwende diese anstelle der Pfeiltasten für Effizienz:
- `h`: Ein Zeichen nach links
- `j`: Eine Zeile nach unten
- `k`: Eine Zeile nach oben
- `l`: Ein Zeichen nach rechts
- `w`: Vorwärts zum Anfang des nächsten Wortes
- `b`: Rückwärts zum Anfang des vorherigen Wortes
- `0`: Zeilenanfang
- `$`: Zeilenende
- `gg`: Dateianfang
- `G`: Dateiende
- `:n`: Zur Zeile n springen (z.B. `:5`)
- Mit Zahlen präfixieren: `5j` (5 Zeilen nach unten)

Zeilennummern aktivieren: `:set number`

## 4. Text einfügen und bearbeiten
- Insertmodus aktivieren:
  - `i`: Vor dem Cursor einfügen
  - `I`: Am Zeilenanfang einfügen
  - `a`: Nach dem Cursor anhängen
  - `A`: Am Zeilenende anhängen
  - `o`: Neue Zeile darunter (aktiviert Insertmodus)
  - `O`: Neue Zeile darüber (aktiviert Insertmodus)
- Insertmodus verlassen: `Esc`
- Einzelnes Zeichen ersetzen: `r` (dann neues Zeichen tippen)
- Rückgängig: `u`
- Wiederherstellen: `Strg + r`
- Letzten Befehl wiederholen: `.`

## 5. Löschen, Kopieren und Einfügen
- Zeichen löschen: `x`
- Zeile löschen: `dd`
- Bereich löschen: `:3,5d` (Zeilen 3 bis 5)
- Zeile kopieren (yank): `yy`
- Ausgewählten Text kopieren: Im Visualmodus (`v`) mit Pfeiltasten markieren, dann `y`
- Nach Cursor einfügen: `p`
- Vor Cursor einfügen: `P`
- Text auswählen: `v` (zeichenweise), dann Cursor bewegen; `Esc`, um Visual zu verlassen.

## 6. Speichern und Beenden
- Speichern: `:w`
- Speichern und beenden: `:wq` oder `:x` oder `ZZ` (zweimal großes Z)
- Erzwingen, zu speichern und zu beenden: `:wq!`
- Ohne Speichern beenden: `:q!` oder `ZQ`

## 7. Suchen
- Vorwärts suchen: `/muster` (z.B. `/hallo`), dann Enter; `n` für nächstes.
- Rückwärts suchen: `?muster`
- Ersetzen: `:%s/alt/neu/g` (alle "alt" durch "neu" ersetzen)

## Schnelle Tipps
- Hilfe: `:help` oder `:h schlüsselwort`
- Geteilten Bildschirm: `:split dateiname` (horizontal) oder `:vsplit dateiname` (vertikal); `Strg + w w` zum Wechseln.
- Übe in einer Testdatei, um Fehler zu vermeiden.
- Syntaxhervorhebung: `:syntax on`

Dies deckt die Grundlagen ab, um dich schnell zum Bearbeiten von Dateien zu befähigen. Für mehr, erkunde `:help` in Vim oder die folgenden Ressourcen.

[Getting started with Vim: The basics](https://opensource.com/article/19/3/getting-started-vim)  
[Basic Vim Commands](https://www.geeksforgeeks.org/linux-unix/basic-vim-commands/)  
[Vim Cheat Sheet](https://vim.rtorr.com/)