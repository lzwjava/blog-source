---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Chiffrement de fichiers avec GPG
translated: true
type: note
---

### Chiffrer un fichier avec votre clé GPG

Votre liste de clés GPG montre une clé publique (pub) avec l'empreinte `982740390B5D33E90B6B6133892BC5A4789B71CD` associée à votre email `lzwjava@gmail.com`. Pour chiffrer un fichier en utilisant cette clé (afin que seul vous puissiez le déchiffrer avec votre clé privée), suivez ces étapes dans votre terminal :

1. **Accédez au répertoire** contenant le fichier que vous voulez chiffrer (par exemple, si votre fichier est `secret.txt`) :
   ```
   cd ~/path/to/your/file
   ```

2. **Chiffrez le fichier** en utilisant l'option `--encrypt` et spécifiez le destinataire (votre email ou l'ID de clé). Cela crée un fichier `.gpg` chiffré.
   
   - En utilisant votre email (plus simple) :
     ```
     gpg --encrypt --recipient lzwjava@gmail.com secret.txt
     ```
   
   - En utilisant l'ID de clé (empreinte complète) :
     ```
     gpg --encrypt --recipient 982740390B5D33E90B6B6133892BC5A4789B71CD secret.txt
     ```
   
   Cela génère `secret.txt.gpg`, qui est la version chiffrée. Le fichier original `secret.txt` reste inchangé.

3. **Vérifiez le chiffrement** (optionnel) :
   ```
   gpg --list-packets secret.txt.gpg
   ```
   Cela affiche les détails du paquet chiffré.

### Déchiffrer le fichier (pour référence ultérieure)

Pour le déchiffrer (uniquement possible avec votre clé privée et votre phrase de passe) :
```
gpg --decrypt secret.txt.gpg > secret.txt.decrypted
```
Saisissez votre phrase de passe lorsqu'elle est demandée.

### Conseils
- **Chiffrement symétrique** (si vous n'avez pas besoin d'une clé de destinataire, seulement d'une phrase de passe) : Utilisez `gpg -c secret.txt` à la place.
- **Chiffrer et signer** (pour prouver que le fichier vient de vous) : Ajoutez `--sign` à la commande de chiffrement, par exemple `gpg --encrypt --sign --recipient lzwjava@gmail.com secret.txt`.
- Si vous rencontrez des erreurs (par exemple, clé non approuvée), exécutez `gpg --edit-key lzwjava@gmail.com` et utilisez `trust` pour la définir sur ultimate.
- Sauvegardez toujours votre répertoire `~/.gnupg` pour la sécurité de vos clés.

Pour plus de détails, consultez le manuel GPG : [Documentation GPG](https://www.gnupg.org/documentation/manpage.html).