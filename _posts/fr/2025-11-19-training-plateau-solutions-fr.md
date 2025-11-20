---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Causes et solutions du plateau d'entraînement
translated: true
type: note
---

Le journal d'entraînement que vous avez publié montre un **plateau sévère** classique dans une exécution nanoGPT à petite échelle sur les données FineWeb-edu. La perte de validation diminue bien au début (de ~10,9 → ~3,57 vers l'itération 14k), mais ensuite elle se stabilise complètement et commence même à **augmenter très lentement** après ~13-14k itérations.

Voici les vraies raisons pour lesquelles votre modèle a cessé de s'améliorer (classées par importance pour cette configuration exacte) :

### 1. Vous surapprenez massivement sur un seul fichier Parquet
- Le nom de votre exécution : `125M-single-parquet-4070`
- Vous entraînez un modèle de 40M–125M (le journal indique 40,56M de paramètres, probablement la configuration originale GPT-2 small) sur **un seul fichier Parquet de FineWeb** (probablement 10–15 GB → ~3–4 milliards de tokens au maximum, mais probablement beaucoup moins après filtrage).
- Vers l'itération 14 000 avec batch_size=16, grad_accum=32, block_size=1024, vous avez déjà vu :
  14 000 iters × 524 288 tokens/iter ≈ **7,3 milliards de tokens**
- Cela signifie que vous avez déjà effectué **2–3 époques complètes** sur exactement les mêmes données.
- FineWeb-edu est de haute qualité mais contient encore beaucoup de quasi-duplicatas et de texte boilerplate. Après 1,5–2 époques sur le(s) même(s) fichier(s), un modèle de 40M–125M va mémoriser presque tout ce qui est utile et la perte stagne fortement.

### 2. Le taux d'apprentissage est maintenant trop élevé après le plateau
- Vous utilisez `learning_rate = 1e-3`, avec une décroissance cosinus jusqu'à `min_lr = 1e-4` sur 20 000 itérations.
- À l'itération 14 000, le LR est toujours d'environ ~2,5e-4 (la décroissance cosinus est lente au début).
- Une fois que le modèle a appris tout ce que les données ont à offrir, garder le LR à des centaines de micro-unités l'empêche de se perfectionner et commence même à nuire à la généralisation → la perte de validation augmente lentement.

### 3. Inadéquation entre la taille du modèle et la diversité des données
Un modèle de 125M (ou même le 40M que vous avez initialisé) sur un seul fichier parquet, c'est comme donner à un étudiant universitaire un seul manuel scolaire et lui demander de continuer à l'étudier pendant des années. Au bout d'un moment, il peut le réciter parfaitement, mais les performances sur de nouveaux textes cessent de s'améliorer et se dégradent même légèrement en raison d'un oubli catastrophique des motifs antérieurs.

### 4. Pas assez de régularisation
- dropout = 0.1 est acceptable, mais pas suffisant lorsque le surapprentissage est aussi prononcé
- weight_decay = 0.1 est standard, mais toujours insuffisant pour 2+ époques sur de si petites données
- Pas de gradient clipping (la valeur par défaut de nanoGPT est 1.0, mais parfois on utilise 0,5 ou moins pour de petites données)

### 5. Tokens vus vs diversité réelle
Même si vous avez vu 7+ milliards de tokens, la **diversité effective** est peut-être de 1–1,5 milliard de tokens uniques de haute qualité après déduplication, suppression du texte boilerplate, des échantillons à faible score éducatif, etc. Ce n'est tout simplement pas suffisant pour qu'un modèle de 125M continue de s'améliorer au-delà d'une perte d'environ ~3,5–3,6 sur cette distribution de texte.

### Preuve tirée de votre propre journal

| Étape | Perte Val | Commentaire |
|---|---|---|
| 0 | 10.87 | Aléatoire |
| 2000 | 4.03 | Progrès rapide |
| 5000 | 3.76 | Toujours bon |
| 8000 | 3.65 | Ralentissement |
| 11000 | 3.61 | Presque plat |
| 13500 | 3.57 | **Le plus bas absolu** |
| 14500 | 3.569 | Déjà en train de remonter → signe classique de surapprentissage |

### Ce que vous devriez faire à la place pour vraiment obtenir une perte plus faible

1. Utiliser beaucoup plus de données
   - Utiliser l'échantillon complet de 100+ GB de FineWeb-edu (ou au moins 10–20 fichiers parquet)
   - Ou streamer depuis HuggingFace datasets avec plusieurs shards

2. S'entraîner pendant exactement 1 époque (ou un peu moins) sur des données diversifiées
   - ~10B–15B tokens au total est le point idéal pour un 125M sur FineWeb-edu
   - Style Llama-3/Phi-3 : 15B tokens → ~3,0–3,2 de perte de validation pour les modèles de classe 125M

3. Réduire le taux d'apprentissage final
   - Utiliser `min_lr = 5e-5` ou `3e-5` (courant dans les récentes exécutions de petits modèles)
   - Ou passer à une décroissance linéaire + une période plus longue avec un LR nul

4. Un modèle légèrement plus grand ou de meilleures astuces d'architecture
   - Le nanoGPT original est de style GPT-2 (pas d'ALiBi, ancien RoPE, etc.)
   - Les modèles modernes de 125M (Qwen2-0.5B, Phi-3-mini, Llama-3 8B réduit) atteignent ~2,8–3,0 sur les mêmes données grâce à SwiGLU, RMSNorm, rotary embeddings, etc.

### TL;DR – Pourquoi votre exécution a plafonné à ~3,57 et n'ira jamais plus bas

Vous entraînez un modèle de 40–125M pendant plusieurs époques sur un seul fichier parquet FineWeb (~quelques milliards de tokens au total). Le modèle a déjà mémorisé tout ce qui est utile vers ~13k itérations. Poursuivre l'entraînement avec un LR encore élevé ne fait que permuter les poids → plateau + légère dégradation due au surapprentissage.

C'est l'erreur numéro 1 que les gens font lorsqu'ils essaient nanoGPT sur FineWeb pour la première fois : "Je vais juste utiliser un fichier pour tester" → se retrouve exactement avec cette courbe de perte.

Solution : soit (a) utiliser 10–50 fois plus de données et s'entraîner pendant ~1 époque au total, soit (b) accepter que ~3,55–3,6 est le plancher absolu pour cette combinaison modèle+données et arrêter l'entraînement.

Si vous voulez une exécution qui atteint réellement une perte de ~3,0–3,2 avec un code de style nanoGPT, vous avez besoin au minimum de l'échantillon complet de 100 GB de FineWeb-edu (ou du nouveau FineWeb-Edu 2.0) et de vous entraîner sur ~15 milliards de tokens maximum.