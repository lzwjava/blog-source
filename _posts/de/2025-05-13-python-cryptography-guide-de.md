---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Python-Kryptografie-Leitfaden
translated: true
type: note
---

### Einführung in das Cryptography-Paket
Das `cryptography`-Paket ist eine beliebte Python-Bibliothek, die kryptografische Primitive und Rezepte für sichere Protokolle bereitstellt. Es konzentriert sich auf Benutzerfreundlichkeit und Sicherheit und implementiert Standards wie AES, RSA und mehr. Es dient nicht zur direkten Implementierung hochrangiger Protokolle wie SSH oder TLS – verwenden Sie es als Baustein. Stellen Sie stets sicher, dass es auf dem neuesten Stand ist, um Sicherheitspatches zu erhalten.

### Installation
Installation via pip:
```bash
pip install cryptography
```
Für eine bessere Leistung (insbesondere bei großen Schlüsseln oder häufigen Operationen) installieren Sie es mit OpenSSL-Unterstützung:
```bash
pip install cryptography[openssl]
```
Hinweis: Auf einigen Systemen müssen Sie die OpenSSL-Header separat installieren (z.B. `apt install libssl-dev` unter Ubuntu).

### Grundkonzepte
- **Primitive**: Niedrige Operationen wie Verschlüsselung/Entschlüsselung.
- **Rezepte**: Hochrangige, vorgegebene Funktionen (z.B. Fernet für symmetrische Verschlüsselung).
- **Gefahrenhinweise**: Die Bibliothek verwendet Warnungen für unsichere Nutzung – achten Sie darauf.

Importieren Sie die Bibliothek:
```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes, asyncioc as a
from cryptography.hazmat.primitives.asymmetric import rsa, padding
```

### Beispiele

#### 1. Symmetrische Verschlüsselung mit Fernet (Am einfachsten für Anfänger)
Fernet verwendet AES-128 im CBC-Modus mit HMAC für Integrität. Es ist ideal zum Speichern verschlüsselter Daten.

```python
from cryptography.fernet import Fernet

# Schlüssel generieren (sicher aufbewahren, z.B. in Umgebungsvariablen)
key = Fernet.generate_key()
cipher = Fernet(key)

# Verschlüsseln
plaintext = b"This is a secret message."
token = cipher.encrypt(plaintext)
print("Verschlüsselt:", token)

# Entschlüsseln
decrypted = cipher.decrypt(token)
print("Entschlüsselt:", decrypted)
```
- **Hinweise**: Schlüssel sind URL-sicheres Base64 (44 Zeichen). Schlüssel niemals im Code hartkodieren; rotieren Sie sie regelmäßig.

#### 2. Asymmetrische Verschlüsselung mit RSA
Generieren Sie ein öffentliches/privates Schlüsselpaar und verschlüsseln Sie Daten, die nur der Besitzer des privaten Schlüssels entschlüsseln kann.

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Privaten Schlüssel generieren
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Für die Speicherung serialisieren
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()  # Verwenden Sie BestAvailableEncryption() für Passwortschutz
)

# Öffentlichen Schlüssel abrufen und serialisieren
public_key = private_key.public_key()
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Mit öffentlichem Schlüssel verschlüsseln
plaintext = b"Secret message"
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

# Mit privatem Schlüssel entschlüsseln
decrypted = private_key.decrypt(
    ciphertext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
print("Entschlüsselt:", decrypted)
```
- **Hinweise**: RSA ist langsam für große Datenmengen; verwenden Sie es für Schlüsselaustausch oder kleine Nachrichten. OAEP-Padding verhindert Angriffe.

#### 3. Erzeugen und Verwenden von Hashwerten
Für Integritätsprüfungen oder Passwort-Hashing.

```python
from cryptography.hazmat.primitives import hashes

# Daten hashen
digest = hashes.Hash(hashes.SHA256())
digest.update(b"Some data")
hash_result = digest.finalize()
print("SHA256 Hash:", hash_result.hex())
```

Für Passwörter verwenden Sie `cryptography.hazmat.primitives.kdf.pbkdf2` für Schlüsselableitung (z.B. PBKDF2 für langsames, gesalzenes Hashing).

#### 4. Digitale Signaturen mit RSA
Signieren Sie Daten, um deren Authentizität zu beweisen.

```python
# Verwendung der RSA-Schlüssel von weiter oben
message = b"Data to sign"
signature = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

# Mit öffentlichem Schlüssel verifizieren
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print("Signatur gültig")
except Exception:
    print("Signatur ungültig")
```

### Best Practices
- **Schlüsselverwaltung**: Bewahren Sie Schlüssel sicher auf (z.B. mit AWS KMS, Hardware Security Modules). Schlüssel niemals wiederverwenden.
- **Padding und Modi**: Verwenden Sie stets sicheres Padding (z.B. OAEP für RSA, GCM für AES).
- **Zufälligkeit**: Verwenden Sie `os.urandom()` oder das `secrets`-Modul für Seeds; vermeiden Sie `random`.
- **Updates**: Kryptografie entwickelt sich weiter – prüfen Sie Ihre Nutzung auf Schwachstellen.
- **Vermeiden Sie Eigenentwicklungen**: Verwenden Sie für komplexe Anforderungen Rezepte oder integrieren Sie höherrangige Bibliotheken wie `pyjwt` oder `boto3`.
- **Tests**: Verwenden Sie die Konstanten und Ausnahmen der Bibliothek für die Fehlerbehandlung.

### Weiterführende Literatur
- [Offizielle Dokumentation](https://cryptography.io/en/latest/) – Detaillierte API-Referenz und Tutorials.
- [PyPI-Seite](https://pypi.org/project/cryptography/) – Versionsverlauf und Integrationen.
- Für fortgeschrittene Themen, erkunden Sie das `cryptography`-Wiki oder RFCs (z.B. RFC 8017 für PKCS#1).

Wenn Sie einen spezifischen Anwendungsfall haben (z.B. das Verschlüsseln von Dateien oder API-Sicherheit), geben Sie weitere Details für maßgeschneiderte Beispiele an.