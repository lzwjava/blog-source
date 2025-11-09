---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Chiffrement et signature GPG expliqués
translated: true
type: note
---

### Principes de base de GPG : Chiffrement vs Signature

Vous mélangez quelques concepts ici—GPG (GNU Privacy Guard) peut faire du **chiffrement** (pour protéger le contenu des fichiers) et de la **signature** (pour vérifier l'identité et l'intégrité)—mais ce sont des fonctionnalités distinctes. Je vais les décomposer étape par étape, confirmer vos points et clarifier où les choses se chevauchent ou diffèrent. Ceci est basé sur l'utilisation standard de GPG (qui n'a pas beaucoup changé en 2025).

#### 1. **Génération des clés et vos informations (Nom/Email)**
   - Lorsque vous configurez GPG pour la première fois, vous générez une **paire de clés** : une clé privée (gardée secrète) et une clé publique (partagée avec les autres).
   - Pendant la génération, vous fournissez votre **nom et email** comme partie de "l'identifiant utilisateur" de la clé (par exemple, `gpg --gen-key`). Cela lie la clé à votre identité.
   - Vous définissez également une **phrase de passe** pour protéger votre clé privée. Cette phrase de passe **n'est pas** utilisée pour chiffrer les fichiers—elle sert uniquement à déverrouiller votre clé privée lorsque nécessaire.
   - Exemple de commande :
     ```
     gpg --gen-key
     ```
     Suivez les invites pour RSA/RSA, la taille de la clé, l'expiration et votre nom/email.

#### 2. **Chiffrement d'un fichier**
   - **Avec un mot de passe (chiffrement symétrique)** : Cela n'implique pas de clés ou votre identité—c'est rapide pour partager un fichier de manière sécurisée. GPG utilise la phrase de passe pour créer une clé unique pour le chiffrement.
     - Commande : `gpg -c nomdufichier.txt` (demande la phrase de passe, produit `nomdufichier.txt.gpg`).
     - Toute personne ayant la phrase de passe peut déchiffrer : `gpg -d nomdufichier.txt.gpg`.
     - Pas de clés publique/privée ici ; pas de vérification d'identité.
   - **Avec des clés publiques (chiffrement asymétrique)** : Pour chiffrer pour quelqu'un en particulier, utilisez sa clé publique. Votre nom/email n'est pas directement impliqué dans le résultat du chiffrement.
     - Commande : `gpg -e -r destinataire@exemple.com nomdufichier.txt` (produit `nomdufichier.txt.gpg`).
     - Seule la clé privée du destinataire peut le déchiffrer.
   - Le résultat du chiffrement est un fichier `.gpg`, mais ce n'est **pas une signature**—ce sont juste des données chiffrées. Pas de "signature GPG" avec le seul chiffrement.

#### 3. **Signature d'un fichier (Ce que vous décrivez)**
   - La signature attache une **signature numérique** à un fichier (ou à son hash) pour prouver qu'il vient de vous et n'a pas été altéré. C'est là que votre **clé privée** et votre identité entrent en jeu.
   - **Oui, vous devez utiliser votre clé privée pour générer la signature.** GPG la déverrouille avec votre phrase de passe.
     - Commande pour une signature détachée : `gpg --detach-sign nomdufichier.txt` (produit `nomdufichier.txt.sig`).
     - Ou en ligne (signe et chiffre en une fois) : `gpg -s nomdufichier.txt` (produit `nomdufichier.txt.gpg` avec la signature intégrée).
   - La signature est une "valeur" cryptographique (comme un hash signé avec votre clé privée) qui inclut l'identifiant de votre clé et votre identifiant utilisateur (nom/email).
   - **Les autres vérifient avec votre clé publique** : Ils importent votre clé publique (par exemple depuis un serveur de clés : `gpg --keyserver keys.openpgp.org --recv-keys VOTRE_ID_DE_CLÉ`), puis exécutent `gpg --verify nomdufichier.txt.sig nomdufichier.txt`.
     - Si cela correspond, cela affiche quelque chose comme "Bonne signature de 'Votre Nom <email>'".
   - **Oui, cela correspond à l'identité et construit la confiance** :
     - La signature prouve que le fichier provient du propriétaire de la clé (vous).
     - Si vous avez partagé votre clé publique via un canal de confiance (par exemple, votre site web) et que la clé est signée par d'autres personnes en qui vous avez confiance, vous pouvez "faire confiance" à la chaîne.
     - Cela ne chiffre pas le fichier—seulement le vérifie. Combinez avec le chiffrement pour une sécurité complète (signer puis chiffrer).

#### Différences clés et vos questions

| Fonctionnalité | Chiffrement (Mot de passe) | Chiffrement (Clé publique) | Signature |
|---------|-----------------------|--------------------------|---------|
| **Utilise une phrase de passe ?** | Oui, pour la clé symétrique | Non (utilise la clé publique du destinataire) | Oui, pour déverrouiller votre clé privée |
| **Implique votre nom/email ?** | Non | Indirectement (via votre clé pour la réponse du déchiffrement) | Oui, intégré dans la signature |
| **Résultat** | Fichier `.gpg` (données chiffrées) | Fichier `.gpg` (données chiffrées) | `.sig` ou intégré dans `.gpg` (valeur de signature) |
| **Clé privée nécessaire ?** | Non | Non (pour chiffrer vers d'autres) | Oui, pour générer |
| **Vérification** | Phrase de passe pour déchiffrer | Clé privée du destinataire | N'importe qui avec votre clé publique |
| **Objectif** | Masquer le contenu | Partage sécurisé | Prouver l'identité/l'intégrité |

- **Correct concernant la clé privée** : Oui, vous **devez** utiliser votre clé privée (déverrouillée par la phrase de passe) pour signer. Ne la partagez jamais !
- **Correct concernant la confiance** : Exactement—si la signature est vérifiée par rapport à votre clé publique, et que vous avez confiance que cette clé appartient à l'auteur déclaré (via le nom/email et le web de confiance), vous pouvez faire confiance au fait que le fichier est authentique et non altéré. C'est comme un notaire numérique.

#### Conseils
- Sauvegardez toujours vos clés : `gpg --export-secret-keys --armor > private.asc` (stockez en sécurité).
- Pour les mots de passe uniquement (pas de clés), des outils comme `age` ou `openssl` sont des alternatives plus simples, mais GPG est excellent pour les choses liées à l'identité.
- Piège courant : Oublier d'exporter/partager votre clé publique empêche les autres de vérifier.

Si vous pensiez à une commande ou un scénario spécifique (par exemple, chiffrer *et* signer), partagez plus de détails !

**Références**  
[Documentation GPG : Chiffrement et Signature](https://www.gnupg.org/documentation/manuals/gnupg/)  
[Guide de démarrage rapide GPG](https://www.gnupg.org/documentation/manuals/gnupg/GnuPG-basics.html)