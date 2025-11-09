---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Behebung von GPG-Signaturverifizierungsfehlern
translated: true
type: note
---

### Den Fehler verstehen

Der Fehler tritt auf, weil der Befehl `gpg --verify` in den meisten Fällen zwei Argumente erwartet: Zuerst die **Signaturdatei** (z.B. `zhs.tw.yaml.sig` oder `zhs.tw.yaml.asc`), gefolgt von der **eigentlichen Datei**, die überprüft werden soll (z.B. `zhs.tw.yaml`).

In Ihrem Befehl:
```
gpg --verify zhs.tw.yaml
```
versucht GPG, `zhs.tw.yaml` sowohl als Signatur- *als auch* als Datendatei zu interpretieren, aber sie enthält keine gültigen OpenPGP-Signaturdaten (YAML-Dateien sind keine Signaturen). Daher die Meldung "no valid OpenPGP data found".

### So beheben Sie den Fehler

1. **Signaturdatei finden**: Sie benötigen die abgetrennte Signaturdatei, die zu Ihrer YAML-Datei gehört. Sie heißt normalerweise:
   - `zhs.tw.yaml.sig` (Binärformat)
   - `zhs.tw.yaml.asc` (ASCII-armored Format)

   Wenn Sie sie nicht haben, müssen Sie sie von der Quelle herunterladen, von der Sie `zhs.tw.yaml` erhalten haben (z.B. ein Projekt-Repo oder eine Website).

2. **Den korrekten Befehl ausführen**: Sobald Sie die Signatur haben, verwenden Sie dieses Format:
   ```
   gpg --verify zhs.tw.yaml.sig zhs.tw.yaml
   ```
   - Ersetzen Sie `.sig` durch `.asc`, falls das Ihr Dateiformat ist.
   - Die Reihenfolge ist wichtig: zuerst die Signatur, dann die Datei.

3. **Erwartete Ausgabe bei Erfolg**:
   Wenn die Signatur gültig ist und Sie dem Schlüssel vertrauen, sehen Sie etwa:
   ```
   gpg: Signature made [date] using [key type]
   gpg: Good signature from "[signer name/email]"
   ```
   Wenn sie ungültig ist oder der Schlüssel nicht vertraut wird, erhalten Sie Warnungen/Fehler.

### Zusätzliche Tipps

- **Öffentlichen Schlüssel importieren**: Falls GPG sich über einen unbekannten Schlüssel beschwert, holen und importieren Sie den öffentlichen Schlüssel des Signierers:
  ```
  gpg --keyserver keyserver.ubuntu.com --recv-keys [KEY_ID]
  ```
  (Ersetzen Sie `[KEY_ID]` durch den tatsächlichen Schlüssel-Fingerprint aus der Fehlerausgabe oder der Projekt-Dokumentation.)

- **Batch-Modus für Skripte**: Wenn Sie dies automatisieren, fügen Sie `--batch` hinzu, um Eingabeaufforderungen zu unterdrücken:
  ```
  gpg --batch --verify zhs.tw.yaml.sig zhs.tw.yaml
  ```

- **Eingebettete Signaturen**: Wenn die Signatur *in* der YAML-Datei eingebettet ist (unwahrscheinlich für `.yaml`), würden Sie einfach `gpg --verify zhs.tw.yaml` ausführen, nachdem Sie sichergestellt haben, dass die Datei mit `-----END PGP SIGNATURE-----` endet. Aber basierend auf dem Fehler handelt es sich um eine abgetrennte Signatur.

Wenn dies das Problem nicht löst oder Sie weitere Details teilen (z.B. woher die Datei stammt), kann ich die Ratschläge verfeinern!

[GNU Privacy Guard Manual](https://www.gnupg.org/documentation/manpage.html)