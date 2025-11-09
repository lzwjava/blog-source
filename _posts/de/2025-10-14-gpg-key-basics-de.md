---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Grundlagen der GPG-Schlüsselverwaltung
translated: true
type: note
---

## Einführung in die GPG-Schlüsselverwaltung

GPG (GNU Privacy Guard) ist eine freie Implementierung des OpenPGP-Standards für sichere Kommunikation, die zur Verschlüsselung, Signierung und Verifizierung von Daten verwendet wird. Im Kern steht die **Public-Key-Kryptografie**, bei der jeder Benutzer einen **öffentlichen Schlüssel** (offen geteilt für Verschlüsselung und Verifizierung) und einen **privaten Schlüssel** (geheim gehalten für Entschlüsselung und Signierung) besitzt. Die Schlüsselverwaltung umfasst das Erstellen, Verteilen, Verwalten und Sichern dieser Schlüssel, um Manipulationen, Kompromittierung oder Missbrauch zu verhindern. Schlechtes Management kann zu Angriffen wie Schlüsselsubstitution führen, bei der ein Angreifer Ihren Schlüssel durch seinen eigenen ersetzt, um Kommunikation abzufangen.

Das "Web of Trust"-Modell in GPG ermöglicht es Benutzern, die Schlüssel anderer zu zertifizieren und so ein Netzwerk verifizierter Identitäten aufzubauen. Schlüssel werden in **Keyrings** gespeichert (öffentliche und private Dateien, z.B. `pubring.kbx` und `secring.gpg` in älteren Versionen, oder vereinheitlicht in neueren). Sichern Sie immer Ihre privaten Schlüssel und verwenden Sie starke Passphrasen.

## Schlüsselstruktur

Ein GPG-Schlüsselpaar ist nicht nur ein einzelner Schlüssel – es ist ein Bündel:
-   **Primärschlüssel**: Ein Master-Signaturschlüssel (z.B. RSA oder DSA), der zum Zertifizieren (Signieren) anderer Schlüssel und zum Selbstsignieren der Schlüsselkomponenten verwendet wird.
-   **Unterschlüssel**: Optionale untergeordnete Schlüssel für spezifische Aufgaben:
    -   Signatur-Unterschlüssel: Zum Signieren von Nachrichten.
    -   Verschlüsselungs-Unterschlüssel: Zum Verschlüsseln von Daten (oft periodisch ausgetauscht).
    -   Authentifizierungs-Unterschlüssel: Für SSH oder ähnliches.
-   **User IDs (UIDs)**: Zeichenketten wie "Alice (Kommentar) <alice@example.com>", die den Schlüssel mit einer echten Identität verknüpfen. Mehrere UIDs für verschiedene Rollen sind möglich.
-   **Selbstsignaturen**: Der Primärschlüssel signiert seine eigenen Komponenten, um Manipulationen zu verhindern.

Zeigen Sie die Struktur eines Schlüssels interaktiv an:
```
gpg --edit-key <Schlüssel-ID-oder-E-Mail>
```
Im Menü verwenden Sie `check`, um Selbstsignaturen zu überprüfen, oder `toggle`, um private Teile zu sehen (falls verfügbar).

## Schlüssel generieren

Beginnen Sie mit einem Primärschlüsselpaar. Verwenden Sie die interaktive Methode für Anfänger:

1.  Führen Sie `gpg --full-gen-key` aus (oder `--gen-key` für Standardeinstellungen).
2.  Wählen Sie den Schlüsseltyp (Standard: RSA für sowohl Signieren als auch Verschlüsseln).
3.  Wählen Sie die Schlüssellänge (z.B. 4096 Bits für stärkere Sicherheit; Minimum 2048 empfohlen).
4.  Legen Sie ein Ablaufdatum fest (z.B. 1y für ein Jahr; "0" für nie – vermeiden Sie nach Möglichkeit unbegrenzte Gültigkeit).
5.  Geben Sie eine User ID (Name, E-Mail) ein.
6.  Legen Sie eine starke Passphrase fest (20+ Zeichen, Groß-/Kleinschreibung/Symbole).

Für schnelle Generierung (nicht-interaktiv):
```
gpg --quick-generate-key "Alice <alice@example.com>" rsa default 1y
```

Nach der Generierung erstellen Sie ein **Widerrufszertifikat** (eine Datei zum Ungültigmachen Ihres Schlüssels bei Kompromittierung):
```
gpg --output revoke.asc --gen-revoke <Ihre-Schlüssel-ID>
```
Bewahren Sie dieses sicher auf (z.B. ausgedruckt in einem Tresor) – teilen Sie es erst mit, wenn es benötigt wird.

Um später Unterschlüssel oder UIDs hinzuzufügen:
-   Geben Sie `gpg --edit-key <Schlüssel-ID>` ein, dann `addkey` (für Unterschlüssel) oder `adduid` (für UID). Diese werden automatisch selbstsigniert.

## Schlüssel auflisten und anzeigen

-   Öffentliche Schlüssel auflisten: `gpg --list-keys` (oder `--list-public-keys`).
-   Private Schlüssel auflisten: `gpg --list-secret-keys`.
-   Detaillierte Ansicht: `gpg --list-keys --with-subkey-fingerprint <Schlüssel-ID>` (zeigt Fingerabdrücke für Unterschlüssel).

Die Ausgabe zeigt Schlüssel-ID (kurz/lang), Erstellungs-/Ablaufdatum, Fähigkeiten (z.B. `[SC]` für Signieren/Zertifizieren) und UIDs.

## Schlüssel exportieren und importieren

**Exportieren** teilt Ihren öffentlichen Schlüssel oder sichert private Schlüssel:
-   Öffentlicher Schlüssel: `gpg --armor --export <Schlüssel-ID> > mykey.asc` (ASCII-armored für E-Mail).
-   Privater Schlüssel (nur Backup): `gpg --armor --export-secret-keys <Schlüssel-ID> > private.asc`.
-   Zu einem Keyserver: `gpg --keyserver hkps://keys.openpgp.org --send-keys <Schlüssel-ID>`.

**Importieren** fügt die Schlüssel anderer zu Ihrem öffentlichen Keyring hinzu:
-   `gpg --import <datei.asc>` (führt mit existierenden zusammen; fügt neue Signaturen/Unterschlüssel hinzu).
-   Vom Keyserver: `gpg --keyserver hkps://keys.openpgp.org --recv-keys <Schlüssel-ID>`.

Überprüfen Sie nach dem Import mit `gpg --edit-key <Schlüssel-ID>` und `check` auf Selbstsignaturen.

## Schlüssel signieren und zertifizieren

Um Vertrauen aufzubauen:
-   Signieren Sie einen Schlüssel (zertifizieren Sie, dass er gültig ist): `gpg --sign-key <anderer-Schlüssel-ID>` (oder `lsign-key` für nur lokal).
-   Schnelles Signieren: `gpg --quick-sign-key <Fingerabdruck> "User ID"`.
-   Vertrauensstufe festlegen: In `--edit-key` verwenden Sie `trust` (z.B. "5" für ultimatives Vertrauen).

Dies erstellt Signaturen auf dem Schlüssel, die in Auflistungen sichtbar sind. Das Web of Trust berechnet die Gültigkeit basierend auf Ihrem Vertrauen in die Signierenden.

## Schlüssel widerrufen

Widerruf macht einen Schlüssel oder eine Komponente ungültig, ohne ihn zu löschen, und stellt sicher, dass andere sehen, dass er nicht mehr gültig ist:
-   Vollständiger Schlüssel: Importieren Sie Ihr Widerrufszertifikat: `gpg --import revoke.asc`, dann exportieren/senden Sie den aktualisierten Schlüssel.
-   Unterschlüssel/UID: In `--edit-key` wählen Sie mit `key 1` oder `uid 1` aus, dann `revkey` oder `revuid`.
-   Schnelles Widerrufen einer UID: `gpg --quick-revoke-uid <Schlüssel-ID> <zu-widerrufende-UID>`.

Gründe für Widerruf: kompromittiert, nicht mehr verwendet, ersetzt. Veröffentlichen Sie immer widerrufene Schlüssel.

## Best Practices

-   **Sicherheit**: Verwenden Sie Hardware-Tokens (z.B. YubiKey) für private Schlüssel. Tauschen Sie Verschlüsselungs-Unterschlüssel jährlich aus (`gpg --quick-add-key <Fingerabdruck> rsa encr 1y`). Ändern Sie Passphrasen regelmäßig (`gpg --change-passphrase <Schlüssel-ID>`).
-   **Ablaufdatum**: Legen Sie angemessene Ablaufdaten fest (1-2 Jahre), um Updates zu erzwingen und Kompromittierungen zu erkennen.
-   **Verteilung**: Teilen Sie öffentliche Schlüssel über Keyserver oder direkt; verifizieren Sie Fingerabdrücke persönlich oder über vertrauenswürdige Kanäle, um Man-in-the-Middle-Angriffe zu vermeiden.
-   **Backup**: Exportieren Sie private Schlüssel in verschlüsselten Speicher. Erstellen Sie Widerrufszertifikate sofort.
-   **Bereinigung**: Verwenden Sie `gpg --edit-key` mit `clean`, um ungültige Signaturen zu entfernen.
-   **Updates**: Ab GnuPG 2.5+ werden quantenresistente Algorithmen unterstützt (z.B. `--quick-generate-key ... pqc`); ziehen Sie eine Migration für Zukunftssicherheit in Betracht.
-   **Häufige Fehler**: Teilen Sie niemals private Schlüssel. Vermeiden Sie unbegrenzte Ablaufdaten. Testen Sie Widerrufe in einer Sandbox.

Für praktische Übungen experimentieren Sie in einem Testverzeichnis mit `gpg --homedir ./test-gpg`.

[GnuPG Handbuch: Schlüsselverwaltung](https://www.gnupg.org/gph/en/manual/c235.html)
[GNU Privacy Guard Handbuch: OpenPGP-Schlüsselverwaltung](https://www.gnupg.org/documentation/manuals/gnupg/OpenPGP-Key-Management.html)
[GnuPG Erste Schritte](https://www.gnupg.org/gph/en/manual/c14.html)