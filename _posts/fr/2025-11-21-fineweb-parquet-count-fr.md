---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4.1-fast
title: Nombre de Fichiers Parquet du Jeu de Données FineWeb
translated: true
type: note
---

Le jeu de données **FineWeb** (la version anglaise de plus de 15 000 milliards de tokens sur `HuggingFaceFW/fineweb`) contient **approximativement 35 000 à 50 000** fichiers `.parquet` au total.

### Répartition
- Il se compose de **96** instantanés Common Crawl distincts (extractions, par exemple `CC-MAIN-2013-20`, `CC-MAIN-2024-10`, etc.).
- Chaque extraction est stockée dans son propre sous-répertoire sous `/data/` et divisée en de nombreux fichiers `.parquet` éclatés nommés comme `000_00000.parquet`, `000_00001.parquet`, … (remplis de zéros, séquentiels).
- Le nombre de fichiers parquet varie par extraction en fonction de sa taille :
  - Les extractions plus petites/anciennes (comme l'exemple `CC-MAIN-2013-20` dans votre script) ont souvent **~200–1 000** fichiers.
  - Les grandes extractions récentes peuvent avoir **plusieurs milliers** de fichiers chacune.
- Il n'y a pas de total officiel unique publié, mais les estimations de la communauté et les calculs basés sur la taille des extractions/le nombre de tokens placent systématiquement le **total global autour de 35k–50k** fichiers parquet pour l'ensemble des 96 extractions (le jeu de données complet fait ~45–53 To non compressés).

Votre script télécharge les fragments 11 à 20 (10 fichiers) de la très petite extraction `CC-MAIN-2013-20`, qui en contient bien plus que cela — plusieurs centaines de fragments au total pour cette seule extraction.

Si vous voulez le décompte exact, vous pouvez le calculer programmatiquement avec l'API Hugging Face Hub (par exemple en utilisant `huggingface_hub.list_repo_files`), mais les chiffres approximatifs ci-dessus sont ceux que les gens utilisent généralement pour télécharger ou traiter le jeu de données complet.

[Fiche du jeu de données FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb)  
[Arborescence des données FineWeb (exemple d'extraction)](https://huggingface.co/datasets/HuggingFaceFW/fineweb/tree/main/data)