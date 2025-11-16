---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Utilisation de la VRAM de la RTX 4070 Expliquée
translated: true
type: note
---

### Pourquoi ~6,5 Go d'utilisation mémoire ?
Le RTX 4070 dispose de 12 Go de VRAM (12288 Mio, affiché comme 12282 Mio probablement en raison d'arrondis/d'espace réservé). Votre processus d'entraînement utilise 6582 Mio (~6,4 Go) au total, le processus Python représentant 4464 Mio (~4,4 Go) ; la différence inclut la surcharge du contexte CUDA, les noyaux temporaires et les caches de `torch.compile` (indiqué dans le log : "compiling the model..."). C'est élevé pour un petit modèle de 30M de paramètres car **la mémoire GPU pendant l'entraînement d'un transformer est dominée par les activations (calculs intermédiaires dans les passes forward/backward), et pas seulement par les paramètres**. Les paramètres seuls n'utiliseraient qu'environ ~0,5 Go, mais les activations augmentent de manière agressive avec le `batch_size`, `block_size`, `n_embd` et `n_layer` de votre configuration. L'autograd de PyTork conserve les sorties de la passe forward en mémoire pour la rétropropagation (pas de `gradient checkpointing` dans nanoGPT par défaut), et des fonctionnalités comme AMP (précision mixte), AdamW fusionné et la compilation du modèle ajoutent de la surcharge.

Principales raisons de ce niveau d'utilisation :
- **Les activations dominent (4–5 Go ici)** : Chaque passe forward à travers les couches du transformer génère de grands tenseurs intermédiaires (par exemple, les projections requête/clé/valeur dans l'attention, les états cachés du feed-forward). La passe backward double cela en allouant des temporaires pour les gradients. L'attention a également une mémoire O(batch_size × num_heads × block_size²) pour les matrices de scores (par exemple, ~50 Mo par couche avant libération), bien que l'implémentation de nanoGPT réutilise les buffers lorsque c'est possible.
- **Aucune optimisation pour la mémoire** : nanoGPT stocke par défaut toutes les activations sans `checkpointing` (qui échange du calcul contre de la mémoire en recalculant la passe forward pendant la backward). `Torch.compile` fusionne les opérations mais peut augmenter l'allocation de pointe pendant la capture et l'exécution du graphe.
- **Surcharge de la précision mixte** : Modèle/gradients en FP16 (2 octets/paramètre), mais les états de l'optimiseur AdamW en FP32 (8 octets chacun pour momentum/variance, ~2× les paramètres). Les lots d'entrée (tokens FP16) sont petits (~16 Ko), mais pas les temporaires.
- **Facteurs d'exécution** : L'accumulation de gradients (steps=4) traite un `batch_size=16` par étape mais ne multiplie pas la mémoire (les gradients s'accumulent sur place) ; cependant, les phases d'évaluation (eval_iters=200) provoquent temporairement un pic d'utilisation. Votre log montre un entraînement stable à l'itération 1300, donc il s'agit de la ligne de base.

En bref, c'est "si élevé" par rapport à la taille du modèle parce que les petits modèles comme celui-ci subissent toujours la surcharge complète du transformer par token, et votre configuration (batch=16, block=512) traite ~8K tokens par étape—suffisamment pour remplir la VRAM de manière significative sans optimisation agressive.

### Comment estimer ~6,5 Go à partir de la configuration
Vous ne pouvez pas prédire *exactement* sans profiler (par exemple, via `torch.utils.bottleneck` ou NVIDIA Nsight), car cela dépend de la version de PyTorch, de CUDA et des détails exacts de l'implémentation. Mais vous pouvez approximer en utilisant les formules standard pour la mémoire d'entraînement des transformers. Celles-ci décomposent la VRAM en composants : paramètres/optimiseur (~10–20% du total), activations (~70–80%) et surcharge (~10%). Tous les calculs ci-dessous supposent un entraînement FP16 (dtype='float16' d'après le GradScaler du log) avec AdamW.

#### 1. **Mémoire des Paramètres (Facile à Estimer : ~0,06 Go)**
   - Formule : num_params × bytes_per_param (modèle en FP16).
   - D'après le log : 29,94M de paramètres.
   - FP16 : 29,94M × 2 octets = 59,88 Mo (~0,06 Go).
   - Comment calculer les paramètres à partir de la configuration (formule nanoGPT) : ≈ 12 × n_layer × n_embd² (blocs transformer) + n_embd × vocab_size (embedding + tête LM).
     - 12 × 6 × 384² = 12 × 6 × 147,456 ≈ 10,6M
     - 384 × 50,304 ≈ 19,3M
     - Total : ~29,9M (correspond au log ; petits extras comme les biais/LN ignorés).

#### 2. **Mémoire des Gradients + Optimiseur (~0,3–0,6 Go)**
   - Gradients : Identique aux paramètres (FP16) : encore ~0,06 Go.
   - Optimiseur (AdamW fusionné, confirmé par le log) : 2 états (momentum, variance) par paramètre décru, typiquement en FP32.
     - Paramètres décrus : 30,13M (log : 26 tenseurs, 30 130 176 paramètres).
     - Formule : decayed_params × 2 × 4 octets (FP32) = 30,13M × 8 ≈ 241 Mo.
     - Non décrus (biais/LN) : Faible, ~5K paramètres, négligeable.
   - Total cœur : params + grads + opt ≈ (2 + 8) octets/paramètre = 10 octets/paramètre × 30M ≈ 300 Mo.
     - Fourchette : 12–20 octets/paramètre si on inclut les poids maîtres FP32 ou les extras (courant en précision mixte).
   - D'après la configuration : Évolue directement avec n_layer, n_embd (plus grand = plus de paramètres). Vos petites tailles gardent ceci faible.

#### 3. **Mémoire des Activations (La plus difficile/piégeuse : ~4–5 Go)**
   - C'est la majeure partie et cela varie selon l'implémentation. C'est O(batch_size × block_size × n_embd × n_layer) pour les parties linéaires, plus O(batch_size × n_head × block_size²) pour les scores d'attention.
   - **Formule de Base** (d'après les estimateurs d'entraînement de transformers) :
     ```
     activations_bytes ≈ batch_size × block_size × n_embd × n_layer × multiplicateur × 2 (octets FP16)
     ```
     - Multiplicateur : Empirique 16–34 pour forward (buffers d'embedding + attn/FFN par couche) + backward (2–3× forward). Valeur courante : 24 (12 pour forward, 12 pour backward ; représente ~4–6 tenseurs/couche comme Q/K/V/out dans attn, up/down dans FFN avec une dimension intermédiaire de 4×).
     - Votre configuration : batch_size=16, block_size=512, n_embd=384, n_layer=6.
     - Base : 16 × 512 × 384 × 6 = 18,87M "éléments".
     - × 24 × 2 octets = 18,87M × 48 ≈ 906 Mo (sous-estimation).
   - **Pic Spécifique à l'Attention** (O(seq²), significatif à block_size=512) :
     - Par couche : batch_size × n_head × block_size² × 2 octets (pour la matrice de scores QK^T).
     - 16 × 6 × 512 × 512 × 2 ≈ 50,3 Mo/couche.
     - × n_layer=6, mais séquentiel (pas tous en même temps) : ~50–100 Mo de pointe par couche pendant forward, plus les temporaires backward. Total ajoute ~0,3–0,5 Go à travers les passes.
   - **Total Empirique Ajusté pour Votre Configuration** : La formule de base sous-estime d'un facteur 4–5× en raison des temporaires PyTorch (par exemple, buffers GEMM dans FFN/attn, pas de libération avant la fin du backward) et des couches basées sur des boucles de nanoGPT stockant toutes les sorties forward (~ L × 4–6 × batch × seq × embd octets). Monde réel : ~ batch_size × block_size × n_embd × n_layer × 160 × 2 octets ≈ 18,87M × 320 ≈ 6 Go (ajusté pour correspondre à votre total de 6,5 Go ; correspond aux rapports similaires pour les petits GPT).
     - Pourquoi 160 ? Inclut le backward complet (sans checkpointing), l'intermédiaire FFN (4× n_embd), les caches de résiduels/LN et ~20–30% de surcharge PyTorch par tenseur.
   - D'après la configuration : Évolue linéairement avec batch_size/block_size (débit de tokens), quadratiquement avec block_size (attn), et avec n_embd/n_layer (profondeur/largeur). Vos valeurs sont modérées mais se combinent : par exemple, diviser le batch_size par 2 (à 8) réduirait les activations d'environ ~50%, économisant ~2–3 Go.

#### 4. **Surcharge et Divers (~1 Go)**
   - CUDA/PyTorch : Contexte (~500 Mo), lancements de noyaux, fragmentation de l'allocateur.
   - Torch.compile : Captures de graphe + opérations fusionnées ajoutent 0,5–1 Go (le log montre la compilation ; peut être profilé avec `torch._dynamo.config`).
   - Données : Tokens du batch (négligeable), mais si l'évaluation est en cours, eval_iters=200 ajoute des batches temporaires.
   - Total : Cœur (0,4 Go) + activations (4,5 Go) + surcharge (1,5 Go) ≈ 6,4 Go.

#### Validation par rapport à des configurations similaires
- NanoGPT/GPT-2 small (124M paramètres, embd=768=2× le vôtre, layers=12=2×, batch~8–16, seq=1024=2×) utilise typiquement 6–10 Go en entraînement FP16. Votre modèle a ~1/4 des paramètres mais un volume de tokens similaire (16×512 vs. 16×1024 /2 pour la mise à l'échelle), donc environ la moitié serait 3–5 Go de base—votre supplément provient de l'absence de checkpointing et de la compilation.
- Outils pour une meilleure prédiction :
  - Exécutez `python -m torch.utils.bottleneck` pendant l'entraînement pour une répartition détaillée.
  - Utilisez `estimate_memory()` de Hugging Face ou des bibliothèques comme `modelscope` pour les estimateurs LLM (adapter pour nanoGPT).
  - Calculateurs en ligne (par exemple, à partir des résultats de recherche) entrant vos paramètres/batch/seq pour une estimation de ~5–7 Go.

Pour réduire à <4 Go : Définissez batch_size=8 (ou utilisez gradient_accumulation_steps=8 pour un batch effectif=64), block_size=256, ou ajoutez du gradient checkpointing (modifiez `model.forward` pour utiliser `torch.utils.checkpoint`). Votre configuration tient confortablement dans 12 Go, mais surveillez avec `nvidia-smi -l 1` pour les pics.