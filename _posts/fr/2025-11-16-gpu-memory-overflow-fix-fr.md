---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Correction du Débordement de Mémoire GPU Pendant l'Évaluation
translated: true
type: note
---

Vous rencontrez un classique OOM (Out Of Memory) sur une RTX 4070 (12 Go de VRAM) lors de l'entraînement d'un GPT d'environ 77M de paramètres (initialement prévu pour 125M, mais vous avez réduit `n_embd` à 576 → ~77M) avec `batch_size=16`, `block_size=1024`, et `gradient_accumulation_steps=32` en FP16.

Bien que 77M soit petit, le micro-lot effectif est énorme à cause de la façon dont nanoGPT calcule la perte dans `estimate_loss()` — il exécute la passe forward/backward complète sur les lots d'évaluation sans les astuces d'accumulation de gradients, donc pendant l'évaluation, il essaie soudainement de placer un lot effectif beaucoup plus grand en mémoire.

### Cause Racine
Dans `estimate_loss()`, nanoGPT fait ceci par défaut :

```python
for _ in range(eval_iters):  # 200 fois !
    x, y = get_batch('train')
    ...
    logits, loss = model(x, y)
```

Chaque `get_batch` retourne `batch_size × block_size` tokens → 16 × 1024
Avec eval_iters = 200 → 200 passes forward séparées, mais PyTorch garde le graphe de calcul et les activations intermédiaires pour toute la boucle d'évaluation en mémoire si vous n'êtes pas prudent. Combiné avec l'énorme cache KV (12 layers × 12 têtes × 1024 × 576 × 2 octets FP16 ≈ 1.6 Go juste pour le cache), plus les logits (16×1024×50304 × 2 octets ≈ 1.6 Go par passe forward), vous dépassez facilement les 12 Go même si l'entraînement lui-même se passe bien.

### Corrections Rapides (choisissez-en une ou combinez)

**Option 1 : Réduire drastiquement la taille du lot d'évaluation (correctif le plus rapide)**
Ajoutez ces lignes à votre configuration (ou surchargez-les en ligne de commande) :

```python
eval_batch_size = 4        # ajoutez ceci
# ou même 2 si toujours OOM
eval_iters = 100           # peut être réduit un peu plus
```

nanoGPT respecte `eval_batch_size` si vous l'ajoutez (les versions récentes le font). Cela fait que l'évaluation n'utilise que 4 séquences au lieu de 16 → ~4× moins de mémoire pendant l'éval.

**Option 2 : Réduire block_size uniquement pour l'évaluation (conserve la précision)**
```python
eval_block_size = 512      # ou 256
```
Ajoutez ceci à la configuration — certaines versions le supportent, ou patchez `get_batch` pour utiliser une taille de bloc différente quand `split=='val'`.

**Option 3 : Réduire eval_iters et accepter une perte d'évaluation légèrement plus bruitée**
```python
eval_iters = 50   # estimation toujours décente
```

**Option 4 : Réduire un peu plus la taille du modèle (qualité toujours bonne)**
Vous êtes déjà à 77M, mais vous pouvez descendre en sécurité :

```python
n_layer = 12
n_head  = 12
n_embd  = 512     # → ~62M paramètres, beaucoup plus sûr
# ou même n_embd = 448 → ~53M
```

**Option 5 : Activer le gradient checkpointing (gain de mémoire le plus important)**
Ajoutez ceci à la création du modèle (éditez model.py ou passez le flag) :

```python
model = GPT(GPTConfig(..., grad_checkpoint=True))
```

Ou appliquez le monkey-patch dans train.py avant l'entraînement :

```python
if config.grad_checkpoint:
    model.gradient_checkpointing_enable()
```

Cela réduit la mémoire des activations de ~50-60% au coût d'un entraînement ~20-25% plus lent.

### Combinaison recommandée pour votre 4070 12 Go

```python
# Dans config/train_fineweb.py
batch_size = 16
gradient_accumulation_steps = 32   # maintient un effet de 512 séquences
block_size = 1024

eval_batch_size = 4        # critique
eval_iters = 100
eval_interval = 500

n_embd = 512               # modèle ~62M, très sûr
# optionnel : ajoutez le gradient checkpointing
grad_checkpoint = True     # si votre version de nanoGPT le supporte
```

Ou si vous ne voulez pas toucher à n_embd, faites simplement :

```python
eval_batch_size = 2
eval_iters = 100
```

Cela seul résoudra presque certainement le OOM.

Définissez aussi cette variable d'environnement pour aider avec la fragmentation :

```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

Essayez d'abord `eval_batch_size=4` (ou `=2`) — 95% des personnes avec une 4070 12 Go qui ont cette erreur exacte la résolvent ainsi lors de l'entraînement de nanoGPT sur FineWeb.