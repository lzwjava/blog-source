---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GnuPG-Benutzerverzeichnisinhalte erklärt
translated: true
type: note
---

Diese Dateien und Verzeichnisse sind Teil Ihres GnuPG (GPG)-Heimatverzeichnisses (`~/.gnupg/`), das kryptografische Schlüssel und zugehörige Daten für Verschlüsselung, Signierung und Authentifizierung speichert. GPG ist ein Tool für sichere Kommunikation und Datenschutz. Hier ist eine Aufschlüsselung basierend auf dem Standardverhalten von GnuPG 2.1+:

- **openpgp-revocs.d**: Ein Verzeichnis, das Widerrufszertifikate (`.rev`-Dateien) enthält, die bei der Erstellung von Schlüsselpaaren generiert werden. Diese werden verwendet, um Ihre Schlüssel zu widerrufen (ungültig zu machen), falls sie kompromittiert wurden oder nicht mehr benötigt werden, um eine weitere Nutzung zu verhindern.

- **private-keys-v1.d**: Ein Verzeichnis, das Ihre privaten (geheimen) Schlüssel im modernen Schlüsselformat speichert, das in GnuPG 2.1 eingeführt wurde. Jeder Schlüssel befindet sich in seiner eigenen Datei für mehr Sicherheit und besseres Management. Schützen Sie dieses Verzeichnis hochgradig – es ist wie Ihr digitales Tresor.

- **pubring.kbx**: Die öffentliche Keyring-Datei im neuen "Keybox"-Format (`.kbx`). Sie enthält die von Ihnen importierten öffentlichen Schlüssel anderer Personen, die Sie verwenden, um Nachrichten an diese zu verschlüsseln oder deren Signaturen zu verifizieren.

- **pubring.kbx~**: Eine Sicherungskopie von `pubring.kbx`, die automatisch von GPG während Bearbeitungen oder Updates erstellt wird. Die Tilde (`~`)-Endung ist eine gängige Linux-Konvention für Sicherungen.

- **trustdb.gpg**: Die Trust-Datenbank-Datei, die die von Ihnen festgelegten Vertrauensstufen für öffentliche Schlüssel verfolgt (z.B. "ultimate" für Ihre eigenen Schlüssel oder Stufen für andere basierend auf Signaturen). Sie hilft GPG dabei, zu entscheiden, ob ein Schlüssel für die Validierung zuverlässig ist.

Wenn Sie kürzlich Schlüssel generiert oder importiert haben, ist dieser Aufbau normal. Sichern Sie Ihr gesamtes `~/.gnupg/`-Verzeichnis immer sicher und teilen Sie niemals private Schlüssel. Weitere Details finden Sie in der offiziellen GnuPG-Dokumentation.

[Using the GNU Privacy Guard](https://www.gnupg.org/documentation/manuals/gnupg.pdf)
[GnuPG Part 2 - Create and Manage Keys](https://www.hacksanity.com/kb/gnupg-create-manage-keys/)
[How to Back Up and Restore Your GPG Keys on Linux](https://www.howtogeek.com/816878/how-to-back-up-and-restore-gpg-keys-on-linux/)
[GPG(1) Manual](https://www.gnupg.org/(en)/documentation/manuals/gnupg24/gpg.1.html)