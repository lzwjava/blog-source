---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Kryptografische Algorithmen in GnuPG
translated: true
type: note
---

### Unterstützte Algorithmen in kryptografischer Software (z.B. GnuPG)

Diese Liste gibt einen Überblick über die Algorithmen, die von einem Tool wie GnuPG (GPG) unterstützt werden, welches häufig für sichere E-Mails (PGP/MIME), Dateiverschlüsselung und digitale Signaturen verwendet wird. Sie kategorisiert diese in Public-Key-Kryptografie (asymmetrisch) für Schlüsselaustausch und Signatur, symmetrische Chiffren für die Massendatenverschlüsselung, Hash-Funktionen für Integritätsprüfungen und Signaturen sowie Kompressionsmethoden zur Verringerung der Datengröße vor der Verschlüsselung. Im Folgenden werde ich sie nach Kategorien aufschlüsseln und jede Algorithmus kurz in Bezug auf Zweck und Haupteigenschaften erklären.

#### Public-Key-Algorithmen (Pubkey)
Diese handhaben asymmetrische Operationen: Ein Schlüssel (öffentlich) dient zur Verschlüsselung/Signaturprüfung, ein anderer (privat) zur Entschlüsselung/Signatur. Sie werden in Schlüsselpaaren für sichere Kommunikation verwendet.

-   **RSA**: Rivest-Shamir-Adleman. Ein grundlegender Algorithmus für sowohl Verschlüsselung als auch digitale Signaturen. Weit verbreitet aufgrund seiner Sicherheit bei großen Schlüsselgrößen (z.B. 2048+ Bits), aber rechenintensiv.
-   **ELG**: ElGamal. Primär für Verschlüsselung (nicht für Signaturen). Basiert auf dem Problem des diskreten Logarithmus; effizient für Schlüsselaustausch, erzeugt aber größere Chiffrate.
-   **DSA**: Digital Signature Algorithm. Ausschließlich für digitale Signaturen konzipiert (nicht für Verschlüsselung). Basiert auf diskreten Logarithmen; verbreitet in älteren Systemen, aber weitgehend durch ECDSA aus Effizienzgründen ersetzt.
-   **ECDH**: Elliptic Curve Diffie-Hellman. Für Schlüsselvereinbarung/-austausch unter Verwendung elliptischer Kurven. Bietet starke Sicherheit mit kleineren Schlüsseln als traditionelles DH, ideal für mobile/eingeschränkte Geräte.
-   **ECDSA**: Elliptic Curve Digital Signature Algorithm. Eine Elliptic-Curve-Variante von DSA für Signaturen. Schneller und sicherer pro Bit als DSA, mit weit verbreiteter Verwendung in modernen Protokollen wie TLS.
-   **EDDSA**: Edwards-curve Digital Signature Algorithm. Ein hochgeschwindigkeits Elliptic-Curve-Signaturverfahren (z.B. Ed25519-Variante). Resistent gegen Side-Channel-Angriffe; bevorzugt in Protokollen wie SSH und Signal aufgrund seiner Einfachheit und Geschwindigkeit.

#### Symmetrische Chiffren
Diese verschlüsseln Daten mit einem gemeinsamen geheimen Schlüssel (schneller für große Dateien). Blockchiffren verarbeiten Daten in Blöcken fester Größe, oft mit Modi wie CBC für Verkettung.

-   **IDEA**: International Data Encryption Algorithm. Eine 64-Bit-Blockchiffre aus den 1990ern; einst populär, aber jetzt aufgrund der Schlüsselgröße und Brute-Force-Risiken als schwach angesehen.
-   **3DES**: Triple Data Encryption Standard. Wendet DES dreimal für zusätzliche Sicherheit an. Legacy-Algorithmus; langsam und anfällig für Angriffe, zugunsten von AES ausgemustert.
-   **CAST5**: CAST-128. Eine 64-Bit-Blockchiffre (CAST-Familie). Ausgewogenes Verhältnis von Geschwindigkeit/Sicherheit für seine Ära; wird noch verwendet, aber von AES überschattet.
-   **BLOWFISH**: Eine 64-Bit-Blockchiffre mit variablen Schlüssellängen (bis zu 448 Bits). Schnell und flexibel; gut für Software, aber nicht hardwarebeschleunigt wie AES.
-   **AES**: Advanced Encryption Standard (128-Bit-Schlüssel). NIST-geprüfte Blockchiffre; der Goldstandard für symmetrische Verschlüsselung – sicher, schnell und allgegenwärtig.
-   **AES192**: AES mit 192-Bit-Schlüsseln. Bietet einen Sicherheitsboost in der Mitte zwischen Standard-AES und AES256.
-   **AES256**: AES mit 256-Bit-Schlüsseln. Variante von AES mit der höchsten Sicherheit; empfohlen für hochsensible Daten.
-   **TWOFISH**: Eine 128-Bit-Blockchiffre (AES-Finalist). Hochsicher mit flexiblen Schlüsselgrößen; gute Leistung in Software.
-   **CAMELLIA128**: Camellia-Blockchiffre (128-Bit-Schlüssel). Japanischer/europäischer Standard; AES-ähnliche Sicherheit und Geschwindigkeit.
-   **CAMELLIA192**: Camellia mit 192-Bit-Schlüsseln. Erweiterte Sicherheitsstufe.
-   **CAMELLIA256**: Camellia mit 256-Bit-Schlüsseln. Top-Variante, vergleichbar mit AES256.

#### Hash-Algorithmen
Diese erzeugen Digest fester Länge aus Daten, um Integrität, Authentizität zu überprüfen oder für Signaturen/Passwörter zu verwenden. Kollisionsresistenz ist entscheidend (obwohl SHA1 jetzt gebrochen ist).

-   **SHA1**: Secure Hash Algorithm 1. Erzeugt 160-Bit-Digests; schnell aber unsicher aufgrund von Kollisionsschwachstellen – für neue Anwendungen vermeiden.
-   **RIPEMD160**: RACE Integrity Primitives Evaluation Message Digest (160-Bit). Europäische Alternative zu SHA1; immer noch recht sicher, aber alternd.
-   **SHA256**: SHA-2-Familie (256-Bit). Robust und weit verbreitet; Grundlage für Bitcoin und sichere Passwörter.
-   **SHA384**: SHA-2 (384-Bit). Längerer Digest für höhere Sicherheit in sensiblen Anwendungen.
-   **SHA512**: SHA-2 (512-Bit). Größte SHA-2-Variante; exzellent für High-Security-Hashing.
-   **SHA224**: SHA-2 (224-Bit). Ein gekürzter SHA-256 für Legacy-Kompatibilität.

#### Kompressionsalgorithmen
Diese verkleinern Daten vor der Verschlüsselung, um die Verarbeitung zu beschleunigen und die Speicher-/Übertragungsgröße zu reduzieren. Werden in Tools wie GPG transparent angewendet.

-   **Uncompressed**: Keine Komprimierung – Daten werden unverändert verschlüsselt. Nützlich für bereits komprimierte Dateien (z.B. JPEGs), um Overhead zu vermeiden.
-   **ZIP**: DEFLATE-Algorithmus (LZ77 + Huffman-Codierung). Üblich in Dateiarchiven; gute Balance aus Geschwindigkeit und Kompressionsrate.
-   **ZLIB**: Erweiterter DEFLATE mit Headern/Prüfsummen. Ähnlich wie ZIP, aber flexibler für Streams.
-   **BZIP2**: Burrows-Wheeler-Transformation + Huffman. Langsamer, erreicht aber bessere Kompressionsraten als ZIP/ZLIB, besonders für Text.

Diese Konfiguration ermöglicht flexible, sichere Arbeitsabläufe – z.B. Signieren mit ECDSA, Verschlüsseln mit AES256, Hashen mit SHA256 und Komprimieren mit ZLIB. Für die neuesten GnuPG-Details siehe das [offizielle Handbuch](https://www.gnupg.org/documentation/manuals/gnupg/index.html).