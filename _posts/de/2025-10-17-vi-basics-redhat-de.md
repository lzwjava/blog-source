---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Grundlagen des Vi-Editors für Red Hat Linux
translated: true
type: note
---

Vi ist ein leistungsstarker, tastaturgesteuerter Texteditor, der auf Linux-Systemen, einschließlich Red Hat Enterprise Linux (RHEL), Standard ist. Er ist leichtgewichtig und effizient für das Bearbeiten von Konfigurationsdateien, Skripten und mehr. Unter Red Hat verweist der `vi`-Befehl typischerweise auf `vim` (Vi IMproved), welches Funktionen wie Syntax-Hervorhebung hinzufügt. Dieser Leitfaden behandelt die Grundlagen für Anfänger.

## Installation
Vi ist auf den meisten Red Hat-Systemen vorinstalliert. Falls Sie das vollständige `vim`-Paket benötigen (oder es fehlt), installieren Sie es über den Paketmanager:

- Für RHEL 7/8:
  ```
  sudo yum install vim
  ```

- Für RHEL 9+:
  ```
  sudo dnf install vim
  ```

Nach der Installation können Sie `vi` oder `vim` synonym verwenden.

## Vi starten
1. Öffnen Sie ein Terminal.
2. Führen Sie `vi dateiname.txt` aus (ersetzen Sie `dateiname.txt` mit Ihrem Dateipfad).
   - Wenn die Datei existiert, wird sie zur Bearbeitung geöffnet.
   - Wenn nicht, wird eine neue, leere Datei erstellt.
3. Um ohne Datei zu öffnen (zum Üben): `vi`.
Vi startet im **Befehlsmodus** (dem Standardmodus). Sie sehen einen leeren Bildschirm oder Dateiinhalt mit einem Cursor oben links.

## Modi verstehen
Vi hat drei Hauptmodi – das Wechseln zwischen ihnen ist der Schlüssel:
- **Befehlsmodus**: Standardmodus für Navigation, Löschen und die meisten Aktionen. Drücken Sie `Esc`, um von anderen Modi hierher zu gelangen oder zurückzukehren.
- **Einfügemodus**: Zum Tippen/Bearbeiten von Text. Wechseln Sie vom Befehlsmodus aus (z.B. durch Drücken von `i`).
- **Ex-Modus**: Für erweiterte Befehle wie Speichern. Wechseln Sie durch Eingabe von `:` im Befehlsmodus.

Befehle sind case-sensitiv. Sie können Befehle mit Zahlen wiederholen (z.B. löscht `3dd` 3 Zeilen).

## Grundlegende Navigation (im Befehlsmodus)
Verwenden Sie die Tasten der Grundreihe für die Cursorbewegung – keine Maus nötig:
- `h`: Ein Zeichen nach links
- `j`: Eine Zeile nach unten
- `k`: Eine Zeile nach oben
- `l`: Ein Zeichen nach rechts
- `w`: Ein Wort vorwärts
- `b`: Ein Wort rückwärts
- `0` (Null): Zeilenanfang
- `$`: Zeilenende
- `gg`: Dateianfang
- `G`: Dateiende
- `Strg + F`: Eine Seite nach unten
- `Strg + B`: Eine Seite nach oben

## Einfügemodus betreten und Bearbeiten
Drücken Sie im Befehlsmodus eine dieser Tasten, um in den Einfügemodus zu wechseln und mit dem Tippen zu beginnen:
- `i`: Vor dem Cursor einfügen
- `I`: Am Zeilenanfang einfügen
- `a`: Nach dem Cursor anhängen
- `A`: Am Zeilenende anhängen
- `o`: Neue Zeile unterhalb
- `O`: Neue Zeile oberhalb

Um den Einfügemodus zu verlassen: Drücken Sie `Esc` (zurück zum Befehlsmodus).

Häufige Bearbeitungsbefehle (im Befehlsmodus):
- **Löschen**:
  - `x`: Zeichen unter dem Cursor löschen
  - `X`: Zeichen vor dem Cursor löschen
  - `dd`: Aktuelle Zeile löschen
  - `dw`: Aktuelles Wort löschen
  - `D`: Bis zum Zeilenende löschen
- **Kopieren (Yank)**:
  - `yy`: Aktuelle Zeile kopieren
  - `y`: Auswahl kopieren (nach `v` zum Auswählen)
- **Einfügen**:
  - `p`: Nach dem Cursor einfügen
  - `P`: Vor dem Cursor einfügen
- **Rückgängig**:
  - `u`: Letzte Änderung rückgängig machen
  - `U`: Alle Änderungen an der aktuellen Zeile rückgängig machen
- **Wiederholen**: `.` (wiederholt den letzten Befehl)

## Speichern und Beenden
Dies sind **Ex-Befehle** – geben Sie `:` im Befehlsmodus ein, dann den Befehl und drücken Sie `Enter`:
- `:w`: Änderungen speichern (write)
- `:q`: Beenden (quit), wenn keine Änderungen vorliegen
- `:wq` oder `ZZ` (im Befehlsmodus): Speichern und beenden
- `:q!`: Beenden ohne zu speichern (Änderungen verwerfen, erzwingen)
- `:w dateiname`: Als neue Datei speichern

Wenn Sie feststecken, bringt Sie `:q!` sicher heraus.

## Suchen und Ersetzen
- Vorwärts suchen: `/muster` (z.B. `/error`), dann `n` für den nächsten Treffer, `N` für den vorherigen.
- Rückwärts suchen: `?muster`.
- Alle ersetzen: `:%s/alt/neu/g` (global ersetzen; fügen Sie `c` für Bestätigung hinzu, z.B. `:%s/alt/neu/gc`).

## Tipps für Red Hat Benutzer
- Anpassungen in `~/.vimrc` vornehmen (falls nicht vorhanden, erstellen):
  ```
  set number          # Zeilennummern anzeigen
  syntax on           # Syntax-Hervorhebung
  set tabstop=4       # Tab-Breite
  set autoindent      # Automatischer Einzug
  ```
  Bearbeiten mit `vi ~/.vimrc`, Zeilen hinzufügen, dann `:wq`.
- Für mehrere Dateien: `vi datei1.txt datei2.txt`, wechseln mit `:n` (next) oder `:prev` (previous).
- Üben Sie in einer Testdatei, um Fehler in Systemdateien zu vermeiden.

Vi erfordert Übung, wird aber intuitiv. Fangen Sie einfach an und verwenden Sie `Esc` häufig!

## Referenzen
[How to get started with the Vi editor - Red Hat](https://www.redhat.com/en/blog/get-started-vi-editor)
[LFCS #2: How to Install and Use Vi/Vim as a Full Text Editor in Linux](https://www.tecmint.com/vi-editor-usage/)
[vi Editor in Linux - GeeksforGeeks](https://www.geeksforgeeks.org/linux-unix/vi-editor-unix/)