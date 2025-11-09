---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Répertoire personnel GPG avec barres obliques
translated: true
type: note
---

### Séparateurs de chemins pour `--homedir` de GPG dans Git Bash (Windows)

Dans Git Bash sur Windows, **utilisez toujours des barres obliques (`/`)** pour le chemin `--homedir`. Git Bash est un environnement de type Unix (basé sur MSYS2), il attend donc des chemins de style POSIX avec `/` comme séparateur. Les barres obliques inverses (`\`) vont probablement causer des erreurs, car GPG dans ce contexte ne les gère pas nativement sans échappement, ce qui est une complication inutile.

#### Pourquoi `/` ?
- Git Bash mappe les lecteurs Windows vers une structure de type Unix : `C:\Users\VotreNom` devient `/c/Users/VotreNom`.
- GPG (inclus avec Git pour Windows) suit la même convention. Utiliser `\` peut entraîner des échecs de résolution de chemin ou nécessiter un double échappement (par exemple, `\\`), ce qui est source d'erreurs.
- Les exemples officiels et les configurations communautaires (par exemple, pour la signature Git) utilisent systématiquement `/` dans Git Bash.

#### Exemple d'utilisation
```
gpg --homedir /c/Users/VotreNom/.gnupg --list-secret-keys
```
- Ceci pointe vers votre répertoire GPG par défaut sur le lecteur C:.
- Pour un répertoire personnalisé : `gpg --homedir /d/MyCustomGpgDir --full-generate-key` (lecteur D:).

#### Test rapide
Dans Git Bash :
1. Exécutez `pwd` — cela affichera quelque chose comme `/c/Users/VotreNom` (uniquement des `/`).
2. Essayez `gpg --homedir /c/Users/VotreNom/.gnupg --version` (fonctionne).
3. Comparez avec `\` : `gpg --homedir C:\Users\VotreNom\.gnupg --version` (échoue ou génère un avertissement).

Si vous utilisez également Windows CMD/PowerShell, ceux-ci acceptent à la fois `/` et `\`, mais utilisez `/` dans Git Bash pour rester cohérent. Pour en savoir plus, consultez le [Manuel GnuPG sur les Options de Configuration](https://www.gnupg.org/documentation/manuals/gnupg/Configuration-Options.html).