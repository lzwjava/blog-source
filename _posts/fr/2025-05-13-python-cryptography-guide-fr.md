---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide de Cryptographie Python
translated: true
type: note
---

### Introduction au package Cryptography
Le package `cryptography` est une bibliothèque Python populaire qui fournit des primitives cryptographiques et des recettes pour des protocoles sécurisés. Il se concentre sur la facilité d'utilisation et la sécurité, implémentant des standards comme AES, RSA, et plus encore. Il n'est pas destiné à implémenter directement des protocoles de haut niveau comme SSH ou TLS—utilisez-le comme un composant de base. Vérifiez toujours qu'il est à jour avec les correctifs de sécurité.

### Installation
Installez via pip :
```bash
pip install cryptography
```
Pour de meilleures performances (surtout pour les grandes clés ou les opérations fréquentes), installez avec le support OpenSSL :
```bash
pip install cryptography[openssl]
```
Note : Sur certains systèmes, vous devrez peut-être installer les en-têtes OpenSSL séparément (par exemple, `apt install libssl-dev` sur Ubuntu).

### Concepts de base
- **Primitives** : Opérations de bas niveau comme le chiffrement/déchiffrement.
- **Recettes** : Fonctions de haut niveau, orientées (par exemple, Fernet pour le chiffrement symétrique).
- **Avertissements de danger** : La bibliothèque utilise des avertissements pour les utilisations non sécurisées—soyez attentif à eux.

Importez la bibliothèque :
```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes, asyncioc as a
from cryptography.hazmat.primitives.asymmetric import rsa, padding
```

### Exemples

#### 1. Chiffrement symétrique avec Fernet (Le plus simple pour les débutants)
Fernet utilise AES-128 en mode CBC avec HMAC pour l'intégrité. Il est idéal pour stocker des données chiffrées.

```python
from cryptography.fernet import Fernet

# Générer une clé (stockez-la de manière sécurisée, par exemple dans des variables d'environnement)
key = Fernet.generate_key()
cipher = Fernet(key)

# Chiffrer
plaintext = b"Ceci est un message secret."
token = cipher.encrypt(plaintext)
print("Chiffré :", token)

# Déchiffrer
decrypted = cipher.decrypt(token)
print("Déchiffré :", decrypted)
```
- **Notes** : Les clés sont en base64 sûre pour les URL (44 caractères). Ne codez jamais les clés en dur ; faites-les tourner périodiquement.

#### 2. Chiffrement asymétrique avec RSA
Générez une paire de clés publique/privée et chiffrez des données que seul le détenteur de la clé privée peut déchiffrer.

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Générer une clé privée
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Sérialiser pour le stockage
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()  # Utilisez BestAvailableEncryption() pour une protection par mot de passe
)

# Obtenir la clé publique et la sérialiser
public_key = private_key.public_key()
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Chiffrer avec la clé publique
plaintext = b"Message secret"
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

# Déchiffrer avec la clé privée
decrypted = private_key.decrypt(
    ciphertext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
print("Déchiffré :", decrypted)
```
- **Notes** : RSA est lent pour les grandes quantités de données ; utilisez-le pour l'échange de clés ou les petits messages. Le remplissage OAEP prévient les attaques.

#### 3. Génération et utilisation de hachages
Pour les vérifications d'intégrité ou le hachage de mots de passe.

```python
from cryptography.hazmat.primitives import hashes

# Hacher des données
digest = hashes.Hash(hashes.SHA256())
digest.update(b"Quelques données")
hash_result = digest.finalize()
print("Hachage SHA256 :", hash_result.hex())
```

Pour les mots de passe, utilisez `cryptography.hazmat.primitives.kdf.pbkdf2` pour la dérivation de clé (par exemple, PBKDF2 pour un hachage lent et salé).

#### 4. Signatures numériques avec RSA
Signez des données pour en prouver l'authenticité.

```python
# En utilisant les clés RSA de l'exemple précédent
message = b"Données à signer"
signature = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

# Vérifier avec la clé publique
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print("Signature valide")
except Exception:
    print("Signature invalide")
```

### Bonnes pratiques
- **Gestion des clés** : Stockez les clés de manière sécurisée (par exemple, en utilisant AWS KMS, des modules de sécurité matériels). Ne réutilisez jamais les clés.
- **Remplissage et modes** : Utilisez toujours un remplissage sécurisé (par exemple, OAEP pour RSA, GCM pour AES).
- **Aléatoire** : Utilisez `os.urandom()` ou le module `secrets` pour les graines ; évitez `random`.
- **Mises à jour** : La cryptographie évolue—vérifiez les vulnérabilités dans votre utilisation.
- **Évitez de créer votre propre solution** : Pour des besoins complexes, utilisez les recettes ou intégrez avec des bibliothèques de plus haut niveau comme `pyjwt` ou `boto3`.
- **Tests** : Utilisez les constantes et exceptions de la bibliothèque pour la gestion des erreurs.

### Pour aller plus loin
- [Documentation officielle](https://cryptography.io/en/latest/) – Référence API détaillée et tutoriels.
- [Page PyPI](https://pypi.org/project/cryptography/) – Historique des versions et intégrations.
- Pour les sujets avancés, explorez le wiki `cryptography` ou les RFC (par exemple, RFC 8017 pour PKCS#1).

Si vous avez un cas d'utilisation spécifique (par exemple, chiffrer des fichiers ou sécuriser une API), fournissez plus de détails pour des exemples adaptés.