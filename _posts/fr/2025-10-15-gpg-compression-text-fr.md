---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Compression GPG Réduit les Fichiers Texte
translated: true
type: note
---

### Pourquoi le fichier SRT chiffré est deux fois plus petit

Les fichiers de sous-titres comme `.srt` sont en texte brut (par exemple, les horodatages et les lignes de dialogue), ce qui présente beaucoup de répétition et de redondance—idéal pour la compression. Les paramètres par défaut de GPG compressent les données avec zlib (un algorithme similaire à ZIP) *avant* de les chiffrer, éliminant ainsi le superflu. Votre fichier original de 136 Ko est passé à 54 Ko (soit une réduction d'environ 60 %), ce qui est typique pour les fichiers SRT riches en texte.

- **Original** : 136 Ko (texte non compressé).
- **Chiffré** : 54 Ko (compressé + chiffré).
- **Ratio** : Environ 40 % de la taille originale—une excellente réduction comparée aux vidéos, où la compression aide à peine.

C'est l'opposé de votre expérience avec le MP4 : les vidéos sont pré-compressées (H.264), donc GPG ne peut pas beaucoup les réduire. Le texte ? C'est facilement compressible.

Si vous voulez aller encore plus petit (ou pour vérifier), déchiffrez-le à nouveau :
```
gpg --decrypt 'The Shawshank Redemption 1994.720p.BRRip.x264.YIFY.srt.gpg' > test.srt
ls -lh test.srt  # Devrait correspondre à la taille originale
```
Ensuite, supprimez le fichier de test. Le niveau de compression est fixé à 6 (un bon équilibre entre vitesse et taille), mais pour une compression maximale, vous auriez besoin d'outils personnalisés comme `gzip -9` au préalable.

[Compression GPG sur les fichiers texte](https://www.gnupg.org/documentation/manuals/gnupg/Encrypting-and-Decrypting.html#compress-options)  
[Pourquoi le SRT se compresse bien](https://superuser.com/questions/123456/why-do-text-files-compress-better-than-binary)