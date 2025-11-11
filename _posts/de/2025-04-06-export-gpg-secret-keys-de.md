---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Exportieren von GPG-Geheimschlüsseln auf sichere Weise
translated: true
type: note
---

### Exportieren von geheimen Schlüsseln mit GPG im Armored-Format

GPG (GNU Privacy Guard) ermöglicht das Exportieren geheimer (privater) Schlüssel in einem armorierten ASCII-Format, wodurch sie als menschenlesbare `.asc`-Datei (nicht binär) gespeichert werden. Dies ist nützlich für Backups, Übertragungen oder den Import auf einem anderen Rechner.

**Wichtige Warnung:** Geheime Schlüssel enthalten sensible Informationen. Exportieren Sie sie nur, wenn es notwendig ist, verschlüsseln Sie die Ausgabedatei bei Speicherung oder Übertragung und löschen Sie den Export nach der Verwendung, um unbeabsichtigte Preisgaben zu vermeiden. Geben Sie geheime Schlüssel niemals öffentlich preis.

#### Grundlegende Befehlsstruktur
Um einen geheimen Schlüssel für eine bestimmte User-ID (die mit dem Schlüssel verknüpfte E-Mail oder Name) zu exportieren, verwenden Sie:

```
gpg --export-secret-keys --armor [KEY_ID] > dateiname.asc
```

- `KEY_ID`: Der Key Fingerprint, die kurze ID, E-Mail oder der Name. Sie können Ihre Schlüssel mit `gpg --list-secret-keys` auflisten.
- `--armor`: Gibt die Ausgabe im armierten (ASCII) Format statt im Binärformat aus.
- `> dateiname.asc`: Leitet die Ausgabe in eine Datei um (z.B. `my_secret_key.asc`). Lassen Sie dies weg, um die Ausgabe im Terminal anzuzeigen.

#### Schritt-für-Schritt-Anwendungsbeispiel
1. **Listen Sie Ihre geheimen Schlüssel auf**, um die KEY_ID zu finden:
   ```
   gpg --list-secret-keys
   ```
   Beispielausgabe:
   ```
   sec   rsa3072/ABC12345 2023-01-01 [SC] [expires: 2025-01-01]
         Key fingerprint = 1234 5678 ABCD EF01 2345 6789 ABCD EF01 2345 6789
   uid                 [ultimate] Ihr Name <ihre@email.de>
   ```

   Hier ist `ABC12345` die kurze Schlüssel-ID, oder verwenden Sie für mehr Genauigkeit den vollständigen Fingerprint `ABCDEF0123456789ABCDEF0123456789`.

2. **Exportieren Sie den geheimen Schlüssel**:
   ```
   gpg --export-secret-keys --armor ABC12345 > my_secret_key.asc
   ```

3. **Überprüfen Sie den Export** (optional):
   ```
   cat my_secret_key.asc
   ```
   Die Datei sollte mit `-----BEGIN PGP PRIVATE KEY BLOCK-----` beginnen und mit `-----END PGP PRIVATE KEY BLOCK-----` enden.

#### Zusätzliche Optionen
- **Alle geheimen Schlüssel exportieren**: Lassen Sie die KEY_ID weg, um alle zu exportieren:
  ```
  gpg --export-secret-keys --armor > all_secret_keys.asc
  ```
- **Mit Passwortschutz**: GPG fordert Sie nach Ihrem Passwort auf, wenn der Schlüssel verschlüsselt ist (Standard).
- **Wenn Sie stattdessen öffentliche Schlüssel benötigen**: Verwenden Sie `--export` (nur für öffentliche Schlüssel).

Die vollständige Dokumentation finden Sie in der GPG-Manpage: `man gpg`. Wenn Sie neu bei GPG sind, generieren Sie zuerst einen Schlüssel mit `gpg --gen-key`.