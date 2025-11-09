---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Algorithmes cryptographiques dans GnuPG
translated: true
type: note
---

### Algorithmes pris en charge dans les logiciels cryptographiques (par exemple, GnuPG)

Cette liste présente les algorithmes pris en charge par un outil comme GnuPG (GPG), couramment utilisé pour la messagerie sécurisée (PGP/MIME), le chiffrement de fichiers et les signatures numériques. Elle les catégorise en cryptographie à clé publique (asymétrique) pour l'échange de clés et la signature, en chiffrements symétriques pour le chiffrement en masse des données, en fonctions de hachage pour les vérifications d'intégrité et les signatures, et en méthodes de compression pour réduire la taille des données avant le chiffrement. Ci-dessous, je les détaillerai par catégorie avec de brèves explications sur l'utilité et les caractéristiques principales de chaque algorithme.

#### Algorithmes à clé publique (Pubkey)
Ils gèrent les opérations asymétriques : une clé (publique) pour le chiffrement/la vérification de signature, une autre (privée) pour le déchiffrement/la signature. Ils sont utilisés dans des paires de clés pour une communication sécurisée.

- **RSA** : Rivest-Shamir-Adleman. Un algorithme fondamental pour le chiffrement et les signatures numériques. Très répandu en raison de sa sécurité avec de grandes tailles de clés (par exemple, 2048+ bits), mais gourmand en calculs.
- **ELG** : ElGamal. Principalement pour le chiffrement (pas les signatures). Basé sur le problème du logarithme discret ; efficace pour l'échange de clés mais produit des textes chiffrés plus volumineux.
- **DSA** : Digital Signature Algorithm. Conçu uniquement pour les signatures numériques (pas le chiffrement). Repose sur les logarithmes discrets ; courant dans les systèmes plus anciens mais largement remplacé par ECDSA pour des raisons d'efficacité.
- **ECDH** : Elliptic Curve Diffie-Hellman. Pour l'accord/échange de clés utilisant les courbes elliptiques. Offre une sécurité robuste avec des clés plus petites que le DH traditionnel, idéal pour les appareils mobiles/contraints.
- **ECDSA** : Elliptic Curve Digital Signature Algorithm. Une variante à courbes elliptiques du DSA pour les signatures. Plus rapide et plus sécurisé par bit que DSA, avec une utilisation généralisée dans les protocoles modernes comme TLS.
- **EDDSA** : Edwards-curve Digital Signature Algorithm. Un schéma de signature à courbes elliptiques haute vitesse (par exemple, la variante Ed25519). Résistant aux attaques par canaux auxiliaires ; privilégié dans des protocoles comme SSH et Signal pour sa simplicité et sa vitesse.

#### Chiffrements symétriques
Ils chiffrent les données avec une clé secrète partagée (plus rapides pour les gros fichiers). Les chiffrements par bloc traitent les données en blocs de taille fixe, souvent avec des modes comme CBC pour le chaînage.

- **IDEA** : International Data Encryption Algorithm. Un chiffrement par bloc de 64 bits des années 1990 ; autrefois populaire mais maintenant considéré comme faible en raison de la taille de la clé et des risques de force brute.
- **3DES** : Triple Data Encryption Standard. Applique le DES trois fois pour une sécurité accrue. Algorithme hérité ; lent et vulnérable aux attaques, remplacé par l'AES.
- **CAST5** : CAST-128. Un chiffrement par bloc de 64 bits (famille CAST). Équilibre vitesse/sécurité pour son époque ; encore utilisé mais éclipsé par l'AES.
- **BLOWFISH** : Un chiffrement par bloc de 64 bits avec des longueurs de clé variables (jusqu'à 448 bits). Rapide et flexible ; bon pour les logiciels mais pas accéléré matériellement comme l'AES.
- **AES** : Advanced Encryption Standard (clé 128 bits). Chiffrement par bloc approuvé par le NIST ; la référence absolue pour le chiffrement symétrique — sécurisé, rapide et omniprésent.
- **AES192** : AES avec des clés de 192 bits. Offre un renforcement de sécurité intermédiaire par rapport à l'AES standard.
- **AES256** : AES avec des clés de 256 bits. Variante de l'AES offrant la sécurité la plus élevée ; recommandée pour les données hautement sensibles.
- **TWOFISH** : Un chiffrement par bloc de 128 bits (finaliste de l'AES). Très sécurisé avec des tailles de clé flexibles ; performant en logiciel.
- **CAMELLIA128** : Chiffrement par bloc Camellia (clé 128 bits). Standard japonais/européen ; sécurité et vitesse similaires à l'AES.
- **CAMELLIA192** : Camellia avec des clés de 192 bits. Niveau de sécurité amélioré.
- **CAMELLIA256** : Camellia avec des clés de 256 bits. Variante haut de gamme, comparable à l'AES256.

#### Algorithmes de hachage
Ils créent des empreintes de taille fixe à partir de données pour vérifier l'intégrité, l'authenticité, ou pour une utilisation dans les signatures/mots de passe. La résistance aux collisions est essentielle (bien que SHA1 soit maintenant cassé).

- **SHA1** : Secure Hash Algorithm 1. Produit des empreintes de 160 bits ; rapide mais non sécurisé en raison de vulnérabilités aux collisions — à éviter pour de nouvelles utilisations.
- **RIPEMD160** : RACE Integrity Primitives Evaluation Message Digest (160 bits). Alternative européenne à SHA1 ; encore raisonnablement sécurisé mais vieillissant.
- **SHA256** : Famille SHA-2 (256 bits). Robuste et largement utilisé ; base pour Bitcoin et les mots de passe sécurisés.
- **SHA384** : SHA-2 (384 bits). Empreinte plus longue pour une sécurité accrue dans les applications sensibles.
- **SHA512** : SHA-2 (512 bits). Plus grande variante de SHA-2 ; excellente pour le hachage haute sécurité.
- **SHA224** : SHA-2 (224 bits). Un SHA-256 tronqué pour la compatibilité avec les systèmes hérités.

#### Algorithmes de compression
Ils réduisent la taille des données avant le chiffrement pour accélérer le traitement et réduire la taille du stockage/transmission. Appliqués de manière transparente dans des outils comme GPG.

- **Uncompressed** : Aucune compression — les données sont chiffrées telles quelles. Utile pour les fichiers déjà compressés (par exemple, JPEG) pour éviter la surcharge.
- **ZIP** : Algorithme DEFLATE (LZ77 + codage Huffman). Courant dans les archives de fichiers ; bon équilibre entre vitesse et taux de compression.
- **ZLIB** : DEFLATE amélioré avec en-têtes et sommes de contrôle. Similaire à ZIP mais plus flexible pour les flux.
- **BZIP2** : Transformation de Burrows-Wheeler + Huffman. Plus lent mais obtient de meilleurs taux de compression que ZIP/ZLIB, surtout pour le texte.

Cette configuration permet des flux de travail flexibles et sécurisés — par exemple, signer avec ECDSA, chiffrer avec AES256, hacher avec SHA256 et compresser avec ZLIB. Pour les derniers détails sur GnuPG, consultez le [manuel officiel](https://www.gnupg.org/documentation/manuals/gnupg/index.html).