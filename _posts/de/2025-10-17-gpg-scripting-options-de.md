---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GPG-Befehlsoptionen für Skripte
translated: true
type: note
---

### Erklärung der GPG-Befehlsoptionen

Die Optionen `--batch`, `--yes`, `-o` und `--pinentry-mode` sind gängige Flags, die mit dem `gpg`-Befehl (GNU Privacy Guard) für nicht-interaktive oder automatisierte Operationen verwendet werden, wie z.B. Verschlüsselung, Entschlüsselung oder Signierung. Hier eine Aufschlüsselung:

- **`--batch`**: Aktiviert den Batch-Modus, der verhindert, dass `gpg` interaktive Fragen stellt oder interaktive Befehle zulässt. Dies ist nützlich für Skripte oder Automatisierung, bei denen keine Benutzereingabe möglich ist. Es kann mit `--no-batch` deaktiviert werden.

- **`--yes`**: Nimmt automatisch "Ja" als Antwort auf die meisten Bestätigungsaufforderungen an (z.B. das Überschreiben von Dateien). Dies vermeidet Unterbrechungen aufgrund von Ja/Nein-Fragen.

- **`-o` (oder `--output`)**: Spezifiziert die Ausgabedatei für die Operation. Es muss ein Dateiname folgen, z.B. `-o output.txt`. Ohne diese Option geht die Ausgabe möglicherweise an stdout oder einen Standardort.

- **`--pinentry-mode`**: Steuert, wie die PIN-Eingabe (Passwortabfrage) vom GPG-Agenten behandelt wird. Es erfordert einen Moduswert wie `ask` (Standard: öffnet eine grafische oder Konsolenabfrage), `loopback` (erlaubt Passworteingabe via stdin für Skripte, ohne Popup), `cancel` (bricht Operationen ab, die eine PIN benötigen) oder `error` (gibt einen Fehler zurück, anstatt eine Abfrage zu starten). Dies wird oft mit `loopback` in Batch-Skripten für sichere, nicht-interaktive Passworteingabe verwendet.

Diese Optionen werden häufig in Skripten kombiniert, z.B. `gpg --batch --yes -o decrypted.txt --pinentry-mode loopback --decrypt encrypted.gpg`, um vollständig automatisiert zu laufen.

#### Referenzen
- [GPG Man Page](https://linux.die.net/man/1/gpg)
- [GnuPG Agent Options](https://www.gnupg.org/documentation/manuals/gnupg/Agent-Options.html)
- [GnuPG Manual](https://www.gnupg.org/documentation/manuals/gnupg/index.html)