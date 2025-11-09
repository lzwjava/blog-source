---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GPG-Verschlüsselung und Signatur erklärt
translated: true
type: note
---

### GPG Grundlagen: Verschlüsselung vs. Signieren

Sie vermischen hier ein paar Konzepte – GPG (GNU Privacy Guard) kann **Verschlüsselung** (zum Schutz von Dateiinhalten) und **Signieren** (zur Überprüfung von Identität und Integrität) durchführen – aber das sind separate Funktionen. Ich werde es Schritt für Schritt aufschlüsseln, Ihre Punkte bestätigen und klären, wo sich Dinge überschneiden oder unterscheiden. Dies basiert auf der Standard-GPG-Nutzung (die sich Stand 2025 nicht wesentlich geändert hat).

#### 1. **Schlüssel generieren und Ihre Daten (Name/E-Mail)**
   - Wenn Sie GPG zum ersten Mal einrichten, generieren Sie ein **Schlüsselpaar**: einen privaten Schlüssel (geheim gehalten) und einen öffentlichen Schlüssel (mit anderen geteilt).
   - Während der Generierung geben Sie Ihren **Namen und Ihre E-Mail-Adresse** als Teil der "User ID" des Schlüssels an (z.B. `gpg --gen-key`). Dies bindet den Schlüssel an Ihre Identität.
   - Sie legen auch eine **Passphrase** fest, um Ihren privaten Schlüssel zu schützen. Diese Passphrase wird **nicht** zum Verschlüsseln von Dateien verwendet – sie dient nur dazu, Ihren privaten Schlüssel bei Bedarf freizuschalten.
   - Befehlsbeispiel:
     ```
     gpg --gen-key
     ```
     Folgen Sie den Eingabeaufforderungen für RSA/RSA, Schlüsselgröße, Ablaufdatum und Ihren Namen/Ihre E-Mail.

#### 2. **Eine Datei verschlüsseln**
   - **Mit einem Passwort (symmetrische Verschlüsselung)**: Dies beinhaltet keine Schlüssel oder Ihre Identität – es ist eine schnelle Methode, um eine Datei sicher zu teilen. GPG verwendet die Passphrase, um einen einzelnen Schlüssel für die Verschlüsselung zu erstellen.
     - Befehl: `gpg -c dateiname.txt` (fordert zur Passphrase-Eingabe auf, erzeugt `dateiname.txt.gpg`).
     - Jeder mit der Passphrase kann entschlüsseln: `gpg -d dateiname.txt.gpg`.
     - Hier werden keine öffentlichen/privaten Schlüssel verwendet; keine Identitätsüberprüfung.
   - **Mit öffentlichen Schlüsseln (asymmetrische Verschlüsselung)**: Um für einen bestimmten Empfänger zu verschlüsseln, verwenden Sie dessen öffentlichen Schlüssel. Ihr Name/Ihre E-Mail-Adresse ist nicht direkt am Verschlüsselungs-Ergebnis beteiligt.
     - Befehl: `gpg -e -r recipient@example.com dateiname.txt` (erzeugt `dateiname.txt.gpg`).
     - Nur der private Schlüssel des Empfängers kann es entschlüsseln.
   - Das Verschlüsselungsergebnis ist eine `.gpg`-Datei, aber es ist **keine Signatur** – es sind nur verschlüsselte Daten. Keine "GPG-Signatur" durch reine Verschlüsselung.

#### 3. **Eine Datei signieren (was Sie beschreiben)**
   - Das Signieren fügt einer Datei (oder ihrem Hash) eine **digitale Signatur** hinzu, um zu beweisen, dass sie von Ihnen stammt und nicht manipuliert wurde. Hier kommen Ihr **privater Schlüssel** und Ihre Identität ins Spiel.
   - **Ja, Sie müssen Ihren privaten Schlüssel verwenden, um die Signatur zu generieren.** GPG entsperrt ihn mit Ihrer Passphrase.
     - Befehl für eine abgetrennte (detached) Signatur: `gpg --detach-sign dateiname.txt` (erzeugt `dateiname.txt.sig`).
     - Oder inline (signiert und verschlüsselt in einem Schritt): `gpg -s dateiname.txt` (erzeugt `dateiname.txt.gpg` mit eingebetteter Signatur).
   - Die Signatur ist ein kryptografischer "Wert" (wie ein mit Ihrem privaten Schlüssel signierter Hash), der Ihre Schlüssel-ID und User-ID (Name/E-Mail) enthält.
   - **Andere verifizieren mit Ihrem öffentlichen Schlüssel**: Sie importieren Ihren öffentlichen Schlüssel (z.B. von einem Keyserver: `gpg --keyserver keys.openpgp.org --recv-keys IHRE_SCHLÜSSEL_ID`), und führen dann `gpg --verify dateiname.txt.sig dateiname.txt` aus.
     - Wenn es übereinstimmt, erscheint eine Meldung wie "Good signature from 'Ihr Name <email>'".
   - **Ja, dies bestätigt die Identität und schafft Vertrauen**:
     - Die Signatur beweist, dass die Datei vom Schlüsselinhaber (Ihnen) stammt.
     - Wenn Sie Ihren öffentlichen Schlüssel über einen vertrauenswürdigen Kanal (z.B. Ihre Website) geteilt haben und der Schlüssel von anderen, denen Sie vertrauen, signiert wurde, können Sie der Kette "vertrauen".
     - Es verschlüsselt die Datei nicht – es verifiziert sie nur. Kombinieren Sie es mit Verschlüsselung für vollständige Sicherheit (signieren, dann verschlüsseln).

#### Wichtige Unterschiede und Ihre Fragen

| Merkmal | Verschlüsselung (Passwort) | Verschlüsselung (Öffentl. Schlüssel) | Signieren |
|---------|-----------------------|--------------------------|---------|
| **Verwendet Passphrase?** | Ja, für symmetrischen Schlüssel | Nein (verwendet öffentl. Schlüssel des Empf.) | Ja, zum Entsperren des privaten Schlüssels |
| **Bezieht Name/E-Mail ein?** | Nein | Indirekt (über Ihren Schlüssel für Entschl.) | Ja, in Signatur eingebettet |
| **Ausgabe** | `.gpg`-Datei (verschl. Daten) | `.gpg`-Datei (verschl. Daten) | `.sig` oder eingebettet in `.gpg` (Signaturwert) |
| **Priv. Schlüssel nötig?** | Nein | Nein (zum Verschl. für andere) | Ja, zum Generieren |
| **Verifizierung** | Passphrase zum Entschl. | Priv. Schlüssel des Empf. | Jeder mit Ihrem öffentl. Schlüssel |
| **Zweck** | Inhalt verbergen | Sichere Weitergabe | Identität/Integrität beweisen |

- **Richtig bezüglich des privaten Schlüssels**: Ja, Sie **müssen** Ihren privaten Schlüssel (durch Passphrase freigeschaltet) zum Signieren verwenden. Teilen Sie ihn niemals!
- **Richtig bezüglich Vertrauen**: Genau – wenn die Signatur gegen Ihren öffentlichen Schlüssel verifiziert wird und Sie diesem Schlüssel vertrauen (durch Name/E-Mail und Web of Trust), können Sie darauf vertrauen, dass die Datei authentisch und unverändert ist. Es ist wie ein digitaler Notar.

#### Tipps
- Sichern Sie immer Ihre Schlüssel: `gpg --export-secret-keys --armor > private.asc` (sicher speichern).
- Für reine Passwörter (ohne Schlüssel) sind Tools wie `age` oder `openssl` einfachere Alternativen, aber GPG ist großartig für identitätsbezogene Dinge.
- Häufige Fehlerquelle: Das Vergessen, den öffentlichen Schlüssel zu exportieren/teilen, bedeutet, dass andere nicht verifizieren können.

Falls Sie einen bestimmten Befehl oder ein Szenario meinten (z.B. gleichzeitiges Verschlüsseln *und* Signieren), teilen Sie bitte mehr Details mit!

**Referenzen**  
[GPG-Dokumentation: Verschlüsseln und Signieren](https://www.gnupg.org/documentation/manuals/gnupg/)  
[GPG Schnellstart-Anleitung](https://www.gnupg.org/documentation/manuals/gnupg/GnuPG-basics.html)