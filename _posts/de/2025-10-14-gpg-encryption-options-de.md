---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GPG-Verschlüsselungsoptionen erklärt
translated: true
type: note
---

### Erklärung der GPG-Optionen

Der `gpg`-Befehl (GNU Privacy Guard) ist ein Tool für Verschlüsselung, Entschlüsselung und Schlüsselverwaltung. Die von Ihnen genannten Optionen werden häufig gemeinsam verwendet, um Dateien für einen bestimmten Empfänger zu verschlüsseln. Hier ist die Bedeutung jeder Option:

-   **`--homedir <Verzeichnis>`**: Gibt das GnuPG-Heimverzeichnis an (Standard ist `~/.gnupg`). Hier speichert GPG Schlüsselbund-Dateien, Konfigurationsdateien und andere Daten. Diese Option überschreibt die `GNUPGHOME`-Umgebungsvariable und ist nützlich, um GPG-Operationen auf einen benutzerdefinierten Ort zu isolieren (z. B. für mehrere Profile oder aus Sicherheitsgründen). Sie muss in der Befehlszeile angegeben werden.

-   **`-e` (oder `--encrypt`)**: Verschlüsselt die Eingabedaten mit Public-Key-Kryptografie. Dies ist der primäre Modus für asymmetrische Verschlüsselung, bei der die Daten mit dem öffentlichen Schlüssel des Empfängers verschlüsselt werden. Er kann mit anderen Optionen wie Signieren kombiniert werden.

-   **`-r <User-ID>` (oder `--recipient <User-ID>`)**: Gibt den/die Empfänger für die Verschlüsselung an. Die `<User-ID>` kann eine Schlüssel-ID, eine E-Mail-Adresse oder ein Name sein, der mit dem öffentlichen Schlüssel verknüpft ist. GPG verwendet den entsprechenden öffentlichen Schlüssel, um die Daten zu verschlüsseln. Mehrere Empfänger können für Gruppenverschlüsselung angegeben werden.

#### Beispielhafte Verwendung

Ein gängiger Befehl, der diese Optionen kombiniert, könnte so aussehen:
```
gpg --homedir /pfad/zu/benutzerdef/verz -e -r recipient@example.com inputfile.txt
```
Dies verschlüsselt `inputfile.txt` für `recipient@example.com` unter Verwendung der Schlüssel aus `/pfad/zu/benutzerdef/verz` und erzeugt `inputfile.txt.gpg`.

Weitere Details finden Sie, indem Sie `gpg --help` ausführen oder die Manpage konsultieren.

[ArchWiki: GnuPG](https://wiki.archlinux.org/title/GnuPG)
[GPG Cheat Sheet](https://irtfweb.ifa.hawaii.edu/~lockhart/gpg/)
[GPG Command in Linux](https://www.tutorialspoint.com/unix_commands/gpg.htm)