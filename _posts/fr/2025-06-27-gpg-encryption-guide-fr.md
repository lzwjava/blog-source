---
audio: false
generated: true
lang: fr
layout: post
title: 'Comprendre GPG : un outil de communication sécurisé'
translated: true
type: note
---

## Qu'est-ce que GPG ?
GPG, ou GNU Privacy Guard, est une implémentation open source de la norme OpenPGP (Pretty Good Privacy). C'est un outil de communication sécurisée, fournissant le chiffrement, le déchiffrement, les signatures numériques et la gestion des clés. GPG est largement utilisé pour sécuriser les emails, les fichiers et d'autres données, garantissant la confidentialité, l'intégrité et l'authenticité.

GPG est disponible sur la plupart des systèmes d'exploitation, y compris Linux, macOS et Windows. Il est basé sur une interface en ligne de commande mais peut être intégré à des outils graphiques ou à des clients de messagerie comme Thunderbird.

---

## Fonctionnement de GPG
GPG utilise une combinaison de **cryptographie à clé symétrique** et de **cryptographie à clé publique** pour sécuriser les données :

1. **Cryptographie à clé symétrique** :
   - Utilise une seule clé pour le chiffrement et le déchiffrement.
   - GPG utilise des algorithmes à clé symétrique (par exemple, AES) pour chiffrer les données réelles car ils sont plus rapides pour les grands ensembles de données.
   - Une clé de session aléatoire est générée pour chaque opération de chiffrement.

2. **Cryptographie à clé publique** :
   - Utilise une paire de clés : une **clé publique** pour le chiffrement et une **clé privée** pour le déchiffrement.
   - GPG prend en charge des algorithmes comme RSA ou ECDSA pour les paires de clés.
   - La clé publique chiffre la clé de session, qui est ensuite utilisée pour chiffrer les données. Le destinataire utilise sa clé privée pour déchiffrer la clé de session, qui est ensuite utilisée pour déchiffrer les données.

3. **Signatures numériques** :
   - GPG permet aux utilisateurs de signer des données à l'aide de leur clé privée pour en prouver l'authenticité et l'intégrité.
   - Le destinataire vérifie la signature à l'aide de la clé publique de l'expéditeur.

4. **Gestion des clés** :
   - GPG gère les clés dans un porte-clés (keyring), qui stocke les clés publiques et privées.
   - Les clés peuvent être générées, importées, exportées et publiées sur des serveurs de clés.

### Processus de chiffrement GPG
Lors du chiffrement d'un fichier ou d'un message :
1. GPG génère une **clé de session** aléatoire pour le chiffrement symétrique.
2. Les données sont chiffrées avec la clé de session à l'aide d'un algorithme symétrique (par exemple, AES-256).
3. La clé de session est chiffrée avec la **clé publique** du destinataire à l'aide d'un algorithme asymétrique (par exemple, RSA).
4. La clé de session chiffrée et les données chiffrées sont combinées en un seul fichier ou message de sortie.

Lors du déchiffrement :
1. Le destinataire utilise sa **clé privée** pour déchiffrer la clé de session.
2. La clé de session est utilisée pour déchiffrer les données avec l'algorithme symétrique.

Cette approche hybride combine la vitesse du chiffrement symétrique avec la sécurité du chiffrement asymétrique.

---

## Installation de GPG
GPG est préinstallé sur de nombreuses distributions Linux. Pour les autres systèmes :
- **Linux** : Installez via le gestionnaire de paquets :
  ```bash
  sudo apt install gnupg  # Debian/Ubuntu
  sudo yum install gnupg  # CentOS/RHEL
  ```
- **macOS** : Installez via Homebrew :
  ```bash
  brew install gnupg
  ```
- **Windows** : Téléchargez Gpg4win depuis [gpg4win.org](https://gpg4win.org/).

Vérifiez l'installation :
```bash
gpg --version
```

---

## Génération de clés GPG
Pour utiliser GPG, vous avez besoin d'une paire de clés (clé publique et clé privée).

### Génération de clés étape par étape
Exécutez la commande suivante pour générer une paire de clés :
```bash
gpg --full-generate-key
```

1. **Choisir le type de clé** :
   - Le type par défaut est RSA et RSA (option 1).
   - RSA est largement utilisé et sécurisé pour la plupart des usages.

2. **Taille de la clé** :
   - Recommandé : 2048 ou 4096 bits (4096 est plus sécurisé mais plus lent).
   - Exemple : Sélectionnez 4096.

3. **Expiration de la clé** :
   - Choisissez une date d'expiration (par exemple, 1 an) ou sélectionnez 0 pour aucune expiration.
   - Les clés avec expiration améliorent la sécurité en limitant la durée de vie de la clé.

4. **Identifiant utilisateur** :
   - Entrez votre nom, votre email et un commentaire optionnel.
   - Exemple : `John Doe <john.doe@example.com>`.

5. **Phrase de passe** :
   - Définissez une phrase de passe robuste pour protéger la clé privée.
   - Cette phrase de passe est requise pour le déchiffrement et la signature.

Exemple de sortie après l'exécution de la commande :
```
gpg: key 0x1234567890ABCDEF marked as ultimately trusted
gpg: generated key pair
```

### Exportation des clés
- **Exporter la clé publique** :
  ```bash
  gpg --armor --output public-key.asc --export john.doe@example.com
  ```
  Cela crée un fichier (`public-key.asc`) contenant votre clé publique au format ASCII.

- **Exporter la clé privée** (soyez prudent, gardez-la sécurisée) :
  ```bash
  gpg --armor --output private-key.asc --export-secret-keys john.doe@example.com
  ```

---

## Chiffrement et déchiffrement de fichiers
### Chiffrement d'un fichier
Pour chiffrer un fichier pour un destinataire :
1. Assurez-vous d'avoir la clé publique du destinataire dans votre porte-clés :
   ```bash
   gpg --import recipient-public-key.asc
   ```
2. Chiffrez le fichier :
   ```bash
   gpg --encrypt --recipient john.doe@example.com --output encrypted-file.gpg input-file.txt
   ```
   - `--recipient` : Spécifie l'email ou l'ID de clé du destinataire.
   - `--output` : Spécifie le fichier de sortie.
   - Le résultat est `encrypted-file.gpg`, que seul le destinataire peut déchiffrer.

### Déchiffrement d'un fichier
Pour déchiffrer un fichier chiffré pour vous :
```bash
gpg --decrypt --output decrypted-file.txt encrypted-file.gpg
```
- Entrez votre phrase de passe lorsque vous y êtes invité.
- Le contenu déchiffré est enregistré dans `decrypted-file.txt`.

---

## Signature et vérification de données
### Signature d'un fichier
La signature prouve l'authenticité et l'intégrité des données.
- **Signature en clair** (inclut une signature lisible par l'homme) :
  ```bash
  gpg --clearsign input-file.txt
  ```
  Sortie : `input-file.txt.asc` avec le contenu du fichier et la signature.

- **Signature détachée** (fichier de signature séparé) :
  ```bash
  gpg --detach-sign input-file.txt
  ```
  Sortie : `input-file.txt.sig`.

### Vérification d'une signature
Pour vérifier un fichier signé :
```bash
gpg --verify input-file.txt.asc
```
Pour une signature détachée :
```bash
gpg --verify input-file.txt.sig input-file.txt
```
Vous avez besoin de la clé publique du signataire dans votre porte-clés.

---

## Génération de mots de passe avec GPG
GPG peut générer des données aléatoires, qui peuvent être utilisées pour créer des mots de passe sécurisés. Bien que GPG ne soit pas principalement un générateur de mots de passe, sa génération de nombres aléatoires est cryptographiquement sécurisée.

### Commande pour générer un mot de passe
```bash
gpg --gen-random --armor 1 32
```
- `--gen-random` : Génère des octets aléatoires.
- `--armor` : Produit la sortie au format ASCII.
- `1` : Niveau de qualité (1 est adapté pour un usage cryptographique).
- `32` : Nombre d'octets (ajustez pour la longueur de mot de passe souhaitée).

Exemple de sortie :
```
4eX9j2kPqW8mZ3rT5vY7nL9xF2bC6dA8
```
Pour le rendre plus semblable à un mot de passe, vous pouvez le rediriger vers un convertisseur base64 ou hexadécimal, ou le tronquer à la longueur souhaitée.

### Exemple : Générer un mot de passe de 20 caractères
```bash
gpg --gen-random --armor 1 15 | head -c 20
```
Cela génère une chaîne aléatoire de 20 caractères.

---

## Gestion des clés
### Lister les clés
- Lister les clés publiques :
  ```bash
  gpg --list-keys
  ```
- Lister les clés privées :
  ```bash
  gpg --list-secret-keys
  ```

### Publication des clés publiques
Partagez votre clé publique via un serveur de clés :
```bash
gpg --keyserver hkps://keys.openpgp.org --send-keys 0x1234567890ABCDEF
```
Remplacez `0x1234567890ABCDEF` par votre ID de clé.

### Importation de clés
Importez une clé publique depuis un fichier :
```bash
gpg --import public-key.asc
```
Ou depuis un serveur de clés :
```bash
gpg --keyserver hkps://keys.openpgp.org --recv-keys 0x1234567890ABCDEF
```

### Révoquer une clé
Si une clé est compromise ou expire :
1. Générez un certificat de révocation (faites-le lors de la création de la clé) :
   ```bash
   gpg --output revoke.asc --gen-revoke john.doe@example.com
   ```
2. Importez et publiez la révocation :
   ```bash
   gpg --import revoke.asc
   gpg --keyserver hkps://keys.openpgp.org --send-keys john.doe@example.com
   ```

---

## Bonnes pratiques
1. **Sauvegardez les clés** :
   - Stockez les clés privées et les certificats de révocation en lieu sûr (par exemple, sur une clé USB chiffrée).
   - Ne partagez jamais les clés privées.

2. **Utilisez des phrases de passe robustes** :
   - Utilisez une phrase de passe longue et unique pour votre clé privée.

3. **Mettez à jour régulièrement les clés** :
   - Définissez une date d'expiration et renouvelez les clés périodiquement.

4. **Vérifiez les empreintes de clés** :
   - Avant de faire confiance à une clé publique, vérifiez son empreinte avec son propriétaire :
     ```bash
     gpg --fingerprint john.doe@example.com
     ```

5. **Utilisez les serveurs de clés de manière sécurisée** :
   - Utilisez des serveurs de clés de confiance comme `hkps://keys.openpgp.org`.

6. **Signez uniquement les clés de confiance** :
   - Lorsque vous signez la clé de quelqu'un d'autre, vérifiez son identité en personne ou via un canal de confiance.

---

## Résumé des commandes GPG courantes
Voici un aide-mémoire pour les commandes GPG courantes :
- Générer une paire de clés : `gpg --full-generate-key`
- Chiffrer un fichier : `gpg --encrypt --recipient <email> --output <output.gpg> <input.txt>`
- Déchiffrer un fichier : `gpg --decrypt --output <output.txt> <input.gpg>`
- Signer un fichier : `gpg --clearsign <input.txt>` ou `gpg --detach-sign <input.txt>`
- Vérifier une signature : `gpg --verify <file.asc>` ou `gpg --verify <file.sig> <file>`
- Exporter une clé publique : `gpg --armor --output public-key.asc --export <email>`
- Importer une clé : `gpg --import <key.asc>`
- Générer un mot de passe aléatoire : `gpg --gen-random --armor 1 <bytes>`

---

## Dépannage
- **Erreur "No secret key"** : Assurez-vous que la clé privée est dans votre porte-clés (`gpg --list-secret-keys`) et qu'elle correspond à la clé publique du destinataire.
- **Phrase de passe oubliée** : Si vous perdez votre phrase de passe, vous devez révoquer la clé et en générer une nouvelle.
- **Clé non trouvée** : Importez la clé publique du destinataire ou vérifiez le serveur de clés.
- **Problèmes de version GPG** : Assurez-vous que toutes les parties utilisent des versions compatibles de GPG (vérifiez avec `gpg --version`).

---

## Fonctionnalités avancées
1. **Intégration avec l'email** :
   - Utilisez GPG avec des clients de messagerie comme Thunderbird via des plugins (par exemple, Enigmail ou la partie OpenPGP intégrée).