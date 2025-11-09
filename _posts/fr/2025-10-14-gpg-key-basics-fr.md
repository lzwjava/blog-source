---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Principes de base de la gestion des clés GPG
translated: true
type: note
---

## Introduction à la gestion des clés GPG

GPG (GNU Privacy Guard) est une implémentation libre du standard OpenPGP pour la communication sécurisée, utilisée pour chiffrer, signer et vérifier des données. Son cœur repose sur la **cryptographie à clé publique**, où chaque utilisateur possède une **clé publique** (partagée ouvertement pour le chiffrement et la vérification) et une **clé privée** (conservée secrète pour le déchiffrement et la signature). La gestion des clés implique la création, la distribution, la maintenance et la sécurisation de ces clés pour empêcher la falsification, la compromission ou l'utilisation abusive. Une mauvaise gestion peut entraîner des attaques comme la substitution de clé, où un attaquant remplace votre clé par la sienne pour intercepter les communications.

Le modèle de "toile de confiance" dans GPG permet aux utilisateurs de certifier mutuellement leurs clés, construisant un réseau d'identités vérifiées. Les clés sont stockées dans des **porte-clés** (fichiers publics et privés, par exemple `pubring.kbx` et `secring.gpg` dans les anciennes versions, ou unifiés dans les nouvelles). Sauvegardez toujours vos clés privées et utilisez des phrases de passe robustes.

## Structure d'une clé

Une paire de clés GPG n'est pas une seule clé — c'est un ensemble :
- **Clé primaire** : Une clé maîtresse de signature (par exemple, RSA ou DSA) utilisée pour certifier (signer) d'autres clés et pour auto-signer les composants de votre clé.
- **Sous-clés** : Clés subordonnées optionnelles pour des tâches spécifiques :
  - Sous-clé de signature : Pour signer les messages.
  - Sous-clé de chiffrement : Pour chiffrer les données (souvent changée périodiquement).
  - Sous-clé d'authentification : Pour SSH ou similaire.
- **Identifiants utilisateur (UID)** : Chaînes de caractères comme "Alice (Commentaire) <alice@example.com>" liant la clé à une identité réelle. Plusieurs UID peuvent exister pour différents rôles.
- **Auto-signatures** : La clé primaire signe ses propres composants pour empêcher la falsification.

Visualisez la structure d'une clé de manière interactive :
```
gpg --edit-key <id-clé-ou-email>
```
Dans le menu, utilisez `check` pour vérifier les auto-signatures ou `toggle` pour voir les parties privées (si disponibles).

## Génération des clés

Commencez par une paire de clés primaires. Utilisez la méthode interactive pour les débutants :

1. Exécutez `gpg --full-gen-key` (ou `--gen-key` pour les valeurs par défaut).
2. Choisissez le type de clé (par défaut : RSA pour la signature et le chiffrement).
3. Sélectionnez la taille de la clé (par exemple, 4096 bits pour une sécurité renforcée ; minimum 2048 recommandé).
4. Définissez l'expiration (par exemple, 1y pour un an ; "0" pour jamais — évitez l'expiration indéfinie si possible).
5. Entrez l'identifiant utilisateur (nom, email).
6. Définissez une phrase de passe robuste (20+ caractères, mélange de majuscules/minuscules/symboles).

Pour une génération rapide (non interactive) :
```
gpg --quick-generate-key "Alice <alice@example.com>" rsa default 1y
```

Après la génération, créez un **certificat de révocation** (un fichier pour invalider votre clé si elle est compromise) :
```
gpg --output revoke.asc --gen-revoke <votre-id-clé>
```
Stockez-le en lieu sûr (par exemple, imprimé dans un coffre) — ne le partagez pas avant d'en avoir besoin.

Pour ajouter des sous-clés ou des UID plus tard :
- Entrez `gpg --edit-key <id-clé>`, puis `addkey` (pour une sous-clé) ou `adduid` (pour un UID). Ceux-ci sont auto-signés automatiquement.

## Lister et visualiser les clés

- Lister les clés publiques : `gpg --list-keys` (ou `--list-public-keys`).
- Lister les clés privées : `gpg --list-secret-keys`.
- Vue détaillée : `gpg --list-keys --with-subkey-fingerprint <id-clé>` (affiche les empreintes pour les sous-clés).

La sortie montre l'ID de clé (court/long), les dates de création/expiration, les capacités (par exemple, `[SC]` pour signer/certifier) et les UID.

## Exporter et importer des clés

**L'exportation** permet de partager votre clé publique ou de sauvegarder les clés privées :
- Clé publique : `gpg --armor --export <id-clé> > mykey.asc` (format ASCII pour l'email).
- Clé privée (sauvegarde uniquement) : `gpg --armor --export-secret-keys <id-clé> > private.asc`.
- Vers un serveur de clés : `gpg --keyserver hkps://keys.openpgp.org --send-keys <id-clé>`.

**L'importation** ajoute les clés des autres à votre porte-clés public :
- `gpg --import <fichier.asc>` (fusionne avec l'existant ; ajoute de nouvelles signatures/sous-clés).
- Depuis un serveur de clés : `gpg --keyserver hkps://keys.openpgp.org --recv-keys <id-clé>`.

Après l'importation, vérifiez avec `gpg --edit-key <id-clé>` et `check` pour les auto-signatures.

## Signer et certifier des clés

Pour construire la confiance :
- Signer une clé (certifier qu'elle est valide) : `gpg --sign-key <autre-id-clé>` (ou `lsign-key` pour local uniquement).
- Signature rapide : `gpg --quick-sign-key <empreinte> "Identifiant Utilisateur"`.
- Définir le niveau de confiance : Dans `--edit-key`, utilisez `trust` (par exemple, "5" pour confiance ultime).

Cela crée des signatures sur la clé, visibles dans les listages. La toile de confiance calcule la validité en fonction de votre confiance dans les signataires.

## Révoquer des clés

La révocation invalide une clé ou un composant sans la supprimer, garantissant que les autres voient qu'elle n'est plus valide :
- Clé complète : Importez votre certificat de révocation : `gpg --import revoke.asc`, puis exportez/envoyez la clé mise à jour.
- Sous-clé/UID : Dans `--edit-key`, sélectionnez avec `key 1` ou `uid 1`, puis `revkey` ou `revuid`.
- Révoquer un UID rapidement : `gpg --quick-revoke-uid <id-clé> <uid-à-révoquer>`.

Raisons de révocation : compromise, plus utilisée, remplacée. Publiez toujours les clés révoquées.

## Bonnes pratiques

- **Sécurité** : Utilisez des tokens matériels (par exemple, YubiKey) pour les clés privées. Changez les sous-clés de chiffrement annuellement (`gpg --quick-add-key <empreinte> rsa encr 1y`). Changez les phrases de passe régulièrement (`gpg --change-passphrase <id-clé>`).
- **Expiration** : Définissez des expirations raisonnables (1-2 ans) pour forcer les mises à jour et détecter les compromissions.
- **Distribution** : Partagez les clés publiques via des serveurs de clés ou directement ; vérifiez les empreintes en personne ou via des canaux de confiance pour éviter les attaques de l'homme du milieu.
- **Sauvegarde** : Exportez les clés privées vers un stockage chiffré. Générez les certificats de révocation immédiatement.
- **Nettoyage** : Utilisez `gpg --edit-key` avec `clean` pour supprimer les signatures invalides.
- **Mises à jour** : À partir de 2025, GnuPG 2.5+ supporte les algorithmes résistants aux quanta (par exemple, `--quick-generate-key ... pqc`) ; envisagez une migration pour la pérennité.
- **Pièges courants** : Ne partagez jamais les clés privées. Évitez les expirations indéfinies. Testez les révocations dans un environnement de test.

Pour une pratique, expérimentez dans un répertoire de test avec `gpg --homedir ./test-gpg`.

[GnuPG Handbook: Key Management](https://www.gnupg.org/gph/en/manual/c235.html)  
[GNU Privacy Guard Manual: OpenPGP Key Management](https://www.gnupg.org/documentation/manuals/gnupg/OpenPGP-Key-Management.html)  
[GnuPG Getting Started](https://www.gnupg.org/gph/en/manual/c14.html)