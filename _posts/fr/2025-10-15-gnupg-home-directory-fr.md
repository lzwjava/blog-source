---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Contenu du répertoire personnel de GnuPG expliqué
translated: true
type: note
---

Ces fichiers et répertoires font partie de votre répertoire personnel GnuPG (GPG) (`~/.gnupg/`), qui stocke les clés cryptographiques et les données associées pour le chiffrement, la signature et l'authentification. GPG est un outil pour la communication sécurisée et la protection des données. Voici une explication de chacun, basée sur le comportement standard de GnuPG 2.1+ :

- **openpgp-revocs.d** : Un répertoire contenant les certificats de révocation (fichiers `.rev`) générés lorsque vous créez des paires de clés. Ils sont utilisés pour révoquer (invalider) vos clés si elles sont compromises ou ne sont plus nécessaires, empêchant ainsi toute utilisation ultérieure.

- **private-keys-v1.d** : Un répertoire stockant vos clés privées (secrètes) dans le format de clé moderne introduit dans GnuPG 2.1. Chaque clé se trouve dans son propre fichier pour une meilleure sécurité et gestion. Protégez-le absolument — c'est comme votre coffre-fort numérique.

- **pubring.kbx** : Le fichier du trousseau de clés publiques dans le nouveau format "keybox" (`.kbx`). Il contient les clés publiques que vous avez importées d'autres personnes, que vous utilisez pour leur chiffrer des messages ou vérifier leurs signatures.

- **pubring.kbx~** : Une copie de sauvegarde de `pubring.kbx`, créée automatiquement par GPG lors des modifications ou mises à jour. Le suffixe tilde (`~`) est une convention Linux courante pour les sauvegardes.

- **trustdb.gpg** : Le fichier de base de données de confiance, qui suit les niveaux de confiance que vous avez attribués aux clés publiques (par exemple, "ultimate" pour vos propres clés, ou des niveaux pour les autres basés sur les signatures). Il aide GPG à décider si une clé est fiable pour la validation.

Si vous avez récemment généré ou importé des clés, cette configuration est normale. Sauvegardez toujours l'intégralité de votre répertoire `~/.gnupg/` de manière sécurisée et ne partagez jamais les clés privées. Pour plus de détails, consultez la documentation officielle de GnuPG.

[Using the GNU Privacy Guard](https://www.gnupg.org/documentation/manuals/gnupg.pdf)
[GnuPG Part 2 - Create and Manage Keys](https://www.hacksanity.com/kb/gnupg-create-manage-keys/)
[How to Back Up and Restore Your GPG Keys on Linux](https://www.howtogeek.com/816878/how-to-back-up-and-restore-gpg-keys-on-linux/)
[GPG(1) Manual](https://www.gnupg.org/(en)/documentation/manuals/gnupg24/gpg.1.html)