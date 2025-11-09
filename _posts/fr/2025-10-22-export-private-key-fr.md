---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Exportation d’une clé privée GPG
translated: true
type: note
---

### Exporter une clé privée GPG depuis le serveur

Pour exporter votre clé privée, vous devez avoir accès au serveur via SSH ou un terminal. Les clés privées GPG sont sensibles — manipulez-les de manière sécurisée et supprimez le fichier exporté après le transfert.

1. **Lister vos clés secrètes** (pour identifier la clé par email ou ID de clé) :  
   ```
   gpg --list-secret-keys
   ```  
   Recherchez l'entrée du type `sec   rsa4096/ABC123DEF456 2023-01-01 [SC]`. Notez l'email ou l'ID de clé (par exemple, `user@example.com` ou `ABC123DEF456`).

2. **Exporter la clé privée** (utilisez `--armor` pour le format ASCII, plus facile à transférer) :  
   ```
   gpg --export-secret-keys --armor user@example.com > private-key.asc
   ```  
   - Remplacez `user@example.com` par votre véritable email ou ID de clé.  
   - Cela crée le fichier `private-key.asc` dans votre répertoire actuel.  
   - Si vous avez plusieurs clés, spécifiez l'ID de clé pour plus de précision : `gpg --export-secret-keys --armor ABC123DEF456 > private-key.asc`.  
   - **Note de sécurité** : Cette commande exporte la clé *sans* sa phrase de passe. Vous devrez saisir la phrase de passe lors de l'importation si vous y êtes invité.

3. **Transférer le fichier de manière sécurisée** vers votre ordinateur portable local :  
   - Utilisez `scp` (depuis votre machine locale) :  
     ```
     scp user@server-ip:/path/to/private-key.asc ./
     ```  
     Remplacez `user@server-ip` par les détails de votre serveur et `/path/to/` par le chemin réel.  
   - Alternatives : `rsync` pour les fichiers volumineux ou SFTP pour une option graphique. Évitez les emails ou les canaux non sécurisés.

4. **Nettoyer sur le serveur** :  
   ```
   rm private-key.asc
   ```  
   Vérifiez sa suppression avec `ls`.

### Importer la clé privée GPG sur votre ordinateur portable local

En supposant que vous ayez GPG installé (par exemple, via `apt install gnupg` sur Linux, `brew install gnupg` sur macOS, ou Chocolatey sur Windows).

1. **Importer la clé** :  
   ```
   gpg --import private-key.asc
   ```  
   - Vous verrez une sortie comme "gpg: key ABC123DEF456: secret key imported".  
   - Si vous êtes invité à saisir une phrase de passe lors de l'importation, entrez la phrase de passe d'origine.

2. **Vérifier l'importation** :  
   ```
   gpg --list-secret-keys
   ```  
   Votre clé devrait maintenant apparaître sous "sec".

3. **Optionnel : Définir le niveau de confiance** (si vous l'utilisez pour la signature/email) :  
   ```
   gpg --edit-key user@example.com
   ```  
   - Dans l'invite, tapez `trust`, sélectionnez "ultimate" (option 5), puis `save` et `quit`.  
   - Cela marque la clé comme entièrement fiable sur votre machine locale.

### Conseils et Avertissements
- **Phrase de passe** : Utilisez toujours une phrase de passe robuste. Si vous l'oubliez, la clé devient inutilisable.
- **Sous-clés** : Si votre clé a des sous-clés (par exemple, pour le chiffrement), exportez-les également avec `--export-secret-subkeys`.
- **Sauvegarde** : Stockez les exports dans un coffre-fort sécurisé (par exemple, un disque chiffré).
- **Versions** : Testé sur GPG 2.x ; fonctionne de manière similaire sur 1.x.
- Pour plus de détails, consultez la documentation officielle de GPG : [GnuPG Manual](https://www.gnupg.org/documentation/manuals/gnupg/).