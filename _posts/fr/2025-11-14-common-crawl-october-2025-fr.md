---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résumé du jeu de données d'octobre 2025 de Common Crawl
translated: true
type: note
---

Ce tableau est le résumé officiel du **crawl d'octobre 2025 de Common Crawl**, spécifiquement l'ensemble de données étiqueté **CC-MAIN-2025-43**. Common Crawl est un projet à but non lucratif qui parcourt l'intégralité du web public tous les mois ou deux et publie les données brutes gratuitement afin que les chercheurs, les entreprises et toute autre personne puissent les utiliser (par exemple, pour entraîner de grands modèles de langage comme GPT, LLaMA, Grok, etc.).

Voici ce que signifie chaque partie du tableau :

### Faits de base
- **Nom** : CC-MAIN-2025-43 → le 43ème crawl hebdomadaire publié en 2025, effectué approximativement en octobre 2025.
- **Taille** : 2,61 milliards de pages web individuelles ont été capturées.

### Les différents types de données et ce qu'ils contiennent

| Type de données        | Qu'est-ce que c'est                                                                         | Taille totale non compressée | # de fichiers | Taille compressée |
|------------------------|----------------------------------------------------------------------------------------------|------------------------------|---------------|-------------------|
| **WARC**               | Les données brutes et complètes du crawl (réponses HTTP complètes : en-têtes + HTML + ressources intégrées) | ~ des centaines de Tio       | 100 000       | 97,73 Tio         |
| **WAT**                | Métadonnées extraites des fichiers WARC (par ex., liens sortants, langue, taille du contenu, etc.) au format JSON |                              | 100 000       | 18,39 Tio         |
| **WET**                | Seul le texte brut extrait (pas de balises HTML, pas d'éléments standardisés, juste le texte nettoyé) |                              | 100 000       | 7,38 Tio          |
| **Fichiers Robots.txt**| Tous les fichiers robots.txt qui ont été récupérés pendant le crawl                          |                              | 100 000       | 0,15 Tio          |
| **Réponses non-200**   | Réponses qui n'ont pas abouti (404, 500, redirections, etc.)                                |                              | 100 000       | 3,07 Tio          |
| **Fichiers d'index d'URL** | Index permettant de trouver quel fichier WARC contient une URL spécifique (ancien format) |                              | 302           | 0,20 Tio          |
| **Index d'URL columnar** | Nouvel index columnaire plus rapide (format Parquet) pour les outils de big data comme Spark, DuckDB, etc. |                              | 900           | 0,23 Tio          |

### Pourquoi les différents formats existent
- Si vous voulez juste entraîner un modèle de langage → vous téléchargez généralement les fichiers **WET** (texte déjà nettoyé, taille la plus petite).
- Si vous avez besoin du HTML complet, des images, du CSS, etc. → vous téléchargez les fichiers **WARC** (les plus volumineux).
- Si vous avez besoin des métadonnées (liens, langue détectée, etc.) sans le HTML complet → **WAT**.
- Les index vous permettent de trouver des pages sans avoir à parcourir l'intégralité des 100 000 fichiers.

### Comment les fichiers sont organisés
Tout est divisé en 100 **segments** (environ 1 Tio compressé chacun pour les WARC). Chaque segment contient de nombreux fichiers .warc.gz (ou .wat.gz, .wet.gz) plus petits. Les fichiers *.paths.gz que vous voyez listés sont simplement des fichiers texte qui contiennent la liste complète des URL S3 pour chaque type.

Vous pouvez accéder à tout gratuitement sur AWS S3 à l'adresse :
`s3://commoncrawl/crawl-data/CC-MAIN-2025-43/`
(ou via HTTPS : https://data.commoncrawl.org/)

En bref : Il s'agit de l'un des plus grands ensembles de données web ouvertes au monde (2,61 milliards de pages d'octobre 2025), librement disponibles sous différentes formes traitées, et le tableau vous indique simplement la taille de chaque version traitée et où trouver les listes de fichiers.