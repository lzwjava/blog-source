---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Exportieren eines GPG-Privatschlüssels
translated: true
type: note
---

### Exportieren eines GPG-Privatschlüssels vom Server

Um Ihren Privatschlüssel zu exportieren, benötigen Sie Zugriff auf den Server über SSH oder ein Terminal. GPG-Privatschlüssel sind sensibel – gehen Sie sicher mit ihnen um und löschen Sie die exportierte Datei nach der Übertragung.

1. **Listen Sie Ihre geheimen Schlüssel auf** (um den Schlüssel anhand der E-Mail oder Schlüssel-ID zu identifizieren):  
   ```
   gpg --list-secret-keys
   ```  
   Suchen Sie nach einem Eintrag wie `sec   rsa4096/ABC123DEF456 2023-01-01 [SC]`. Notieren Sie sich die E-Mail oder Schlüssel-ID (z.B. `user@example.com` oder `ABC123DEF456`).

2. **Exportieren Sie den Privatschlüssel** (verwenden Sie `--armor` für das ASCII-Format, das einfacher zu übertragen ist):  
   ```
   gpg --export-secret-keys --armor user@example.com > private-key.asc
   ```  
   - Ersetzen Sie `user@example.com` mit Ihrer tatsächlichen E-Mail-Adresse oder Schlüssel-ID.  
   - Dies erstellt `private-key.asc` in Ihrem aktuellen Verzeichnis.  
   - Wenn Sie mehrere Schlüssel haben, geben Sie zur Genauigkeit die Schlüssel-ID an: `gpg --export-secret-keys --armor ABC123DEF456 > private-key.asc`.  
   - **Sicherheitshinweis**: Dies exportiert den Schlüssel *ohne* sein Passphrase. Sie müssen das Passphrase beim Import eingeben, falls dazu aufgefordert.

3. **Übertragen Sie die Datei sicher** auf Ihren lokalen Laptop:  
   - Verwenden Sie `scp` (von Ihrem lokalen Rechner aus):  
     ```
     scp user@server-ip:/path/to/private-key.asc ./
     ```  
     Ersetzen Sie `user@server-ip` mit Ihren Server-Daten und `/path/to/` mit dem tatsächlichen Pfad.  
   - Alternativen: `rsync` für größere Dateien oder SFTP für eine GUI-Option. Vermeiden Sie E-Mail oder ungesicherte Kanäle.

4. **Räumen Sie auf dem Server auf**:  
   ```
   rm private-key.asc
   ```  
   Verifizieren Sie mit `ls`, dass die Datei gelöscht wurde.

### Importieren des GPG-Privatschlüssels auf Ihrem lokalen Laptop

Voraussetzung: Sie haben GPG installiert (z.B. via `apt install gnupg` unter Linux, `brew install gnupg` auf macOS oder Chocolatey unter Windows).

1. **Importieren Sie den Schlüssel**:  
   ```
   gpg --import private-key.asc
   ```  
   - Sie sehen eine Ausgabe wie "gpg: key ABC123DEF456: secret key imported".  
   - Wenn Sie während des Imports nach einem Passphrase gefragt werden, geben Sie das ursprüngliche ein.

2. **Verifizieren Sie den Import**:  
   ```
   gpg --list-secret-keys
   ```  
   Ihr Schlüssel sollte nun unter "sec" erscheinen.

3. **Optional: Legen Sie die Vertrauensstufe fest** (falls Sie den Schlüssel zum Signieren/Verschlüsseln von E-Mails verwenden):  
   ```
   gpg --edit-key user@example.com
   ```  
   - Geben Sie in der Eingabeaufforderung `trust` ein, wählen Sie "ultimate" (Option 5), dann `save` und `quit`.  
   - Dies markiert den Schlüssel auf Ihrem lokalen Rechner als vollständig vertrauenswürdig.

### Tipps und Warnungen
- **Passphrase**: Verwenden Sie immer eine starke Passphrase. Wenn Sie sie vergessen, wird der Schlüssel unbrauchbar.
- **Subkeys**: Wenn Ihr Schlüssel Subkeys hat (z.B. für Verschlüsselung), exportieren Sie diese ebenfalls mit `--export-secret-subkeys`.
- **Backup**: Lagern Sie Exporte in einem sicheren Tresor (z.B. einer verschlüsselten Festplatte).
- **Versionen**: Getestet mit GPG 2.x; funktioniert ähnlich unter 1.x.
- Für weitere Details siehe die offizielle GPG-Dokumentation: [GnuPG Manual](https://www.gnupg.org/documentation/manuals/gnupg/).