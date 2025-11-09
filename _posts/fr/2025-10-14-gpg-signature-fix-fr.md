---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Corriger les erreurs de vérification de signature GPG
translated: true
type: note
---

### Comprendre l'erreur

L'erreur que vous voyez se produit car la commande `gpg --verify` attend généralement deux arguments : le **fichier de signature** (par exemple `zhs.tw.yaml.sig` ou `zhs.tw.yaml.asc`) en **premier**, suivi du **fichier réel** à vérifier (par exemple `zhs.tw.yaml`).

Dans votre commande :
```
gpg --verify zhs.tw.yaml
```
GPG essaie d'interpréter `zhs.tw.yaml` à la fois comme la signature *et* le fichier de données, mais il ne contient pas de données de signature OpenPGP valides (les fichiers YAML ne sont pas des signatures). D'où le message "no valid OpenPGP data found".

### Comment corriger l'erreur

1. **Localiser le fichier de signature** : Vous avez besoin du fichier de signature détachée qui correspond à votre YAML. Il est généralement nommé ainsi :
   - `zhs.tw.yaml.sig` (format binaire)
   - `zhs.tw.yaml.asc` (format ASCII armoré)

   Si vous ne l'avez pas, vous devrez le télécharger depuis la source où vous avez obtenu `zhs.tw.yaml` (par exemple, un dépôt de projet ou un site web).

2. **Exécuter la commande correcte** : Une fois que vous avez la signature, utilisez ce format :
   ```
   gpg --verify zhs.tw.yaml.sig zhs.tw.yaml
   ```
   - Remplacez `.sig` par `.asc` si c'est le format de votre fichier.
   - L'ordre est important : la signature d'abord, puis le fichier.

3. **Résultat attendu en cas de succès** :
   Si la signature est valide et que vous faites confiance à la clé, vous verrez quelque chose comme :
   ```
   gpg: Signature faite le [date] en utilisant [type de clé]
   gpg: Bonne signature de « [nom/email du signataire] »
   ```
   Si elle est invalide ou si la clé n'est pas approuvée, vous obtiendrez des avertissements/erreurs.

### Conseils supplémentaires

- **Importer la clé publique** : Si GPG signale une clé inconnue, récupérez et importez la clé publique du signataire :
  ```
  gpg --keyserver keyserver.ubuntu.com --recv-keys [ID_CLÉ]
  ```
  (Remplacez `[ID_CLÉ]` par l'empreinte réelle de la clé provenant de la sortie d'erreur ou de la documentation du projet.)

- **Mode batch pour les scripts** : Si vous automatisez cette opération, ajoutez `--batch` pour supprimer les invites :
  ```
  gpg --batch --verify zhs.tw.yaml.sig zhs.tw.yaml
  ```

- **Signatures intégrées** : Si la signature est *intégrée* dans le YAML (peu probable pour un fichier `.yaml`), vous devriez simplement exécuter `gpg --verify zhs.tw.yaml` après vous être assuré que le fichier se termine par `-----END PGP SIGNATURE-----`. Mais selon l'erreur, il s'agit probablement d'une signature détachée.

Si cela ne résout pas le problème ou si vous partagez plus de détails (par exemple, la provenance du fichier), je peux affiner les conseils !

[Manuel de GNU Privacy Guard](https://www.gnupg.org/documentation/manpage.html)