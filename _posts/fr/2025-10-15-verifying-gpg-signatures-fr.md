---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Vérification des signatures numériques GPG
translated: true
type: note
---

### Vérification des signatures avec GPG

GnuPG (GPG) vous permet de vérifier les signatures numériques pour vous assurer qu'un fichier ou un message n'a pas été altéré et provient bien de l'expéditeur déclaré. La vérification nécessite que la clé publique du signataire se trouve dans votre trousseau. Voici les étapes et les commandes pour les scénarios courants.

#### Prérequis
1. **Installer GPG** : Assurez-vous que GnuPG est installé sur votre système (par exemple, via `apt install gnupg` sur les systèmes basés sur Debian ou `brew install gnupg` sur macOS).
2. **Importer la clé publique du signataire** : Vous avez besoin de la clé publique de la personne ou de l'entité qui a signé le fichier. Téléchargez-la depuis un serveur de clés ou un fichier, puis importez-la :
   ```
   gpg --import public-key.asc
   ```
   (Remplacez `public-key.asc` par le fichier de clé réel. S'il provient d'un serveur de clés, utilisez `gpg --keyserver keyserver.ubuntu.com --recv-keys KEYID` où `KEYID` est l'empreinte ou l'ID de la clé.)

#### Étapes de vérification
La commande exacte dépend de la façon dont la signature a été créée (par exemple, intégrée dans le fichier ou détachée).

1. **Vérifier une signature détachée** (courant pour les fichiers comme les versions logicielles ; la signature se trouve dans un fichier `.sig` séparé) :
   ```
   gpg --verify signature.sig fichier-original
   ```
   - Exemple de sortie pour une bonne signature :
     ```
     gpg: Signature faite le [date] en utilisant la clé [type de clé] ID [KEYID]
     gpg: Bonne signature de « [Nom] <email@example.com> »
     ```
   - Si la clé n'est pas de confiance, vous pouvez voir un avertissement comme « Cette clé n'est pas certifiée avec une signature de confiance ! ». Vous pouvez ajuster les niveaux de confiance avec `gpg --edit-key KEYID` puis `trust`.

2. **Vérifier un fichier signé en ligne** (la signature est intégrée au fichier, souvent en binaire) :
   - Pour vérifier uniquement la signature :
     ```
     gpg --verify fichier-signé
     ```
   - Pour vérifier et extraire le contenu original :
     ```
     gpg --output fichier-original --decrypt fichier-signé
     ```
     Cela demandera une phrase secrète si le fichier est chiffré, mais pour les signatures seules, il se contente de vérifier.

3. **Vérifier un message en clair signé** (texte lisible par l'homme avec une signature ASCII armorée, courant dans les e-mails ou les README) :
   ```
   gpg --verify fichier-signe-en-clair.txt
   ```
   La sortie montrera le statut de la signature sans altérer le fichier.

#### Dépannage
- **Erreur « Aucune clé publique »** : Importez la clé comme indiqué ci-dessus.
- **Mauvaise signature** : Le fichier a peut-être été modifié — retéléchargez-le.
- **Validité de la clé** : Vérifiez les détails de la clé avec `gpg --list-keys` ou vérifiez que les empreintes correspondent à la source officielle.
- Pour une vérification par lots ou des scripts, ajoutez `--batch --exit-on-status-write-error`.

Pour plus de détails sur la signature ou les options avancées, consultez le manuel officiel.

[Créer et vérifier des signatures - Manuel GnuPG](https://www.gnupg.org/gph/en/manual/x135.html)