---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Correction des chemins du répertoire GPG sur Windows
translated: true
type: note
---

Oui, vous avez raison. Dans Git Bash sur Windows (qui s'exécute dans un environnement de type MSYS2/Cygwin), l'utilisation de barres obliques inverses (`\`) dans le chemin `--homedir` pour `gpg` amène le shell à interpréter incorrectement l'argument en raison du fonctionnement des échappements et des conversions de chemin. Cela altère le chemin (par exemple, `C:\Users\me\.gnupg` pourrait devenir quelque chose d'invalide comme `C:Usersme.gnupg` ou être encore plus déformé lors de la conversion automatique au format Windows), rendant le répertoire introuvable. Par conséquent, GPG ne peut pas localiser les fichiers de clés, ce qui entraîne une erreur "no secret key" (ou similaire, comme "No such file or directory" pour `pubring.kbx`).

### Solution Rapide
- Utilisez des barres obliques (`/`) avec le préfixe de lecteur de style MSYS2 : `gpg --homedir /c/Users/me/.gnupg ...`
- Cela est automatiquement converti par MSYS2 en chemin Windows correct (par exemple, `C:\Users\me\.gnupg`) lorsqu'il est transmis au binaire natif de GPG.
- Évitez les lettres de lecteur comme `c:/` sans le `/` initial — elles sont traitées comme des chemins relatifs, ajoutant votre répertoire de travail actuel et provoquant le même échec de recherche.

Pour les variables d'environnement comme `GNUPGHOME`, la même règle s'applique : définissez-les avec `/` (par exemple, `export GNUPGHOME=/c/Users/me/.gnupg`).

[MSYS2 Filesystem Paths](https://www.msys2.org/docs/filesystem-paths/)  
[GNUPGHOME in MSYS2 Discussion](https://lists.gnupg.org/pipermail/gnupg-users/2025-February/067536.html)  
[GPG --homedir Bug on Windows/MSYS2](https://www.reddit.com/r/GnuPG/comments/1cl4dw8/bug_windows_homedir_with_drive_letter_treated_as/)