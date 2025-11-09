---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Verschlüsseln von Dateien mit GPG
translated: true
type: note
---

### Verschlüsseln einer Datei mit Ihrem GPG-Schlüssel

Ihre GPG-Schlüssel-Liste zeigt einen öffentlichen Schlüssel (pub) mit dem Fingerabdruck `982740390B5D33E90B6B6133892BC5A4789B71CD`, der Ihrer E-Mail `lzwjava@gmail.com` zugeordnet ist. Um eine Datei mit diesem Schlüssel zu verschlüsseln (so dass nur Sie sie mit Ihrem privaten Schlüssel entschlüsseln können), führen Sie diese Schritte in Ihrem Terminal aus:

1. **Navigieren Sie in das Verzeichnis**, das die zu verschlüsselnde Datei enthält (z. B. wenn Ihre Datei `secret.txt` heißt):
   ```
   cd ~/pfad/zur/datei
   ```

2. **Verschlüsseln Sie die Datei** mit der Option `--encrypt` und geben Sie den Empfänger an (Ihre E-Mail oder die Schlüssel-ID). Dies erstellt eine verschlüsselte `.gpg`-Datei.
   
   - Verwenden Sie Ihre E-Mail (einfacher):
     ```
     gpg --encrypt --recipient lzwjava@gmail.com secret.txt
     ```
   
   - Verwenden Sie die Schlüssel-ID (vollständiger Fingerabdruck):
     ```
     gpg --encrypt --recipient 982740390B5D33E90B6B6133892BC5A4789B71CD secret.txt
     ```
   
   Dies erzeugt `secret.txt.gpg`, die verschlüsselte Version. Die ursprüngliche Datei `secret.txt` bleibt unverändert.

3. **Überprüfen Sie die Verschlüsselung** (optional):
   ```
   gpg --list-packets secret.txt.gpg
   ```
   Dies zeigt Details über das verschlüsselte Paket an.

### Entschlüsseln der Datei (als spätere Referenz)

Um sie wieder zu entschlüsseln (nur möglich mit Ihrem privaten Schlüssel und Ihrer Passphrase):
```
gpg --decrypt secret.txt.gpg > secret.txt.decrypted
```
Geben Sie Ihre Passphrase ein, wenn Sie dazu aufgefordert werden.

### Tipps
- **Symmetrische Verschlüsselung** (wenn Sie keinen Empfängerschlüssel benötigen, nur eine Passphrase): Verwenden Sie stattdessen `gpg -c secret.txt`.
- **Verschlüsseln und signieren** (um zu beweisen, dass sie von Ihnen stammt): Fügen Sie `--sign` zum Verschlüsselungsbefehl hinzu, z. B. `gpg --encrypt --sign --recipient lzwjava@gmail.com secret.txt`.
- Wenn Sie Fehler erhalten (z. B. Schlüssel nicht vertrauenswürdig), führen Sie `gpg --edit-key lzwjava@gmail.com` aus und verwenden Sie `trust`, um ihn auf "ultimate" zu setzen.
- Sichern Sie immer Ihr `~/.gnupg`-Verzeichnis, um Ihre Schlüssel zu schützen.

Weitere Details finden Sie im GPG-Handbuch: [GPG-Dokumentation](https://www.gnupg.org/documentation/manpage.html).