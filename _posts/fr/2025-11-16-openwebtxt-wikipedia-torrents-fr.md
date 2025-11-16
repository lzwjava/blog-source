---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Jeux de données OpenWebText et Wikipedia en torrent
translated: true
type: note
---

### Torrents du jeu de données OpenWebText

OpenWebText est une réplication open-source du jeu de données WebText d'OpenAI, constitué d'environ 38 Go de texte nettoyé extrait de liens Reddit à haut karma (principalement des pages web scrapées et filtrées pour leur qualité). C'est un corpus de texte à grande échelle populaire pour l'entraînement de modèles de langage. Bien que le texte scrapé complet ne soit pas toujours disponible directement sous forme d'un seul torrent, voici des options fiables :

- **Liste d'URLs (Filtrée, ~480 Mo)** : Une liste pré-filtrée d'environ 26 millions d'URLs utilisées pour le scraping d'OpenWebText. Vous pouvez l'utiliser pour télécharger et traiter le texte vous-même.
  - Torrent : [OpenWebText-urls-26M-filtered.xz](https://academictorrents.com/details/f5161721b322bca66ed74da32b963c1066e64312)
  - Source : Academic Torrents (seedé par la communauté).

- **Liste d'URLs (Complète, ~1,75 Go)** : La liste complète dédupliquée des URLs provenant des soumissions Reddit.
  - Torrent : [WebText dataset urls.txt.tar.gz](https://academictorrents.com/details/15f3494b2991e75194d3af72bf7afa5025a7abc3)
  - Source : Academic Torrents (seedé par la communauté).

- **Version Tokenisée (~16 Go)** : Fichiers texte tokenisés par GPT-2 à partir du corpus scrapé (395 fichiers, prêts pour l'entraînement de modèles).
  - Torrent : [OpenWebText (Gokaslan's distribution, 2019), GPT-2 Tokenized](https://academictorrents.com/details/36c39b25657ce1639ccec0a91cf242b42e1f01db)
  - Source : Academic Torrents (seedé par OSUOSL et la communauté).

Pour le corpus de texte brut complet, consultez le site officiel pour les téléchargements directs (non basés sur le torrent) ou utilisez les URLs ci-dessus avec les scripts de scraping du [dépôt GitHub OpenWebText](https://github.com/eukaryote31/openwebtext). Une version améliorée, OpenWebText2 (~échelle multi-To), est disponible via le [dépôt d'EleutherAI](https://github.com/EleutherAI/openwebtext2) mais utilise le streaming plutôt que les torrents.

### Torrents des exports Wikipedia

Les exports Wikipedia sont des exports XML mensuels de l'intégralité de la base de données (articles, révisions, métadonnées). La version anglaise est massive (~20-25 Go compressés pour les abstracts, jusqu'à 100+ Go pour l'historique complet). Les torrents sont maintenus par la communauté (non officiels mais vérifiés par rapport aux sommes de contrôle officielles) et sont seedés via le web depuis les serveurs de Wikimedia pour la fiabilité. Vérifiez toujours les téléchargements par rapport aux hachages de [dumps.wikimedia.org](https://dumps.wikimedia.org/enwiki/latest/).

Le hub principal pour les torrents est la [page Meta-Wiki Data Dump Torrents](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki), qui liste les derniers exports de Wikipedia anglais (par exemple, enwiki-20251101). Voici un résumé des plus récents :

| Date de l'export | Type de fichier | Taille compressée | Lien du torrent | Notes |
|-----------|-----------|-----------------|--------------|-------|
| 2025-11-01 | Pages-Articles (XML, abstracts uniquement) | ~22 Go | [enwiki-20251101-pages-articles-multistream.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | Format multistream ; le plus facile pour l'extraction de texte. |
| 2025-11-01 | Pages-Articles-History (XML, révisions complètes) | ~120 Go | [enwiki-20251101-pages-meta-history*.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | Inclut toutes les modifications ; divisé en streams pour une manipulation plus facile. |
| 2025-10-01 | Pages-Articles (XML, abstracts uniquement) | ~21 Go | [enwiki-20251001-pages-articles-multistream.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | Mois précédent ; utile pour les comparaisons historiques. |

- **Collection complète** : Parcourez tous les torrents historiques de Wikipedia anglais sur la [Collection Wikipedia d'Academic Torrents](https://academictorrents.com/collection/wikipedia) (inclut des exports plus anciens remontant à ~2010).
- **Format Kiwix ZIM** : Si vous voulez une Wikipedia hors ligne navigable (HTML, ~100 Go), essayez [wikipedia_en_all_maxi_2024-01.zim.torrent](https://download.kiwix.org/zim/wikipedia/wikipedia_en_all_maxi_2024-01.zim.torrent) – seedé par la communauté, mais vérifiez les mises à jour 2025 sur les [téléchargements Kiwix](https://download.kiwix.org/zim/wikipedia/).

Pour traiter ces fichiers en texte brut, utilisez des outils comme `wikiextractor` de Python. Les torrents réduisent la charge sur les serveurs et permettent de reprendre les téléchargements interrompus – utilisez un client comme qBittorrent. Si vous avez besoin d'exports pour d'autres langues ou sous-ensembles, la page Meta-Wiki propose des filtres.