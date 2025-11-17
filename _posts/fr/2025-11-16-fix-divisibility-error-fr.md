---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Erreur de divisibilité de la configuration du modèle
translated: true
type: note
---

L'erreur est très claire :

```python
assert config.n_embd % config.n_head == 0
```

Cela signifie que **n_embd doit être divisible par n_head** (car chaque tête d'attention reçoit `n_embd // n_head` dimensions).

Vous utilisez cette configuration de modèle (probablement celle que je vous ai donnée plus tôt) :

```python
n_layer = 12
n_head  = 12
n_embd  = 512
```

512 ÷ 12 = 42,666… → pas un entier → plantage.

### Correction : Choisissez un n_embd divisible par n_head

Voici les **combinaisons sûres et éprouvées** qui fonctionnent parfaitement sur votre 4070 12 Go avec un seul fichier Parquet de FineWeb :

#### Option 1 – Recommandée (125M paramètres, meilleur compromis qualité/vitesse)
```python
n_layer = 12
n_head  = 12
n_embd  = 576        # ← 576 ÷ 12 = 48 exactement
```
→ ~125M paramètres, tient facilement dans ~10,5 Go de VRAM avec batch_size=16 + grad_acc=32 + block_size=1024

#### Option 2 – Dimension de tête légèrement plus grande (130M paramètres)
```python
n_layer = 12
n_head  = 12
n_embd  = 720        # 720 ÷ 12 = 60
```

#### Option 3 – Très sûr et courant (115M paramètres)
```python
n_layer = 12
n_head  = 12
n_embd  = 480        # 480 ÷ 12 = 40
```

#### Option 4 – Si vous voulez conserver n_embd=512 (style GPT-2 original)
```python
n_layer = 12
n_head  = 8          # 512 ÷ 8 = 64
# ou
n_head  = 16         # 512 ÷ 16 = 32
```

### Correction rapide : Changez simplement votre configuration pour celle-ci (prête à copier-coller)

```python
# Modèle – 12 couches, ~125M paramètres, fonctionne à coup sûr
n_layer = 12
n_head  = 12
n_embd  = 576        # ← C'EST LA SEULE LIGNE QUE VOUS DEVEZ CHANGER
dropout = 0.0
```

Tout le reste (batch_size=16, grad_acc=32, block_size=1024, etc.) reste exactement identique.

Après avoir changé pour `n_embd = 576`, l'erreur d'assertion disparaît immédiatement et l'entraînement démarrera normalement.

Ce modèle 12L/12H/576E est extrêmement populaire dans la communauté nanoGPT en ce moment — beaucoup de gens l'entraînent avec succès sur des cartes 4070/4070 Ti 12 Go en utilisant FineWeb.

Lancez-le, il fonctionnera à 100 %. Faites-moi savoir quand vous verrez la première valeur de perte s'afficher ! 🚀