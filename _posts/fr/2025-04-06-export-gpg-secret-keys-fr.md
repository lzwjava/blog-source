---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Exportation sécurisée des clés secrètes GPG
translated: true
type: note
---

### Exportation de clés secrètes avec GPG en format blindé

GPG (GNU Privacy Guard) permet d'exporter les clés secrètes (privées) dans un format ASCII blindé, qui les enregistre dans un fichier `.asc` lisible par un humain (et non binaire). Ceci est utile pour les sauvegardes, les transferts ou l'importation sur une autre machine.

**Avertissement important :** Les clés secrètes contiennent des informations sensibles. Exportez-les uniquement lorsque c'est nécessaire, chiffrez le fichier de sortie si vous le stockez ou le transmettez, et supprimez l'exportation après usage pour éviter toute fuite involontaire. Ne partagez jamais vos clés secrètes publiquement.

#### Structure de base de la commande
Pour exporter une clé secrète pour un identifiant utilisateur spécifique (e-mail ou nom associé à la clé), utilisez :

```
gpg --export-secret-keys --armor [KEY_ID] > filename.asc
```

- `KEY_ID` : L'empreinte de la clé, l'ID court, l'e-mail ou le nom. Vous pouvez lister vos clés avec `gpg --list-secret-keys`.
- `--armor` : Produit la sortie en format blindé (ASCII) au lieu du format binaire.
- `> filename.asc` : Redirige la sortie vers un fichier (par exemple, `my_secret_key.asc`). Omettez cette partie pour afficher le résultat dans le terminal.

#### Exemple d'utilisation étape par étape
1. **Lister vos clés secrètes** pour trouver le KEY_ID :
   ```
   gpg --list-secret-keys
   ```
   Exemple de sortie :
   ```
   sec   rsa3072/ABC12345 2023-01-01 [SC] [expires: 2025-01-01]
         Key fingerprint = 1234 5678 ABCD EF01 2345 6789 ABCD EF01 2345 6789
   uid                 [ultimate] Votre Nom <votre@email.com>
   ```

   Ici, `ABC12345` est l'ID court de la clé, ou utilisez l'empreinte complète `ABCDEF0123456789ABCDEF0123456789` pour plus de précision.

2. **Exporter la clé secrète** :
   ```
   gpg --export-secret-keys --armor ABC12345 > my_secret_key.asc
   ```

3. **Vérifier l'exportation** (optionnel) :
   ```
   cat my_secret_key.asc
   ```
   Le fichier doit commencer par `-----BEGIN PGP PRIVATE KEY BLOCK-----` et se terminer par `-----END PGP PRIVATE KEY BLOCK-----`.

#### Options supplémentaires
- **Exporter toutes les clés secrètes** : Omettez le KEY_ID pour tout exporter :
  ```
  gpg --export-secret-keys --armor > all_secret_keys.asc
  ```
- **Avec protection par phrase de passe** : GPG demandera votre phrase de passe si la clé est chiffrée (comportement par défaut).
- **Si vous avez besoin des clés publiques uniquement** : Utilisez `--export` (pour les clés publiques seulement).

Pour la documentation complète, reportez-vous à la page de manuel de GPG : `man gpg`. Si vous débutez avec GPG, générez d'abord une clé avec `gpg --gen-key`.