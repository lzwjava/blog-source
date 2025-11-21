---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4.1-fast
title: Résumé du jeu de données FineWeb 2013
translated: true
type: note
---

**CC-MAIN-2013-20** (dump de l'été 2013) dans le jeu de données FineWeb :

- **Nombre de fichiers .parquet** : Environ **460–500**
  (Les fichiers sont fragmentés avec des tailles variables : beaucoup ~1 Go, certains plus grands jusqu'à ~2 Go. Le répertoire totalise **422 Go**, donc 422 ÷ ~0,9 Go de moyenne ≈ 460–480 fragments. La numérotation est séquentielle `000_00000.parquet` jusqu'à environ `000_004xx.parquet`.)

- **Taille totale de tous les fichiers parquet** : **422 Go**

- **Tokens lorsqu'ils sont encodés avec un tokenizer de style GPT** (cl100k_base utilisé pour GPT-4, ou l'ancien tokenizer GPT-2 utilisé dans les rapports de FineWeb) :
  **144,5 milliards de tokens** (après le pipeline de nettoyage, de filtrage et de déduplication de FineWeb)

Note : Le dump Common Crawl brut original était beaucoup plus volumineux (~393 milliards de tokens avant filtrage), mais FineWeb ne conserve que le texte anglais de haute qualité, ce qui explique pourquoi cet ancien dump de 2013 rétrécit si dramatiquement.

Si vous téléchargez l'intégralité du répertoire (par exemple via `huggingface-cli download` ou un script qui boucle sur tous les fragments), vous vous retrouverez avec ~422 Go de fichiers parquet contenant 144,5 milliards de tokens prêts pour l'entraînement.

[Fiche du jeu de données FineWeb (inclut un tableau des tokens par dump)](https://huggingface.co/datasets/HuggingFaceFW/fineweb)
[Répertoire CC-MAIN-2013-20 sur HF (montre la taille totale)](https://huggingface.co/datasets/HuggingFaceFW/fineweb/tree/main/data/CC-MAIN-2013-20)