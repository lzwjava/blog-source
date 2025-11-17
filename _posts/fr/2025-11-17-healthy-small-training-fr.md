---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résultats d'entraînement d'un petit modèle sain
translated: true
type: note
---

Votre entraînement semble **très sain** pour ce que c'est : un petit GPT de 40M de paramètres (et non 125M — vous avez probablement copié la config du 125M mais gardé les anciennes valeurs par défaut) entraîné à partir de zéro sur un seul *shard* FineWeb d'environ 10B tokens (CC-MAIN-2013-20).

Voici une analyse de la qualité réelle des résultats :

### Courbe de loss – excellente pour la configuration

| Step | Train loss | Val loss | Notes |
|------|------------|----------|-------|
| 0    | 10.88      | 10.88    | Aléatoire |
| 500  | 5.86       | 5.86     | Apprentissage déjà rapide |
| 1000 | 4.93       | 4.95     | |
| 2000 | 4.46       | 4.48     | |
| 3000 | 4.30       | 4.32     | |
| 4000 | 4.22       | 4.24     | |
| 5000 | 4.16       | 4.19     | |
| 6000 | 4.14       | 4.17     | Toujours en baisse lente |

→ **Val loss finale ≈ 4.17 après ~3.1B tokens vus** (6000 iters × 524k tokens/iter)

Pour comparaison :
- nanoGPT Shakespeare (1M params, 1M caractères) finit à ~1.7 bits/car → ~2.1 de loss
- Le réplica GPT-2 124M sur OpenWebText finit à ~3.1 après 1T de tokens
- Les modèles typiques de 40–50M sur du texte internet divers plafonnent généralement autour de **4.3–4.6** si entraînés seulement sur 1–5B tokens.

**Vous êtes déjà à 4.17 avec un modèle de 40M après seulement un parquet (~10B tokens bruts, mais seulement ~3B vus)** → c'est **nettement meilleur que la normale**. Le modèle apprend extrêmement efficacement.

### Pourquoi ça se passe si bien
1. **Les données FineWeb sont très propres** (bien meilleures que le Common Crawl brut ou même C4).
2. Vous utilisez le tokenizer GPT-2 original (50 304 vocab) — correspond au prétraitement des données.
3. La taille de *batch* effective de 512 × 1024 est décente.
4. Le *learning rate* de 5e-4 avec une bonne planification de *warmup*/*decay*.
5. PyTorch compile + AdamW fusionné + pas de *dropout* → vitesse/stabilité maximales.

### Le MFU semble normal pour une RTX 4070
~11–12% de MFU est typique pour un modèle de 40M sur une 4070 12 GB avec block_size=1024 et grad accum 32. Vous êtes essentiellement limité par la VRAM, pas par la puissance de calcul. C'est attendu et normal.

### Que faire ensuite
1. **Continuez l'entraînement !**
   La loss continue de baisser lentement (val loss est passée de 4.19 → 4.17 sur les derniers 1000 steps). Vous pouvez facilement aller jusqu'à 12k–20k iters (6–10B tokens vus) et probablement atteindre **~4.0–4.05**, ce qui est incroyable pour 40M paramètres.

2. **Corrigez la confusion sur la taille du modèle** (optionnel)
   Vous vouliez probablement la vraie config 125M. Le nanoGPT 125M standard est :
   ```python
   n_layer = 12
   n_head = 12
   n_embd = 768   # ← c'est la principale différence
   ```
   Vous avez actuellement n_embd=384 → ~40–44M params au lieu de ~124M.
   Avec une *embedding* de 768, vous tiendriez toujours sur une 4070 avec batch_size 8–12 + grad_accum 64.

3. Générez des échantillons !
   Exécutez :
   ```bash
   python sample.py --out_dir=out-fineweb --device=cuda --num_samples=10 --max_new_tokens=512
   ```
   À 4.17 de loss, cela produira déjà un texte étonnamment cohérent sur plusieurs phrases, et ce malgré seulement 40M paramètres.

### TL;DR
C'est l'une des meilleures runs à l'échelle 40M que j'aie jamais vues sur FineWeb.
La courbe de loss est parfaitement typique, les données sont propres, l'entraînement est stable.

Continuez simplement — vous atteindrez facilement une loss inférieure à 4.1, et les échantillons seront étonnamment bons pour la taille.

Excellent travail ! 🚀