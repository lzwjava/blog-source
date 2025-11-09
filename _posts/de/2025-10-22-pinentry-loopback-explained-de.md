---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GPG Pinentry Loopback-Modus erklärt
translated: true
type: note
---

### Was ist `--pinentry-mode loopback` in GPG?

In GNU Privacy Guard (GPG) steuert die Option `--pinentry-mode loopback`, wie das Tool Passphrase-Abfragen während Verschlüsselungs-, Entschlüsselungs- oder Signiervorgängen behandelt. Pinentry ist der Mechanismus von GPG für die sichere Eingabe von Passphrasen (wie Passwörter für private Schlüssel), typischerweise über einen grafischen Dialog, eine Konsolenabfrage oder andere Schnittstellen.

#### Wichtige Bedeutung und Zweck
- **Loopback-Modus**: Dies setzt das Pinentry auf ein "Loopback"-Verhalten, bei dem GPG kein externes Pinentry-Programm (z.B. ein GUI-Popup) startet. Stattdessen sendet es Abfragen direkt zurück zum aufrufenden Prozess (wie ein Skript oder eine Anwendung). Dies ermöglicht es, die Passphrase programmatisch bereitzustellen, z.B. über Standardeingabe (STDIN), Umgebungsvariablen oder Dateien, ohne interaktive Benutzerabfragen.
  
- **Warum wird es verwendet?**
  - Ideal für **Automatisierung**: In Bash-Skripten, CI/CD-Pipelines (z.B. GitHub Actions) oder headless-Umgebungen (wie SSH-Sitzungen), in denen ein grafischer Dialog nicht erscheinen kann.
  - Vermeidet Hängenbleiben oder Fehlschlagen in nicht-interaktiven Setups.
  - Seit GnuPG 2.1.12 ist Loopback oft standardmäßig mit `--allow-loopback-pinentry` erlaubt, aber die explizite Angabe von `--pinentry-mode loopback` stellt sicher, dass es verwendet wird.

- **Häufiges Anwendungsbeispiel**:
  Um eine Datei in einem Skript zu entschlüsseln und die Passphrase über STDIN bereitzustellen:
  ```
  echo "Ihre-Passphrase" | gpg --pinentry-mode loopback --passphrase-fd 0 --decrypt encrypted-file.gpg > decrypted-file.txt
  ```
  - `--passphrase-fd 0`: Liest die Passphrase vom Dateideskriptor 0 (STDIN).
  - Dies fordert einmalig ab (oder verwendet gecachte Werte, falls konfiguriert) und funktioniert nicht-interaktiv.

#### Mögliche Fallstricke
- **Hinweis zur Sicherheit**: Loopback kann Passphrasen in Prozesslisten oder Logs offenlegen, wenn nicht sorgfältig damit umgegangen wird – verwenden Sie es nur in vertrauenswürdigen Umgebungen.
- **Konfiguration**: Um es global zu aktivieren, fügen Sie `allow-loopback-pinentry` zu `~/.gnupg/gpg-agent.conf` hinzu und laden Sie die Konfiguration mit `gpgconf --reload gpg-agent` neu.
- Wenn es wiederholt zur Eingabe auffordert, überprüfen Sie die Cache-Timeouts in `gpg-agent.conf` (z.B. `default-cache-ttl 3600` für 1 Stunde).

Dieser Modus ist besonders praktisch für Entwickler, die GPG in Tools wie Git-Signing oder Emacs-Workflows integrieren.

#### Referenzen
- [How do I use gpg --pinentry-mode loopback in a bash script?](https://stackoverflow.com/questions/77231645/how-do-i-use-gpg-pinentry-mode-loopback-in-a-bash-script)
- [Agent OPTION (GnuPG Manual)](https://www.gnupg.org/documentation/manuals/gnupg/Agent-OPTION.html)
- [GnuPG - ArchWiki](https://wiki.archlinux.org/title/GnuPG)