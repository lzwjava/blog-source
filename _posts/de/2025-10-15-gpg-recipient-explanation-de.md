---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GPG-Verschlüsselung Empfängererklärung
translated: true
type: note
---

### Den GPG-Befehl und die Eingabeaufforderung für "Recipient" verstehen

Der Befehl, den Sie ausführen, dient zum Verschlüsseln einer Datei (`inputfile.txt`) mit GnuPG (GPG):

```
gpg --homedir /pfad/zu/benutzerdefiniertem/verzeichnis -e -r recipient@example.com --encrypt inputfile.txt
```

- `--homedir /pfad/zu/benutzerdefiniertem/verzeichnis`: Verwendet ein benutzerdefiniertes Verzeichnis für den GPG-Schlüsselbund und die Konfiguration (anstelle des Standardverzeichnisses `~/.gnupg`).
- `-e` (oder `--encrypt`): Weist GPG an, die Datei zu verschlüsseln.
- `-r recipient@example.com`: Spezifiziert den **Empfänger** (die Person oder Entität, für die Sie verschlüsseln). Dies sollte deren E-Mail, Name oder Schlüssel-ID aus ihrem öffentlichen Schlüssel sein.
- `--encrypt inputfile.txt`: Die zu verschlüsselnde Datei (die Ausgabe wird `inputfile.txt.gpg` sein).

#### Was bedeutet "Recipient" hier?
Bei der GPG-Verschlüsselung:
- Der **Empfänger** ist die Person, die die Datei *empfangen und entschlüsseln* wird. Sie verschlüsseln die Datei mit *deren öffentlichem Schlüssel*, sodass nur sie (mit ihrem privaten Schlüssel) sie entschlüsseln kann.
- Es ist nicht der "Absender" (Sie), weil die Verschlüsselung die Daten *für den Empfänger* schützt. Ihre Rolle als Absender betrifft eher das Signieren (wenn Sie `-s` für Signatur hinzufügen), aber hier geht es um reine Verschlüsselung.

Sie haben recht, dass dies für das "Senden" sicherer Daten ist, aber die Terminologie konzentriert sich auf den Empfänger, weil dessen Schlüssel die Sicherheit gewährleistet. Stellen Sie es sich vor, wie eine Kiste mit dem Vorhängeschloss einer anderen Person zu verschließen – nur sie können es öffnen.

#### Warum der Fehler: "You did not specify a user ID. (you may use '-r')" und die Eingabeaufforderung?
Diese interaktive Eingabeaufforderung erscheint, weil:
1.  GPG keinen öffentlichen Schlüssel finden konnte, der `recipient@example.com` in Ihrem Schlüsselbund (im benutzerdefinierten Home-Verzeichnis) entspricht.
2.  Das Flag `-r` wurde angegeben, aber es konnte keinem gültigen Schlüssel zugeordnet werden, also fordert GPG Sie interaktiv auf, die Benutzer-ID manuell einzugeben.

Die Eingabeaufforderung lautet:
```
Current recipients:
Enter the user ID.  End with an empty line:
```

- **User ID** bedeutet die vollständige Kennung des Empfängers, wie `Max Mustermann <recipient@example.com>` oder deren Schlüssel-Fingerabdruck/ID (z.B. `ABCDEF123456`).
- Geben Sie sie zeilenweise ein, falls nötig (z.B. Name, E-Mail, Kommentar), und drücken Sie dann zweimal die Eingabetaste (leere Zeile), um abzuschließen.

#### Wie man das Problem behebt
1.  **Importieren Sie zuerst den öffentlichen Schlüssel des Empfängers** (häufigste Ursache):
    - Bitten Sie den Empfänger, Ihnen seinen öffentlichen Schlüssel zu senden (exportiert via `gpg --export -a their@email.com`).
    - Importieren Sie ihn: `gpg --homedir /pfad/zu/benutzerdefiniertem/verzeichnis --import their-public-key.asc`.
    - Führen Sie dann Ihren Befehl erneut aus.

2.  **Wenn der Schlüssel bereits importiert wurde, aber nicht übereinstimmt**:
    - Schlüssel auflisten: `gpg --homedir /pfad/zu/benutzerdefiniertem/verzeichnis --list-keys`.
    - Verwenden Sie die exakte Benutzer-ID von dort in `-r` (z.B. `-r "Max Mustermann <recipient@example.com>"`).

3.  **In der Eingabeaufforderung** (als schnelle Problemumgehung):
    - Geben Sie die vollständige Benutzer-ID ein, z. B.:
      ```
      Max Mustermann
      recipient@example.com
      
      ```
      (Leere Zeile beendet die Eingabe.)

#### Warum "Recipient" statt "Sender"?
- Verschlüsselung ist *asymmetrisch*: Öffentlicher Schlüssel (jeder kann verschlüsseln) → Privater Schlüssel (nur der Besitzer kann entschlüsseln).
- Absender (Sie) verschlüsselt mit dem **öffentlichen** Schlüssel des Empfängers.
- Wenn Sie beweisen möchten, dass Sie der Absender sind, fügen Sie eine Signatur hinzu: `gpg ... -e -r recipient@example.com -s --encrypt inputfile.txt` (verwendet *Ihren* privaten Schlüssel zum Signieren).
- "Recipient" ist die Standard-Terminologie in GPG – es geht nicht darum, wer sendet, sondern wer empfängt/entschlüsselt. Es "Sender" zu nennen, wäre verwirrend, da Absender keinen Schlüssel für die Verschlüsselung benötigen (nur für die Signatur).

Wenn dies das Problem nicht löst, teilen Sie die Ausgabe von `--list-keys` mit (zensieren Sie sensible Informationen), und ich kann bei der Fehlersuche helfen!

#### Referenzen
- [GPG Encryption Basics](https://www.gnupg.org/documentation/manuals/gnupg/Encrypting-and-Decrypting.html)
- [GPG Man Page](https://www.gnupg.org/documentation/manuals/gnupg/gpg.html)