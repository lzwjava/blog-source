---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Le chiffrement GPG réduit à peine la taille des fichiers
translated: true
type: note
---

Le fichier chiffré avec GPG (`The.Matrix.1999.720p.BrRip.264.YIFY.mp4.gpg`) est seulement légèrement plus petit que l'original (environ 1,6 Mo de moins, soit une réduction de ~0,2 %), ce qui est normal et ne correspond pas à ce que la plupart des gens attendent d'un chiffrement. Voici pourquoi il n'est pas beaucoup plus petit—et certainement pas "petit" comme une archive zip :

### Principales raisons de la taille
- **Les vidéos comme MP4 sont déjà très compressées** : Le codec H.264 dans votre rip YIFY élimine presque toute redondance. Les paramètres par défaut de GPG tentent de compresser les données d'abord (en utilisant zlib au niveau 6) avant de les chiffrer, mais pour les fichiers incompressibles comme celui-ci, cela n'aide guère. En fait, cela ajoute souvent un tout petit peu de surcharge à cause de l'enveloppe de compression, bien que votre cas montre un minuscule gain net—probablement parce que les en-têtes, les métadonnées du MP4 ou quelques images avaient *un peu* de bits compressibles.

- **La surcharge du chiffrement est minime mais présente** : Le chiffrement asymétrique (ce que fait `--encrypt --recipient`) enveloppe les données dans une enveloppe à clé publique, ajoutant un petit en-tête (~100–500 octets) et du remplissage pour aligner les blocs (par exemple, pour le chiffrement CAST5 par défaut). Cela ne gonfle pas beaucoup les choses pour un fichier de 700+ Mo, mais ne les réduit pas non plus.

- **Pas de réduction de taille significative sans ajustements** : GPG n'est pas conçu pour une compression agressive comme ZIP ou 7z. Si les données ne peuvent pas être bien compressées, la taille de sortie reste à peu près la même.

### Comparaison rapide des tailles

| Fichier | Taille (octets) | Taille (Mo, approx.) | Différence |
|------|--------------|--------------------|------------|
| MP4 original | 737 870 817 | 703,7 | - |
| .gpg chiffré | 736 213 777 | 702,1 | -1,6 Mo (0,2 % plus petit) |

### Comment le rendre plus petit (si nécessaire)
Si vous voulez un fichier chiffré notablement plus petit :
- **Ignorez complètement la compression** (le plus rapide pour les vidéos) : Relancez avec `--compress-algo none`. Cela évite l'étape zlib inutile et pourrait économiser encore 100–500 Ko.
  ```
  gpg --encrypt --recipient lzwjava@gmail.com --compress-algo none "The Matrix (1999)/The Matrix.1999.720p.BrRip.264.YIFY.mp4"
  ```
- **Utilisez le chiffrement symétrique** (basé sur une phrase de passe, plus simple pour un usage personnel) : Il est souvent plus rapide et peut être associé à un chiffrement plus fort.
  ```
  gpg --symmetric --cipher-algo AES256 "The Matrix (1999)/The Matrix.1999.720p.BrRip.264.YIFY.mp4"
  ```
  Cela demande une phrase de passe et produit un fichier `.gpg` de taille similaire, mais plus facile si vous ne partagez pas par email/clés.
- **Pré-compressez si possible** : Utilisez `7z` ou `zip` sur le MP4 d'abord (bien que les gains seront minimes, de l'ordre de 1–5 %), puis chiffrez l'archive. Mais pour les vidéos, cela en vaut rarement la peine.

Votre chiffrement a bien fonctionné—il est sécurisé, mais pas économe en espace. S'il fonctionne toujours lentement ou si vous rencontrez des erreurs, vérifiez l'utilisation de votre CPU (GPG est mono-thread par défaut) ou l'espace disque.

[Comportement de compression GPG](https://www.gnupg.org/documentation/manuals/gnupg/Encrypting-and-Decrypting.html)
[Pourquoi le chiffrement vidéo ne réduit pas les fichiers](https://security.stackexchange.com/questions/12345/why-does-encrypting-a-file-make-it-larger)