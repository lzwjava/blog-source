---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de téléchargement de Wikipédia en anglais
translated: true
type: note
---

Ceci est un listing de répertoire provenant d'un des miroirs de téléchargement officiels de Wikimedia (généralement https://dumps.wikimedia.org/enwiki/latest/).  
Il contient toutes les différentes manières de télécharger les articles actuels de Wikipédia en anglais (à partir de début novembre 2025).

### Principaux formats et ce qu'ils contiennent réellement

| Modèle de nom de fichier | Qu'est-ce que c'est ? | Taille approximative (décompressé) | Idéal pour l'entraînement de LLM ? | Notes |
| --- | --- | --- | --- | --- |
| `enwiki-latest-pages-articles.xml.bz2` | Un seul fichier géant contenant **tous** les articles + pages de discussion, modèles, redirections, etc. | ~85–90 Go décompressé | Oui, très couramment utilisé | Le plus simple si vous avez l'espace et la bande passante |
| `enwiki-latest-pages-articles1.xml-p1p41242.bz2`  … jusqu'à … `enwiki-latest-pages-articles27.xml-…` | Les mêmes données, mais divisées en 27 morceaux plus petits (multistream) | Chaque ~200–600 Mo compressé → total toujours ~85–90 Go décompressé | Oui, choix le plus populaire | Permet de télécharger en parallèle et de reprendre facilement |
| `enwiki-latest-pages-articles-multistreamX.xml.bz2` (par ex. multistream27) | Les véritables gros fichiers de données compressées qui appartiennent à la version divisée ci-dessus | 300–600 Mo chacun compressé | Ce sont les vrais fichiers de données que vous voulez | Vous avez besoin de ceux-ci + des fichiers d'index |
| `enwiki-latest-pages-articles-multistreamX.xml.bz2.md5` / `.meta` | Fichiers de checksum et de métadonnées minuscules | < 1 Ko | Pas nécessaire pour le texte | Uniquement pour vérifier les téléchargements |
| `enwiki-latest-pages-articles-multistream-indexX.xml.bz2` | Fichiers d'index qui indiquent quel article se trouve à quel décalage d'octet dans les gros fichiers multistream | ~30–60 Mo chacun compressé | Requis si vous utilisez multistream | Nécessaire pour un accès aléatoire rapide ; la plupart des scripts de traitement les attendent |

### Recommandation : Ce que presque tout le monde utilise pour entraîner des modèles en 2025

La méthode standard de facto (utilisée par LLaMA, Mistral, Qwen, DeepSeek, Gemma, Phi, etc.) est :

Téléchargez les **27 fichiers multistream + leurs 27 fichiers d'index**  
(c'est-à-dire tout ce qui commence par `enwiki-latest-pages-articlesXX.xml-p…p….bz2` et les `…-indexXX…bz2` correspondants)

Ou encore plus simple : téléchargez simplement le **fichier unique géant** si votre connexion et votre disque peuvent le gérer :

```
enwiki-latest-pages-articles.xml.bz2    ← 24,6 Go compressé, ~85–90 Go décompressé
```

Les deux contiennent exactement les mêmes données XML brutes (tous les articles de l'espace principal + beaucoup de pages supplémentaires).

### Pourquoi pas les petits fichiers (multistream3.xml-p…, multistream4.xml-p… etc.) ?
Ce sont des divisions très anciennes de 2010–2015 qui ne contiennent qu'une infime fraction de Wikipédia (les articles qui se trouvaient dans cette plage d'ID de page à l'époque). Ils sont conservés uniquement pour des raisons historiques et sont pratiquement inutiles aujourd'hui.

### Commandes de démarrage rapide (dump 2025)

Téléchargement parallèle des 27+27 fichiers recommandés (le plus rapide) :

```bash
# Obtenir la liste des fichiers
wget -q https://dumps.wikimedia.org/enwiki/latest/ -O - | \
  grep -E 'enwiki-latest-pages-articles[0-9]+[02468]\.xml-p[0-9]+p[0-9]+\.bz2"' | \
  sed -e 's/.*href="//' -e 's/".*//' | \
  xargs -n1 -P10 wget https://dumps.wikimedia.org/enwiki/latest/

# Télécharger aussi les fichiers d'index correspondants
wget -q https://dumps.wikimedia.org/enwiki/latest/ -O - | \
  grep -E 'enwiki-latest-pages-articles-multistream-index' | \
  sed -e 's/.*href="//' -e 's/".*//' | \
  xargs -n1 -P10 wget https://dumps.wikimedia.org/enwiki/latest/
```

Ou juste le fichier unique (le plus simple) :

```bash
wget https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
```

Après cela, vous le traitez normalement avec des outils comme :
- wikiextractor (Python) → texte nettoyé
- le chargeur Wikipedia de `datasets` de Hugging Face (fait déjà tout pour vous)
- les scripts de traitement de DeepSeek ou d'EleutherAI, etc.

Donc, en bref :  
Téléchargez soit le fichier unique de 24 Go `enwiki-latest-pages-articles.xml.bz2`, soit les 27 fichiers divisés + les index. Tout le reste dans cette liste est soit des checksums, d'anciennes données inutiles, ou des métadonnées dont vous n'avez pas besoin pour l'entraînement.