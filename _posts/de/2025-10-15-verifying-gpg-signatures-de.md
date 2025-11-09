---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Überprüfung von GPG-Digitalen Signaturen
translated: true
type: note
---

### Signaturen mit GPG überprüfen

GnuPG (GPG) ermöglicht es Ihnen, digitale Signaturen zu überprüfen, um sicherzustellen, dass eine Datei oder Nachricht nicht manipuliert wurde und vom angegebenen Absender stammt. Für die Überprüfung benötigen Sie den öffentlichen Schlüssel des Signierers in Ihrem Schlüsselbund. Nachfolgend finden Sie die Schritte und Befehle für gängige Szenarien.

#### Voraussetzungen
1. **GPG installieren**: Stellen Sie sicher, dass GnuPG auf Ihrem System installiert ist (z. B. via `apt install gnupg` auf Debian-basierten Systemen oder `brew install gnupg` auf macOS).
2. **Öffentlichen Schlüssel des Signierers importieren**: Sie benötigen den öffentlichen Schlüssel der Person oder Entität, die die Datei signiert hat. Laden Sie ihn von einem Keyserver oder aus einer Datei herunter und importieren Sie ihn dann:
   ```
   gpg --import public-key.asc
   ```
   (Ersetzen Sie `public-key.asc` durch die tatsächliche Schlüsseldatei. Wenn er von einem Keyserver stammt, verwenden Sie `gpg --keyserver keyserver.ubuntu.com --recv-keys KEYID`, wobei `KEYID` der Fingerabdruck oder die ID des Schlüssels ist.)

#### Schritte zur Überprüfung
Der genaue Befehl hängt davon ab, wie die Signatur erstellt wurde (z. B. inline in der Datei oder separat).

1. **Eine separate Signatur überprüfen** (üblich für Dateien wie Software-Releases; die Signatur befindet sich in einer separaten `.sig`-Datei):
   ```
   gpg --verify signature.sig original-file
   ```
   - Beispielausgabe für eine gültige Signatur:
     ```
     gpg: Signature made [date] using [key type] key ID [KEYID]
     gpg: Good signature from "[Name] <email@example.com>"
     ```
   - Wenn der Schlüssel nicht als vertrauenswürdig eingestuft ist, erscheint möglicherweise eine Warnung wie "This key is not certified with a trusted signature!". Sie können die Vertrauensstufe mit `gpg --edit-key KEYID` und dann `trust` anpassen.

2. **Eine inline-signierte Datei überprüfen** (die Signatur ist in der Datei eingebettet, oft binär):
   - Nur die Signatur prüfen:
     ```
     gpg --verify signed-file
     ```
   - Die Signatur überprüfen und den ursprünglichen Inhalt extrahieren:
     ```
     gpg --output original-file --decrypt signed-file
     ```
     Dies fordert bei Verschlüsselung zur Eingabe einer Passphrase auf, aber bei reinen Signaturen wird nur die Signatur überprüft.

3. **Eine Clear-Signatur-Nachricht überprüfen** (menschenlesbarer Text mit ASCII-armorierter Signatur, üblich in E-Mails oder READMEs):
   ```
   gpg --verify clearsigned-file.txt
   ```
   Die Ausgabe zeigt den Status der Signatur an, ohne die Datei zu verändern.

#### Problembehebung
- **Fehler "No public key"**: Importieren Sie den Schlüssel wie oben gezeigt.
- **Ungültige Signatur (Bad signature)**: Die Datei wurde möglicherweise verändert – laden Sie sie erneut herunter.
- **Schlüsselgültigkeit**: Überprüfen Sie die Schlüsseldetails mit `gpg --list-keys` oder verifizieren Sie, ob die Fingerabdrücke mit der offiziellen Quelle übereinstimmen.
- Für die Stapelverarbeitung (Batch Verification) oder Skripte fügen Sie `--batch --exit-on-status-write-error` hinzu.

Weitere Details zum Signieren oder zu erweiterten Optionen finden Sie im offiziellen Handbuch.

[Signatures erstellen und überprüfen - GnuPG Handbuch](https://www.gnupg.org/gph/en/manual/x135.html)