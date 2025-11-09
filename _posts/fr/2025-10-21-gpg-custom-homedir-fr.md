---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Utilisation de GPG avec un répertoire personnel personnalisé
translated: true
type: note
---

### Utilisation de l'option `--homedir` de GPG

L'option `--homedir` (note : c'est `--homedir`, pas `--home-dir` — GPG utilise un seul mot) indique à GPG d'utiliser un répertoire personnalisé comme « home » pour stocker les fichiers de configuration, les porte-clés, les bases de données de confiance et autres données. Par défaut, GPG utilise `~/.gnupg` (par exemple, `/c/Users/VotreNom/.gnupg` dans Git Bash sur Windows). Cette option est utile pour :
- Isoler plusieurs configurations GPG (par exemple, une pour les clés personnelles, une autre pour le travail).
- Tester ou éviter les conflits avec les configurations GPG système.
- Exécuter GPG dans un environnement portable ou personnalisé.

#### Syntaxe de base
```
gpg --homedir /chemin/vers/repertoire/personnalise [autres commandes gpg]
```
- Remplacez `/chemin/vers/repertoire/personnalise` par le chemin de répertoire de votre choix.
- Dans Git Bash sur Windows, **utilisez toujours des barres obliques (`/`)** pour les chemins, même pour les lecteurs Windows (par exemple, `/c/Users/VotreNom/mon-repertoire-gpg`).
- Le répertoire doit exister ; GPG ne le créera pas automatiquement. Créez-le d'abord avec `mkdir -p /chemin/vers/repertoire/personnalise`.

#### Exemple : Configuration et utilisation d'un répertoire home personnalisé
1. **Créer le répertoire personnalisé** (dans Git Bash) :
   ```
   mkdir -p /c/Users/VotreNom/mon-gpg-personnalise
   ```

2. **Générer une paire de clés en utilisant le homedir personnalisé** :
   ```
   gpg --homedir /c/Users/VotreNom/mon-gpg-personnalise --full-generate-key
   ```
   - Ceci stocke vos clés et votre configuration dans `mon-gpg-personnalise`, et non dans le répertoire par défaut.

3. **Lister les clés de ce répertoire** :
   ```
   gpg --homedir /c/Users/VotreNom/mon-gpg-personnalise --list-secret-keys --keyid-format LONG
   ```

4. **Chiffrer un fichier en utilisant les clés du répertoire personnalisé** :
   ```
   gpg --homedir /c/Users/VotreNom/mon-gpg-personnalise --encrypt --recipient ADRESSE_EMAIL_DU_DESTINATAIRE secret.txt
   ```

5. **Déchiffrer un fichier** :
   ```
   gpg --homedir /c/Users/VotreNom/mon-gpg-personnalise --output decrypted.txt --decrypt secret.txt.gpg
   ```

#### Conseils pour Git Bash sur Windows
- **Chemins :** Utilisez toujours `/` — par exemple, évitez `\` ou les barres mixtes, car elles peuvent faire échouer les commandes.
- **Permissions :** Assurez-vous que le répertoire personnalisé a les droits de lecture/écriture (utilisez `chmod 700 /chemin/vers/repertoire/personnalise` pour la sécurité, comme le `.gnupg` par défaut).
- **Alternative par variable d'environnement :** Au lieu d'utiliser `--homedir` à chaque fois, définissez `export GNUPGHOME=/c/Users/VotreNom/mon-gpg-personnalise` dans votre `.bashrc` (exécutez `source ~/.bashrc` après modification). Ensuite, GPG l'utilisera automatiquement.
- **Intégration avec Git :** Si vous l'utilisez pour la signature Git, configurez-le avec l'option :
  ```
  git config --global gpg.program "gpg --homedir /c/Users/VotreNom/mon-gpg-personnalise"
  ```
- **Problèmes courants :** Si GPG signale des fichiers manquants, il peut avoir besoin d'une initialisation — exécutez d'abord `gpg --homedir /chemin --gen-key`. Sur Windows, évitez les chemins avec des espaces, à moins qu'ils ne soient entre guillemets.

Pour plus de détails, consultez le manuel GPG : [GnuPG Documentation](https://www.gnupg.org/documentation/manuals/gnupg/)