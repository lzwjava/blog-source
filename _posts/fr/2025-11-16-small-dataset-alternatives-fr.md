---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Alternatives de petits ensembles de données de haute qualité
translated: true
type: note
---

Oui, OpenWebText est énorme (~9 milliards de tokens, fichier de 17 Go en uint16) et son prétraitement prend beaucoup de temps et d'espace disque. Voici des alternatives de haute qualité bien plus petites, couramment utilisées pour les tests, le débogage ou l'entraînement rapide de petits modèles :

| Dataset                  | Tokens approximatifs | Taille finale .bin (uint16) | Pourquoi les gens l'aiment                                                                 | Comment l'obtenir rapidement                                      |
|--------------------------|----------------------|-----------------------------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| **OpenWebText-10k**      | ~40M                 | ~80 Mo                      | Même distribution que le OpenWebText complet, seulement les 10 000 premiers documents | `load_dataset("openwebtext", split="train[:10k]")`                |
| **OpenWebText-100k**     | ~400M                | ~800 Mo                     | Reste très représentatif, finit de tokeniser en quelques minutes                      | `split="train[:100k]"`                                            |
| **FineWeb-Edu sample**   | 50M–1B               | 100 Mo–2 Go                 | Qualité supérieure à OWT (filtrage style LLama), très populaire récemment             | `load_dataset("HuggingFaceFW/fineweb-edu", name="sample-10BQ", split="train")` → ~50M tokens |
| **Shakespeare**          | ~1M                  | ~2 Mo                       | Dataset miniature classique, parfait pour des vérifications rapides                   | `load_dataset("tiny_shakespeare")` ou télécharger le simple fichier .txt |
| **PG-19 (books)**        | Complet 2.8B         | ~5.5 Go                     | Livres du domaine public très propres, mais vous pouvez n'en prendre qu'une partie    | `load_dataset("pg19", split="train[:5%]")` → ~140M tokens         |
| **C4 (subset)**          | variable             | variable                    | Common Crawl nettoyé par l'équipe T5, anglais uniquement                              | `load_dataset("allenai/c4", "en", split="train[:1%]")` streaming=True |
| **RedPajama sample**     | 5M–200M              | 10 Mo–400 Mo                | Mélange de sources (CommonCrawl, Wikipedia, livres, etc.), même recette que LLaMA     | `load_dataset("togethercomputer/RedPajama-Data-1T", name="sample", split="train")` |

### Mes recommandations personnelles selon votre objectif

1. Vous voulez juste quelque chose qui s'exécute en < 5 minutes et tient n'importe où → **tiny_shakespeare**  
   (les utilisateurs de nanoGPT l'adorent)

2. Vous voulez quelque chose qui reste du "vrai texte internet" mais minuscule → Les 10 000 premiers documents de OpenWebText  
   ```python
   dataset = load_dataset("openwebtext", split="train[:10000]")
   ```

3. Vous voulez le petit dataset de plus haute qualité actuellement (2025) → L'échantillon FineWeb-Edu de 10 milliards de tokens  
   (~50M tokens, mais beaucoup plus propre que OWT, qualité quasi identique à ce qu'utilisent les meilleurs labos)

   ```python
   dataset = load_dataset(
       "HuggingFaceFW/fineweb-edu",
       name="sample-10BQ",  # 10 milliards de tokens échantillonnés, ~50M par fragment si on découpe
       split="train"
   )
   ```

4. Vous voulez quelque chose < 500 Mo mais toujours diversifié → L'échantillon RedPajama (version 200M tokens)  
   ```python
   dataset = load_dataset("togethercomputer/RedPajama-Data-1T", name="sample-200M", split="train")
   ```

Tous ces datasets s'intègrent dans votre script de prétraitement exactement tel quel sans aucune modification (remplacez simplement la ligne load_dataset).

Pour une itération rapide, je garde généralement trois binaires sur le disque :
- `shakespeare.bin`   (~2 Mo)   → tests de surapprentissage
- `owt_10k.bin`       (~80 Mo)  → débogage de nouveau code
- `fineweb_edu_1B.bin` (~2 Go) → entraînement de petit modèle réel

Dites-moi la taille que vous souhaitez et je peux vous donner la commande exacte en une ligne !